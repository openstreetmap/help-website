+++
type = "question"
title = "Why does our own tile server sometimes abort rendering tiles?"
description = '''I am set up a tile server to render tiles for a Slippy Map which is used in one of our web applications. I used the tutorial Manually building a tile server (12 04) to build up the server. For testing, I installed the server on a vm (VMware) on my own PC first. Everything works fine by using &quot;hambur...'''
date = "2012-11-02T09:43:00Z"
lastmod = "2012-11-03T01:14:00Z"
weight = 17398
keywords = [ "openlayers", "osm_tile", "osm", "slippymap", "mapnik" ]
aliases = [ "/questions/17398" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why does our own tile server sometimes abort rendering tiles?](/questions/17398/why-does-our-own-tile-server-sometimes-abort-rendering-tiles)

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
<span id="post-17398-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17398-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17398-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am set up a tile server to render tiles for a Slippy Map which is used in one of our web applications. I used the tutorial <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/">Manually building a tile server (12 04)</a> to build up the server. For testing, I installed the server on a vm (VMware) on my own PC first. Everything works fine by using "hamburg.osm.bz2". After testing it locally, I set it up on a server vm (Citrix Xenserver, Ubuntu 12.04.1 LTS, Postgres 9.1, 4 CPUs, 4GB RAM) and I used the file "germany.osm.bz2" for the map data.</p>
<p>If I move over the map or zoom in and out I have more often a map like this: <img src="/upfiles/osm_map.PNG" alt="alt text" /></p>
<p>Firebug show's for this tiles a "404 Not Found", but if I type the URL in the address line I can see the Image. If I scroll into the map and out of the map I also the see tile.</p>
<p>I don't have any idea how can I fix it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-osm_tile" rel="tag" title="see questions tagged &#39;osm_tile&#39;">osm_tile</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-slippymap" rel="tag" title="see questions tagged &#39;slippymap&#39;">slippymap</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Nov '12, 09:43</strong></p>
<img src="https://secure.gravatar.com/avatar/ebe0e0280c4ca913274eed32dd387807?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="marco-2012&#39;s gravatar image" />
<p><span>marco-2012</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="marco-2012 has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-17398" class="comments-container">
&#10;</div>
<div id="comment-tools-17398" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17398-form-container" class="comment-form-container">
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

<span id="17399"></span>

<div id="answer-container-17399" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17399-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17399-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17399-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="marco-2012 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My guess is that the first time the tile is rendered it takes too long to be available so you get the 404. By the time you type the URL or zoom in and out the rendering has finished and the tile is available to you. To solve it I guess you get a faster tile renderer or pre-render areas you are most interested in.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Nov '12, 10:00</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-17399" class="comments-container">
<span id="17405"></span>
<div id="comment-17405" class="comment">
<div id="post-17405-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What do you mean with a faster tile renderer? To increase the server hardware (RAM etc.)? We will try to pre-render the tiles.</p>
</div>
<div id="comment-17405-info" class="comment-info">
<span class="comment-age">(02 Nov '12, 12:15)</span> <span class="comment-user userinfo">marco-2012</span>
</div>
</div>
<span id="17409"></span>
<div id="comment-17409" class="comment">
<div id="post-17409-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is the server yevaud, aka tile.openstreetmap.org <a href="https://wiki.openstreetmap.org/wiki/Servers/yevaud">https://wiki.openstreetmap.org/wiki/Servers/yevaud</a> - I think having the database on the SSD was found to help a lot, but even then complex tiles might still exhibit the behaviour you have seen. If you look elsewhere in these forums you'll see questions about why people can't see their changes - in this case they will often be served a cached (old data) tile if the new tile doesn't render quickly enough (I believe). If there is no tile then they'd get the 404 tile</p>
</div>
<div id="comment-17409-info" class="comment-info">
<span class="comment-age">(02 Nov '12, 13:10)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="17412"></span>
<div id="comment-17412" class="comment">
<div id="post-17412-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>We currently can not use a SSD for the database. Thus we will try to pre-render the tiles. May be it will help.</p>
</div>
<div id="comment-17412-info" class="comment-info">
<span class="comment-age">(02 Nov '12, 13:54)</span> <span class="comment-user userinfo">marco-2012</span>
</div>
</div>
<span id="17432"></span>
<div id="comment-17432" class="comment">
<div id="post-17432-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>You can also increase the timeout for which mod_tile waits for the rendering to complete until it gives up and returns a 404. This is set by the "ModTileMissingRequestTimeout" parameter in the site definition of Apache. The default is set to 10 seconds, but you can set it higher. However, pre-rendering of tiles at least for the low zoom levels (e.g. Z0 - z12) is probably preferred.</p>
</div>
<div id="comment-17432-info" class="comment-info">
<span class="comment-age">(03 Nov '12, 01:14)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
</div>
<div id="comment-tools-17399" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17399-form-container" class="comment-form-container">
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

