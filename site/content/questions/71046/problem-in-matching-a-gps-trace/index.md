+++
type = "question"
title = "Problem in matching a GPS trace!"
description = '''I have a GPS trace of a route used by a vehicle. I am trying to find out whether this path is the same as estimated/propose by OSM. But GPS trace is missing some points, so it forms a straight line between two points(line goes over through some places on map instead of following a road). My solution...'''
date = "2019-10-05T14:10:00Z"
lastmod = "2019-10-08T20:36:00Z"
weight = 71046
keywords = [ "gps-traces", "osrm", "polyline", "osm", "gps" ]
aliases = [ "/questions/71046" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Problem in matching a GPS trace!](/questions/71046/problem-in-matching-a-gps-trace)

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
<span id="post-71046-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71046-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71046-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a GPS trace of a route used by a vehicle. I am trying to find out whether this path is the same as estimated/propose by OSM. But GPS trace is missing some points, so it forms a straight line between two points(line goes over through some places on map instead of following a road). My solution to this was using a Match service provided by OSRM. It works fine but sometimes it generates a loop over some routes (keeps on circling the same route near a roundabout), when it should have gone straight. How I can solve this issue.</p>
<p><img src="/upfiles/Screenshot_from_2019-10-09_13-13-24.png" alt="alt text" /></p>
<p>I used following request to local server</p>
<p><a href="http://localhost:5000/match/v1/car/polyline(%7Bpoly_line%7D)?overview=full&amp;steps=true&amp;geometries=polyline"><code>http://localhost:5000/match/v1/car/polyline({poly_line})?overview=full&amp;steps=true&amp;geometries=polyline</code></a></p>
<p>and extracted the generated poly-line and then used that to plot this map using folium</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gps-traces" rel="tag" title="see questions tagged &#39;gps-traces&#39;">gps-traces</span> <span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-polyline" rel="tag" title="see questions tagged &#39;polyline&#39;">polyline</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Oct '19, 14:10</strong></p>
<img src="https://secure.gravatar.com/avatar/45c1cced3ea049e72e23496b4715be45?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vsaadnet&#39;s gravatar image" />
<p><span>vsaadnet</span><br />
<span class="score" title="45 reputation points">45</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vsaadnet has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Oct '19, 09:19</strong> </span></p>
</div>
</div>
<div id="comments-container-71046" class="comments-container">
<span id="71050"></span>
<div id="comment-71050" class="comment">
<div id="post-71050-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For Info. GPX points are recorded at intervals, which you see if you open one with a text editor you will see the positions and their times. If one point is just before a bend in road and the next one or two seconds later is around this bend the line will be straight between the points. Some Sat Navs lock to road so that the display does not look incorrect.</p>
</div>
<div id="comment-71050-info" class="comment-info">
<span class="comment-age">(05 Oct '19, 21:39)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="71053"></span>
<div id="comment-71053" class="comment">
<div id="post-71053-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/644/andy-mackey"></a><a href="https://help.openstreetmap.org/users/644/andy-mackey">@andy mackey</a>, this is not the problem here, missing points are not just bends apart there are literally a mile apart. Concerned dept. told us that sometimes GPS is not functioning at various locations, so, we have to use match o snap to road api's to visualize the path taken.</p>
</div>
<div id="comment-71053-info" class="comment-info">
<span class="comment-age">(06 Oct '19, 12:06)</span> <span class="comment-user userinfo">vsaadnet</span>
</div>
</div>
<span id="71057"></span>
<div id="comment-71057" class="comment">
<div id="post-71057-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe the GPS tracking device is not set to record at short time intervals. The GPS may not be good enough to do the job required or it's signal is degraded by high buildings or even degraded by radio interference, either by accident or design. such as this article <a href="https://www.theguardian.com/technology/2013/feb/13/gps-jammers-uk-roads-risks">https://www.theguardian.com/technology/2013/feb/13/gps-jammers-uk-roads-risks</a></p>
</div>
<div id="comment-71057-info" class="comment-info">
<span class="comment-age">(07 Oct '19, 07:05)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="71075"></span>
<div id="comment-71075" class="comment">
<div id="post-71075-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/644/andy-mackey">@andy mackey</a>, problem is not that gps device is missing its about Matching a GPS trace properly using OSM/OSRM. API calls are returning duplicate data.</p>
</div>
<div id="comment-71075-info" class="comment-info">
<span class="comment-age">(08 Oct '19, 16:19)</span> <span class="comment-user userinfo">vsaadnet</span>
</div>
</div>
<span id="71078"></span>
<div id="comment-71078" class="comment">
<div id="post-71078-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could you edit your question and upload a jpeg showing the problem?</p>
</div>
<div id="comment-71078-info" class="comment-info">
<span class="comment-age">(08 Oct '19, 20:36)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-71046" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71046-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

