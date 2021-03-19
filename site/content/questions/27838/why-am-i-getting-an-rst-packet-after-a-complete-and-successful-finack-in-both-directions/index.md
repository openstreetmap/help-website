+++
type = "question"
title = "Why am I getting an RST packet after a complete and successful fin/ack in both directions?"
description = '''I have a client device requesting data from a server device, periodically following a fin/ack, ack, fin/ack, ack, the server device proceeds to send an RST packet... why would this happen? this packet should never happen right? the session is closed, why send an RST?'''
date = "2013-12-05T10:44:00Z"
lastmod = "2013-12-06T11:49:00Z"
weight = 27838
keywords = [ "rst" ]
aliases = [ "/questions/27838" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Why am I getting an RST packet after a complete and successful fin/ack in both directions?](/questions/27838/why-am-i-getting-an-rst-packet-after-a-complete-and-successful-finack-in-both-directions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27838-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a client device requesting data from a server device, periodically following a fin/ack, ack, fin/ack, ack, the server device proceeds to send an RST packet... why would this happen? this packet should never happen right? the session is closed, why send an RST?</p></div><div id="question-tags" class="tags-container tags">rst</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '13, 10:44</strong></p><img src="https://secure.gravatar.com/avatar/4b364045859a8ed82e0c579cf4f73fe4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jwolf&#39;s gravatar image" /><p>jwolf<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jwolf has no accepted answers">0%</span></p></div></div><div id="comments-container-27838" class="comments-container"></div><div id="comment-tools-27838" class="comment-tools"></div><div class="clear"></div><div id="comment-27838-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27842"></span>

<div id="answer-container-27842" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27842-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The server probably never sent it. Some firewalls do this when they cleanup their connection table. Did you check the ip.ttl / ip.id of the RST packet and compare it to the server's other packets?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '13, 21:23</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-27842" class="comments-container"><span id="27876"></span><div id="comment-27876" class="comment"><div id="post-27876-score" class="comment-score"></div><div class="comment-text"><p>this is on a controlled test environment with only one switch and no firewalls. ip.ttl is 128 and the ip.id is incremented by 1 just like the previous packets from that server device, I call it a server device because that is how it is functioning in the modbus communication.</p></div><div id="comment-27876-info" class="comment-info"><span class="comment-age">(06 Dec '13, 11:32)</span> jwolf</div></div></div><div id="comment-tools-27842" class="comment-tools"></div><div class="clear"></div><div id="comment-27842-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27877"></span>

<div id="answer-container-27877" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27877-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>why send an RST?</p></blockquote><p>because of the way the TCP/IP stack of that device was programmed. Could be intentional, could be a bug. Without insight into the code, you will never know. Some versions of Windows do that, for no good reason.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Dec '13, 11:49</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Dec '13, 11:51</p></div></div><div id="comments-container-27877" class="comments-container"><span id="27879"></span><div id="comment-27879" class="comment"><div id="post-27879-score" class="comment-score"></div><div class="comment-text"><p>it does not use windows and its not a server parse, its a device that collects and sends data to a data collection device, it technically is the server in the server client relationship. so you are saying that it is either a potential error or it was programmed that way intentionally? thanks for the response.</p></div><div id="comment-27879-info" class="comment-info"><span class="comment-age">(06 Dec '13, 12:54)</span> jwolf</div></div><span id="27881"></span><div id="comment-27881" class="comment"><div id="post-27881-score" class="comment-score"></div><div class="comment-text"><p>I'm saying, if it is some embedded device, it could be a bug in the TCP/IP implementation. However, it could also be intentional. I don't know a good reason, but maybe the developer of that IP stack knew one while he was writing the code. Who knows....</p><p>Do you know if that device uses any standard OS (Linux, BSD, vxworks, QNX, etc.)</p></div><div id="comment-27881-info" class="comment-info"><span class="comment-age">(06 Dec '13, 13:34)</span> Kurt Knochner ♦</div></div><span id="27884"></span><div id="comment-27884" class="comment"><div id="post-27884-score" class="comment-score"></div><div class="comment-text"><p>There is an internet draft describing a client sending a RST after FIN to avoid too many TIME_WAIT connections. <a href="http://tools.ietf.org/html/draft-faber-time-wait-avoidance-00">http://tools.ietf.org/html/draft-faber-time-wait-avoidance-00</a> . So at least someone thought of doing this as a 'good reason'</p></div><div id="comment-27884-info" class="comment-info"><span class="comment-age">(07 Dec '13, 00:01)</span> mrEEde</div></div><span id="27888"></span><div id="comment-27888" class="comment"><div id="post-27888-score" class="comment-score"></div><div class="comment-text"><p>That's a good reason for the <strong>client</strong> to send a RST. In fact IE on Windows is doing that, while Firefox on the same client does not send the RST, which indeed leads to the situation that the Firefox connection is shown much longer in TIME_WAIT state on the server (netstat -na).</p><p><strong>However</strong>, the OP reported the server sending the RST. And I don't know a good reason for that. There might be one, I just don't know one.</p></div><div id="comment-27888-info" class="comment-info"><span class="comment-age">(07 Dec '13, 06:58)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-27877" class="comment-tools"></div><div class="clear"></div><div id="comment-27877-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

