+++
type = "question"
title = "Nominatim setup for own tile server"
description = '''Hi all, I&#x27;ve my own instance of OSM tile server (PostgreSQL 9.3, Postgis 2.1). Now I&#x27;m trying to run own Nominatim search engine on the same host (Nominatim 2.3.1). Tile server is working OK and serving sample Luxembourg test map tiles. Nominatim search page is displayed OK, but the following proble...'''
date = "2015-06-21T09:44:00Z"
lastmod = "2015-06-22T19:44:00Z"
weight = 43672
keywords = [ "instance", "tiles", "nominatim", "local" ]
aliases = [ "/questions/43672" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim setup for own tile server](/questions/43672/nominatim-setup-for-own-tile-server)

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
<span id="post-43672-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43672-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43672-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I've my own instance of OSM tile server (PostgreSQL 9.3, Postgis 2.1).</p>
<p>Now I'm trying to run own Nominatim search engine on the same host (Nominatim 2.3.1).</p>
<p>Tile server is working OK and serving sample Luxembourg test map tiles. Nominatim search page is displayed OK, but the following problems occur:</p>
<p>1) it displays 'Data: DB Error: insufficient permissions' warning,</p>
<p>2) my Nominatim instance is using public OSM tile server instead of mine tile server.</p>
<p>3) when search is used, it displays 'Details: Could not get word tokens' error.</p>
<p>I've setup local.php properties for Nominatim, including:</p>
<p>@define('CONST___Website_BaseURL', 'http://mysite/nominatim/')</p>
<p>but still no success.</p>
<p>After some debug (debug=1) I've found more detailed error messages:</p>
<p>Offending query is:</p>
<p>string(138) "select word_id,word_token, word, class, type, country_code, operator, search_name_count from word where word_token in (' beggen','beggen')"</p>
<p>and message is:</p>
<p>[nativecode=ERROR: permission denied for relation word]</p>
<p>Could anyone point me where to seek for solution?</p>
<p>How to setup Nominatim to use my tile server?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-instance" rel="tag" title="see questions tagged &#39;instance&#39;">instance</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-local" rel="tag" title="see questions tagged &#39;local&#39;">local</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jun '15, 09:44</strong></p>
<img src="https://secure.gravatar.com/avatar/a542fec92e66e8e590b6446838f072c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jaglu&#39;s gravatar image" />
<p><span>jaglu</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jaglu has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jun '15, 10:22</strong> </span></p>
</div>
</div>
<div id="comments-container-43672" class="comments-container">
<span id="43677"></span>
<div id="comment-43677" class="comment">
<div id="post-43677-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do you just want to use the same server, or the same database?</p>
<p>Do you have a different own database for each, Nominatim and Tile Rendering?</p>
<p>If not, I found the following:</p>
<p><a href="http://gis.stackexchange.com/questions/137122/is-it-possible-to-render-map-tiles-with-a-nominatim-postgis-db">http://gis.stackexchange.com/questions/137122/is-it-possible-to-render-map-tiles-with-a-nominatim-postgis-db</a></p>
<p>and</p>
<p><a href="https://lists.openstreetmap.org/pipermail/dev/2011-April/022309.html">https://lists.openstreetmap.org/pipermail/dev/2011-April/022309.html</a></p>
</div>
<div id="comment-43677-info" class="comment-info">
<span class="comment-age">(21 Jun '15, 11:18)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="43679"></span>
<div id="comment-43679" class="comment">
<div id="post-43679-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>Do you just want to use the same server, or the same database?</p>
</blockquote>
<p>I want to use the same server. It's my own VM running Ubuntu 12.04. I'm aware that, at the moment, setup both Nominatim and Tile Rendering on the same database is impossible.</p>
<blockquote>
<p>Do you have a different own database for each, Nominatim and Tile Rendering?</p>
</blockquote>
<p>I have two separate databases for Nominatim and Tile Rendering. I'm fine with having two databases, because I plan to serve OSM map &amp; search for a single country.</p>
</div>
<div id="comment-43679-info" class="comment-info">
<span class="comment-age">(21 Jun '15, 18:16)</span> <span class="comment-user userinfo">jaglu</span>
</div>
</div>
<span id="43681"></span>
<div id="comment-43681" class="comment">
<div id="post-43681-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was able to move forward few steps just by invoking: GRANT ALL PRIVILEGES ON TABLE some-nominatim-table TO "myuser"; Now the debug stacktrace displays two tables with results from 'word' and 'search_name' tables, but suck again on: Details: Could not get details for place. When I invoke the debbuged sql statement directly in psql, it displays data just fine.</p>
</div>
<div id="comment-43681-info" class="comment-info">
<span class="comment-age">(21 Jun '15, 18:55)</span> <span class="comment-user userinfo">jaglu</span>
</div>
</div>
<span id="43684"></span>
<div id="comment-43684" class="comment">
<div id="post-43684-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Half of the problems solved: 1) search is working well after I've granted ALL PRIVILEGES to 'www-user' instead of 'myuser' in PSQL. 2) 'Data: DB Error: insufficient permissions' warning is gone. This is the difference between Nominatim and Tile Rendering: Tile Rendering is using 'myuser' to run renderd daemon. Nominatim is using plain apache's 'www-data' user to run php pages. Hope it can save someone a day :)</p>
</div>
<div id="comment-43684-info" class="comment-info">
<span class="comment-age">(21 Jun '15, 20:14)</span> <span class="comment-user userinfo">jaglu</span>
</div>
</div>
<span id="43685"></span>
<div id="comment-43685" class="comment not_top_scorer">
<div id="post-43685-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Still my Nominatim map is using default public OSM tile server instead of my own tile server. Any ideas? Strange fact: Nominatim's JSON search is using my database, because if I seek for results outside my example map (Luxembourg only), it returns no results.</p>
</div>
<div id="comment-43685-info" class="comment-info">
<span class="comment-age">(21 Jun '15, 20:17)</span> <span class="comment-user userinfo">jaglu</span>
</div>
</div>
<span id="43703"></span>
<div id="comment-43703" class="comment not_top_scorer">
<div id="post-43703-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So you need a redirection for your tile requests from OSM tile servers to your own servers like localhost or similar?</p>
<p>What is your HTML or Javascript code about tile display? OpenLayers or Leafletjs???</p>
</div>
<div id="comment-43703-info" class="comment-info">
<span class="comment-age">(22 Jun '15, 17:25)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="43705"></span>
<div id="comment-43705" class="comment not_top_scorer">
<div id="post-43705-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I want my own nominatim instance to use my tile server (i.e: <a href="http://myserver/osm_tiles/).">http://myserver/osm_tiles/).</a> Now my nominatim is using: map.addLayer(new OpenLayers.Layer.OSM.Mapnik("Default"));</p>
</div>
<div id="comment-43705-info" class="comment-info">
<span class="comment-age">(22 Jun '15, 18:54)</span> <span class="comment-user userinfo">jaglu</span>
</div>
</div>
<span id="43706"></span>
<div id="comment-43706" class="comment not_top_scorer">
<div id="post-43706-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There's a simple Openlayers example here:</p>
<p><a href="https://switch2osm.org/using-tiles/getting-started-with-openlayers/">https://switch2osm.org/using-tiles/getting-started-with-openlayers/</a></p>
<p>That should give you an item what to look for.</p>
</div>
<div id="comment-43706-info" class="comment-info">
<span class="comment-age">(22 Jun '15, 18:57)</span> <span class="comment-user userinfo">SomeoneElse2</span>
</div>
</div>
<span id="43707"></span>
<div id="comment-43707" class="comment not_top_scorer">
<div id="post-43707-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, I'm perfectly aware how to make OSM map use layer of my own tile server. I've just hoped there is a Nominatim's configuration I could setup to use different (my own) tile server instead of default one. If there isn't such a configuration, I'll just modify Nominatim's php sources, although this is not a nice solution. Am I right? Should I modify raw php sources?</p>
</div>
<div id="comment-43707-info" class="comment-info">
<span class="comment-age">(22 Jun '15, 19:05)</span> <span class="comment-user userinfo">jaglu</span>
</div>
</div>
<span id="43710"></span>
<div id="comment-43710" class="comment not_top_scorer">
<div id="post-43710-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was not aware that Nominatim configuration has any influence on tile displaying, can you explain that a bit more? ... I fear you should describe your issue in more detailed way.</p>
</div>
<div id="comment-43710-info" class="comment-info">
<span class="comment-age">(22 Jun '15, 19:28)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="43712"></span>
<div id="comment-43712" class="comment">
<div id="post-43712-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I run my own tile server and own Nominatim service as a part of my own apache instance. If I import only Luxembourg to my 'gis' database, tile server is rendering only Luxembourg on my map. The rest of map is blank, of course. If I import only Luxembourg to my 'nominatim' database, the search is restricted only to the addresses' in Luxembourg, of course. Both cases are perfectly fine for me. What is not fine: if I browse to <a href="http://myserver/nominatim/,">http://myserver/nominatim/,</a> the map is displayed for the whole planet. I want to narrow Nominatim's default map to the tiles generated only by my tile server. Which is Luxembourg only :)</p>
</div>
<div id="comment-43712-info" class="comment-info">
<span class="comment-age">(22 Jun '15, 19:44)</span> <span class="comment-user userinfo">jaglu</span>
</div>
</div>
</div>
<div id="comment-tools-43672" class="comment-tools">
<span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-43672-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

