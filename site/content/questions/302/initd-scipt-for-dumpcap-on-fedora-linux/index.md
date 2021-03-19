+++
type = "question"
title = "init.d scipt for dumpcap on Fedora Linux?"
description = '''I&#x27;ve been using the following script to run dumpcap as a daemon on Ubuntu machine and it was working great.  link:tsharkd I am trying to do the same on a Fedora Core 13 machine but the script doesn&#x27;t work. Can anybody provide a working script or advise on how to change the original one, so it runs o...'''
date = "2010-09-23T11:43:00Z"
lastmod = "2010-09-23T20:59:00Z"
weight = 302
keywords = [ "daemon", "fedora", "dumpcap" ]
aliases = [ "/questions/302" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [init.d scipt for dumpcap on Fedora Linux?](/questions/302/initd-scipt-for-dumpcap-on-fedora-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-302-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been using the following script to run dumpcap as a daemon on Ubuntu machine and it was working great. link:<a href="http://new.networkprotocolspecialists.com/downloads/tsharkd">tsharkd</a></p><p>I am trying to do the same on a Fedora Core 13 machine but the script doesn't work. Can anybody provide a working script or advise on how to change the original one, so it runs on Fedora?</p></div><div id="question-tags" class="tags-container tags">daemon fedora dumpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Sep '10, 11:43</strong></p><img src="https://secure.gravatar.com/avatar/e7d1d3994349a9ea0554a6430dbe2ec8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="naskop&#39;s gravatar image" /><p>naskop<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="naskop has no accepted answers">0%</span></p></div></div><div id="comments-container-302" class="comments-container"><span id="306"></span><div id="comment-306" class="comment"><div id="post-306-score" class="comment-score"></div><div class="comment-text"><p>gteissier, Already tried what you suggested and it errors out on /sbin/start-stop-daemon (I guess that's not used in Fedora)</p></div><div id="comment-306-info" class="comment-info"><span class="comment-age">(23 Sep '10, 21:09)</span> naskop</div></div></div><div id="comment-tools-302" class="comment-tools"></div><div class="clear"></div><div id="comment-302-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="305"></span>

<div id="answer-container-305" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-305-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Replace the second line of the script you linked by set -v -x, and running the script again will give you details about what is going on.</p><p>That said, your question is not related to Wireshark, but rather to Fedora Core &amp; Ubuntu differences.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '10, 20:59</strong></p><img src="https://secure.gravatar.com/avatar/5583aa0f44e8c6dd129ad09c3d5d6732?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gteissier&#39;s gravatar image" /><p>gteissier<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gteissier has no accepted answers">0%</span></p></div></div><div id="comments-container-305" class="comments-container"></div><div id="comment-tools-305" class="comment-tools"></div><div class="clear"></div><div id="comment-305-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

