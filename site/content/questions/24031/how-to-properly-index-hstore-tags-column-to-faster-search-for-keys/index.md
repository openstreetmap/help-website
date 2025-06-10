+++
type = "question"
title = "How to properly index hstore tags column to faster search for keys"
description = '''Hi, I imported a large area of planet.osm file into a postgresql database using pgsnapshot schema. I need to extract nodes along a line that have certain keys in the tags column. To do that I use the following query: SELECT id, tags  FROM nodes  WHERE ST_DWithin(nodes.geom, ST_MakeLine(&#x27;{$geom1}&#x27;, &#x27;...'''
date = "2013-07-06T13:37:00Z"
lastmod = "2013-07-13T10:55:00Z"
weight = 24031
keywords = [ "index", "searching", "tags" ]
aliases = [ "/questions/24031" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to properly index hstore tags column to faster search for keys](/questions/24031/how-to-properly-index-hstore-tags-column-to-faster-search-for-keys)

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
<span id="post-24031-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24031-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24031-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I imported a large area of planet.osm file into a postgresql database using pgsnapshot schema. I need to extract nodes along a line that have certain keys in the tags column. To do that I use the following query:</p>
<pre><code>SELECT id, tags  
FROM nodes  
WHERE ST_DWithin(nodes.geom, ST_MakeLine(&#39;{$geom1}&#39;, &#39;{$geom2}&#39;), 0.001)  
AND tags ? &#39;{$type}&#39;;</code></pre>
<p>$geom1 and $geom2 are geometries for start and end points of my line.<br />
The $type variable contains the key I want to search for. Now, it can have one of the following values: 'historic' or 'tourist'.</p>
<p>The query given above works but it is too slow. I guess searching for a key in tags column takes too much time. I read about GIN and GIST indexes and I generated a GIN index using the following query:</p>
<pre><code>CREATE INDEX nodes_tags_idx ON nodes USING GIN(tags);</code></pre>
<p>After creating the index I searched again for nodes using the same first query but there is no change in performance.<br />
</p>
<p>How can I properly use GIN and GIST to index tags column so I can faster search for nodes that have a certain key in tags column?</p>
<p>Thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-index" rel="tag" title="see questions tagged &#39;index&#39;">index</span> <span class="post-tag tag-link-searching" rel="tag" title="see questions tagged &#39;searching&#39;">searching</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jul '13, 13:37</strong></p>
<img src="https://secure.gravatar.com/avatar/af030346f57b37767fe7e80f23e07d7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="raduzugravu&#39;s gravatar image" />
<p><span>raduzugravu</span><br />
<span class="score" title="31 reputation points">31</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="raduzugravu has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-24031" class="comments-container">
<span id="24033"></span>
<div id="comment-24033" class="comment">
<div id="post-24033-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I think this is really a Stack Exchange query: it is really asking about fundamental performing tuning issues for PostgreSQL.</p>
<p>I suspect that when you have a predicate that uses a GIST index then that is the only index which will be used: therefore indexing the tags column is unlikely to give you any benefit whatever index strategy you use. I am no expert on these aspects of PostgreSQL so can't comment further: however, the place to start is with running EXPLAIN on your queries before you do anything else.</p>
</div>
<div id="comment-24033-info" class="comment-info">
<span class="comment-age">(06 Jul '13, 15:06)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-24031" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24031-form-container" class="comment-form-container">
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

<span id="24202"></span>

<div id="answer-container-24202" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24202-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="raduzugravu has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That is the correct way to create an index on tags, and your query looks fine.</p>
<p>Make sure you run ANALYZE after creating it.</p>
<p>Without any more detail such as EXPLAIN ANALYZE results, it's pretty much impossible to say what's going on.</p>
<p>Another option is a composite index, but that really depends on what you're doing. See <a href="http://lists.openstreetmap.org/pipermail/osmosis-dev/2013-January/001485.html">http://lists.openstreetmap.org/pipermail/osmosis-dev/2013-January/001485.html</a> for more information.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jul '13, 10:55</strong></p>
<img src="https://secure.gravatar.com/avatar/5634c46072077e10f5b7c0da9b4bbb62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pnorman&#39;s gravatar image" />
<p><span>pnorman</span><br />
<span class="score" title="2352 reputation points"><span>2.4k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pnorman has 9 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-24202" class="comments-container">
&#10;</div>
<div id="comment-tools-24202" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24202-form-container" class="comment-form-container">
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

