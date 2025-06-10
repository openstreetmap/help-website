+++
type = "question"
title = "How to download OSM data in specified region with specific tag (I.E. highway)"
description = '''I want to download OSM data in *.shp format for specified region with specified tag (in example highway). There are any web services for doing that or I should write a script?'''
date = "2015-11-20T04:45:00Z"
lastmod = "2015-11-20T07:18:00Z"
weight = 46733
keywords = [ "download", "shapefile", "tag", "export", "tags" ]
aliases = [ "/questions/46733" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to download OSM data in specified region with specific tag (I.E. highway)](/questions/46733/how-to-download-osm-data-in-specified-region-with-specific-tag-ie-highway)

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
<span id="post-46733-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46733-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46733-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to download OSM data in *.shp format for specified region with specified tag (in example highway).</p>
<p>There are any web services for doing that or I should write a script?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-tag" rel="tag" title="see questions tagged &#39;tag&#39;">tag</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Nov '15, 04:45</strong></p>
<img src="https://secure.gravatar.com/avatar/566c7716d2528aa19cfc5651e8df9f62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nojarathma&#39;s gravatar image" />
<p><span>Nojarathma</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nojarathma has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Nov '15, 05:22</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-46733" class="comments-container">
&#10;</div>
<div id="comment-tools-46733" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46733-form-container" class="comment-form-container">
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

<span id="46738"></span>

<div id="answer-container-46738" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46738-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46738-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-46738-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Nojarathma has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are some web sites where you can download ready-made shape files (e.g. extract.bbbike.org, download.geofabrik.de) but you cannot choose which tags you want. If you want to create your own shape file, download the OSM data in .osm.pbf format and then use e.g. osm2pgsql to import to PostGIS, then pgsql2shp to create shape file, or use a modern version of ogr2ogr to convert from pbf to shp directly. More: <a href="http://wiki.openstreetmap.org/wiki/Shapefiles">http://wiki.openstreetmap.org/wiki/Shapefiles</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Nov '15, 06:49</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-46738" class="comments-container">
<span id="46739"></span>
<div id="comment-46739" class="comment">
<div id="post-46739-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>If the "region" isn't too big, using Overpass-Turbo might be easier. For example, download all highway ways: <a href="http://overpass-turbo.eu/s/cPW">http://overpass-turbo.eu/s/cPW</a> . Then use QGIS for conversion to SHP.</p>
</div>
<div id="comment-46739-info" class="comment-info">
<span class="comment-age">(20 Nov '15, 07:18)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
</div>
<div id="comment-tools-46738" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46738-form-container" class="comment-form-container">
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

