+++
type = "question"
title = "creating layers on offline tiles"
description = '''I want to have tiles available for and offline web-app (local server). However the overlay of POIs will change occasionally. Furthermore, I need to draw routes (vector lines) on the map in real-time based on updating data from the db. Is this possible?'''
date = "2011-02-20T07:00:00Z"
lastmod = "2011-02-21T15:55:00Z"
weight = 3210
keywords = [ "tile", "offline", "overlay" ]
aliases = [ "/questions/3210" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [creating layers on offline tiles](/questions/3210/creating-layers-on-offline-tiles)

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
<span id="post-3210-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3210-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3210-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to have tiles available for and offline web-app (local server). However the overlay of POIs will change occasionally. Furthermore, I need to draw routes (vector lines) on the map in real-time based on updating data from the db.</p>
<p>Is this possible?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tile" rel="tag" title="see questions tagged &#39;tile&#39;">tile</span> <span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span> <span class="post-tag tag-link-overlay" rel="tag" title="see questions tagged &#39;overlay&#39;">overlay</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Feb '11, 07:00</strong></p>
<img src="https://secure.gravatar.com/avatar/987544e21386bb96293f4b96a3f0005c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lee&#39;s gravatar image" />
<p><span>Lee</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lee has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-3210" class="comments-container">
<span id="3212"></span>
<div id="comment-3212" class="comment">
<div id="post-3212-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How big is this area you are talking about, how many routes, and what database?</p>
</div>
<div id="comment-3212-info" class="comment-info">
<span class="comment-age">(20 Feb '11, 08:13)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
</div>
<div id="comment-tools-3210" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3210-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="3238"></span>

<div id="answer-container-3238" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3238-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3238-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-3238-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes it's possible. OpenLayers (a popular slippy map javascript library) can be downloaded and run locally, hence on <a href="http://openlayers.org/"></a><a href="http://openlayers.org"></a><a href="http://openlayers.org">openlayers.org</a> you see a "Link to the hosted version" and a download link. You want to download. And when you come to invoke it with a <code>&lt;script&gt;</code> tag, you would reference a relative path rather than the <a href="http://openlayers.org">openlayers.org</a> URL.</p>
<p>Likewise for the tileset. Rather than having OpenLayers point at a tileset on a remote server (the normal setup) you would point it at relative tile URLs.</p>
<p>You then need tile images arranged in a standard directory structure on your local disk. You might come by these tile files by downloading them from someone else's tile server, e.g. using tile <a href="https://wiki.openstreetmap.org/wiki/Category:Tile_downloading">downloader software</a>, but this approach tends to be problematic for the source server, if you're downloading more than a couple of hundred tiles (a large area of map or several zoom levels). A better thing to do (and much more flexible and fun!) is <a href="https://wiki.openstreetmap.org/wiki/Creating_your_own_tiles">Creating your own tiles</a> (various approaches) Once you've got a directory full of tiles, and figured out how to initialise OpenLayers to the right part of the world... it will happily all work from your local machine, or on webserver on a local network, with no internet connection.</p>
<p>This a unique advantage of OpenStreetMap. Google maps and other providers do not allow their maps to be used in this way.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Feb '11, 15:55</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-3238" class="comments-container">
&#10;</div>
<div id="comment-tools-3238" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3238-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3213"></span>

<div id="answer-container-3213" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3213-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3213-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3213-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It all depends on what you want to do, and what you have: one way would be to:</p>
<ol>
<li>setup a reverse proxy for <a href="http://tile.osm.org">tile.osm.org</a>, to cache tiles. Either a <a href="https://wiki.openstreetmap.org/wiki/ProxySimplePHP">small php script</a>, or <a href="http://www.varnish-cache.org/">Varnish</a></li>
<li>install postgis</li>
<li>install <a href="http://tinyows.org/trac2.">tinyows</a></li>
<li>load WFS from Tinyows on top of Openlayers</li>
</ol>
<p>But I have not seen any tools for updating this in realtime, I'm not entirely sure there are standard tools for that, except just reloading all the features.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Feb '11, 08:28</strong></p>
<img src="https://secure.gravatar.com/avatar/dd3858f5f89f5a6b738f9dbe59824440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emj&#39;s gravatar image" />
<p><span>emj</span><br />
<span class="score" title="2024 reputation points"><span>2.0k</span></span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emj has 11 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-3213" class="comments-container">
&#10;</div>
<div id="comment-tools-3213" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3213-form-container" class="comment-form-container">
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

