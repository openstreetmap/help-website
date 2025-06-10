+++
type = "question"
title = "how to use my osm server for my web site"
description = '''can someone please help me to know how make use of my osm server i have been trying to install openstreetmap web site on my own site and finally succeeded installing a tile server and api server so now how do i do these things  if i want to display a marker of a store for example on a a page from my...'''
date = "2017-10-31T13:38:00Z"
lastmod = "2017-11-03T15:46:00Z"
weight = 60370
keywords = [ "usage" ]
aliases = [ "/questions/60370" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to use my osm server for my web site](/questions/60370/how-to-use-my-osm-server-for-my-web-site)

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
<span id="post-60370-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60370-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60370-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>can someone please help me to know how make use of my osm server</p>
<p>i have been trying to install openstreetmap web site on my own site and finally succeeded installing a tile server and api server</p>
<p>so now how do i do these things</p>
<ul>
<li>if i want to display a marker of a store for example on a a page from my web site (from api or tile)</li>
<li>if i want to display multiple markers on a page that a user may click to view nearby restaurants fetched from my osm server (from api or tile)</li>
<li>if i want to take input from a user (lon,lat) by letting him point a marker (from api or tile)</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-usage" rel="tag" title="see questions tagged &#39;usage&#39;">usage</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Oct '17, 13:38</strong></p>
<img src="https://secure.gravatar.com/avatar/f8c47b3830f7447fdc5ebd166eb210c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="engragy&#39;s gravatar image" />
<p><span>engragy</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="engragy has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Nov '17, 15:09</strong> </span></p>
</div>
</div>
<div id="comments-container-60370" class="comments-container">
<span id="60451"></span>
<div id="comment-60451" class="comment">
<div id="post-60451-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>is this a very hard question or is it too dump please if someone knows a link to some documents that may help please advise</p>
</div>
<div id="comment-60451-info" class="comment-info">
<span class="comment-age">(03 Nov '17, 13:35)</span> <span class="comment-user userinfo">engragy</span>
</div>
</div>
<span id="60452"></span>
<div id="comment-60452" class="comment">
<div id="post-60452-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Perhaps people might be a bit confused about what question you're asking? Maybe some of the things at <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a> and <a href="http://leafletjs.com/examples.html">http://leafletjs.com/examples.html</a> might help?</p>
</div>
<div id="comment-60452-info" class="comment-info">
<span class="comment-age">(03 Nov '17, 14:02)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="60454"></span>
<div id="comment-60454" class="comment">
<div id="post-60454-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thank you for your response but i have already installed tile server and api server and i do know that i have to use openlayers or leaflet but what i dont konw is am i going to work leaflet for example on the api(i mean port 3000) or the normal tile sever</p>
</div>
<div id="comment-60454-info" class="comment-info">
<span class="comment-age">(03 Nov '17, 15:16)</span> <span class="comment-user userinfo">engragy</span>
</div>
</div>
<span id="60455"></span>
<div id="comment-60455" class="comment">
<div id="post-60455-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That depends on where you want things to appear and how interactive they are. If you want something to be displayed as part of the background tile images, then you'd modify the style on the tile server. If you want clickable markers overlaid over the tiles, then you'd use the API to retrieve the necessary information and create markers in Leaflet/OpenLayers.</p>
</div>
<div id="comment-60455-info" class="comment-info">
<span class="comment-age">(03 Nov '17, 15:46)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-60370" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60370-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

