+++
type = "question"
title = "Wireshark can not decode TCP retransmission messages"
description = '''Hello From wireshark version 2 and on, I could not decode diameter messages. Wireshark understand the packet as TCP Retransmission. Even with decode us it was not possible to decode it. Thanks Stavros '''
date = "2016-07-21T01:10:00Z"
lastmod = "2016-07-21T03:39:00Z"
weight = 54211
keywords = [ "message", "retransmissions", "tcp" ]
aliases = [ "/questions/54211" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark can not decode TCP retransmission messages](/questions/54211/wireshark-can-not-decode-tcp-retransmission-messages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54211-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>From wireshark version 2 and on, I could not decode diameter messages. Wireshark understand the packet as TCP Retransmission. Even with decode us it was not possible to decode it.</p><p>Thanks</p><p>Stavros</p><p><img src="https://osqa-ask.wireshark.org/upfiles/diameter_EpCuKns.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">message retransmissions tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jul '16, 01:10</strong></p><img src="https://secure.gravatar.com/avatar/5318038b31cc44ad026905167c9b1824?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="steve21&#39;s gravatar image" /><p>steve21<br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="steve21 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-54211" class="comments-container"><span id="54212"></span><div id="comment-54212" class="comment"><div id="post-54212-score" class="comment-score"></div><div class="comment-text"><p>Are you saying that Wireshark marks even the first occurrence of a packet in the capture as a retransmission, or that it does not bother to dissect again a retransmitted packet if it has already dissected its first occurrence?</p><p>Can you post the capture at cloudshark or some file sharing service and edit your question with a link to it?</p></div><div id="comment-54212-info" class="comment-info"><span class="comment-age">(21 Jul '16, 01:52)</span> sindy</div></div><span id="54213"></span><div id="comment-54213" class="comment"><div id="post-54213-score" class="comment-score"></div><div class="comment-text"><p>Hello</p><p>It is not a re-transmitted message. It's a CCR-U Diameter message.</p><p><a href="https://www.cloudshark.org/captures/92e2092341f2">https://www.cloudshark.org/captures/92e2092341f2</a></p></div><div id="comment-54213-info" class="comment-info"><span class="comment-age">(21 Jul '16, 02:16)</span> steve21</div></div><span id="54214"></span><div id="comment-54214" class="comment"><div id="post-54214-score" class="comment-score"></div><div class="comment-text"><p>Is it a capture of real traffic or is part of the packets (the IP and TCP part in particular) handcrafted? Because the TCP sequence numbers are clearly wrong, having a constant value of 1 for all packets (which explains why Wireshark doesn't bother inspecting the packet in deeper detail because a TCP packet bearing an already used sequence number and non-zero payload size cannot be anything else but a retransmission), so I wonder how something like this could actually work in a real network. Something is also telling me that use of TCP port 0 is not legal, but I may be wrong.</p><p>If it is a real traffic, it only can work because both participants of the conversation use the same incorrect TCP implementation. So interworking with any other vendor's stack would be impossible.</p></div><div id="comment-54214-info" class="comment-info"><span class="comment-age">(21 Jul '16, 02:28)</span> sindy</div></div></div><div id="comment-tools-54211" class="comment-tools"></div><div class="clear"></div><div id="comment-54211-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54215"></span>

<div id="answer-container-54215" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54215-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi again</p><p>The cap was capture from trace tool which we are using in our Gateway. Problem solved. Unchecked the Analyse TCP sequences fro TCP Preferences.</p><p>Thanks for your effort</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jul '16, 03:39</strong></p><img src="https://secure.gravatar.com/avatar/5318038b31cc44ad026905167c9b1824?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="steve21&#39;s gravatar image" /><p>steve21<br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="steve21 has no accepted answers">0%</span></p></div></div><div id="comments-container-54215" class="comments-container"></div><div id="comment-tools-54215" class="comment-tools"></div><div class="clear"></div><div id="comment-54215-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

