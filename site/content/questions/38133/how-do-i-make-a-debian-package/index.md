+++
type = "question"
title = "How do I make a Debian package?"
description = '''How do I make a Debian .deb package of my build of Wireshark? The developer&#x27;s guide indicates there is (or used to be) a debian-package make target. Using the latest development version (commit 152b0c92d6, which builds and appears to run just fine), there is no such make target. Additionally, there ...'''
date = "2014-11-25T10:02:00Z"
lastmod = "2014-11-26T06:19:00Z"
weight = 38133
keywords = [ "development", "installer", "build", "debian" ]
aliases = [ "/questions/38133" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How do I make a Debian package?](/questions/38133/how-do-i-make-a-debian-package)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38133-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do I make a Debian .deb package of my build of Wireshark?</p><p>The <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSrcBinary.html" title="3.11 Binary packaging">developer's guide</a> indicates there is (or used to be) a <code>debian-package</code> make target. Using the latest development version (commit 152b0c92d6, which builds and appears to run just fine), there is no such make target. Additionally, there is no <code>packaging/debian</code> folder. Do I need to pass any particular options to <code>autogen.sh</code> or <code>configure</code> to enable debian package output?<br />
On windows, I would just invoke <code>nmake -f Makefile.nmake packaging</code>, and an NSIS installer that could be shared with anyone is generated automatically. I want to distribute a .deb in the same manner.</p></div><div id="question-tags" class="tags-container tags">development installer build debian</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '14, 10:02</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span> </br></p></div></div><div id="comments-container-38133" class="comments-container"><span id="38135"></span><div id="comment-38135" class="comment"><div id="post-38135-score" class="comment-score"></div><div class="comment-text"><p>Apparently maintaining the <code>debian-package</code> stuff was a headache or less-important use-case for most developers (see <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8190">bug 8190</a>). I'd still like to know how to make a Debian package of Wireshark (a pointer or two about how to get started would be good enough), so I'm leaving the question open.</p></div><div id="comment-38135-info" class="comment-info"><span class="comment-age">(25 Nov '14, 10:29)</span> multipleinte...</div></div></div><div id="comment-tools-38133" class="comment-tools"></div><div class="clear"></div><div id="comment-38133-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38169"></span>

<div id="answer-container-38169" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38169-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Wireshark buildbot for Ubuntu makes one, see <a href="http://buildbot.wireshark.org/trunk/builders/Ubuntu%2014.04%20x64/builds/1374/steps/shell_3/logs/stdio">here</a> for example. Looks like the build step runs <code>dpkg-buildpackage -us -uc -rfakeroot</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '14, 06:19</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-38169" class="comments-container"></div><div id="comment-tools-38169" class="comment-tools"></div><div class="clear"></div><div id="comment-38169-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

