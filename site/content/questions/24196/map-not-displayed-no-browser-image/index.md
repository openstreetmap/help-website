+++
type = "question"
title = "Map not displayed - no browser image"
description = '''Hi All, I&#x27;m very new to all this openstreet and tile server stuff... I have followed the switch2osm link for manually building a tile server on ubunto 12.04 from: http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/ Eventually, the planet.osm import has ended BUT unfortunately ...'''
date = "2013-07-13T06:31:00Z"
lastmod = "2013-07-17T18:25:00Z"
weight = 24196
keywords = [ "tileserver" ]
aliases = [ "/questions/24196" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Map not displayed - no browser image](/questions/24196/map-not-displayed-no-browser-image)

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
<span id="post-24196-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24196-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24196-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All,</p>
<p>I'm very new to all this openstreet and tile server stuff...</p>
<p>I have followed the switch2osm link for manually building a tile server on ubunto 12.04 from: <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/">http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/</a></p>
<p>Eventually, the planet.osm import has ended BUT unfortunately when browsing to the server address has described in the manual - i don't get any image although i can see the request on the Tile Server after starting it.</p>
<p>all i see is: renderd[35717]: DEBUG: Got command Render fd(16) xml(default), z(20), x(30), y(10) renderd[35717]: DEBUG: Connection 8, fd 28 closed, now 8 left</p>
<p>Apache is started successfully (i think): [Sat Jul 13 08:22:16 2013] [warn] Could not determine host name of server to configure tile-json request. Using localhost instead [Sat Jul 13 08:22:16 2013] [notice] Loading tile config style2 at for zooms 0 - 20 from tile directory /var/lib/mod_tile with extension .png and mime type image/png ...done.</p>
<p>Can someone please assist? What am i missing?</p>
<p>I've also found this thread which also is similiar to my problem but still no luck: <a href="/questions/23257/map-not-displayed-in-the-browser-and-mod_tile-folder-is-empty">https://help.openstreetmap.org/questions/23257/map-not-displayed-in-the-browser-and-mod_tile-folder-is-empty</a></p>
<p>Currently my renderd.conf is completely the same as described in this thread (only using my username and gis db).</p>
<p>Any ideas ? How should i debugging this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jul '13, 06:31</strong></p>
<img src="https://secure.gravatar.com/avatar/2f9f3efb452a3ec066382118ee9a48da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Avisht&#39;s gravatar image" />
<p><span>Avisht</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Avisht has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24196" class="comments-container">
<span id="24323"></span>
<div id="comment-24323" class="comment">
<div id="post-24323-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When running osm2pgsql did you get a message such as "Osm2pgsql took 86400s overall" at the end of the data load process?</p>
<p>What happens when you run renderd interactively and try and browse to "http://yourserveraddress/osm_tiles/0/0/0.png"?</p>
</div>
<div id="comment-24323-info" class="comment-info">
<span class="comment-age">(17 Jul '13, 18:25)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-24196" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24196-form-container" class="comment-form-container">
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

<span id="24265"></span>

<div id="answer-container-24265" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24265-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24265-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-24265-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't think we have enough information to tell you where things are going wrong for you, but in general it's probably a good idea to do some checks. Did the Mapnik install go OK? Try using <code>generate_image.py</code> to generate a non-tiled image of a region of map data. No luck with that? Rewind a bit further. Did the postGIS database loading go OK? With psql command-line or using pgadmin tool, poke around in your database and see if there any records.</p>
<p>The switch2osm docs are good but brief. There's more <a href="https://wiki.openstreetmap.org/wiki/Mapnik">Mapnik &amp; OSM install documentation here</a>, which might give more clues when things go wrong.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jul '13, 16:13</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-24265" class="comments-container">
&#10;</div>
<div id="comment-tools-24265" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24265-form-container" class="comment-form-container">
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

