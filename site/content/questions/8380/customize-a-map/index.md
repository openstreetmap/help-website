+++
type = "question"
title = "Customize a map"
description = '''Hello, Newbie question: I am trying to customize an openstreet map, using TileMill to style it. The online map has too many markers, places etc. and the downloadable files from cloudmade do not cover buildings, lakes, so many layers are missing. So, basically I need to be able to produce a middle po...'''
date = "2011-10-10T10:59:00Z"
lastmod = "2011-10-10T12:44:00Z"
weight = 8380
keywords = [ "tilemill", "customization" ]
aliases = [ "/questions/8380" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Customize a map](/questions/8380/customize-a-map)

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
<span id="post-8380-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8380-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8380-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, Newbie question: I am trying to customize an openstreet map, using TileMill to style it.</p>
<p>The online map has too many markers, places etc. and the downloadable files from cloudmade do not cover buildings, lakes, so many layers are missing.</p>
<p>So, basically I need to be able to produce a middle point between these details level, choosing whatever I want to put on the map, and still have shapefiles as the output, no pngs.</p>
<p>I there any way to achieve that? Thanks a lot!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tilemill" rel="tag" title="see questions tagged &#39;tilemill&#39;">tilemill</span> <span class="post-tag tag-link-customization" rel="tag" title="see questions tagged &#39;customization&#39;">customization</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Oct '11, 10:59</strong></p>
<img src="https://secure.gravatar.com/avatar/b70b334d3f7a14266f466e49d91d1b02?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Diego%20Pizarro&#39;s gravatar image" />
<p><span>Diego Pizarro</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Diego Pizarro has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Oct '11, 11:03</strong> </span></p>
</div>
</div>
<div id="comments-container-8380" class="comments-container">
&#10;</div>
<div id="comment-tools-8380" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8380-form-container" class="comment-form-container">
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

<span id="8381"></span>

<div id="answer-container-8381" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8381-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8381-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8381-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The downloadable shape files on <a href="http://download.geofabrik.de">download.geofabrik.de</a> do contain buildings and layers. However you can also create your own shape files using the osm2shp or osmjs tools, or you could download a full OSM exctract and then run a PostGIS importer like osm2pgsql or imposm to load the data into a PostGIS database from where you then render with TileMill. If you want to (re)use an already existing map style, it is a good idea to use the same data provider or import tool as that style, else you have a lot of style modifications ahead of you. Most existing styles are geared towards the table structure that osm2pgsql generates.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Oct '11, 11:04</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-8381" class="comments-container">
<span id="8382"></span>
<div id="comment-8382" class="comment">
<div id="post-8382-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great, I will begin with the files from geoFabrik, which seem to be complete indeed. Then I will tackle the more advanced osm manipulation. Do you suggest I use the tool on openstreetmap to produce the osm extracts? Thanks a lot.</p>
</div>
<div id="comment-8382-info" class="comment-info">
<span class="comment-age">(10 Oct '11, 11:21)</span> <span class="comment-user userinfo">Diego Pizarro</span>
</div>
</div>
<span id="8383"></span>
<div id="comment-8383" class="comment">
<div id="post-8383-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you want to produce extracts in the sense of "small osm files", and the ready-made extracts on sites like <a href="http://download.geofabrik.de">download.geofabrik.de</a> (others are available, check <a href="http://wiki.openstreetmap.org/wiki/Planet.osm)">wiki.openstreetmap.org/wiki/Planet.osm)</a> are not sufficient for you, then you can use the Osmosis tool to create your own extracts.</p>
<p>If you want to produce Shape Files then I suggest you first create an OSM extract and then run the osmjs tool on that.</p>
</div>
<div id="comment-8383-info" class="comment-info">
<span class="comment-age">(10 Oct '11, 12:44)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-8381" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8381-form-container" class="comment-form-container">
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

