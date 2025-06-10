+++
type = "question"
title = "using routing based on past years"
description = '''Hi  I am trying to route some locations using Python code. However I want to use the routes if I was using the infrastructure available in 2010. How can I do this?  i.e. Either calling an old version of a map (say a 2012 extraction - and how can I call this in my code?) or by restricting new routes ...'''
date = "2022-01-05T11:33:00Z"
lastmod = "2022-01-05T11:54:00Z"
weight = 82955
keywords = [ "old_routes" ]
aliases = [ "/questions/82955" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [using routing based on past years](/questions/82955/using-routing-based-on-past-years)

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
<span id="post-82955-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82955-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82955-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I am trying to route some locations using Python code. However I want to use the routes if I was using the infrastructure available in 2010. How can I do this? i.e. Either calling an old version of a map (say a 2012 extraction - and how can I call this in my code?) or by restricting new routes (how to code that a specific route that is using was not there in 2012) ?</p>
<p>thanks!</p>
<pre><code>def get_route(pickup_lon, pickup_lat, dropoff_lon, dropoff_lat):
&#10;loc = &quot;{},{};{},{}&quot;.format(pickup_lon, pickup_lat, dropoff_lon, dropoff_lat)
url = &quot;https://router.project-osrm.org//route/v1/driving/&quot;
r = requests.get(url + loc) 
if r.status_code!= 200:
    return {}
&#10;res = r.json()   
routes = polyline.decode(res[&#39;routes&#39;][0][&#39;geometry&#39;])
start_point = [res[&#39;waypoints&#39;][0][&#39;location&#39;][1], res[&#39;waypoints&#39;][0][&#39;location&#39;][0]]
end_point = [res[&#39;waypoints&#39;][1][&#39;location&#39;][1], res[&#39;waypoints&#39;][1][&#39;location&#39;][0]]
distance = res[&#39;routes&#39;][0][&#39;distance&#39;]
out= pd.DataFrame(routes)
return out</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-old_routes" rel="tag" title="see questions tagged &#39;old_routes&#39;">old_routes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jan '22, 11:33</strong></p>
<img src="https://secure.gravatar.com/avatar/1b437dd173cdeec0e534f7a2d2a99d3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alejandra&#39;s gravatar image" />
<p><span>Alejandra</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alejandra has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82955" class="comments-container">
&#10;</div>
<div id="comment-tools-82955" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82955-form-container" class="comment-form-container">
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

<span id="82956"></span>

<div id="answer-container-82956" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82956-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82956-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-82956-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For this task, you cannot rely on a routing engine that someone else runs for you; you need to run the routing engine yourself. First grab the "history" file of the area you are interested in. Then, use the <code>osmium</code> utility to extract from this history file a snapshot for the day you want to compute the routing for. Then, set up a routing engine with this snapshot (<a href="https://github.com/Project-OSRM">https://github.com/Project-OSRM</a> for the OSRM you seem to be using). This might require substantial resources if running for a large area (possibly more than 128 GB of RAM to compute a world-wide graph). Then finally, you can run your code against your local routing server (i.e. replace router.project-osrm.org with localhost:5001 or so).</p>
<p>It is important to understand that if you extract a 2010 snapshot from OSM data, you will see what OSM knew about the world in 2010, not what the world was like in 2010. For some countries, the 2010 road network will be extremely patchy simply because OSM was not widely used in that country at the time.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jan '22, 11:54</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-82956" class="comments-container">
&#10;</div>
<div id="comment-tools-82956" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82956-form-container" class="comment-form-container">
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

