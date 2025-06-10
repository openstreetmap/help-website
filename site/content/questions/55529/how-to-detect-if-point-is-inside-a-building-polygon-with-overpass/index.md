+++
type = "question"
title = "How to detect if point is inside a building polygon with overpass ?"
description = '''I am trying to figure out how to detect if lat/lng pair is inside a building polygon. So far I have something like this: http://overpass-turbo.eu/s/ocv This code gets me the nearest but it also gets me the closest buildings, which I don&#x27;t want - to avoid that I have made the around parameter as smal...'''
date = "2017-04-07T22:38:00Z"
lastmod = "2020-04-26T13:07:00Z"
weight = 55529
keywords = [ "building", "overpass" ]
aliases = [ "/questions/55529" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to detect if point is inside a building polygon with overpass ?](/questions/55529/how-to-detect-if-point-is-inside-a-building-polygon-with-overpass)

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
<span id="post-55529-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55529-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-55529-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to figure out how to detect if lat/lng pair is inside a building polygon. So far I have something like this: <a href="http://overpass-turbo.eu/s/ocv">http://overpass-turbo.eu/s/ocv</a></p>
<p>This code gets me the nearest but it also gets me the closest buildings, which I don't want - to avoid that I have made the around parameter as small as possible. Is there a better solution ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Apr '17, 22:38</strong></p>
<img src="https://secure.gravatar.com/avatar/a2784e6d6311921579300ae1d0ca11f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krizzz&#39;s gravatar image" />
<p><span>krizzz</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krizzz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55529" class="comments-container">
<span id="74373"></span>
<div id="comment-74373" class="comment">
<div id="post-74373-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>And how to do it efficiently for a lot of points? <a href="https://help.openstreetmap.org/questions/74372/how-to-check-efficiently-if-thousands-of-points-are-located-inside-a-building-polygon-using-overpass">https://help.openstreetmap.org/questions/74372/how-to-check-efficiently-if-thousands-of-points-are-located-inside-a-building-polygon-using-overpass</a></p>
</div>
<div id="comment-74373-info" class="comment-info">
<span class="comment-age">(26 Apr '20, 13:07)</span> <span class="comment-user userinfo">Vucod</span>
</div>
</div>
</div>
<div id="comment-tools-55529" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55529-form-container" class="comment-form-container">
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

<span id="57128"></span>

<div id="answer-container-57128" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57128-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57128-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57128-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is a solution using Python and gis_geometrics [1]. Then create your Python file in the same directory as gis_geometrics.py:</p>
<pre><code>from gis_geometrics import OSM_Polygon, Overpass</code></pre>
<p>First you need to get your building polygon in gis_geometrics. There are several methods for this: Either you use an Overpass answer. Execute the Overpass query in Python using overpy. Then create a buildings dict with Overpass.getBuildingNodes() and pass each element of its items to the constructor of OSM_Polygon.</p>
<p>Or you prefer to get the building using it's way id (e.g. WAY_ID=265258282):</p>
<pre><code>import overpy
api = overpy.Overpass()
building = Overpass.getPolygonByWayId(api, WAY_ID)</code></pre>
<p>See also alternative methods to find a building (Overpass.getBuildingByRelationId, Overpass.getBuildingsByBB, OSM_Polygon.getPolygonByCoords).</p>
<p>Then you can do awesome operations on the building:</p>
<pre><code>if building.isInPolygon(LAT,LON): print(&quot;%f,%f is inside the building.&quot;%(LAT,LON))</code></pre>
<p>[1] <a href="https://github.com/timojuez/home/blob/master/mylib/gis_geometrics.py">https://github.com/timojuez/home/blob/master/mylib/gis_geometrics.py</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jul '17, 11:02</strong></p>
<img src="https://secure.gravatar.com/avatar/784ae08b746dc5cce3dd9ac99959caf5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="timojuez&#39;s gravatar image" />
<p><span>timojuez</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="timojuez has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jul '17, 11:05</strong> </span></p>
</div>
</div>
<div id="comments-container-57128" class="comments-container">
&#10;</div>
<div id="comment-tools-57128" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57128-form-container" class="comment-form-container">
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

