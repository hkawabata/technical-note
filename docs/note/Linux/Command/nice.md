---
title: nice
---

# 概要

# 使い方

```bash
$ nice -n <priority> <command>
```

# オプション

# Tips

## プロセスの nice 値を確かめる

```bash
$ ps -ewfly | grep -e grep -e "S UID"
S UID        PID  PPID  C PRI  NI   RSS    SZ WCHAN  STIME TTY          TIME CMD
S hkawabat 25702 25476  0  80   0   920 25830 pipe_w 16:56 pts/0    00:00:00 grep -e grep -e S UID
```

`NI`カラムが nice 値を示す。

## "sudo nice" vs "nice sudo"

```bash
$ ps -ewfly | grep -e grep -e "S UID"
S UID        PID  PPID  C PRI  NI   RSS    SZ WCHAN  STIME TTY          TIME CMD
S hkawabat 25523 25476  0  80   0   920 25830 pipe_w 16:52 pts/0    00:00:00 grep -e grep -e S UID

$ ps -ewfly | nice -n 19 grep -e grep -e "S UID"
S UID        PID  PPID  C PRI  NI   RSS    SZ WCHAN  STIME TTY          TIME CMD
S hkawabat 25560 25476  0  99  19   928 25830 pipe_w 16:53 pts/0    00:00:00 grep -e grep -e S UID

$ ps -ewfly | sudo nice -n 19 grep -e grep -e "S UID"
S UID        PID  PPID  C PRI  NI   RSS    SZ WCHAN  STIME TTY          TIME CMD
S root     25562 25476  0  80   0  2524 43774 n_tty_ 16:53 pts/0    00:00:00 sudo nice -n 19 grep -e grep -e S UID

$ ps -ewfly | nice -n 19 sudo grep -e grep -e "S UID"
S UID        PID  PPID  C PRI  NI   RSS    SZ WCHAN  STIME TTY          TIME CMD
S root     25566 25476  0  99  19  2752 43818 poll_s 16:53 pts/0    00:00:00 sudo grep -e grep -e S UID
```

`sudo nice`では効かない模様。
