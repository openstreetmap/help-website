+++
type = "question"
title = "Proximity search - node with tag1 near node with tag2"
description = '''Is there a way to search for a node situated within a given distance from at least one other node with a given tag? Applications:  find benches near a body of water (seriously) brothel near police (for fun) swingerclub near place_of_worship stripclub near kindergarten '''
date = "2014-05-12T03:05:00Z"
lastmod = "2014-05-12T07:56:00Z"
weight = 33089
keywords = [ "query", "search", "nodes", "distance" ]
aliases = [ "/questions/33089" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Proximity search - node with tag1 near node with tag2](/questions/33089/proximity-search-node-with-tag1-near-node-with-tag2)

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
<span id="post-33089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33089-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-33089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
3
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to search for a node situated within a given distance from at least one other node with a given tag?</p>
<p>Applications:</p>
<ul>
<li>find benches near a body of water (seriously)</li>
<li><a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dbrothel">brothel</a> near <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dpolice">police</a> (for fun)</li>
<li><a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dswingerclub">swingerclub</a> near <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dplace_of_worship">place_of_worship</a></li>
<li><a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dstripclub">stripclub</a> near <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dkindergarten">kindergarten</a></li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 May '14, 03:05</strong></p>
<img src="https://secure.gravatar.com/avatar/fb5e3a539b1e23c54b080b6d12b411c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dandv&#39;s gravatar image" />
<p><span>dandv</span><br />
<span class="score" title="401 reputation points">401</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dandv has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 May '14, 03:17</strong> </span></p>
</div>
</div>
<div id="comments-container-33089" class="comments-container">
<span id="33095"></span>
<div id="comment-33095" class="comment">
<div id="post-33095-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Uh, those examples are ...</p>
</div>
<div id="comment-33095-info" class="comment-info">
<span class="comment-age">(12 May '14, 07:56)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-33089" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33089-form-container" class="comment-form-container">
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

<span id="33091"></span>

<div id="answer-container-33091" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33091-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33091-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-33091-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thankfully, the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API#Around">Overpass API supports an <code>around</code> operator</a>. One needs to be careful with queries that return many nodes, and the query likely to return the fewest nodes should be first. Bounding boxes help.</p>
<p>Here's an example for the second query:</p>
<pre><code>&lt;query type=&quot;node&quot;&gt;
  &lt;has-kv k=&quot;amenity&quot; v=&quot;brothel&quot;/&gt;
  &lt;bbox-query {{bbox}}/&gt;
&lt;/query&gt;
&lt;query type=&quot;node&quot;&gt;
  &lt;around radius=&quot;1000&quot;/&gt;
  &lt;has-kv k=&quot;amenity&quot; v=&quot;police&quot;/&gt;
&lt;/query&gt;
&#10;&lt;print/&gt;</code></pre>
<p>You can see it <a href="http://overpass-turbo.eu/s/3lE">live for Berlin</a>:</p>
<p><img src="/upfiles/brothels_near_police_in_Berlin.png" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 May '14, 05:04</strong></p>
<img src="https://secure.gravatar.com/avatar/fb5e3a539b1e23c54b080b6d12b411c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dandv&#39;s gravatar image" />
<p><span>dandv</span><br />
<span class="score" title="401 reputation points">401</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dandv has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-33091" class="comments-container">
&#10;</div>
<div id="comment-tools-33091" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33091-form-container" class="comment-form-container">
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

