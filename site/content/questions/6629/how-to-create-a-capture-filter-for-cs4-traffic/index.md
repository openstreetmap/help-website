+++
type = "question"
title = "How to create a capture filter for CS4 Traffic"
description = '''How can i create a capture filter for CS4 traffic? When I look at the captured traffic, I see the Differentiated Services Field: 0x80 (DSCP 0x20: Class Selector 4. '''
date = "2011-09-28T16:49:00Z"
lastmod = "2011-09-30T10:02:00Z"
weight = 6629
keywords = [ "cs4", "capture-filter", "af41", "dscp" ]
aliases = [ "/questions/6629" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to create a capture filter for CS4 Traffic](/questions/6629/how-to-create-a-capture-filter-for-cs4-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6629-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6629-score" class="post-score" title="current number of votes">0</div><span id="post-6629-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can i create a capture filter for CS4 traffic?</p><p>When I look at the captured traffic, I see the Differentiated Services Field: 0x80 (DSCP 0x20: Class Selector 4.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-cs4" rel="tag" title="see questions tagged &#39;cs4&#39;">cs4</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-af41" rel="tag" title="see questions tagged &#39;af41&#39;">af41</span> <span class="post-tag tag-link-dscp" rel="tag" title="see questions tagged &#39;dscp&#39;">dscp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Sep '11, 16:49</strong></p><img src="https://secure.gravatar.com/avatar/1224b4a335d2e0c52c402942d937e645?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="miler&#39;s gravatar image" /><p><span>miler</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="miler has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Sep '11, 09:59</strong> </span></p></div></div><div id="comments-container-6629" class="comments-container"></div><div id="comment-tools-6629" class="comment-tools"></div><div class="clear"></div><div id="comment-6629-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6655"></span>

<div id="answer-container-6655" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6655-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6655-score" class="post-score" title="current number of votes">0</div><span id="post-6655-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jaap has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That worked perfectly, using ip[1] &amp; 0xfc == 0x80 I was able to do perform a packet capture and only capture CS4 packets. Additionally, based on your response I was able to learn how to setup a capture filter for AF41: ip[1] &amp; 0xfc == 0x88<br />
</p><p>I tested the AF41 filter and that worked as well.<br />
</p><p>Thanks for the solution.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '11, 10:02</strong></p><img src="https://secure.gravatar.com/avatar/1224b4a335d2e0c52c402942d937e645?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="miler&#39;s gravatar image" /><p><span>miler</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="miler has one accepted answer">100%</span> </br></br></p></div></div><div id="comments-container-6655" class="comments-container"></div><div id="comment-tools-6655" class="comment-tools"></div><div class="clear"></div><div id="comment-6655-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6630"></span>

<div id="answer-container-6630" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6630-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6630-score" class="post-score" title="current number of votes">2</div><span id="post-6630-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That would be <code>ip[1] &amp; 0xfc == 0x80</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '11, 23:42</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6630" class="comments-container"></div><div id="comment-tools-6630" class="comment-tools"></div><div class="clear"></div><div id="comment-6630-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

