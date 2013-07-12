# -*- coding: utf-8 -*-

import sys, time, subprocess
sys.path.append("../LocalNet")
from interfaces import PrototypeInterface, runPrototype
from OSC import OSCClient, OSCMessage, OSCServer, getUrlStr, OSCClientError

class PantallaServer(PrototypeInterface):
    """ Pantalla prototype class
        all prototypes must define setup() and loop() functions
        self.messageQ will have all messages coming in from LocalNet """

    ## overide the osc handler
    def _oscHandler(self, addr, tags, stuff, source):
        addrTokens = addr.lstrip('/').split('/')
        ## list of all receivers
        if ((addrTokens[0].lower() == "localnet")
              and (addrTokens[1].lower() == "receivers")):
            for rcvr in stuff[0].split(','):
                self.allReceivers[rcvr] = rcvr
        ## hijack /LocalNet/Add !
        elif ((addrTokens[0].lower() == "localnet")
            and (addrTokens[1].lower() == "add")):
            ip = getUrlStr(source).split(":")[0]
            port = int(stuff[0])
            print "adding %s:%s to PantallaServer" % (ip, port)
            self.allClients[(ip,port)] = addrTokens[2]
        ## hijack a /LocalNet/ListReceivers
        elif ((addrTokens[0].lower() == "localnet")
              and (addrTokens[1].lower().startswith("listreceiver"))):
            ip = getUrlStr(source).split(":")[0]
            port = int(stuff[0])
            ## send list of receivers to client
            msg = OSCMessage()
            msg.setAddress("/LocalNet/Receivers")
            msg.append(self.name)
            try:
                self.oscClient.connect((ip, port))
                self.oscClient.sendto(msg, (ip, port))
                self.oscClient.connect((ip, port))
            except OSCClientError:
                print "no connection to %s:%s, can't send list of receivers"%(ip,port)
        ## actual message from AEffect Network !!
        elif (addrTokens[0].lower() == "aeffectlab"):
            self.messageQ.put((addrTokens[1],
                               addrTokens[2],
                               stuff[0].decode('utf-8')))

    def setup(self):
        self.allClients = {}
        self.oscClient = OSCClient()
        ## subscribe to all receivers from localnet
        self.subscribeToAll()

    def loop(self):
        ## check Queue, split stuff and send to clients
        if (not self.messageQ.empty()):
            (locale,type,txt) = self.messageQ.get()
            clientIndex = 0
            words = txt.split()
            for w in words:
                msg = OSCMessage()
                msg.setAddress("/AeffectLab/"+locale+"/"+type)
                msg.append(w)
                (ip,port) = self.allClients.keys()[clientIndex]

                try:
                    self.oscClient.connect((ip, int(port)))
                    self.oscClient.sendto(msg, (ip, int(port)))
                    self.oscClient.connect((ip, int(port)))
                except OSCClientError:
                    print "no connection to %s:%s, can't send message "%(ip,port)

                clientIndex = (clientIndex+1)%len(self.allClients.keys())

if __name__=="__main__":
    ## TODO: get ip and ports from command line
    mAST = PantallaServer(7777,"127.0.0.1",8888)
    runPrototype(mAST)
