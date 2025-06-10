+++
type = "question"
title = "How to use Overpass Api for specific BoundingBox"
description = '''I am trying to get parks from specific area through Overpass API. The Query is like - [out:json][timeout:25]; (  node[&quot;leisure&quot;=&quot;park&quot;]({{bbox}});  way[&quot;leisure&quot;=&quot;park&quot;]({{bbox}});  relation[&quot;leisure&quot;=&quot;park&quot;]({{bbox}}); );  out body; &amp;gt;; out skel qt;  How can I replace bbox with certain specific B...'''
date = "2015-11-27T17:49:00Z"
lastmod = "2015-11-27T18:12:00Z"
weight = 46867
keywords = [ "overpassapi", "bounding", "overpass-turbo" ]
aliases = [ "/questions/46867" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to use Overpass Api for specific BoundingBox](/questions/46867/how-to-use-overpass-api-for-specific-boundingbox)

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
<span id="post-46867-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46867-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46867-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to get parks from specific area through Overpass API. The Query is like -</p>
<pre><code>[out:json][timeout:25];
(
  node[&quot;leisure&quot;=&quot;park&quot;]({{bbox}});
  way[&quot;leisure&quot;=&quot;park&quot;]({{bbox}});
  relation[&quot;leisure&quot;=&quot;park&quot;]({{bbox}});
);
&#10;out body;
&gt;;
out skel qt;</code></pre>
<p>How can I replace bbox with certain specific BoundingBox like '50.6,7.0,50.8,7.3' ?</p>
<p>Any help would be appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-bounding" rel="tag" title="see questions tagged &#39;bounding&#39;">bounding</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Nov '15, 17:49</strong></p>
<img src="https://secure.gravatar.com/avatar/178ab3999806fba209bae2a774cd6ca0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Suri45&#39;s gravatar image" />
<p><span>Suri45</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Suri45 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-46867" class="comments-container">
&#10;</div>
<div id="comment-tools-46867" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46867-form-container" class="comment-form-container">
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

<span id="46868"></span>

<div id="answer-container-46868" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46868-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46868-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46868-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yeah.. i got it. I just entered boundingbox like (50.6,7.0,50.8,7.3) and Its working. Thanks</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Nov '15, 18:12</strong></p>
<img src="https://secure.gravatar.com/avatar/178ab3999806fba209bae2a774cd6ca0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Suri45&#39;s gravatar image" />
<p><span>Suri45</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Suri45 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-46868" class="comments-container">
&#10;</div>
<div id="comment-tools-46868" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46868-form-container" class="comment-form-container">
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

