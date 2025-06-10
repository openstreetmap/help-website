+++
type = "question"
title = "Is there a simple way to turn .osm file to tile.png ?"
description = '''I am a totally newbie for open street map, map drawing etc. I&#x27;m trying to do indoor map for a building. I&#x27;ve draw the map of the building with josm and have .osm file. I have to implement the map to the flutter and found a plugin called flutter_map which is leaflet implementation for flutter. Than I...'''
date = "2021-11-20T13:44:00Z"
lastmod = "2021-11-23T18:27:00Z"
weight = 82628
keywords = [ "generate_tiles", "tiles", "indoor", "josm", "tileserver" ]
aliases = [ "/questions/82628" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a simple way to turn .osm file to tile.png ?](/questions/82628/is-there-a-simple-way-to-turn-osm-file-to-tilepng)

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
<span id="post-82628-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82628-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82628-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am a totally newbie for open street map, map drawing etc. I'm trying to do indoor map for a building. I've draw the map of the building with josm and have .osm file. I have to implement the map to the flutter and found a plugin called flutter_map which is leaflet implementation for flutter. Than I've realized that i have to use tile.png. I googled it and found that i should build my own tile server. Since there is only one little building in my map, isn't there a simpler way to turn .osm in tile.png instead of using server ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-generate_tiles" rel="tag" title="see questions tagged &#39;generate_tiles&#39;">generate_tiles</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-indoor" rel="tag" title="see questions tagged &#39;indoor&#39;">indoor</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Nov '21, 13:44</strong></p>
<img src="https://secure.gravatar.com/avatar/7f1c260e99dffff55f895757e570cf43?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baranacikgoz&#39;s gravatar image" />
<p><span>baranacikgoz</span><br />
<span class="score" title="76 reputation points">76</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baranacikgoz has 2 accepted answers">100%</span></p>
</div>
</div>
<div id="comments-container-82628" class="comments-container">
&#10;</div>
<div id="comment-tools-82628" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82628-form-container" class="comment-form-container">
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

<span id="82650"></span>

<div id="answer-container-82650" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82650-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82650-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82650-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Docker was easier than i thought. Solved with docker tile server.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Nov '21, 16:17</strong></p>
<img src="https://secure.gravatar.com/avatar/7f1c260e99dffff55f895757e570cf43?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baranacikgoz&#39;s gravatar image" />
<p><span>baranacikgoz</span><br />
<span class="score" title="76 reputation points">76</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baranacikgoz has 2 accepted answers">100%</span></p>
</div>
</div>
<div id="comments-container-82650" class="comments-container">
<span id="82651"></span>
<div id="comment-82651" class="comment">
<div id="post-82651-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Was that <a href="https://switch2osm.org/serving-tiles/using-a-docker-container/">https://switch2osm.org/serving-tiles/using-a-docker-container/</a> or something else?</p>
</div>
<div id="comment-82651-info" class="comment-info">
<span class="comment-age">(22 Nov '21, 16:40)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="82664"></span>
<div id="comment-82664" class="comment">
<div id="post-82664-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yep, switch2osm's docker tile server</p>
</div>
<div id="comment-82664-info" class="comment-info">
<span class="comment-age">(23 Nov '21, 18:27)</span> <span class="comment-user userinfo">baranacikgoz</span>
</div>
</div>
</div>
<div id="comment-tools-82650" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82650-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82629"></span>

<div id="answer-container-82629" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82629-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82629-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82629-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't think there is such solution. Probably the most simple way is to learn tool like QGIS, import the data and define how do you want to see all the things, then export the image. This way you avoid server, but still I'm not aware of the solution that would be much simpler than that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Nov '21, 14:08</strong></p>
<img src="https://secure.gravatar.com/avatar/e228dd20b7da2a6c8f559e2118ce08d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kocio&#39;s gravatar image" />
<p><span>kocio</span><br />
<span class="score" title="2054 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kocio has 14 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-82629" class="comments-container">
<span id="82631"></span>
<div id="comment-82631" class="comment">
<div id="post-82631-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The QMetaTiles plugin can export a set of tiles from QGIS.</p>
<p>While QGIS <a href="https://wiki.openstreetmap.org/wiki/QGIS#Vector_data">does support</a> the <code>.osm</code> file format <a href="https://gdal.org/drivers/vector/osm.html">via GDAL</a> the default configuration does not split out the indoor tags for easy rendering, you will probably want to use a custom config file for the indoor tags. You will almost certainly need to create your own style for rendering this. Unfortunately, in my experience QGIS's learning curve is at least as steep as JOSM.</p>
</div>
<div id="comment-82631-info" class="comment-info">
<span class="comment-age">(20 Nov '21, 16:11)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-82629" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82629-form-container" class="comment-form-container">
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

