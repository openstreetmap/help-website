+++
type = "question"
title = "Follow multiple TCP streams"
description = '''Is there any easy way to follow more than one TCP stream? The &#x27;Follow TCP Stream&#x27; will decode the data asociated with a single stream, and display by itself. However I have cases where data is effectively multiplexed over multiple TCP connections, and where I&#x27;d like to arrange all the data chronolog...'''
date = "2011-08-02T05:02:00Z"
lastmod = "2011-08-02T06:02:00Z"
weight = 5396
keywords = [ "tcp.stream", "tcp" ]
aliases = [ "/questions/5396" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Follow multiple TCP streams](/questions/5396/follow-multiple-tcp-streams)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5396-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5396-score" class="post-score" title="current number of votes">0</div><span id="post-5396-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there any easy way to follow more than one TCP stream? The 'Follow TCP Stream' will decode the data asociated with a single stream, and display by itself. However I have cases where data is effectively multiplexed over multiple TCP connections, and where I'd like to arrange all the data chronologically. I can - of course - try to view each stream and correlate against packet times, but this isn't as easy and is prone to user error.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp.stream" rel="tag" title="see questions tagged &#39;tcp.stream&#39;">tcp.stream</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Aug '11, 05:02</strong></p><img src="https://secure.gravatar.com/avatar/0c8509417939f553fb9681b6868ff099?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cbz&#39;s gravatar image" /><p><span>cbz</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cbz has no accepted answers">0%</span></p></div></div><div id="comments-container-5396" class="comments-container"></div><div id="comment-tools-5396" class="comment-tools"></div><div class="clear"></div><div id="comment-5396-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5398"></span>

<div id="answer-container-5398" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5398-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5398-score" class="post-score" title="current number of votes">0</div><span id="post-5398-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>How about this? <code>(tcp.stream eq i) or (tcp.stream eq j)</code> ... where both <code>i</code> and <code>j</code> are the numbers of the two streams you're interested in.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Aug '11, 06:02</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-5398" class="comments-container"></div><div id="comment-tools-5398" class="comment-tools"></div><div class="clear"></div><div id="comment-5398-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

