+++
type = "question"
title = "Overpass QL: How to get nodes that are member of certain ways?"
description = '''Hey guys, Another Overpass QL question. I&#x27;m using Overpass Turbo and trying to realise the following query:  General: I&#x27;m trying to get nodes with a certain tag if there are member of a certain way. Excplicit: I want all nodes that have the tag barrier=lift_gate and are on ways that are highway=livi...'''
date = "2015-01-03T22:18:00Z"
lastmod = "2015-01-04T13:35:00Z"
weight = 40001
keywords = [ "overpass-turbo", "overpass-ql" ]
aliases = [ "/questions/40001" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass QL: How to get nodes that are member of certain ways?](/questions/40001/overpass-ql-how-to-get-nodes-that-are-member-of-certain-ways)

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
<span id="post-40001-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40001-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-40001-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey guys,</p>
<p>Another Overpass QL question. I'm using Overpass Turbo and trying to realise the following query:</p>
<p><strong>General</strong>:</p>
<p>I'm trying to get nodes with a certain tag if there are member of a certain way.</p>
<p><strong>Excplicit</strong>:</p>
<p>I want all nodes that have the tag <code>barrier=lift_gate</code> and are on ways that are <code>highway=living_street</code> or <code>highway=residential</code>.</p>
<p>Here's a first try on Overpass Turbo. I got all nodes and used recurse up to get the corresponding ways. But how do i filter them?</p>
<pre><code>[out:json][timeout:25];
(
node[&quot;barrier&quot;=&quot;lift_gate&quot;]({{bbox}});
&lt;;
);
&#10;out body;
&gt;;
out skel qt;</code></pre>
<p>Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jan '15, 22:18</strong></p>
<img src="https://secure.gravatar.com/avatar/7ec5c174de466f97a699757f71dc398b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kerosin&#39;s gravatar image" />
<p><span>kerosin</span><br />
<span class="score" title="411 reputation points">411</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kerosin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-40001" class="comments-container">
&#10;</div>
<div id="comment-tools-40001" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40001-form-container" class="comment-form-container">
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

<span id="40009"></span>

<div id="answer-container-40009" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40009-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40009-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-40009-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kerosin has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I will use a slightly different approach here: as a first step, we search for all relevant ways in a bbox, then determine all nodes belonging to those ways and eventually filter nodes we're interested in:</p>
<pre><code>[bbox:{{bbox}}];
way[highway~&quot;^(living_street|residential)$&quot;];
node(w)[barrier=lift_gate];
out meta;</code></pre>
<p><a href="http://overpass-turbo.eu/s/6P7">http://overpass-turbo.eu/s/6P7</a></p>
<p>See <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_.28n.2C_w.2C_r.2C_bn.2C_bw.2C_br.29">documentation</a> for details.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jan '15, 09:01</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jan '15, 09:28</strong> </span></p>
</div>
</div>
<div id="comments-container-40009" class="comments-container">
<span id="40012"></span>
<div id="comment-40012" class="comment">
<div id="post-40012-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Okay, thank you very much! I thought the approach of getting all ways first might be too inefficient. Another question, trying to extend your code: I got all nodes (barrier=lift_gate) that are a part of a set of highways (residential+living_street). Is it possible to ask if they are not connected to another type of street (track,service etc)? Mostly the type of highway changes on a barrier node (e.g. way with highway=residential|node with barrier=lift_gate|way with highway=service). I only want to get nodes that are connected on both ends with the same set of highways.</p>
</div>
<div id="comment-40012-info" class="comment-info">
<span class="comment-age">(04 Jan '15, 11:23)</span> <span class="comment-user userinfo">kerosin</span>
</div>
</div>
<span id="40013"></span>
<div id="comment-40013" class="comment">
<div id="post-40013-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>meta: <a href="https://help.openstreetmap.org/users/1228/kerosin"></a><a href="https://help.openstreetmap.org/users/1228/kerosin">@kerosin</a>: I am not sure, but I think this might be suitable for a new question (e.g. "how to remove nodes from a set which are connected to two differently tagged ways"). This would help others having the same question more.</p>
</div>
<div id="comment-40013-info" class="comment-info">
<span class="comment-age">(04 Jan '15, 11:42)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="40014"></span>
<div id="comment-40014" class="comment">
<div id="post-40014-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/1228/kerosin"></a><a href="https://help.openstreetmap.org/users/1228/kerosin">@kerosin</a>: sure that's possible: Compare <a href="http://overpass-turbo.eu/s/6Pv">http://overpass-turbo.eu/s/6Pv</a> vs <a href="http://overpass-turbo.eu/s/6Pu">http://overpass-turbo.eu/s/6Pu</a> . Will you create a new question?</p>
</div>
<div id="comment-40014-info" class="comment-info">
<span class="comment-age">(04 Jan '15, 11:52)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="40021"></span>
<div id="comment-40021" class="comment">
<div id="post-40021-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okay, thanks for suggestions and the overpass query :) Of course I will post a new question for others!</p>
</div>
<div id="comment-40021-info" class="comment-info">
<span class="comment-age">(04 Jan '15, 13:35)</span> <span class="comment-user userinfo">kerosin</span>
</div>
</div>
</div>
<div id="comment-tools-40009" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40009-form-container" class="comment-form-container">
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

