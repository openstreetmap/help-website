+++
type = "question"
title = "Just finished troubleshooting and 101... A question about All Access Pass and the next steps"
description = '''Hi everyone, These past 2 weeks have been an amazing journey for me. I have been working in IT for about 15 years and I have had my occasional brushes with Wireshark in my past but apart from collecting a quick packet capture to send to a third party or inefficiently try and decipher each line for s...'''
date = "2014-04-22T13:42:00Z"
lastmod = "2014-04-22T14:54:00Z"
weight = 32069
keywords = [ "access", "captures", "all", "books", "pass" ]
aliases = [ "/questions/32069" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Just finished troubleshooting and 101... A question about All Access Pass and the next steps](/questions/32069/just-finished-troubleshooting-and-101-a-question-about-all-access-pass-and-the-next-steps)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32069-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone,</p><p>These past 2 weeks have been an amazing journey for me. I have been working in IT for about 15 years and I have had my occasional brushes with Wireshark in my past but apart from collecting a quick packet capture to send to a third party or inefficiently try and decipher each line for some sense in what is going on. One thing i did know is that I realized I really didn't know my stuff on Wireshark.</p><p>I decided to take the plunge 2 weeks ago. I purchased the Wireshark 101 , Troubleshooting Performance and the Network Analysis Second Edition from Amazon. I have been hooked and have finished 101 last week and Troubleshooting yesterday. The books have been amazing! Thank you Laura!</p><p>I am still a bit unsure about a few things like SACK, Retransmissions and the != but I am sure going over the materials again and using the skills practically I will become better versed.</p><p>Now I am thinking what is next? I am looking at a network issue but more on this shortly...</p><p>I would like to become a better versed in Wireshark and also work towards becoming certified. Being based in the UK has anyone else got the WCNA? Is there any UK Wireshark Gurus?</p><p>What is the next best step for someone who cannot afford thousands for a course? Is the all Access Pass the best thing to go for if I want to try and towards a WCNA? Can someone give me some advice as the next best steps please?</p><p>In my work I am currently looking at a network issues which my company has had for many years. The network comprises of our main office connecting via MPLS to our datacentre 100 miles away. Users connect to the internet via a transparent Scansafe proxy which is based in the data centre and the internet breakout point again is in a different datacentre.</p><p>If i remotely connect to the proxy and test net performance I get about 8MB/s when I connect to that proxy from another machine in the same subnet I still get the 8MB. As soon as I connect from a machine in the Main office speeds go down to 700KB/s. This is not just internet traffic it is all traffic SMB as well.</p><p>With third parties all pointing the finger at each other (The MPLS to the firewall network guying) I have been quietly collecting packet captures and analysing them from the client and Proxy.</p><p>My captures were taken on the client and on the proxy with no taps or port spanning used. I am getting allot of errors ...in a 6 minute capture of 500MB: 34 Acknowledgment number: Broken TCP. The acknowledge is nonzero. 26 out of order segments 20 acked segment that wasn't captured 25 previous segment not captured. 16 window is full 15 Zero Window</p><p>Note show 754 retransmissions, 37 fast retranmissions I could go on.</p><p>The client capture is not as bad ..36 ack segment wasnt captured and 5 previous segment not captured.. 219 retransmissions and many duplicate acks and keep alive.</p><p>With my inexperience I am just overwhelmed with a capture file that has the majority of the books problems all in one capture. I think it is a dodgy switch because I think too many packets are being dropped in such a short time ..or is it short? what is an exceptible number? Packets out of order and retransmissions make me think about the switch but the window full and zero window is it something else. How do i address and what are my steps of attack?</p><p>I have looked at the graphs and couldn't see any correlation from the traffic and the tcp.analysis.flag &amp;&amp; !tcp.analysis.window.update but I have about 1503 out of 510217.</p><p>I have decided to ask the mpls guys for a capture tomorrow in the hope to see something there in the hope to narrow down my search but I am really unsure about my next steps.</p><p>Can any network guru give me some tips as I have filled in the checklist pdf but with a checklist with allot going wrong ...where do i begin?</p><p>Many thanks for all your time in reading my mail.</p><p>Jazz</p></div><div id="question-tags" class="tags-container tags">access captures all books pass</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '14, 13:42</strong></p><img src="https://secure.gravatar.com/avatar/1de54471a0cc95cb8604b875d49fe7e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yoyomonkey&#39;s gravatar image" /><p>yoyomonkey<br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yoyomonkey has no accepted answers">0%</span></p></div></div><div id="comments-container-32069" class="comments-container"></div><div id="comment-tools-32069" class="comment-tools"></div><div class="clear"></div><div id="comment-32069-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32070"></span>

<div id="answer-container-32070" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32070-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You always begin with the basics.</p><p>Before taking the test finish reading Network Analysis and don't skip the practice questions. I would also advice to look at other books like The TCP/IP Guide or Internet Core Protocols.. Don't forget to check out the presentations from previous Sharkfests. For the WCNA you can use the Exam Prep Guide.</p><p>In regards to the other question, focus on one source and one destination (please don't test with SMB) and if the network diagram is similar to the one below you have to start the packet capture (simultaneously) on the firewalls or as close to the MPLS routers as possible. Then you can see if the issue is in your network or the ISP.</p><pre><code>PC in HQ - Firewall - MPLS Router - ISP - MPLS router - Firewall - Proxy in DC</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '14, 14:54</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p>Roland<br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-32070" class="comments-container"><span id="32075"></span><div id="comment-32075" class="comment"><div id="post-32075-score" class="comment-score"></div><div class="comment-text"><p>Thank you do much sir for your advice and help.I have made a start in the network analysis book.</p><p>I did ask the network guys fie packet captures on the firewall who also said they could only.provide this by plugging a a laptop into the firewall</p><p>I am worried about this as the throughout of days is high and if they are spanning ports or using a tap they may lose packets from the capture obscuring the problem further?</p><p>The books you recommend I will get them ordered from Amazon who are the authors please?</p><p>Is the access pass worth the 699 and should I wait till after I have covered the network analysis or do they go hand in hand.</p><p>Thanks again for all your advice and help I know I am a very long way off the wcna but with your help I have something to aim for :)</p><p>Cheers</p><p>Jazz</p></div><div id="comment-32075-info" class="comment-info"><span class="comment-age">(22 Apr '14, 18:07)</span> yoyomonkey</div></div><span id="32076"></span><div id="comment-32076" class="comment"><div id="post-32076-score" class="comment-score"></div><div class="comment-text"><p>FYI, I just converted your 'answer' to a 'comment'. To respond to an answer you can use the text box that has 'comment' next to it. The bottom text box is for posting an answer to the question.</p></div><div id="comment-32076-info" class="comment-info"><span class="comment-age">(22 Apr '14, 19:05)</span> Quadratic</div></div><span id="32100"></span><div id="comment-32100" class="comment"><div id="post-32100-score" class="comment-score"></div><div class="comment-text"><p>Oh apologies and thanks for correcting this for me quadratic. cheers jazz</p></div><div id="comment-32100-info" class="comment-info"><span class="comment-age">(23 Apr '14, 07:21)</span> yoyomonkey</div></div><span id="32187"></span><div id="comment-32187" class="comment"><div id="post-32187-score" class="comment-score"></div><div class="comment-text"><p>I don't know what firewalls you are using but most of them have an option to capture packets. You can read the TCP/IP Guide for free online and the other book was written by Eric Hall. A lot of information is free so I would not spend money unless it's necessary. Keep practicing.</p></div><div id="comment-32187-info" class="comment-info"><span class="comment-age">(26 Apr '14, 06:09)</span> Roland</div></div></div><div id="comment-tools-32070" class="comment-tools"></div><div class="clear"></div><div id="comment-32070-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

