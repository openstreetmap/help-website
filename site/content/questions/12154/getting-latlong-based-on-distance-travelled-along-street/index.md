+++
type = "question"
title = "Getting lat/long based on distance travelled along street"
description = '''Hi there! I want to draw a lot of cars moving around on a map. I have the osm data parsed and put into a graph using GraphServer.  What I&#x27;d like is a function to do is this (in C style pseudocode):  Coordinates getCurrentPoint(street,distance_traveled_along_street){  return current_position_in_lat_l...'''
date = "2012-04-19T01:50:00Z"
lastmod = "2012-04-20T18:15:00Z"
weight = 12154
keywords = [ "visualization", "osm", "graphserver" ]
aliases = [ "/questions/12154" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Getting lat/long based on distance travelled along street](/questions/12154/getting-latlong-based-on-distance-travelled-along-street)

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
<span id="post-12154-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12154-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-12154-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there!</p>
<p>I want to draw a lot of cars moving around on a map. I have the osm data parsed and put into a graph using GraphServer.</p>
<p>What I'd like is a function to do is this (in C style pseudocode):</p>
<pre><code>Coordinates getCurrentPoint(street,distance_traveled_along_street){
     return current_position_in_lat_long;
}</code></pre>
<p>So basically, I've travelled so many meters along this street, now where am I in lat/long? Obviously this is isn't hard when the map is a grid, but it does seem VERY tricky to me for more complicated road maps.</p>
<p>Any ideas of where to begin or other projects that I can leverage?<br />
</p>
<p>EDIT:</p>
<p>A bit more explanation...GraphServer (as mentioned in the comments), just gives me nodes and edges. But the nodes map directly back to the osm nodes and the edges map directly to "ways".</p>
<p>So maybe my question is better phrased as...I'm travelling along a way at velocity v, in s seconds, where am I?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-visualization" rel="tag" title="see questions tagged &#39;visualization&#39;">visualization</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-graphserver" rel="tag" title="see questions tagged &#39;graphserver&#39;">graphserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Apr '12, 01:50</strong></p>
<img src="https://secure.gravatar.com/avatar/107f72837cb2e080ad7123f8a734a30b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rex&#39;s gravatar image" />
<p><span>Rex</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rex has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Apr '12, 16:58</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span></p>
</div>
</div>
<div id="comments-container-12154" class="comments-container">
<span id="12176"></span>
<div id="comment-12176" class="comment">
<div id="post-12176-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't know GraphServer, but from a quick googling, it seems GraphServer only deals in nodes and edges, not in real geographical data - so the graph simply does not contain the information you need. Maybe you could explain how you use GraphServer, what information you put into it, and what it does for you?</p>
</div>
<div id="comment-12176-info" class="comment-info">
<span class="comment-age">(19 Apr '12, 15:35)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
<span id="12177"></span>
<div id="comment-12177" class="comment">
<div id="post-12177-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I edited the question :)</p>
</div>
<div id="comment-12177-info" class="comment-info">
<span class="comment-age">(19 Apr '12, 16:46)</span> <span class="comment-user userinfo">Rex</span>
</div>
</div>
</div>
<div id="comment-tools-12154" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12154-form-container" class="comment-form-container">
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

<span id="12181"></span>

<div id="answer-container-12181" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12181-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12181-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12181-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think this boils down to a (relatively!) straightforward navigational problem.</p>
<p>You're at point A with Lat and Long known. and you travel on a course of, say 315T (degrees true) for 10 seconds at a speed of 40KPH, then 320T for 5 seconds at 35KPH etc. etc. (roads are not always straight). So it's either a) a matter of calculating each intermediate position from the previous known position and the vector from there to this position, or b) continuing to "plot" each different course change from the original known position until you want another Lat/Long when you'll do your spherical trigonometry calculation to determine the new position.</p>
<p>If you are using the vehicles' odometers as one of your inputs you'll have take into account the gradient of the road, i.e. the gain/loss in height between each intermediate point as, for example, you will not end up in the same Lat/Long if you head due east (090T) for 10 KM on the level as you would be doing the same up or down a gradient of, say 1 in 5.</p>
<p>When doing your calcs you'll need to consider what level of accuracy you want. And also "mapping" to and from the projection of the OSM map data to whatever is needed for the trig. calcs. The earth is not a true sphere (oblate spheroid) but I doubt this will really affect your calculations at the granularity you indicate you'll be working at.</p>
<p>I suggest taking a look at some navigational works, particularly marine navigation - although they don't have the gradient problem to worry about. Possibly also some stuff on GPS calculations may help.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Apr '12, 17:49</strong></p>
<img src="https://secure.gravatar.com/avatar/956d6fda0f51e8001832540fa2c716a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vagabond&#39;s gravatar image" />
<p><span>vagabond</span><br />
<span class="score" title="195 reputation points">195</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vagabond has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12181" class="comments-container">
&#10;</div>
<div id="comment-tools-12181" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12181-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="12208"></span>

<div id="answer-container-12208" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12208-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12208-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12208-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Go through each segment of the street, calculating distance of the line between each pair of nodes <a href="http://www.movable-type.co.uk/scripts/latlong.html">(see useful formulas)</a>. Consider storing this data for the duration of your program.</p>
<p>Go through each segment of the street, subtracting the length of each segment of street from your total, until the remaining distance is less than the length of a street segment, which means you've found the segment of street you're currently in.</p>
<p>Calculate your position within that segment of street using the remaining distance, by linearly interpolating between its start and end nodes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Apr '12, 18:15</strong></p>
<img src="https://secure.gravatar.com/avatar/3e44debd67415e7aa7759c83b829be6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OJW&#39;s gravatar image" />
<p><span>OJW</span><br />
<span class="score" title="151 reputation points">151</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OJW has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12208" class="comments-container">
&#10;</div>
<div id="comment-tools-12208" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12208-form-container" class="comment-form-container">
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

