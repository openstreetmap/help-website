+++
type = "question"
title = "Cannot capture packets exchanged between Qt Server and Clients"
description = '''Hello, I’m rather fresh with socket programming, and right now I needed some guidance as to where I should start tackling this problem. To put it short, are there any scenarios where WireShark can fail to capture packets from and to a local machine? We have a pair of Simple TCP Server/Client written...'''
date = "2014-05-09T06:35:00Z"
lastmod = "2014-05-12T09:04:00Z"
weight = 32664
keywords = [ "qt5", "qt" ]
aliases = [ "/questions/32664" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Cannot capture packets exchanged between Qt Server and Clients](/questions/32664/cannot-capture-packets-exchanged-between-qt-server-and-clients)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32664-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32664-score" class="post-score" title="current number of votes">0</div><span id="post-32664-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I’m rather fresh with socket programming, and right now I needed some guidance as to where I should start tackling this problem.</p><p>To put it short, are there any scenarios where WireShark can fail to capture packets from and to a local machine?</p><p>We have a pair of Simple TCP Server/Client written with Qt5, using QTcpSocket and QTcpServer. These Qt server and client, both running locally on my own PC, can send strings of text to each other.</p><p>The strange thing is, WireShark can’t seem to capture any packets exchanged between the Qt server and client. I’m pretty sure the packets are there if the server and client managed to receive data from each other, and I can use RawCap to sniff those packets as well.</p><p>I’ve tried writing another server using a WinSock2 socket instead of the QTcpSocket , and still, WireShark can’t detect any packets when the server and client have successfully exchanged data with each other.</p><p>I’ve seen many people using WireShark with their network apps on the Qt forum, so the possibility of WireShark not being compatible with Qt seems quite slim. I also made sure that I’m running with an Administrator account, and the server and client are allowed through my firewall as well. My Ethernet adapter is that of Realtek PCI GBE Family Controller, and the driver is up to date.</p><p>I did read from the FAQ of WireShark, though, that WinPcap might not capture packets with erroneous CRC. Still, by my understanding (correct me if I’m wrong), the CRC is something handled by the Ethernet adapter hardware, and since I can capture mostly all other packets through this same Ethernet Interface with WireShark, that also seems unlikely.</p><p>Is there anything else I can try to have WireShark capture the activities between my server and client?</p><p>Ingrid</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-qt5" rel="tag" title="see questions tagged &#39;qt5&#39;">qt5</span> <span class="post-tag tag-link-qt" rel="tag" title="see questions tagged &#39;qt&#39;">qt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '14, 06:35</strong></p><img src="https://secure.gravatar.com/avatar/557fe8c1fda95d7499d7a5975a8a4c08?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ingridwu&#39;s gravatar image" /><p><span>ingridwu</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ingridwu has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 May '14, 09:03</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-32664" class="comments-container"></div><div id="comment-tools-32664" class="comment-tools"></div><div class="clear"></div><div id="comment-32664-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32669"></span>

<div id="answer-container-32669" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32669-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32669-score" class="post-score" title="current number of votes">2</div><span id="post-32669-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ingridwu has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>These Qt <strong>server and client, both running locally</strong> on my own PC</p></blockquote><p>That's the problem, if you are running the software on the same Windows system.</p><p>Reason: <strong>WinPcap cannot capture localhost traffic</strong>, which is traffic that does not 'physically' leave the system.</p><p>For that case you can use <a href="http://www.netresec.com/?page=RawCap">RawCap</a> to capture the traffic and then user Wireshark to analyze it.</p><p>If you did your test on Linux, Unix, *BSD, please capture on the <strong>loopback interface</strong> (lo, lo0, etc.).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '14, 10:59</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-32669" class="comments-container"><span id="32721"></span><div id="comment-32721" class="comment"><div id="post-32721-score" class="comment-score"></div><div class="comment-text"><p>Okay. Thanks for clearing that up. I guess I will either test the server and client on separate machines, or use RawCap whenever I have them both on a local machine.</p></div><div id="comment-32721-info" class="comment-info"><span class="comment-age">(12 May '14, 01:00)</span> <span class="comment-user userinfo">ingridwu</span></div></div><span id="32732"></span><div id="comment-32732" class="comment"><div id="post-32732-score" class="comment-score"></div><div class="comment-text"><p><span>@ingridwu</span></p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer, do not change the answer title to include [solved]. Please read the FAQ for more information.</p></div><div id="comment-32732-info" class="comment-info"><span class="comment-age">(12 May '14, 09:04)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-32669" class="comment-tools"></div><div class="clear"></div><div id="comment-32669-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

