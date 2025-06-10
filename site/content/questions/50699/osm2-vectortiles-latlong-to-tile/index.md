+++
type = "question"
title = "OSM2 VectorTiles lat/long to tile"
description = '''After a frustrating few days I came to the conclusion that the Slippy Map Wiki only works for raster tiles, not for OSM2VectorTiles data. I can work with the data once I find the correct tile_data BLOB, but actually locating the correct tile via a user lat/long is problematic. The equations given in...'''
date = "2016-07-07T11:01:00Z"
lastmod = "2016-07-07T14:00:00Z"
weight = 50699
keywords = [ "sqlite", "osm2" ]
aliases = [ "/questions/50699" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM2 VectorTiles lat/long to tile](/questions/50699/osm2-vectortiles-latlong-to-tile)

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
<span id="post-50699-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50699-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-50699-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>After a frustrating few days I came to the conclusion that the <a href="http://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Lon..2Flat._to_tile_numbers_5">Slippy Map Wiki</a> only works for raster tiles, not for <a href="http://OSM2VectorTiles.org">OSM2VectorTiles</a> data. I can work with the data once I find the correct tile_data BLOB, but actually locating the correct tile via a user lat/long is problematic. The equations given in the wiki above identify raster tiles correctly, but I'm trying to get this working for an offline version of OpenStreetMap rendering/navigation (meaning I can't just use mapbox's JS API to convert it, also I can't find where the conversion happens in the github repo).</p>
<p>Can anyone offer any advice as to how I can convert a lat/long to the correct tile in an OSM2VT SQLite database?</p>
<p>The query, that works for raster tiles, may be of some use:</p>
<pre><code>    public void UserQuery()
    {
        Console.Write(&quot;Please enter a latitude value: &quot;);
        double userLat = Convert.ToDouble(Console.ReadLine());
        Console.Write(&quot;Please enter a longitude value: &quot;);
        double userLong = Convert.ToDouble(Console.ReadLine());
&#10;        _merc.TileLat = Math.Floor((1.0 - Math.Log(Math.Tan(DegreesToRadians(userLat)) + 1.0 / Math.Cos(DegreesToRadians(userLat))) / Math.PI) * Math.Pow(2, ZoomLevel));
        _merc.TileLong = Math.Floor((userLong + 180.0) / 360.0 * Math.Pow(2, ZoomLevel));
    }</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-sqlite" rel="tag" title="see questions tagged &#39;sqlite&#39;">sqlite</span> <span class="post-tag tag-link-osm2" rel="tag" title="see questions tagged &#39;osm2&#39;">osm2</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jul '16, 11:01</strong></p>
<img src="https://secure.gravatar.com/avatar/a7cb490555f288a4bc1232439157dc1c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesGould&#39;s gravatar image" />
<p><span>JamesGould</span><br />
<span class="score" title="196 reputation points">196</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesGould has one accepted answer">33%</span></p>
</div>
</div>
<div id="comments-container-50699" class="comments-container">
<span id="50700"></span>
<div id="comment-50700" class="comment">
<div id="post-50700-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>cross-posted: <a href="https://gis.stackexchange.com/questions/201257/osm2-vectortiles-lat-long-to-tile">https://gis.stackexchange.com/questions/201257/osm2-vectortiles-lat-long-to-tile</a></p>
</div>
<div id="comment-50700-info" class="comment-info">
<span class="comment-age">(07 Jul '16, 11:41)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-50699" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50699-form-container" class="comment-form-container">
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

<span id="50702"></span>

<div id="answer-container-50702" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50702-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50702-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-50702-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You may find the following code from <a href="http://github.com/systemed/tilemaker">tilemaker</a> relevant:</p>
<p><a href="https://github.com/systemed/tilemaker/blob/master/src/coordinates.cpp">https://github.com/systemed/tilemaker/blob/master/src/coordinates.cpp</a></p>
<p>I don't have any experience with osm2vectortiles because I find Docker and npm about as appealing as sandpapering my eyeballs, but I presume it uses the same tile layout.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jul '16, 14:00</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-50702" class="comments-container">
&#10;</div>
<div id="comment-tools-50702" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50702-form-container" class="comment-form-container">
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

