from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
  <body>
    <h1 allign="centre"> Device Specifications</h1>
    <h2 allign ="right">(Indhumathi) </h2>
    <h3 allign="right">(24900500)</h3>
    <ol type="i">
        <li> Device Name-DESKTOP-MOHHBTU</li>
        <li> Processor-13 th Gen Intel core</li>
        <li> Installed RAM - 16.0 RAM</li>
        <li> Device ID-15 EEA3B2-7 EF5-4 DEC-903 D-577382 C3C005</li>
        <li> Product ID- 00 342-42708-95369-AAOEM</li>
        <li> System tyope- 64-bit operating system, x64-based processor</li>
        <li> Pen and Touch-No pen or touch input is available for this display </li>
    </ol>
  </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()