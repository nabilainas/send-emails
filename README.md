### Building SMTP server with python

On doit commencer par installer le module python avec la commande

pip install secure-smtplib

ensuite pour lancer le server

python3 -m smtpd -n -c DebuggingServer localhost:1025