# timer

### ZSH config

```sh
alias timer='function timer_py(){ python3 ~/code/timer/timer.py $1; };timer_py'
```

### Run

```sh
timer Hours:Minutes:Seconds
```

example:

```sh
# 1 hour, 3 minutes and 25 seconds
timer 1:3:25
```
