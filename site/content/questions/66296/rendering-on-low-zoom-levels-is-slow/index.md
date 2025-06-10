+++
type = "question"
title = "Rendering on low zoom levels is slow"
description = '''Hi everyone, We recently installed our own tile server based on this manual. All went well and everything is running fine. The one issue is that its slow rendering. When we insert a small map then rendering is as fast as google maps for example. But when we load a big map like europe (this is our go...'''
date = "2018-10-11T15:35:00Z"
lastmod = "2018-10-18T02:34:00Z"
weight = 66296
keywords = [ "rendering", "slow", "ubuntu", "tileserver" ]
aliases = [ "/questions/66296" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Rendering on low zoom levels is slow](/questions/66296/rendering-on-low-zoom-levels-is-slow)

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
<span id="post-66296-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66296-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-66296-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone,</p>
<p>We recently installed our own tile server based on <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">this manual</a>. All went well and everything is running fine. The one issue is that its slow rendering. When we insert a small map then rendering is as fast as google maps for example. But when we load a big map like europe (this is our goal) rendering is slow. How slow? my browser gets 404 errors on the .png files.</p>
<p>Of course its a matter of fine tuning im sure, but I don't know where to start. Below are the specs of my server:</p>
<ol>
<li>Ubuntu 18.04.1 LTS</li>
<li>2x 12 core cpu with hyperthreading (48 threads available in total)</li>
<li>64GB Memory</li>
<li>1.5TB all SSD storage in RAID 1+0</li>
</ol>
<p>So all of this should be enough to make it perform. I hope you guys can help :)</p>
<p>Greets, Jeffrey</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Oct '18, 15:35</strong></p>
<img src="https://secure.gravatar.com/avatar/1023b3d6a2bf3539a253541cc8ab14a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jeffrey%20Jaspers&#39;s gravatar image" />
<p><span>Jeffrey Jaspers</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jeffrey Jaspers has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Oct '18, 02:35</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/e228dd20b7da2a6c8f559e2118ce08d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kocio&#39;s gravatar image" />
<p><span>kocio</span><br />
<span class="score" title="2054 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p>
</div>
</div>
<div id="comments-container-66296" class="comments-container">
&#10;</div>
<div id="comment-tools-66296" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66296-form-container" class="comment-form-container">
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

<span id="66374"></span>

<div id="answer-container-66374" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66374-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66374-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66374-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not surprised - rendering zoom levels z0-z12 on OSMF servers <a href="https://munin.openstreetmap.org/static/dynazoom.html?plugin_name=openstreetmap.org%2Frender.openstreetmap.org%2Frenderd_processed&amp;start_iso8601=2018-10-06T14%3A40%3A52%2B0200&amp;stop_iso8601=2018-10-08T06%3A16%3A52%2B0200&amp;start_epoch=1538829652&amp;stop_epoch=1538972212&amp;lower_limit=&amp;upper_limit=&amp;size_x=800&amp;size_y=400&amp;cgiurl_graph=%2Fmunin-cgi%2Fmunin-cgi-graph">takes many hours</a> on proper machines too (look at machines described as "Tile server" on <a href="https://hardware.openstreetmap.org"></a><a href="https://hardware.openstreetmap.org">https://hardware.openstreetmap.org</a>), because a lot of data needs to be read from a database and then get the right look. That's why they are pre-rendered only 1-2 times a month (in the middle of the night, when the demand for tiles rendering is much lower). Whole Europe is visible on ~z4, so that's probably the case.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Oct '18, 02:34</strong></p>
<img src="https://secure.gravatar.com/avatar/e228dd20b7da2a6c8f559e2118ce08d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kocio&#39;s gravatar image" />
<p><span>kocio</span><br />
<span class="score" title="2054 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kocio has 14 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-66374" class="comments-container">
&#10;</div>
<div id="comment-tools-66374" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66374-form-container" class="comment-form-container">
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

