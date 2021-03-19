+++
type = "question"
title = "Connection stays established after RST packet"
description = '''Hello, After server receives RST packet conection stays ESTABLISHED and setting new connection on the same ports is impossible. Can anybody point me why? Thanks for help.  12809 76687.618015000 client server TCP 396 16081→4210 [PSH, ACK] Seq=53 Ack=53 Win=65483 Len=330 TSval=2670952 TSecr=2913999211...'''
date = "2014-12-03T08:58:00Z"
lastmod = "2014-12-08T09:28:00Z"
weight = 38308
keywords = [ "rst" ]
aliases = [ "/questions/38308" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Connection stays established after RST packet](/questions/38308/connection-stays-established-after-rst-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38308-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38308-score" class="post-score" title="current number of votes">0</div><span id="post-38308-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>After server receives RST packet conection stays ESTABLISHED and setting new connection on the same ports is impossible. Can anybody point me why?</p><p>Thanks for help.</p><pre><code>    12809   76687.618015000 client  server  TCP 396 16081→4210 [PSH, ACK] Seq=53 Ack=53 Win=65483 Len=330 TSval=2670952 TSecr=2913999211
    12810   76687.618204000 server  client  TCP 66  4210→16081 [ACK] Seq=2711635446 Ack=3631645278 Win=15616 Len=0 TSval=2989694647 TSecr=2670952
    12811   76688.352263000 server  client  TCP 422 4210→16081 [PSH, ACK] Seq=2711635446 Ack=3631645278 Win=15616 Len=356 TSval=2989695381 TSecr=2670952
    12812   76688.489380000 client  server  TCP 66  16081→4210 [ACK] Seq=383 Ack=409 Win=65127 Len=0 TSval=2670960 TSecr=2989695381
    27223   163174.555440000    client  server  TCP 60  16081→4210 [RST, ACK] Seq=384 Ack=409 Win=0 Len=0
    27224   163174.555562000    server  client  TCP 66  [TCP Dup ACK 12811#1] 4210→16081 [ACK] Seq=2711635802 Ack=3631645278 Win=15616 Len=0 TSval=3076181584 TSecr=2670960
    27277   163485.076719000    client  server  TCP 78  [TCP Port numbers reused] 16081→4210 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 WS=1 TSval=0 TSecr=0 SACK_PERM=1
    27278   163488.154351000    client  server  TCP 78  [TCP Retransmission] 16081→4210 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 WS=1 TSval=0 TSecr=0 SACK_PERM=1
More SYN packets ...</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Dec '14, 08:58</strong></p><img src="https://secure.gravatar.com/avatar/b36472be5d0e708ab8e37b91b0efff41?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JozefB&#39;s gravatar image" /><p><span>JozefB</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JozefB has no accepted answers">0%</span></p></div></div><div id="comments-container-38308" class="comments-container"><span id="38312"></span><div id="comment-38312" class="comment"><div id="post-38312-score" class="comment-score"></div><div class="comment-text"><p>Seems Tcp port 16081 is reused by client after 5 seconds, we can reuse the same socket but only if the SYN packet contains a sequence number which is larger than was previously used.for your reference <a href="http://blog.davidvassallo.me/2010/07/13/time_wait-and-port-reuse/">http://blog.davidvassallo.me/2010/07/13/time_wait-and-port-reuse/</a></p></div><div id="comment-38312-info" class="comment-info"><span class="comment-age">(03 Dec '14, 21:01)</span> <span class="comment-user userinfo">kishan pandey</span></div></div><span id="38319"></span><div id="comment-38319" class="comment"><div id="post-38319-score" class="comment-score"></div><div class="comment-text"><p>Port 16081 is reused after more than 5 minutes (after RST) but i think it doesn't matter (no FIN). Shouldn't connection change state to CLOSED after server receives RST/ACK segment? Now it stays ESTABLISHED.</p></div><div id="comment-38319-info" class="comment-info"><span class="comment-age">(04 Dec '14, 03:31)</span> <span class="comment-user userinfo">JozefB</span></div></div></div><div id="comment-tools-38308" class="comment-tools"></div><div class="clear"></div><div id="comment-38308-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38370"></span>

<div id="answer-container-38370" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38370-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38370-score" class="post-score" title="current number of votes">0</div><span id="post-38370-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming this is a trace taken at the client, I'd say the reset did not make it to the server's TCP layer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '14, 10:49</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-38370" class="comments-container"><span id="38440"></span><div id="comment-38440" class="comment"><div id="post-38440-score" class="comment-score"></div><div class="comment-text"><p>The trace was taken at the server.</p></div><div id="comment-38440-info" class="comment-info"><span class="comment-age">(08 Dec '14, 07:17)</span> <span class="comment-user userinfo">JozefB</span></div></div><span id="38444"></span><div id="comment-38444" class="comment"><div id="post-38444-score" class="comment-score"></div><div class="comment-text"><p>RFC 793 Says,In all states except SYN-SENT, all reset (RST) segments are validated by checking their SEQ-fields. A reset is valid if its sequence number is in the window. In the SYN-SENT state (a RST received in response to an initial SYN), the RST is acceptable if the ACK field acknowledges the SYN.Can you post the capture because in capture seq no. are not matching not sure why(because relative sequence feature or capture taken at some proxy or FW device)</p></div><div id="comment-38444-info" class="comment-info"><span class="comment-age">(08 Dec '14, 09:28)</span> <span class="comment-user userinfo">kishan pandey</span></div></div></div><div id="comment-tools-38370" class="comment-tools"></div><div class="clear"></div><div id="comment-38370-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

