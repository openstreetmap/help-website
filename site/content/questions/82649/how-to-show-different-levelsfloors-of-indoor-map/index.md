+++
type = "question"
title = "How to show different levels/floors of indoor map ?"
description = '''I have 2 different method of showing map but same question;   I have a local tile server which is running with docker. I&#x27;ve added different levels to my indoor map with josm indoorHelper plugin. How can i show/switch between these levels?  Different from this tile server, i am working on second map ...'''
date = "2021-11-22T14:48:00Z"
lastmod = "2021-11-22T19:05:00Z"
weight = 82649
keywords = [ "openstreetmap", "mapsforge", "indoor", "flutter", "tileserver" ]
aliases = [ "/questions/82649" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to show different levels/floors of indoor map ?](/questions/82649/how-to-show-different-levelsfloors-of-indoor-map)

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
<span id="post-82649-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82649-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82649-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have 2 different method of showing map but same question;</p>
<ol>
<li>I have a local tile server which is running with docker. I've added different levels to my indoor map with josm indoorHelper plugin. How can i show/switch between these levels?</li>
<li>Different from this tile server, i am working on second map showing method. Have a flutter app and a plugin called mapsforge with it. I have the same indoor map. And plugins readme offers this code; <code>new MapFileData( url: "https://raw.githubusercontent.com/mikes222/mapsforge_flutter/master/example/map_files/Chemnitz Uni.map", fileName: "Chemnitz Uni.map", displayedName: "Chemnitz - University (Indoor)", initialPositionLat: 50.81348, initialPositionLong: 12.92936, initialZoomLevel: 18, indoorZoomOverlay: true, indoorLevels: {1: 'OG', 0: 'EG', -1: 'UG'}, ),</code> So there is a section <code>indoorLevels: {1: 'OG', 0: 'EG', -1: 'UG'},</code> and when i write this code with my map, these levels shows nothing. How can i define my different levels?</li>
</ol>
<p>To sum up with 1st and 2nd method i am having difficulties to show different levels/floors</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-mapsforge" rel="tag" title="see questions tagged &#39;mapsforge&#39;">mapsforge</span> <span class="post-tag tag-link-indoor" rel="tag" title="see questions tagged &#39;indoor&#39;">indoor</span> <span class="post-tag tag-link-flutter" rel="tag" title="see questions tagged &#39;flutter&#39;">flutter</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Nov '21, 14:48</strong></p>
<img src="https://secure.gravatar.com/avatar/7f1c260e99dffff55f895757e570cf43?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baranacikgoz&#39;s gravatar image" />
<p><span>baranacikgoz</span><br />
<span class="score" title="76 reputation points">76</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baranacikgoz has 2 accepted answers">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Nov '21, 14:49</strong> </span></p>
</div>
</div>
<div id="comments-container-82649" class="comments-container">
<span id="82652"></span>
<div id="comment-82652" class="comment">
<div id="post-82652-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I don't know if these are remotely helpful for you, but the three websites used for examples on the <a href="https://wiki.openstreetmap.org/wiki/Simple_Indoor_Tagging">Simple Indoor tagging</a> page all appear to be open source according to their wiki pages: <a href="https://wiki.openstreetmap.org/wiki/OpenLevelUp">OpenLevelUp</a>,<a href="https://wiki.openstreetmap.org/wiki/Indoor%3D">Indoor=</a>,<a href="https://wiki.openstreetmap.org/wiki/OpenIndoor">OpenIndoor</a>. It may be possible to crib what they do? I would not recommend hitting overpass repeatedly for the same building, but if they're using GeoJSON it might be a very small file to store locally if you're only doing one building.</p>
</div>
<div id="comment-82652-info" class="comment-info">
<span class="comment-age">(22 Nov '21, 19:05)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-82649" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82649-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

