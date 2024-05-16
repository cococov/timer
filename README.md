# timer

![image](https://github.com/cococov/timer/assets/19384973/43449fc0-b7b1-4cb8-a880-fd69e999a3d3)

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
