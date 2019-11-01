#import requests
#response = requests.get('http://aosabook.org/en/500L/web-server/testpage.html')
#print('status code:'+' '+str(response.status_code))
#print('content length:'+' '+response.headers['content-length'])
#print(response.text)
import http.server
class RequestHandler(http.server.BaseHTTPRequestHandler):
    '''Handle HTTP requests by return a fixed page'''
    #page to send back
    Page='''\
<html>
<body>
<p>Hello world</p>
</body>
</html>
'''
    Page1=bytes(Page, encoding = "ASCII")
    #Handle a GET request.
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type','text/html')
        self.send_header('Content-Length',str(len(self.Page)))
        self.wfile.write(self.Page1)

#------------------------------------------------------------------


if __name__ == '__main__':
    serverAddress =('', 8080)
    server = http.server.HTTPServer(serverAddress,RequestHandler)
    server.serve_forever()

