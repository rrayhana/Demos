############################################################################
# YOU MAY NEED TO ADJUST SOME OF THE VALUES TO MAKE IT WORK WITH YOUR CAR. #
############################################################################

# first we import socketio we use this to connect to the PiCar
import socketio 
# next we import time we will use this to delay the code
import time

# create a socketio object
# socketio is a module that allows us to easily use websockets.
# Websockets are a protocol that allows two programs to communicate with each other in real time
# Over the internet. 
sio = socketio.Client()

# we try to connect to the PiCar
try:
    sio.connect('http://192.168.0.10:3000')
# if we fail we print out an error message and exit the program
except:
    print("Failed to connect to PiCar")
    print("Check that your laptop is connected to the PiCar network")
    exit()

# now we can start moving the car
# we set the angle of the steering to 90 degrees
# this is the middle position (180 being fully right and 0 being fully left)
sio.emit('steer', 90)
# we set the speed to 50%
sio.emit('drive', 50)
# we wait for 5 second this is how long the car will move for
time.sleep(5)
# now we stop the car by setting the speed to 0%
sio.emit('drive', 0)
# we stay stopped for 2 seconds
time.sleep(2)
# now we reverse by setting the speed to -50%
sio.emit('drive', -50)
# we wait for 5 seconds again
time.sleep(5)
# now we stop the car by setting the speed to 0%
# don't forget to stop the car!
# Otherwise it'll run away!
sio.emit('drive', 0)