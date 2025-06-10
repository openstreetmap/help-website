+++
type = "question"
title = "Generate overlays maps with roads and paths only (Key:highway=*)"
description = '''Is there a way to generate offline overlays maps with roads and pathways only? (Key:highway=*)  I want to use it in an Android app to extend older raster maps. Preferably in RMaps SQLite Maps (*.sqlitedb) format. (Using Alpinequest)  It doesn&#x27;t need to be offline, but I have not yet found a tile ser...'''
date = "2021-07-05T14:10:00Z"
lastmod = "2021-07-09T17:18:00Z"
weight = 80828
keywords = [ "path", "sqlite", "offlinemaps", "highway", "overlay" ]
aliases = [ "/questions/80828" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Generate overlays maps with roads and paths only (Key:highway=\*)](/questions/80828/generate-overlays-maps-with-roads-and-paths-only-keyhighway)

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
<span id="post-80828-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80828-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80828-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to generate offline overlays maps with roads and pathways <strong>only</strong>? (Key:highway=*) I want to use it in an Android app to extend older raster maps.</p>
<p>Preferably in RMaps SQLite Maps (*.sqlitedb) format. (Using Alpinequest)</p>
<p>It doesn't need to be offline, but I have not yet found a tile server that does highway only. There is hiking.waymarkedtrails.org. but it shows waymarked trails only.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-path" rel="tag" title="see questions tagged &#39;path&#39;">path</span> <span class="post-tag tag-link-sqlite" rel="tag" title="see questions tagged &#39;sqlite&#39;">sqlite</span> <span class="post-tag tag-link-offlinemaps" rel="tag" title="see questions tagged &#39;offlinemaps&#39;">offlinemaps</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span> <span class="post-tag tag-link-overlay" rel="tag" title="see questions tagged &#39;overlay&#39;">overlay</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jul '21, 14:10</strong></p>
<img src="https://secure.gravatar.com/avatar/b72600e8c4b6b538b85bb3937677bef0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="knix&#39;s gravatar image" />
<p><span>knix</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="knix has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Jul '21, 13:03</strong> </span></p>
</div>
</div>
<div id="comments-container-80828" class="comments-container">
&#10;</div>
<div id="comment-tools-80828" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80828-form-container" class="comment-form-container">
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

<span id="80853"></span>

<div id="answer-container-80853" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80853-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80853-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-80853-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This probably is nowhere near the best solution, but OsmAnd <a href="https://docs.osmand.net/en/main@latest/osmand/map/raster-maps">allows</a> raster map backgrounds with a highway overlay and is open source.</p>
<p>If you already have a way of generating the tiles you need, but need a way of excluding certain features, there are tools like <a href="https://wiki.openstreetmap.org/wiki/Osmosis">osmosis</a> and <a href="https://wiki.openstreetmap.org/wiki/Osmium">osmium</a> for filtering data before you feed it into your tile generator.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jul '21, 19:07</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-80853" class="comments-container">
<span id="80896"></span>
<div id="comment-80896" class="comment">
<div id="post-80896-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was not able to find any setting that allows OsmAnd to overlay highways only, can you please elaborate?</p>
</div>
<div id="comment-80896-info" class="comment-info">
<span class="comment-age">(09 Jul '21, 10:07)</span> <span class="comment-user userinfo">knix</span>
</div>
</div>
<span id="80898"></span>
<div id="comment-80898" class="comment">
<div id="post-80898-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In OsmAnd you need to:</p>
<ol>
<li>Enable the online maps plugin.</li>
<li>In the <em>Configure Map</em> dialogue:</li>
<li>enable an Underlay map</li>
<li>suppress undesired features under the <em>Hide</em> menu.</li>
</ol>
<p>The description for the Online maps plugin mentions that it can display tiles pre-packaged as a SQLite database and dropped in the data folder (<a href="https://shallowsky.com/blog/mapping/osmand-making-overlay-maps.html">Googled tutoiral</a>), I'm not sure if it can be configured to point at another online provider.</p>
</div>
<div id="comment-80898-info" class="comment-info">
<span class="comment-age">(09 Jul '21, 12:59)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="80899"></span>
<div id="comment-80899" class="comment">
<div id="post-80899-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Adding a new online map source now seems to be something like:</p>
<p>Menu / Configure Map / Map source / Add</p>
<p>Either enter details for a new one or "select existing". Edit and save</p>
<p>example URL <a href="http://map.atownsend.org.uk/hot/%7B0%7D/%7B1%7D/%7B2%7D.png">http://map.atownsend.org.uk/hot/{0}/{1}/{2}.png</a></p>
<p>min zoom 0 max zoom 24 don't tick "elliptic mercator"</p>
<p>(those last settings will vary by site of course)</p>
</div>
<div id="comment-80899-info" class="comment-info">
<span class="comment-age">(09 Jul '21, 13:25)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="80901"></span>
<div id="comment-80901" class="comment">
<div id="post-80901-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm still not able to follow. I have no problem to add online sources or custom maps. That's not what am asking for.<br />
I have set my own map as default map and OSM online as Underlay. Then Hiding features in the "Hide" menu does nothing.</p>
</div>
<div id="comment-80901-info" class="comment-info">
<span class="comment-age">(09 Jul '21, 14:08)</span> <span class="comment-user userinfo">knix</span>
</div>
</div>
<span id="80904"></span>
<div id="comment-80904" class="comment">
<div id="post-80904-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The original question was a way to have OSM roads over raster maps on Android. Offline rendering in OsmAnd uses OSM data and always considers itself to be the middle, so if you want OSM over your raster tiles you need to set your raster tiles to be "underlay". This will then default to suppressing area rendering but not building or highway rendering (buildings can be suppressed in the hide menu). You will have to have downloaded the OsmAnd map for the country/region you are in for offline rendering to work.</p>
</div>
<div id="comment-80904-info" class="comment-info">
<span class="comment-age">(09 Jul '21, 15:19)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="80907"></span>
<div id="comment-80907" class="comment not_top_scorer">
<div id="post-80907-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, thanks I got it work, I had to disable "Show polygons" on the underlay map. Here is the complete steps</p>
<ol>
<li><p>Set Mapsource = Offline vector maps</p></li>
<li><p>Overlay map = none</p></li>
<li><p>Underlay map = Your map (Disable "Show polygons")</p></li>
<li><p>Map style = OsmAnd</p></li>
<li><p>Hide = Enable everything except "Overground objects"</p></li>
</ol>
</div>
<div id="comment-80907-info" class="comment-info">
<span class="comment-age">(09 Jul '21, 17:18)</span> <span class="comment-user userinfo">knix</span>
</div>
</div>
</div>
<div id="comment-tools-80853" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-80853-form-container" class="comment-form-container">
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

