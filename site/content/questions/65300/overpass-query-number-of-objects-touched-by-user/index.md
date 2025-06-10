+++
type = "question"
title = "Overpass query number of objects touched by user"
description = '''Is it possible to build a query that just returns the number of objects of a certain type in a certain area? Possible use case: define some things that require local knowledge, run query, get a toplist of people who have been working on those things. Find local mappers! (you could even query only th...'''
date = "2018-08-13T14:33:00Z"
lastmod = "2018-08-15T13:31:00Z"
weight = 65300
keywords = [ "overpass", "overpass-turbo" ]
aliases = [ "/questions/65300" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass query number of objects touched by user](/questions/65300/overpass-query-number-of-objects-touched-by-user)

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
<span id="post-65300-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65300-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-65300-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to build a query that just returns the number of objects of a certain type in a certain area? Possible use case: define some things that require local knowledge, run query, get a toplist of people who have been working on those things. Find local mappers! (you could even query only things that are at version 1 to have higher probability that it's original mapping) I didn't get further than this: <a href="http://overpass-turbo.eu/s/B12">http://overpass-turbo.eu/s/B12</a></p>
<p>Also: is this much heavier for the servers than running the query and doing the counting client-side?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Aug '18, 14:33</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-65300" class="comments-container">
<span id="65322"></span>
<div id="comment-65322" class="comment">
<div id="post-65322-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It may be possible with some of the newer features. You can see similar queries (in that they group a result set and do some statistics on it) described at <a href="https://dev.overpass-api.de/blog/sliced_time_and_space.html">https://dev.overpass-api.de/blog/sliced_time_and_space.html</a>.</p>
<p>I'm not certain it is possible to get the new <code>for</code> block to loop over users though.</p>
</div>
<div id="comment-65322-info" class="comment-info">
<span class="comment-age">(14 Aug '18, 11:30)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="65323"></span>
<div id="comment-65323" class="comment">
<div id="post-65323-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's going to be at least an interesting read. Thanks! (I'll report back here if I make progress)</p>
</div>
<div id="comment-65323-info" class="comment-info">
<span class="comment-age">(14 Aug '18, 11:37)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
</div>
<div id="comment-tools-65300" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65300-form-container" class="comment-form-container">
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

<span id="65364"></span>

<div id="answer-container-65364" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65364-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65364-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-65364-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="joost schouppe has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>So the for loop <a href="http://overpass-turbo.eu/s/B4i">does work on user</a>:</p>
<pre><code>[out:csv(user,total,nodes,ways,relations)][timeout:25];
{{geocodeArea:Antwerpen}}-&gt;.searchArea;
(
  way[&quot;building&quot;=&quot;hotel&quot;](area.searchArea);
  relation[&quot;building&quot;=&quot;hotel&quot;](area.searchArea);
  node[&quot;tourism&quot;=&quot;hotel&quot;](area.searchArea);
  way[&quot;tourism&quot;=&quot;hotel&quot;](area.searchArea);
  relation[&quot;tourism&quot;=&quot;hotel&quot;](area.searchArea);
);
for (user()){
    make stat 
     &quot;user&quot;=_.val,
     nodes=count(nodes),
     ways=count(ways),
     relations=count(relations),
     total = count(nodes) + count(ways) + count(relations);
    out;
};</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Aug '18, 13:31</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-65364" class="comments-container">
&#10;</div>
<div id="comment-tools-65364" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65364-form-container" class="comment-form-container">
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

