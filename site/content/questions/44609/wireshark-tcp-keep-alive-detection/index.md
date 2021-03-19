+++
type = "question"
title = "Wireshark TCP Keep-Alive detection"
description = '''Hi, I have a trace showing two packets; both with a TCP Length of 1 byte, both with a payload of 0x00 and both with the ACK flag set. In fact they are identical except for seq no., ack no. and checksum. The Info column shows TCP Segment of a reassembled PDU for the first packet and TCP Keep-Alive fo...'''
date = "2015-07-29T14:41:00Z"
lastmod = "2015-07-31T03:01:00Z"
weight = 44609
keywords = [ "keep-alive", "tcp", "keepalive" ]
aliases = [ "/questions/44609" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark TCP Keep-Alive detection](/questions/44609/wireshark-tcp-keep-alive-detection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44609-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44609-score" class="post-score" title="current number of votes">0</div><span id="post-44609-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a trace showing two packets; both with a TCP Length of 1 byte, both with a payload of 0x00 and both with the ACK flag set. In fact they are identical except for seq no., ack no. and checksum. The Info column shows TCP Segment of a reassembled PDU for the first packet and TCP Keep-Alive for the second packet.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/tcp-keep-alive_oWmRjcw.jpg" alt="alt text" /></p><p>The screenshot above shows the hex dumps of both packets (1 and 8). Why does Wireshark interpret these two packets differently? I believe that they are both Keep-Alives.</p><p>Thanks and regards...Paul</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-keep-alive" rel="tag" title="see questions tagged &#39;keep-alive&#39;">keep-alive</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-keepalive" rel="tag" title="see questions tagged &#39;keepalive&#39;">keepalive</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jul '15, 14:41</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p><span>PaulOfford</span><br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></img></div></div><div id="comments-container-44609" class="comments-container"><span id="44610"></span><div id="comment-44610" class="comment"><div id="post-44610-score" class="comment-score"></div><div class="comment-text"><p>This is not easy to answer because we need to see the sequence numbers of the packets from the same source before the two packets you posted. Can you upload the (sanitized?) pcap to cloudshark? It's much easier to work with pcaps than with screenshots...</p></div><div id="comment-44610-info" class="comment-info"><span class="comment-age">(29 Jul '15, 14:46)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="44621"></span><div id="comment-44621" class="comment"><div id="post-44621-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper,</p><p>The tracefile is here <a href="http://www.tribelabzero.com/download/tds_sql_batch_bug1.pcapng">http://www.tribelabzero.com/download/tds_sql_batch_bug1.pcapng</a></p></div><div id="comment-44621-info" class="comment-info"><span class="comment-age">(29 Jul '15, 23:29)</span> <span class="comment-user userinfo">PaulOfford</span></div></div></div><div id="comment-tools-44609" class="comment-tools"></div><div class="clear"></div><div id="comment-44609-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44624"></span>

<div id="answer-container-44624" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44624-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44624-score" class="post-score" title="current number of votes">0</div><span id="post-44624-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jasper has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>OK - I've just had a bit of a lesson on TCP from a colleague and I now understand the issue.</p><p>A TCP Keep-Alive is sent with a Seq No one less than the sequence number the receiver is expecting. Because the receiver has already ACKd the Seq No of the Keep-Alive (because that Seq No was in the range of an earlier segment), it just ACKs it again and discards the segment (packet).</p><p>In my trace I haven't captured the previous packets and so Wireshark doesn't know what the next expected sequence number should be, and so it is unable to determine the first packet as a Keep-Alive</p><p>Best regards...Paul</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jul '15, 03:37</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p><span>PaulOfford</span><br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-44624" class="comments-container"><span id="44646"></span><div id="comment-44646" class="comment"><div id="post-44646-score" class="comment-score"></div><div class="comment-text"><p>Yes it is the answer that I would give you, too.</p><p>So I think you can accept yourself the answer, so others can learn.</p></div><div id="comment-44646-info" class="comment-info"><span class="comment-age">(30 Jul '15, 12:30)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="44673"></span><div id="comment-44673" class="comment"><div id="post-44673-score" class="comment-score"></div><div class="comment-text"><p>I'll do it for Paul, no problem ;-)</p></div><div id="comment-44673-info" class="comment-info"><span class="comment-age">(31 Jul '15, 03:01)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-44624" class="comment-tools"></div><div class="clear"></div><div id="comment-44624-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

