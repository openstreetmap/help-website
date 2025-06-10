+++
type = "question"
title = "Problems counting bridges"
description = '''Hello, for a degree thesis I would like to carry out a census of Italian bridges with the data present from OpenStreetMap, which seem to me quite complete. I extracted the data with Overpass Turbo and then exported it to uMap. There are only two problems: 1) Many bridges are counted double because t...'''
date = "2023-01-02T13:05:00Z"
lastmod = "2023-01-02T13:46:00Z"
weight = 86414
keywords = [ "overpass", "italy", "overpass-turbo", "bridge" ]
aliases = [ "/questions/86414" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Problems counting bridges](/questions/86414/problems-counting-bridges)

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
<span id="post-86414-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86414-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86414-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, for a degree thesis I would like to carry out a census of Italian bridges with the data present from OpenStreetMap, which seem to me quite complete.</p>
<p>I extracted the data with Overpass Turbo and then exported it to uMap.</p>
<p>There are only two problems: 1) Many bridges are counted double because they are part of a two-way street. Is it possible to eliminate one of the two in the count? 2) By extracting the data province by province, the figures do not add up compared to a count made at the national level, because there are many bridges between one province and another. How can I delete duplicates?</p>
<p>Thanks to those who will answer me and happy new year. a</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-italy" rel="tag" title="see questions tagged &#39;italy&#39;">italy</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-bridge" rel="tag" title="see questions tagged &#39;bridge&#39;">bridge</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jan '23, 13:05</strong></p>
<img src="https://secure.gravatar.com/avatar/f5e6d7b17e803442c7f989ccabafa27d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fraccio&#39;s gravatar image" />
<p><span>Fraccio</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fraccio has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86414" class="comments-container">
<span id="86415"></span>
<div id="comment-86415" class="comment">
<div id="post-86415-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please post your routine</p>
</div>
<div id="comment-86415-info" class="comment-info">
<span class="comment-age">(02 Jan '23, 13:33)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-86414" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86414-form-container" class="comment-form-container">
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

<span id="86416"></span>

<div id="answer-container-86416" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86416-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86416-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86416-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<pre><code>/*
This has been generated by the overpass-turbo wizard.
The original search was:
“&quot;bridge&quot; is not null”
*/
[out:json][timeout:250];
// fetch area Italia” to search in
  {{geocodeArea:Italia}}-&gt;.searchArea;
// gather results
&#10;(
  // query part for: “bridge=*”
  node[&quot;bridge&quot;]({{bbox}})(area.searchArea);
  way[&quot;bridge&quot;]({{bbox}})(area.searchArea);
  relation[&quot;bridge&quot;]({{bbox}})(area.searchArea);
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jan '23, 13:46</strong></p>
<img src="https://secure.gravatar.com/avatar/f5e6d7b17e803442c7f989ccabafa27d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fraccio&#39;s gravatar image" />
<p><span>Fraccio</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fraccio has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86416" class="comments-container">
&#10;</div>
<div id="comment-tools-86416" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86416-form-container" class="comment-form-container">
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

