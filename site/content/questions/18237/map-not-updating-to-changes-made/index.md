+++
type = "question"
title = "map not updating to changes made"
description = '''Hi I have my own tile-server which serves an OSM map. I have the OSM data stored in a PostGIS database and use Mod_tile, renderd and mapnik. I have added a point the the points table and have confirmed it has been added. However the change doesn&#x27;t show on the map. How long does it take for the chang...'''
date = "2012-12-06T12:16:00Z"
lastmod = "2012-12-07T22:59:00Z"
weight = 18237
keywords = [ "rendering", "renderd", "osm", "mapnik", "mod_tile" ]
aliases = [ "/questions/18237" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [map not updating to changes made](/questions/18237/map-not-updating-to-changes-made)

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
<span id="post-18237-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18237-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18237-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I have my own tile-server which serves an OSM map. I have the OSM data stored in a PostGIS database and use Mod_tile, renderd and mapnik.</p>
<p>I have added a point the the points table and have confirmed it has been added. However the change doesn't show on the map. How long does it take for the change to display? I made the edit about 15 hours ago. I even added /dirty to the end of the url of the changed tile but it still has not re-rendered.</p>
<p>Also, is there a way to view the queue of tiles waiting to be rendered?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Dec '12, 12:16</strong></p>
<img src="https://secure.gravatar.com/avatar/8f19a0a6b0afe902c224e03a8eb38ece?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srose&#39;s gravatar image" />
<p><span>srose</span><br />
<span class="score" title="161 reputation points">161</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srose has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18237" class="comments-container">
&#10;</div>
<div id="comment-tools-18237" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18237-form-container" class="comment-form-container">
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

<span id="18252"></span>

<div id="answer-container-18252" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18252-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18252-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18252-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Did you read <a href="https://wiki.openstreetmap.org/wiki/Mod_tile#renderd">https://wiki.openstreetmap.org/wiki/Mod_tile#renderd</a> -&gt; tile expiry ?</p>
<p>As long as you do not a full planet import which would update the import time stamp, tiles are not expired. You have to do this manually. For testing you could just delete the tile or all tiles from the tile-cache folder.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Dec '12, 15:20</strong></p>
<img src="https://secure.gravatar.com/avatar/9ac1de0d402dfdf47bd4c4d664156c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AddisMap_Alexander&#39;s gravatar image" />
<p><span>AddisMap_Ale...</span><br />
<span class="score" title="1120 reputation points"><span>1.1k</span></span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AddisMap_Alexander has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18252" class="comments-container">
<span id="18289"></span>
<div id="comment-18289" class="comment">
<div id="post-18289-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi. Thanks for the response. Got a few questions. First, where is the cache folder for the tiles? The only folder I could find with tiles in it was the default folder in /var/lib/mod_tile.</p>
<p>Also, the the app that I'm making will be making changes to the osm data in the postgis DB. What would be a good way of getting the data to automatically re render without me having to manually delete the cache folder?</p>
</div>
<div id="comment-18289-info" class="comment-info">
<span class="comment-age">(07 Dec '12, 22:59)</span> <span class="comment-user userinfo">srose</span>
</div>
</div>
</div>
<div id="comment-tools-18252" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18252-form-container" class="comment-form-container">
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

