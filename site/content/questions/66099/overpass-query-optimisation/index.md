+++
type = "question"
title = "Overpass query optimisation"
description = '''I am trying to write a query that will return all pubs and bars around a certain point. I&#x27;m having issues with the results that are ways. At the moment I am getting all the nodes for the way and then using some post processing to match up the first node of the way to the node lat/long data. Obviousl...'''
date = "2018-09-29T23:26:00Z"
lastmod = "2018-09-30T12:10:00Z"
weight = 66099
keywords = [ "overpassapi", "overpass", "overpass-ql" ]
aliases = [ "/questions/66099" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass query optimisation](/questions/66099/overpass-query-optimisation)

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
<span id="post-66099-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66099-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66099-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to write a query that will return all pubs and bars around a certain point. I'm having issues with the results that are ways. At the moment I am getting all the nodes for the way and then using some post processing to match up the first node of the way to the node lat/long data. Obviously, this is largely inefficient. This is the query I'm currently using. Many thanks.</p>
<p><code>[out:json]; (node[amenity=pub](around:5000,51.5152117,-0.144044); foreach(out;) way[amenity=pub](around:5000,51.5152117,-0.144044); foreach( out; node(w); out; ); node[amenity=bar](around:5000,51.5152117,-0.144044); foreach(out;) way[amenity=bar](around:5000,51.5152117,-0.144044); foreach( out; node(w); out;);); (._;%3E;)</code></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Sep '18, 23:26</strong></p>
<img src="https://secure.gravatar.com/avatar/e12abf3595bf70ec5646c1a9de9da622?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adam__&#39;s gravatar image" />
<p><span>adam__</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adam__ has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66099" class="comments-container">
&#10;</div>
<div id="comment-tools-66099" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66099-form-container" class="comment-form-container">
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

<span id="66100"></span>

<div id="answer-container-66100" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66100-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66100-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-66100-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="adam__ has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Each way lists it's member nodes, so in your post processing you can build a mapping of node ids to nodes and use that to retrieve a way node, you don't need to order the output. So a query like <a href="http://overpass-turbo.eu/s/Cne">http://overpass-turbo.eu/s/Cne</a> should work.</p>
<pre><code>[out:json];
(node[amenity=pub](around:5000,51.5152117,-0.144044);
way[amenity=pub](around:5000,51.5152117,-0.144044);
node[amenity=bar](around:5000,51.5152117,-0.144044);
way[amenity=bar](around:5000,51.5152117,-0.144044);
);
(._;&gt;;);
out;</code></pre>
<p>You might also be interested in <code>out center;</code> which converts ways to a node at the center of the bounding box of the way (or relation).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Sep '18, 04:30</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-66100" class="comments-container">
<span id="66101"></span>
<div id="comment-66101" class="comment">
<div id="post-66101-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>out center is exactly what I'm after. My final query is <a href="http://overpass-turbo.eu/s/Cns">http://overpass-turbo.eu/s/Cns</a> since I don't need individual lat/lon of the ways nodes</p>
</div>
<div id="comment-66101-info" class="comment-info">
<span class="comment-age">(30 Sep '18, 12:10)</span> <span class="comment-user userinfo">adam__</span>
</div>
</div>
</div>
<div id="comment-tools-66100" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66100-form-container" class="comment-form-container">
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

