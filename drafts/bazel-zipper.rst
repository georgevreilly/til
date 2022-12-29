Bazel Zipper
############

:date: 2022-12-21 13:20
:tags: bazel
:slug: bazel-zipper
:authors: George V. Reilly
:summary: Bazel's hermetic Zipper tool

We use `Bazel`_ at work to build large projects.
It's scalable and powerful—and difficult and complicated.

A colleague was trying to create a zipfile in Bazel.
Initially, they used the `Info-ZIP`_ ``zip`` tool.
Another colleague pointed out that Bazel has its own zipper_ tool.

Apparently, the classic ``zip`` tool
generates slightly different files each time it's run,
while ``zipper`` is hermetic_ and generates identical files.

::

    $ sha256sum z*.zip
    05d1984de38e1b529aeb2037ad87654268b52853e6397164a82f1457e4a6f69b  z1.zip
    b239a4f51b1fe9b54d9f050da813b555d19a97d8ba40c107476412e3a45b8966  z2.zip
    a93b6e24bcdcc399c90921920dfc09c6cf85bc11ab4652318ef1ce267b8b68be  z3.zip
    a93b6e24bcdcc399c90921920dfc09c6cf85bc11ab4652318ef1ce267b8b68be  z4.zip

``z1.zip`` and ``z2.zip`` were created with ``zip``,
while ``z{3,4}.zip`` were created with ``zipper``.
They all have identical contents
but ``zip`` creates slightly different files.

::

    $ cmp -l z{1,2}.zip
     2337 114 301
     2338   6  20
     2339 235 246
    17709 357 301
    17710 377  20
    17711 231 246
    18186  23 301
    18187 123  20
    18188 243 246

It turns out that `Bazel isn't always hermetic`_.



.. _Bazel: https://bazel.build/
.. _Info-ZIP: https://en.wikipedia.org/wiki/Info-ZIP
.. _zipper: https://stackoverflow.com/a/57915191/6364
.. _hermetic: https://bazel.build/basics/hermeticity
.. _Bazel isn't always hermetic:
    https://www.tweag.io/blog/2022-09-15-hermetic-bazel/
