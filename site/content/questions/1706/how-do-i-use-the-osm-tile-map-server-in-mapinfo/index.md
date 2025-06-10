+++
type = "question"
title = "How do I use the osm tile map server in mapinfo?"
description = '''How do I use the osm tile map server in mapinfo 10.5? What do the .tab and .xml files have to contain? What does the projection data look like?'''
date = "2010-12-02T15:04:00Z"
lastmod = "2010-12-03T09:28:00Z"
weight = 1706
keywords = [ "tile", "mapinfo10.5", "server" ]
aliases = [ "/questions/1706" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do I use the osm tile map server in mapinfo?](/questions/1706/how-do-i-use-the-osm-tile-map-server-in-mapinfo)

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
<span id="post-1706-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1706-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1706-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do I use the osm tile map server in mapinfo 10.5? What do the .tab and .xml files have to contain? What does the projection data look like?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tile" rel="tag" title="see questions tagged &#39;tile&#39;">tile</span> <span class="post-tag tag-link-mapinfo10.5" rel="tag" title="see questions tagged &#39;mapinfo10.5&#39;">mapinfo10.5</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Dec '10, 15:04</strong></p>
<img src="https://secure.gravatar.com/avatar/c7dfe3b189b79e6e81fa213a4a491cd1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jp_osm&#39;s gravatar image" />
<p><span>jp_osm</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jp_osm has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Jan '11, 14:11</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span></p>
</div>
</div>
<div id="comments-container-1706" class="comments-container">
&#10;</div>
<div id="comment-tools-1706" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1706-form-container" class="comment-form-container">
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

<span id="1710"></span>

<div id="answer-container-1710" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1710-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1710-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-1710-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap tiles are in Spherical Mercator EPSG:900913 (EPSG:3857). The origin is top left. The URL layout is <a href="http://tile.openstreetmap.org/%Z/%X/%Y.png">http://tile.openstreetmap.org/%Z/%X/%Y.png</a></p>
<p>I've never used MapInfo, but a likely good starting point is to modify an existing .tab/.xml setup designed for Google Maps or similar map service.</p>
<p>The OpenStreetMap Tile server has a usage policy: <a href="http://wiki.openstreetmap.org/wiki/Tile_Usage_Policy"></a><a href="http://wiki.openstreetmap.org/wiki/Tile_Usage_Policy"></a><a href="http://wiki.openstreetmap.org/wiki/Tile_Usage_Policy">http://wiki.openstreetmap.org/wiki/Tile_Usage_Policy</a></p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Dec '10, 17:41</strong></p>
<img src="https://secure.gravatar.com/avatar/e79628d44a15e95c607f8c5007d0ccd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Firefishy&#39;s gravatar image" />
<p><span>Firefishy ♦♦</span><br />
<span class="score" title="1296 reputation points"><span>1.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="36 badges"><span class="silver">●</span><span class="badgecount">36</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Firefishy has 14 accepted answers">29%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Dec '10, 17:43</strong> </span></p>
</div>
</div>
<div id="comments-container-1710" class="comments-container">
&#10;</div>
<div id="comment-tools-1710" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1710-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1712"></span>

<div id="answer-container-1712" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1712-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1712-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1712-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thnx The documentation of MapInfo is not very elaborate on it : V 10.5 has Bing incorporated, and further the documentation just says OSM is fully supported.</p>
<p>So from the Bing files and the info of Firefishy I produced :</p>
<p>TAB file:</p>
<p>!table !version 1050 !charset WindowsLatin1</p>
<p>Definition Table</p>
<p>File "open_street.xml"</p>
<p>Type "TILESERVER"</p>
<p>CoordSys Earth Projection 10, 157, 7, 0 Bounds (-20037508.343,-20037508.343) (20037508.343,20037508.343)</p>
<p>and XML file :</p>
<p>[?xml version="1.0" encoding="utf-8"?]</p>
<p>[TileServerInfo Type="LevelRowColumn"]</p>
<p><a href="http://%5BUrl%5Dhttp://tile.openstreetmap.org">[Url]http://tile.openstreetmap.org</a>/{LEVEL}/{ROW}/{COL}.png[/Url]</p>
<p>[MaxLevel]18[/MaxLevel]</p>
<p>[TileSize Height="256" /]</p>
<p>[AttributionText Font="Font("Arial",3,12,0,16777215)"]OpenStreetMap[/AttributionText] [/TileServerInfo]</p>
<p>This works fairly well, but it has the same problem as I had with Bing (which promted my efforts in the first place) : the produced maps are not very sharp, they appear somewhat fuzzy at any zoom level.</p>
<p>Probably has to do with resolution of mapwindows in MapInfo, compared to the downloaded tiles : I suppose I have to somehow adjust the MapWindow to multiples of 256 pixels or so ...</p>
<p>Not sure on how to go about that : Any ideas are welcom</p>
<p>By the way, I am a very light user.</p>
<p>jp_osm</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Dec '10, 09:28</strong></p>
<img src="https://secure.gravatar.com/avatar/c7dfe3b189b79e6e81fa213a4a491cd1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jp_osm&#39;s gravatar image" />
<p><span>jp_osm</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jp_osm has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1712" class="comments-container">
&#10;</div>
<div id="comment-tools-1712" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1712-form-container" class="comment-form-container">
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

