+++
type = "question"
title = "TCP features for congestion window (cwnd)"
description = '''Which among the following features are very important (critical ones) for estimating a TCP congestion window (cwnd) from a passive trace?  [_id]  ,[_timestamp]  ,[parent_ip]  ,[tcp_srcport]  ,[tcp_dstport]  ,[tcp_port]  ,[tcp_stream]  ,[tcp_len]  ,[tcp_seq]  ,[tcp_hdr_len]  ,[tcp_window_size_value] ...'''
date = "2017-04-22T01:59:00Z"
lastmod = "2017-04-25T06:30:00Z"
weight = 60959
keywords = [ "congestion-control", "wireshark", "tcp", "congestion" ]
aliases = [ "/questions/60959" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP features for congestion window (cwnd)](/questions/60959/tcp-features-for-congestion-window-cwnd)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60959-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60959-score" class="post-score" title="current number of votes">0</div><span id="post-60959-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Which among the following features are very important (critical ones) for estimating a TCP congestion window (cwnd) from a passive trace?</p><pre><code>   [_id]
  ,[_timestamp]
  ,[parent_ip]
  ,[tcp_srcport]
  ,[tcp_dstport]
  ,[tcp_port]
  ,[tcp_stream]
  ,[tcp_len]
  ,[tcp_seq]
  ,[tcp_hdr_len]
  ,[tcp_window_size_value]
  ,[tcp_window_size]
  ,[tcp_ack]
  ,[tcp_window_size_scalefactor]
  ,[tcp_nxtseq]
 ,[tcp_analysis_bytes_in_flight]
 ,[tcp_analysis_lost_segment]
 ,[tcp_analysis_out_of_order]
 ,[tcp_analysis_retransmission]
 ,[tcp_analysis_rto]
 ,[tcp_analysis_rto_frame]
 ,[tcp_analysis_zero_window_probe]
,tcp_flags (ack, psh, fin, syn, res, cwr,...etc) 
,tcp_time_stamps</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-congestion-control" rel="tag" title="see questions tagged &#39;congestion-control&#39;">congestion-control</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-congestion" rel="tag" title="see questions tagged &#39;congestion&#39;">congestion</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '17, 01:59</strong></p><img src="https://secure.gravatar.com/avatar/6dd3e71b974fad46455a71063cb9c319?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="armodes&#39;s gravatar image" /><p><span>armodes</span><br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="armodes has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Apr '17, 02:15</strong> </span></p></div></div><div id="comments-container-60959" class="comments-container"><span id="60961"></span><div id="comment-60961" class="comment"><div id="post-60961-score" class="comment-score"></div><div class="comment-text"><p>You can only guess it. But Bytes_in_flight and window_size can be used for this guessing.</p></div><div id="comment-60961-info" class="comment-info"><span class="comment-age">(22 Apr '17, 02:22)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="60962"></span><div id="comment-60962" class="comment"><div id="post-60962-score" class="comment-score"></div><div class="comment-text"><p>But the tcp_window_size is pretty consistent. It doesn't vary much. For example: in my case i have around 300,000 capture packets the window size varies only 2 times (it starts with 29312 and stays pretty the same and then changes to 30336 at the end).</p></div><div id="comment-60962-info" class="comment-info"><span class="comment-age">(22 Apr '17, 02:54)</span> <span class="comment-user userinfo">armodes</span></div></div><span id="60988"></span><div id="comment-60988" class="comment"><div id="post-60988-score" class="comment-score">1</div><div class="comment-text"><p>Yes, but there is still no way to determine cwnd from a trace. You can guess what it is, but it's not possible to get a 100% correct value from packets. It all depends on what the sending stacks thinks about the situation, and that's not in the packets.</p></div><div id="comment-60988-info" class="comment-info"><span class="comment-age">(23 Apr '17, 09:15)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-60959" class="comment-tools"></div><div class="clear"></div><div id="comment-60959-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60990"></span>

<div id="answer-container-60990" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60990-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60990-score" class="post-score" title="current number of votes">2</div><span id="post-60990-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Bytes in Flight is probably the best estimate. It tells us what the sender has actually decided to transmit.</p><p>The receiver's advertised "Receive Window" is the maximum that a sender can ever have in flight. It is usually fairly consistent - unless the receiving application gets into trouble.</p><p>The sender's "Transmit Window" must be equal or less than the Receive Window. In congestion avoidance mode, the transmit window (bytes in flight) will be sender's CWND.<br />
</p><p>Note that Wireshark has an outstanding "bug" in that it doesn't include data in its count if the packets weren't in the trace.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '17, 10:56</strong></p><img src="https://secure.gravatar.com/avatar/35a0c1d0cf15b9d54d73bf54ae28abcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Philst&#39;s gravatar image" /><p><span>Philst</span><br />
<span class="score" title="431 reputation points">431</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Philst has 6 accepted answers">27%</span> </br></p></div></div><div id="comments-container-60990" class="comments-container"><span id="61043"></span><div id="comment-61043" class="comment"><div id="post-61043-score" class="comment-score"></div><div class="comment-text"><p>I also thought of that but the problem is since bytes_in_flgiht is a calculated value from tcpdump (or wireshark) - i mean not part of the TCP header, how can we derive its relation with the cwnd? I am joining the passive trace from the monitor to a TCP kernel state of the sender where we get the value of the cwnd that have the same sequence number.</p><p>tcp_seq=1256867582, tcp_nxt_seq=1256869030, tcp_len=1448, tcp_window_size=29312, tcp_bytes_in_flight=11622, cwnd=16</p><p>Is there anyway to derive (or estimate sort to say) the value of the congestion window (cwnd=16) from the bytes_in_flight or the sequence number? I am so confused. The receiver window size is constant for all packets.</p></div><div id="comment-61043-info" class="comment-info"><span class="comment-age">(25 Apr '17, 06:30)</span> <span class="comment-user userinfo">armodes</span></div></div></div><div id="comment-tools-60990" class="comment-tools"></div><div class="clear"></div><div id="comment-60990-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

