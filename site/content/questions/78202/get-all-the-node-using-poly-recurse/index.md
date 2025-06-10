+++
type = "question"
title = "get all the node using poly Recurse"
description = '''hi I&#x27;m using overpass turbo and im trying to get all the node in this bounded box using recurse poly I tried this code  //[out:json][timeout:25][bbox:40.73112,-73.89061,40.73391,-73.88807]; way(poly:&quot;40.73112,-73.89061,40.73391,-73.88807&quot;) node(w); out center;  but it gives me an error how can I sol...'''
date = "2021-01-03T07:23:00Z"
lastmod = "2021-01-03T14:34:00Z"
weight = 78202
keywords = [ "openstreetmap", "overpass" ]
aliases = [ "/questions/78202" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [get all the node using poly Recurse](/questions/78202/get-all-the-node-using-poly-recurse)

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
<span id="post-78202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78202-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hi I'm using overpass turbo and im trying to get all the node in this bounded box using recurse poly I tried this code</p>
<pre><code>//[out:json][timeout:25][bbox:40.73112,-73.89061,40.73391,-73.88807];
way(poly:&quot;40.73112,-73.89061,40.73391,-73.88807&quot;)
node(w);
out center;</code></pre>
<p>but it gives me an error how can I solve it</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jan '21, 07:23</strong></p>
<img src="https://secure.gravatar.com/avatar/00b20ea2eb5708a716896e0d335050f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rabeeqasem&#39;s gravatar image" />
<p><span>rabeeqasem</span><br />
<span class="score" title="31 reputation points">31</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rabeeqasem has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78202" class="comments-container">
&#10;</div>
<div id="comment-tools-78202" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78202-form-container" class="comment-form-container">
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

<span id="78207"></span>

<div id="answer-container-78207" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78207-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78207-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78207-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rabeeqasem has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the future, when asking for help it is generally good to specify exactly what the error message is that you receive, rather than "it gives me an error".</p>
<p>You say you want to get all the nodes in a given bounding box.</p>
<p>The query to use for that would be</p>
<pre><code>node  (40.73112,-73.89061,40.73391,-73.88807);
out;</code></pre>
<p>No ways or recursion involved.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jan '21, 14:08</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-78207" class="comments-container">
&#10;</div>
<div id="comment-tools-78207" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78207-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78208"></span>

<div id="answer-container-78208" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78208-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78208-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78208-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your solution is provided in the error dialog: "at least 3 lat/lon float value pairs must be provided.", but you don't need it. If you want nodes of ways:</p>
<pre><code>[bbox:40.73112,-73.89061,40.73391,-73.88807];
way;
node(w);
out;</code></pre>
<p>Else use Fredrik's solution.</p>
<p>Plus you were missing a semicolon.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jan '21, 14:34</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-78208" class="comments-container">
&#10;</div>
<div id="comment-tools-78208" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78208-form-container" class="comment-form-container">
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

