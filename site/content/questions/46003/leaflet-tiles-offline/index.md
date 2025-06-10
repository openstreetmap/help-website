+++
type = "question"
title = "leaflet tiles offline"
description = '''in purpose to understand better the ability to work offline with leaflet i need to know couple of things. first i need to know what does it mean : &#x27;https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}&#x27; i understand that this is the url template which provides the tiles, bu...'''
date = "2015-10-20T00:13:00Z"
lastmod = "2015-10-23T20:02:00Z"
weight = 46003
keywords = [ "leaflet", "tiles", "offline" ]
aliases = [ "/questions/46003" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [leaflet tiles offline](/questions/46003/leaflet-tiles-offline)

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
<span id="post-46003-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46003-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46003-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>in purpose to understand better the ability to work offline with leaflet i need to know couple of things.</p>
<p>first i need to know what does it mean : 'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}'</p>
<p>i understand that this is the url template which provides the tiles, but how does it work . which type of file it provides . what the z,x,y represent.</p>
<p>second can someone direct to me to way of getting tiles which suits to leaflet api.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Oct '15, 00:13</strong></p>
<img src="https://secure.gravatar.com/avatar/6b66d6d6b94b411a9d897ff1887c43e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="elad159&#39;s gravatar image" />
<p><span>elad159</span><br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="elad159 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Oct '15, 20:14</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-46003" class="comments-container">
&#10;</div>
<div id="comment-tools-46003" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46003-form-container" class="comment-form-container">
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

<span id="46004"></span>

<div id="answer-container-46004" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46004-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46004-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-46004-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's nobody who provides unlimited free tiles for downloading and using offline. You can get away with downloading <strong>small</strong> <strong>quantities</strong> of tiles from public tile servers using any tile downloader software but you will be blocked if you download larger areas because you're violating their usage policies.</p>
<p>You have to understand the difference between free data (OSM data is free for the taking - you can download everything in one large file) and free services (producing and distributing tiles costs CPU time and bandwidth and these things are not free).</p>
<p>Leaflet will be able to consume standard tile sources with z/x/y tile layout from the local disk. See <a href="http://wiki.openstreetmap.org/wiki/Slippy_map_tilenames">the Wiki</a> for details about the layout.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Oct '15, 00:19</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-46004" class="comments-container">
<span id="46006"></span>
<div id="comment-46006" class="comment">
<div id="post-46006-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>okay so lets sum it up , tiles sources z/x/y is explained in the wiki.</p>
<p>but about the OSM data i dont get it , can i download it from osm , and make it suitable to load up on leaflet. i believe that i have not understand it well yet..</p>
</div>
<div id="comment-46006-info" class="comment-info">
<span class="comment-age">(20 Oct '15, 00:26)</span> <span class="comment-user userinfo">elad159</span>
</div>
</div>
<span id="46007"></span>
<div id="comment-46007" class="comment">
<div id="post-46007-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes:</p>
<p><a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/</a></p>
</div>
<div id="comment-46007-info" class="comment-info">
<span class="comment-age">(20 Oct '15, 00:38)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="46016"></span>
<div id="comment-46016" class="comment">
<div id="post-46016-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i found this site <a href="http://download.geofabrik.de/">http://download.geofabrik.de/</a> as a tiles providers, but still my biggest misunderstanding is about the type of file/image suitable using the slippy maps.</p>
<p>i get to know that the slippy map is a png. "Each zoom level is a directory, each column is a subdirectory, and each tile in that column is a file"</p>
<p>okay but how i make it by my own... i really get messed here, hope someone could help get out this troubles..</p>
</div>
<div id="comment-46016-info" class="comment-info">
<span class="comment-age">(20 Oct '15, 11:55)</span> <span class="comment-user userinfo">elad159</span>
</div>
</div>
<span id="46018"></span>
<div id="comment-46018" class="comment">
<div id="post-46018-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/11589/elad159">@elad159</a> - read <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/</a> . That explains what you need to do to generate the tiles that you are interested in.</p>
</div>
<div id="comment-46018-info" class="comment-info">
<span class="comment-age">(20 Oct '15, 12:28)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="46019"></span>
<div id="comment-46019" class="comment">
<div id="post-46019-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>i think i got it finally...</p>
<p>i will try it later with the server configuration.</p>
<p>thank you very much <a href="http://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> !!</p>
</div>
<div id="comment-46019-info" class="comment-info">
<span class="comment-age">(20 Oct '15, 12:31)</span> <span class="comment-user userinfo">elad159</span>
</div>
</div>
<span id="46082"></span>
<div id="comment-46082" class="comment not_top_scorer">
<div id="post-46082-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> @Fredrick Ramm</p>
</div>
<div id="comment-46082-info" class="comment-info">
<span class="comment-age">(23 Oct '15, 20:02)</span> <span class="comment-user userinfo">elad159</span>
</div>
</div>
</div>
<div id="comment-tools-46004" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-46004-form-container" class="comment-form-container">
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

