+++
type = "question"
title = "Tile cache update frequency"
description = '''Hi, I am having a customized OSM setup with our own database. Currently I&#x27;m getting the data as per my requirement edited by iD editor. Now I want this data to be rendered as map. Also I want to cache the generated tiles of this data. So some requirement:   I want to know standard practices for gene...'''
date = "2014-01-09T11:33:00Z"
lastmod = "2014-01-09T15:10:00Z"
weight = 29710
keywords = [ "tiles", "cache", "deployment" ]
aliases = [ "/questions/29710" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tile cache update frequency](/questions/29710/tile-cache-update-frequency)

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
<span id="post-29710-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29710-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29710-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am having a customized OSM setup with our own database. Currently I'm getting the data as per my requirement edited by iD editor. Now I want this data to be rendered as map. Also I want to cache the generated tiles of this data. So some requirement:</p>
<ol>
<li><p>I want to know standard practices for generating map using above data. Like taking .osm data offline, do some processing, make a shapefile, publish it in GeoServer or is there any other way also?</p></li>
<li><p>Since tile cache is a suitable option for faster data/tile rendering, what are the practices to generate tiles and how to update these tiles as data will be modified/added/updated regularly through iD editor.</p></li>
</ol>
<p>Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-cache" rel="tag" title="see questions tagged &#39;cache&#39;">cache</span> <span class="post-tag tag-link-deployment" rel="tag" title="see questions tagged &#39;deployment&#39;">deployment</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jan '14, 11:33</strong></p>
<img src="https://secure.gravatar.com/avatar/c59921537afd0b14f63f47aac9b4b600?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GoldenCompass&#39;s gravatar image" />
<p><span>GoldenCompass</span><br />
<span class="score" title="40 reputation points">40</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GoldenCompass has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jan '14, 14:59</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span></p>
</div>
</div>
<div id="comments-container-29710" class="comments-container">
<span id="29711"></span>
<div id="comment-29711" class="comment">
<div id="post-29711-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(just in case it isn't clear) <a href="https://help.openstreetmap.org/questions/28799/import-shapefile-as-osm">from previous questions</a> I believe that the questioner has their own copy of the rails port deployed.</p>
</div>
<div id="comment-29711-info" class="comment-info">
<span class="comment-age">(09 Jan '14, 11:39)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="29712"></span>
<div id="comment-29712" class="comment">
<div id="post-29712-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@SomeoneElse</span> Yes, I am having a copy of OSM setup (as per my requirement) up and running and getting data from concerned users.</p>
</div>
<div id="comment-29712-info" class="comment-info">
<span class="comment-age">(09 Jan '14, 11:44)</span> <span class="comment-user userinfo">GoldenCompass</span>
</div>
</div>
</div>
<div id="comment-tools-29710" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29710-form-container" class="comment-form-container">
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

<span id="29721"></span>

<div id="answer-container-29721" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29721-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29721-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29721-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>IMHO you need to decide which way you want to use to create your tiles:</p>
<ol>
<li><strong>Rendering on demand</strong><br />
So your TMS get's the client tile requests and renders/splits the desired area on the fly.</li>
<li><strong>Preprocessing all tiles</strong><br />
All tiles are rendered and then only the affected areas (by your edits) get updated and rerendered. This takes a lot of space (if you need to provide it as global service), but it scales better if you have a larger amount of clients.</li>
</ol>
<p>Both ways can be combined with <a href="http://wiki.openstreetmap.org/wiki/MapProxy">mapcaches</a>, but of course this limits the tile update frequency as the way to the client get's longer and the caches need time to propagate changes and to get flushed.</p>
<p>In every case you need to create a PostGIS DB that suits the rendering stack requirements (AFAIK this is <a href="http://wiki.openstreetmap.org/wiki/Database_schema#Database_Schemas">a different one</a> from the central rails port). Then you setup the <a href="http://wiki.openstreetmap.org/wiki/Mapnik">Mapnik</a> renderer (or a different one) and decide if you call them after edits or if you get a client request. A good tutorial is www.switch2osm.org also you might read <a href="http://wiki.openstreetmap.org/wiki/Creating_your_own_tiles">http://wiki.openstreetmap.org/wiki/Creating_your_own_tiles</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jan '14, 15:10</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span> </br></br></p>
</div>
</div>
<div id="comments-container-29721" class="comments-container">
&#10;</div>
<div id="comment-tools-29721" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29721-form-container" class="comment-form-container">
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

