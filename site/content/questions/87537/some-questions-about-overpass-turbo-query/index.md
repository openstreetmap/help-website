+++
type = "question"
title = "Some questions about overpass-turbo query"
description = '''I&#x27;m trying to figure out the syntax of overpass-turbo query. I have found a couple of queries. One that ends with out body center qt: [out:json][timeout:600]; (  node[&quot;craft&quot;=&quot;window_construction&quot;];  way[&quot;craft&quot;=&quot;window_construction&quot;];  relation[&quot;craft&quot;=&quot;window_construction&quot;];  node[&quot;craft&quot;=&quot;carpent...'''
date = "2023-07-24T16:30:00Z"
lastmod = "2023-07-25T08:22:00Z"
weight = 87537
keywords = [ "query", "nodes", "syntax", "overpass-turbo", "tags" ]
aliases = [ "/questions/87537" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Some questions about overpass-turbo query](/questions/87537/some-questions-about-overpass-turbo-query)

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
<span id="post-87537-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87537-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87537-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to figure out the syntax of overpass-turbo query. I have found a couple of queries.</p>
<p>One that ends with <code>out body center qt</code>:</p>
<p><code>[out:json][timeout:600]; ( node["craft"="window_construction"]; way["craft"="window_construction"]; relation["craft"="window_construction"]; node["craft"="carpenter"]; way["craft"="carpenter"]; relation["craft"="carpenter"]; ); out body center qt;</code></p>
<p>And one that has <code>;&gt;</code> at the end of every row and that ends with <code>out skel qt</code>:</p>
<p><code>[out:json][timeout:600]; ( node["craft"="window_construction"];&gt;; way["craft"="window_construction"];&gt;; relation["craft"="window_construction"];&gt;; node["craft"="carpenter"];&gt;; way["craft"="carpenter"];&gt;; relation["craft"="carpenter"];&gt;; ); out skel qt;</code></p>
<p>It seems to produce the same output. Can you tell me what's the difference? And what does it change if I just end the query with just <code>out</code>?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-syntax" rel="tag" title="see questions tagged &#39;syntax&#39;">syntax</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jul '23, 16:30</strong></p>
<img src="https://secure.gravatar.com/avatar/50334ab2e351e4f5af1917f7f6ef8dc8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andreanovenove&#39;s gravatar image" />
<p><span>Andreanovenove</span><br />
<span class="score" title="126 reputation points">126</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andreanovenove has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jul '23, 16:31</strong> </span></p>
</div>
</div>
<div id="comments-container-87537" class="comments-container">
&#10;</div>
<div id="comment-tools-87537" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87537-form-container" class="comment-form-container">
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

<span id="87542"></span>

<div id="answer-container-87542" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87542-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87542-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87542-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The documentation for the <code>out</code> statement is <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#out">here</a>. I think in the second output all the tags are missing.</p>
<p>the <code>&gt;</code> <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_down_(%3E)">is meant</a> to recurse down to get e.g. nodes for all ways. I have never seen this used at the end of every line of a set of queries being aggregated. A more typical use might be the one used in the equivalent Query Wizard output:</p>
<pre><code>/*
This has been generated by the overpass-turbo wizard.
The original search was:
“craft=window_construction OR craft=carpenter”
*/
[out:json][timeout:25];
// gather results
(
  // query part for: “craft=window_construction”
  node[&quot;craft&quot;=&quot;window_construction&quot;]({{bbox}});
  way[&quot;craft&quot;=&quot;window_construction&quot;]({{bbox}});
  relation[&quot;craft&quot;=&quot;window_construction&quot;]({{bbox}});
  // query part for: “craft=carpenter”
  node[&quot;craft&quot;=&quot;carpenter&quot;]({{bbox}});
  way[&quot;craft&quot;=&quot;carpenter&quot;]({{bbox}});
  relation[&quot;craft&quot;=&quot;carpenter&quot;]({{bbox}});
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jul '23, 23:42</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-87542" class="comments-container">
<span id="87543"></span>
<div id="comment-87543" class="comment">
<div id="post-87543-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your reply. Can you tell me why you said in the second query all the tags are missing? Why is there a double <code>out</code> in the wizard query you posted?</p>
</div>
<div id="comment-87543-info" class="comment-info">
<span class="comment-age">(25 Jul '23, 08:22)</span> <span class="comment-user userinfo">Andreanovenove</span>
</div>
</div>
</div>
<div id="comment-tools-87542" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87542-form-container" class="comment-form-container">
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

