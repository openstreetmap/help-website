+++
type = "question"
title = "How to request a limited no of features in Overpass api?"
description = '''I am using Overpass api to query Building data from OpenStreetMap. the query string is like this  (way[building](bbox);node(w););out body;  This works really fine (the bounding box is specified by Openlayers). Now i want to improve it, such that only 10 buildings are returned by the query, to speed ...'''
date = "2013-03-04T05:13:00Z"
lastmod = "2014-09-11T13:21:00Z"
weight = 20472
keywords = [ "building", "overpass", "api", "openlayers", "speed" ]
aliases = [ "/questions/20472" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to request a limited no of features in Overpass api?](/questions/20472/how-to-request-a-limited-no-of-features-in-overpass-api)

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
<span id="post-20472-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20472-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-20472-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using Overpass api to query Building data from OpenStreetMap. the query string is like this</p>
<pre><code>(way[building](bbox);node(w););out body;</code></pre>
<p>This works really fine (the bounding box is specified by Openlayers).</p>
<p>Now i want to improve it, such that only 10 buildings are returned by the query, to speed up the process. For this i used the query</p>
<pre><code>(way[building](bbox);node(w););out 10;</code></pre>
<p>but doing this returns only 10 nodes <a href="http://overpass-turbo.eu/?Q=%28%0A%20%20way%28%7B%7Bbbox%7D%7D%29%5Bbuilding%5D;%0A%20%20node%28w%29;%0A%20%20%29;%0Aout%2010;&amp;C=27.7281;85.30042;18&amp;R">like here</a></p>
<p>What i want is 10 buildings.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-speed" rel="tag" title="see questions tagged &#39;speed&#39;">speed</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Mar '13, 05:13</strong></p>
<img src="https://secure.gravatar.com/avatar/651103e616e49724bb139f1a3e0a1a39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amritkarma&#39;s gravatar image" />
<p><span>amritkarma</span><br />
<span class="score" title="684 reputation points">684</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amritkarma has one accepted answer">11%</span></p>
</div>
</div>
<div id="comments-container-20472" class="comments-container">
<span id="36764"></span>
<div id="comment-36764" class="comment">
<div id="post-36764-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Updated Sep 2014 due to new available features</p>
</div>
<div id="comment-36764-info" class="comment-info">
<span class="comment-age">(11 Sep '14, 13:21)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-20472" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20472-form-container" class="comment-form-container">
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

<span id="20474"></span>

<div id="answer-container-20474" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20474-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20474-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-20474-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="amritkarma has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm sorry, this is not feasible yet. I'll add it to the list of suggested features.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '13, 07:07</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-20474" class="comments-container">
&#10;</div>
<div id="comment-tools-20474" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20474-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="36763"></span>

<div id="answer-container-36763" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36763-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36763-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-36763-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the meantime this is now possible by using the new geometry feature:</p>
<pre><code>way({{bbox}})[building];
out geom meta 10;</code></pre>
<p>It will display exactly 10 buildings.</p>
<p>Note that there's a small rendering issue in overpass turbo at this time, as only the boundary box is shown. However, as the geometry feature is rather new, I'm sure the rendering will be ok pretty soon. This has no impact on the query itself, though.</p>
<p>Try on Overpass Turbo: <a href="http://overpass-turbo.eu/s/50g">http://overpass-turbo.eu/s/50g</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Sep '14, 13:20</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Sep '14, 13:30</strong> </span></p>
</div>
</div>
<div id="comments-container-36763" class="comments-container">
&#10;</div>
<div id="comment-tools-36763" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36763-form-container" class="comment-form-container">
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

