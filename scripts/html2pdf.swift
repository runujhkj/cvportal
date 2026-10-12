// Print an HTML file to a paginated US Letter PDF with the system WebKit.
// usage: swift scripts/html2pdf.swift IN.html OUT.pdf [vertical-margin-in] [horizontal-margin-in]
//
// WebKit prints at 72 CSS px per inch where browsers use 96, and also lays the
// page out 1.25x wider than the printable area and shrinks it by 0.8. To match a
// browser's print layout, the page is printed on slightly larger paper
// (0.75 * 1.25 = 0.9375) and each page is redrawn, as vectors, scaled onto Letter.
import AppKit
import WebKit

let args = CommandLine.arguments
guard args.count >= 3 else { fputs("usage: html2pdf IN.html OUT.pdf [vmargin-in] [hmargin-in]\n", stderr); exit(2) }
let input = URL(fileURLWithPath: args[1]), output = URL(fileURLWithPath: args[2])
let vMargin = CGFloat(Double(args.count > 3 ? args[3] : "0.45") ?? 0.45) * 72
let hMargin = CGFloat(Double(args.count > 4 ? args[4] : "0.6") ?? 0.6) * 72
let letter = CGSize(width: 612, height: 792)
let scale: CGFloat = 0.9375
let big = NSSize(width: letter.width / scale, height: letter.height / scale)
let oversized = FileManager.default.temporaryDirectory.appendingPathComponent("html2pdf-\(ProcessInfo.processInfo.processIdentifier).pdf")

func scaleToLetter() -> Bool {
    guard let source = CGPDFDocument(oversized as CFURL) else { return false }
    var box = CGRect(origin: .zero, size: letter)
    guard let ctx = CGContext(output as CFURL, mediaBox: &box, nil) else { return false }
    for n in 1...max(source.numberOfPages, 1) {
        guard let page = source.page(at: n) else { continue }
        ctx.beginPDFPage(nil)
        ctx.scaleBy(x: scale, y: scale)
        ctx.drawPDFPage(page)
        ctx.endPDFPage()
    }
    ctx.closePDF()
    try? FileManager.default.removeItem(at: oversized)
    return true
}

final class Printer: NSObject, WKNavigationDelegate {
    let frame = NSRect(origin: .zero, size: big)
    lazy var window = NSWindow(contentRect: frame, styleMask: [.borderless], backing: .buffered, defer: false)
    lazy var web = WKWebView(frame: frame)

    func start() {
        window.contentView = web
        web.navigationDelegate = self
        web.loadFileURL(input, allowingReadAccessTo: input.deletingLastPathComponent())
    }

    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        let info = NSPrintInfo()
        info.paperSize = big
        info.topMargin = vMargin / scale; info.bottomMargin = vMargin / scale
        info.leftMargin = hMargin / scale; info.rightMargin = hMargin / scale
        info.horizontalPagination = .automatic
        info.verticalPagination = .automatic
        info.jobDisposition = .save
        info.dictionary()[NSPrintInfo.AttributeKey.jobSavingURL] = oversized
        let op = webView.printOperation(with: info)
        op.showsPrintPanel = false
        op.showsProgressPanel = false
        op.view?.frame = frame
        op.runModal(for: window, delegate: self, didRun: #selector(done(_:success:contextInfo:)), contextInfo: nil)
    }

    func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) {
        fputs("load failed: \(error.localizedDescription)\n", stderr); exit(1)
    }

    @objc func done(_ op: NSPrintOperation, success: Bool, contextInfo: UnsafeMutableRawPointer?) {
        exit(success && scaleToLetter() ? 0 : 1)
    }
}

let app = NSApplication.shared
app.setActivationPolicy(.accessory)
let printer = Printer()
printer.start()
DispatchQueue.main.asyncAfter(deadline: .now() + 60) { fputs("timed out\n", stderr); exit(1) }
app.run()
