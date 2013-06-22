en pseudocódigo:

`
class Canvas:
	x = 0
	y = 0
	segments = []

class CanvasMessage:
	"a message to be drawn on a canvas"
	
	done = true
	playhead = 0
	steps = 0

	def __init( self, message ) :
		self.message = message

	def setSteps( numSteps ) :
		self.steps = numSteps

	def fwd() :
		playhead++
		if( playhead == steps)



def getListeners() :
	# lo optimo sería implementar un método para "descubrir"
	# nodos esclavos

	# por ahora hardcode:

	listeners = [ "direccion/de/esclava1", "direccion/de/esclava2"]

	return [ listeners ]


def getMessages() :

	messages = []

	if isMaster :
		# revisar twitter, http, sms, etc. 

		twitterMssgs = twitter.getMessages()
		httpMssgs = http.getMessages()
		smsMssgs = sms.getMessages()
		
		for message in twitterMssgs :
			messages.add( ( CanvasMessage( message )   )
		for message in httpMssgs :
			messages.add( ( CanvasMessage( message )   )
		for message in smsMssgs :
			messages.add( ( CanvasMessage( message )   )


	
		if messages : 
			# iterar por los mensjes
			for mensajes : 
				# crear clase mensaje

				message

		else

			# exception


		# 

		#

		# integrar un mensaje e 

			messages.add(  ) 

	else :
		# revisar si la pantalla maestra ha enviado mensajes nuevos



def animate() :

	if messages :
		# avanzar animacion de todos los mensajes un "paso"
		for message in canvasMessages :
			if message.done

	



def draw() :


def main() :

	listeners = getListeners()

    messages = getMessages
	if messages:
		if isMaster:
			# enviar mensajes a pantallas esclavas

		else:
			if animationRunning : 

				animate()


    # repetir esto inf veces

`
