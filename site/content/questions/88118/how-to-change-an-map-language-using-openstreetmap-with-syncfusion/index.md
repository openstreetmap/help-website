+++
type = "question"
title = "How to change an map language using OpenStreetMap with Syncfusion"
description = '''Hello, I am trying to use OSM with the Syncfusion Map component. Everything looks great, but I just encountered the issue where all the country names are translated into their default region language. For example, the United Kindom is displayed as the United Kingdom, Germany as Deutschland, and Pola...'''
date = "2024-01-05T15:43:00Z"
lastmod = "2024-01-08T14:28:00Z"
weight = 88118
keywords = [ "map", "blazor", "syncfusion", "osm", "language" ]
aliases = [ "/questions/88118" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to change an map language using OpenStreetMap with Syncfusion](/questions/88118/how-to-change-an-map-language-using-openstreetmap-with-syncfusion)

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
<span id="post-88118-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88118-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88118-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I am trying to use OSM with the Syncfusion Map component. Everything looks great, but I just encountered the issue where all the country names are translated into their default region language. For example, the United Kindom is displayed as the United Kingdom, Germany as Deutschland, and Poland as Polska.</p>
<p>How can I make it more general and use just English names so all from the previous example will be displayed as United Kindom, Germany and Poland?</p>
<p>Please see below the simplest code snipped using the OSM as a Sublayer for SfMaps</p>
<p>&lt;sfmaps&gt; &lt;mapszoomsettings enable=""/&gt; &lt;mapslayers&gt; &lt;mapslayer urltemplate="https://tile.openstreetmap.org/level/tileX/tileY.png" tvalue="string"/&gt; &lt;/mapslayers&gt; &lt;/sfmaps&gt;</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-blazor" rel="tag" title="see questions tagged &#39;blazor&#39;">blazor</span> <span class="post-tag tag-link-syncfusion" rel="tag" title="see questions tagged &#39;syncfusion&#39;">syncfusion</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-language" rel="tag" title="see questions tagged &#39;language&#39;">language</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jan '24, 15:43</strong></p>
<img src="https://secure.gravatar.com/avatar/c8f028e2de5fe0461b8cdd962c94da80?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pawelszo&#39;s gravatar image" />
<p><span>Pawelszo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pawelszo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-88118" class="comments-container">
&#10;</div>
<div id="comment-tools-88118" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88118-form-container" class="comment-form-container">
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

<span id="88120"></span>

<div id="answer-container-88120" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-88120-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88120-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88120-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You would need to use a tile provider that offers English labels all across the globe.</p>
<p>As you are using raster tiles, the labels are ingrained in the images, so the normal tiles by the OSMF won't help.</p>
<p>Instead you'll need an alternative tile provider with raster tiles that carries English labels only.</p>
<p>Have a look at <a href="https://wiki.openstreetmap.org/wiki/Raster_tile_providers">https://wiki.openstreetmap.org/wiki/Raster_tile_providers</a></p>
<p>where you'll find several ones.</p>
<p>Example map with raster tiles where English is used globally: <a href="https://www.osmap.uk">www.osmap.uk</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jan '24, 14:28</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jan '24, 08:32</strong> </span></p>
</div>
</div>
<div id="comments-container-88120" class="comments-container">
&#10;</div>
<div id="comment-tools-88120" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88120-form-container" class="comment-form-container">
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

