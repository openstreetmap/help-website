+++
type = "question"
title = "Tweaking routing algorithm"
description = '''I&#x27;&#x27;ve got the task to tune an existing routing algorithm t0 take the following points into account and display the route on a map.  Winding narrow country roads. Ease of route over journey time.  Roundabout avoidance.  Traffic light avoidance. Right-turn avoidance.  Using OSM data, where would I sta...'''
date = "2014-01-22T20:52:00Z"
lastmod = "2014-01-23T06:57:00Z"
weight = 30121
keywords = [ "routing", "algorithm" ]
aliases = [ "/questions/30121" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tweaking routing algorithm](/questions/30121/tweaking-routing-algorithm)

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
<span id="post-30121-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30121-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30121-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I''ve got the task to tune an existing routing algorithm t0 take the following points into account and display the route on a map.</p>
<ul>
<li>Winding narrow country roads.</li>
<li>Ease of route over journey time.</li>
<li>Roundabout avoidance.</li>
<li>Traffic light avoidance.</li>
<li>Right-turn avoidance.</li>
</ul>
<p>Using OSM data, where would I start?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-algorithm" rel="tag" title="see questions tagged &#39;algorithm&#39;">algorithm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jan '14, 20:52</strong></p>
<img src="https://secure.gravatar.com/avatar/98d8e52ef549b0b12d0bb84e17581ff1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mumf&#39;s gravatar image" />
<p><span>mumf</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mumf has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jan '14, 06:40</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span></p>
</div>
</div>
<div id="comments-container-30121" class="comments-container">
&#10;</div>
<div id="comment-tools-30121" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30121-form-container" class="comment-form-container">
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

<span id="30122"></span>

<div id="answer-container-30122" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30122-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-30122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Welcome to OSM and our OSQA support forum :)</p>
<p>As data and (most) tools are open, it's straight forward to realize this task:</p>
<ul>
<li><a href="https://wiki.openstreetmap.org/wiki/Routing">routing wikipage</a> will present you existing solutions and which OSM tags might be important</li>
<li>after checking which of your features are already realized, you pick a router that you want to modify</li>
<li>adapt the source of a router/navigation solution</li>
</ul>
<p>You might also check out the <a href="http://code.google.com/p/trafficmining/">Trafficmining framework</a> that is build to develop and benchmark routing algorithms on OSM. But I don't know if you get access to all OSM tags or just get the most usual ones ... You can lookup all relevant OSM tags at <a href="https://wiki.openstreetmap.org/wiki/Map_features">Map features list</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jan '14, 21:03</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-30122" class="comments-container">
<span id="30126"></span>
<div id="comment-30126" class="comment">
<div id="post-30126-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@iii</span> because the documentation for Traffic Mining framework is bad. I thought I would see if you have any answers:</p>
<p>I am getting this error:</p>
<p>Jan 22, 2014 10:10:04 PM de.lmu.ifi.dbs.trafficmining.LoadGraphListener propertyChange SEVERE: null java.util.concurrent.ExecutionException: java.lang.NumberFormatException: For input string: "2153445071"</p>
<p>when I try to load an .osm file from:</p>
<p><a href="http://download.geofabrik.de/europe/monaco.html">http://download.geofabrik.de/europe/monaco.html</a></p>
</div>
<div id="comment-30126-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 22:15)</span> <span class="comment-user userinfo">mumf</span>
</div>
</div>
<span id="30138"></span>
<div id="comment-30138" class="comment">
<div id="post-30138-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't have any experience with the framework. So I can just recommend to make use of the official support channels :(</p>
</div>
<div id="comment-30138-info" class="comment-info">
<span class="comment-age">(23 Jan '14, 06:37)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="30141"></span>
<div id="comment-30141" class="comment">
<div id="post-30141-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please stop creating dupe crossposting <a href="/questions/30121/tweaking-routing-algorithm">https://help.openstreetmap.org/questions/30121/tweaking-routing-algorithm</a> <a href="https://stackoverflow.com/questions/21207220/osm-editing-routing-algorithm/21208259">https://stackoverflow.com/questions/21207220/osm-editing-routing-algorithm/21208259</a></p>
</div>
<div id="comment-30141-info" class="comment-info">
<span class="comment-age">(23 Jan '14, 06:57)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
</div>
<div id="comment-tools-30122" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30122-form-container" class="comment-form-container">
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

