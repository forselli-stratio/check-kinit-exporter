#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 0.5

import http.server
import socketserver
import subprocess

kdestroy='kdestroy'.split(" ")
kinit='kinit -kt zkuserland-backup@STRATIO.COM.keytab zkuserland-backup@STRATIO.COM'.split(" ")
klist='klist -s'.split(" ")
PORT=9118

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/metrics":
            #This URL will trigger our sample function and send what it returns back to the browser
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()

            def kdestroy_func():
                        subprocess.run(kdestroy, stdout=subprocess.PIPE)
            
            def kinit_func():
                        subprocess.run(kinit, stdout=subprocess.PIPE)
            
            def has_kerberos_ticket():
                return True if subprocess.call(klist) == 0 else False
            
            kdestroy_func()
            kinit_func()
            has_kerberos_ticket()
            

            if has_kerberos_ticket():
                output='kerberos_kinit_status 1\n'
                self.wfile.write(output.encode())
            else:
                output='kerberos_kinit_status 0\n'
                self.wfile.write(output.encode())
            return
socketserver.TCPServer.allow_reuse_address = True
#with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    #print("serving at port", PORT)
    #httpd.serve_forever()

httpd = socketserver.TCPServer(("", PORT), CustomHandler)
print("serving at port", PORT)
httpd.serve_forever()