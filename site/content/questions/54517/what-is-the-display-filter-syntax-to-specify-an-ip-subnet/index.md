+++
type = "question"
title = "What is the display filter syntax to specify an IP subnet?"
description = '''In the display filter, &#x27;net&#x27; is not even in the list of expressions/filters to apply. When you type &#x27;net&#x27; in the display filter field, it goes red and shows a list of options - none of which correspond to anything having to do with searching for an entire subnet.  This feature would be nice though a...'''
date = "2016-08-02T08:16:00Z"
lastmod = "2016-08-02T08:24:00Z"
weight = 54517
keywords = [ "filter", "capture", "display" ]
aliases = [ "/questions/54517" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What is the display filter syntax to specify an IP subnet?](/questions/54517/what-is-the-display-filter-syntax-to-specify-an-ip-subnet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54517-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54517-score" class="post-score" title="current number of votes">1</div><span id="post-54517-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In the display filter, 'net' is not even in the list of expressions/filters to apply. When you type 'net' in the display filter field, it goes red and shows a list of options - none of which correspond to anything having to do with searching for an entire subnet. This feature would be nice though and if it does exist let us know the real deal.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Aug '16, 08:16</strong></p><img src="https://secure.gravatar.com/avatar/a441d91a7fef635a72174ba2d9eecf53?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DBP1968&#39;s gravatar image" /><p><span>DBP1968</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DBP1968 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>02 Aug '16, 08:36</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-54517" class="comments-container"></div><div id="comment-tools-54517" class="comment-tools"></div><div class="clear"></div><div id="comment-54517-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54518"></span>

<div id="answer-container-54518" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54518-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54518-score" class="post-score" title="current number of votes">3</div><span id="post-54518-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That's because you mix up <strong>capture</strong> filters (which the Question to which you have originally piggy-backed your one deals with) and <strong>display</strong> filters (which can be Applied).</p><p>Ιn the display filter, you can use IP subnets (or even IP ranges if you want): <code>ip.addr == 10.5.232.0/24</code> has the same effect like <code>ip.addr &gt;= 10.5.232.0 and ip.addr &lt;= 10.5.232.255</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Aug '16, 08:24</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Aug '16, 11:10</strong> </span></p></div></div><div id="comments-container-54518" class="comments-container"></div><div id="comment-tools-54518" class="comment-tools"></div><div class="clear"></div><div id="comment-54518-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

