+++
type = "question"
title = "Round trip time direction"
description = '''I have some basic questions about calculating round trip time in wireshark as I have some mis-understandings about it. After filtering my TCP session (http download), to get the RTT time, it looks like we need to select the source port from the server e.g. 80, then plot RTT graph. If I was tracing f...'''
date = "2014-02-27T06:27:00Z"
lastmod = "2014-02-27T13:44:00Z"
weight = 30233
keywords = [ "rtt" ]
aliases = [ "/questions/30233" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Round trip time direction](/questions/30233/round-trip-time-direction)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30233-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30233-score" class="post-score" title="current number of votes">0</div><span id="post-30233-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have some basic questions about calculating round trip time in wireshark as I have some mis-understandings about it. After filtering my TCP session (http download), to get the RTT time, it looks like we need to select the source port from the server e.g. 80, then plot RTT graph.</p><p>If I was tracing from the server I guess I would select destination port of 80? to see the RTT time to the client.</p><p>From the client perspective if I was uploading e.g. a large post request and wanted to get RTT for that session, would I still select source port=80? i.e to get the RTT time that the server was acknowledged my requests?</p><p>What is the difference between selecting an ack packet in the tcp stream and plotting a RTT graph, and selecting "statistics/io graphs, filtering on source port=80, and then tcp.analysis.ack.rtt" ? I am asking as from the former I see higher values than the latter (even selecting MAX in statistics section).</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtt" rel="tag" title="see questions tagged &#39;rtt&#39;">rtt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Feb '14, 06:27</strong></p><img src="https://secure.gravatar.com/avatar/88b9a87459850d6b19d660a07a417924?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Brummy&#39;s gravatar image" /><p><span>Brummy</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Brummy has no accepted answers">0%</span></p></div></div><div id="comments-container-30233" class="comments-container"></div><div id="comment-tools-30233" class="comment-tools"></div><div class="clear"></div><div id="comment-30233-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30246"></span>

<div id="answer-container-30246" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30246-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30246-score" class="post-score" title="current number of votes">0</div><span id="post-30246-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unless you are interesting in the 'internal' RTT through the TCPIP stack you typically need to select inbound packets to measure the 'network' RTT. So <code>!ip.src == 10.11.1.10 and tcp.analysis.ack_rtt</code> looks like a more generic filter for all sessions. If you are interested in the RTT to a certain destination address you'd select the remote address as ip.src</p><p>"What is the difference between selecting an ack packet in the tcp stream and plotting a RTT graph, and selecting "statistics/io graphs, filtering on source port=80, and then tcp.analysis.ack.rtt" ? I am asking as from the former I see higher values than the latter (even selecting MAX in statistics section)."</p><p>The statistics RTT Graph plots for <em><em>every</em></em> packet whereas the io graph builds the min/max/avg of all packets within the tick interval so to get realistic results you need to shrink the tick interval as much as needed depending on the packet rate of the acks..</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Feb '14, 13:44</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-30246" class="comments-container"></div><div id="comment-tools-30246" class="comment-tools"></div><div class="clear"></div><div id="comment-30246-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

