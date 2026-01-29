# Event API | 8-oy | Final exam

Ushbu loyiha so'nggi oy imtihon uchun.

## O'rnatish
Terminalni ochamiz va Githubdan loyihani clone qilamiz:
```bash
git clone https://github.com/newbiestart/api_events.git
```
Virtual muhit yaratamiz (Linux uchun):
```bash
python3 -m venv env
```
Va yaratgan virtual muhitimizni aktivatsiya qilamiz:
```bash
source env/bin/activate
```

pip bilan kerakli requirementsni o'rnatamiz:

```bash
pip install -r requirements.txt
```
Keyin esa:
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
Va yana terminalda:
```bash
python3 manage.py runserver
```

/bot fayli ichidagi BOT_TOKEN ga o'z bot tokeningizni qo'yasiz, yangi terminalda esa:
```bash
cd bot
python3 bot.py
``` 

## License

[MIT](https://github.com/newbiestart/api_events/tree/main?tab=MIT-1-ov-file)
