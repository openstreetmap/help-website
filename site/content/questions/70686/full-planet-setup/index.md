+++
type = "question"
title = "Full Planet Setup"
description = '''Hi there I want to build a full planet map tiles service that should serve a lot of traffic, something like 300M requests/day. I thought about:  PostGIS Server  Tile Servers (behind a load balancer) CDN for tile servers (SaaS, not self hosted)  Since I want to run it on a cloud provider (google/aws)...'''
date = "2019-09-09T08:00:00Z"
lastmod = "2019-09-09T11:19:00Z"
weight = 70686
keywords = [ "planet", "rendering", "tileserver" ]
aliases = [ "/questions/70686" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Full Planet Setup](/questions/70686/full-planet-setup)

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
<span id="post-70686-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70686-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70686-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there I want to build a full planet map tiles service that should serve a lot of traffic, something like 300M requests/day.</p>
<p>I thought about:</p>
<ol>
<li>PostGIS Server</li>
<li>Tile Servers (behind a load balancer)</li>
<li>CDN for tile servers (SaaS, not self hosted)</li>
</ol>
<p>Since I want to run it on a cloud provider (google/aws), is there a way to share-cache between tiles server so that they can auto-scale or even run on spot instances? (thus can be terminated in a 2-3 minutes heads up)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Sep '19, 08:00</strong></p>
<img src="https://secure.gravatar.com/avatar/47110f56c594a7515b757d9975b9a8c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LiorM&#39;s gravatar image" />
<p><span>LiorM</span><br />
<span class="score" title="31 reputation points">31</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LiorM has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Sep '19, 08:02</strong> </span></p>
</div>
</div>
<div id="comments-container-70686" class="comments-container">
&#10;</div>
<div id="comment-tools-70686" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70686-form-container" class="comment-form-container">
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

<span id="70690"></span>

<div id="answer-container-70690" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70690-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70690-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70690-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The bottleneck when rendering new tiles is the PostGIS database and its disk storage, not the actual rendering of tiles. Therefore I am not sure if scaling up the number of tile servers but not scaling up the PostGIS database is any good. A more promising approach in my opinion would be to have a fast local PostGIS database on the tile servers that may be fed from one master PostGIS using Slony or another PostgreSQL replication mechanism. That would give you a startup time for a new tile server of a couple of hours (better than the ~16 hours it would require to actually import a full database) AND you'd be distributing the database load. But YMMV - if you expect most of those 300m tiles/day to be for the same hot spots then the CDN and the tile server's cache will already take away most of the load.</p>
<p>To answer your question, mod_tile and renderd support "pluggable storage backends" (<a href="https://lists.openstreetmap.org/pipermail/dev/2013-March/026689.html)">https://lists.openstreetmap.org/pipermail/dev/2013-March/026689.html)</a> which is something you might want to explore, however I am not aware of anyone using that in production.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Sep '19, 09:41</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-70690" class="comments-container">
<span id="70691"></span>
<div id="comment-70691" class="comment">
<div id="post-70691-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So, assuming that I have a machine image (AMI) with PostGIS + Render on it, how can I put (and scale) more than 1 instances behind a Load Balancer and make them autoscale? the Load Balancer will send a request to each render at a time thus creating same files on the renders...how can I share the cache between of all them (metafiles) ?</p>
</div>
<div id="comment-70691-info" class="comment-info">
<span class="comment-age">(09 Sep '19, 09:58)</span> <span class="comment-user userinfo">LiorM</span>
</div>
</div>
<span id="70695"></span>
<div id="comment-70695" class="comment">
<div id="post-70695-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Options:</p>
<ul>
<li>use the pluggable storage backends (link in previous message, and as I said, these are mostly uncharted waters) to implement a shared cache;</li>
<li>use a network-mounted drive as a tile cache (depends on what your cloud provider supports)</li>
<li>use local storage and rsync</li>
</ul>
</div>
<div id="comment-70695-info" class="comment-info">
<span class="comment-age">(09 Sep '19, 11:19)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-70690" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70690-form-container" class="comment-form-container">
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

