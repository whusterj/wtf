# WTF

Most programmers are familiar with this iconic comic:

![WTF](img/wtfm.jpg)
[Source](http://www.osnews.com/story/19266/WTFs_m)

And anyone who has ever done code review or even just tried to read code knows how true this is.

# WTF. Why?

Well, I've been doing more code reviews lately, and I found myself wishing I had an easy way to record those moments that just make me go: "WTF". 

Seriously, though, it's useful to keep a log of your thoughts while doing code review for later summary. I thought it might be even _better_ to timestamp those thoughts. That way, I could quantify exactly how much of my life had been wasted on crappy code. Inspired by the comic above, I also wanted to generate a WTF/min score as a useful (stretching that word) code review benchmark.

It's also just plain cathartic to pound out a *WTF* or two if ever you find yourself looking at very. bad. code.

# Use

WTF is a single, dependency-free Python file. I recommend Python 3.3 and above.

To record a WTF moment, just execute it:

```python
./wtf.py
```

By default this will write a timestamp to a file in the local directory called 'wtfs.txt'.

Want to add some detail about the sheer idiocy that's blowing your mind right now? Just use the `--message` argument (`-m` for short). Make sure your message is in quotes (just like `git commit -m`):

```python
./wtf.py -m "Why the hell would someone indent with tabs in this module, when all of the other modules use spaces!? ARG1!@!fk.dfaskdnfasvnowe"
```

You can change the location of the output file with the `--output`/`-o` option:

```python
./wtf.py -m "I just can't even." -o code-review-01.txt
```

And finally, you can get summary stats with the `--read`/`-r` options. Just supply the name of the file to read:

```python
./wtf.py -r code-review-01.txt
```

And you'll get an output like this:

    Total WTFs: 35
    Duration (minutes): 20.54
    WTFs/min: 1.704

Run `./wtf.py -h` to see the complete usage info:

    usage: wtf.py [-h] [-m MESSAGE] [-o OUTFILE] [-r READ]

    Easily record WTF moments.

    optional arguments:
      -h, --help            show this help message and exit
      -m MESSAGE, --message MESSAGE
                            Record the thing that made you go WTF
      -o OUTFILE, --outfile OUTFILE
                            Specify a filename for your WTF log.
      -r READ, --read READ  Read a WTF log file. Outputs stats and WTFs per
                            minute.