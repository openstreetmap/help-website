+++
type = "question"
title = "Bytes_in_flight and TCP cwnd relationship"
description = '''I was thinking of using the bytes_in_flgiht in order to estimate a TCP cwnd from passive traces but it is not clear for on how we can we derive its relation with the cwnd. I am joining the passive trace from the monitor to a TCP kernel state of the sender where we get the value of the cwnd that have...'''
date = "2017-04-25T07:25:00Z"
lastmod = "2017-04-26T00:02:00Z"
weight = 61048
keywords = [ "tcp-bytes-in-flight", "wireshark", "cwnd", "tcp", "congestion" ]
aliases = [ "/questions/61048" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Bytes\_in\_flight and TCP cwnd relationship](/questions/61048/bytes_in_flight-and-tcp-cwnd-relationship)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61048-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61048-score" class="post-score" title="current number of votes">0</div><span id="post-61048-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was thinking of using the bytes_in_flgiht in order to estimate a TCP cwnd from passive traces but it is not clear for on how we can we derive its relation with the cwnd. I am joining the passive trace from the monitor to a TCP kernel state of the sender where we get the value of the cwnd that have the same sequence number in the trace file.</p><p>tcp_seq=1256867582, tcp_nxt_seq=1256869030, tcp_len=1448, tcp_window_size=29312, tcp_bytes_in_flight=11622, cwnd=16</p><p>Is there any way to derive (or estimate sort to say) the value of the congestion window (for example: cwnd=16) from the bytes_in_flight or the sequence number? I am so confused.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp-bytes-in-flight" rel="tag" title="see questions tagged &#39;tcp-bytes-in-flight&#39;">tcp-bytes-in-flight</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-cwnd" rel="tag" title="see questions tagged &#39;cwnd&#39;">cwnd</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-congestion" rel="tag" title="see questions tagged &#39;congestion&#39;">congestion</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Apr '17, 07:25</strong></p><img src="https://secure.gravatar.com/avatar/6dd3e71b974fad46455a71063cb9c319?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="armodes&#39;s gravatar image" /><p><span>armodes</span><br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="armodes has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Apr '17, 07:44</strong> </span></p></div></div><div id="comments-container-61048" class="comments-container"></div><div id="comment-tools-61048" class="comment-tools"></div><div class="clear"></div><div id="comment-61048-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61054"></span>

<div id="answer-container-61054" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61054-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61054-score" class="post-score" title="current number of votes">0</div><span id="post-61054-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>cwnd is accounted in MSS. So, cwnd (in Bytes)=cwnd * MSS. BUT when you're estimating cwnd from bytes_in_flight, you have to consider in that case cwnd MUST be the limiting factor for the sender. In your case cwnd = 16 * MSS = 16 * 1448 Bytes = 23168 Bytes. This is much more than actual bytes_in_flight, and it just means the sender can continue sending packets without receiving ACKs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Apr '17, 00:02</strong></p><img src="https://secure.gravatar.com/avatar/1e22670f8d643ca08d658b80a6782932?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Packet_vlad&#39;s gravatar image" /><p><span>Packet_vlad</span><br />
<span class="score" title="436 reputation points">436</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Packet_vlad has 5 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Apr '17, 00:26</strong> </span></p></div></div><div id="comments-container-61054" class="comments-container"></div><div id="comment-tools-61054" class="comment-tools"></div><div class="clear"></div><div id="comment-61054-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

