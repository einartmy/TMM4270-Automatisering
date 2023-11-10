from http.server import BaseHTTPRequestHandler, HTTPServer
import time

HOST_NAME = '127.0.0.1' 
PORT_NUMBER = 1234 # Maybe set this to 1234
#file path of this python file
filePath = 'M:\\KBE\\TMM4270-Automatisering\\A3\\DFAs' #The folder you put dfas into

# Handler of HTTP requests / responses
class MyHandler(BaseHTTPRequestHandler):
	def do_HEAD(s):
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
	
	def do_GET(s):
		"""Respond to a GET request."""
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		
		# Check what is the path
		path = s.path
		if path.find("/") != -1 and len(path) == 1:
			s.wfile.write(bytes('<html><head><title>Cool interface.</title></head>', 'utf-8'))
			s.wfile.write(bytes("<body><p>Current path: " + path + "</p>", "utf-8"))
			s.wfile.write(bytes('</body></html>', "utf-8"))
		elif path.find("/info") != -1:
			s.wfile.write(bytes('<html><head><title>Cool interface.</title></head>', 'utf-8'))
			s.wfile.write(bytes("<body><p>Current path: " + path + "</p>", "utf-8"))
			s.wfile.write(bytes("<body><p>Let's change the side of the cube</p>", "utf-8"))
			s.wfile.write(bytes('</body></html>', "utf-8"))
		elif path.find("/setSide") != -1:
			s.wfile.write(bytes('<html><body><h2>Block</h2>', 'utf-8'))
			s.wfile.write(bytes('<form action="/setSide" method="post">', 'utf-8'))
			s.wfile.write(bytes('<label for="slength">Set Side:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="slength" name="slength" value="100"><br><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="submit" value="Submit">', 'utf-8'))
			s.wfile.write(bytes('</form></body></html>', 'utf-8'))
		else:
			s.wfile.write(bytes('<html><head><title>Cool interface.</title></head>', 'utf-8'))
			s.wfile.write(bytes("<body><p>The path: " + path + "</p>", "utf-8"))
			s.wfile.write(bytes('</body></html>', "utf-8"))
			
	def do_POST(s):

		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		
		# Check what is the path
		path = s.path
		print("Path: ", path)
		if path.find("/setSide") != -1:
			content_len = int(s.headers.get('Content-Length'))
			post_body = s.rfile.read(content_len)
			param_line = post_body.decode()
			print("Body: ", param_line)
			
			#Get the param value
			pair = param_line.split("=")
			
			#Open the template file
			f = open(filePath + "\\templates\\Colored_Block_2023_DYN.dfa", "r")
			txt = f.read()

			
			s.wfile.write(bytes('<html><body><h2>Block</h2>', 'utf-8'))
			s.wfile.write(bytes('<form action="/setSide" method="post">', 'utf-8'))
			s.wfile.write(bytes('<label for="slength">Set Side:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="slength" name="slength" value="' + pair[1] +'"><br><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="submit" value="Submit">', 'utf-8'))
			
			s.wfile.write(bytes('<p>The value of the side was set to ' + pair[1] + '</p>', 'utf-8'))
			
			s.wfile.write(bytes('</form></body></html>', 'utf-8'))
			
			# Replacing and writing the file to correct location
			txt = txt.replace("<SIDE>", pair[1])

			#Writing to the correct location
			f = open(filePath + "\\Colored_Block2023_DYN.dfa", "w")
			f.write(txt)
			f.close()


			
			
 
if __name__ == '__main__':
	server_class = HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
	print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
	
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
	print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))
