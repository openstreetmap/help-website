+++
type = "question"
title = "Overpass Turbo: How to filter for Construction Zone Signs, School Zone Signs, LED Speed Limit Signs, and Horizontal Traffic Lights??"
description = '''Hey everyone! I need help with using Overpass Turbo to get School Zone signs, Construction Zone Signs, LED speed limit signs, and horizontal traffic lights. I need the GPS coords in some areas of Canada to I can map it out on google earth.  Please help I don&#x27;t understand and I tried using Mapillary ...'''
date = "2021-10-04T16:20:00Z"
lastmod = "2021-10-07T10:39:00Z"
weight = 82025
keywords = [ "overpass", "mapillary", "overpass-turbo", "coordinates", "signs" ]
aliases = [ "/questions/82025" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass Turbo: How to filter for Construction Zone Signs, School Zone Signs, LED Speed Limit Signs, and Horizontal Traffic Lights??](/questions/82025/overpass-turbo-how-to-filter-for-construction-zone-signs-school-zone-signs-led-speed-limit-signs-and-horizontal-traffic-lights)

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
<span id="post-82025-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82025-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82025-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey everyone!</p>
<p>I need help with using Overpass Turbo to get School Zone signs, Construction Zone Signs, LED speed limit signs, and horizontal traffic lights. I need the GPS coords in some areas of Canada to I can map it out on google earth.</p>
<p>Please help I don't understand and I tried using Mapillary tool but they don't give you the GPS coordinates and the zoom is too small. I'm not a programmer so I have no idea how to access the API or whatever it is.</p>
<p>I've been trying to get this data for a week but I'm just so confused.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-mapillary" rel="tag" title="see questions tagged &#39;mapillary&#39;">mapillary</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-signs" rel="tag" title="see questions tagged &#39;signs&#39;">signs</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Oct '21, 16:20</strong></p>
<img src="https://secure.gravatar.com/avatar/c9107481b5a520b6b6314eea8d9eea7b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Brian218&#39;s gravatar image" />
<p><span>Brian218</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Brian218 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82025" class="comments-container">
<span id="82031"></span>
<div id="comment-82031" class="comment">
<div id="post-82031-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi Brian. OpenStreetMap and Mapillary are separate services. Each use information from the other but in general they hold different type of data. Construction zone signs, nature of speed limit signs and orientation of traffic lights are not usually mapped in OpenStreetMap, hence you won't find them with Overpass Turbo, either.</p>
<p>If Mapillary detects this kind of information in its pictures then you have to get the data from Mapillary itself. (I cannot check right now. The Mapillary page seems to have gone down with the rest of the Facebook servers). There is a quite active <a href="https://forum.mapillary.com/">Mapillary forum</a> where you might get more help on this matter.</p>
</div>
<div id="comment-82031-info" class="comment-info">
<span class="comment-age">(04 Oct '21, 21:06)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-82025" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82025-form-container" class="comment-form-container">
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

<span id="82052"></span>

<div id="answer-container-82052" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82052-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82052-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82052-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe this <a href="https://help.mapillary.com/hc/en-us/articles/4407521157138-Downloading-map-data-with-the-Mapillary-Web-App">Mapillary help article</a> helps. I just downloaded a speed limit sign with coordinates. But there is a restriction to the size of the area.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Oct '21, 10:39</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-82052" class="comments-container">
&#10;</div>
<div id="comment-tools-82052" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82052-form-container" class="comment-form-container">
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

