+++
type = "question"
title = "Find top 10 places furthest away from any any road/building/structure using Overpass QL"
description = '''I am trying to find the &#x27;remotest&#x27; places in Denmark using Overpass QL. How do I construct a query that will show me the 10 places furthest from any &#x27;civilization&#x27; or man-made structure?'''
date = "2022-01-31T06:22:00Z"
lastmod = "2023-03-31T21:09:00Z"
weight = 83273
keywords = [ "overpass", "overpass-turbo", "overpass-ql" ]
aliases = [ "/questions/83273" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Find top 10 places furthest away from any any road/building/structure using Overpass QL](/questions/83273/find-top-10-places-furthest-away-from-any-any-roadbuildingstructure-using-overpass-ql)

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
<span id="post-83273-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83273-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83273-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to find the 'remotest' places in Denmark using Overpass QL.</p>
<p>How do I construct a query that will show me the 10 places furthest from any 'civilization' or man-made structure?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Jan '22, 06:22</strong></p>
<img src="https://secure.gravatar.com/avatar/85e8d762cefef7779d8fa047523b0cea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eowhvad&#39;s gravatar image" />
<p><span>eowhvad</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eowhvad has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83273" class="comments-container">
&#10;</div>
<div id="comment-tools-83273" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83273-form-container" class="comment-form-container">
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

<span id="87035"></span>

<div id="answer-container-87035" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87035-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87035-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87035-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Working from the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example#Banks_far_away_from_police_stations">example in the Overpass example page</a> (which shows how to find banks that are far from police stations), came up with this. It's not exactly what you were after, but with a year with no answers, perhaps it's of some use :)</p>
<p>It looks for nodes or ways (address points or buildings with an assigned address) that are further than some distance from any road (highway=*). I used this criteria, as looking for other buildings could easily miss many cases where two buildings are very isolated from everything else. "Man-made structure" can also be pretty vague, as maybe there's some abandoned water tower, fence or anything else. In any case, both of the blocks can be expanded as needed, to include specific types of road or adapt what the "places" are.</p>
<pre><code>[out:json][bbox:{{bbox}}][timeout:800];
&#10;(
  node[&quot;addr:housename&quot;];
  way[&quot;addr:housename&quot;];
)-&gt;.housenames;
&#10;( 
  way[highway];
)-&gt;.roads;
&#10;(
  node.housenames(around.roads:1000);
  way.housenames(around.roads:1000);
)-&gt;.namesNearRoads;
&#10;(.housenames; - .namesNearRoads;);
&#10;out geom meta;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Mar '23, 21:09</strong></p>
<img src="https://secure.gravatar.com/avatar/ba4d3e91f235ed21dacc1766b94e26a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richlv&#39;s gravatar image" />
<p><span>Richlv</span><br />
<span class="score" title="1740 reputation points"><span>1.7k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richlv has 5 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-87035" class="comments-container">
&#10;</div>
<div id="comment-tools-87035" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87035-form-container" class="comment-form-container">
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

