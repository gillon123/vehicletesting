import sys
import getopt
import coapy.connection
import coapy.options
import coapy.link
import socket

msg = coapy.connection.Message(code=coapy.GET, uri_path="ASDF")
ep = coapy.connection.EndPoint(address_family=socket.AF_INET)
ep.send(msg, ("mulle.csproject.org", 61616))

ep.process(0)
