+++
type = "question"
title = "Bad TCP Connection closure detection"
description = '''I am investigating an issue on a network at the moment and although I have found the issue, it has highlighted a behavior in Wireshark that I hope someone can explain to me. I can&#x27;t post the pcap as its quite large and contains sensitive data, but the sttached screenshot of the TCP information shoul...'''
date = "2014-02-04T01:04:00Z"
lastmod = "2014-02-04T01:58:00Z"
weight = 29417
keywords = [ "expert-info", "tshark", "tcp", "retransmissions" ]
aliases = [ "/questions/29417" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Bad TCP Connection closure detection](/questions/29417/bad-tcp-connection-closure-detection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29417-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am investigating an issue on a network at the moment and although I have found the issue, it has highlighted a behavior in Wireshark that I hope someone can explain to me. I can't post the pcap as its quite large and contains sensitive data, but the sttached screenshot of the TCP information should help. On this, we are looking at treams with index 0 &amp; 1. <img src="https://osqa-ask.wireshark.org/upfiles/tcp-bug.PNG" alt="alt text" /> You can see that the TCP handshake sets up correctly, and a small amount of data is sent and ACKed in both directions. Then the server sends a [FIN, ACK], but gets no response. Wireshark correctly detects the retransmission of the [FIN, ACK] packets as shown in the screenshot.</p><p>As these 'bad clients' have caused issues with the server by not ACKing the [FIN, ACK] packet in the past, I am trying to script the detection of these occurances using tshark.</p><p>However if I run the same file through tshark like this:</p><blockquote><p>tshark -r bad-tcp-2.cap -R 'expert.message == "Retransmission (suspected)"'</p></blockquote><p>it doesn't find any of these retransmissions.</p><p>Is this a bug in Tshark, or an expected difference in behavior, or just something I am doing wrong int he first place?</p></div><div id="question-tags" class="tags-container tags">expert-info tshark tcp retransmissions</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '14, 01:04</strong></p><img src="https://secure.gravatar.com/avatar/13434718a8ed6f82f6c90be14d9acec6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Boidy&#39;s gravatar image" /><p>Boidy<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Boidy has no accepted answers">0%</span></p></img></div></div><div id="comments-container-29417" class="comments-container"><span id="29423"></span><div id="comment-29423" class="comment"><div id="post-29423-score" class="comment-score"></div><div class="comment-text"><p>I appreciate this isn't a support forum for Cascade Pilot, but I can't get that to detect these retransmissions either.</p></div><div id="comment-29423-info" class="comment-info"><span class="comment-age">(04 Feb '14, 03:41)</span> Boidy</div></div></div><div id="comment-tools-29417" class="comment-tools"></div><div class="clear"></div><div id="comment-29417-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29419"></span>

<div id="answer-container-29419" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29419-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please try to run tshark with option -2 (two pass analysis) and</p><blockquote><p>-R 'expert.message <strong>contains</strong> "Retransmission (suspected)"'</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '14, 01:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Feb '14, 02:02</p></div></div><div id="comments-container-29419" class="comments-container"><span id="29422"></span><div id="comment-29422" class="comment"><div id="post-29422-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your response. The version of Tshark I had installed on the box doesn't support '-2', and its not a trivial job to upgrade it. I put the test pcap file on another platform with the latest Tshark, and your suggestion worked. Surprisingly, running it without -2 and with a -Y option set instead of -R, also found the packets. So I'm guessing that there is bug in the version of TShark I have on my server.</p></div><div id="comment-29422-info" class="comment-info"><span class="comment-age">(04 Feb '14, 03:15)</span> Boidy</div></div></div><div id="comment-tools-29419" class="comment-tools"></div><div class="clear"></div><div id="comment-29419-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

