+++
type = "question"
title = "How to show certain nodes and aministrative geometry?"
description = '''How can I show nodes of a certain type such as http://overpass-turbo.eu/s/pt7 and at the same time show the boundary of its administrative level as shown in http://overpass-turbo.eu/s/pt5 For the administrative level, I only would like the outline, not a a filled polygonal. Thanks.'''
date = "2017-06-02T10:24:00Z"
lastmod = "2017-06-02T19:10:00Z"
weight = 56413
keywords = [ "overpass" ]
aliases = [ "/questions/56413" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to show certain nodes and aministrative geometry?](/questions/56413/how-to-show-certain-nodes-and-aministrative-geometry)

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
<span id="post-56413-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56413-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56413-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I show nodes of a certain type such as <a href="http://overpass-turbo.eu/s/pt7">http://overpass-turbo.eu/s/pt7</a> and at the same time show the boundary of its administrative level as shown in <a href="http://overpass-turbo.eu/s/pt5">http://overpass-turbo.eu/s/pt5</a> For the administrative level, I only would like the outline, not a a filled polygonal. Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jun '17, 10:24</strong></p>
<img src="https://secure.gravatar.com/avatar/1fb0d12cfde0dfa6aa364a5758928ea8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pander&#39;s gravatar image" />
<p><span>pander</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pander has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56413" class="comments-container">
&#10;</div>
<div id="comment-tools-56413" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56413-form-container" class="comment-form-container">
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

<span id="56422"></span>

<div id="answer-container-56422" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56422-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56422-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56422-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One way is to use the union operator in the Overpass language, grouping the queries before the out statement with parentheses.</p>
<p>For the queries you show, <a href="http://overpass-turbo.eu/s/pu5">multiple out statements is probably easier</a>:</p>
<pre><code>{{geocodeArea:&quot;Gemert-Bakel&quot;}}-&gt;.searchArea;
rel(pivot.searchArea);
way(r);
out body geom;
node[natural=tree](area.searchArea);
out;</code></pre>
<p>The <code>way(r)</code> line just retrieves the way members of the relation. It would probably be nicer to override the style for the relation but I'm not sure if that is possible.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jun '17, 19:10</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-56422" class="comments-container">
&#10;</div>
<div id="comment-tools-56422" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56422-form-container" class="comment-form-container">
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

