Chat server application written in Python that is functional at the moment although it still needs some tweaks to
improve message sending. Next step is to have server source to run on Raspberry Pi so users can connect from separate
machines.

## Requirements

- Python 3
- PyQt4, only when running the optional desktop chat client

## Running the Server

Start the socket server from the repository root:

```sh
python3 bin/server.py
```

The server listens on port `9009` and accepts connections from any network interface.

## Running the Client

If PyQt4 is installed, start the generated desktop client with:

```sh
python3 bin/chat_ui.py
```

Enter the server IP address in the client and connect. For local testing on the same machine, use `127.0.0.1`.
