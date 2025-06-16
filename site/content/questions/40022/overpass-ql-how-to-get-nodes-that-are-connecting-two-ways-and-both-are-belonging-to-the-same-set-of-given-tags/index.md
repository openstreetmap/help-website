+++
type = "question"
title = "Overpass QL: How to get nodes that are connecting two ways and both are belonging to the same set of given tags"
description = '''Hey, Another Overpass QL question. I&#x27;m using Overpass Turbo and trying to realise the following query: General: I&#x27;m trying to get nodes with a certain tag that are connecting two ways. The nodes should be filtered out, if both of these ways are not corresponding with a set of tags. So both ways can ...'''
date = "2015-01-04T13:50:00Z"
lastmod = "2015-01-05T00:52:00Z"
weight = 40022
keywords = [ "overpass-turbo", "overpass-ql" ]
aliases = [ "/questions/40022" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass QL: How to get nodes that are connecting two ways and both are belonging to the same set of given tags](/questions/40022/overpass-ql-how-to-get-nodes-that-are-connecting-two-ways-and-both-are-belonging-to-the-same-set-of-given-tags)

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
<span id="post-40022-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40022-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40022-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey,</p>
<p>Another Overpass QL question. I'm using Overpass Turbo and trying to realise the following query:</p>
<p><strong>General</strong>:</p>
<p>I'm trying to get nodes with a certain tag that are connecting two ways. The nodes should be filtered out, if both of these ways are not corresponding with a set of tags. So both ways can have unequal values of the same key, but have to be defined in the given set. Ways with the same tag shouldn't be discarded.</p>
<p><strong>Excplicit</strong>:</p>
<p>I want all nodes that have the tag <code>barrier=lift_gate</code>. These nodes should connect at least two ways, which are tagged as <code>highway=living_street</code> or <code>highway=residential</code>. (So that ways with tags like <code>highway=service</code> or <code>highway=track</code> should be discarded).</p>
<p>Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jan '15, 13:50</strong></p>
<img src="https://secure.gravatar.com/avatar/7ec5c174de466f97a699757f71dc398b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kerosin&#39;s gravatar image" />
<p><span>kerosin</span><br />
<span class="score" title="411 reputation points">411</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kerosin has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jan '15, 13:53</strong> </span></p>
</div>
</div>
<div id="comments-container-40022" class="comments-container">
&#10;</div>
<div id="comment-tools-40022" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40022-form-container" class="comment-form-container">
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

<span id="40025"></span>

<div id="answer-container-40025" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40025-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40025-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-40025-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kerosin has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Filtering based on counting something is outside of the scope of Overpass API (as of today), so a bit of post processing is required.</p>
<p>The closest way I could think of is the following: for each <code>barrier=lift_gate</code> node in a bbox, we first print the OSM node id, followed by the number of OSM ways, which are either living_street or residential. As an example, this query will return <a href="https://www.openstreetmap.org/node/304989602">node 304989602</a> with two connected ways. Your task would then be to filter out node ids with less than 2 ways, which could be done in Excel or LibreOffice.</p>
<pre><code>[out:csv(::id,::count)]
[bbox:{{bbox}}];
node[barrier=lift_gate];
foreach(
  out;  
  way(bn)[highway~&quot;^(living_street|residential)$&quot;];
  out count;
);</code></pre>
<p><a href="http://overpass-turbo.eu/s/6PS">http://overpass-turbo.eu/s/6PS</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jan '15, 18:07</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jan '15, 18:09</strong> </span></p>
</div>
</div>
<div id="comments-container-40025" class="comments-container">
<span id="40031"></span>
<div id="comment-40031" class="comment">
<div id="post-40031-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks again :) I said "at least two ways" and I meant two or more ways. I don't want to count the ways, so if it is problematic I would be very happy for a solution that simply gives all nodes with "barrier=lift_gate" and if there are ways that this node is connected to they should be part of the given set (residential/livingstreet) (should I open again a new question? ;)) A out of the box solution on Overpass would be really great! Anyway great work, I appreciate it!</p>
</div>
<div id="comment-40031-info" class="comment-info">
<span class="comment-age">(05 Jan '15, 00:52)</span> <span class="comment-user userinfo">kerosin</span>
</div>
</div>
</div>
<div id="comment-tools-40025" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40025-form-container" class="comment-form-container">
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

