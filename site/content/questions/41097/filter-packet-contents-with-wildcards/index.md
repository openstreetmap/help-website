+++
type = "question"
title = "Filter Packet Contents with Wildcards"
description = '''I&#x27;m looking for a way to filter the contents of a packet for social security numbers using wildcards (-**-*).  Our UTM uses a builtin regular expression to identify US SSN&#x27;s passing through it. The UTM will notify us when it identifies a match, but we&#x27;ve been unable to validate it. I&#x27;m looking to se...'''
date = "2015-04-01T09:05:00Z"
lastmod = "2015-04-01T09:33:00Z"
weight = 41097
keywords = [ "filter", "capture-filter", "filters", "display-filter" ]
aliases = [ "/questions/41097" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filter Packet Contents with Wildcards](/questions/41097/filter-packet-contents-with-wildcards)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41097-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41097-score" class="post-score" title="current number of votes">0</div><span id="post-41097-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm looking for a way to filter the contents of a packet for social security numbers using wildcards (<strong><em>-**-</em></strong>*).<br />
</p><p>Our UTM uses a builtin regular expression to identify US SSN's passing through it. The UTM will notify us when it identifies a match, but we've been unable to validate it. I'm looking to see if the UTM is properly identifying them or if it is a false positive.</p><p>Any assistance you could provide would be much appreciated.</p><p>Please let me know if you have any questions.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-filters" rel="tag" title="see questions tagged &#39;filters&#39;">filters</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '15, 09:05</strong></p><img src="https://secure.gravatar.com/avatar/aa1de6de005d00e5baa84365224ee267?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="invadingrabbit&#39;s gravatar image" /><p><span>invadingrabbit</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="invadingrabbit has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-41097" class="comments-container"></div><div id="comment-tools-41097" class="comment-tools"></div><div class="clear"></div><div id="comment-41097-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41099"></span>

<div id="answer-container-41099" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41099-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41099-score" class="post-score" title="current number of votes">0</div><span id="post-41099-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please try this:</p><blockquote><p>frame contains "-\d+-\d+-"</p></blockquote><p><strong>contains</strong> allows you to use regular expressions in display filters.</p><p>HINT: If the data is transmitted over encrypted channels (HTTPS) you won't see anything and if the data is transmitted in binary form, the ASCII based regular expression won't match either.</p><p>If you can provide a capture file with a social security number in it, I will check if it's possible to match that with the mentioned filter.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Apr '15, 09:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-41099" class="comments-container"></div><div id="comment-tools-41099" class="comment-tools"></div><div class="clear"></div><div id="comment-41099-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

