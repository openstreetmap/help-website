+++
type = "question"
title = "Why are area queries in my own Overpass server returning different results from the official server?"
description = '''Here&#x27;s my query to collect all of the States within the US: [out:json]; area[&#x27;admin_level&#x27;=&#x27;2&#x27;][&#x27;name&#x27;=&#x27;United States&#x27;]; (relation[&#x27;admin_level&#x27;=&#x27;4&#x27;](area);); out tags; My Overpass server returns Baja California in the results for this query, even though this state is in Mexico. Overpass Turbo corre...'''
date = "2019-09-03T16:39:00Z"
lastmod = "2019-09-07T16:22:00Z"
weight = 70615
keywords = [ "openstreetmap", "overpass", "overpass-api" ]
aliases = [ "/questions/70615" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why are area queries in my own Overpass server returning different results from the official server?](/questions/70615/why-are-area-queries-in-my-own-overpass-server-returning-different-results-from-the-official-server)

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
<span id="post-70615-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70615-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-70615-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Here's my query to collect all of the States within the US:</p>
<p><code>[out:json]; area['admin_level'='2']['name'='United States']; (relation['admin_level'='4'](area);); out tags;</code></p>
<p>My Overpass server returns <a href="https://www.openstreetmap.org/relation/2589601">Baja California</a> in the results for this query, even though this state is in Mexico. <a href="http://overpass-turbo.eu/s/LOo">Overpass Turbo</a> correctly excludes this from the results.</p>
<p>Similarly, my query to collect all of the cities within Indiana returns Chicago in the results (while the Overpass Turbo only includes East Chicago &amp; New Chicago):</p>
<p><code>[timeout:900][out:json]; area['ISO3166-2'~'^US']['admin_level'='4']['name'='Indiana']; (relation['admin_level'~'8'](area);); out tags;</code></p>
<p>I'm using the <a href="https://hub.docker.com/r/wiktorn/overpass-api">wiktorn/overpass-api</a> Docker image that I started it with:</p>
<p><code>docker run \ -e OVERPASS_META=yes \ -e OVERPASS_MODE=clone \ -e OVERPASS_DIFF_URL=</code><a href="https://planet.openstreetmap.org/replication/minute/"><code>https://planet.openstreetmap.org/replication/minute/</code></a><code> \ -v /home/ubuntu/overpass_clone_db/:/db \ -p 80:80 \ -i -t \ --name overpass_world \ wiktorn/overpass-api</code></p>
<p>Is there something that I can do to correct these results?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Sep '19, 16:39</strong></p>
<img src="https://secure.gravatar.com/avatar/0ada7b97d85873855231744286452af4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesChevalier&#39;s gravatar image" />
<p><span>JamesChevalier</span><br />
<span class="score" title="151 reputation points">151</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesChevalier has one accepted answer">25%</span></p>
</div>
</div>
<div id="comments-container-70615" class="comments-container">
&#10;</div>
<div id="comment-tools-70615" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70615-form-container" class="comment-form-container">
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

<span id="70675"></span>

<div id="answer-container-70675" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70675-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70675-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70675-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SimonPoole has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There was something wrong with my initial attempt at using the Docker image. I deleted my container and retried the process - everything worked great.</p>
<p>Also, installing Overpass directly onto a server worked great too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Sep '19, 16:22</strong></p>
<img src="https://secure.gravatar.com/avatar/0ada7b97d85873855231744286452af4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JamesChevalier&#39;s gravatar image" />
<p><span>JamesChevalier</span><br />
<span class="score" title="151 reputation points">151</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JamesChevalier has one accepted answer">25%</span></p>
</div>
</div>
<div id="comments-container-70675" class="comments-container">
&#10;</div>
<div id="comment-tools-70675" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70675-form-container" class="comment-form-container">
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

