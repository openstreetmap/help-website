+++
type = "question"
title = "The wireshark for retransmission judgment mechanism"
description = '''hi： my wireshark version is Version 1.8.6 (SVN Rev 48142 from /trunk-1.8) Found in the analysis of the data package software for TCP retransmission judgment problems, can help explain whether the software is how to determine the retransmission. How do I upload the data packet to the forum？ Thank you...'''
date = "2013-03-25T06:41:00Z"
lastmod = "2013-03-25T07:11:00Z"
weight = 19806
keywords = [ "retransmission" ]
aliases = [ "/questions/19806" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [The wireshark for retransmission judgment mechanism](/questions/19806/the-wireshark-for-retransmission-judgment-mechanism)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19806-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi： my wireshark version is Version 1.8.6 (SVN Rev 48142 from /trunk-1.8) Found in the analysis of the data package software for TCP retransmission judgment problems, can help explain whether the software is how to determine the retransmission.</p><p>How do I upload the data packet to the forum？</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">retransmission</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Mar '13, 06:41</strong></p><img src="https://secure.gravatar.com/avatar/c66d8077ef5f4d265694332542e2fbd4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mengsunny&#39;s gravatar image" /><p>mengsunny<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mengsunny has no accepted answers">0%</span></p></div></div><div id="comments-container-19806" class="comments-container"><span id="19807"></span><div id="comment-19807" class="comment"><div id="post-19807-score" class="comment-score"></div><div class="comment-text"><p>You can use <a href="http://www.cloudshark.org">http://www.cloudshark.org</a> and post the URL here.</p></div><div id="comment-19807-info" class="comment-info"><span class="comment-age">(25 Mar '13, 06:43)</span> Jasper ♦♦</div></div><span id="19809"></span><div id="comment-19809" class="comment"><div id="post-19809-score" class="comment-score"></div><div class="comment-text"><p><a href="http://www.cloudshark.org/captures/099a3ae7d9e8">http://www.cloudshark.org/captures/099a3ae7d9e8</a></p><p>Packets have uploaded</p></div><div id="comment-19809-info" class="comment-info"><span class="comment-age">(25 Mar '13, 06:49)</span> mengsunny</div></div><span id="19810"></span><div id="comment-19810" class="comment"><div id="post-19810-score" class="comment-score"></div><div class="comment-text"><p>Whether the software will only compare the TCP sequence and acknowledgment numbers, rather than see if the TCP data content exists</p></div><div id="comment-19810-info" class="comment-info"><span class="comment-age">(25 Mar '13, 06:57)</span> mengsunny</div></div></div><div id="comment-tools-19806" class="comment-tools"></div><div class="clear"></div><div id="comment-19806-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19812"></span>

<div id="answer-container-19812" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19812-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark will compare Sequence and Acknowledge numbers, and will NOT care about what the TCP data content actually is. That's what checksums are for: making sure that the received data in the packet is what the sender was sending out.</p><p>By the way, your trace is kinda strange. It shows that port numbers are reused within about 4 seconds from SYN to SYN (Packets 1, 19, 46...). This is not good, which means that the node with IP 202.107.238.218 is probably doing something very wrong. Whatever the reason why the node does, it will most likely lead to chaos.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '13, 07:11</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Mar '13, 07:13</p></div></div><div id="comments-container-19812" class="comments-container"><span id="19813"></span><div id="comment-19813" class="comment"><div id="post-19813-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your explanation, this is a problem being analyzed, found that frequent client to reuse socket, but the server will still accept the connection, communication, there are some problems.</p><p>RFC1122 When a connection is closed actively, it MUST linger in TIME-WAIT state for a time 2xMSL (Maximum Segment Lifetime). However, it MAY accept a new SYN from the remote TCP to reopen the connection directly from TIME-WAIT state, if it: (1) assigns its initial sequence number for the new connection to be larger than the largest sequence number it used on the previous connection incarnation,and (2) returns to TIME-WAIT state if the SYN turns out to be an old duplicate.</p><p>Obviously, my analysis of the problem does not meet this requirement, but can not explain why the connection is established successfully</p></div><div id="comment-19813-info" class="comment-info"><span class="comment-age">(25 Mar '13, 07:25)</span> mengsunny</div></div><span id="19814"></span><div id="comment-19814" class="comment"><div id="post-19814-score" class="comment-score"></div><div class="comment-text"><p>By the way, the client equipment and SSL connection establishment, rather than a real web server</p></div><div id="comment-19814-info" class="comment-info"><span class="comment-age">(25 Mar '13, 07:31)</span> mengsunny</div></div><span id="19815"></span><div id="comment-19815" class="comment"><div id="post-19815-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-19815-info" class="comment-info"><span class="comment-age">(25 Mar '13, 07:35)</span> grahamb ♦</div></div></div><div id="comment-tools-19812" class="comment-tools"></div><div class="clear"></div><div id="comment-19812-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

