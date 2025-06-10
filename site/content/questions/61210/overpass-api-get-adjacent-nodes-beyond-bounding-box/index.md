+++
type = "question"
title = "Overpass API: get adjacent nodes beyond bounding box?"
description = '''I&#x27;m using Overpass QL to retrieve data for a bounding box (about 2 km square). I&#x27;d like to get:  all the nodes, ways, and rels within the box all the ways and rels that reference these items nearby nodes on included ways, for rendering  Currently, my request looks like this:  [bbox:...];  ( node; wa...'''
date = "2017-12-16T00:55:00Z"
lastmod = "2017-12-16T04:49:00Z"
weight = 61210
keywords = [ "bounding", "recurse", "overpass-ql" ]
aliases = [ "/questions/61210" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API: get adjacent nodes beyond bounding box?](/questions/61210/overpass-api-get-adjacent-nodes-beyond-bounding-box)

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
<span id="post-61210-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61210-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61210-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm using Overpass QL to retrieve data for a bounding box (about 2 km square). I'd like to get:</p>
<ul>
<li>all the nodes, ways, and rels within the box</li>
<li>all the ways and rels that reference these items</li>
<li>nearby nodes on included ways, for rendering</li>
</ul>
<p>Currently, my request looks like this:</p>
<pre><code>  [bbox:...];
  ( node; way; rel; );
  ( ._; &lt;&lt;; ); out;</code></pre>
<p>This mostly works, but it doesn't give me nearby nodes on included ways, if the nodes are outside the box. So, for example, I can't draw the path the freeway takes heading out of the box. I'm afraid to use the &gt;&gt; operator, however, lest I get inundated by data (eg, every node on Interstate 10 :-). I could make my bounding box larger and clip the results, but that seems wasteful.</p>
<p>Comments, clues, suggestions?</p>
<p>-r</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bounding" rel="tag" title="see questions tagged &#39;bounding&#39;">bounding</span> <span class="post-tag tag-link-recurse" rel="tag" title="see questions tagged &#39;recurse&#39;">recurse</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Dec '17, 00:55</strong></p>
<img src="https://secure.gravatar.com/avatar/d4d28bd014f9e7324bad99dcc3b0d390?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rich_Morin&#39;s gravatar image" />
<p><span>Rich_Morin</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rich_Morin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61210" class="comments-container">
&#10;</div>
<div id="comment-tools-61210" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61210-form-container" class="comment-form-container">
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

<span id="61211"></span>

<div id="answer-container-61211" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61211-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61211-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61211-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As a workaround, I'm currently using a pair of bounding boxes, as follows:</p>
<ul>
<li>Use the "real" bounding box (b1) to get nodes, rels, and ways.</li>
<li>Recurse upward to get referencing rels and ways.</li>
<li>Fold in nodes from a slightly larger bounding box (b2).</li>
</ul>
<p>Making b2 20% wider and taller than b1 produces clean results, at the cost of downloading about 30% more data. Currently, my request looks something like this:</p>
<pre><code>( node(b1); way(b1); rel(b1); );
( ._; &lt;&lt;; node(b2); ); out;</code></pre>
<p>Still hoping for a cleaner solution...</p>
<p>-r</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Dec '17, 04:49</strong></p>
<img src="https://secure.gravatar.com/avatar/d4d28bd014f9e7324bad99dcc3b0d390?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rich_Morin&#39;s gravatar image" />
<p><span>Rich_Morin</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rich_Morin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61211" class="comments-container">
&#10;</div>
<div id="comment-tools-61211" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61211-form-container" class="comment-form-container">
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

