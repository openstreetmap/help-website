+++
type = "question"
title = "Pull street name from mbtiles using lat long"
description = '''I&#x27;m trying to interact with .mbtiles databases to pull street level data relating to a lat/long query. I do not need to render the map itself, just access the information relating to the particular tile. At the moment I&#x27;m struggling to find a vector tile that extends past zoom_level 14, which is the...'''
date = "2016-07-07T13:22:00Z"
lastmod = "2016-07-07T14:01:00Z"
weight = 50701
keywords = [ "c#", "sqlite", "vector", "mbtiles" ]
aliases = [ "/questions/50701" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Pull street name from mbtiles using lat long](/questions/50701/pull-street-name-from-mbtiles-using-lat-long)

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
<span id="post-50701-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50701-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50701-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to interact with .mbtiles databases to pull street level data relating to a lat/long query. I do not need to render the map itself, just access the information relating to the particular tile.</p>
<p>At the moment I'm struggling to find a vector tile that extends past <code>zoom_level 14</code>, which is the max for the SQLite databases over at <a href="http://osm2vectortiles.org/">OSM2VectorTiles</a>. I wanted to download raw OSM data, convert it to an SQLite database and then query with it that way (if it provides a zoom level beyond 14, I need residential street names etc) but I'm not sure if that's the right path.</p>
<p>Is there a particular way to query a lat/long in an offline client which pulls back vector data from the tile and then print it into a console?</p>
<p>I've been posting both here and on <code>gis.stackexchange.com</code> for a few days with varying problems but everything seems to be a dead end. Any lat/long values that I query using my code (below) relate to a raster tile based database which isn't functioning as intended when using vector tile information.</p>
<p>My current query to convert a lat/long and read data from the <code>tile_data</code> BLOB found in an .mbtiles database:</p>
<pre><code>    public void UserQuery()
    {
        Console.Write(&quot;Please enter a latitude value: &quot;);
        double userLat = Convert.ToDouble(Console.ReadLine());
        Console.Write(&quot;Please enter a longitude value: &quot;);
        double userLong = Convert.ToDouble(Console.ReadLine());
&#10;        _merc.TileLat = Math.Floor((1.0 - Math.Log(Math.Tan(DegreesToRadians(userLat)) + 1.0 / Math.Cos(DegreesToRadians(userLat))) / Math.PI) * Math.Pow(2, ZoomLevel));
        _merc.TileLong = Math.Floor((userLong + 180.0) / 360.0 * Math.Pow(2, ZoomLevel));
    }
&#10;    private double DegreesToRadians(double angle)
    {
        return Math.PI * angle / 180;
    }</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-c#" rel="tag" title="see questions tagged &#39;c#&#39;">c#</span> <span class="post-tag tag-link-sqlite" rel="tag" title="see questions tagged &#39;sqlite&#39;">sqlite</span> <span class="post-tag tag-link-vector" rel="tag" title="see questions tagged &#39;vector&#39;">vector</span> <span class="post-tag tag-link-mbtiles" rel="tag" title="see questions tagged &#39;mbtiles&#39;">mbtiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jul '16, 13:22</strong></p>
<img src="https://secure.gravatar.com/avatar/a7cb490555f288a4bc1232439157dc1c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesGould&#39;s gravatar image" />
<p><span>JamesGould</span><br />
<span class="score" title="196 reputation points">196</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesGould has one accepted answer">33%</span></p>
</div>
</div>
<div id="comments-container-50701" class="comments-container">
&#10;</div>
<div id="comment-tools-50701" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50701-form-container" class="comment-form-container">
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

<span id="50703"></span>

<div id="answer-container-50703" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50703-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50703-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-50703-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JamesGould has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It seems to me that the vector tile route is unnecessarily convoluted. Download a suitable OSM PBF data extract, load it into a PostGIS database with osm2pgsql, and then make your queries against that. You don't say which "street level data" you want to "pull" but if it's the name and geometry of a street, you'd be doing something like</p>
<pre><code>SELECT name, highway, way 
FROM planet_osm_line
WHERE ST_DWITHIN(ST_TRANSFORM(ST_SETSRID(ST_MAKEPOINT(mylon, mylat),4326),3857), way, 100)
AND highway IS NOT NULL
ORDER BY ST_DISTANCE(ST_TRANSFORM(ST_SETSRID(ST_MAKEPOINT(mylon, mylat),4326),3857), way)
LIMIT 10;</code></pre>
<p>This will look for all street geometries coming near 100 Mercator units (that's roughly metres but depends on where you are) of your point, and list the 10 that come closest.</p>
<p>Another option of doing the same is using the Nominatim geocoder and its reverse geocoding capability; it will essentially do the same internally, but give you a nicer output that includes an address hierarchy.</p>
<p>Trying to use vector tiles for this seems a bit error-prone.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jul '16, 14:01</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jul '16, 15:07</strong> </span></p>
</div>
</div>
<div id="comments-container-50703" class="comments-container">
&#10;</div>
<div id="comment-tools-50703" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50703-form-container" class="comment-form-container">
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

