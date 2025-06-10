+++
type = "question"
title = "Overpass Turbo query for city/voivodeship/city hierarchy in poly"
description = '''Hey guys! I ask for a hint how to build a query that will provide me a poly of each city in voivodeship. Thanks!'''
date = "2021-06-18T10:52:00Z"
lastmod = "2021-06-24T12:13:00Z"
weight = 80616
keywords = [ "query", "cities", "overpass-turbo", "polygons" ]
aliases = [ "/questions/80616" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass Turbo query for city/voivodeship/city hierarchy in poly](/questions/80616/overpass-turbo-query-for-cityvoivodeshipcity-hierarchy-in-poly)

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
<span id="post-80616-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80616-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80616-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey guys!</p>
<p>I ask for a hint how to build a query that will provide me a poly of each city in voivodeship.</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-cities" rel="tag" title="see questions tagged &#39;cities&#39;">cities</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-polygons" rel="tag" title="see questions tagged &#39;polygons&#39;">polygons</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jun '21, 10:52</strong></p>
<img src="https://secure.gravatar.com/avatar/d1d8c7f084a62c78fb4b054c47e718ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="siemaeniownik&#39;s gravatar image" />
<p><span>siemaeniownik</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="siemaeniownik has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80616" class="comments-container">
&#10;</div>
<div id="comment-tools-80616" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80616-form-container" class="comment-form-container">
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

<span id="80685"></span>

<div id="answer-container-80685" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80685-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80685-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80685-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here is an example for municipalities in "Lower Silesian" in Poland:</p>
<pre><code>[out:json][timeout:120];
{{geocodeArea:Lower Silesian}}-&gt;.searchArea;
(
  relation[&quot;admin_level&quot;=&quot;7&quot;](area.searchArea);
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
<p>If the voivodeship has its municipalities or cities as ways instead of relations, just change "relation" to "way" in the code above.</p>
<p>If you really only want cities instead of municipalities, change the admin level from 7 to 8 (might time out). If you want this query for another country (you didn't specify), take a look at this table to see which admin level you need:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative">Tag:boundary=administrative</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jun '21, 12:13</strong></p>
<img src="https://secure.gravatar.com/avatar/ec46821d791b304a5c3c9380ab661d11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Discostu36&#39;s gravatar image" />
<p><span>Discostu36</span><br />
<span class="score" title="236 reputation points">236</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Discostu36 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80685" class="comments-container">
&#10;</div>
<div id="comment-tools-80685" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80685-form-container" class="comment-form-container">
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

