+++
type = "question"
title = "Filter by TCP Connection (handshake) time."
description = '''I&#x27;m looking to filter data by how long the TCP handshake took.  By this, I mean the time between the first SYN and the last ACK (after the FIN-ACK).  Is this something I can do in wireshark, or something I&#x27;m going to have to sort through by hand?'''
date = "2014-04-02T09:21:00Z"
lastmod = "2014-04-02T12:36:00Z"
weight = 31401
keywords = [ "duration", "connection", "tcp", "time" ]
aliases = [ "/questions/31401" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filter by TCP Connection (handshake) time.](/questions/31401/filter-by-tcp-connection-handshake-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31401-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31401-score" class="post-score" title="current number of votes">0</div><span id="post-31401-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm looking to filter data by how long the TCP handshake took.</p><p>By this, I mean the time between the first SYN and the last ACK (after the FIN-ACK).</p><p>Is this something I can do in wireshark, or something I'm going to have to sort through by hand?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-duration" rel="tag" title="see questions tagged &#39;duration&#39;">duration</span> <span class="post-tag tag-link-connection" rel="tag" title="see questions tagged &#39;connection&#39;">connection</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Apr '14, 09:21</strong></p><img src="https://secure.gravatar.com/avatar/8250d92afcd545710fdbc8d35dda489b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TrolliOlli&#39;s gravatar image" /><p><span>TrolliOlli</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TrolliOlli has no accepted answers">0%</span></p></div></div><div id="comments-container-31401" class="comments-container"></div><div id="comment-tools-31401" class="comment-tools"></div><div class="clear"></div><div id="comment-31401-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31421"></span>

<div id="answer-container-31421" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31421-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31421-score" class="post-score" title="current number of votes">0</div><span id="post-31421-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The connections overview will show this (to some extend).</p><blockquote><p>Statistics -&gt; Conversations -&gt; TCP [tab]</p></blockquote><p>Then sort the conversations for the column 'duration'.</p><p>Hint: This will also show not yet 'completed' TCP sessions, simply because the capture process was ended while the connections were still active!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '14, 12:36</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-31421" class="comments-container"></div><div id="comment-tools-31421" class="comment-tools"></div><div class="clear"></div><div id="comment-31421-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

