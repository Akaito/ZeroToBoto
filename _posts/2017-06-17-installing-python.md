---
category: info
info_order: 1
date: 2017-06-17 17:00 -07:00
title: Installing Python
---

Try `python --version` at the command line.  If you don't see '2.7' somewhere in there, do these steps first.

<!-- more -->

### Windows

Use [this installer](https://www.python.org/ftp/python/2.7.13/python-2.7.13.amd64.msi) ([GPG signature](https://www.python.org/ftp/python/2.7.13/python-2.7.13.amd64.msi.asc)), or an on-site copy of a 2.7 installer if your organization has one.

If you want to use the above GPG signature to verify that installer, get the Python release manager public keys with<br/>
`gpg --recv-keys 6A45C816 36580288 7D9DC8D2 18ADD4FF A4135B38 A74B06BF EA5BBD71 ED9D77D5 E6DF025C AA65421D 6F5E1540 F73C700D 487034E5`

### Linux

Use your package manager.  `apt install python` on Debian-like systems.

---

Once either process above is followed, confirm the output from `python --version` looks something like `Python 2.7.10`.

