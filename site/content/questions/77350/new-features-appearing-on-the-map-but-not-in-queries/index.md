+++
type = "question"
title = "New features appearing on the map, but not in queries"
description = '''Earlier today, I added some features to OpenStreetMap. They are now visible on the Standard map layer, as well as the OPNVKarte and Humanitarian layers. However, nothing that I added in this changeset can be found using the query tool, or by running a query on overpass-turbo.eu, even a few hours lat...'''
date = "2020-11-01T22:35:00Z"
lastmod = "2020-11-01T23:02:00Z"
weight = 77350
keywords = [ "query", "mapnik" ]
aliases = [ "/questions/77350" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [New features appearing on the map, but not in queries](/questions/77350/new-features-appearing-on-the-map-but-not-in-queries)

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
<span id="post-77350-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77350-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77350-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Earlier today, I added some features to OpenStreetMap. They are now visible on the Standard map layer, as well as the OPNVKarte and Humanitarian layers. However, nothing that I added in this changeset can be found using the query tool, or by running a query on overpass-turbo.eu, even a few hours later and after clearing my browser cache. I find this very strange; normally new features appear in queries immediately after they're saved, while it may take minutes or hours for the map tiles to be reloaded. Is anyone else having this problem, and is there anything I can do about it?</p>
<p>The changeset in question: <a href="https://www.openstreetmap.org/changeset/93380611">https://www.openstreetmap.org/changeset/93380611</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Nov '20, 22:35</strong></p>
<img src="https://secure.gravatar.com/avatar/c10af86a93e949af74215b18a7797886?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="reschultzed&#39;s gravatar image" />
<p><span>reschultzed</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="reschultzed has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77350" class="comments-container">
&#10;</div>
<div id="comment-tools-77350" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77350-form-container" class="comment-form-container">
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

<span id="77351"></span>

<div id="answer-container-77351" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77351-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77351-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-77351-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When using Overpass Turbo, you can check how up to date the results are by hovering over the object counts in the lower right corner. I don't have any insight into why, but at the moment the data is about 1 day behind the main OSM database.</p>
<p>The query tool is also implemented using Overpass-API (using the server that is the default on Overpass Turbo), so it's the same issue in a different place.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '20, 23:02</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-77351" class="comments-container">
&#10;</div>
<div id="comment-tools-77351" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77351-form-container" class="comment-form-container">
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

