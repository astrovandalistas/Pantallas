# -*- coding: utf-8 -*-

import sys, time, subprocess, getopt
sys.path.append("../LocalNet")
from interfaces import PrototypeInterface, runPrototype
from OSC import OSCClient, OSCMessage, OSCServer, getUrlStr, OSCClientError
from random import random, shuffle

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
            if(self.subscribedToAll and not self.subscribedReceivers):
                self.subscribeToAll()
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
                #self.oscClient.connect((ip, port))
                self.oscClient.sendto(msg, (ip, port))
                #self.oscClient.connect((ip, port))
            except OSCClientError:
                print "no connection to %s:%s, can't send list of receivers"%(ip,port)
        ## actual message from AEffect Network !!
        elif (addrTokens[0].lower() == "aeffectlab"):
            self.messageQ.put((addrTokens[1],
                               addrTokens[2],
                               stuff[0].decode('utf-8')))
        ## ping
        if ((addrTokens[0].lower() == "localnet")
            and (addrTokens[1].lower() == "ping")):
            self.lastPingTime = time.time()
            # forward to clients
            for (ip,port) in self.allClients.keys():
                try:
                    #self.oscClient.connect((ip, int(port)))
                    self.oscClient.sendto(self.oscPingMessage, (ip, int(port)))
                    #self.oscClient.connect((ip, int(port)))
                except OSCClientError:
                    print ("no connection to %s:%s, can't send bang"%(ip,port))

    def setup(self):
        self.allClients = {}
        self.oscClient = OSCClient()
        ## subscribe to all receivers from localnet
        self.subscribeToAll()
        self.oldMessages = []
        self.lastQueueCheck = time.time()
        self.oscPingMessage = OSCMessage()
        self.oscPingMessage.setAddress("/LocalNet/Ping")
        ## use empty byte blob
        self.oscPingMessage.append("", 'b')


    def _oneWordToEach(self, locale,type,txt):
        clientIndex = 0
        words = txt.split()
        for w in words:
            msg = OSCMessage()
            msg.setAddress("/AeffectLab/"+locale+"/"+type)
            msg.append(w.encode('utf-8'), 'b')
            (ip,port) = self.allClients.keys()[clientIndex]

            try:
                #self.oscClient.connect((ip, int(port)))
                self.oscClient.sendto(msg, (ip, int(port)))
                #self.oscClient.connect((ip, int(port)))
            except OSCClientError:
                print "no connection to %s:%s, can't send message "%(ip,port)
                #del self.allClients[(ip,port)]
            
            if (self.allClients):
                clientIndex = (clientIndex+1)%len(self.allClients.keys())

    def _oneMessageToEach(self, locale,type,txt):
        clientKeys = self.allClients.keys()
        ## get a random client to push the new message
        shuffle(clientKeys,random)
        self.oldMessages.append(txt)
        probability = 1.1
        for (ip,port) in clientKeys:
            if(random() < probability):
                msg = OSCMessage()
                msg.setAddress("/AeffectLab/"+locale+"/"+type)
                msg.append(self.oldMessages[-1].encode('utf-8'),'b')
                try:
                    #self.oscClient.connect((ip, int(port)))
                    self.oscClient.sendto(msg, (ip, int(port)))
                    #self.oscClient.connect((ip, int(port)))
                except OSCClientError:
                    print "no connection to %s:%s, can't send message "%(ip,port)
                    #del self.allClients[(ip,port)]

                probability = 0.66
                shuffle(self.oldMessages)
        if(len(self.oldMessages) > 10):
            self.oldMessages.pop()

    def loop(self):
        ## check Queue, split stuff and send to clients
        if ((not self.messageQ.empty()) and 
            (time.time()-self.lastQueueCheck > 10) and
            (self.allClients)):
            (locale,type,txt) = self.messageQ.get()

            if(random() < 0.66):
                self._oneMessageToEach(locale,type,txt)
            else:
                self._oneWordToEach(locale,type,txt)
            self.lastQueueCheck = time.time()

if __name__=="__main__":
    (inIp, inPort, localNetAddress, localNetPort) = ("127.0.0.1", 8989, "127.0.0.1", 8900)
    opts, args = getopt.getopt(sys.argv[1:],"i:p:n:o:",["inip=", "inport=","localnet=","localnetport="])
    for opt, arg in opts:
        if(opt in ("--inip","-i")):
            inIp = str(arg)
        elif(opt in ("--inport","-p")):
            inPort = int(arg)
        elif(opt in ("--localnet","-n")):
            localNetAddress = str(arg)
        elif(opt in ("--localnetport","-o")):
            localNetPort = int(arg)

    mVLE = PantallaServer(inIp, inPort, localNetAddress, localNetPort)
    runPrototype(mVLE)
