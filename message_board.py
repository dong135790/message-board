# Make sure to install flask!
# I did this with the following command:
# python3 -m pip install flask 

# Run with the following command:
# flask --app message_board run

from flask import Flask
from flask import render_template
from flask import request
from message import Message

message_list = [] # data structure to store all messages

app = Flask(__name__) #create a new instance of Flask

# This application supports a single URL -- /messages 
@app.route('/messages/')
def messages():

	# retrieve the message parameter (if present)
	message = request.args.get('message')
	author = request.args.get('author')

	# if there was a message 
	if message and len(message) > 0:
		if author and len(author) > 0:
			# create a new message Object
			new_message = Message(message, author) 
		else:
			new_message = Message(message) 
		# add the message to the list
		message_list.append(new_message) 
	# render using the message_board template in the templates directory
	return render_template('message_board.html', items=message_list)
