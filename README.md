# tock-py-bot-demo

Source code contains :

- A sample html file for the chat widget : [web/index.html](web/index.html)
- Simple python-based bot implementation
    - [bot](bot.py)
    - [websocket](start-websocket.py)
    - [webhook](start-webhook.py)
    
Install dependencies :

    pip install -r requirements.txt

    
Start websocket mode :

    TOCK_APIKEY=%YOUR-API-KEY% ./start-websocket.py
    
Start webhook mode :
    
    TOCK_WEBHOOK_PATH=%YOUR-WEBHOOK-PATH% ./start-webhook.py
