+++
type = "question"
title = "how to accurately measure network packet loss in a trace"
description = '''We do have several expert info from wireshark but all are indicative based on the recevied/sent SEQ number with adjacent packets and it is not reflecting the reality on the wire. How can I get the exact percentage/rate of packet loss using wireshark (if I for instance setup a specific lost rate usin...'''
date = "2015-10-31T14:33:00Z"
lastmod = "2015-10-31T15:48:00Z"
weight = 47119
keywords = [ "loss", "packetloss" ]
aliases = [ "/questions/47119" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to accurately measure network packet loss in a trace](/questions/47119/how-to-accurately-measure-network-packet-loss-in-a-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47119-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We do have several expert info from wireshark but all are indicative based on the recevied/sent SEQ number with adjacent packets and it is not reflecting the reality on the wire. How can I get the exact percentage/rate of packet loss using wireshark (if I for instance setup a specific lost rate using TC netem).</p><p>For instance (on receiver side trace): "tcp.analysis.lost_segment" could happen even when there is no packet loss, it could happen when packets received out of order with the next one (the next one will have out-of-order expert info).</p><p>(also on receiver side trace): there could be multiple instances of "tcp.analysis.duplicate_ack" for single lost packet from the sender since the sender keep sending packets with higher SEQ and the receiver keep sending duplicate ACKs (with SACK option enabled telling sender to just resend the missing SEQ range).</p><p>So all in all using those filters we can only get a percentage of packets that is related/triggered by packet loss and not the exact packet loss rate/percentage itself which can be configured on Netem, is there a way to get the exact packet loss rate from the trace? I think doing it manually on one TCP stream at the time could work but that is too inefficient.</p></div><div id="question-tags" class="tags-container tags">loss packetloss</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Oct '15, 14:33</strong></p><img src="https://secure.gravatar.com/avatar/1e84fb88c367cef82ae127b8c164750e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yhzs8&#39;s gravatar image" /><p>yhzs8<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yhzs8 has no accepted answers">0%</span></p></div></div><div id="comments-container-47119" class="comments-container"></div><div id="comment-tools-47119" class="comment-tools"></div><div class="clear"></div><div id="comment-47119-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47121"></span>

<div id="answer-container-47121" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47121-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I think doing it manually on one TCP stream at the time could work but that is too inefficient.</p></blockquote><p>If you try to do it with manually, you won't get <strong>exact</strong> results for UDP (as there is no SEQ/ACK numbers) and you will face the very same problems that Wireshark has with packets out of order, real missing frames, etc.</p><blockquote><p>is there a way to get the <strong>exact</strong> packet loss rate from the trace?</p></blockquote><p>You can only determine the <strong>exact</strong> packet loss by capturing at two places, near the sender and near the receiver, and then compare the capture files.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Oct '15, 15:48</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Nov '15, 08:17</p></div></div><div id="comments-container-47121" class="comments-container"><span id="47122"></span><div id="comment-47122" class="comment"><div id="post-47122-score" class="comment-score"></div><div class="comment-text"><p>Yes I only discuss TCP here.</p><p>Well by capturing at two places and compare them will become even more manual/inefficient work. I think capturing at the receiver-end should get the exact packet loss under the assumption that the sender is fully TCP-RFC compliant and whatever packet is lost is due to netowrk. from the receiver end trace it should understand those two different kind of packet loss: downstream packet loss resulting in tcp.analysis.lost_segment followed by tcp.analysis.duplicate_ack. upstream packet loss will result in tcp_analysis.retansmission followed by tcp.analysis.duplicate_ack. but as said before those could be false positives and it need to be studied on case-by-case basis.</p><p>Can you please elaborate more technically why both side of traces are needed and why we can not be 100% certain if only using receiver-side trace?</p></div><div id="comment-47122-info" class="comment-info"><span class="comment-age">(31 Oct '15, 16:04)</span> yhzs8</div></div><span id="47154"></span><div id="comment-47154" class="comment"><div id="post-47154-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Can you please elaborate more technically why both side of traces are needed and why we can not be 100% certain if only using receiver-side trace?</p></blockquote><p>It depends on the definition of <strong>packet loss</strong>. If you define it as <strong>missing frames in a TCP conversation</strong> (sounds like that's what you are after) then you can detect that at one side by looking at the TCP SEQ/ACK numbers. You will have the same 'problems' as Wireshark, meaning you'll have to take into account packet reordering, duplicates, etc. If you can do that manually or via scripting, you're fine.</p></div><div id="comment-47154-info" class="comment-info"><span class="comment-age">(02 Nov '15, 05:19)</span> Kurt Knochner ♦</div></div><span id="47155"></span><div id="comment-47155" class="comment"><div id="post-47155-score" class="comment-score"></div><div class="comment-text"><p>Still, just looking at SEQ/ACK may not be good enough as you can still run into out of orders or packet loss after the capture location. Each packet loss needs to be verified specifically by looking at all the symptoms and timings.</p></div><div id="comment-47155-info" class="comment-info"><span class="comment-age">(02 Nov '15, 05:38)</span> Jasper ♦♦</div></div><span id="47156"></span><div id="comment-47156" class="comment"><div id="post-47156-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Still, just looking at SEQ/ACK may not be good enough</p></blockquote><p>Very true. It all depends on the defintion of packet loss and what the OP want's to figure out.</p><blockquote><p>(if I for instance setup a specific lost rate using TC netem).</p></blockquote><p>especially in that case (artificial packet loss), you will probaly see DUP-ACK in one direction, but no missing frames in the other direction if re-sending worked, which would always be the case if the TCP stream finished successfully. That's what I meant by 'the same problems as Wireshark'.</p><p>As I said: It all depends on the definition of 'packet loss' and one will only get the 'big (correct) picture' by looking at the capture files taken at both sides.</p></div><div id="comment-47156-info" class="comment-info"><span class="comment-age">(02 Nov '15, 08:16)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-47121" class="comment-tools"></div><div class="clear"></div><div id="comment-47121-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

