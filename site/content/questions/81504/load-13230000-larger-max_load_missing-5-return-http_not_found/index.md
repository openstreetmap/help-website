+++
type = "question"
title = "Load (13.230000) larger max_load_missing (5). Return HTTP_NOT_FOUND."
description = '''I&#x27;m running a local OSM tile server, and I can pre-render tiles which are loaded without any problems on my leaflet site. But whenever I zoom into a level which has not been pre-rendered, I immediately receive a 404... But when I check the error logs of apache2, I keep seeing the same error over and...'''
date = "2021-08-26T15:48:00Z"
lastmod = "2021-08-27T07:05:00Z"
weight = 81504
keywords = [ "render_list", "osm2pgsql", "tileserver" ]
aliases = [ "/questions/81504" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Load (13.230000) larger max_load_missing (5). Return HTTP_NOT_FOUND.](/questions/81504/load-13230000-larger-max_load_missing-5-return-http_not_found)

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
<span id="post-81504-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81504-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81504-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm running a local OSM tile server, and I can pre-render tiles which are loaded without any problems on my leaflet site.</p>
<p>But whenever I zoom into a level which has not been pre-rendered, I immediately receive a 404...</p>
<p>But when I check the error logs of apache2, I keep seeing the same error over and over again:</p>
<pre><code>Load (13.230000) larger max_load_missing (5). Return HTTP_NOT_FOUND.</code></pre>
<p>So I guess it takes 13,23 seconds to load something, but it's larger than the allowed 5 seconds or something?</p>
<p>I might be reading this completely incorrect, but I'm stuck anyhow... So would anyone have an idea what I'm doing wrong?</p>
<p>I'm running the tile server on an Azure VM (Ubuntu 20.04) w/ 8 CPU and 32GB RAM - With renderd</p>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-render_list" rel="tag" title="see questions tagged &#39;render_list&#39;">render_list</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Aug '21, 15:48</strong></p>
<img src="https://secure.gravatar.com/avatar/04175cc004ecad1e262fad8e94f86d62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KoenMlt&#39;s gravatar image" />
<p><span>KoenMlt</span><br />
<span class="score" title="42 reputation points">42</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KoenMlt has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Aug '21, 07:06</strong> </span></p>
</div>
</div>
<div id="comments-container-81504" class="comments-container">
<span id="81505"></span>
<div id="comment-81505" class="comment">
<div id="post-81505-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Without more information (e.g. what software you are actually running) it'll be very difficult for anyone to usefully comment.</p>
<p>What I'd suggest you do is to restart Apache and renderd (or whatever you're using) and watch the renderd logs after you restart it, once you make a single high-zoom tile request. If it's renderd you should see "START TILE" and "DONE TILE" wherever it writes its logs. The length of time for a single high-zoom request might help show what is actually wrong (e.g. missing indexes).</p>
</div>
<div id="comment-81505-info" class="comment-info">
<span class="comment-age">(26 Aug '21, 16:00)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="81506"></span>
<div id="comment-81506" class="comment">
<div id="post-81506-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The "load" is a metric commonly used on Unix systems to reflect the number of processes either keeping a CPU busy or waiting for access to a CPU. While a load of 13 doesn't mean much on a 64-core server, on a 4-core system it will mean that things are getting a bit cramped. The Unix command <code>top</code> will show you the processes that use most CPU. <code>mod_tile</code> is configured to not even attempt the rendering of a new tile when the load is above 5. While you could change that setting to, say, 20 in order to force it to render tiles on high load, this would likely only lead to long waiting times and timeouts until you find and remedy the cause of the high system load.</p>
</div>
<div id="comment-81506-info" class="comment-info">
<span class="comment-age">(26 Aug '21, 16:08)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="81515"></span>
<div id="comment-81515" class="comment">
<div id="post-81515-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> I added some more info</p>
</div>
<div id="comment-81515-info" class="comment-info">
<span class="comment-age">(27 Aug '21, 07:05)</span> <span class="comment-user userinfo">KoenMlt</span>
</div>
</div>
</div>
<div id="comment-tools-81504" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81504-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

