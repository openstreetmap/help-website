+++
type = "question"
title = "Overpass API: Find something else than points (node)"
description = '''Hello I have a query which works great for playgrounds that are points: node[&quot;name&quot;=&quot;Les Ulis&quot;]; node  (around:5000)  [&quot;leisure&quot;=&quot;playground&quot;]; out body;  But it does not work when the playgrounds are shape, like square. How could I do that? thank you'''
date = "2015-07-03T10:17:00Z"
lastmod = "2015-07-04T09:00:00Z"
weight = 43943
keywords = [ "ways", "overpass", "nodes", "query" ]
aliases = [ "/questions/43943" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API: Find something else than points (node)](/questions/43943/overpass-api-find-something-else-than-points-node)

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
<span id="post-43943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43943-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello I have a query which works great for playgrounds that are points:</p>
<pre><code>node[&quot;name&quot;=&quot;Les Ulis&quot;];
node
  (around:5000)
  [&quot;leisure&quot;=&quot;playground&quot;];
out body;</code></pre>
<p>But it does not work when the playgrounds are shape, like square. How could I do that? thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jul '15, 10:17</strong></p>
<img src="https://secure.gravatar.com/avatar/475f485ebcd73adde35434f45410b449?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bodtx&#39;s gravatar image" />
<p><span>bodtx</span><br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bodtx has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jul '15, 11:04</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-43943" class="comments-container">
&#10;</div>
<div id="comment-tools-43943" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43943-form-container" class="comment-form-container">
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

<span id="43945"></span>

<div id="answer-container-43945" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43945-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43945-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-43945-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Ok answer are in the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#All_kind_of_objects">ways</a> :)</p>
<pre><code>node[&quot;name&quot;=&quot;Bures-sur-Yvette&quot;];
(
way
  (around:5000)
  [&quot;leisure&quot;=&quot;playground&quot;];
node
  (around:5000)
  [&quot;leisure&quot;=&quot;playground&quot;];
  );
(._;&gt;;);
out body;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jul '15, 10:35</strong></p>
<img src="https://secure.gravatar.com/avatar/475f485ebcd73adde35434f45410b449?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bodtx&#39;s gravatar image" />
<p><span>bodtx</span><br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bodtx has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43945" class="comments-container">
<span id="43947"></span>
<div id="comment-43947" class="comment">
<div id="post-43947-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>You might also want to include relations.</p>
</div>
<div id="comment-43947-info" class="comment-info">
<span class="comment-age">(03 Jul '15, 11:10)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
<span id="43971"></span>
<div id="comment-43971" class="comment">
<div id="post-43971-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Please note that your query does not behave like you think it does. <code>node(around:5000)...</code> in your case will find all nodes, which are up to 5000m away from all ways, which in turn are up to 5000m away from Bures-sur-Yvette. Obviously, this will return nodes, which are much further away from Bures-sur-Yvette than 5000m. To fix this, use the following: <a href="http://overpass-turbo.eu/s/afS">http://overpass-turbo.eu/s/afS</a></p>
</div>
<div id="comment-43971-info" class="comment-info">
<span class="comment-age">(04 Jul '15, 09:00)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-43945" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43945-form-container" class="comment-form-container">
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

