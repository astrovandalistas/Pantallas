en pseudocódigo:

`
class Canvas:
	x = 0
	y = 0
	segments = []

	def appendSegment( self, width, height ) :

class CanvasMessage:
	"a message to be drawn on a canvas"
	
	done = true
	playhead = 0
	steps = 0
	message = "..."
	x = 0
	y = 0
	fontSize = 0
	stepX = 0
	stepY = 0

	def __init( self, message ) :
		self.message = message
		return

	def setSteps( self, numSteps ) :
		self.steps = numSteps
		return

	def fontSize( self, fontSize ) :
		self.fontSize = fontSize
		return


	def animate( startX, startY, endX, endY, numSteps ) :
		self.stepX = ( endX - startX ) / numSteps
		self.stepY = ( endY - startY ) / numSteps
		self.steps = 
		done = false
		return

	def fwd( self ) :
		if( self.playhead == self.steps)
			done = true			
		else 
			self.x = self.x + stepX
			self.y = self.y + stepY
			self.playhead = self.playhead + 1
		return




def getListeners() :
		# lo optimo sería implementar un método para "descubrir"
		# nodos esclavos

	# por ahora hardcode:

	listeners = [ "direccion/de/esclava1", "direccion/de/esclava2"]

	return [ listeners ]


def getOSCmessages() :
	# revisar si s ehan recibido msjs de una pantalla master
	messages = osc...
	return messages

def getMessages() :

	messages = []

	if isMaster :
		# revisar twitter, http, sms, etc. 

		twitterMssgs = twitter.getMessages()
		httpMssgs = http.getMessages()
		smsMssgs = sms.getMessages()
		
		for message in twitterMssgs :
			messages.append( CanvasMessage( message ) )
		for message in httpMssgs :
			messages.append( CanvasMessage( message ) )
		for message in smsMssgs :
			messages.append( CanvasMessage( message ) )

	else :
		# revisar si la pantalla maestra ha enviado mensajes nuevos
		oscMssgs = getOSCmessages()


	return [messages]



# canvasMessages = []



def animate() :

	messages = getMessages()

	if messages :
		# avanzar animacion de todos los mensajes un "paso"
			if ! message.done
				message.fwd()		
			else 
				del message ???
				# delete message from messages

	return



def draw() :

	return



def main() :

	listeners = getListeners()


	# loop
	while(True) :

	    messages = getMessages()

		if messages:
			if isMaster:

				animate

				for  message in messages :
					# enviar mensajes OSC a pantallas esclavas con el formato
					# ( "direccion/a/pantallaN", x, y, fontsize )

					direccion = "direccion/a/pantallaN"

					sendOSC ( direccion, message.x, message.y, message.fontsize )

			else:
				# dibujar aqui el mensaje OSC ( "direccion/a/pantallaN", x, y, fontsize )


`
