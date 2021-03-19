+++
type = "question"
title = "Doubt in TCP RFC(seg.seq+seg.len-1=last seq no of segment)"
description = '''Below is the trace of client side communication(all the way from first packet to last) from which i am looking to understand a statement in RFC793. In pg.28 :seg.seq(first seq number of a segment)+seg.len(the no.of octets occupied by data)-1=last seq no of segment Here my first sequence number is 0 ...'''
date = "2013-06-23T22:21:00Z"
lastmod = "2013-06-24T00:00:00Z"
weight = 22263
keywords = [ "rfc793" ]
aliases = [ "/questions/22263" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Doubt in TCP RFC(seg.seq+seg.len-1=last seq no of segment)](/questions/22263/doubt-in-tcp-rfcsegseqseglen-1last-seq-no-of-segment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22263-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Below is the trace of client side communication(all the way from first packet to last) from which i am looking to understand a statement in RFC793.</p><p>In pg.28 :seg.seq(first seq number of a segment)+seg.len(the no.of octets occupied by data)-1=last seq no of segment</p><p>Here my first sequence number is 0 and total amount of data that traversed is 723 bytes but if we apply this formula the last no should be [0+723-1]=722 which is obviously wrong.Please let me clarify if i am missing any thing here.</p><p>Trace:</p><pre><code>35   5.680942 192.168.0.101 -&gt; 199.232.41.10 TCP 62  nhci &gt; http [SYN] Seq=0 Win=64240 Len=0 MSS=1460 SACK_PERM=1
42   5.721403 192.168.0.101 -&gt; 199.232.41.10 TCP 54  nhci &gt; http [ACK] Seq=1 Ack=1 Win=64240 Len=0
43   5.745246 192.168.0.101 -&gt; 199.232.41.10 HTTP 393  GET /gnu.css HTTP/1.1
48   5.791402 192.168.0.101 -&gt; 199.232.41.10 TCP 54  nhci &gt; http [ACK] Seq=340 Ack=1604 Win=64240 Len=0
49   5.806331 192.168.0.101 -&gt; 199.232.41.10 HTTP 438  GET /graphics/gnu-head-sm.jpg HTTP/1.1
53   5.851962 192.168.0.101 -&gt; 199.232.41.10 TCP 54  nhci &gt; http [ACK] Seq=724 Ack=4524 Win=64240 Len=0
57   5.895093 192.168.0.101 -&gt; 199.232.41.10 TCP 54  nhci &gt; http [ACK] Seq=724 Ack=7226 Win=64240 Len=0
72  22.646439 192.168.0.101 -&gt; 199.232.41.10 TCP 54  nhci &gt; http [ACK] Seq=724 Ack=7227 Win=64240 Len=0
73  31.086352 192.168.0.101 -&gt; 199.232.41.10 TCP 54  nhci &gt; http [FIN, ACK] Seq=724 Ack=7227 Win=64240 Len=0</code></pre></div><div id="question-tags" class="tags-container tags">rfc793</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jun '13, 22:21</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p>krishnayeddula<br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Jun '13, 01:46</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-22263" class="comments-container"></div><div id="comment-tools-22263" class="comment-tools"></div><div class="clear"></div><div id="comment-22263-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22266"></span>

<div id="answer-container-22266" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22266-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>seg.seq(first seq number of a segment)+seg.len(the no.of octets occupied by data)-1=last seq no of segment</p></blockquote><p>These sequence numbers refer to the sequence numbers in one segment, not to the sequence numbers in the whole TCP stream.</p><p>So in your case:</p><ul><li>Frame 35: SYN packet, no length, do add 1 for the phantom byte</li><li>Frame 42; ACK packet, no length, start seq = 1 (because of the phantom byte after the SYN)</li><li>Frame 43: GET request, seq nr of first byte in segment is 1, length is 723, so seq nr of last byte in segment is 1+339-1=339, next seq nr should be 339+1 = 340</li><li>Frame 48: ACK packet, no length</li><li>Frame 43: GET request, seq nr of first byte in segment is 340, length is 384, so seq nr of last byte in segment is 340+384-1=723, next seq nr should be 723+1 = 724</li></ul><p>I guess you did not take into account the phantom byte after the SYN packet. See <a href="http://tools.ietf.org/html/rfc793#page-16">page 16 of rfc 723</a>:</p><pre><code>The sequence number of the first data octet in this segment (except
when SYN is present). If SYN is present the sequence number is the
initial sequence number (ISN) and the first data octet is ISN+1.</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '13, 00:00</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Jun '13, 02:21</p></div></div><div id="comments-container-22266" class="comments-container"></div><div id="comment-tools-22266" class="comment-tools"></div><div class="clear"></div><div id="comment-22266-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22265"></span>

<div id="answer-container-22265" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22265-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>The solution is pretty simple: The SYN like the FIN Bits count as one Byte sent, which is why there's an ACK for those packets as well. So if you sent 723 Bytes you've sent those with Seq.Nr. 1 instead of 0 because those were sent after the SYN.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jun '13, 23:45</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-22265" class="comments-container"></div><div id="comment-tools-22265" class="comment-tools"></div><div class="clear"></div><div id="comment-22265-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

