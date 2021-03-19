+++
type = "question"
title = "Multicore scaling?"
description = '''Any plans for this? On larger files, would significantly speed up the use of complex display filters.'''
date = "2011-02-02T07:33:00Z"
lastmod = "2011-02-02T18:45:00Z"
weight = 2104
keywords = [ "filter", "multicore" ]
aliases = [ "/questions/2104" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Multicore scaling?](/questions/2104/multicore-scaling)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2104-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2104-score" class="post-score" title="current number of votes">0</div><span id="post-2104-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Any plans for this? On larger files, would significantly speed up the use of complex display filters.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-multicore" rel="tag" title="see questions tagged &#39;multicore&#39;">multicore</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Feb '11, 07:33</strong></p><img src="https://secure.gravatar.com/avatar/df586f16ccf93c27cac38f433ce07777?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rancur3p1c&#39;s gravatar image" /><p><span>rancur3p1c</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rancur3p1c has no accepted answers">0%</span></p></div></div><div id="comments-container-2104" class="comments-container"></div><div id="comment-tools-2104" class="comment-tools"></div><div class="clear"></div><div id="comment-2104-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2106"></span>

<div id="answer-container-2106" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2106-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2106-score" class="post-score" title="current number of votes">1</div><span id="post-2106-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think it's on a lot of developer's minds, but it is not/will not be easy.</p><p>There is a <a href="http://wiki.wireshark.org/Development/multithreading">wiki entry</a> that discusses some of what must be done from a development perspective.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Feb '11, 07:56</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-2106" class="comments-container"></div><div id="comment-tools-2106" class="comment-tools"></div><div class="clear"></div><div id="comment-2106-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2119"></span>

<div id="answer-container-2119" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2119-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2119-score" class="post-score" title="current number of votes">1</div><span id="post-2119-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Complex display filters do not themselves require lots of CPU time. <em>Dissecting packets</em> does, and you need to dissect packets to handle <em>any</em> display filters. See <a href="http://wiki.wireshark.org/Development/Wishlist#General_.2BAC8_Unsorted">item 6 in this list</a> for some discussion of parallelizing dissection; unfortunately, it's an "embarrassingly serial" problem in the general case, but there's <em>some</em> stuff that could be parallelized.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Feb '11, 18:45</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-2119" class="comments-container"></div><div id="comment-tools-2119" class="comment-tools"></div><div class="clear"></div><div id="comment-2119-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

