+++
type = "question"
title = "wireshark based 3g protocol analyzer"
description = '''how do i get wireshark based 3g protocol analyzer? I am a learner of 3G protocol and i need an software where I can study wcdma utms protocol stack from sample packets of wcdma , rlc, rrc, etc....'''
date = "2012-04-25T07:23:00Z"
lastmod = "2012-04-25T17:16:00Z"
weight = 10437
keywords = [ "protocol", "based", "3g", "analyzer", "wireshark" ]
aliases = [ "/questions/10437" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark based 3g protocol analyzer](/questions/10437/wireshark-based-3g-protocol-analyzer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10437-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how do i get wireshark based 3g protocol analyzer? I am a learner of 3G protocol and i need an software where I can study wcdma utms protocol stack from sample packets of wcdma , rlc, rrc, etc....</p></div><div id="question-tags" class="tags-container tags">protocol based 3g analyzer wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Apr '12, 07:23</strong></p><img src="https://secure.gravatar.com/avatar/93a4c56b6418d23362d6e787c2f9b1e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="souhal67&#39;s gravatar image" /><p>souhal67<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="souhal67 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Apr '12, 18:47</p></div></div><div id="comments-container-10437" class="comments-container"></div><div id="comment-tools-10437" class="comment-tools"></div><div class="clear"></div><div id="comment-10437-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10451"></span>

<div id="answer-container-10451" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10451-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It sounds as if you want a protocol analyzer that can capture on one or more of the 3G air interfaces. That would require either:</p><ul><li>some form of hardware that can capture that traffic and that can plug into the machine running Wireshark - that would require either support for that hardware in libpcap/WinPcap or a program that can capture from that hardware and write to a pcap or pcap-ng file</li></ul><p>or</p><ul><li>some device that can capture that traffic and send it over the network - that would require either support in libpcap/WinPcap to receive that traffic over the network, a program that can receive it and write to a pcap or pcap-ng file, or a dissector for that protocol in Wireshark.</li></ul><p>It would also require dissectors for the protocols running on that interface.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '12, 17:16</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Apr '12, 19:49</p></div></div><div id="comments-container-10451" class="comments-container"></div><div id="comment-tools-10451" class="comment-tools"></div><div class="clear"></div><div id="comment-10451-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

