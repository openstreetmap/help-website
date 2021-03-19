+++
type = "question"
title = "What&#x27;s the difference between receiver address and Destination address?"
description = '''I see that some addresses have transmitter/receiver address in place of source/ destination address. My intuition says that they are the intermediary nodes of a packet trace. But I am unable to see any packets that are connected to this packet before or after. I see such packets in the 802.11 protoc...'''
date = "2014-11-08T18:17:00Z"
lastmod = "2014-11-08T19:19:00Z"
weight = 37706
keywords = [ "packet-capture", "mac-address", "recvraddress", "address" ]
aliases = [ "/questions/37706" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [What's the difference between receiver address and Destination address?](/questions/37706/whats-the-difference-between-receiver-address-and-destination-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37706-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I see that some addresses have transmitter/receiver address in place of source/ destination address. My intuition says that they are the intermediary nodes of a packet trace. But I am unable to see any packets that are connected to this packet before or after. I see such packets in the 802.11 protocol i.e in the physical layer.</p><p>Could someone explain me what exactly is taking place ?</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags">packet-capture mac-address recvraddress address</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '14, 18:17</strong></p><img src="https://secure.gravatar.com/avatar/94eb1c86b27e316bf3c613eaea1feefe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srik11&#39;s gravatar image" /><p>srik11<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srik11 has no accepted answers">0%</span></p></div></div><div id="comments-container-37706" class="comments-container"></div><div id="comment-tools-37706" class="comment-tools"></div><div class="clear"></div><div id="comment-37706-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37707"></span>

<div id="answer-container-37707" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37707-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Basically yes. In 802.11 you can see a different number of these depending on where the frame is coming from and where it's going:</p><ul><li>"Destination Address" or "DA" is the MAC of the final destination of the frame.</li><li>"Source Address" or "SA" is the MAC of the original sender of the frame.</li><li>"Receiver Address" or "RA" is the MAC of the next immediate recipient of the frame.</li><li>"Transmitter Address" or "TA" is the MAC of the system that is directly transmitting the frame.</li></ul><p>So, original source (SA), final destination (DA), and the immediate sending/receiving systems (TA/RA) are four different MACs. Formal definitions would be found in the 802.11 standard itself:</p><p><a href="http://standards.ieee.org/about/get/802/802.11.html">http://standards.ieee.org/about/get/802/802.11.html</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '14, 19:19</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Nov '14, 19:22</p></div></div><div id="comments-container-37707" class="comments-container"><span id="37710"></span><div id="comment-37710" class="comment"><div id="post-37710-score" class="comment-score"></div><div class="comment-text"><p>@Quadratic: Thanks a lot! I have one follow up question. In the 802.11 ack frames, i always find that there is neither source address nor transmitter address. I was wondering if it were because of wrong settings or why ?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screenshot_from_2014-11-09_01:17:49.png" alt="Screenshot" /></p></div><div id="comment-37710-info" class="comment-info"><span class="comment-age">(08 Nov '14, 22:21)</span> srik11</div></div><span id="37713"></span><div id="comment-37713" class="comment"><div id="post-37713-score" class="comment-score"></div><div class="comment-text"><p>Yes, different types of frames will have different MAC fields. The formal breakdown of all 802.11 messages and their expected formats is broken down in section 8.3 in the most recent 802.11 spec paper (from that link above), where frames such as ACK and CTS have only the RA address field included.</p></div><div id="comment-37713-info" class="comment-info"><span class="comment-age">(09 Nov '14, 09:13)</span> Quadratic</div></div></div><div id="comment-tools-37707" class="comment-tools"></div><div class="clear"></div><div id="comment-37707-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

