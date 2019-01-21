curl -L "http://ekstrabladet.dk/nationen/1849" >> ./1849.html
curl -L "http://ekstrabladet.dk/nationen" >> ./nationen.html
python3 nationen_parser.py
