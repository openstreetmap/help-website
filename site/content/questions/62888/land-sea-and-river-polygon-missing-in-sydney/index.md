+++
type = "question"
title = "Land, sea and river polygon missing in Sydney"
description = '''I have downloaded the OSM file for Sydney and imported it into QGIS. As you can see I have all the lines and areas. However, there is no polygon for the land itself, and no polygon for the neighbouring Pacific ocean, and no polygon for the water in the Sydney harbour, which then snakes inland into t...'''
date = "2018-04-03T11:43:00Z"
lastmod = "2018-04-06T04:52:00Z"
weight = 62888
keywords = [ "qgis", "land", "river", "sea", "polygon" ]
aliases = [ "/questions/62888" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Land, sea and river polygon missing in Sydney](/questions/62888/land-sea-and-river-polygon-missing-in-sydney)

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
<span id="post-62888-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62888-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62888-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have downloaded the OSM file for Sydney and imported it into QGIS. As you can see I have all the lines and areas. However, there is no polygon for the land itself, and no polygon for the neighbouring Pacific ocean, and no polygon for the water in the Sydney harbour, which then snakes inland into the Parramatta river.</p>
<p>I thought these would be very large polygons, and that's why they don't show up - they are larger than the bounding box of Sydney. However, I tried downloading the OSM for New South Wales but I still don't have the land mass, oceans, or rivers.</p>
<p>I then thought maybe those polygons are special and need to be generated - I found <a href="http://openstreetmapdata.com/data">http://openstreetmapdata.com/data</a> which has land and water polygons. That gives me the land, the sea, but not the water polygon for the Sydney harbour and the main Parramatta river.</p>
<p>What am I doing wrong?</p>
<p><img src="https://ibin.co/3x2SC0mHuJ2E.png" alt="QGIS result" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-land" rel="tag" title="see questions tagged &#39;land&#39;">land</span> <span class="post-tag tag-link-river" rel="tag" title="see questions tagged &#39;river&#39;">river</span> <span class="post-tag tag-link-sea" rel="tag" title="see questions tagged &#39;sea&#39;">sea</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Apr '18, 11:43</strong></p>
<img src="https://secure.gravatar.com/avatar/2e608794bb2ce50d409737a5d9012091?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Moult&#39;s gravatar image" />
<p><span>Moult</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Moult has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-62888" class="comments-container">
&#10;</div>
<div id="comment-tools-62888" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62888-form-container" class="comment-form-container">
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

<span id="62925"></span>

<div id="answer-container-62925" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62925-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62925-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62925-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In OpenStreetMap the land and the sea/ocean aren't explicitly mapped. Instead the coastline is mapped as a way (line) <a href="https://wiki.openstreetmap.org/wiki/Coastline.">https://wiki.openstreetmap.org/wiki/Coastline.</a></p>
<p>From the coastline, you can generate polygons for the land and/or ocean. <a href="https://wiki.openstreetmap.org/wiki/OSMCoastline">https://wiki.openstreetmap.org/wiki/OSMCoastline</a> is one such tool which does this as you've found out.</p>
<p>Sydney Harbour <a href="https://www.openstreetmap.org/relation/1252425/history">https://www.openstreetmap.org/relation/1252425/history</a> has seen some recent edits, so you might need to re-download your data, but it should show up since it's tagged as a multipolygon.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Apr '18, 04:52</strong></p>
<img src="https://secure.gravatar.com/avatar/7284ad488e18a2b052a9c7b8fe1e3922?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aharvey&#39;s gravatar image" />
<p><span>aharvey</span><br />
<span class="score" title="523 reputation points">523</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aharvey has 4 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-62925" class="comments-container">
&#10;</div>
<div id="comment-tools-62925" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62925-form-container" class="comment-form-container">
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

