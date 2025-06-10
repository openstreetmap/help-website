+++
type = "question"
title = "Rendering tiles of specific state"
description = '''The basic starting guides kind of left me with a couple of doubts  You import the full north american pbf We can&#x27;t zoom further than 13 on any zone because the tiles don&#x27;t seem to have been rendered  Do we have to run render_list to get more zoom levels? Can we render zoom levels of a specific state...'''
date = "2018-04-15T19:24:00Z"
lastmod = "2018-04-27T05:30:00Z"
weight = 63004
keywords = [ "render_list", "zoomlevel", "tiles", "tileserver" ]
aliases = [ "/questions/63004" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Rendering tiles of specific state](/questions/63004/rendering-tiles-of-specific-state)

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
<span id="post-63004-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63004-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63004-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The basic starting guides kind of left me with a couple of doubts</p>
<ol>
<li>You import the full north american pbf</li>
<li>We can't zoom further than 13 on any zone because the tiles don't seem to have been rendered</li>
</ol>
<p>Do we have to run render_list to get more zoom levels?</p>
<p>Can we render zoom levels of a specific state? Is this the command?</p>
<p>osm2pgsql -s -C 3000 -d gis -U gis --prefix MI -S default.style -e 12-20 MI.osm</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-render_list" rel="tag" title="see questions tagged &#39;render_list&#39;">render_list</span> <span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Apr '18, 19:24</strong></p>
<img src="https://secure.gravatar.com/avatar/7dc2ca85ad0fdecfb5c66a390b83180a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gfitz&#39;s gravatar image" />
<p><span>gfitz</span><br />
<span class="score" title="46 reputation points">46</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gfitz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jun '18, 12:13</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-63004" class="comments-container">
<span id="63005"></span>
<div id="comment-63005" class="comment">
<div id="post-63005-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's not actually clear from the question so far what you're actually trying to do - maybe add a bit more detail about what problems you're hitting?</p>
<p>For the avoidance of doubt if you follow <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a> you'll get a tile server that renders tiles on demand. If you want to manually render tiles you can use "render_list" (and you might find <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1804_tileserver_load#Force_Rendering_Tiles">https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1804_tileserver_load#Force_Rendering_Tiles</a> to help with that), but be aware that if you force render high zooms you will get a <em>lot</em> of very empty tiles.</p>
</div>
<div id="comment-63005-info" class="comment-info">
<span class="comment-age">(15 Apr '18, 19:41)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63006"></span>
<div id="comment-63006" class="comment">
<div id="post-63006-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Already did all that through the apt-get package for 14.04 that loads all the planet and then we imported the entire north american PBF. It doesn't load further than zoom level 13. And render_list has been running for days.</p>
</div>
<div id="comment-63006-info" class="comment-info">
<span class="comment-age">(15 Apr '18, 20:42)</span> <span class="comment-user userinfo">gfitz</span>
</div>
</div>
<span id="63007"></span>
<div id="comment-63007" class="comment">
<div id="post-63007-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>Already did all that through the apt-get package for 14.04</p>
</blockquote>
<p>One big caveat - the "with packages" instructions use lots of quite old software versions. I wouldn't personally recommend it, although on 14.04 it should still work (though you may hit old bugs later on).</p>
<blockquote>
<p>that loads all the planet</p>
</blockquote>
<p>To be clear, you can load any data you want at that stage. I'd personally suggest something much smaller while ensuring that the process works.</p>
<blockquote>
<p>It doesn't load further than zoom level 13</p>
</blockquote>
<p>I'm guessing here that you mean "the data loads OK but when I manually run render_list it doesn't get further than zoom level 13".</p>
<p>To re-ask my original question - what are you actually trying to do?</p>
</div>
<div id="comment-63007-info" class="comment-info">
<span class="comment-age">(15 Apr '18, 22:23)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63009"></span>
<div id="comment-63009" class="comment">
<div id="post-63009-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is render running? Restart it and post the useful output of: grep syslog | grep renderd</p>
</div>
<div id="comment-63009-info" class="comment-info">
<span class="comment-age">(16 Apr '18, 05:12)</span> <span class="comment-user userinfo">yvecai</span>
</div>
</div>
</div>
<div id="comment-tools-63004" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63004-form-container" class="comment-form-container">
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

<span id="63008"></span>

<div id="answer-container-63008" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63008-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63008-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63008-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gfitz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suspect that what you're trying to do here is to:</p>
<ul>
<li>load data into a database</li>
<li>Render tiles up to a particular zoom level in a particular geographical area from that data</li>
</ul>
<p>In order to load data I'd suggest following <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">this</a> for Ubuntu 16.04 or <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">this</a> for 18.04. I wouldn't suggest anything older because:</p>
<ul>
<li>The ubuntu version it needs will be out of support soon</li>
<li>The packages used (mod_tile, osm2pgsql etc.) are quite old and you'll be limited in terms of what map styles you can use because of that.</li>
</ul>
<p>If you want a US state, I'd suggest that you get data for the state you want from <a href="http://download.geofabrik.de/north-america.html">here</a>. You can pick a <a href="http://download.geofabrik.de/north-america/us/rhode-island.html">small one</a> for testing.</p>
<p>Once loaded, you'll have a database and a tile server but no map tiles yet. You can let map tiles render "on the fly" as people try and access them (but this will initially be slow) or you can use something like "<code>render_list</code>" (part of mod_tile) to render all tiles worldwide at certain zoom levels.</p>
<p>However, if you're only interested in tiles for a US state rendering all tiles worldwide (most of which will be empty) is pretty wasteful. <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1804_tileserver_load#Force_Rendering_Tiles">This link</a> explains how to render tiles for a particular area only. The example given there renders zoom 11 tiles for the UK only; for your US state you'd need to find the min and max lat and lon values and min and max zoom levels and amend the example command line given to match.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Apr '18, 22:37</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-63008" class="comments-container">
<span id="63186"></span>
<div id="comment-63186" class="comment">
<div id="post-63186-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Alright now. Followed that guide. /0/0/0.png is returning a pic of the world. After a few 404s tho. Also loaded the entire north american continent. Now leafletjs returns 404 on the pngs it's trying to fetch.</p>
</div>
<div id="comment-63186-info" class="comment-info">
<span class="comment-age">(27 Apr '18, 05:15)</span> <span class="comment-user userinfo">gfitz</span>
</div>
</div>
<span id="63188"></span>
<div id="comment-63188" class="comment">
<div id="post-63188-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry the path was /hot/x/y/z.png. My bad</p>
</div>
<div id="comment-63188-info" class="comment-info">
<span class="comment-age">(27 Apr '18, 05:30)</span> <span class="comment-user userinfo">gfitz</span>
</div>
</div>
</div>
<div id="comment-tools-63008" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63008-form-container" class="comment-form-container">
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

