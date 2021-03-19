+++
type = "question"
title = "ModBus TCP communication problem"
description = '''I have a device (lets call it MovaColor) which communicates with clients connected via modbus tcp. The clients make read/write operations to the movacolor. Client 1 is plc based hardware (B&amp;amp;R PP41), client 2 is IPC based implemented in Labview with modbus library running on windows XP (IPC is al...'''
date = "2014-02-27T01:39:00Z"
lastmod = "2014-03-05T04:22:00Z"
weight = 30228
keywords = [ "modbus", "fragmentation", "tcp" ]
aliases = [ "/questions/30228" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ModBus TCP communication problem](/questions/30228/modbus-tcp-communication-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30228-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30228-score" class="post-score" title="current number of votes">0</div><span id="post-30228-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a device (lets call it MovaColor) which communicates with clients connected via modbus tcp. The clients make read/write operations to the movacolor. Client 1 is plc based hardware (B&amp;R PP41), client 2 is IPC based implemented in Labview with modbus library running on windows XP (IPC is also from B&amp;R APC 810). I have reproducible communication problems :</p><p>When client 2 (IPC) communicates with movacolor then reading registers is without problem (after connection), but after writing once, the next read response is fragmented, an I get an an error message from client 2, that the network connection was closed by the peer. Than, after few seconds, there is also an RST frame.</p><p><a href="http://www.cloudshark.org/captures/0882b3aee4ea">I have an pcap file for this communication.</a></p><p>In comparison to that I tested the communication between movacolor and client 1 (plc based). Also with read/write requests. Reading from the device is no problem, but after writing once, the next read response is fragmented as in the situation above, but does not lead to connection reset. I uploaded an <a href="http://www.cloudshark.org/captures/c7d63da655df">pcap for the Movacolor - Client 1 communication also.</a></p><p>I compared both traces and found that client 2 has set the don't fragment bit and client 1 does not. What does it mean ?. My knowledge is kind of limited here. I ask myself why the fragmentation does occure at all, even if it is only 70 byte. I asked the OEM of the movacolor for the MTU size of the controller unit, unfortunately it is not known.</p><p>Any help in this issue is higly appreciated.</p><p>Jörn</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-modbus" rel="tag" title="see questions tagged &#39;modbus&#39;">modbus</span> <span class="post-tag tag-link-fragmentation" rel="tag" title="see questions tagged &#39;fragmentation&#39;">fragmentation</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Feb '14, 01:39</strong></p><img src="https://secure.gravatar.com/avatar/4cc466de24d3e4cd638ee3b06476eade?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joernheit&#39;s gravatar image" /><p><span>joernheit</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joernheit has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Feb '14, 23:49</strong> </span></p></div></div><div id="comments-container-30228" class="comments-container"></div><div id="comment-tools-30228" class="comment-tools"></div><div class="clear"></div><div id="comment-30228-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30441"></span>

<div id="answer-container-30441" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30441-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30441-score" class="post-score" title="current number of votes">0</div><span id="post-30441-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In the capture for client 2, in frame 26 the remote device sends back an incorrect response to the Write Multiple Registers request sent in frame 24. The erroneous response includes the byte count and data that were transmitted in the request (02 00 01). If you have Modbus TCP Reassembly turned on, this then messes up the dissection of the next response in frame 29.</p><p>Regardless of the above I can see no reason in the dissected Modbus traffic for the remote device to then send the RST in frame 31. It does send the RST after a delay of 3 seconds so I wonder if the client device is confused by the erroneous response and stops communicating and the remote device times out.</p><p>In the capture for client 1, the client seems to ignore the erroneous response and so communication proceeds as expected.</p><p>Purely conjecture, but I suspect that client 1 is draining the receive stream of all data after reading the expected response, before transmitting the next query and so handles the erroneous response. Client 2 probably doesn't do this and after the subsequent query response is coalesced with the erroneous trailer the client is confused and stops communicating.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '14, 04:22</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-30441" class="comments-container"></div><div id="comment-tools-30441" class="comment-tools"></div><div class="clear"></div><div id="comment-30441-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

