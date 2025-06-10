+++
type = "question"
title = "How to download high level info only of a large area"
description = '''I am searching for a way to download only high-level info (big cities, highways, major rivers, big lakes) of a large area (several countries). I would like to create some kind of basemap that I can use from within an airplane (as a passenger... :-) ), so I can identify large cities, highway intersec...'''
date = "2018-03-30T15:53:00Z"
lastmod = "2018-03-30T16:59:00Z"
weight = 62860
keywords = [ "download", "level_of_detail", "convert", "basemap", "osmosis" ]
aliases = [ "/questions/62860" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to download high level info only of a large area](/questions/62860/how-to-download-high-level-info-only-of-a-large-area)

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
<span id="post-62860-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62860-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62860-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am searching for a way to download only high-level info (big cities, highways, major rivers, big lakes) of a large area (several countries). I would like to create some kind of basemap that I can use from within an airplane (as a passenger... :-) ), so I can identify large cities, highway intersections, rivers, lakes, as we fly over them. Target platform is Android (Locus Map), and I am familiar with downloading smaller areas and converting the .osm.xml format into maps, using osmosis. I want to prevent having to download several gigabytes with lowest level of detail information, to end up using only a fraction of the information. Is it possible to specify the level of detail that you are interested in (like some kind of zoom level). Or are these maps readily available (as are maps for most countries). My area of interest is Western Europe (or in large blocks, like Northern West Europe, Southern West Europe...)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-level_of_detail" rel="tag" title="see questions tagged &#39;level_of_detail&#39;">level_of_detail</span> <span class="post-tag tag-link-convert" rel="tag" title="see questions tagged &#39;convert&#39;">convert</span> <span class="post-tag tag-link-basemap" rel="tag" title="see questions tagged &#39;basemap&#39;">basemap</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Mar '18, 15:53</strong></p>
<img src="https://secure.gravatar.com/avatar/02c7b884e7db241c8b949323c1db820a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bgeenen&#39;s gravatar image" />
<p><span>bgeenen</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bgeenen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62860" class="comments-container">
&#10;</div>
<div id="comment-tools-62860" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62860-form-container" class="comment-form-container">
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

<span id="62861"></span>

<div id="answer-container-62861" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62861-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62861-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-62861-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Some filtering can be done with Overpass but you'll probably stretch its limits. Also, remember that filtering isn't the only thing you will want; even if you manage to filter out only motorways, they will be hugely detailed and consist of tons of pieces with a very fine geometry, much too fine for your use case. Downloading the full Europe file and working on it yourself, likely with the help of a database, might be unavoidable.</p>
<p>I think that your best bet might be to skip OpenStreetMap altogether and see if you can use the data from naturalearthdata.com - much less detail but perhpas that's just what you need!</p>
<p>Another avenue worth pursuing could be that of "vector tiles" where you would only download e.g. zoom 8 vector tiles or so. There's readily available libraries for vector tile rendering on mobile so maybe that's an option; you'll be limited to what the vector tile provider has chosen to appear on a certain zoom level of course.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Mar '18, 16:59</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-62861" class="comments-container">
&#10;</div>
<div id="comment-tools-62861" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62861-form-container" class="comment-form-container">
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

