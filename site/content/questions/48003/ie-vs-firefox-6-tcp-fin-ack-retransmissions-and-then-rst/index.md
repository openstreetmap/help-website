+++
type = "question"
title = "IE vs firefox, 6 tcp fin ack retransmissions and then rst?"
description = '''Hello, I have two conversations that are made with two browsers IE 11 and Firefox. The IE 11 conversation ends in a weird way, trying to send FIN ACK, but never receives a response, and then eventually resets.  This does not happen when I am using Firefox browser to the same webserver.   Client: 172...'''
date = "2015-11-26T02:26:00Z"
lastmod = "2015-11-26T08:36:00Z"
weight = 48003
keywords = [ "firefox", "tcp", "browser" ]
aliases = [ "/questions/48003" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [IE vs firefox, 6 tcp fin ack retransmissions and then rst?](/questions/48003/ie-vs-firefox-6-tcp-fin-ack-retransmissions-and-then-rst)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48003-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have two conversations that are made with two browsers IE 11 and Firefox. The IE 11 conversation ends in a weird way, trying to send FIN ACK, but never receives a response, and then eventually resets.</p><p>This does not happen when I am using Firefox browser to the same webserver.</p><ul><li>Client: 172.16.179.100</li><li><p>Webserver: 11.22.33.44</p></li><li><p>Firefox: <a href="https://www.cloudshark.org/captures/2add6af2c177">https://www.cloudshark.org/captures/2add6af2c177</a></p></li><li>IE 11: <a href="https://www.cloudshark.org/captures/999642ccd04d">https://www.cloudshark.org/captures/999642ccd04d</a></li></ul></div><div id="question-tags" class="tags-container tags">firefox tcp browser</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '15, 02:26</strong></p><img src="https://secure.gravatar.com/avatar/ac57eafee11d4f51450a1ef272a33725?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OlofL&#39;s gravatar image" /><p>OlofL<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OlofL has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Nov '15, 02:28</p></div></div><div id="comments-container-48003" class="comments-container"></div><div id="comment-tools-48003" class="comment-tools"></div><div class="clear"></div><div id="comment-48003-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48009"></span>

<div id="answer-container-48009" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48009-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In the firefox case the server closes the session 5 seconds after the HTTP reply was sent. Firefox immediately issues a close and the FIN gets sent out and ACKed immediately.</p><p>In the IE case it takes 81 seconds for the client to send its FIN In the meantime the server has already closed the socket so you don't get an ACK to your FIN .</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Selection_155.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '15, 08:36</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div></div><div id="comments-container-48009" class="comments-container"><span id="48015"></span><div id="comment-48015" class="comment"><div id="post-48015-score" class="comment-score"></div><div class="comment-text"><p>Yeah is this normal behaviour? We are getting loads of invalid hits in our firewall.</p></div><div id="comment-48015-info" class="comment-info"><span class="comment-age">(26 Nov '15, 23:08)</span> OlofL</div></div><span id="48016"></span><div id="comment-48016" class="comment"><div id="post-48016-score" class="comment-score"></div><div class="comment-text"><p>sure it is not, but you have to claim it with Microsoft.</p></div><div id="comment-48016-info" class="comment-info"><span class="comment-age">(27 Nov '15, 01:27)</span> sindy</div></div></div><div id="comment-tools-48009" class="comment-tools"></div><div class="clear"></div><div id="comment-48009-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

