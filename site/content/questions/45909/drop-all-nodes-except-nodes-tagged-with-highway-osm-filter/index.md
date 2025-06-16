+++
type = "question"
title = "drop all nodes except nodes tagged with highway [OSM Filter]"
description = '''Hi all, I&#x27;m using OSM filter to filter my .osm, and I want to remove each nodes besides the ones with a tag highway :  node id=&quot;120044012&quot; lat=&quot;50.9301459&quot; lon=&quot;1.8091746&quot; -&amp;gt; I want to remove it  node id=&quot;120044014&quot; lat=&quot;50.9295054&quot; lon=&quot;1.8098138&quot; -&amp;gt; I want to keep it  tag k=&quot;crossing&quot; v=&quot;unc...'''
date = "2015-10-15T12:35:00Z"
lastmod = "2015-10-19T23:04:00Z"
weight = 45909
keywords = [ "nodes", "osmfilter" ]
aliases = [ "/questions/45909" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [drop all nodes except nodes tagged with highway \[OSM Filter\]](/questions/45909/drop-all-nodes-except-nodes-tagged-with-highway-osm-filter)

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
<span id="post-45909-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45909-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45909-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all, I'm using OSM filter to filter my .osm, and I want to remove each nodes besides the ones with a tag highway :</p>
<pre><code>node id=&quot;120044012&quot; lat=&quot;50.9301459&quot; lon=&quot;1.8091746&quot; -&gt; I want to remove it
&#10;node id=&quot;120044014&quot; lat=&quot;50.9295054&quot; lon=&quot;1.8098138&quot; -&gt; I want to keep it
    tag k=&quot;crossing&quot; v=&quot;uncontrolled&quot;
    tag k=&quot;crossing_ref&quot; v=&quot;zebra&quot;
    tag k=&quot;highway&quot; v=&quot;crossing&quot;
node</code></pre>
<p>I tried --keep-nodes="highway=<em>", and --drop-nodes="highway!=</em>" but nothing is working. How can you do that ? I'm very new to this, thank you :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Oct '15, 12:35</strong></p>
<img src="https://secure.gravatar.com/avatar/4d538c0ffc26fe6f362418e08c4308c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kevin_matta&#39;s gravatar image" />
<p><span>kevin_matta</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kevin_matta has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-45909" class="comments-container">
&#10;</div>
<div id="comment-tools-45909" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45909-form-container" class="comment-form-container">
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

<span id="46002"></span>

<div id="answer-container-46002" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46002-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46002-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46002-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>(converted a comment thread to an answer)</p>
<p>You need to follow the instructions on the <a href="https://wiki.openstreetmap.org/wiki/Osmfilter#Keep_specific_Object_Type">relevant wiki page</a>. Use</p>
<pre><code>--keep= --keep-nodes=highway</code></pre>
<p>If you want to also keep ways tagged with the highway tag (and use --keep-ways to that effect) then this will also add those nodes that do not have a highway tag, but are needed to construct a way with a highway tag. This can be switched off with <code>--ignore-dependencies</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Oct '15, 23:04</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-46002" class="comments-container">
<span id="45918"></span>
<div id="comment-45918" class="comment">
<div id="post-45918-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It's working fine now, thank you again. In fact I was trying to get nodes about highway and junctions between highway, so I guess I don't need any dependencies.</p>
</div>
<div id="comment-45918-info" class="comment-info">
<span class="comment-age">(15 Oct '15, 15:41)</span> <span class="comment-user userinfo">kevin_matta</span>
</div>
</div>
</div>
<div id="comment-tools-46002" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46002-form-container" class="comment-form-container">
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

