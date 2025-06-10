+++
type = "question"
title = "Where are layers (shp files) for public transportation?"
description = '''Hi I&#x27;m new to using OSM. Currently I&#x27;m looking at OSM data through a GIS program (MapInfo) I have downloaded shape files for my country (Denmark) and looking through data. I&#x27;m interested in ferry lines, and I can not figure out where to find the data containing public transportation. Is it possible ...'''
date = "2013-05-22T14:20:00Z"
lastmod = "2013-05-22T16:45:00Z"
weight = 22638
keywords = [ "shapefile", "ferry" ]
aliases = [ "/questions/22638" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Where are layers (shp files) for public transportation?](/questions/22638/where-are-layers-shp-files-for-public-transportation)

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
<span id="post-22638-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22638-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22638-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I'm new to using OSM. Currently I'm looking at OSM data through a GIS program (MapInfo) I have downloaded shape files for my country (Denmark) and looking through data. I'm interested in ferry lines, and I can not figure out where to find the data containing public transportation. Is it possible I have to extract this data myself somehow and convert it into shapefiles in order to see it? I can't find any premade shapefiles containing ferry routes/lines.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-ferry" rel="tag" title="see questions tagged &#39;ferry&#39;">ferry</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 May '13, 14:20</strong></p>
<img src="https://secure.gravatar.com/avatar/f50be95d62f004abde67a67c48ec7d8b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kasper%20Pedersen&#39;s gravatar image" />
<p><span>Kasper Pedersen</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kasper Pedersen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-22638" class="comments-container">
&#10;</div>
<div id="comment-tools-22638" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22638-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="22641"></span>

<div id="answer-container-22641" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22641-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-22641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Ferry lines are often present in OSM as simple line geometries tagged appropriately. Extracting these from OSM using e.g. osm2shp or osmjs should be straightforward. Other public transport - trains, buses - is often more complex as it is modelled in the form of relations which are not perfectly supported by these tools. Your best bet is perhaps to import the data into a PostGIS database with osm2pgsql and then export from there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 May '13, 15:29</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-22641" class="comments-container">
&#10;</div>
<div id="comment-tools-22641" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22641-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="22646"></span>

<div id="answer-container-22646" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22646-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22646-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-22646-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, you'll have to extract them yourself, using e.g. <a href="http://www.osm974.re/osm2gis/">http://www.osm974.re/osm2gis/</a> or one of the other methods described in the wiki at <a href="http://wiki.openstreetmap.org/wiki/Shapefiles">http://wiki.openstreetmap.org/wiki/Shapefiles</a> .</p>
<p>The Key-Value-Combination you need is <code>route=ferry</code></p>
<p>edit: osm2gis does seem to be quite bad for obtaining large-scale sparse data extracts. So you'll be best off by downloading a denmark OSM extract, then filtering for <code>route=ferry</code> using osmfilter and then creating a shapefile from that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 May '13, 16:45</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 May '13, 16:48</strong> </span></p>
</div>
</div>
<div id="comments-container-22646" class="comments-container">
&#10;</div>
<div id="comment-tools-22646" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22646-form-container" class="comment-form-container">
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

