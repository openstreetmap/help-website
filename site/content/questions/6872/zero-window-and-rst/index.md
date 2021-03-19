+++
type = "question"
title = "Zero window and RST"
description = '''Hi Experts, I am facing with the follwoving contradiction. In RFC 793 can be read the following sentences: once: &quot;all reset (RST) segments are validated by checking their SEQ-fields. A reset is valid if its sequence number is in the window.&quot; on other part of the doc: &quot;However, when the receive windo...'''
date = "2011-10-12T09:43:00Z"
lastmod = "2012-03-06T01:27:00Z"
weight = 6872
keywords = [ "rst", "rfc793", "zero-window", "tcp" ]
aliases = [ "/questions/6872" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Zero window and RST](/questions/6872/zero-window-and-rst)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6872-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Experts,</p><p>I am facing with the follwoving contradiction. In RFC 793 can be read the following sentences:</p><p>once: "all reset (RST) segments are validated by checking their SEQ-fields. A reset is valid if its sequence number is in the window."</p><p>on other part of the doc: "However, when the receive window is zero, a TCP must process the RST and URG fields of all incoming segments"</p><p>Which is "more" true?</p><p>My exact problem is, that I have to decide, and declare which device is wrong (a client or Cisco ACE). The problem begins, when the server (ACE) sends a FIN. The communication looks like this (client:100.1.1.7):</p><pre><code>  1 19:30:57.486 100.1.1.7             100.1.1.2             64    TCP      51591 &gt; 33067 [SYN] Seq=0 Win=0 Len=0 MSS=1400
  2 19:30:57.498 100.1.1.2             100.1.1.7             64    TCP      33067 &gt; 51591 [SYN, ACK] Seq=0 Ack=1 Win=8192 Len=0 MSS=1460
  3 19:30:57.532 100.1.1.7             100.1.1.2             64    TCP      51591 &gt; 33067 [ACK] Seq=1 Ack=1 Win=4095 Len=0
  4 19:31:00.720 100.1.1.7             100.1.1.2             201   TCP      51591 &gt; 33067 [PSH, ACK] Seq=1 Ack=1 Win=4095 Len=143
  5 19:31:00.781 100.1.1.2             100.1.1.7             64    TCP      33067 &gt; 51591 [ACK] Seq=1 Ack=144 Win=8192 Len=0
  6 19:31:00.797 100.1.1.2             100.1.1.7             140   TCP      33067 &gt; 51591 [PSH, ACK] Seq=1 Ack=144 Win=8192 Len=82
  7 19:31:00.800 100.1.1.2             100.1.1.7             64    TCP      33067 &gt; 51591 [FIN, ACK] Seq=83 Ack=144 Win=8192 Len=0
  8 19:31:00.863 100.1.1.7             100.1.1.2             64    TCP      51591 &gt; 33067 [ACK] Seq=144 Ack=83 Win=4013 Len=0
  9 19:31:00.874 100.1.1.7             100.1.1.2             64    TCP      [TCP ZeroWindow] 51591 &gt; 33067 [ACK] Seq=144 Ack=84 Win=0 Len=0
 10 19:31:04.381 100.1.1.7             100.1.1.2             64    TCP      51591 &gt; 33067 [RST] Seq=145 Win=0 Len=0
 11 19:31:04.382 100.1.1.2             100.1.1.7             64    TCP      [TCP ZeroWindow] 33067 &gt; 51591 [ACK] Seq=84 Ack=144 Win=0 Len=0</code></pre><p>The client doesn't replies normally to the FIN, it replies wit a simple ACK (#8), with unchanged ACK field. Furthermore it sends a zero window ACK (#9) where Ack+1. This window size shouldn't influence the server side rcv.wnd, which was 8192 in packet #6 and #7. Here comes the worst, that the server ignores the incoming (#10) RST packet (comes with Ack+1), and pretends like the sesion is still open. In the next message (#11) server sets zero window as well with seq=144) This is my question: should the server process this RST? What is the server side rcv.wnd size when the RST arrives, and if it were zero, shuld have process the RST if that has an out-of-window seq or not? (server ack=144+0 win.siz. incoming RST seq=145). This is a special communication, where the client and server uses fixed TCP src and dst ports, thus the client cannot re-estabilis a conn, until the server runs on timeout (several minutes).</p><p>The converstaion follows like this:</p><pre><code> 12 19:42:14.450 100.1.1.7             100.1.1.2             64    TCP      [TCP Port numbers reused] 51591 &gt; 33067 [SYN] Seq=0 Win=0 Len=0 MSS=1400
 13 19:42:14.450 100.1.1.2             100.1.1.7             64    TCP      [TCP ZeroWindow] 33067 &gt; 51591 [ACK] Seq=1 Ack=3592380271 Win=0 Len=0
 14 19:42:16.596 100.1.1.7             100.1.1.2             64    TCP      51591 &gt; 33067 [SYN] Seq=0 Win=0 Len=0 MSS=1400
 15 19:42:16.596 100.1.1.2             100.1.1.7             64    TCP      [TCP ZeroWindow] 33067 &gt; 51591 [ACK] Seq=1 Ack=3592380271 Win=0 Len=0
 16 19:42:18.622 100.1.1.7             100.1.1.2             64    TCP      51591 &gt; 33067 [SYN] Seq=0 Win=0 Len=0 MSS=1400
 17 19:42:18.622 100.1.1.2             100.1.1.7             64    TCP      [TCP ZeroWindow] 33067 &gt; 51591 [ACK] Seq=1 Ack=3592380271 Win=0 Len=0
 18 19:42:22.893 100.1.1.7             100.1.1.2             64    TCP      51591 &gt; 33067 [SYN] Seq=0 Win=0 Len=0 MSS=1400
 19 19:42:22.893 100.1.1.2             100.1.1.7             64    TCP      [TCP ZeroWindow] 33067 &gt; 51591 [ACK] Seq=1 Ack=3592380271 Win=0 Len=0
 20 19:42:30.896 100.1.1.7             100.1.1.2             64    TCP      51591 &gt; 33067 [SYN] Seq=0 Win=0 Len=0 MSS=1400
 21 19:42:30.896 100.1.1.2             100.1.1.7             64    TCP      [TCP ZeroWindow] 33067 &gt; 51591 [ACK] Seq=1 Ack=3592380271 Win=0 Len=0</code></pre><p>etc.</p><p>Thank you for your help in advance.</p><p>BR: jonagy</p></div><div id="question-tags" class="tags-container tags">rst rfc793 zero-window tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Oct '11, 09:43</strong></p><img src="https://secure.gravatar.com/avatar/85d8fe8a9beb6ee92840fad4ad52f373?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jonagy&#39;s gravatar image" /><p>jonagy<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jonagy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Feb '12, 19:25</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-6872" class="comments-container"><span id="9315"></span><div id="comment-9315" class="comment"><div id="post-9315-score" class="comment-score"></div><div class="comment-text"><p>@ jonagy: Still an issue?</p></div><div id="comment-9315-info" class="comment-info"><span class="comment-age">(02 Mar '12, 10:59)</span> Landi</div></div><span id="9387"></span><div id="comment-9387" class="comment"><div id="post-9387-score" class="comment-score"></div><div class="comment-text"><p>not really, without final conclusion</p></div><div id="comment-9387-info" class="comment-info"><span class="comment-age">(06 Mar '12, 01:11)</span> jonagy</div></div></div><div id="comment-tools-6872" class="comment-tools"></div><div class="clear"></div><div id="comment-6872-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9389"></span>

<div id="answer-container-9389" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9389-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>From what I see:</p><ul><li>The Server sending a FIN in #7 means "no more data from me", so the zero window from the client in #9 is perfectly fine, though unusual - but since no more data from the other side it is ok</li><li>The RST from the server in #10 though doesn't have a matching SEQnr. because it should ne 144 there. Normally wihtin rec. window this should not be a problem, but if you take a look at the delta time between #10 and #11, you see that the RST cannot have yet arrived at the other side when you see the window update in #11, setting rec.window to zero. Here I see the issue, because after the FIN in #7 over 3 seconds passed with the other side sending no data, which could have triggered the rec.window being set to zero (just a guess). Anyways -&gt; the RST is out of the rec.window with SEQnr. 145, so I guess that's why is is not accepted and the session is still open.</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '12, 01:27</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Mar '12, 01:27</p></div></div><div id="comments-container-9389" class="comments-container"><span id="9390"></span><div id="comment-9390" class="comment"><div id="post-9390-score" class="comment-score"></div><div class="comment-text"><p>thank you for sharing your views on this.</p></div><div id="comment-9390-info" class="comment-info"><span class="comment-age">(06 Mar '12, 02:06)</span> jonagy</div></div></div><div id="comment-tools-9389" class="comment-tools"></div><div class="clear"></div><div id="comment-9389-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

