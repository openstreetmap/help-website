+++
type = "question"
title = "Extract osm data for zoom 1-4"
description = '''Hey, I have a working local tile server with all planet data imported to its postgres DB. I also kept the planet file that I&#x27;ve used to import with. Now, I need another local-tile server which must have data only for zoom level 1-4 (inclusive). How can I extract this data from my previous server in ...'''
date = "2015-03-25T14:17:00Z"
lastmod = "2015-03-31T12:42:00Z"
weight = 41915
keywords = [ "extract", "export", "local-tile-server", "osm", "osmosis" ]
aliases = [ "/questions/41915" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extract osm data for zoom 1-4](/questions/41915/extract-osm-data-for-zoom-1-4)

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
<span id="post-41915-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41915-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41915-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey, I have a working local tile server with all planet data imported to its postgres DB. I also kept the planet file that I've used to import with.</p>
<p>Now, I need another local-tile server which must have data only for zoom level 1-4 (inclusive). How can I extract this data from my previous server in order to load it to the new one??</p>
<p>have tried osmosis with no luck (both on pg &amp; xml)</p>
<p>Thanks, Nir</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-local-tile-server" rel="tag" title="see questions tagged &#39;local-tile-server&#39;">local-tile-server</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Mar '15, 14:17</strong></p>
<img src="https://secure.gravatar.com/avatar/6baeac6eaec0495b46facbe28aafac46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arvivn&#39;s gravatar image" />
<p><span>arvivn</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arvivn has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-41915" class="comments-container">
&#10;</div>
<div id="comment-tools-41915" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41915-form-container" class="comment-form-container">
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

<span id="41916"></span>

<div id="answer-container-41916" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41916-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41916-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-41916-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The total number of tiles for zoom levels 1-4, world-wide, is 341. I suggest that you download those with wget or any tile downloader from your old server, and put them into the web space of the new server; problem solved, no tile server needed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Mar '15, 14:27</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-41916" class="comments-container">
<span id="42058"></span>
<div id="comment-42058" class="comment">
<div id="post-42058-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>the "small" tile server contains a few countries with full OSM data so I can't give up for it....</p>
<p>Your idea of pre-fetching is good and now the question is where and shall I put the tiles on the "small" tile-server so that it will use them instead of rendering (ie CAHCE).</p>
<p>Thanks! Nir</p>
</div>
<div id="comment-42058-info" class="comment-info">
<span class="comment-age">(31 Mar '15, 09:46)</span> <span class="comment-user userinfo">arvivn</span>
</div>
</div>
<span id="42061"></span>
<div id="comment-42061" class="comment">
<div id="post-42061-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Put them anywhere you like - just point whatever library you're using to serve tiles at that location.</p>
<p>If you're using <a href="http://leafletjs.com/">leaflet</a>, something like <a href="https://github.com/SomeoneElseOSM/OSMembedded/blob/master/Scripts/leaflet_embed.js#L16">this</a> would work.</p>
</div>
<div id="comment-42061-info" class="comment-info">
<span class="comment-age">(31 Mar '15, 11:33)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="42066"></span>
<div id="comment-42066" class="comment">
<div id="post-42066-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>didn't catch that... I have a map client which accepts an address of tiles-server. where shall I put the cached tiles so the server will use them fluently?</p>
</div>
<div id="comment-42066-info" class="comment-info">
<span class="comment-age">(31 Mar '15, 12:29)</span> <span class="comment-user userinfo">arvivn</span>
</div>
</div>
<span id="42067"></span>
<div id="comment-42067" class="comment">
<div id="post-42067-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In any directory you want as long as this directory is available via your HTTP server. The address of your HTTP server plus this directory will then be your tile server address.</p>
</div>
<div id="comment-42067-info" class="comment-info">
<span class="comment-age">(31 Mar '15, 12:42)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41916" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41916-form-container" class="comment-form-container">
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

