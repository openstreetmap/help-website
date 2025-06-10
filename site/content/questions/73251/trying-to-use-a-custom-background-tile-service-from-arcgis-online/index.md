+++
type = "question"
title = "Trying to use a custom background tile service from ArcGIS Online"
description = '''I&#x27;m trying to use a web tile service I have hosted in ArcGIS Online as a custom background in OSM editor.  the url to query my tiles is: https://tiles.arcgis.com/tiles/CnkB6jCzAsyli34z/arcgis/rest/services/AberdeenOrtho/MapServer/WMTS/tile/1.0.0/AberdeenOrtho/default/default028mm/14/5264/2605.png? h...'''
date = "2020-02-27T01:34:00Z"
lastmod = "2021-04-13T18:55:00Z"
weight = 73251
keywords = [ "basemap", "esri" ]
aliases = [ "/questions/73251" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Trying to use a custom background tile service from ArcGIS Online](/questions/73251/trying-to-use-a-custom-background-tile-service-from-arcgis-online)

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
<span id="post-73251-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73251-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73251-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to use a web tile service I have hosted in ArcGIS Online as a custom background in OSM editor.</p>
<p>the url to query my tiles is:<br />
<span></span><a href="https://tiles.arcgis.com/tiles/CnkB6jCzAsyli34z/arcgis/rest/services/AberdeenOrtho/">https://tiles.arcgis.com/tiles/CnkB6jCzAsyli34z/arcgis/rest/services/AberdeenOrtho/</a><br />
MapServer/WMTS/tile/1.0.0/AberdeenOrtho/default/default028mm/14/5264/2605.png?</p>
<p>however when i use the tokens:<br />
<span></span><a href="https://tiles.arcgis.com/tiles/CnkB6jCzAsyli34z/arcgis/rest/services/AberdeenOrtho/">https://tiles.arcgis.com/tiles/CnkB6jCzAsyli34z/arcgis/rest/services/AberdeenOrtho/</a><br />
/WMTS/tile/1.0.0/AberdeenOrtho/default/default028mm/{zoom}/{x}/{y}.png?</p>
<p>I get nothing. Projection is WGS84 and tiling scheme is the standard google etc. I have lot's of GIS and esri experience but am relatively new to OSM. Any help would be greatly appreciated</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-basemap" rel="tag" title="see questions tagged &#39;basemap&#39;">basemap</span> <span class="post-tag tag-link-esri" rel="tag" title="see questions tagged &#39;esri&#39;">esri</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Feb '20, 01:34</strong></p>
<img src="https://secure.gravatar.com/avatar/a0e6718bcaa8213d077010df292e43ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uncle%20Lope&#39;s gravatar image" />
<p><span>Uncle Lope</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uncle Lope has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Feb '20, 02:20</strong> </span></p>
</div>
</div>
<div id="comments-container-73251" class="comments-container">
<span id="79588"></span>
<div id="comment-79588" class="comment">
<div id="post-79588-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, if have the same issue as described here (X/Y swap between OSM and arcGIS), any idea how to solve/transpose this?</p>
</div>
<div id="comment-79588-info" class="comment-info">
<span class="comment-age">(09 Apr '21, 16:13)</span> <span class="comment-user userinfo">MarcelVanDer...</span>
</div>
</div>
</div>
<div id="comment-tools-73251" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73251-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="73257"></span>

<div id="answer-container-73257" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73257-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73257-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73257-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>"...2606.png" looks east of "...2605.png" to me. Have you got x and y transposed?</p>
<p>The 'default' render seems with url schema: "<code>http://[abc].tile.openstreetmap.org/zoom/x/y.png</code>" seems to have equivalent tiles at:</p>
<p><a href="https://b.tile.openstreetmap.org/14/2605/5264.png"><code>https://b.tile.openstreetmap.org/14/2605/5264.png</code></a><code> </code><a href="https://b.tile.openstreetmap.org/14/2606/5264.png"><code>https://b.tile.openstreetmap.org/14/2606/5264.png</code></a></p>
<p><img src="https://b.tile.openstreetmap.org/14/2605/5264.png" alt="2605/5264" /><img src="https://b.tile.openstreetmap.org/14/2606/5264.png" alt="2606/5264" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Feb '20, 07:54</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span> </br></br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Feb '20, 07:55</strong> </span></p>
</div>
</div>
<div id="comments-container-73257" class="comments-container">
&#10;</div>
<div id="comment-tools-73257" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73257-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="79587"></span>

<div id="answer-container-79587" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79587-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79587-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79587-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, if have the same issue as described here (X/Y swap between OSM and arcGIS), any idea how to solve/transpose this?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Apr '21, 16:13</strong></p>
<img src="https://secure.gravatar.com/avatar/5d4d76db5b69466db19240b19b4bd55f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MarcelVanDerJagt&#39;s gravatar image" />
<p><span>MarcelVanDer...</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MarcelVanDerJagt has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-79587" class="comments-container">
&#10;</div>
<div id="comment-tools-79587" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79587-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="79652"></span>

<div id="answer-container-79652" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79652-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79652-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79652-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://tiles.arcgis.com/tiles/CnkB6jCzAsyli34z/arcgis/rest/services/AberdeenOrtho/">https://tiles.arcgis.com/tiles/CnkB6jCzAsyli34z/arcgis/rest/services/AberdeenOrtho/</a> /WMTS/tile/1.0.0/AberdeenOrtho/default/default028mm/{zoom}/{x}/{y}.png? just flip the last two values so it would be /{zoom}/{y}/{x}</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Apr '21, 18:55</strong></p>
<img src="https://secure.gravatar.com/avatar/a0e6718bcaa8213d077010df292e43ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uncle%20Lope&#39;s gravatar image" />
<p><span>Uncle Lope</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uncle Lope has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79652" class="comments-container">
&#10;</div>
<div id="comment-tools-79652" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79652-form-container" class="comment-form-container">
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

