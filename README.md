# pomodoro-py

terminal pomodoro timer made by python scripts

## REQUIREMENT

run `python` commands on a terminal

## USAGE

```sh
## at project root dir
## START POMODORO
$ python3 script.py start [task_name];
## after 25minutes, pomodoro finish automatically

## START REST
$ python3 script.py rest
## after 5minutes, rest finish automatically

```

## POMODORO RECORDS

your pomodoros are recorded at `~/pomodoro-history.csv`

the file contents are like below.

※this is sample file, so `start` and `rest` stop within 6 seconds

```csv
START,TEST,2024-12-21 17:55:37.649985+09:00
FINISH,TEST,2024-12-21 17:55:46.728259+09:00
START,REST,2024-12-21 18:01:49.686105+09:00
FINISH,REST,2024-12-21 18:01:58.766694+09:00
```
