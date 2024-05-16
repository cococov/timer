# timer

![image](https://github.com/cococov/timer/assets/19384973/a559e7ae-385b-49c5-bf4e-61d150afe641)


### ZSH config

```sh
function timer { python3 ~/code/timer/timer.py $1; }'
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
