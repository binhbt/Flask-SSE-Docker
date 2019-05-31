# Flask-SSE-Docker  
Implement http Server Sent Event (SSE) streams by PYTHON  
Using for setup PUSH NOTIFICATIONS server  
#Server side  
cd flask-sse  
docker-compose up --build  
#Client side
pip install sseclient  
python client.py  

#Open browser  
http://localhost:5000/send  
You will see on client console  
{"message": "Hello!"}


