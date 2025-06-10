+++
type = "question"
title = "Fences distances in overpass turbo"
description = '''Is it possible to query the sum of fences distances (in kilometers) in the view window or a bounding box of overpass turbo ?'''
date = "2018-05-12T08:17:00Z"
lastmod = "2018-05-13T12:35:00Z"
weight = 63425
keywords = [ "fence" ]
aliases = [ "/questions/63425" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Fences distances in overpass turbo](/questions/63425/fences-distances-in-overpass-turbo)

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
<span id="post-63425-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63425-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63425-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to query the sum of fences distances (in kilometers) in the view window or a bounding box of overpass turbo ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-fence" rel="tag" title="see questions tagged &#39;fence&#39;">fence</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 May '18, 08:17</strong></p>
<img src="https://secure.gravatar.com/avatar/bd6750f79ca0bdd872654ff19e3123c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sang3&#39;s gravatar image" />
<p><span>sang3</span><br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sang3 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63425" class="comments-container">
&#10;</div>
<div id="comment-tools-63425" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63425-form-container" class="comment-form-container">
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

<span id="63438"></span>

<div id="answer-container-63438" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63438-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63438-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63438-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://overpass-turbo.eu/s/yL6">Here is a quick example</a>. You have to scroll to the bottom of the "data" tab to see the results.</p>
<pre><code>[out:json][timeout:25][bbox:{{bbox}}];
way[barrier=fence];
out geom;
make stats length=sum(length()),section_lengths=set(length());
out;</code></pre>
<p>Script is lightly modified version of the example given in <a href="https://github.com/drolbr/Overpass-API/issues/237">https://github.com/drolbr/Overpass-API/issues/237</a>.</p>
<p>(As far as I know, there is no area evaluator, I see you've asked the similar question about that)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 May '18, 12:35</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-63438" class="comments-container">
&#10;</div>
<div id="comment-tools-63438" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63438-form-container" class="comment-form-container">
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

