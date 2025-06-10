+++
type = "question"
title = "Can I use OSM data as layer in my WMS server"
description = '''Can I use OSM data as layer in my WMS server and show it as overlay on top of bluemarble in OpenLayers?'''
date = "2013-07-22T14:56:00Z"
lastmod = "2013-07-23T15:34:00Z"
weight = 24453
keywords = [ "wms", "openlayers" ]
aliases = [ "/questions/24453" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can I use OSM data as layer in my WMS server](/questions/24453/can-i-use-osm-data-as-layer-in-my-wms-server)

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
<span id="post-24453-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24453-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24453-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can I use OSM data as layer in my WMS server and show it as overlay on top of bluemarble in OpenLayers?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wms" rel="tag" title="see questions tagged &#39;wms&#39;">wms</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jul '13, 14:56</strong></p>
<img src="https://secure.gravatar.com/avatar/621445c30169bf1ad7ace0b81bfb0355?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gjw01&#39;s gravatar image" />
<p><span>gjw01</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gjw01 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24453" class="comments-container">
&#10;</div>
<div id="comment-tools-24453" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24453-form-container" class="comment-form-container">
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

<span id="24455"></span>

<div id="answer-container-24455" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24455-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24455-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-24455-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use OSM <em>data</em> but you will need suitable styling rules for your WMS to make OSM data appear like a nice map. Check out <a href="https://github.com/mapserver/basemaps">https://github.com/mapserver/basemaps</a> if your WMS is a UMN MapServer, or search the web for suitable stylings and import rules if you use a different WMS.</p>
<p>There are existing WMS servers with OSM data that you can use; some are free, some cost money. Some cover all of the world, some just a part. Some are updated regularly, some just twice a year. See <a href="http://wiki.openstreetmap.org/wiki/WMS">our Wiki</a> for details.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jul '13, 15:45</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-24455" class="comments-container">
<span id="24489"></span>
<div id="comment-24489" class="comment">
<div id="post-24489-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for the quick response. We have a home-grown WMS server, which serves up base imagery. What we are missing is map-like overlay with geonames, roadways, etc. I was hoping we could adapt OSM data for this purpose.</p>
</div>
<div id="comment-24489-info" class="comment-info">
<span class="comment-age">(23 Jul '13, 15:34)</span> <span class="comment-user userinfo">gjw01</span>
</div>
</div>
</div>
<div id="comment-tools-24455" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24455-form-container" class="comment-form-container">
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

