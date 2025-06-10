+++
type = "question"
title = "Direction of lanes:forward/lanes:backward with (e.g.) oneway=reverse"
description = '''Hi. On the Wiki page of key &#x27;lanes&#x27; I read the following: &quot;The key lanes:forward= hereby refers to lanes which direction is equal to the direction of the OSM way, and lanes:backward= to the opposite direction.&quot; My question is: Does this mean that &#x27;lanes:forward&#x27; refers to the direction of which the ...'''
date = "2020-04-22T14:34:00Z"
lastmod = "2020-04-22T15:48:00Z"
weight = 74331
keywords = [ "lanes", "oneway" ]
aliases = [ "/questions/74331" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Direction of lanes:forward/lanes:backward with (e.g.) oneway=reverse](/questions/74331/direction-of-lanesforwardlanesbackward-with-eg-onewayreverse)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74331-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74331-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74331-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi. On the Wiki page of key 'lanes' I read the following: "The key lanes:forward= <em>hereby refers to lanes which direction is equal to the direction of the OSM way, and lanes:backward=</em> to the opposite direction."</p>
<p>My question is: Does this mean that 'lanes:forward' refers to the direction of which the nodes of the way were listed, or the direction of which you can travel on the way? In different terms: For instance, let's say that the way has tag 'oneway'='reverse'. This means that the way of which you can travel on the way (let's call this dirA) is the opposite of how the way was "drawn" (let's call this dirB). Does 'lanes:forward' refer to the number of lanes in direction dirA or in direction dirB? This makes quite a difference for how you would use these numbers.</p>
<p>Thank you for your help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-lanes" rel="tag" title="see questions tagged &#39;lanes&#39;">lanes</span> <span class="post-tag tag-link-oneway" rel="tag" title="see questions tagged &#39;oneway&#39;">oneway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Apr '20, 14:34</strong></p>
<img src="https://secure.gravatar.com/avatar/305258babc6da7f52cf1d1c2c3a1efd6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="issibelli&#39;s gravatar image" />
<p><span>issibelli</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="issibelli has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74331" class="comments-container">
&#10;</div>
<div id="comment-tools-74331" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74331-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="74332"></span>

<div id="answer-container-74332" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74332-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-74332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The order of the nodes within the way definition. Not the direction of travel.</p>
<p>That said, a number of QA tools will tell you that the <a href="https://wiki.openstreetmap.org/wiki/Key:oneway"><code>oneway=-1</code> or <code>oneway=reverse</code> is not desireable</a> and strongly suggest you reverse the order of the nodes in the way and use <code>oneway=yes</code>. If you follow that advice, then on oneway roads the direction of travel and the order of the nodes is the same. But then in that case you also don't need to worry about <code>lanes:backward</code> or <code>lanes:forward</code> either.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Apr '20, 15:36</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-74332" class="comments-container">
<span id="74333"></span>
<div id="comment-74333" class="comment">
<div id="post-74333-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for the quick reply. What do you mean with your last sentence?</p>
</div>
<div id="comment-74333-info" class="comment-info">
<span class="comment-age">(22 Apr '20, 15:43)</span> <span class="comment-user userinfo">issibelli</span>
</div>
</div>
<span id="74334"></span>
<div id="comment-74334" class="comment">
<div id="post-74334-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>the <code>:forward</code> and <code>:reverse</code> tag name suffixes are only needed and used on two way roads. So if travel on the road is restricted to a single direction they are not normally used.</p>
</div>
<div id="comment-74334-info" class="comment-info">
<span class="comment-age">(22 Apr '20, 15:48)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
</div>
<div id="comment-tools-74332" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74332-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

