+++
type = "question"
title = "Shapefile download"
description = '''Hey guys! I need to import spatial data via oracle map builder of only one city - st. Petersburg for my bachelor&#x27;s thesis in shapefile format. I need to have BOUNDARY_POLYGON, BUILDING_POLYGON, and HIGHWAY_LINE files. Could you please tell me how to get these files?'''
date = "2021-04-26T19:39:00Z"
lastmod = "2021-04-26T22:33:00Z"
weight = 79877
keywords = [ "oracle", "shapefile", "download" ]
aliases = [ "/questions/79877" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Shapefile download](/questions/79877/shapefile-download)

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
<span id="post-79877-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79877-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79877-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey guys! I need to import spatial data via oracle map builder of only one city - st. Petersburg for my bachelor's thesis in shapefile format. I need to have BOUNDARY_POLYGON, BUILDING_POLYGON, and HIGHWAY_LINE files. Could you please tell me how to get these files?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-oracle" rel="tag" title="see questions tagged &#39;oracle&#39;">oracle</span> <span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Apr '21, 19:39</strong></p>
<img src="https://secure.gravatar.com/avatar/53e5a5cef4c0834f107e7ef778e29ea2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="korfoo&#39;s gravatar image" />
<p><span>korfoo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="korfoo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79877" class="comments-container">
&#10;</div>
<div id="comment-tools-79877" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79877-form-container" class="comment-form-container">
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

<span id="79880"></span>

<div id="answer-container-79880" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79880-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79880-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79880-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not sure if this provides boundary polygons, but bbbike does provide simple shapefile extracts for given areas: e.g., <a href="https://extract.bbbike.org/?lang=en&amp;sw_lng=29.582&amp;sw_lat=59.789&amp;ne_lng=30.605&amp;ne_lat=60.117&amp;format=shp.zip&amp;oi=0&amp;city=Saint%20Petersburg%2C%20Northwestern%20Federal%20District%2C%20190000%2C%20Russia&amp;layers=B000T">St Petersburg</a>. The shapefiles are likely missing many OSM tags.</p>
<p>The alternative is to use overpass(-turbo) to extract the layers you want as geojson, and convert to .SHP with ogr2ogr.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Apr '21, 22:33</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-79880" class="comments-container">
&#10;</div>
<div id="comment-tools-79880" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79880-form-container" class="comment-form-container">
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

