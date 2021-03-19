+++
type = "question"
title = "HTTP packets displayed as TCP"
description = '''Hello, I am using version 2.0.0rc1 on OS X.  I am just looking at packets on my own machine (not in monitor mode). I am trying to view HTTP packets but whenever I do a curl command or go to a website they come across as TCP and I can&#x27;t see the HTTP data, is that expected? I can look at the TCP packe...'''
date = "2015-10-22T13:48:00Z"
lastmod = "2015-10-22T13:56:00Z"
weight = 46855
keywords = [ "packets", "http", "tcp" ]
aliases = [ "/questions/46855" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [HTTP packets displayed as TCP](/questions/46855/http-packets-displayed-as-tcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46855-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am using version 2.0.0rc1 on OS X.</p><p>I am just looking at packets on my own machine (not in monitor mode). I am trying to view HTTP packets but whenever I do a curl command or go to a website they come across as TCP and I can't see the HTTP data, is that expected? I can look at the TCP packets and see that they are HTTP related because they have the HTTP coloring code.</p></div><div id="question-tags" class="tags-container tags">packets http tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Oct '15, 13:48</strong></p><img src="https://secure.gravatar.com/avatar/e36c43bf179a6484df6f0db750675a02?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="calers&#39;s gravatar image" /><p>calers<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="calers has no accepted answers">0%</span></p></div></div><div id="comments-container-46855" class="comments-container"></div><div id="comment-tools-46855" class="comment-tools"></div><div class="clear"></div><div id="comment-46855-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46856"></span>

<div id="answer-container-46856" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46856-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This isn't referring to TCP / HTTP packets but its related to this bug: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11593">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11593</a></p><p>Downloading the newest RC here will fix it: <a href="https://www.wireshark.org/download/automated/">https://www.wireshark.org/download/automated/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '15, 13:56</strong></p><img src="https://secure.gravatar.com/avatar/e36c43bf179a6484df6f0db750675a02?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="calers&#39;s gravatar image" /><p>calers<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="calers has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Oct '15, 13:59</p></div></div><div id="comments-container-46856" class="comments-container"><span id="46857"></span><div id="comment-46857" class="comment"><div id="post-46857-score" class="comment-score"></div><div class="comment-text"><p>Here is the same observation: <a href="https://ask.wireshark.org/questions/46764/http-in-packet-list-frame-vs-display-filter?page=1&amp;focusedAnswerId=46775#46775">https://ask.wireshark.org/questions/46764/http-in-packet-list-frame-vs-display-filter?page=1&amp;focusedAnswerId=46775#46775</a></p></div><div id="comment-46857-info" class="comment-info"><span class="comment-age">(22 Oct '15, 14:00)</span> Christian_R</div></div></div><div id="comment-tools-46856" class="comment-tools"></div><div class="clear"></div><div id="comment-46856-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

