#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import sys
import Adafruit_DHT

html_style = "<style>* {margin:0;padding:0} body {font-family:'Open Sans', sans-serif; font-size:2em; color:#fff; background-color:#224;} article, aside {width:16em; padding:1em 3em; margin:2em auto;} article {border:0.3em solid #789; background:#234;} ul {font-size:0.5em;}</style>"
html_start = "<html><head><title>P1X IoT</title>"+html_style+"</head><body>"
html_end = "</body></html>"
html_form = "<form action = \"\\\" method = \"post\"><input type = \"submit\" value = \"Read sensor.. (this takes 8 seconds)\" /></form>"
html_sensor_start = "<article><h1>DHT11 Pi Sensor</h1>"
html_sensor_end = "</article>"
html_log_start = "<aside><ul>Historical data:"
html_log_end = "</ul></aside>"

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(html_start)
        self.wfile.write(html_sensor_start + html_form + html_sensor_end)
        self.show_LOG()
        self.wfile.write(html_end)

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        self._set_headers()
        self.wfile.write(html_start)
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        reads = "<p>" + 'Temp: {0:0.1f} C,  Humidity: {1:0.1f} %\n'.format(temperature, humidity) + "</p><hr/><br/>"
        self.wfile.write(html_sensor_start + reads + html_sensor_end)
        self.show_LOG()
        self.wfile.write(html_end)

    def show_LOG(self):
        logfile = open('readouts.log', 'r')
        self.wfile.write(html_log_start)
        for log_line in logfile:
            self.wfile.write("<li>" + log_line + "</li>")
        self.wfile.write(html_log_end)

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting IoT server...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
