+++
type = "question"
title = "Downloading specific shapefiles"
description = '''I was wondering if there was a way to download shapefile data for specific feature types. For example selecting all amenity = restaurant within a certain area and downloading the data as a shapefile. Thanks.'''
date = "2017-05-01T12:59:00Z"
lastmod = "2017-05-01T18:50:00Z"
weight = 55970
keywords = [ "shapefile" ]
aliases = [ "/questions/55970" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Downloading specific shapefiles](/questions/55970/downloading-specific-shapefiles)

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
<span id="post-55970-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55970-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55970-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I was wondering if there was a way to download shapefile data for specific feature types. For example selecting all amenity = restaurant within a certain area and downloading the data as a shapefile. Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 May '17, 12:59</strong></p>
<img src="https://secure.gravatar.com/avatar/8438e333d147e654dc689816faff7b72?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mikaelamoschella&#39;s gravatar image" />
<p><span>mikaelamosch...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mikaelamoschella has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55970" class="comments-container">
&#10;</div>
<div id="comment-tools-55970" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55970-form-container" class="comment-form-container">
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

<span id="55973"></span>

<div id="answer-container-55973" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55973-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55973-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-55973-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't know of anything that will directly export a filtered shapefile. <a href="http://overpass-turbo.eu/">Overpass Turbo</a> has a wizard to help with simple searches and can export geoJSON (which hopefully you can at least convert to a shapefile).</p>
<p>For your example, adjust the map to the area of interest, click "Wizard", input "amenity=restaurant" and click "build and run query", then click "Export" and select geoJSON.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 May '17, 15:19</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-55973" class="comments-container">
<span id="55978"></span>
<div id="comment-55978" class="comment">
<div id="post-55978-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>QGIS or ogr2ogr can convert from GeoJSON to shape.</p>
</div>
<div id="comment-55978-info" class="comment-info">
<span class="comment-age">(01 May '17, 18:50)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-55973" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55973-form-container" class="comment-form-container">
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

