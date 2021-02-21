# GoogleHomeSpeak
This is a demo system that speaks Google Home voluntarily.

### Set Up
This system requires Python development Enviroment.
Also, Install libraries.
```
$ pip install -r requirements.txt
```

### Usage
Run Django local server as:
```
$ python manage.py runserver 0.0.0.0:8000
```
, and  run [main.py](main.py) script:
```
$ python main.py "<Google Home device name>" "Spoken text" -l "<`en`(English) or `ja`(Japanese)>"
```

On the other hand, you can run above processes by running [speak.sh](/speak.sh) process with one command as:
```
./speak.sh
```

### Author
[IKEP](https://ikep.jp)

### LICENSE
Copyright (c) 2021 IKEP

[MIT](/LICENSE)
