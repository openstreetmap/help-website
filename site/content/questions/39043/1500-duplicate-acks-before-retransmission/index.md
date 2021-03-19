+++
type = "question"
title = "1500+ Duplicate Ack&#x27;s before retransmission."
description = '''Hi All. I&#x27;m investigating some network slowness. As a part of this I&#x27;m checking the pcaps of file transfers around my network. I&#x27;m seeing 4/5 instances of packet loss per file transfer (regardless of size??) and in each instance there is a large number of duplicate acks being sent before a retransmi...'''
date = "2015-01-11T06:17:00Z"
lastmod = "2015-01-11T07:27:00Z"
weight = 39043
keywords = [ "duplicate", "retransmissions" ]
aliases = [ "/questions/39043" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [1500+ Duplicate Ack's before retransmission.](/questions/39043/1500-duplicate-acks-before-retransmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39043-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All.</p><p>I'm investigating some network slowness. As a part of this I'm checking the pcaps of file transfers around my network. I'm seeing 4/5 instances of packet loss per file transfer (regardless of size??) and in each instance there is a large number of duplicate acks being sent before a retransmission is received. Image: <a href="http://imgur.com/d17qXQD">Image</a></p><p>In the capture I'm looking at at the moment there are 1763 acks sent before receiving a response.</p><p>Anyone know if this is normal or what I should focus on next?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">duplicate retransmissions</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jan '15, 06:17</strong></p><img src="https://secure.gravatar.com/avatar/87f6f1ddaab2f208c791681a051b2de6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CarlitoGrey&#39;s gravatar image" /><p>CarlitoGrey<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CarlitoGrey has no accepted answers">0%</span></p></div></div><div id="comments-container-39043" class="comments-container"></div><div id="comment-tools-39043" class="comment-tools"></div><div class="clear"></div><div id="comment-39043-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39044"></span>

<div id="answer-container-39044" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39044-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like classic <a href="http://en.wikipedia.org/wiki/Bufferbloat">buffer bloating</a> to me. The problem appears when you send large amounts of data from a high speed network to a lesser speed network real fast, causing the switch or router buffers to fill up. At that point, packet loss will occur, and the receiver will send duplicate ACKs to notify the sender of the missing segment(s).</p><p>The problem is: since the full buffer is still constantly slammed with more packets the retransmission can't get through fast but has to "get in line" like all the other packets, which means that it takes a long time to get to the receiver. That's the reason why you see very high numbers of duplicate ACKs for the same missing segment.</p><p>The only thing you can do is to have the receiver advertise a smaller receive window, to prevent overloading the network.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jan '15, 07:27</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Jan '15, 07:28</p></div></div><div id="comments-container-39044" class="comments-container"><span id="39050"></span><div id="comment-39050" class="comment"><div id="post-39050-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer and link to the article - makes sense to me (I'm not a networking guy, just a security guy fed up with the network speed when I know how decent the back end equipment is).</p><p>There's only one switch (well a stack) between the client and the server I'm interpreting that to be that the server is filling the switch stack's buffer at 1Gbps, not knowing the client is connected to the switch at 10Mbps.</p><p>I'll pass this on to the 'networking' guys.</p></div><div id="comment-39050-info" class="comment-info"><span class="comment-age">(11 Jan '15, 09:05)</span> CarlitoGrey</div></div><span id="39051"></span><div id="comment-39051" class="comment"><div id="post-39051-score" class="comment-score"></div><div class="comment-text"><p>Woah, 1Gbps down to 10MBbs? That's a nightmare - factor 100 slowdown, no wonder the buffers are exploding :-)</p></div><div id="comment-39051-info" class="comment-info"><span class="comment-age">(11 Jan '15, 09:12)</span> Jasper ♦♦</div></div><span id="39054"></span><div id="comment-39054" class="comment"><div id="post-39054-score" class="comment-score"></div><div class="comment-text"><p>Actually the virtual hosts have four 1Gbps links teamed together. Am I right in thinking they can in theory transfer data at 4gbps? The clients have a Nortel IP phone between them and the switch, the phone only supports 10mbps :(.</p><p>I've enabled discarded packets on PRTG and I can see packets being dropped for the link I'm using.</p><p>Would the output buffer be shared between all ports on a switch (cisco 3750's in a stack)? If so would transferring a large amount of data between myself and the server also cause the switch to drop packets for other destinations in the output buffer?</p></div><div id="comment-39054-info" class="comment-info"><span class="comment-age">(11 Jan '15, 10:01)</span> CarlitoGrey</div></div><span id="39055"></span><div id="comment-39055" class="comment"><div id="post-39055-score" class="comment-score"></div><div class="comment-text"><p>In theory, yes, up to 4GPs, but not for a single TCP connection - for that the maximum is one physical link.</p><p>Anyway, you should really come up with a plan to remove the 10MBps point of failure as soon as you can - I know this is often easier said when done, but 10MBps is too slow for current networks.</p><p>The buffer architecture depends on the switch model - some have a "big" common buffer for all ports, others have small dedicated buffers per port. AFAIK Cisco has 100KByte buffers per port, so you'll overrun them with your kind of problem almost instantaneously.</p><p>It may still affect other ports as well, which is kinda hard to say - I'm not sure how the switch deals with that kind of overload precisely.</p></div><div id="comment-39055-info" class="comment-info"><span class="comment-age">(11 Jan '15, 10:07)</span> Jasper ♦♦</div></div></div><div id="comment-tools-39044" class="comment-tools"></div><div class="clear"></div><div id="comment-39044-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

