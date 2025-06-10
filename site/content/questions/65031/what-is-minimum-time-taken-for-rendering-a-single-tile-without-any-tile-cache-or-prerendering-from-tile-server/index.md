+++
type = "question"
title = "What is minimum time taken for rendering a single tile without any tile cache or prerendering from tile server?"
description = '''I have implemented a tile server. But I haven&#x27;t build any tile cache yet. For the very first time when I open a tile in browser, it took around 53seconds to load for a single tile(256*256, zoom level 1, openstreetmap carto style ).  My question is - Is this time taken normal? or Should I look into m...'''
date = "2018-07-30T21:49:00Z"
lastmod = "2018-08-11T05:39:00Z"
weight = 65031
keywords = [ "openstreetmap", "generate_tiles", "postgresql", "tileserver" ]
aliases = [ "/questions/65031" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What is minimum time taken for rendering a single tile without any tile cache or prerendering from tile server?](/questions/65031/what-is-minimum-time-taken-for-rendering-a-single-tile-without-any-tile-cache-or-prerendering-from-tile-server)

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
<span id="post-65031-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65031-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65031-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have implemented a tile server. But I haven't build any tile cache yet. For the very first time when I open a tile in browser, it took around 53seconds to load for a single tile(256*256, zoom level 1, openstreetmap carto style ).</p>
<p>My question is - <strong>Is this time taken normal? or Should I look into my Postgres configuration to further minimize the time. And Is there any minimum time for tile loading(without any prerender or cache) that can be achieved using postgres tuning?</strong></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-generate_tiles" rel="tag" title="see questions tagged &#39;generate_tiles&#39;">generate_tiles</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jul '18, 21:49</strong></p>
<img src="https://secure.gravatar.com/avatar/943a788b771da12a63057582fbf250b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anuranpal&#39;s gravatar image" />
<p><span>anuranpal</span><br />
<span class="score" title="21 reputation points">21</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anuranpal has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jul '18, 22:02</strong> </span></p>
</div>
</div>
<div id="comments-container-65031" class="comments-container">
<span id="65032"></span>
<div id="comment-65032" class="comment">
<div id="post-65032-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What zoom level and what stylesheet?</p>
</div>
<div id="comment-65032-info" class="comment-info">
<span class="comment-age">(30 Jul '18, 21:53)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="65033"></span>
<div id="comment-65033" class="comment">
<div id="post-65033-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>zoom level one. openstreet carto style</p>
</div>
<div id="comment-65033-info" class="comment-info">
<span class="comment-age">(30 Jul '18, 21:55)</span> <span class="comment-user userinfo">anuranpal</span>
</div>
</div>
</div>
<div id="comment-tools-65031" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65031-form-container" class="comment-form-container">
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

<span id="65110"></span>

<div id="answer-container-65110" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65110-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65110-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-65110-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="anuranpal has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is strongly dependent on the zoom level we are talking about.</p>
<p>Fastest rendering would be in "high" zoomlevels like 18 or 19:</p>
<p><code>&gt; time render_single_tile.py s osm.xml -o out.png -u /19/274383/180030.png real 0m11.298s user 0m1.152s sys 0m0.316s</code></p>
<p>If you give me an exact tile URL I can check how long it takes on my tileserver.</p>
<p>In case you wonder where to get render_single_tile.py have a look at</p>
<p><a href="https://github.com/giggls/openstreetmap-carto-de/blob/master/scripts/render_single_tile.py">https://github.com/giggls/openstreetmap-carto-de/blob/master/scripts/render_single_tile.py</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Aug '18, 15:29</strong></p>
<img src="https://secure.gravatar.com/avatar/ed4b275dcccc85019201630e7cf0e3b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="giggls&#39;s gravatar image" />
<p><span>giggls</span><br />
<span class="score" title="126 reputation points">126</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="giggls has 2 accepted answers">50%</span></p>
</div>
</div>
<div id="comments-container-65110" class="comments-container">
<span id="65265"></span>
<div id="comment-65265" class="comment">
<div id="post-65265-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you so much for your help :-) <a href="https://help.openstreetmap.org/users/1957/giggls">@giggls</a></p>
</div>
<div id="comment-65265-info" class="comment-info">
<span class="comment-age">(11 Aug '18, 05:39)</span> <span class="comment-user userinfo">anuranpal</span>
</div>
</div>
</div>
<div id="comment-tools-65110" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65110-form-container" class="comment-form-container">
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

