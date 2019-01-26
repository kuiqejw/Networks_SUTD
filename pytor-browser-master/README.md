![logo](src/renderer/onion.png)

# PyTor Browser [![Codacy Badge](https://api.codacy.com/project/badge/Grade/41fa263f875e4d50b5d290a15f5c3d6c)](https://www.codacy.com/app/limyaojie93/pytor-browser?utm_source=github.com&utm_medium=referral&utm_content=causztic/pytor-browser&utm_campaign=Badge_Grade)

A simple demonstration of onion-routing done in Python and Electron/NodeJS.

## Pre-Requisites

-   Yarn

-   Any Node LTS (I built it with v11)

-   Respective system libraries if you are building cross platform,
    see electron-builder's [documentation](https://www.electron.build/multi-platform-build).

-   Python 3.6.5 (preferably with pyenv) and corresponding Pip

## Setup

```sh
yarn install
python -m pip install cryptography requests
```

## Running

```sh
sudo chmod +x test_spawns.sh
sudo ./test_spawns.sh
yarn dev
```

## Details

After setting up and running `yarn dev`, a simple web browser will appear. It starts **Client**, which is essentially a proxy server which will process the requests in place of the normal HTTP servers. 

**Client** starts with the default URL of `localhost:27182`.

`test_spawns.sh` will spawn 1 **Directory** and 3 **Relays**.

Behind the scenes, this is what happens:

1.  User goes to a particular website, say example.com.

2.  Client prepares a 3-layer encrypted HTTP request and sends it to the first
    node.

3.  First node will decrypt the first layer, ie. peeling the encryption layer
    off and pass the result along to the second node.

4.  The second node will do the same and pass to third node.

5.  The third node will peel off the last layer and pass the raw HTTP request to
    the HTTP server of example.com.

6.  The third node receives the HTTP response, encrypts it, ie. adding an
    encryption layer and pass it to the second node.

7.  This happens to both second and first node, so the client will receive a
    3-layer encrypted HTTP response.

8.  The client decrypts it to get the raw HTTP response and pass it to the browser
    to process and render.
