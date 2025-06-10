+++
type = "question"
title = "Tile server usage limit - does free tile server without limit exist?"
description = '''Hi Everyone, We have a leaflet application which is targeted for general public and need to use one of the open-sourced tile server as the basemap. In finding the right tile server, we learned that most of the existing servers have limit on the number of mapviews (number of tiles loaded) per month, ...'''
date = "2014-08-20T19:17:00Z"
lastmod = "2014-08-20T21:53:00Z"
weight = 36032
keywords = [ "leaflet", "tile", "openstreetmap", "mapbox" ]
aliases = [ "/questions/36032" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tile server usage limit - does free tile server without limit exist?](/questions/36032/tile-server-usage-limit-does-free-tile-server-without-limit-exist)

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
<span id="post-36032-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36032-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-36032-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi Everyone,</p>
<p>We have a leaflet application which is targeted for general public and need to use one of the open-sourced tile server as the basemap. In finding the right tile server, we learned that most of the existing servers have limit on the number of mapviews (number of tiles loaded) per month, for example, Mapbox limits 3000 mapviews (1 mapview = 15 tiles) per month under a free account. So I am wondering is there any tile server which provides basemaps that do not have any limit on the number of tiles/request? Does the OpenSreetMap standard style (http://{s}.tile.osm.org/{z}/{x}/{y}.png) also have this limit?</p>
<p>We do not anticipate heavy usage for loading the tiles. I am posting this because my client only want something that's 100% open sourced (free).</p>
<p>Thanks for any input.</p>
<p>Aster</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-tile" rel="tag" title="see questions tagged &#39;tile&#39;">tile</span> <span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-mapbox" rel="tag" title="see questions tagged &#39;mapbox&#39;">mapbox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Aug '14, 19:17</strong></p>
<img src="https://secure.gravatar.com/avatar/5b46329f207d5f257866f5d2d9897f9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="asterxiang&#39;s gravatar image" />
<p><span>asterxiang</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="asterxiang has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Aug '14, 19:18</strong> </span></p>
</div>
</div>
<div id="comments-container-36032" class="comments-container">
&#10;</div>
<div id="comment-tools-36032" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36032-form-container" class="comment-form-container">
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

<span id="36033"></span>

<div id="answer-container-36033" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36033-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-36033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To my knowledge, the most liberal tile server is that run by Mapquest (open.mapquest.com). However, your client seems to mix up two things. OpenStreetMap data is 100% open and doesn't cost you a penny to use, because it is contributed by volunteers who in turn are not paid.</p>
<p>Running a tile server, on the other hand, does cost money. Last I checked, there were no hardware vendors who gave away processors for free, or power companies giving you free power consumption, or Internet providers giving you free access. You need to buy a server, set it up, pay for rack space and power consumption, and so on.</p>
<p>There are organisations who have decided to pay this money and make tile servers available free of charge, but that is totally different from the "open source" or "open data" idea and the two should not be mixed. When you use a free tile server, that is essentially a "sponsored" server, and that "sponsorship" can change end at any time. Unlike the openness of OSM data which is guaranteed by the license and cannot stop.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Aug '14, 21:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-36033" class="comments-container">
<span id="36034"></span>
<div id="comment-36034" class="comment">
<div id="post-36034-score" class="comment-score">
4
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/9492/asterxiang"></a><a href="http://help.openstreetmap.org/users/9492/asterxiang">@asterxiang</a>: I would just like to add the option of running an <a href="http://switch2osm.org/serving-tiles/">own tile server</a>. This has no fixed "limit on the number of tiles/request" – only a hardware limit. And of course you need to run and set it up (which is no simple and cheap task). Setting an own tile server is possible because the OSM data is free (as in "freedom", not as in "free beer", as you already noticed).</p>
</div>
<div id="comment-36034-info" class="comment-info">
<span class="comment-age">(20 Aug '14, 21:53)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-36033" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36033-form-container" class="comment-form-container">
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

