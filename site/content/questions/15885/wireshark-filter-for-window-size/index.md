+++
type = "question"
title = "Wireshark filter for window size"
description = '''Hi. Is there a way to graph packets&#x27; window size. What I want to do is to see how TCP stream&#x27;s receive window size changes in the I/O graph. I&#x27;m aware of the tcp.window_size and tcp.window_size_value filters but those just graph every packet that has any window size in the first place. Thanks. -Rakk...'''
date = "2012-11-14T00:55:00Z"
lastmod = "2015-04-26T02:38:00Z"
weight = 15885
keywords = [ "filter", "window", "tcp", "size" ]
aliases = [ "/questions/15885" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark filter for window size](/questions/15885/wireshark-filter-for-window-size)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15885-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15885-score" class="post-score" title="current number of votes">0</div><span id="post-15885-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. Is there a way to graph packets' window size. What I want to do is to see how TCP stream's receive window size changes in the I/O graph. I'm aware of the tcp.window_size and tcp.window_size_value filters but those just graph every packet that has any window size in the first place. Thanks.</p><p>-Rakki</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-window" rel="tag" title="see questions tagged &#39;window&#39;">window</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-size" rel="tag" title="see questions tagged &#39;size&#39;">size</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '12, 00:55</strong></p><img src="https://secure.gravatar.com/avatar/387f58c09269aee8709bb3d68f33ea93?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rakki&#39;s gravatar image" /><p><span>rakki</span><br />
<span class="score" title="0 reputation points">0</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rakki has no accepted answers">0%</span></p></div></div><div id="comments-container-15885" class="comments-container"><span id="41851"></span><div id="comment-41851" class="comment"><div id="post-41851-score" class="comment-score"></div><div class="comment-text"><p>If you want to plot the value of a field, you can do this with the advanced plot features in the I/O Graph dialog.</p></div><div id="comment-41851-info" class="comment-info"><span class="comment-age">(26 Apr '15, 02:38)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-15885" class="comment-tools"></div><div class="clear"></div><div id="comment-15885-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="15886"></span>

<div id="answer-container-15886" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15886-score" class="post-score" title="current number of votes">2</div><span id="post-15886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>did you try this?</p><blockquote><p><code>Statistics -&gt; TCP Stream Graph -&gt; Window Scaling Graph</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '12, 01:23</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-15886" class="comments-container"><span id="15888"></span><div id="comment-15888" class="comment"><div id="post-15888-score" class="comment-score"></div><div class="comment-text"><p>Exactly what I was looking for. Thanks, Kurt.</p></div><div id="comment-15888-info" class="comment-info"><span class="comment-age">(14 Nov '12, 01:43)</span> <span class="comment-user userinfo">rakki</span></div></div><span id="15904"></span><div id="comment-15904" class="comment"><div id="post-15904-score" class="comment-score"></div><div class="comment-text"><p>If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-15904-info" class="comment-info"><span class="comment-age">(14 Nov '12, 07:45)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-15886" class="comment-tools"></div><div class="clear"></div><div id="comment-15886-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15887"></span>

<div id="answer-container-15887" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15887-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15887-score" class="post-score" title="current number of votes">2</div><span id="post-15887-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Besides the answer of <span>@Kurt</span>: you can see also the Window size in the TCP Time-Sequence Graph when choosing the tcptrace style. The window size is the line above the actual sequence number line, and in that graph it is very nice to see how the sequence numbers relate to the remaining window size. The same graph also shows a third line (below the sequence line) that will tell you what has been ACKed.</p><p>Also, you could add a column to your Wireshark setup containing the window size and export the packet list as CSV. That way you can graph whatever you like in programs like Excel or similar tools.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '12, 01:40</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-15887" class="comments-container"></div><div id="comment-tools-15887" class="comment-tools"></div><div class="clear"></div><div id="comment-15887-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

