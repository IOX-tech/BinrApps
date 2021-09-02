default_port = 800

port = default_port

link = "localhost://" + default_port#localhost 800, 1000, 1200 , 1400........

content = None #extract contemnt from link using webrequests

while content is not None:
    port += 200
else: # comes to else if the port is Empty and hence generates the link
    port = port

def generate():
    return port