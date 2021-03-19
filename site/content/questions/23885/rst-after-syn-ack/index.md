+++
type = "question"
title = "RST after SYN-ACK"
description = '''Hi, i´m facing a strange behavior for a simple telnet connection test, my station send the SYN packet, that go to a server, receive the [SYN, ACK], and just then send a RST. I believe the SYN,ACK packet its malformed, but i couldnt identify what its wrong. Can anyone help me.  Here is the packet cap...'''
date = "2013-08-20T15:58:00Z"
lastmod = "2013-09-19T09:47:00Z"
weight = 23885
keywords = [ "rst", "ack", "after", "syn" ]
aliases = [ "/questions/23885" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [RST after SYN-ACK](/questions/23885/rst-after-syn-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23885-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, i´m facing a strange behavior for a simple telnet connection test, my station send the SYN packet, that go to a server, receive the [SYN, ACK], and just then send a RST. I believe the SYN,ACK packet its malformed, but i couldnt identify what its wrong. Can anyone help me.</p><p>Here is the packet capture, pcap format: <a href="https://docs.google.com/file/d/0B9Co4kddbAUWa0lCRlJ2WmJGS2M/edit?usp=sharing">https://docs.google.com/file/d/0B9Co4kddbAUWa0lCRlJ2WmJGS2M/edit?usp=sharing</a></p><p>Thanks a lot!</p></div><div id="question-tags" class="tags-container tags">rst ack after syn</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Aug '13, 15:58</strong></p><img src="https://secure.gravatar.com/avatar/1b22bfd2ccd87323d4d6be9ae2252033?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fabioalkas&#39;s gravatar image" /><p>fabioalkas<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fabioalkas has no accepted answers">0%</span></p></div></div><div id="comments-container-23885" class="comments-container"></div><div id="comment-tools-23885" class="comment-tools"></div><div class="clear"></div><div id="comment-23885-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23890"></span>

<div id="answer-container-23890" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23890-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The acknowledgment numbers in the SYN/ACK packets are not correct for the SYN packets that they are acknowledging.</p><p>For example, the (absolute) sequence number in frame 1 is 3839424768. The acknowledgment number in the SYN/ACK packet in frame 3 should be 3839424769, but instead frame 3 has an acknowledgment number of 14744888. Because of this, the SYN/ACK packet from 10.223.100.100 does not correspond to a SYN packet sent by 10.0.5.45, so 10.0.5.45 sends a RST.</p><p>If the server is under your control, try capturing on both the client and server simultaneously. Either:</p><ol><li>The sequence number in the SYN packet from the client is being changed by an interconnecting device, and the server is responding to this changed sequence number, or</li><li>The acknowledgment number in the SYN/ACK packet from the server is being changed by an interconnecting device, or</li><li>Something has gone wrong with the server's TCP/IP stack and it is responding with the wrong acknowledgment number.</li></ol><p>You might check the configuration of your Sonicwall firewall to see if it is mangling sequence and/or acknowledgment numbers. If you can, try capturing the same communication on both sides of the firewall simultaneously so that you can see what, if anything, is changed as packets pass through the firewall.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '13, 21:40</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-23890" class="comments-container"></div><div id="comment-tools-23890" class="comment-tools"></div><div class="clear"></div><div id="comment-23890-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24960"></span>

<div id="answer-container-24960" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24960-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I have seen an issue which looks like multi-pathing problems on an Amazon EC2 VM with a 3.4.x kernel and a proper network config ... it's not always the firewall :) The bug is that the kernel sends the wrong TCP sequence number to the client in the SYN_ACK packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Sep '13, 09:47</strong></p><img src="https://secure.gravatar.com/avatar/27eeb3a12dcb160480c0b037fa2619f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dave%20Crooke&#39;s gravatar image" /><p>Dave Crooke<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dave Crooke has no accepted answers">0%</span></p></div></div><div id="comments-container-24960" class="comments-container"></div><div id="comment-tools-24960" class="comment-tools"></div><div class="clear"></div><div id="comment-24960-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

