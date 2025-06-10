+++
type = "question"
title = "How many request per second OSRM/Backend docker can handle ?"
description = '''Is there a limit, that following API can handle request per second, if I hosted in our own server? http://127.0.0.1:5000/route/v1/driving/13.388860,52.517037;13.385983,52.496891?steps=true I did exactly what has mentioned in the https://hub.docker.com/r/osrm/osrm-backend/ link to run the OSRM docker...'''
date = "2017-11-10T05:23:00Z"
lastmod = "2017-11-13T14:24:00Z"
weight = 60527
keywords = [ "load", "nginx", "docker", "route", "driving" ]
aliases = [ "/questions/60527" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How many request per second OSRM/Backend docker can handle ?](/questions/60527/how-many-request-per-second-osrmbackend-docker-can-handle)

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
<span id="post-60527-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60527-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60527-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a limit, that following API can handle request per second, if I hosted in our own server?</p>
<p><a href="http://127.0.0.1:5000/route/v1/driving/13.388860,52.517037;13.385983,52.496891?steps=true">http://127.0.0.1:5000/route/v1/driving/13.388860,52.517037;13.385983,52.496891?steps=true</a></p>
<p>I did exactly what has mentioned in the <a href="https://hub.docker.com/r/osrm/osrm-backend/">https://hub.docker.com/r/osrm/osrm-backend/</a> link to run the OSRM docker instruction. (Note I'm not using front-end)</p>
<p>Everything seems working fine, even If I execute the following API (note here the source limit is 3) <a href="http://127.0.0.1:5000/table/v1/driving/79.865184,6.856469;79.867051,6.858589;79.862052,6.860068;79.863039,6.862401?sources=1;2;3&amp;destinations=0">http://127.0.0.1:5000/table/v1/driving/79.865184,6.856469;79.867051,6.858589;79.862052,6.860068;79.863039,6.862401?sources=1;2;3&amp;destinations=0</a></p>
<p>I'm getting response in 44ms.</p>
<p>However, if I increase the sources information in above API like for 50 and send 1000 request per second, I'm getting 7 to 8 second response time and the CPU usage goes for 60-70 usage.</p>
<p>Here is my server and OSRM file size info: map.osrm file size: 1.6GB 16 Core CPU 24GB Ram ulimit -n 1024</p>
<p>I tried Nginx load balancing also as follows briefly:</p>
<p>docker run -t -i -p 5000:5000 -v $(pwd):/data osrm/osrm-backend osrm-routed --algorithm mld /data/map.osrm docker run -t -i -p 5001:5000 -v $(pwd):/data osrm/osrm-backend osrm-routed --algorithm mld /data/map.osrm</p>
<p>and accessed the API as:</p>
<p><a href="http://127.0.0.1/table/v1/driving/79.865184,6.856469;79.867051,6.858589;79.862052,6.860068;79.863039,6.862401?sources=1;2;3&amp;destinations=0">http://127.0.0.1/table/v1/driving/79.865184,6.856469;79.867051,6.858589;79.862052,6.860068;79.863039,6.862401?sources=1;2;3&amp;destinations=0</a></p>
<p>nginx.conf brief setup as follows:</p>
<p><strong>-----------------------------------------------------</strong> `worker_processes auto;</p>
<p>events { worker_connections 2048; multi_accept on; }</p>
<p>upstream myapp1 { server 127.0.0.1:5000 weight=1; server 127.0.0.1:5001 weight=2;</p>
<p>}</p>
<p>server { listen 192.168.180.93:80;</p>
<pre><code>    location / {
            proxy_pass http://myapp1;
    }</code></pre>
<p>}` <strong>-----------------------------------------------------</strong></p>
<p>Now my question is how can I make/keep it the response time very low (below 100ms) even if I increase it to 50 or more?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-load" rel="tag" title="see questions tagged &#39;load&#39;">load</span> <span class="post-tag tag-link-nginx" rel="tag" title="see questions tagged &#39;nginx&#39;">nginx</span> <span class="post-tag tag-link-docker" rel="tag" title="see questions tagged &#39;docker&#39;">docker</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-driving" rel="tag" title="see questions tagged &#39;driving&#39;">driving</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Nov '17, 05:23</strong></p>
<img src="https://secure.gravatar.com/avatar/66d0b06bb7986a6c350dbb8787625e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fazlul-RM&#39;s gravatar image" />
<p><span>Fazlul-RM</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fazlul-RM has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Nov '17, 05:25</strong> </span></p>
</div>
</div>
<div id="comments-container-60527" class="comments-container">
&#10;</div>
<div id="comment-tools-60527" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60527-form-container" class="comment-form-container">
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

<span id="60528"></span>

<div id="answer-container-60528" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60528-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60528-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-60528-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Fazlul-RM has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think the 15ms per route that you measured in your first example is realistic. If you want to compute 50 routes that would then take 750ms of CPU time. Asking this in a single matrix request means it will be run on one CPU core alone so it will take 750ms wall clock time. If you split the request in 5 smaller requests with 10 sources each, and if you have 5 CPU cores available, it should be possible to bring down the response time to below 100ms.</p>
<p>There are some economies of scale with the matrix request of course, so you have to find the "sweet spot" - more routes per request means more latency because you have to wait for one core to complete them all, but the total CPU time spent per route will be smaller.</p>
<p>If you want to compute 50k routes per second (you said you were trying 1000 requests per second with 50 sources each), that will probably take somewhere around 500 seconds of CPU time, i.e. you need 500 CPU cores to do that in one second of wall clock time.</p>
<p>Note that you will be able to squeeze a little more performance from the server if you switch to CH instead of MLD. Maybe then you only need 250 cores.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Nov '17, 06:48</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Nov '17, 06:50</strong> </span></p>
</div>
</div>
<div id="comments-container-60528" class="comments-container">
<span id="60531"></span>
<div id="comment-60531" class="comment">
<div id="post-60531-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi <a href="https://help.openstreetmap.org/users/104/frederik-ramm">@Frederik</a>, Thanks for your quick reply can you tell me what's the CH and MLD? sorry if it's sill qq.</p>
</div>
<div id="comment-60531-info" class="comment-info">
<span class="comment-age">(10 Nov '17, 08:53)</span> <span class="comment-user userinfo">Fazlul-RM</span>
</div>
</div>
<span id="60534"></span>
<div id="comment-60534" class="comment">
<div id="post-60534-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Contraction Hierarchies (CH) and Multi-Level Dijkstra (MLD) are different techniques for preprocessing the routing data. The <a href="https://github.com/Project-OSRM/osrm-backend/wiki/Running-OSRM#quickstart">Quickstart</a> explains how to choose between those two.</p>
</div>
<div id="comment-60534-info" class="comment-info">
<span class="comment-age">(10 Nov '17, 12:23)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="60599"></span>
<div id="comment-60599" class="comment">
<div id="post-60599-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi <a href="https://help.openstreetmap.org/users/2897/fredrikr">@Fredrik</a>, Sorry for delay, is it possible to add a cluster for this?</p>
</div>
<div id="comment-60599-info" class="comment-info">
<span class="comment-age">(13 Nov '17, 14:24)</span> <span class="comment-user userinfo">Fazlul-RM</span>
</div>
</div>
</div>
<div id="comment-tools-60528" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60528-form-container" class="comment-form-container">
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

