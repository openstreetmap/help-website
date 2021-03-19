+++
type = "question"
title = "VoWLAN jitter and packet loss"
description = '''Hi,  I&#x27;m doing a test in a WLAN with 5 computers connected to the AP, but only both of them are doing a VoIP call between them. The computer A has the follow characteristics: Windows 7 home premium, Processador:2,13GhZ, Ram:4G, Wireless speed : between 65 and 130 Mbps. Computer B: Windows XP Profess...'''
date = "2012-12-06T17:24:00Z"
lastmod = "2012-12-11T07:15:00Z"
weight = 16663
keywords = [ "loss", "jitter", "packet", "vowlan" ]
aliases = [ "/questions/16663" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [VoWLAN jitter and packet loss](/questions/16663/vowlan-jitter-and-packet-loss)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16663-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm doing a test in a WLAN with 5 computers connected to the AP, but only both of them are doing a VoIP call between them.</p><p>The computer A has the follow characteristics: Windows 7 home premium, Processador:2,13GhZ, Ram:4G, Wireless speed : between 65 and 130 Mbps.</p><p>Computer B: Windows XP Professional, Service Pack 3, Processor: 1'5'GHz, Ram :1,99G, Wireless speed: 54Mbps</p><p>The problem is that when I have finished to capture the RTP comunication between them (15 minutes of call) always are more packet loss in the communication A--&gt;B than for B--&gt;A, on the other hand the jitter is always higher in A--&gt;B than in B--&gt;A.</p><p>Somebody knows why? I supose that it has to be something related with the CPU and/or the speed wireless, but I don't understand how.</p></div><div id="question-tags" class="tags-container tags">loss jitter packet vowlan</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Dec '12, 17:24</strong></p><img src="https://secure.gravatar.com/avatar/96dc4282b6b2916bfdc223c7082d8140?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vickynp123&#39;s gravatar image" /><p>Vickynp123<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vickynp123 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Dec '12, 19:40</p></div></div><div id="comments-container-16663" class="comments-container"></div><div id="comment-tools-16663" class="comment-tools"></div><div class="clear"></div><div id="comment-16663-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16767"></span>

<div id="answer-container-16767" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16767-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>always are more packet loss in the communication A--&gt;B than for B--&gt;A,</p></blockquote><p>packet loss can have several reasons and the Wifi connection is a good candidate.</p><blockquote><p>on the other hand the jitter is always higher in A--&gt;B than in B--&gt;A.</p></blockquote><p>The jitter calculation results are only comparable if you captured at both sides of the connection. If you've done it only on one side (client), the jitter calculation might show "wrong" values. See my answer to your similar question:</p><blockquote><p><code>http://ask.wireshark.org/questions/15445/different-results-for-the-same-communication-rtp</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Dec '12, 07:15</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-16767" class="comments-container"></div><div id="comment-tools-16767" class="comment-tools"></div><div class="clear"></div><div id="comment-16767-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

