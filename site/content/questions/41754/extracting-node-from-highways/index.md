+++
type = "question"
title = "Extracting node from highways"
description = '''I am using overpas turbo to extract nodes from highways(=motorway). Below is the code that I am using. However, this code gives me all the nodes in the bounding box and does not filter the highways. [out:xml]; ( (way(39.90,32.83,39.96,32.89);)-&amp;gt;.a; ((way.a[&quot;highway&quot;=&quot;motorway&quot;]);)-&amp;gt;.b; ((way.a...'''
date = "2015-03-17T05:04:00Z"
lastmod = "2015-03-17T07:44:00Z"
weight = 41754
keywords = [ "overpass", "overpass-turbo", "highway" ]
aliases = [ "/questions/41754" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Extracting node from highways](/questions/41754/extracting-node-from-highways)

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
<span id="post-41754-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41754-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41754-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using overpas turbo to extract nodes from highways(=motorway). Below is the code that I am using. However, this code gives me all the nodes in the bounding box and does not filter the highways.</p>
<pre><code>[out:xml];
(
(way(39.90,32.83,39.96,32.89);)-&gt;.a;
((way.a[&quot;highway&quot;=&quot;motorway&quot;]);)-&gt;.b;
((way.a[&quot;highway&quot;=&quot;motorway_link&quot;]);)-&gt;.b;
);
(.b;&gt;;);
out body qt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Mar '15, 05:04</strong></p>
<img src="https://secure.gravatar.com/avatar/68d84633d5832a44cfc5f791b3746063?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Manish%20Bansal&#39;s gravatar image" />
<p><span>Manish Bansal</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Manish Bansal has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Mar '15, 05:12</strong> </span></p>
</div>
</div>
<div id="comments-container-41754" class="comments-container">
&#10;</div>
<div id="comment-tools-41754" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41754-form-container" class="comment-form-container">
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

<span id="41756"></span>

<div id="answer-container-41756" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41756-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41756-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-41756-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Manish Bansal has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You must specify the input set of the recuse down operator as well: <code>.b &gt;;</code>, otherwise it will recuse down the current default input set, which here is set by the outermost union parentheses.</p>
<p>Also: when you set the same output data set twice to the same variable (here: <code>-&gt;.b</code>), the former will be overridden by the latter. If you want to merge the results, you'd have to use an union: <code>(…)-&gt;.b;</code>. You can also combine a bbox and a tag query into one statement to get the query more concise: <code>way(&lt;bbox&gt;)[&lt;tag&gt;];</code>. In the end the query you are looking for could look like this: <a href="http://overpass-turbo.eu/s/8e0">http://overpass-turbo.eu/s/8e0</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Mar '15, 07:01</strong></p>
<img src="https://secure.gravatar.com/avatar/eca34689e074411e0daca0d994f532b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tyr_asd&#39;s gravatar image" />
<p><span>tyr_asd</span><br />
<span class="score" title="1196 reputation points"><span>1.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tyr_asd has 11 accepted answers">64%</span></p>
</div>
</div>
<div id="comments-container-41756" class="comments-container">
<span id="41757"></span>
<div id="comment-41757" class="comment">
<div id="post-41757-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much for your help.</p>
</div>
<div id="comment-41757-info" class="comment-info">
<span class="comment-age">(17 Mar '15, 07:44)</span> <span class="comment-user userinfo">Manish Bansal</span>
</div>
</div>
</div>
<div id="comment-tools-41756" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41756-form-container" class="comment-form-container">
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

