+++
type = "question"
title = "Wireshark display TCP ack number in TCP header"
description = '''Got a pcap file where a telnet client was talking to a strange TCP server. Packet 7 is an ack packet but its ACK number is not displayed correctly by Wireshark. Granted that the strange server itself has some problems. The Wireshark is 1.10.6, but I tried Wireshark 2.0 and it has the same issue. Can...'''
date = "2016-05-24T12:27:00Z"
lastmod = "2016-05-24T14:09:00Z"
weight = 52870
keywords = [ "wireshark" ]
aliases = [ "/questions/52870" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark display TCP ack number in TCP header](/questions/52870/wireshark-display-tcp-ack-number-in-tcp-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52870-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Got a <a href="https://www.dropbox.com/s/bww4upc5it8gbvs/tcp_ack_wrong.pcap">pcap file</a> where a telnet client was talking to a strange TCP server. Packet 7 is an ack packet but its ACK number is not displayed correctly by Wireshark. Granted that the strange server itself has some problems.</p><p>The Wireshark is 1.10.6, but I tried Wireshark 2.0 and it has the same issue.</p><p>Can some confirm?</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 May '16, 12:27</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p>pktUser1001<br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-52870" class="comments-container"></div><div id="comment-tools-52870" class="comment-tools"></div><div class="clear"></div><div id="comment-52870-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="52875"></span>

<div id="answer-container-52875" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52875-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark was using relative seq number for the previous packets, this confused me why Wireshark switched to absolutely seq number display. Turned out the TCP header length for packet 7 was set to be 24 even though there are only 20 bytes available (according to IP total length). After fixing this issue on the crazy server, it's ok now.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '16, 14:09</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p>pktUser1001<br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-52875" class="comments-container"></div><div id="comment-tools-52875" class="comment-tools"></div><div class="clear"></div><div id="comment-52875-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52872"></span>

<div id="answer-container-52872" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52872-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks good to me - the packet is having some issues with the various length values, but the ACK number is fine. Unless you use relative sequence numbers - because then it seems that Wireshark doesn't calculate the relative number and uses absolute values instead. I'm not sure why though.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '16, 13:24</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-52872" class="comments-container"><span id="52876"></span><div id="comment-52876" class="comment"><div id="post-52876-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the comment, wireshark was using relative seq no.</p></div><div id="comment-52876-info" class="comment-info"><span class="comment-age">(24 May '16, 14:10)</span> pktUser1001</div></div></div><div id="comment-tools-52872" class="comment-tools"></div><div class="clear"></div><div id="comment-52872-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

