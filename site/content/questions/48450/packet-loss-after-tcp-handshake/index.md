+++
type = "question"
title = "Packet loss after tcp handshake"
description = '''Good morning, A program is receiving packets, but I&#x27;m not seeing anything after the handshake in wireshark. Is it possible to view this in wireshark? I appreciate your patience.'''
date = "2015-12-11T07:11:00Z"
lastmod = "2015-12-11T08:44:00Z"
weight = 48450
keywords = [ "handshake", "tcp" ]
aliases = [ "/questions/48450" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Packet loss after tcp handshake](/questions/48450/packet-loss-after-tcp-handshake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48450-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Good morning,</p><p>A program is receiving packets, but I'm not seeing anything after the handshake in wireshark. Is it possible to view this in wireshark? I appreciate your patience.</p></div><div id="question-tags" class="tags-container tags">handshake tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Dec '15, 07:11</strong></p><img src="https://secure.gravatar.com/avatar/b4a22c0d00e6c1914c6419657e35f6a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="beepboop&#39;s gravatar image" /><p>beepboop<br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="beepboop has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Dec '15, 07:22</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-48450" class="comments-container"></div><div id="comment-tools-48450" class="comment-tools"></div><div class="clear"></div><div id="comment-48450-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="48451"></span>

<div id="answer-container-48451" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48451-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Before digging in any other direction, please try to deactivate any security/antivirus software running on the machine on which you capture and try again. This type of applications often interferes with capturing process, or even worse, causes mysterious malfunctions of some network communication (which seems not to be your case).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Dec '15, 07:26</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-48451" class="comments-container"></div><div id="comment-tools-48451" class="comment-tools"></div><div class="clear"></div><div id="comment-48451-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="48455"></span>

<div id="answer-container-48455" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48455-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you capturing on Windows Server 2008 or later? If so, read <a href="https://blog.wireshark.org/2009/09/missing-packets-and-chimnies/">this link</a>, and then see if TCP Chimney is enabled on your system. If it is, either turn it off, or capture from the wire instead of on the server.</p><p>Actually, moving your capture point to capture from the wire instead of directly on an endpoint will probably resolve the problem regardless of the cause.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Dec '15, 08:44</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-48455" class="comments-container"></div><div id="comment-tools-48455" class="comment-tools"></div><div class="clear"></div><div id="comment-48455-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

