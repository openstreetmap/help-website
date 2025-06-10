+++
type = "question"
title = "Route with optimize waypoints"
description = '''I am working on a route planning application and I would like to used your REST API, but I need to know if your API allows you to enter a vehicle, start and end of the route,  waypoints of up to 80 in the request. The start and end of the route + waypoints will be in Lat Lon format. This planed rout...'''
date = "2020-05-15T21:13:00Z"
lastmod = "2020-05-18T12:39:00Z"
weight = 74843
keywords = [ "route", "optimize", "waypoints" ]
aliases = [ "/questions/74843" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Route with optimize waypoints](/questions/74843/route-with-optimize-waypoints)

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
<span id="post-74843-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74843-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74843-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am working on a route planning application and I would like to used your REST API, but I need to know if your API allows you to enter a vehicle, start and end of the route, waypoints of up to 80 in the request. The start and end of the route + waypoints will be in Lat Lon format. This planed route will be use for country The Czech Republic.</p>
<p>The result of the response should include: a) Total distance traveled b) Waypoints re-order so as to minimize travel costs.</p>
<p>I don't need to display a map and the number of requests does not exceed 500 per month.</p>
<p>Thank you very much for your answer</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-optimize" rel="tag" title="see questions tagged &#39;optimize&#39;">optimize</span> <span class="post-tag tag-link-waypoints" rel="tag" title="see questions tagged &#39;waypoints&#39;">waypoints</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 May '20, 21:13</strong></p>
<img src="https://secure.gravatar.com/avatar/26c38ee34e1a1fa51d9a92759df4105d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Milan&#39;s gravatar image" />
<p><span>Milan</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Milan has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74843" class="comments-container">
&#10;</div>
<div id="comment-tools-74843" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74843-form-container" class="comment-form-container">
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

<span id="74850"></span>

<div id="answer-container-74850" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74850-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74850-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-74850-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no "your API" in this cases, the routing engines demoed on openstreetmap.org are kindly provided by third parties.</p>
<p>Direct API access and available features needs to be discussed with the operators directly (AFAIK all them allow via-points and 500 queries sounds low). Multiple of the routing engines are open source software so you in principle could run one yourself, but with 500 queries/month that is unlikely to make sense.</p>
<p>See <a href="https://wiki.openstreetmap.org/wiki/List_of_OSM-based_services#Routing">https://wiki.openstreetmap.org/wiki/List_of_OSM-based_services#Routing</a> for more information.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 May '20, 09:02</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-74850" class="comments-container">
<span id="74851"></span>
<div id="comment-74851" class="comment">
<div id="post-74851-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much for link, may I'll find some sollution.</p>
</div>
<div id="comment-74851-info" class="comment-info">
<span class="comment-age">(16 May '20, 11:27)</span> <span class="comment-user userinfo">Milan</span>
</div>
</div>
<span id="74852"></span>
<div id="comment-74852" class="comment">
<div id="post-74852-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Note that the Fossgis OSRM may work for you, OSM API documentation <a href="http://project-osrm.org/docs/v5.22.0/api/#general-options">http://project-osrm.org/docs/v5.22.0/api/#general-options</a></p>
</div>
<div id="comment-74852-info" class="comment-info">
<span class="comment-age">(16 May '20, 11:45)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="74853"></span>
<div id="comment-74853" class="comment">
<div id="post-74853-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>To SimonPoole: Thank you for your tip i have already sent e-mail to project-osrm.org with my requests.</p>
</div>
<div id="comment-74853-info" class="comment-info">
<span class="comment-age">(16 May '20, 12:19)</span> <span class="comment-user userinfo">Milan</span>
</div>
</div>
<span id="74854"></span>
<div id="comment-74854" class="comment">
<div id="post-74854-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>AFAIK the OSRM project no longer has a working public instance. so you really need to talk to FOSSGIS that operates <a href="http://routing.openstreetmap.de/">http://routing.openstreetmap.de/</a></p>
</div>
<div id="comment-74854-info" class="comment-info">
<span class="comment-age">(16 May '20, 12:36)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-74850" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74850-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74868"></span>

<div id="answer-container-74868" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74868-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74868-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74868-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Routing engines will only gives you the route of the locations in the given order. To obtain the minimized trip, your are actually looking for tools solving Vehicle Routing Problems : <a href="https://en.wikipedia.org/wiki/Vehicle_routing_problem">https://en.wikipedia.org/wiki/Vehicle_routing_problem</a></p>
<p>Various open source projects are available at this purpose and maintained by private companies, which provides APIs for theses projects.</p>
<ul>
<li><strong>Jsprit</strong> <a href="https://github.com/graphhopper/jsprit">https://github.com/graphhopper/jsprit</a> by Graphhoppper.</li>
<li><strong>Optimizer-API</strong> <a href="https://github.com/Mapotempo/optimizer-api">https://github.com/Mapotempo/optimizer-api</a> by Mapotempo</li>
<li><strong>VROOM</strong> <a href="https://github.com/VROOM-Project/">https://github.com/VROOM-Project/</a> by Verso-optim</li>
</ul>
<p><em>Note: my opinion may be oriented as I work at Mapotempo.</em></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 May '20, 09:32</strong></p>
<img src="https://secure.gravatar.com/avatar/a8c2a1fb48d0e9d314d90f6bedd7b24d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sheeplieder&#39;s gravatar image" />
<p><span>Sheeplieder</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sheeplieder has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74868" class="comments-container">
<span id="74870"></span>
<div id="comment-74870" class="comment">
<div id="post-74870-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Worth noting that OSRM does have a simple TSP solver built in, though it's much more rudimentary than the above.</p>
</div>
<div id="comment-74870-info" class="comment-info">
<span class="comment-age">(18 May '20, 12:39)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-74868" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74868-form-container" class="comment-form-container">
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

