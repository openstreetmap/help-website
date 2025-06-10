+++
type = "question"
title = "overpass: stats per value"
description = '''I&#x27;d like to generate some statistics about the members of a relation. This is as far as I&#x27;ve gotten: [out:csv(number,length)][timeout:25]; (  relation(id:3121667)-&amp;gt;.groute; ); way(r.groute); make stat number=count(ways),length=sum(length()); out;  Now, I would like to have a row in the CSV for ev...'''
date = "2020-12-15T12:32:00Z"
lastmod = "2020-12-15T13:24:00Z"
weight = 77931
keywords = [ "stats", "overpass-turbo" ]
aliases = [ "/questions/77931" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [overpass: stats per value](/questions/77931/overpass-stats-per-value)

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
<span id="post-77931-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77931-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77931-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'd like to generate some statistics about the members of a relation. This is as far as I've gotten:</p>
<pre><code>[out:csv(number,length)][timeout:25];
(
  relation(id:3121667)-&gt;.groute;
);
way(r.groute);
make stat number=count(ways),length=sum(length());
out;</code></pre>
<p>Now, I would like to have a row in the CSV for every unique combination of highway and surface. So for example the total length of secondary - asphalt roads in this relation. I looked at the API doc and the examples, but I really don't see how</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-stats" rel="tag" title="see questions tagged &#39;stats&#39;">stats</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Dec '20, 12:32</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-77931" class="comments-container">
&#10;</div>
<div id="comment-tools-77931" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77931-form-container" class="comment-form-container">
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

<span id="77935"></span>

<div id="answer-container-77935" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77935-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77935-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-77935-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="joost schouppe has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<pre><code>[out:csv(highway,surface,number,length)][timeout:25];
relation(id:3121667)-&gt;.groute;
way(r.groute);
&#10;for-&gt;.hw (t[&quot;highway&quot;]) {
  for.hw (t[&quot;surface&quot;]) {
    make stat highway=hw.val, surface=_.val, number=count(ways), length=sum(length());
    out;
  }
}</code></pre>
<p>This was a great help to figure out <code>for</code> loops and how to access the tags we're grouping by (<code>hw.val</code> and <code>_.val</code>): <a href="https://dev.overpass-api.de/blog/loop_and_group.html">https://dev.overpass-api.de/blog/loop_and_group.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Dec '20, 13:24</strong></p>
<img src="https://secure.gravatar.com/avatar/23463b99b62a72f26ed677cc556c44e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="M1dgard&#39;s gravatar image" />
<p><span>M1dgard</span><br />
<span class="score" title="156 reputation points">156</span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="M1dgard has one accepted answer">16%</span></p>
</div>
</div>
<div id="comments-container-77935" class="comments-container">
&#10;</div>
<div id="comment-tools-77935" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77935-form-container" class="comment-form-container">
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

