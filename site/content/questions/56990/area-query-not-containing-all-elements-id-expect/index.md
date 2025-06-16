+++
type = "question"
title = "area query not containing all elements I&#x27;d expect"
description = '''Hi everyone, I&#x27;m testing in Overpass Turbo with following command: [out:json]; (node[&quot;amenity&quot;=&quot;fast_food&quot;](area:3600062484); rel[&quot;amenity&quot;=&quot;fast_food&quot;](area:3600062484); way[&quot;amenity&quot;=&quot;fast_food&quot;](area:3600062484); ); out;  I do get results, but not all I&#x27;d expect from looking at the map. For examp...'''
date = "2017-07-10T13:49:00Z"
lastmod = "2017-07-10T20:50:00Z"
weight = 56990
keywords = [ "overpass", "api", "area" ]
aliases = [ "/questions/56990" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [area query not containing all elements I'd expect](/questions/56990/area-query-not-containing-all-elements-id-expect)

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
<span id="post-56990-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56990-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56990-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone,</p>
<p>I'm testing in Overpass Turbo with following command:</p>
<pre><code>[out:json];
(node[&quot;amenity&quot;=&quot;fast_food&quot;](area:3600062484);
rel[&quot;amenity&quot;=&quot;fast_food&quot;](area:3600062484);
way[&quot;amenity&quot;=&quot;fast_food&quot;](area:3600062484);
);
out;</code></pre>
<p>I do get results, but not all I'd expect from looking at the map. For example, I'd expect <a href="https://www.openstreetmap.org/node/1783787144">this node</a> - which fulfills the amenity fast_food condition - to be in the <a href="https://www.openstreetmap.org/relation/62484#map=11/48.5512/12.1516">area 3600062484</a> and therefore in the result set amongst others, which unfortunately it isn't.</p>
<p>What am I doing wrong?</p>
<p>Thankful for any help I can get here.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jul '17, 13:49</strong></p>
<img src="https://secure.gravatar.com/avatar/e784d5df54cdda12fd979efa7d9c0114?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robmso&#39;s gravatar image" />
<p><span>robmso</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robmso has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56990" class="comments-container">
&#10;</div>
<div id="comment-tools-56990" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56990-form-container" class="comment-form-container">
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

<span id="56999"></span>

<div id="answer-container-56999" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56999-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56999-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56999-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Running your query on the public overpass-turbo instance gives the expected results for me (Kebab TURM is returned).</p>
<p>I have a screen shot if necessary.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '17, 20:18</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-56999" class="comments-container">
<span id="57000"></span>
<div id="comment-57000" class="comment">
<div id="post-57000-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No need for a screen shot, I believe you - I just cannot replicate the result after testing again now. I assume by "the public overpass-turbo instance" you mean overpass-turbo.eu, which I also use (new to the topic in general, might be wrong here).</p>
<p>Interestingly, when I'm loading the same query as an URI against overpass-api.de ( <a href="http://overpass-api.de/api/interpreter?data=%5Bout:json%5D;(node">http://overpass-api.de/api/interpreter?data=[out:json];(node</a><span>%22amenity%22=%22fast_food%22</span>;rel<span>%22amenity%22=%22fast_food%22</span>;way<span>%22amenity%22=%22fast_food%22</span>;);out; ), I do get a more complete result, as it seems (contains the node used as example, at least).</p>
<p>Since I'll be using that way to access the data for my task, the behavior is acceptable to me - I just would have liked to test queries in Overpass Turbo and do not quite understand what makes my results different to e.g. yours.</p>
</div>
<div id="comment-57000-info" class="comment-info">
<span class="comment-age">(10 Jul '17, 20:33)</span> <span class="comment-user userinfo">robmso</span>
</div>
</div>
<span id="57001"></span>
<div id="comment-57001" class="comment">
<div id="post-57001-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes, overpass-turbo.eu</p>
<p>Really didn't do anything special, just a C&amp;P of your query and then "run".</p>
</div>
<div id="comment-57001-info" class="comment-info">
<span class="comment-age">(10 Jul '17, 20:50)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-56999" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56999-form-container" class="comment-form-container">
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

