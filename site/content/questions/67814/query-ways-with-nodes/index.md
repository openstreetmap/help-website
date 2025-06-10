+++
type = "question"
title = "Query Ways with Nodes"
description = '''I managed to select ways or nodes, but not both at the same time. I am wondering if it was not intended by Overpass QL?  What I got so far:  [out:csv(::id,::type, ::lat, ::lon,&quot;name&quot;, &quot;addr:street&quot;)];  area[name=&quot;Prenzlauer Berg&quot;][boundary=administrative]-&amp;gt;.prenzlauer_berg; (  way(area.prenzlauer...'''
date = "2019-01-30T14:44:00Z"
lastmod = "2019-01-31T10:29:00Z"
weight = 67814
keywords = [ "overpass", "overpass-ql" ]
aliases = [ "/questions/67814" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Query Ways with Nodes](/questions/67814/query-ways-with-nodes)

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
<span id="post-67814-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67814-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67814-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I managed to select ways or nodes, but not both at the same time. I am wondering if it was not intended by Overpass QL?</p>
<p>What I got so far:</p>
<pre><code>[out:csv(::id,::type, ::lat, ::lon,&quot;name&quot;, &quot;addr:street&quot;)]; 
area[name=&quot;Prenzlauer Berg&quot;][boundary=administrative]-&gt;.prenzlauer_berg;
(
  way(area.prenzlauer_berg)[~&quot;highway&quot;~&quot;.&quot;][name] ;     
  node(w);
)-&gt;.result_set;
out geom;</code></pre>
<p>I would like something like this as a result:</p>
<pre><code>way_id, way_name, node_id, position, ...
way1, some_name, node1, 0, ...
way1, some_name, node2, 1, ...
way2, some_name_ node3, 0, ..</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jan '19, 14:44</strong></p>
<img src="https://secure.gravatar.com/avatar/49f0c5218671e039c889fc520ea55a92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="np00&#39;s gravatar image" />
<p><span>np00</span><br />
<span class="score" title="51 reputation points">51</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="np00 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67814" class="comments-container">
&#10;</div>
<div id="comment-tools-67814" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67814-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="67816"></span>

<div id="answer-container-67816" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67816-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67816-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67816-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Without looking at it real closely I imagine the simplest thing is to ask Overpass-API for JSON and then transform that into the row format you want. I don't think there is a way to get it to emit a way line for each member node.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jan '19, 17:14</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-67816" class="comments-container">
&#10;</div>
<div id="comment-tools-67816" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67816-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="67819"></span>

<div id="answer-container-67819" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67819-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67819-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67819-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://help.openstreetmap.org/questions/45212/how-to-get-ways-and-associated-nodes-in-csv-with-overpass-ql">This earlier question may be relevant.</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jan '19, 10:29</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-67819" class="comments-container">
&#10;</div>
<div id="comment-tools-67819" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67819-form-container" class="comment-form-container">
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

