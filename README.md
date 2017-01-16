#Self made MANpages

You know how you always forget what tar flags to use, so you have to look it up every single time, even though you know it? I know that feeling too.

So I made this. 

Put in whatever you forget, and query it fast over the web with curl or whatever, so you never have to leave your beloved terminal.

i.e,

```
http://localhost:5000/learn/paste%20in%20vim

  "count": 1, 
  "results": [
    {
      "body": "open vim, then enter <:set paste>. This will stop vim from auto indenting and all that other stuff. To leave this mode, type <:set unpaste>", 
      "description": "how to paste items into vim safely", 
      "tags": "vim, terminal", 
      "title": "paste into vim"
    }
  ]
}
```

it uses flask and sqlite
