---
category: info
info_order: 85
date: 2017-08-09 09:22 -07:00
title: Functions and References
---

TODO!

<!-- more -->

---

```python
def build(word, guesses):
    result = ''
    for letter in word:
        if letter in guesses:
            result += letter
        else:
            result += '.'
    return result

target_word = 'otter'
guesses = ['t', 'r']

print build(target_word, guesses)
```

---

### Executed to line 9

<table></table>

<div border=1> program heap
&lt;function&gt; 1
</div>

<div border=1> program stack
<div border=1> global scope
<div border=1> objects
build -> &lt;function&gt; 1
</div>
</div>
</div>

---

