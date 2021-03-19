+++
type = "question"
title = "TCP ZeroWindow loop"
description = '''My NFS client and NetApp filer got stuck in this loop of ACKs and ZeroWindows. This repeated over and over until i finally dropped the connection with tcpdrop. I&#x27;m thinking this is a bug on the NetApp filer, can someone help me break down exactly what is happening? It seems like my client (10.231.96...'''
date = "2012-01-16T10:25:00Z"
lastmod = "2012-09-21T14:05:00Z"
weight = 8412
keywords = [ "zero-window" ]
aliases = [ "/questions/8412" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP ZeroWindow loop](/questions/8412/tcp-zerowindow-loop)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8412-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8412-score" class="post-score" title="current number of votes">0</div><span id="post-8412-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My NFS client and NetApp filer got stuck in this loop of ACKs and ZeroWindows. This repeated over and over until i finally dropped the connection with tcpdrop. I'm thinking this is a bug on the NetApp filer, can someone help me break down exactly what is happening? It seems like my client (10.231.96.85) is waiting for an acknowledgment of 55k of data, but the filer (10.231.96.105) is just sending ZeroWindow back forever:</p><pre><code>  1   0.000000 10.231.96.105 -&gt; 10.231.96.85 TCP [TCP ZeroWindow] nfs &gt; oob-ws-http [ACK] Seq=1 Ack=1 Win=0 Len=0 TSV=122735999 TSER=828368381
  2   0.000004 10.231.96.85 -&gt; 10.231.96.105 TCP [TCP ACKed lost segment] oob-ws-http &gt; nfs [ACK] Seq=55773 Ack=2 Win=1029 Len=0 TSV=953767461 TSER=122735063
  3   0.000006 10.231.96.105 -&gt; 10.231.96.85 TCP [TCP ZeroWindow] [TCP Keep-Alive] nfs &gt; oob-ws-http [ACK] Seq=1 Ack=1 Win=0 Len=0 TSV=122735999 TSER=828368381
  4   0.000009 10.231.96.85 -&gt; 10.231.96.105 TCP [TCP Keep-Alive ACK] oob-ws-http &gt; nfs [ACK] Seq=55773 Ack=2 Win=1029 Len=0 TSV=953767461 TSER=122735063
  5   0.000011 10.231.96.105 -&gt; 10.231.96.85 TCP [TCP ZeroWindow] [TCP Keep-Alive] nfs &gt; oob-ws-http [ACK] Seq=1 Ack=1 Win=0 Len=0 TSV=122735999 TSER=828368381
  6   0.000015 10.231.96.85 -&gt; 10.231.96.105 TCP [TCP Keep-Alive ACK] oob-ws-http &gt; nfs [ACK] Seq=55773 Ack=2 Win=1029 Len=0 TSV=953767461 TSER=122735063
  7   0.000017 10.231.96.105 -&gt; 10.231.96.85 TCP [TCP ZeroWindow] [TCP Keep-Alive] nfs &gt; oob-ws-http [ACK] Seq=1 Ack=1 Win=0 Len=0 TSV=122735999 TSER=828368381
  8   0.000021 10.231.96.85 -&gt; 10.231.96.105 TCP [TCP Keep-Alive ACK] oob-ws-http &gt; nfs [ACK] Seq=55773 Ack=2 Win=1029 Len=0 TSV=953767461 TSER=122735063
  9   0.000022 10.231.96.105 -&gt; 10.231.96.85 TCP [TCP ZeroWindow] [TCP Keep-Alive] nfs &gt; oob-ws-http [ACK] Seq=1 Ack=1 Win=0 Len=0 TSV=122735999 TSER=828368381
 10   0.000026 10.231.96.85 -&gt; 10.231.96.105 TCP [TCP Keep-Alive ACK] oob-ws-http &gt; nfs [ACK] Seq=55773 Ack=2 Win=1029 Len=0 TSV=953767461 TSER=122735063</code></pre><p>What could cause this to happen? I thought it might've been described in Section 2.17 of RFC 2525 "Known TCP Implementation Problems" - <a href="http://www.ietf.org/rfc/rfc2525.txt:">http://www.ietf.org/rfc/rfc2525.txt:</a></p><blockquote><p>Name of Problem Failure to RST on close with data pending</p><p>Description When an application closes a connection in such a way that it can no longer read any received data, the TCP SHOULD, per section 4.2.2.13 of RFC 1122, send a RST if there is any unread received data, or if any new data is received. A TCP that fails to do so exhibits "Failure to RST on close with data pending".</p><pre><code> Note that, for some TCPs, this situation can be caused by an
 application &quot;crashing&quot; while a peer is sending data.

 We have observed a number of TCPs that exhibit this problem.  The
 problem is less serious if any subsequent data sent to the now-
 closed connection endpoint elicits a RST (see illustration below).</code></pre><p>Significance This problem is most significant for endpoints that engage in large numbers of connections, as their ability to do so will be curtailed as they leak away resources.</p><p>Implications Failure to reset the connection can lead to permanently hung connections, in which the remote endpoint takes no further action to tear down the connection because it is waiting on the local TCP to first take some action. This is particularly the case if the local TCP also allows the advertised window to go to zero, and fails to tear down the connection when the remote TCP engages in "persist" probes (see example below).</p></blockquote></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-zero-window" rel="tag" title="see questions tagged &#39;zero-window&#39;">zero-window</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jan '12, 10:25</strong></p><img src="https://secure.gravatar.com/avatar/bb2a6c0e2fc64197079b42004de7bcdc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="administraitor&#39;s gravatar image" /><p><span>administraitor</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="administraitor has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Sep '12, 08:42</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-8412" class="comments-container"><span id="14441"></span><div id="comment-14441" class="comment"><div id="post-14441-score" class="comment-score"></div><div class="comment-text"><p>Any chance you can post the actual pcap somewhere? And can you post the real seq#'s as opposed to relative numbers? Edit, Preference, Protocols, TCP, Relative sequence numbers"</p><p>Also, what is your window scaling factor?</p></div><div id="comment-14441-info" class="comment-info"><span class="comment-age">(21 Sep '12, 14:05)</span> <span class="comment-user userinfo">hansangb</span></div></div></div><div id="comment-tools-8412" class="comment-tools"></div><div class="clear"></div><div id="comment-8412-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8434"></span>

<div id="answer-container-8434" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8434-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8434-score" class="post-score" title="current number of votes">1</div><span id="post-8434-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The snippet you've included does seem to match up with the behavior you're seeing...but...the packet timestamps are confusing me. The endpoint that receives the ZeroWindow advert is supposed to wait for a while before sending a "zero window" probe - and that wait period is supposed to increase as more ZeroWindow adverts are received.</p><p>From <a href="http://www.usenix.org/publications/library/proceedings/bos94/full_papers/lin.a">http://www.usenix.org/publications/library/proceedings/bos94/full_papers/lin.a</a></p><blockquote><blockquote><ol><li>Keep sending data to the echo port without reading the echoed data.</li></ol></blockquote><p>As Figure 6 shows, because the probe program sends data without reading the echo, the receive buffer of TCP A eventually becomes full, causing it to send a zero-window ACK segment to TCP B. Because TCP B cannot send data to TCP A, the send buffer of TCP B will become full of echoed data. When the echo server on B cannot send more data, the receive buffer of TCP B will become full. Once the receive buffer of TCP B becomes full, it advertises a zero window to TCP A. After the zero-window condition exists for more than a threshold time period, both sides begin sending zero-window probes.</p><p>4.2 Results</p><p>Operating &amp; Data size in &amp; Min. probe &amp; Max. probe System<br />
&amp; 0-win probe seg. &amp; Interval &amp; Interval Solaris 2.1 &amp; 1 MSS octets &amp; 200 ms &amp; 60 sec. SunOS 4.1.1 &amp; 1 octet &amp; 5 sec. &amp; 60 sec. SunOS 4.0.3 &amp; 1 octet<br />
&amp; 5 sec. &amp; 60 sec. HP-UX 9.0<br />
&amp; 1 octet &amp; 4 sec. &amp; 60 sec.<br />
IRIX 5.1.1 &amp; 1 octet &amp; 5 sec.<br />
&amp; 60 sec.</p></blockquote><p>If I were a guessing man, and I am, I'd say that you're looking at some kind of stack implementation bug.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jan '12, 06:23</strong></p><img src="https://secure.gravatar.com/avatar/9e493496d59bb4ce33c37cd6e7a26a4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeonJay&#39;s gravatar image" /><p><span>GeonJay</span><br />
<span class="score" title="470 reputation points">470</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeonJay has 2 accepted answers">5%</span> </br></br></p></div></div><div id="comments-container-8434" class="comments-container"></div><div id="comment-tools-8434" class="comment-tools"></div><div class="clear"></div><div id="comment-8434-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

