+++
type = "question"
title = "Overpass query to find nodes of a way that I&#x27;ve modified"
description = '''Could I get some help with the syntax of an Overpass query? I modified an administrative boundary when adding a stream that borders that boundary. I thought I was careful to not join any nodes between the boundary way and the stream way and on checking in the iD editor I don&#x27;t see any. So I&#x27;m trying...'''
date = "2021-08-29T03:45:00Z"
lastmod = "2021-08-29T06:09:00Z"
weight = 81525
keywords = [ "filtering", "overpass-turbo" ]
aliases = [ "/questions/81525" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass query to find nodes of a way that I've modified](/questions/81525/overpass-query-to-find-nodes-of-a-way-that-ive-modified)

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
<span id="post-81525-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81525-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81525-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Could I get some help with the syntax of an Overpass query? I modified an administrative boundary when adding a stream that borders that boundary. I thought I was careful to not join any nodes between the boundary way and the stream way and on checking in the iD editor I don't see any. So I'm trying to figure out the syntax of an Overpass query that would help me find the nodes in the boundary way that I may have changed inadvertently. I've tried the following but it doesn't give me the intersection of the nodes I've changed that are also part of the boundary.</p>
<p>( way<a href="%7B%7Bbbox%7D%7D">"name"="name of admin boundary"</a>; node(user:"myuserid"); );</p>
<p>thanks much!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filtering" rel="tag" title="see questions tagged &#39;filtering&#39;">filtering</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Aug '21, 03:45</strong></p>
<img src="https://secure.gravatar.com/avatar/dfbf4141bd05182318d157ff3d1f0b04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mccarbc&#39;s gravatar image" />
<p><span>mccarbc</span><br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mccarbc has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81525" class="comments-container">
&#10;</div>
<div id="comment-tools-81525" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81525-form-container" class="comment-form-container">
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

<span id="81526"></span>

<div id="answer-container-81526" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81526-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81526-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81526-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I figured out the answer, I needed to do the node recursion. Here is the final query that I used.</p>
<pre><code>[out:json][timeout:25];
// gather results
(
   way[&quot;name&quot;=&quot;name of admin boundary&quot;]({{bbox}});
);
&#10;  node(w)(user:&quot;myuserid&quot;);
&#10;// print results
out body;
&gt;;
out skel qt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Aug '21, 06:09</strong></p>
<img src="https://secure.gravatar.com/avatar/dfbf4141bd05182318d157ff3d1f0b04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mccarbc&#39;s gravatar image" />
<p><span>mccarbc</span><br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mccarbc has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81526" class="comments-container">
&#10;</div>
<div id="comment-tools-81526" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81526-form-container" class="comment-form-container">
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

