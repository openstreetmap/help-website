+++
type = "question"
title = "Embedded Python in dissector"
description = '''I have modified one of the dissectors to display additional details and works great. What I want to do next is to write the result after each packet is dissected into a DB. My first thought was to use Python embedded into the dissector to save into sqlite db. I added the Python.h header and getting ...'''
date = "2014-07-24T07:35:00Z"
lastmod = "2014-07-24T08:02:00Z"
weight = 34883
keywords = [ "python-embedded" ]
aliases = [ "/questions/34883" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Embedded Python in dissector](/questions/34883/embedded-python-in-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34883-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have modified one of the dissectors to display additional details and works great. What I want to do next is to write the result after each packet is dissected into a DB. My first thought was to use Python embedded into the dissector to save into sqlite db. I added the Python.h header and getting the error below. Not sure which file to update to allow the include path to be searched. Can this be done, if yes, what do I need to do to correct this. Any help would be appreciated. Thank you.</p><p>packet-fix.c(31) : fatal error C1083: Cannot open include file: 'Python.h': No such file or directory</p></div><div id="question-tags" class="tags-container tags">python-embedded</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '14, 07:35</strong></p><img src="https://secure.gravatar.com/avatar/df3883c2c65a6be2ba9d90d73edc7f13?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DennisVecchio&#39;s gravatar image" /><p>DennisVecchio<br />
<span class="score" title="36 reputation points">36</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DennisVecchio has one accepted answer">100%</span></p></div></div><div id="comments-container-34883" class="comments-container"></div><div id="comment-tools-34883" class="comment-tools"></div><div class="clear"></div><div id="comment-34883-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34884"></span>

<div id="answer-container-34884" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34884-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wouldn't you be better off just using the SQLite C API, rather than bringing python in?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '14, 08:02</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-34884" class="comments-container"><span id="34885"></span><div id="comment-34885" class="comment"><div id="post-34885-score" class="comment-score"></div><div class="comment-text"><p>thx grahamb for responding. Yes I can, I just wanted to try embedding python into the mix. Thx.</p></div><div id="comment-34885-info" class="comment-info"><span class="comment-age">(24 Jul '14, 08:25)</span> DennisVecchio</div></div><span id="34886"></span><div id="comment-34886" class="comment"><div id="post-34886-score" class="comment-score"></div><div class="comment-text"><p>If you really have to use Python I hope you aren't expecting to live capture at high bit rate as I suspect performance would take a dive with the C &gt; Python &gt; C conversions.</p><p>You haven't stated how and what platform you're building on. Depending on the config method (autofoo, CMake or nmake) you'll need to adjust the include path that's presented to the compiler.</p><p>On Windows you'll also have to make sure that you're using the same version of Visual Studio as is used by the Python dll to prevent crt mismatches.</p></div><div id="comment-34886-info" class="comment-info"><span class="comment-age">(24 Jul '14, 08:34)</span> grahamb ♦</div></div><span id="34890"></span><div id="comment-34890" class="comment"><div id="post-34890-score" class="comment-score"></div><div class="comment-text"><p>Sorry about that, it’s on a window machine with VS 10 and Python27. Yes, I agree with you as the performance would take a hit. Thx, will check nmake files and adjust the include path. When I originally looked, I wasn't sure where/what to modify, but will look again. By trade, I am network guy and writing code when I’m free (help automate/troubleshoot network tasks/issues). If you can guide me to which files to modify, it would be very helpful. Much appreciated!</p></div><div id="comment-34890-info" class="comment-info"><span class="comment-age">(24 Jul '14, 11:23)</span> DennisVecchio</div></div><span id="34891"></span><div id="comment-34891" class="comment"><div id="post-34891-score" class="comment-score"></div><div class="comment-text"><p>The include directory would be added to CFLAGS in <code>epan\dissectors\Makefile.nmake</code> as another /I option. You'll probably have to add the Python import library to libwireshark_LIBS in <code>epan\Makefile.nmake</code> as well.</p></div><div id="comment-34891-info" class="comment-info"><span class="comment-age">(24 Jul '14, 11:38)</span> grahamb ♦</div></div><span id="34894"></span><div id="comment-34894" class="comment"><div id="post-34894-score" class="comment-score"></div><div class="comment-text"><p>Thank you much grahamb! Will work on it tonight. thx again!</p></div><div id="comment-34894-info" class="comment-info"><span class="comment-age">(24 Jul '14, 11:48)</span> DennisVecchio</div></div><span id="34901"></span><div id="comment-34901" class="comment not_top_scorer"><div id="post-34901-score" class="comment-score"></div><div class="comment-text"><p>Hey grahamb, In wireshark\config.nmake contains variables/flags (PYTHON_CFLAGS) for Python. There was a flag PYTHON_EMBED=1, which is the trigger to setup all of the Python variables/flags and it was commented out by default. I took the comment out and added $(PYTHON_CFLAGS) to CFLAGS in dissector\Makefile.nmake and successfully compiled. Thank you for your help!!</p></div><div id="comment-34901-info" class="comment-info"><span class="comment-age">(24 Jul '14, 15:42)</span> DennisVecchio</div></div></div><div id="comment-tools-34884" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-34884-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

