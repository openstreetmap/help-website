+++
type = "question"
title = "How to filter TCP SO_KEEPALIVE packets?"
description = '''I would like to look for packets sent between to Linux 2.6.32 systems that are coming from the kernel due to sockets that have SO_KEEPALIVE set having been idle long enough to cause keep alive packets to be sent. What filter expression should I use? I&#x27;d prefer a capture filter but if only a display ...'''
date = "2013-05-23T15:06:00Z"
lastmod = "2013-06-30T00:19:00Z"
weight = 21423
keywords = [ "capture-filter", "linux", "keepalive" ]
aliases = [ "/questions/21423" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to filter TCP SO\_KEEPALIVE packets?](/questions/21423/how-to-filter-tcp-so_keepalive-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21423-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to look for packets sent between to Linux 2.6.32 systems that are coming from the kernel due to sockets that have SO_KEEPALIVE set having been idle long enough to cause keep alive packets to be sent. What filter expression should I use? I'd prefer a capture filter but if only a display filter works I can use that instead. Thanks</p></div><div id="question-tags" class="tags-container tags">capture-filter linux keepalive</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 May '13, 15:06</strong></p><img src="https://secure.gravatar.com/avatar/65f06def3d83622f7624f6247eb9e1e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="token&#39;s gravatar image" /><p>token<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="token has no accepted answers">0%</span></p></div></div><div id="comments-container-21423" class="comments-container"></div><div id="comment-tools-21423" class="comment-tools"></div><div class="clear"></div><div id="comment-21423-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21424"></span>

<div id="answer-container-21424" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21424-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>You might not be able to see this in the packets themselves unless they have some specific bytes that makes them distinguishable, and the keep-alives I have seen so far are usually normal TCP packets without any payload. The Wireshark TCP expert marks them as keep-alives though because it keeps track of the TCP session. You can filter for them by using the display filter, "tcp.analysis.keep_alive".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '13, 15:13</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Jun '13, 23:59</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-21424" class="comments-container"></div><div id="comment-tools-21424" class="comment-tools"></div><div class="clear"></div><div id="comment-21424-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22481"></span>

<div id="answer-container-22481" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22481-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>TCP network packets with no data in it and the ACK flag turned on.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jun '13, 00:19</strong></p><img src="https://secure.gravatar.com/avatar/f2239b90c0c4d5519661418823eb7116?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Inge%20Eivind%20Henriksen&#39;s gravatar image" /><p>Inge Eivind ...<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Inge Eivind Henriksen has no accepted answers">0%</span></p></div></div><div id="comments-container-22481" class="comments-container"><span id="22494"></span><div id="comment-22494" class="comment"><div id="post-22494-score" class="comment-score"></div><div class="comment-text"><p>That'll also see normal ACK-only packets, sent because the machine sending the ACK-only packet has no data to transmit but needs to acknowledge data it received.</p></div><div id="comment-22494-info" class="comment-info"><span class="comment-age">(30 Jun '13, 20:10)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-22481" class="comment-tools"></div><div class="clear"></div><div id="comment-22481-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

