+++
type = "question"
title = "capture filter for duplicate ack on packet"
description = '''I am able to use the filter on tcp.analysis.duplicate_ack_num to filter for duplicate packets. I need to translate to allow me to use this filter on a bluecoat proxy. I am able to use the filter tcp[0xd]&amp;amp;2=2 to locate only SYN packets but, would like to know how to translate it the duplicate pac...'''
date = "2016-01-21T09:15:00Z"
lastmod = "2016-01-21T12:29:00Z"
weight = 49434
keywords = [ "capture-filter" ]
aliases = [ "/questions/49434" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [capture filter for duplicate ack on packet](/questions/49434/capture-filter-for-duplicate-ack-on-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49434-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am able to use the filter on tcp.analysis.duplicate_ack_num to filter for duplicate packets. I need to translate to allow me to use this filter on a bluecoat proxy. I am able to use the filter tcp[0xd]&amp;2=2 to locate only SYN packets but, would like to know how to translate it the duplicate packet to this type of format.</p><p>Direction on how to do it or what the filter is would be greatly appreciated!</p><p>note: update on the title as it should have mentioned the ack versus a duplicate packet.</p></div><div id="question-tags" class="tags-container tags">capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jan '16, 09:15</strong></p><img src="https://secure.gravatar.com/avatar/f206413b6aa2b980cc2d0e3656a31f19?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="polar315&#39;s gravatar image" /><p>polar315<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="polar315 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Jan '16, 09:36</p></div></div><div id="comments-container-49434" class="comments-container"></div><div id="comment-tools-49434" class="comment-tools"></div><div class="clear"></div><div id="comment-49434-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49439"></span>

<div id="answer-container-49439" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49439-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You cannot filter for duplicate ACKs with a capture filter.</p><p>The reason is that Wireshark determines a packet to be a duplicate ACK while examining it with it's TCP expert module. It's basically a calculation that checks dependencies between two or more packets - all of which is not possible for a capture filter, as it's much too slow. Capture filters cannot keep track of the state of a TCP conversation, as it would have to back-buffer packets. And it doesn't even know how long it has to keep them, because the duplicate ACK may be hundreds of packets away.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '16, 12:29</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-49439" class="comments-container"><span id="49452"></span><div id="comment-49452" class="comment"><div id="post-49452-score" class="comment-score"></div><div class="comment-text"><p>I am running a capture filter on tcp.analysis.duplicate_ack &amp;&amp; !tcp.analysis.duplicate_ack_num == 1 during a capture and successfully show the duplicate acks. This is allowing me to grab the duplicate packets without filling my buffers.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/dup-ack.jpg" alt="alt text" /></p></div><div id="comment-49452-info" class="comment-info"><span class="comment-age">(22 Jan '16, 05:54)</span> polar315</div></div><span id="49460"></span><div id="comment-49460" class="comment"><div id="post-49460-score" class="comment-score"></div><div class="comment-text"><p>There is a substantial difference between a <em>display</em> filter and a <em>capture</em> filter.</p><p>@Jasper's has answered to you as (just guessing ;-) ) he's seen the keyword "capture" in the subject of your question; I have seen that you have used the display filter syntax in the body of the question, but I was unable to answer until now.</p><p>Please look at the difference between the two at Wireshark wiki. Next, please re-read this part</p><blockquote><p>I am able to use the filter tcp[0xd]&amp;2=2 to locate only SYN packets but, would like to know how to translate it the duplicate packet to this type of format.</p></blockquote><p>of your question as if you were reading it for the first time, and try to explain better what you want to achieve with the <em>display</em> filter.</p></div><div id="comment-49460-info" class="comment-info"><span class="comment-age">(22 Jan '16, 08:01)</span> sindy</div></div><span id="49462"></span><div id="comment-49462" class="comment"><div id="post-49462-score" class="comment-score"></div><div class="comment-text"><p>Understand the confusion. It is a display filter as all the other packets are still in the capture, but it is only displaying the duplicate acks. So it is not a capture filter I have in place.</p><p>As the Bluecoat pcap has a 100 meg limit and the data will fill that in less than a second I wanted to get a capture filter that would only get the duplicates.</p><p>rock &lt;-me-&gt; hard place.</p><p>Thanks for the clarification.</p></div><div id="comment-49462-info" class="comment-info"><span class="comment-age">(22 Jan '16, 11:10)</span> polar315</div></div><span id="49464"></span><div id="comment-49464" class="comment"><div id="post-49464-score" class="comment-score"></div><div class="comment-text"><p>Well, as you've mentioned that you can set up a capture filter for packets with SYN bit set, I was wondering whether it could be that it was enough for you to identify retransmissions of the initial SYN packets from client through detecting retransmission of (SYN, ACK) from server corresponding to them.</p><p>Because in such case, you could use your <em>capture</em> filter <code>tcp[0xd]&amp;2=2</code> (only guessing that you can use capture filters at the bluecoat, because the way you wrote it I didn't get whether you can get to its shell to run a regular tcpdump there or whether it is an appliance so you can use only some pre-defined capture options), and then use your tcp.analysis.duplicate_ack_num <em>display</em> filter on the resulting file. That way, you would capture only the SYN packets from the client and the (SYN, ACK) ones from the server, where the former would define the absolute sequence numbers so the retransmissions of the latter could be identified as retransmissions. So if the SYN, ACK would get lost on their way to the client, the client would send a new SYN and the SYN,ACK would be identified as a retransmission.</p></div><div id="comment-49464-info" class="comment-info"><span class="comment-age">(22 Jan '16, 12:40)</span> sindy</div></div></div><div id="comment-tools-49439" class="comment-tools"></div><div class="clear"></div><div id="comment-49439-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

