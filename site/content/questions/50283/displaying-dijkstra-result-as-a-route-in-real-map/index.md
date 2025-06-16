+++
type = "question"
title = "displaying Dijkstra result as a route in real map"
description = '''So I got the result of Dijkstra as sequence of coordinates lat_1,lon_1 lat_2,lon_2 .... .... lat_n,lon_n  where lat_1,lon_1 is the start point and lat_n,lon_n is the end point of the vehicle route. I need to display this path on real map. After adding node_id and description, I used GPSVisluazer web...'''
date = "2016-06-17T12:50:00Z"
lastmod = "2016-06-17T17:10:00Z"
weight = 50283
keywords = [ "dijkstra", "osm", "display" ]
aliases = [ "/questions/50283" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [displaying Dijkstra result as a route in real map](/questions/50283/displaying-dijkstra-result-as-a-route-in-real-map)

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
<span id="post-50283-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50283-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50283-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>So I got the result of Dijkstra as sequence of coordinates</p>
<pre><code>lat_1,lon_1
lat_2,lon_2
....
....
lat_n,lon_n</code></pre>
<p>where lat_1,lon_1 is the start point and lat_n,lon_n is the end point of the vehicle route. I need to display this path on real map. After adding node_id and description, I used GPSVisluazer website to create GPX file. I opened it in jpeg and Google Map and all show just set of points or markers with no connected lines between them. Now my question is: how to display the result of Dijkstra on OSM or at least having it as image? I checked rendering and routing sections in openstreetmap.org but there is nothing obvious.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-dijkstra" rel="tag" title="see questions tagged &#39;dijkstra&#39;">dijkstra</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jun '16, 12:50</strong></p>
<img src="https://secure.gravatar.com/avatar/1d1ed8c153e7a5ad729b406614e525f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xline&#39;s gravatar image" />
<p><span>xline</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xline has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50283" class="comments-container">
&#10;</div>
<div id="comment-tools-50283" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50283-form-container" class="comment-form-container">
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

<span id="50288"></span>

<div id="answer-container-50288" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50288-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50288-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-50288-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you have a gpx with waypoints and just want a straight line joining the points, you could use a text editor and replace the 'wpt' tags with 'trk' tags and then the points will be joined by a line when viewed in gpsvisualizer. I haven't tried this but it should be easy enough if you open an example of a gpx track to use as an example. I suspect you instead require a road route between the points, and if so, you can upload the gpx file of the waypoints to a site like www.gpsies.com and draw a route to each point.<br />
Example of correct tags here <a href="https://wiki.openstreetmap.org/wiki/GPX">https://wiki.openstreetmap.org/wiki/GPX</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jun '16, 17:10</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jun '16, 17:46</strong> </span></p>
</div>
</div>
<div id="comments-container-50288" class="comments-container">
&#10;</div>
<div id="comment-tools-50288" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50288-form-container" class="comment-form-container">
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

