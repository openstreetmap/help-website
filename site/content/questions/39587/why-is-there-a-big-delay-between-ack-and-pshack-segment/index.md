+++
type = "question"
title = "why is there a big delay between ACK and [PSH,ACK] segment"
description = '''Hello, In my wireshark capture I am seeing a delay of approximately 3 seconds between ACK segment and [PSH,ACK] having the same sequence numbers. I am trying to understand why is this delay of the 3 seconds because our application cannot tolerate such big delays. However, elsewhere in the wireshark ...'''
date = "2015-02-02T17:40:00Z"
lastmod = "2015-02-03T02:40:00Z"
weight = 39587
keywords = [ "delay", "retransmission" ]
aliases = [ "/questions/39587" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [why is there a big delay between ACK and \[PSH,ACK\] segment](/questions/39587/why-is-there-a-big-delay-between-ack-and-pshack-segment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39587-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, In my wireshark capture I am seeing a delay of approximately 3 seconds between ACK segment and [PSH,ACK] having the same sequence numbers. I am trying to understand why is this delay of the 3 seconds because our application cannot tolerate such big delays. However, elsewhere in the wireshark trace I have seen a delays little above 1 second between the ACK and [PSH,ACK] segments. Pasting the wireshark trace here.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/w2.png" alt="alt text" /></p><p>As you can see from the above the picture frame 3140 and frame 3146 are having the same sequence number, frame 3146 gets transmitted after approx. 1 second. In between those frames there were retransmissions whose RTOs in the wireshark was 9 seconds. I was wondering initially these retransmissions would affect the connection between 192.168.21.31 and 192.168.21.41. I have seen a similar packets exchange except this time between the ACK and [PSH,ACK] of the same sequence number there is a delay of 3 seconds. Attached is the picture of the delay of 3 seconds.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/w1.png" alt="alt text" /></p><p>From the above picture frame 4303 is having the same sequence number as the frame 4300. Could the retransmissions in between the frames 4300 and 4303 can cause this delay. If so, why there was no delay in the first picture between frames 3140 and 3146. Are the retransmissions between the frames affecting the RTO between 192.168.21.31 and 192.168.21.41.?</p><pre><code>192.168.21.31  - Linux box
192.168.21.41  - Windows 7 PC</code></pre>Can experts help me understand this problem.<p>Thank you so much DP</p></div><div id="question-tags" class="tags-container tags">delay retransmission</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Feb '15, 17:40</strong></p><img src="https://secure.gravatar.com/avatar/180026b97aa308ecc6a3b10e521bedc6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DPnetwork&#39;s gravatar image" /><p>DPnetwork<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DPnetwork has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 03 Feb '15, 02:34</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></img></div></div><div id="comments-container-39587" class="comments-container"></div><div id="comment-tools-39587" class="comment-tools"></div><div class="clear"></div><div id="comment-39587-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39594"></span>

<div id="answer-container-39594" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39594-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It seems you are capturing on the windows PC (192.168.21.41) or at least on a span port copying the traffic from the port on which this PC is attached.</p><p>If this is true, then the only conclusion you can draw from the captured data is that the process responsible for this connection is taking 1s (or 3s in the second example) to respond. Either the PC is very busy and the process does not get enough priority or the process needs time to come up with the response. Are there any secondary connections like a DB connection? Or is there much disk IO involved?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '15, 02:40</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-39594" class="comments-container"><span id="39612"></span><div id="comment-39612" class="comment"><div id="post-39612-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the response SYN-bit.</p><p>There is no DB connection in this application. I am still not ruling out CPU being busy because of disk IO or the application is waiting for something. the 1 second or 3 second delay happened on the Linux(192.168.21.31) not on the Windows PC(192.168.21.41).</p><p>These are the question I have. a) Did the 1 second delay in frame 3146 caused the increase in delay in frame 4303? I am just wondering if this 1 second delay is called the RTO between 192.168.21.31 and 192.168.21.41. if so, did the RTO bumped in the frame 4300. Because the delays I understand change 1, 3, 6,12,24... b) Whenever this delays happened there will always be TCP retransmissions like frame 4301 in second case also frame 3141, 3143 in second case whos RTOs are like 8 or 9 seconds. I am just wondering whether the RTOs in the retransmissions affected the RTO between 192.xx.xx.31 and 192.xx.xx.41 connection. I read somewhere RTOs vary between each TCP connection, so if so it should not. I just want to confirm. Again I will look into if the CPU being busy will cause this problem. But, I want to understand if this is caused from the network behavior.</p><p>Thanks again. DineshP</p></div><div id="comment-39612-info" class="comment-info"><span class="comment-age">(03 Feb '15, 10:23)</span> DPnetwork</div></div></div><div id="comment-tools-39594" class="comment-tools"></div><div class="clear"></div><div id="comment-39594-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

