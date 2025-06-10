+++
type = "question"
title = "Overpass API double admin_level for one coordinate (is_in)"
description = '''Overpass API delivers a result with two &quot;admin_level: 4&quot; entries for one coordinate as shown: http://overpass-api.de/api/interpreter?data=[out:json];is_in(%2253.166591%22,%229.841431%22);out+body;%3E;out+skel; This leads to filtering problems. How does that happen?'''
date = "2018-09-02T18:59:00Z"
lastmod = "2018-09-02T19:35:00Z"
weight = 65695
keywords = [ "overpass-api" ]
aliases = [ "/questions/65695" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API double admin_level for one coordinate (is_in)](/questions/65695/overpass-api-double-admin_level-for-one-coordinate-is_in)

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
<span id="post-65695-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65695-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65695-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Overpass API delivers a result with two "admin_level: 4" entries for one coordinate as shown:</p>
<p><a href="http://overpass-api.de/api/interpreter?data=%5Bout:json%5D;is_in(%2253.166591%22,%229.841431%22);out+body;%3E;out+skel;">http://overpass-api.de/api/interpreter?data=[out:json];is_in(%2253.166591%22,%229.841431%22);out+body;%3E;out+skel;</a></p>
<p>This leads to filtering problems. How does that happen?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Sep '18, 18:59</strong></p>
<img src="https://secure.gravatar.com/avatar/c03d22e1058608727ad93f2aecc26ea4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jolipo&#39;s gravatar image" />
<p><span>jolipo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jolipo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65695" class="comments-container">
&#10;</div>
<div id="comment-tools-65695" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65695-form-container" class="comment-form-container">
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

<span id="65696"></span>

<div id="answer-container-65696" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65696-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65696-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65696-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The reason the are both returned is that they both exist in the data and are both interpreted as areas by Overpass-API. Which isn't very helpful.</p>
<p>One of the objects represents just the land area:</p>
<p><a href="https://www.openstreetmap.org/relation/454192">https://www.openstreetmap.org/relation/454192</a></p>
<p>I guess you could filter on an additional tag like <a href="http://overpass-turbo.eu/s/BzC"><code>boundary=administrative</code></a> (or whatever might be suitable).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Sep '18, 19:35</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Sep '18, 19:38</strong> </span></p>
</div>
</div>
<div id="comments-container-65696" class="comments-container">
&#10;</div>
<div id="comment-tools-65696" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65696-form-container" class="comment-form-container">
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

