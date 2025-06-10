+++
type = "question"
title = "Export hierarchical structure of (administrative) relations"
description = '''I&#x27;m looking for a way or tool to get a list of all type=boundary, boundary=administrative relations and their hierarchical structure (relation A has children B and C and B has children D and E and so on...). So something like: all boroughs of Berlin, Germany and all localities of all the boroughs of...'''
date = "2021-09-06T15:46:00Z"
lastmod = "2021-09-06T20:07:00Z"
weight = 81641
keywords = [ "hierarchy", "extract", "relations" ]
aliases = [ "/questions/81641" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Export hierarchical structure of (administrative) relations](/questions/81641/export-hierarchical-structure-of-administrative-relations)

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
<span id="post-81641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81641-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm looking for a way or tool to get a list of all <code>type=boundary, boundary=administrative</code> relations and their hierarchical structure (relation A has children B and C and B has children D and E and so on...). So something like: all boroughs of Berlin, Germany and all localities of all the boroughs of Berlin, Germany (<a href="https://upload.wikimedia.org/wikipedia/commons/c/c5/Berlin%2C_administrative_divisions_%28%2Bdistricts_%2Bboroughs_-pop%29_-_de_-_colored_%28less_colors%29.svg">Wikipedia</a>).</p>
<p>Basically, I only need the <code>osm_id</code>s.</p>
<p>I tried using the <a href="https://overpass-turbo.eu">Overpass API</a> (<a href="https://overpass-turbo.eu/s/1aVA">https://overpass-turbo.eu/s/1aVA</a>) but unfortunately it's very slow and I only get the immediate children. Now I could make a request for each of the children and get their children etc, but it takes forever.</p>
<p>Is there any good tool or way to achieve this? I'm sure I'm not the first to need the hierarchical structure of relations.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hierarchy" rel="tag" title="see questions tagged &#39;hierarchy&#39;">hierarchy</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Sep '21, 15:46</strong></p>
<img src="https://secure.gravatar.com/avatar/81b333e4578e71045002acaa98989729?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="foodev&#39;s gravatar image" />
<p><span>foodev</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="foodev has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81641" class="comments-container">
&#10;</div>
<div id="comment-tools-81641" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81641-form-container" class="comment-form-container">
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

<span id="81650"></span>

<div id="answer-container-81650" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81650-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81650-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81650-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at <a href="https://osm-boundaries.com">OSM Boundaries</a>. I haven't used it myself do download data but it seems to provide what you are looking for.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Sep '21, 20:07</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-81650" class="comments-container">
&#10;</div>
<div id="comment-tools-81650" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81650-form-container" class="comment-form-container">
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

