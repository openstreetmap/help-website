+++
type = "question"
title = "In which layer wireshark exactly captures the packets ?"
description = '''I am having a small question regarding wireshark , In which Layer wireshark works.  I.e , on which Layer wireshark capturing the data ? Because I am not getting Ethernet header checksum in my capture , Any Idea ? Thanks'''
date = "2013-11-28T21:03:00Z"
lastmod = "2013-11-29T06:28:00Z"
weight = 27546
keywords = [ "ethernet", "capture" ]
aliases = [ "/questions/27546" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [In which layer wireshark exactly captures the packets ?](/questions/27546/in-which-layer-wireshark-exactly-captures-the-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27546-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am having a small question regarding wireshark , In which Layer wireshark works.</p><p>I.e , on which Layer wireshark capturing the data ?</p><p>Because I am not getting Ethernet header checksum in my capture , Any Idea ?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">ethernet capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Nov '13, 21:03</strong></p><img src="https://secure.gravatar.com/avatar/1c8c710fe5e468a684cea20a8459d45b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="si98765&#39;s gravatar image" /><p>si98765<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="si98765 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Nov '13, 21:07</p></div></div><div id="comments-container-27546" class="comments-container"></div><div id="comment-tools-27546" class="comment-tools"></div><div class="clear"></div><div id="comment-27546-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27550"></span>

<div id="answer-container-27550" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27550-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It generally captures at the link layer.</p><p>That does not, however, mean that the FCS is included (I assume by "Ethernet header checksum" you mean the Ethernet FCS; it is a checksum on the entire packet, not the header). It usually isn't, as the driver usually doesn't configure the Ethernet adapter to provide the FCS of incoming packets to the host (and outgoing packets are captured before the adapter sees the packet and adds the FCS). Sometimes it's provided, but usually it isn't.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Nov '13, 01:32</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-27550" class="comments-container"></div><div id="comment-tools-27550" class="comment-tools"></div><div class="clear"></div><div id="comment-27550-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27565"></span>

<div id="answer-container-27565" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27565-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>See the answer and the comments to a similar question</p><blockquote><p><a href="http://ask.wireshark.org/questions/22956/where-exactly-wireshark-does-captures-packets">http://ask.wireshark.org/questions/22956/where-exactly-wireshark-does-captures-packets</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Nov '13, 06:28</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-27565" class="comments-container"></div><div id="comment-tools-27565" class="comment-tools"></div><div class="clear"></div><div id="comment-27565-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

