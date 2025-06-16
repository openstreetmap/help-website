+++
type = "question"
title = "OpenStreetMap in non-Web application"
description = '''Hi all, first of all, sorry for my newbie question as I am new to OpenStreetMap and could not really find answers to my questions. I hope someone has the patience to answer these. Thanks in advance. I have a commercial non-Web windows app (Windows Forms or WPF) and I would like this app to have a ma...'''
date = "2014-09-11T07:40:00Z"
lastmod = "2014-10-01T14:46:00Z"
weight = 36745
keywords = [ "wpf", "commercial", "gmap" ]
aliases = [ "/questions/36745" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [OpenStreetMap in non-Web application](/questions/36745/openstreetmap-in-non-web-application)

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
<span id="post-36745-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36745-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36745-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>first of all, sorry for my newbie question as I am new to OpenStreetMap and could not really find answers to my questions. I hope someone has the patience to answer these. Thanks in advance.</p>
<p>I have a commercial non-Web windows app (Windows Forms or WPF) and I would like this app to have a map window that would be based on downloading map tiles on the background and offer the user all expected features like moving, zooming the map etc. and displaying his own localized objects (stored locally) - very similar what the GMap.NET project does.</p>
<ol>
<li><p>Is it possible to make such an application to download all the map data from the OpenStreetMap servers or do we have to find a different (commercial) provider? Using Google Maps for example, one has to pay when the traffic of downloading all the map tiles gets high.</p></li>
<li><p>Is there an API that is recommended for this purpose (ie. downloading map tiles for different map areas to build an interactive map? I know, that GMap.NET found a way, but is this a documented API, which is not subject to future changes which would, of course, break such an application?</p></li>
</ol>
<p>Thank you very much.</p>
<p>Alex</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wpf" rel="tag" title="see questions tagged &#39;wpf&#39;">wpf</span> <span class="post-tag tag-link-commercial" rel="tag" title="see questions tagged &#39;commercial&#39;">commercial</span> <span class="post-tag tag-link-gmap" rel="tag" title="see questions tagged &#39;gmap&#39;">gmap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Sep '14, 07:40</strong></p>
<img src="https://secure.gravatar.com/avatar/db462b8ae34a93bca420176e8c4723eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alex780526&#39;s gravatar image" />
<p><span>Alex780526</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alex780526 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-36745" class="comments-container">
<span id="36760"></span>
<div id="comment-36760" class="comment">
<div id="post-36760-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just to clarify: would your application be connected to the internet (i.e. could it request map tiles from an external server), or do you want to have all the map tiles stored locally?</p>
</div>
<div id="comment-36760-info" class="comment-info">
<span class="comment-age">(11 Sep '14, 12:14)</span> <span class="comment-user userinfo">Lightsider</span>
</div>
</div>
</div>
<div id="comment-tools-36745" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36745-form-container" class="comment-form-container">
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

<span id="36759"></span>

<div id="answer-container-36759" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36759-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36759-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-36759-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Alex780526 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Wiki page <a href="https://wiki.openstreetmap.org/wiki/Tile_usage_policy">tile usage policy</a> could help to answer your question. The underlying <em>data</em> is free to download and use; the map tiles (ie the visualised data) are not. It's a question of server costs - users of your application would be creating an additional load for the OSM tile servers.</p>
<p>For your internal testing purposes, you can use the tiles generated by the OSM tile servers (for information on how to do this, see the <a href="https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames">slippy map</a> page on the Wiki or the <a href="http://switch2osm.org/using-tiles/">"using tiles"</a> page on switch2osm - I'm afraid I'm not an expert in this). Once you deploy your application, however, it would be best to use a commercial third-party tile server (such as MapQuest Open, Geofabrik, Mapbox, etc - see lists <a href="https://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services">here</a> and <a href="http://switch2osm.org/providers/">here</a>) - although note that they also have conditions you have to abide by. Alternatively, you can set up your own server to generate the map tiles and make them available to your application (the <a href="http://switch2osm.org/">switch2osm</a> web site has some guidance on how to set up your own server).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Sep '14, 12:13</strong></p>
<img src="https://secure.gravatar.com/avatar/390c3a1e9ea7b1f10deea61828ad66eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lightsider&#39;s gravatar image" />
<p><span>Lightsider</span><br />
<span class="score" title="1540 reputation points"><span>1.5k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lightsider has 9 accepted answers">42%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Sep '14, 13:32</strong> </span></p>
</div>
</div>
<div id="comments-container-36759" class="comments-container">
<span id="36767"></span>
<div id="comment-36767" class="comment">
<div id="post-36767-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>You missed an important point : it is also possible to use third party OSM tiles providers like MapQuest Open, Geofabrik, Mapbox, etc. They have also restrictions and depends on the traffic. To be checked with them. List here <a href="https://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services">https://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services</a></p>
</div>
<div id="comment-36767-info" class="comment-info">
<span class="comment-age">(11 Sep '14, 15:18)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="36796"></span>
<div id="comment-36796" class="comment">
<div id="post-36796-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Good point; thank you! I have updated my answer.</p>
</div>
<div id="comment-36796-info" class="comment-info">
<span class="comment-age">(12 Sep '14, 13:32)</span> <span class="comment-user userinfo">Lightsider</span>
</div>
</div>
<span id="37188"></span>
<div id="comment-37188" class="comment">
<div id="post-37188-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Ok, guys, thank you both for the informative answers. Alex</p>
</div>
<div id="comment-37188-info" class="comment-info">
<span class="comment-age">(01 Oct '14, 14:46)</span> <span class="comment-user userinfo">Alex780526</span>
</div>
</div>
</div>
<div id="comment-tools-36759" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36759-form-container" class="comment-form-container">
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

