+++
type = "question"
title = "rtp.timestamp units"
description = '''What are the units of rtp.timestamp? When I capture RTP traffic, I have a field under Real-Time Transport Protocol that shows TimeStamp = 2218552874. What are the units of this number (sec, ms, usec, nsec)? And where does it come from? Mac Layer? Libpcap? System clock?'''
date = "2011-12-12T11:10:00Z"
lastmod = "2011-12-12T13:05:00Z"
weight = 7916
keywords = [ "timestamp", "rtp" ]
aliases = [ "/questions/7916" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [rtp.timestamp units](/questions/7916/rtptimestamp-units)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7916-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What are the units of <code>rtp.timestamp</code>? When I capture RTP traffic, I have a field under <em>Real-Time Transport Protocol</em> that shows <code>TimeStamp = 2218552874</code>.</p><p>What are the units of this number (sec, ms, usec, nsec)? And where does it come from? Mac Layer? Libpcap? System clock?</p></div><div id="question-tags" class="tags-container tags">timestamp rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Dec '11, 11:10</strong></p><img src="https://secure.gravatar.com/avatar/559f374efd2eaeaafac5616bbec62008?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AminGho&#39;s gravatar image" /><p>AminGho<br />
<span class="score" title="51 reputation points">51</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AminGho has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Dec '11, 14:06</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-7916" class="comments-container"></div><div id="comment-tools-7916" class="comment-tools"></div><div class="clear"></div><div id="comment-7916-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7924"></span>

<div id="answer-container-7924" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7924-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>From <a href="http://tools.ietf.org/html/rfc3550#page-13">RFC 3550</a>:</p><blockquote><pre><code>timestamp: 32 bits

  The timestamp reflects the sampling instant of the first octet in
  the RTP data packet.  The sampling instant MUST be derived from a
  clock that increments monotonically and linearly in time to allow
  synchronization and jitter calculations (see Section 6.4.1).  The
  resolution of the clock MUST be sufficient for the desired
  synchronization accuracy and for measuring packet arrival jitter
  (one tick per video frame is typically not sufficient).  The clock
  frequency is dependent on the format of data carried as payload
  and is specified statically in the profile or payload format
  specification that defines the format, or MAY be specified
  dynamically for payload formats defined through non-RTP means.</code></pre></blockquote><p>So there is no default timestamp unit.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '11, 13:05</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-7924" class="comments-container"><span id="7935"></span><div id="comment-7935" class="comment"><div id="post-7935-score" class="comment-score"></div><div class="comment-text"><p>Dear Jaap,</p><p>Thanks for you answer. Just to confirm, so there is no direct translation to any time measurement units from RTP timestamp!?</p><p>How about the MAC Timestamp in the Radio tap hearder? it says that the unit is in usec but for example what does this number means in usec : 84818688</p><p>Does it mean it took this much time (84818688 usec) to receive the packet? I doubt it because that's too long?</p><p>I really appreciate your help and comments on this.</p><p>Regards, Amin</p></div><div id="comment-7935-info" class="comment-info"><span class="comment-age">(13 Dec '11, 01:12)</span> AminGho</div></div><span id="7937"></span><div id="comment-7937" class="comment"><div id="post-7937-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>Just to confirm, so there is no direct translation to any time measurement units from RTP timestamp!?</p></blockquote><p>Well, there can be. From the quote:</p><pre><code>  The clock frequency is dependent on the format of data carried as payload
  and is specified statically in the profile or payload format specification
  that defines the format, or MAY be specified dynamically for payload 
  formats defined through non-RTP means.</code></pre><p>So, for instance, the PCMA codec has a fixed sample clock of 8kHz. That results in a timetick of 125 µs, for that given codec.</p></div><div id="comment-7937-info" class="comment-info"><span class="comment-age">(13 Dec '11, 02:21)</span> Jaap ♦</div></div></div><div id="comment-tools-7924" class="comment-tools"></div><div class="clear"></div><div id="comment-7924-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

