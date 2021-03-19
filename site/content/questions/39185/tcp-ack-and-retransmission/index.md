+++
type = "question"
title = "tcp ack and retransmission"
description = '''Hi, I am seeing the following: TCP ACK SEQ 2640421534 ACK 3886631705 tcp.len is 0 bytes, ACK FLAG TCP DATA PACKET SEQ 2640421534 ACK 3886631705 tcp.len 19 bytes, PUSH and ACK flags, Wireshark expert analysis marks it has a RETRANSMISSION.  I confused why this is a RETRANSMISSION. The SEQ and ACK num...'''
date = "2015-01-15T21:54:00Z"
lastmod = "2015-01-16T01:35:00Z"
weight = 39185
keywords = [ "retransmission" ]
aliases = [ "/questions/39185" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tcp ack and retransmission](/questions/39185/tcp-ack-and-retransmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39185-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am seeing the following:</p><pre><code>TCP ACK SEQ 2640421534 ACK 3886631705 tcp.len is 0 bytes, ACK FLAG
TCP DATA PACKET SEQ 2640421534 ACK 3886631705 tcp.len 19 bytes, PUSH and ACK flags, Wireshark expert analysis marks it has a RETRANSMISSION.</code></pre><p>I confused why this is a RETRANSMISSION. The SEQ and ACK numbers are the same, but one packet is simple ACK and the subsequent is a data packet.</p></div><div id="question-tags" class="tags-container tags">retransmission</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '15, 21:54</strong></p><img src="https://secure.gravatar.com/avatar/a75a28c9bc7acf32bfc20ec1e984da19?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dummycat&#39;s gravatar image" /><p>Dummycat<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dummycat has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jan '15, 00:29</p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-39185" class="comments-container"></div><div id="comment-tools-39185" class="comment-tools"></div><div class="clear"></div><div id="comment-39185-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39194"></span>

<div id="answer-container-39194" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39194-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In order to be able to give an answer to your question, you would have to show a few more packets before the ACK packet, as there is most likely already data sent in this direction with a sequence number of 2640421534.</p><p>If you are able to upload the capture data to www.cloudshark.org, that would make it easier to analyze and help you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jan '15, 01:35</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-39194" class="comments-container"><span id="39199"></span><div id="comment-39199" class="comment"><div id="post-39199-score" class="comment-score"></div><div class="comment-text"><p>SYN-bit,</p><p>Thanks for your response. I can't upload the file because it contains client data.</p><p>This is what I have done before I posted</p><ul><li>Created columns for SEQ, NEXT SEQ and ACK numbers then sorted by SEQ number. This created two different behaviors:</li><li>If Wireshark analysis of the TCP ACK (tcp.len=0) packet has the message "TCP previous segment not capture" then the subsequent TCP DATA (tcp.len=19) packet is analyzed without any issues.</li><li><p>If the TCP ACK (tcp.len=0) packet does not have any issues then the TCP DATA (tcp.len=19) packet is classified as a retransmission</p></li><li><p>versions 1.10.12 and 1.12.2 (same issue)</p></li><li>exporting the stream to another file (this is the fix when intermittently out-of-order are classified as retransmissions)</li></ul></div><div id="comment-39199-info" class="comment-info"><span class="comment-age">(16 Jan '15, 04:35)</span> Dummycat</div></div><span id="39206"></span><div id="comment-39206" class="comment"><div id="post-39206-score" class="comment-score"></div><div class="comment-text"><p>Maybe use TraceWrangler (<a href="http://www.tracewrangler.com">http://www.tracewrangler.com</a>) to sanitize your file, and make sure you select the option to remove unknown payloads. You can also force cutting after layer 4, which leaves you with everything up to the TCP layer, which is probably good enough in this case. Together with IP address randomization you should do fine, but of course you should check the sanitized file before uploading.</p></div><div id="comment-39206-info" class="comment-info"><span class="comment-age">(16 Jan '15, 06:49)</span> Jasper ♦♦</div></div><span id="39246"></span><div id="comment-39246" class="comment"><div id="post-39246-score" class="comment-score"></div><div class="comment-text"><p>Sounds like the packet before the ACK (tcp.len==0) has a length that should include (part of) the data from the DATA packet (tcp.len==19).</p><p>Could you either use TraceWrangler and post an anonimized version of the file (like Jasper suggested) or post the output of:</p><pre><code>tshark -nr &lt;file&gt; -T fields -e frame.number -e tcp.srcport -e tcp.dstport -e tcp.seq -e tcp.len -e tcp.ack</code></pre></div><div id="comment-39246-info" class="comment-info"><span class="comment-age">(18 Jan '15, 09:02)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-39194" class="comment-tools"></div><div class="clear"></div><div id="comment-39194-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

