+++
type = "question"
title = "a 30+ second delay"
description = '''I have a linux server which I test by sending thousands of calls to get a JS file. The problem is that every few hundreds (sometimes thousands) calls, I get a delay of ~30 seconds. It happens only when the client is OSX (never on windows). Attached is a wireshark capture of two consecutive sessions....'''
date = "2014-11-19T00:36:00Z"
lastmod = "2014-11-20T02:00:00Z"
weight = 37958
keywords = [ "latency", "tcp" ]
aliases = [ "/questions/37958" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [a 30+ second delay](/questions/37958/a-30-second-delay)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37958-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a linux server which I test by sending thousands of calls to get a JS file. The problem is that every few hundreds (sometimes thousands) calls, I get a delay of ~30 seconds. It happens only when the client is OSX (never on windows). Attached is a wireshark capture of two consecutive sessions. I've noticed that while the port number of the second session's SYN request (Frame 12) is 55295, the destination port of the SYN-ACK (Frame 13) is 55199, the port of the first session. I guess that's why when the server sends SYN-ACK he gets RST, because the client already closed the first session. As for the second session, because the client did not receive the SYN-ACK, it keeps retransmitting SYN. Did I get it right? What can be a solution on the server side? <a href="http://i.stack.imgur.com/eZezJ.png">http://i.stack.imgur.com/eZezJ.png</a> <img src="http://i.stack.imgur.com/eZezJ.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">latency tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '14, 00:36</strong></p><img src="https://secure.gravatar.com/avatar/236c4658f28665a5fc01b59bc5b75cea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Eran%20Raichel&#39;s gravatar image" /><p>Eran Raichel<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Eran Raichel has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 19 Nov '14, 00:46</p></div></div><div id="comments-container-37958" class="comments-container"><span id="37969"></span><div id="comment-37969" class="comment"><div id="post-37969-score" class="comment-score"></div><div class="comment-text"><p>Hi,If you see on packet no. 12 client sends syn request and after mulitple retransmissions in packet no. 40 after 36 seconds server responds with syn ack.So if possible do capture on both ends to have more precise answer.</p></div><div id="comment-37969-info" class="comment-info"><span class="comment-age">(19 Nov '14, 06:38)</span> kishan pandey</div></div></div><div id="comment-tools-37958" class="comment-tools"></div><div class="clear"></div><div id="comment-37958-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38004"></span>

<div id="answer-container-38004" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38004-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Frame #13 (and the consecutive re-transmissions of it) is the problem.</p><p>As you can see, that frame contains the same SYN-ACK of frame #2, <strong>however</strong> with a totally wrong SEQ/ACK number. It should be SEQ=0, ACK=1. What we see is SEQ=69452, ACK=367003392. That's wrong and that's the reason why Wireshark flags the frame and why the receiver sends a RESET. The reson for this behaviour is unclear and you won't find it in the capture file. Maybe the system itself (38.126.142.158) has a problem or a device "on the way" alter (or generates) those frames, like a firewall, load balancer, wan accelerator, etc.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '14, 02:00</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-38004" class="comments-container"><span id="38005"></span><div id="comment-38005" class="comment"><div id="post-38005-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt for your answer, I also see that the seq/ack are wrong. what about the wrong destination port? any idea? BTW, this is how it looks with absolute seq numbers: <img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2014-11-20_at_12.04.46.png" alt="alt text" /></p><p>And this is the TCP session (port 55199) that was used a few seconds before, been closed, but for some reason the server uses it to send the SYN, ACK <img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2014-11-20_at_12.05.28.png" alt="alt text" /></p></div><div id="comment-38005-info" class="comment-info"><span class="comment-age">(20 Nov '14, 02:09)</span> Eran Raichel</div></div><span id="38006"></span><div id="comment-38006" class="comment"><div id="post-38006-score" class="comment-score"></div><div class="comment-text"><blockquote><p>what about the wrong destination port? any idea?</p></blockquote><p>As I said. You won't find the <strong>reason</strong> for that behaviour in the capture file. It could be one of the things I mentioned.</p><p>And the wrong SYN-ACK isn't necessarily a response to the second SYN (port 55294). Maybe it's just a resend of the original SYN-ACK (port 55199) and then there is no "wrong destination port" ;-)</p></div><div id="comment-38006-info" class="comment-info"><span class="comment-age">(20 Nov '14, 02:14)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-38004" class="comment-tools"></div><div class="clear"></div><div id="comment-38004-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

