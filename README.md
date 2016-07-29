# sign-msg
Sign a message with a bitcoin private key

I made this because [Jaxx](https://jaxx.io) doesn't have a built in signing tool.
To sign something with this, go to Tools > Display Private Keys > Display Bitcoin Keys, then copy the private key for whatever address you want.

Here is the output of `./sign-msg -h`
```
usage: sign-msg [-h] (-m MSG | -f FILE) -p PRIVKEY [-F]

A tool for signing messages with a bitcoin private key.

optional arguments:
  -h, --help            show this help message and exit
  -m MSG, --msg MSG     The message you want to sign.
  -f FILE, --file FILE  A file who's content you want to sign.
  -p PRIVKEY, --privkey PRIVKEY
	                The base58 encoded private key for signing.
  -F, --full            Prints out something that looks more.. full?

You can verify the output with something like
'https://tools.bitcoin.com/verifier.html'.
```

Before you use this script, you should do these commands:
```
git clone https://github.com/ChrisCalderon/sign-msg.git # clone the repo (only do this the first time!)
virtualenv --python=python2 sign-msg # make a virtualenv in the repo (only do this the first time!)
cd sign-msg # go inside!
source bin/activate # activate the virtualenv
pip install -r requirements.txt # install the dependency (only do this the first time!)
./sign-msg ...
```
# UPDATE
It turns out that the dependcy comes with a command line tool to do this, so just use this instead:
```
git clone https://github.com/vbuterin/pybitcointools.git
virtualenv --python=python2 pybitcointools
cd pybitcointools
source bin/activate
python setup.py install
pybtctool ecdsa_sign "message" privkey
```
