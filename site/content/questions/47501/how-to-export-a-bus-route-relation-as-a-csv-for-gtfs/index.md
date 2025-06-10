+++
type = "question"
title = "How to export a bus route relation as a CSV for GTFS?"
description = '''I&#x27;m attempting to use OpenStreetMap to maintain the canonical geography for the bus routes for our transit system, and would like to export from OSM into a CSV for creating the shapes.txt file for the GTFS feed for the system. I&#x27;ve created relations for each route:  http://www.openstreetmap.org/rela...'''
date = "2016-01-13T20:04:00Z"
lastmod = "2016-01-14T22:00:00Z"
weight = 47501
keywords = [ "gtfs", "export", "route", "relation", "gpx" ]
aliases = [ "/questions/47501" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to export a bus route relation as a CSV for GTFS?](/questions/47501/how-to-export-a-bus-route-relation-as-a-csv-for-gtfs)

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
<span id="post-47501-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47501-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47501-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm attempting to use OpenStreetMap to maintain the canonical geography for the bus routes for our transit system, and would like to export from OSM into a CSV for creating <a href="https://developers.google.com/transit/gtfs/reference#shapes_fields">the shapes.txt file</a> for the GTFS feed for the system.</p>
<p>I've created relations for each route:</p>
<ul>
<li><a href="http://www.openstreetmap.org/relation/5838068">http://www.openstreetmap.org/relation/5838068</a></li>
<li><a href="http://www.openstreetmap.org/relation/3439454">http://www.openstreetmap.org/relation/3439454</a></li>
<li><a href="http://www.openstreetmap.org/relation/3425884">http://www.openstreetmap.org/relation/3425884</a></li>
<li><a href="http://www.openstreetmap.org/relation/5838881">http://www.openstreetmap.org/relation/5838881</a></li>
<li><a href="http://www.openstreetmap.org/relation/5838217">http://www.openstreetmap.org/relation/5838217</a></li>
</ul>
<p>What I need to do next is to find a way to export the points along these routes as a simple series of lat/lon points, in the right sequence. Each way in each route is tagged with "forward" or "backward" so, in theory, all the data needed to do this is present in OSM.</p>
<p>I've experimented with using <a href="http://blog.velocarte66.fr/?q=de/node/170">rel2gpx.pl</a> for this, converting the relation for each route into a GPX. I then extract the track points from the GPX to make the CSV.</p>
<p>This works well for simple routes with a single track, <a href="https://gist.github.com/reinvented/0c105dc8fdc65a3b07a1">as in this example for relation ID 3425884</a>.</p>
<p>But for more complex routes, where there are ways that appear more than once in the same route (for example, driving up a road, turning around, and driving back the same road), I'm running into problems.</p>
<p>For example, <a href="https://gist.github.com/reinvented/386296af30df4b2cd80d">in this GPX created from relation 5838068</a>, the track segments appear out of route order, and so the resulting CSV file (which I extract from the GPX simply by extracting the lat/lon from each trkpt, in the natural order of the file) does not contain the points in route order, and when previewed in the <a href="https://github.com/google/transitfeed/wiki/ScheduleViewer">schedule_viewer.py</a> it looks like this:</p>
<p><img src="http://media.ruk.ca/images//community_bus_problems-20160113-155442.jpg" alt="schedule_viewer.py rendering the route" /></p>
<p>If you compare that rendering to the <a href="http://ra.osmsurround.org/analyzeMap?relationId=5838068">rendering of the route in the OSM Relation Analyzer</a> you will quickly see where things are going wrong.</p>
<p>I'm looking for help in either solving this issue improving the approach I've taken, or in identifying a different approach.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gtfs" rel="tag" title="see questions tagged &#39;gtfs&#39;">gtfs</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jan '16, 20:04</strong></p>
<img src="https://secure.gravatar.com/avatar/e2ed169f43b7aae4f46de5fa9ef837e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ruk&#39;s gravatar image" />
<p><span>ruk</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ruk has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-47501" class="comments-container">
&#10;</div>
<div id="comment-tools-47501" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47501-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="47507"></span>

<div id="answer-container-47507" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47507-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47507-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-47507-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>rel2gpx has been designed for bicycle and hiking routes and it generally gives good results for linear routes without loops. In cases where the ways in the relation can not be assembled together to form a single line, it results in a collection of GPX tracks that have to be postprocessed manually if one wants to have a GPX track, for example to navigate along with a GPS device.</p>
<p>The different rendering by the schedule_viewer and the OSM relation analyzer is duto the fact, that rel2gpx results in six segments and apparently schedule_viewer interconnects the segments by straight lines to have a single line. If you leave out these interconnections, the rel2gpx GPX file is rendered the same way as does the OSM relation analyzer.</p>
<p>I am not familiar with public transport relations but I think that rel2gpx is not the appropriate tool for your purpose. There a are probably specific tags for this kind of relation which allow to create a list of points on the line in the correct order.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jan '16, 07:16</strong></p>
<img src="https://secure.gravatar.com/avatar/71c1ae65b2c4cb9d6603635965a86fe1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rainerU&#39;s gravatar image" />
<p><span>rainerU</span><br />
<span class="score" title="106 reputation points">106</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rainerU has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47507" class="comments-container">
&#10;</div>
<div id="comment-tools-47507" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47507-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47514"></span>

<div id="answer-container-47514" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47514-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is the very old <a href="http://svn.openstreetmap.org/applications/utils/export/OSM2GTFS/">OSM2GTFS</a>, but keep in mind what will be done with the GTFS path data. If it ends up in Google, that would probably violate the OpenStreetMap license. OSM2GTFS is very basic, and consider that it will likely require a software developer to produce good results.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jan '16, 11:34</strong></p>
<img src="https://secure.gravatar.com/avatar/1dd5f61a81b99dd54ec6f33d96aa38b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20N&#39;s gravatar image" />
<p><span>Mike N</span><br />
<span class="score" title="2926 reputation points"><span>2.9k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike N has 16 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-47514" class="comments-container">
&#10;</div>
<div id="comment-tools-47514" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47514-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47519"></span>

<div id="answer-container-47519" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47519-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47519-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47519-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I ended up hacking together a solution in PHP (<a href="https://gist.github.com/reinvented/b994ef0846d50eac8758">sample code here</a>) that uses the OSM API to grab the full XML of each relation, and then assembles the points, traversing each way forward or backward per the role assignment in the relation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jan '16, 22:00</strong></p>
<img src="https://secure.gravatar.com/avatar/e2ed169f43b7aae4f46de5fa9ef837e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ruk&#39;s gravatar image" />
<p><span>ruk</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ruk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47519" class="comments-container">
&#10;</div>
<div id="comment-tools-47519" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47519-form-container" class="comment-form-container">
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

