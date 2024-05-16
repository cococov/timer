# timer

![image](https://github.com/cococov/timer/assets/19384973/24816b11-91bd-4320-8c89-1196689ac079)

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
