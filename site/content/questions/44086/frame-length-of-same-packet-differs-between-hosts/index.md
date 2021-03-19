+++
type = "question"
title = "Frame Length of Same Packet Differs Between Hosts"
description = '''Hi,  I&#x27;m looking at a problem with communication to a new Kafka server in our environment and have a capture of the comms between the two hosts. The sending host sends a request: sudo /tmp/kafka_2.10-0.8.2.1/bin/kafka-console-producer.sh --broker-list kafka-012:9092 --topic test  Which results in a ...'''
date = "2015-07-13T03:21:00Z"
lastmod = "2015-07-16T05:30:00Z"
weight = 44086
keywords = [ "ack", "frame", "difference", "hosts", "length" ]
aliases = [ "/questions/44086" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Frame Length of Same Packet Differs Between Hosts](/questions/44086/frame-length-of-same-packet-differs-between-hosts)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44086-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44086-score" class="post-score" title="current number of votes">0</div><span id="post-44086-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm looking at a problem with communication to a new Kafka server in our environment and have a capture of the comms between the two hosts. The sending host sends a request:</p><pre><code>sudo /tmp/kafka_2.10-0.8.2.1/bin/kafka-console-producer.sh --broker-list kafka-012:9092 --topic test</code></pre><p>Which results in a failure response that I don't think it network related but when digging into the capture I noticed something that I am unsure about.</p><p>The TCP handshake is established as normal and the sending server, 01, sends a PSH,ACK that is successfully received by kafka server. The corresponding ACK when sent is 432 bits in size but the frame received by 01 is 480 bits in size. I can't see why this might be from the capture output, can anybody give any clues please?</p><p>Many thanks,</p><p>JT</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-frame" rel="tag" title="see questions tagged &#39;frame&#39;">frame</span> <span class="post-tag tag-link-difference" rel="tag" title="see questions tagged &#39;difference&#39;">difference</span> <span class="post-tag tag-link-hosts" rel="tag" title="see questions tagged &#39;hosts&#39;">hosts</span> <span class="post-tag tag-link-length" rel="tag" title="see questions tagged &#39;length&#39;">length</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jul '15, 03:21</strong></p><img src="https://secure.gravatar.com/avatar/b517dd33ff6fab5007e97e44c50b759a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alienbob&#39;s gravatar image" /><p><span>alienbob</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alienbob has no accepted answers">0%</span></p></div></div><div id="comments-container-44086" class="comments-container"><span id="44087"></span><div id="comment-44087" class="comment"><div id="post-44087-score" class="comment-score"></div><div class="comment-text"><p>What does a Statistics -&gt; Comments Summary show on each side. are the traces using the same encapsulation?</p></div><div id="comment-44087-info" class="comment-info"><span class="comment-age">(13 Jul '15, 04:16)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="44205"></span><div id="comment-44205" class="comment"><div id="post-44205-score" class="comment-score"></div><div class="comment-text"><p>Both were Ethernet encapsulation.</p></div><div id="comment-44205-info" class="comment-info"><span class="comment-age">(16 Jul '15, 05:30)</span> <span class="comment-user userinfo">alienbob</span></div></div></div><div id="comment-tools-44086" class="comment-tools"></div><div class="clear"></div><div id="comment-44086-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="44102"></span>

<div id="answer-container-44102" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44102-score" class="post-score" title="current number of votes">0</div><span id="post-44102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="alienbob has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As Jaap indicated, the frame as captured on the machine that sent it is 432 bits = 432/8 bytes = 54 bytes, whereas the same frame, as captured on the machine that received it, is 480 bits = 480/8 bytes = 60 bytes.</p><p>A TCP frame with no TCP payload, and no TCP or IP options, sent over IPv4 over Ethernet, has a 14-byte Ethernet header, a 20-byte IPv4 header, and a 20-byte TCP header, for a total of 54 bytes.</p><p>If you're capturing on the machine that sends the packet, that 54-byte packet is "wrapped around" inside the OS networking stack and handed to the packet capture mechanism that libpcap/WinPcap (as used by Wireshark) uses to capture packets, so it sees a 54-byte packet.</p><p>When it's transmitted on the Ethernet, however, it must be padded to a minimum of 60 bytes, and have a 4-byte CRC appended to it. Therefore, when it's received, a 54-byte frame would be 64 bytes long, including the CRC.</p><p>Most drivers and capture mechanisms won't provide the CRC, so the frame, as provided to libpcap/WinPcap by the capture mechanism, will be 60 bytes long on any machine <em>other</em> than the machine that sent it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jul '15, 10:27</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-44102" class="comments-container"><span id="44204"></span><div id="comment-44204" class="comment"><div id="post-44204-score" class="comment-score"></div><div class="comment-text"><p>Thanks, all for the snappy responses sorry it took a while to respond. yes, that appears to be exactly the reason, as each is a 0 length packet that makes perfect sense and looking through further packets the same applies in both directions!</p></div><div id="comment-44204-info" class="comment-info"><span class="comment-age">(16 Jul '15, 05:29)</span> <span class="comment-user userinfo">alienbob</span></div></div></div><div id="comment-tools-44102" class="comment-tools"></div><div class="clear"></div><div id="comment-44102-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="44088"></span>

<div id="answer-container-44088" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44088-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44088-score" class="post-score" title="current number of votes">0</div><span id="post-44088-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Possible explanation:</p><ul><li>480 / 8 = 60 bytes</li><li>60 bytes + 4 byte CRC = 64 bytes</li><li>Minimum Ethernet frame size = 64 bytes, of which you see 60 bytes, as the NIC strips the CRC.</li></ul><p>So you would see some padding at the end of the frame?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jul '15, 04:26</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-44088" class="comments-container"></div><div id="comment-tools-44088" class="comment-tools"></div><div class="clear"></div><div id="comment-44088-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

