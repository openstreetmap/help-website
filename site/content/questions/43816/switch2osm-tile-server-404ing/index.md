+++
type = "question"
title = "switch2osm tile server 404ing"
description = '''Hello, I run Amazon EC2 t2.medium server (4G ram, 2cpu) and after following switch2osm tutorial, everything works ok. But before tile is rendered 1st time - it sometimes ends with 404. Its probably caused by too many parallel connection, b/c its fine when i resize the map window. But why does it ter...'''
date = "2015-06-26T16:08:00Z"
lastmod = "2015-06-26T18:18:00Z"
weight = 43816
keywords = [ "tileserver", "renderd", "mapnik", "switch2osm" ]
aliases = [ "/questions/43816" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [switch2osm tile server 404ing](/questions/43816/switch2osm-tile-server-404ing)

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
<span id="post-43816-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43816-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43816-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I run Amazon EC2 t2.medium server (4G ram, 2cpu) and after following switch2osm tutorial, everything works ok. But before tile is rendered 1st time - it sometimes ends with 404. Its probably caused by too many parallel connection, b/c its fine when i resize the map window. But why does it terminate them instead of queue them? (Possibly apache conf? or EC2 terminiting conns?)</p>
<p>See <a href="https://www.dropbox.com/s/0ooyac7syd47xln/Screenshot%202015-06-26%2017.02.33.png?dl=0">screenshot</a> for more details or live server <a href="http://52.27.56.136/osm/slippymap.html?zoom=10&amp;lat=49.05209&amp;lon=16.28577&amp;layers=B0">here</a>.</p>
<h1 id="configuration">Configuration:</h1>
<ul>
<li>default ubuntu-server-trusty</li>
<li>+Posgres tuned like this:</li>
</ul>
<pre><code>default_statistics_target = 50 # pgtune wizard 2015-06-25
constraint_exclusion = on # pgtune wizard 2015-06-25
checkpoint_completion_target = 0.9 # pgtune wizard 2015-06-25
checkpoint_segments = 16 # pgtune wizard 2015-06-25
max_connections = 50 # pgtune wizard 2015-06-25
maintenance_work_mem = 240MB # pgtune wizard 2015-06-25
effective_cache_size = 2816MB # pgtune wizard 2015-06-25
work_mem = 36MB # pgtune wizard 2015-06-25
wal_buffers = 8MB # pgtune wizard 2015-06-25
shared_buffers = 960MB # pgtune wizard 2015-06-25</code></pre>
<p>Any help welcomed!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jun '15, 16:08</strong></p>
<img src="https://secure.gravatar.com/avatar/97235063baed8a04a2ee73e3e18e7db6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zby-cz&#39;s gravatar image" />
<p><span>zby-cz</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zby-cz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jun '15, 16:15</strong> </span></p>
</div>
</div>
<div id="comments-container-43816" class="comments-container">
&#10;</div>
<div id="comment-tools-43816" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43816-form-container" class="comment-form-container">
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

<span id="43817"></span>

<div id="answer-container-43817" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43817-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43817-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43817-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="zby-cz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You're probably looking for the settings <code>ModTileRequestTimeout</code> and <code>ModTileMissingRequestTimeout</code>. See <a href="http://wiki.openstreetmap.org/wiki/HowTo_mod_tile">http://wiki.openstreetmap.org/wiki/HowTo_mod_tile</a> for details.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '15, 18:18</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-43817" class="comments-container">
&#10;</div>
<div id="comment-tools-43817" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43817-form-container" class="comment-form-container">
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

