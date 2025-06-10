+++
type = "question"
title = "Getting tile row/column with lat/long query"
description = '''I&#x27;ve been Slippy Tiles Wiki page for equations to convert lat/long values (given via the user) to tile references, and then work with the data relating to the tile. My problem is the wiki&#x27;s equation always does one of the following:   Returns a location 20+ miles away from my given lat/long. The ran...'''
date = "2016-07-06T11:08:00Z"
lastmod = "2016-07-06T15:08:00Z"
weight = 50661
keywords = [ "c#", "mbtiles" ]
aliases = [ "/questions/50661" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Getting tile row/column with lat/long query](/questions/50661/getting-tile-rowcolumn-with-latlong-query)

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
<span id="post-50661-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50661-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-50661-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been <a href="http://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Lon..2Flat._to_tile_numbers_5">Slippy Tiles Wiki</a> page for equations to convert lat/long values (given via the user) to tile references, and then work with the data relating to the tile.</p>
<p>My problem is the wiki's equation always does one of the following:</p>
<ul>
<li><p>Returns a location 20+ miles away from my given lat/long. The range is ~18 miles to 200+ miles, no consistency.</p></li>
<li><p>Returns absolutely nothing, and the tile_row value (XXXXX) is always off by a considerable amount. This ranges from 40 (10810 instead of 10850) to 300+ (10417 in stead of 10817).</p></li>
</ul>
<p>This happens for all lat longs, sourced from varying online mapping tools. So far I've tested this with Google Maps, OSM's own browsing tool and used lat/long generation tools for random locations across the UK.</p>
<p>Here's my code so far:</p>
<pre><code>    public void UserQuery()
    {
        Console.Write(&quot;Please enter a latitude value: &quot;);
        double userLat = Convert.ToDouble(Console.ReadLine());
        Console.Write(&quot;Please enter a longitude value: &quot;);
        double userLong = Convert.ToDouble(Console.ReadLine());
&#10;        _merc.TileLat =  Math.Floor((1.0 - Math.Log(Math.Tan(DegreesToRadians(userLat)) + 1.0 / Math.Cos(DegreesToRadians(userLat))) / Math.PI)  * (1 &lt;&lt; ZoomLevel));
        _merc.TileLong = Math.Floor((userLong + 180.0) / 360.0 * (1 &lt;&lt; ZoomLevel));
    }
&#10;    private double DegreesToRadians(double angle)
    {
        return Math.PI * angle / 180;
    }</code></pre>
<p>The longitude value works perfectly everytime, it's just in there for reference.</p>
<p>The wiki's version of the equation is:</p>
<p><code>((1.0 - Math.Log(Math.Tan(lat * Math.PI / 180.0) + 1.0 / Math.Cos(lat * Math.PI / 180.0)) / Math.PI) / 2.0 * (1 &lt;&lt; zoom));</code></p>
<p>but my problem is that the last <code>/ 2</code> before bitshifting returns a value half of what's generally expected, so <code>5308</code> instead of <code>10616</code>. In terms of changes made to the equation, that's the only difference. I created a small method to work out radians =&gt; degrees because the original was hard to read and track (problems with brackets).</p>
<p>Thanks for any help in advance, this has put me at a standstill for upwards of 2 days now.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-c#" rel="tag" title="see questions tagged &#39;c#&#39;">c#</span> <span class="post-tag tag-link-mbtiles" rel="tag" title="see questions tagged &#39;mbtiles&#39;">mbtiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jul '16, 11:08</strong></p>
<img src="https://secure.gravatar.com/avatar/a7cb490555f288a4bc1232439157dc1c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesGould&#39;s gravatar image" />
<p><span>JamesGould</span><br />
<span class="score" title="196 reputation points">196</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesGould has one accepted answer">33%</span></p>
</div>
</div>
<div id="comments-container-50661" class="comments-container">
<span id="50662"></span>
<div id="comment-50662" class="comment not_top_scorer">
<div id="post-50662-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Looking at the history, I see a large number of edits by a wiki editor who has caused problems with equations in the past (the one who used "coherent variant names" in a comment).</p>
<p>I'd suggest looking back in the history <a href="http://wiki.openstreetmap.org/w/index.php?title=Slippy_map_tilenames&amp;action=history">http://wiki.openstreetmap.org/w/index.php?title=Slippy_map_tilenames&amp;action=history</a> , finding a version before their first edit, and using the equations from there.</p>
<p>If that works, paste those equations into the current page.</p>
</div>
<div id="comment-50662-info" class="comment-info">
<span class="comment-age">(06 Jul '16, 11:12)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="50664"></span>
<div id="comment-50664" class="comment not_top_scorer">
<div id="post-50664-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> thank you so much. Thishad me and a few colleagues confused, I thought I was being an idiot and not using the given equation properly but if it's incorrect in the CE wiki then I can see why it'd be a problem. On the hunt I go...</p>
</div>
<div id="comment-50664-info" class="comment-info">
<span class="comment-age">(06 Jul '16, 11:21)</span> <span class="comment-user userinfo">JamesGould</span>
</div>
</div>
<span id="50670"></span>
<div id="comment-50670" class="comment not_top_scorer">
<div id="post-50670-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/387/someoneelse"></a><a href="http://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> tried and used the equations past said wiki user (my god a lot of edits) and the result has been the same. I was informed on SO that bitshifting wasn't the same as using <code>Math.Pow(2, zoomLevel)</code> so I tried the older equations with both and the result remained the same, for reference.</p>
</div>
<div id="comment-50670-info" class="comment-info">
<span class="comment-age">(06 Jul '16, 11:46)</span> <span class="comment-user userinfo">JamesGould</span>
</div>
</div>
<span id="50671"></span>
<div id="comment-50671" class="comment not_top_scorer">
<div id="post-50671-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you mix up lat and lon by chance? Also take a look at <a href="http://oms.wff.ch/calc.htm">WebCalc</a> which produces valid results and (roughly) uses the JavaScript example code from the Wiki. It might help while debugging your application.</p>
</div>
<div id="comment-50671-info" class="comment-info">
<span class="comment-age">(06 Jul '16, 12:45)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="50673"></span>
<div id="comment-50673" class="comment not_top_scorer">
<div id="post-50673-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/158/scai">@scai</a> I don't believe so no. I swapped the equations around and it came back with both the lat and long incorrect, rather than just the lat. I queried the same UK based lat/long in WebCalc and the result was the same as my application, but it doesn't exist in the database. Even all values, not taking the zoom_level as a parameter gave me back 0 results.</p>
</div>
<div id="comment-50673-info" class="comment-info">
<span class="comment-age">(06 Jul '16, 13:11)</span> <span class="comment-user userinfo">JamesGould</span>
</div>
</div>
<span id="50674"></span>
<div id="comment-50674" class="comment">
<div id="post-50674-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>WebCalc returned the same values as your application? Please tell us your exact input and output.</p>
</div>
<div id="comment-50674-info" class="comment-info">
<span class="comment-age">(06 Jul '16, 13:19)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="50675"></span>
<div id="comment-50675" class="comment not_top_scorer">
<div id="post-50675-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/158/scai"></a><a href="http://help.openstreetmap.org/users/158/scai">@scai</a> correct it did. My inputs are <code>lat: 52.298059</code>, <code>long: -0.1275920</code> using zoom 14- these should resolve to 10 Downing Street, London.</p>
<p>The output for the values are: <code>X: 8186</code> (tile column) and <code>Y: 5448</code> (tile row). I'm using a UK based .mbtiles file from osm2vectortiles.org. My SQL query is: <code>string query = string.Format("SELECT tile_data FROM tiles WHERE zoom_level = {0} AND tile_column = {1} AND tile_row = {2}", ZoomLevel, _merc.TileLong, _merc.TileLat);</code></p>
</div>
<div id="comment-50675-info" class="comment-info">
<span class="comment-age">(06 Jul '16, 13:28)</span> <span class="comment-user userinfo">JamesGould</span>
</div>
</div>
<span id="50676"></span>
<div id="comment-50676" class="comment not_top_scorer">
<div id="post-50676-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Nope, <a href="https://www.openstreetmap.org/#map=14/52.2981/-0.1276">lat 52.2981 lon -0.1276</a> is <em>not</em> in London. <a href="https://www.openstreetmap.org/search?query=10%20Downing%20Street%2C%20London">10 Downing Street, London</a> is <a href="https://www.openstreetmap.org/#map=19/51.50345/-0.12710">lat 51.50345 lon -0.12710</a> and has tile <a href="http://tile.openstreetmap.org/19/261958/174348.png">261958/174348</a> for zoom level 19 and <a href="http://tile.openstreetmap.org/14/8186/5448.png">8186/5448</a> for zoom level 14.</p>
</div>
<div id="comment-50676-info" class="comment-info">
<span class="comment-age">(06 Jul '16, 13:39)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="50677"></span>
<div id="comment-50677" class="comment not_top_scorer">
<div id="post-50677-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/158/scai">@scai</a> I honestly have no idea what's going on. I just queried the lat/long you gave me above for downing street and it's given me a tile about 100 miles away. Do OSM provide their own vector tiles that I can query using SQL or something similar? I can't tell if it's my code or the data I'm using that's the issue.</p>
</div>
<div id="comment-50677-info" class="comment-info">
<span class="comment-age">(06 Jul '16, 13:47)</span> <span class="comment-user userinfo">JamesGould</span>
</div>
</div>
<span id="50678"></span>
<div id="comment-50678" class="comment">
<div id="post-50678-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>No, OSM doesn't provide vector tiles. To be exact, OSM doesn't provide any tiles at all, just map data. And the official tile server for OSM provides just raster tiles.</p>
<p>Regarding WebCalc and the numbers from my previous comment: If I enter these numbers into WebCalc (zoom 14, lon -0.12710, lat 51.50345) then it correctly returns 8186 for X and 5448 for Y.</p>
</div>
<div id="comment-50678-info" class="comment-info">
<span class="comment-age">(06 Jul '16, 13:56)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="50679"></span>
<div id="comment-50679" class="comment not_top_scorer">
<div id="post-50679-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/158/scai">@scai</a> if I use those lat/longs above and query the tile in the osm2vectortiles.org united_kingdom.mbtiles file, it gives back data from west sussex, about 50 miles south of the lat long query location. Is that going to be a problem with my code or a problem with the data? This is all using zoom level 14.</p>
</div>
<div id="comment-50679-info" class="comment-info">
<span class="comment-age">(06 Jul '16, 14:07)</span> <span class="comment-user userinfo">JamesGould</span>
</div>
</div>
<span id="50681"></span>
<div id="comment-50681" class="comment">
<div id="post-50681-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Silly question - but are you sure that the data in united_kingdom.mbtiles is correct (i.e. are you aware of anyone using it and creating maps with it), and are you sure that the "slippy map tilenames" page also applies to data in it?</p>
</div>
<div id="comment-50681-info" class="comment-info">
<span class="comment-age">(06 Jul '16, 14:22)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="50682"></span>
<div id="comment-50682" class="comment">
<div id="post-50682-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> me and a collegaue have just gone through it all and came to the same concluson - the data is wrong. We couldn't find a source for the database used in WebCalc (if you know it please tell me!) so I'm using the data I have right now (sourced from osm2vectortiles) and start working on figuring out lat long tile values from the max/min bounds of the DB.</p>
</div>
<div id="comment-50682-info" class="comment-info">
<span class="comment-age">(06 Jul '16, 14:47)</span> <span class="comment-user userinfo">JamesGould</span>
</div>
</div>
<span id="50683"></span>
<div id="comment-50683" class="comment not_top_scorer">
<div id="post-50683-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It is possible that mbtiles are based on a different calculation model. The algorithms from the slippy map tilenames page apply to OSM's raster map tiles and can be completely wrong for other tiles.</p>
</div>
<div id="comment-50683-info" class="comment-info">
<span class="comment-age">(06 Jul '16, 15:07)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="50684"></span>
<div id="comment-50684" class="comment">
<div id="post-50684-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/158/scai">@scai</a> ah that would make a lot of sense as to why they're working with the online browser and not the db I've got. I'll get cracking, thank you both for your help.</p>
</div>
<div id="comment-50684-info" class="comment-info">
<span class="comment-age">(06 Jul '16, 15:08)</span> <span class="comment-user userinfo">JamesGould</span>
</div>
</div>
</div>
<div id="comment-tools-50661" class="comment-tools">
<span class="comments-showing"> showing 5 of 15 </span> <a href="#" class="show-all-comments-link">show 10 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-50661-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

