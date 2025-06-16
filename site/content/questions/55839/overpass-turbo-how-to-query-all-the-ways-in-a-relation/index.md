+++
type = "question"
title = "overpass turbo : how to query all the ways in a relation"
description = '''I&#x27;m trying to query the Great Lakes in overpass using the id (https://www.openstreetmap.org/relation/1124369)...is this plausible? Here is what I have so far. [out:json][timeout:2500];  ( relation[&quot;name&quot;=&quot;Great Lakes&quot;][ref=1124369]; way(r); node(w); );  out skel qt; '''
date = "2017-04-25T00:54:00Z"
lastmod = "2017-04-26T22:03:00Z"
weight = 55839
keywords = [ "lakesuperior", "super-relations", "relations" ]
aliases = [ "/questions/55839" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [overpass turbo : how to query all the ways in a relation](/questions/55839/overpass-turbo-how-to-query-all-the-ways-in-a-relation)

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
<span id="post-55839-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55839-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55839-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to query the Great Lakes in overpass using the id (<a href="https://www.openstreetmap.org/relation/1124369)...is">https://www.openstreetmap.org/relation/1124369)...is</a> this plausible?</p>
<p>Here is what I have so far.</p>
<pre><code>[out:json][timeout:2500];
&#10;(   relation[&quot;name&quot;=&quot;Great Lakes&quot;][ref=1124369];   way(r);   node(w); );
&#10;out skel qt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-lakesuperior" rel="tag" title="see questions tagged &#39;lakesuperior&#39;">lakesuperior</span> <span class="post-tag tag-link-super-relations" rel="tag" title="see questions tagged &#39;super-relations&#39;">super-relations</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Apr '17, 00:54</strong></p>
<img src="https://secure.gravatar.com/avatar/d8301f4449cd62755a06bd46e11db349?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="goldfishinriver&#39;s gravatar image" />
<p><span>goldfishinriver</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="goldfishinriver has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55839" class="comments-container">
&#10;</div>
<div id="comment-tools-55839" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55839-form-container" class="comment-form-container">
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

<span id="55842"></span>

<div id="answer-container-55842" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55842-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55842-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-55842-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="goldfishinriver has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To query by OSM id, do something like <code>rel(1124369);</code></p>
<p>Once you have that object you need to use the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_down_relations_.28.3E.3E.29">recurse down relations</a> operator:</p>
<pre><code>[out:json][timeout:25];
rel(1124369);
(._;&gt;&gt;;);
out;</code></pre>
<p>It's about 90 megabytes of data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Apr '17, 01:51</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-55842" class="comments-container">
<span id="55900"></span>
<div id="comment-55900" class="comment">
<div id="post-55900-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! Worked great!</p>
</div>
<div id="comment-55900-info" class="comment-info">
<span class="comment-age">(26 Apr '17, 22:03)</span> <span class="comment-user userinfo">goldfishinriver</span>
</div>
</div>
</div>
<div id="comment-tools-55842" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55842-form-container" class="comment-form-container">
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

