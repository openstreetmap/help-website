+++
type = "question"
title = "TCP client does not send DUP ACKs for lost packets"
description = '''Hello people,  I am working on a capture from wireshark, and the TCP client sometimes does not send a DUP ACK or may be it is lost by the network? I have a duplex link with 1 percent packet loss. Wireshark reports that &quot;previous segment not captured&quot;, which is true but the DUP ACK is not sent for th...'''
date = "2016-07-26T08:19:00Z"
lastmod = "2016-07-27T06:18:00Z"
weight = 54345
keywords = [ "dup-ack", "tcp" ]
aliases = [ "/questions/54345" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP client does not send DUP ACKs for lost packets](/questions/54345/tcp-client-does-not-send-dup-acks-for-lost-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54345-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54345-score" class="post-score" title="current number of votes">0</div><span id="post-54345-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello people,</p><p>I am working on a capture from wireshark, and the TCP client sometimes does not send a DUP ACK or may be it is lost by the network? I have a duplex link with 1 percent packet loss. Wireshark reports that "previous segment not captured", which is true but the DUP ACK is not sent for the missing segment.</p><p>The next ACK from the client is a sequence number higher than the "lost" packet. The sender just sends the segment with expected sequence number and does not send the "lost" packet.<br />
</p><p>I am analyzing delays for each segments of video frame, but I cannot find the "lost" segment in the receiver.</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dup-ack" rel="tag" title="see questions tagged &#39;dup-ack&#39;">dup-ack</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jul '16, 08:19</strong></p><img src="https://secure.gravatar.com/avatar/6ac558d50e14e1baababd985172501e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Varisetty&#39;s gravatar image" /><p><span>Varisetty</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Varisetty has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-54345" class="comments-container"></div><div id="comment-tools-54345" class="comment-tools"></div><div class="clear"></div><div id="comment-54345-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54346"></span>

<div id="answer-container-54346" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54346-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54346-score" class="post-score" title="current number of votes">2</div><span id="post-54346-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The fact that Wireshark reports "Previous segment not captured" means that the missing packet is not in your trace file, but the fact that the client does not send duplicate ACKs <strong>AND</strong> the next ACK is a higher number than the lost packet means that the client actually did receive that packet.</p><p>If the packet was actually received, but it's not in your trace file, the most likely causes are:</p><p>1) There is asymmetric routing, and not all packets went past your capture point;</p><p>2) Wireshark simply couldn't keep up. The packet showed up, but wasn't written into the trace file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '16, 09:18</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-54346" class="comments-container"><span id="54368"></span><div id="comment-54368" class="comment"><div id="post-54368-score" class="comment-score"></div><div class="comment-text"><p>thanks Jim for the answer, but the network topology is very small with no asymmetrical routing. In this case, the packet arrived on the interface but not captured into the wireshark trace file?</p></div><div id="comment-54368-info" class="comment-info"><span class="comment-age">(27 Jul '16, 06:08)</span> <span class="comment-user userinfo">Varisetty</span></div></div><span id="54369"></span><div id="comment-54369" class="comment"><div id="post-54369-score" class="comment-score"></div><div class="comment-text"><p>On top of packet loss during capture, which happens when capturing a relatively heavy traffic using relatively weak machines, another reason for this may be TCP offload provided by the network card if you happen to capture on the card through which the traffic actually runs. With TCP offloading switched on, the capturing filter (libpcap, WinPcap, NPcap) may not get all frames. If it is your case, the remedy is to disable TCP offloading in your network card's settings. Several other Questions here deal with the topic, your keywords would be "offload" and "chimney".</p></div><div id="comment-54369-info" class="comment-info"><span class="comment-age">(27 Jul '16, 06:18)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-54346" class="comment-tools"></div><div class="clear"></div><div id="comment-54346-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

