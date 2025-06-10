+++
type = "question"
title = "*.tile.openstreetmap.org is timed out"
description = '''Hi, My web page embeds a common OSM map, which doesn&#x27;t work now (yesterday it was ok), since all requests of type *.tile.openstreetmap.org (e.g., http://c.tile.openstreetmap.org/10/637/386.png) are timed out. I tried to ping with the following results: $ping tile.openstreetmap.org  PING baku.tile.op...'''
date = "2014-08-05T17:28:00Z"
lastmod = "2014-08-06T10:46:00Z"
weight = 35540
keywords = [ "tile", "timeout" ]
aliases = [ "/questions/35540" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\*.tile.openstreetmap.org is timed out](/questions/35540/tileopenstreetmaporg-is-timed-out)

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
<span id="post-35540-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35540-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35540-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>My web page embeds a common OSM map, which doesn't work now (yesterday it was ok), since all requests of type *.tile.openstreetmap.org (e.g., <a href="http://c.tile.openstreetmap.org/10/637/386.png">http://c.tile.openstreetmap.org/10/637/386.png</a>) are timed out. I tried to ping with the following results:</p>
<pre><code>$ping tile.openstreetmap.org
&#10;PING baku.tile.openstreetmap.org (94.20.20.55) 56(84) bytes of data.
--- baku.tile.openstreetmap.org ping statistics ---
20 packets transmitted, 0 received, 100% packet loss, time 20237ms</code></pre>
<p>The service is down for almost 12 hours (starting from this morning), please deal with this.</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tile" rel="tag" title="see questions tagged &#39;tile&#39;">tile</span> <span class="post-tag tag-link-timeout" rel="tag" title="see questions tagged &#39;timeout&#39;">timeout</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Aug '14, 17:28</strong></p>
<img src="https://secure.gravatar.com/avatar/1d81acb7ee1fab78c4daef9c111ec365?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="armmarti&#39;s gravatar image" />
<p><span>armmarti</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="armmarti has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Aug '14, 17:33</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-35540" class="comments-container">
<span id="35543"></span>
<div id="comment-35543" class="comment">
<div id="post-35543-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>FWIW, the server from which your tiles are served seems to work for me:</p>
<pre><code>Pinging baku.tile.openstreetmap.org [94.20.20.55] with 32 bytes of data:
Reply from 94.20.20.55: bytes=32 time=105ms TTL=54
Reply from 94.20.20.55: bytes=32 time=105ms TTL=54
Reply from 94.20.20.55: bytes=32 time=105ms TTL=54
Reply from 94.20.20.55: bytes=32 time=104ms TTL=54</code></pre>
<p>What does a traceroute have to say?</p>
</div>
<div id="comment-35543-info" class="comment-info">
<span class="comment-age">(05 Aug '14, 17:36)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="35563"></span>
<div id="comment-35563" class="comment">
<div id="post-35563-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for quick response, SomeoneElse. I think this is a political issue, since I request the tiles from Armenia, whereas tile.openstreetmap.org redirects to baku.tile.openstreetmap.org (to Azerbaijan). It seems, they blocked all requests from Armenian IPs... So, I guess it's totally against OpenStreetMap's policy!</p>
</div>
<div id="comment-35563-info" class="comment-info">
<span class="comment-age">(06 Aug '14, 09:00)</span> <span class="comment-user userinfo">armmarti</span>
</div>
</div>
</div>
<div id="comment-tools-35540" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35540-form-container" class="comment-form-container">
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

<span id="35566"></span>

<div id="answer-container-35566" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35566-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35566-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-35566-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>With a bit of luck (based on comments on #osm-dev) this might start working again shortly.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Aug '14, 10:40</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> wikified <strong>06 Aug '14, 10:41</strong> </span></p>
</div>
</div>
<div id="comments-container-35566" class="comments-container">
<span id="35567"></span>
<div id="comment-35567" class="comment">
<div id="post-35567-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Nice, it works, thank you very much!</p>
</div>
<div id="comment-35567-info" class="comment-info">
<span class="comment-age">(06 Aug '14, 10:46)</span> <span class="comment-user userinfo">armmarti</span>
</div>
</div>
</div>
<div id="comment-tools-35566" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35566-form-container" class="comment-form-container">
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

