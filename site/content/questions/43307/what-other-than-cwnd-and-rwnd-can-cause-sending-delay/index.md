+++
type = "question"
title = "What other than CWND and RWND can cause sending delay?"
description = '''Investigating some sending latency in a packet capture shows a continual pattern of packet sends sometimes waiting for an incoming Ack: -&amp;gt; Timely outgoing packet -&amp;gt; Timely outgoing packet .. (waiting) &amp;lt;- Ack -&amp;gt; Delayed outgoing packet  Strace shows the write calls to the kernal are all t...'''
date = "2015-06-18T00:33:00Z"
lastmod = "2015-06-18T00:33:00Z"
weight = 43307
keywords = [ "tcppackets" ]
aliases = [ "/questions/43307" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What other than CWND and RWND can cause sending delay?](/questions/43307/what-other-than-cwnd-and-rwnd-can-cause-sending-delay)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43307-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43307-score" class="post-score" title="current number of votes">0</div><span id="post-43307-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Investigating some sending latency in a packet capture shows a continual pattern of packet sends sometimes waiting for an incoming Ack:</p><pre><code>-&gt; Timely outgoing packet
-&gt; Timely outgoing packet
.. (waiting)
&lt;- Ack
-&gt; Delayed outgoing packet</code></pre><p>Strace shows the write calls to the kernal are all timely. TCP no delay is enabled. The two main obvious candidates for the kernel awaiting an ack before sending a buffered packet would be congestion window or receiver window. But there is no packet loss at all, so presumably the cwnd will be sufficiently high, and the window sizes in the incoming acks show no problems with rwnd values. Are there any other reasons that could delay a packet being sent before an ack is received?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcppackets" rel="tag" title="see questions tagged &#39;tcppackets&#39;">tcppackets</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jun '15, 00:33</strong></p><img src="https://secure.gravatar.com/avatar/9ce49d8ccbe223631140d6f15d2b893b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="glyn_walters&#39;s gravatar image" /><p><span>glyn_walters</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="glyn_walters has no accepted answers">0%</span></p></div></div><div id="comments-container-43307" class="comments-container"></div><div id="comment-tools-43307" class="comment-tools"></div><div class="clear"></div><div id="comment-43307-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

