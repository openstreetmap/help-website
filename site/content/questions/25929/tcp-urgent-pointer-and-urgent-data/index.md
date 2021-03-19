+++
type = "question"
title = "TCP urgent pointer and urgent data"
description = '''Hi, In the TCP header, the urgent pointer points to the last byte of the urgent data, if present. I couldn&#x27;t understand what&#x27;s the idea behind this. What could this be possibly used for? I think that beginning of the urgent data might be more useful as it would help TCP (on the receiving end) know w...'''
date = "2013-10-11T22:56:00Z"
lastmod = "2013-10-12T03:45:00Z"
weight = 25929
keywords = [ "tcp" ]
aliases = [ "/questions/25929" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP urgent pointer and urgent data](/questions/25929/tcp-urgent-pointer-and-urgent-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25929-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>In the TCP header, the urgent pointer points to the last byte of the urgent data, if present.</p><p>I couldn't understand what's the idea behind this. What could this be possibly used for? I think that beginning of the urgent data might be more useful as it would help TCP (on the receiving end) know where exactly the urgent data begins and ends.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '13, 22:56</strong></p><img src="https://secure.gravatar.com/avatar/ebc6c07016107ce674e93e9d7293e59a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hdnivara&#39;s gravatar image" /><p>hdnivara<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hdnivara has no accepted answers">0%</span></p></div></div><div id="comments-container-25929" class="comments-container"></div><div id="comment-tools-25929" class="comment-tools"></div><div class="clear"></div><div id="comment-25929-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25933"></span>

<div id="answer-container-25933" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25933-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is a <a href="http://tools.ietf.org/html/rfc6093">recent survey of the <strong>urgent mechanism</strong></a> and the current implementations. Actually there seems to exist some 'confusion' about the urgent mechanism, because of 'errors' in RFCs and different implementations. Especially the definition of the urgent pointer (how to interpret it) has been unclear in several RFCs. See <a href="http://tools.ietf.org/html/rfc6093">RFC6093 On the Implementation of the TCP Urgent Mechanism</a>.</p><blockquote><p>I couldn't understand what's the idea behind this.</p></blockquote><p>The urgent flag and the urgent pointer simply tells the receiver when to enter "urgent data mode" and when to leave it. Enter it, when you receiver a segment with urgent flag set and leave it, when the segment with SEQ+urgent pointer has been received (see 2.1. Semantics of Urgent Indications in RFC 6093).</p><p>From <a href="http://tools.ietf.org/html/rfc793">RFC793</a></p><pre><code>  TCP also provides a means to communicate to the receiver of data that
  at some point further along in the data stream than the receiver is
  currently reading there is urgent data.  TCP does not attempt to
  define what the user specifically does upon being notified of pending
  urgent data, but the general notion is that the receiving process will
  take action to process the urgent data quickly.</code></pre><p>So, we define that there might be a thing called "urgent data", but we don't tell you why and what to do whit them. What exactly is meant by "take action" and "process quickly"? Well..., the early RFCs are sometimes more like a philosophical statement than a clear technical description ;-).</p><p>So, what is it good for? Apparently some applications use the urgent mechanism to send out-of-band data. TCP itself defines no control channel mechanism for a connection. So, if you need a control channel you either have two connections like FTP (control and data channel) or you add control data by the use of the urgent mechanism to implement out-of-band data (like a control channel). See: <a href="http://alas.matf.bg.ac.rs/manuals/lspe/snode=126.html">http://alas.matf.bg.ac.rs/manuals/lspe/snode=126.html</a></p><p>However RFC6093 states:</p><pre><code>   It should be reinforced that the aforementioned implementations are
   broken.  The TCP urgent mechanism is not a mechanism for delivering
   &quot;out-of-band&quot; data.</code></pre><p>So, yes it <strong>can</strong> be used as an out-of-band mechanism and it <strong>is</strong> used (e.g. telnet), however RFC6093 mandates not to do it.</p><p>RFC6093 is more clear on the whole thing.</p><pre><code>5. Advice to New Applications Employing TCP

   As a result of the issues discussed in Section 3.2 and Section 3.4,
   new applications SHOULD NOT employ the TCP urgent mechanism.
   However, TCP implementations MUST still include support for the
   urgent mechanism such that existing applications can still use it.</code></pre><p>In simple words. Don't use it.</p><p>Now it's up to the reader to decide: Follow the latest RFC or the "best practice approach"? ;-)</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Oct '13, 03:45</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Oct '13, 09:06</p></div></div><div id="comments-container-25933" class="comments-container"></div><div id="comment-tools-25933" class="comment-tools"></div><div class="clear"></div><div id="comment-25933-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

