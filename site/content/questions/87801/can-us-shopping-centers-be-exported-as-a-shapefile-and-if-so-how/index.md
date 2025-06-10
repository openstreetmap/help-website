+++
type = "question"
title = "Can U.S. shopping centers be exported as a shapefile and if so, how?"
description = '''New to OSM: Can U.S. shopping centers be exported as a shapefile and if so, how? Thanks!'''
date = "2023-09-06T14:50:00Z"
lastmod = "2023-09-07T13:44:00Z"
weight = 87801
keywords = [ "shapefile", "shopping_center" ]
aliases = [ "/questions/87801" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can U.S. shopping centers be exported as a shapefile and if so, how?](/questions/87801/can-us-shopping-centers-be-exported-as-a-shapefile-and-if-so-how)

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
<span id="post-87801-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87801-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87801-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>New to OSM: Can U.S. shopping centers be exported as a shapefile and if so, how? Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-shopping_center" rel="tag" title="see questions tagged &#39;shopping_center&#39;">shopping_center</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Sep '23, 14:50</strong></p>
<img src="https://secure.gravatar.com/avatar/cd8cc4b6b7dbd400ce4f247174534d56?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="charris801&#39;s gravatar image" />
<p><span>charris801</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="charris801 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87801" class="comments-container">
&#10;</div>
<div id="comment-tools-87801" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87801-form-container" class="comment-form-container">
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

<span id="87806"></span>

<div id="answer-container-87806" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87806-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87806-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-87806-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If your question is: "Is there a web site where I can click a few buttons and out comes a shapefile with all US shopping centers" then the answer is no. But if you're willing to invest more time then it is possible.</p>
<p>The closest you'll get to "a web site where..." is the "Overpass Turbo" service (example: <a href="http://overpass-turbo.eu/s/1zTh)">http://overpass-turbo.eu/s/1zTh)</a> but this requires that you do some research as to which OSM tags you want (malls? supermarkets?), also Overpass Turbo will only output GeoJSON (not shape files but converters exist), and might refuse to run on an area as large as the US - you might have to run it in batches.</p>
<p>A more robust method is downloading a raw OSM data file that contains data for the US (e.g. from download.geofabrik.de), then run the "osmium" command line program (requires Linux) to filter out the objects of interest (requires the same research about what exactly you want that I mentioned in #1) and then convert them to GeoJSON.</p>
<p>Alternatively you can import the OSM data into a PostGIS database with osm2pgsql (both PostGIS and osm2pgsql are available on Windows but running on Linux is easier), and then use the standard PostGIS tool "pgsql2shp" to create a shape file based on a SQL query formulated to return all shopping centers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Sep '23, 23:09</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-87806" class="comments-container">
<span id="87818"></span>
<div id="comment-87818" class="comment">
<div id="post-87818-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great - thank you very much!</p>
</div>
<div id="comment-87818-info" class="comment-info">
<span class="comment-age">(07 Sep '23, 13:44)</span> <span class="comment-user userinfo">charris801</span>
</div>
</div>
</div>
<div id="comment-tools-87806" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87806-form-container" class="comment-form-container">
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

