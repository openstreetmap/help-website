+++
type = "question"
title = "Want to see ALL individual 802.11 frames"
description = '''I am currently using AirPcap Nx and Wireshark, and I want to be sure that I am not missing any individual 802.11 frames. In particular, if I see a packet that Wireshark labels LLC, TCP, RTMP, HTTP, etc., is this still a single 802.11 packet communicated over the air interface OR is such a packet an ...'''
date = "2011-12-13T17:46:00Z"
lastmod = "2011-12-13T23:43:00Z"
weight = 7952
keywords = [ "802.11" ]
aliases = [ "/questions/7952" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Want to see ALL individual 802.11 frames](/questions/7952/want-to-see-all-individual-80211-frames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7952-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am currently using AirPcap Nx and Wireshark, and I want to be sure that I am not missing any individual 802.11 frames. In particular, if I see a packet that Wireshark labels LLC, TCP, RTMP, HTTP, etc., is this still a single 802.11 packet communicated over the air interface OR is such a packet an aggregation of multiple 802.11 packets or fragments.</p></div><div id="question-tags" class="tags-container tags">802.11</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Dec '11, 17:46</strong></p><img src="https://secure.gravatar.com/avatar/02cf4ed95be4ca7470e1bd5ed538c62d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="S_P&#39;s gravatar image" /><p>S_P<br />
<span class="score" title="21 reputation points">21</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="S_P has no accepted answers">0%</span></p></div></div><div id="comments-container-7952" class="comments-container"></div><div id="comment-tools-7952" class="comment-tools"></div><div class="clear"></div><div id="comment-7952-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7953"></span>

<div id="answer-container-7953" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7953-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You're in luck. Wireshark, as a network sniffer, is interested in collecting individual frames, so you have them. But Wireshark also tries to make a higer layer presentation of the protocol riding on top of these frames. Sometimes this requires reassembly of fragmented messages. But you can always drill down to the individual frames.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Dec '11, 23:43</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-7953" class="comments-container"></div><div id="comment-tools-7953" class="comment-tools"></div><div class="clear"></div><div id="comment-7953-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

