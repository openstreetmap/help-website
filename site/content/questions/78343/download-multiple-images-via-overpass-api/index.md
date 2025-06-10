+++
type = "question"
title = "Download multiple images via overpass API"
description = '''Hello, What is the way to download shape data centered around the given longitude and latitude coordinates (for example 1000 images from 1000 different locations)? Is there a way to automate that process in python using overpy? I am new in this field, therefore each advice would be helpful. '''
date = "2021-01-13T23:24:00Z"
lastmod = "2021-01-14T01:40:00Z"
weight = 78343
keywords = [ "download", "overpy", "shape", "data" ]
aliases = [ "/questions/78343" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Download multiple images via overpass API](/questions/78343/download-multiple-images-via-overpass-api)

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
<span id="post-78343-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78343-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78343-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>What is the way to download shape data centered around the given longitude and latitude coordinates (for example 1000 images from 1000 different locations)? Is there a way to automate that process in python using overpy? I am new in this field, therefore each advice would be helpful.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-overpy" rel="tag" title="see questions tagged &#39;overpy&#39;">overpy</span> <span class="post-tag tag-link-shape" rel="tag" title="see questions tagged &#39;shape&#39;">shape</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jan '21, 23:24</strong></p>
<img src="https://secure.gravatar.com/avatar/ef2aa845a8e784f7b8ee09ea4a715c94?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Miki450&#39;s gravatar image" />
<p><span>Miki450</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Miki450 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78343" class="comments-container">
&#10;</div>
<div id="comment-tools-78343" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78343-form-container" class="comment-form-container">
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

<span id="78344"></span>

<div id="answer-container-78344" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78344-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78344-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78344-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is an extremely broad question and more about Python (and scripting/programming in general) than about OpenStreetMap or Overpass-API.</p>
<p>Also, beware that Overpass-API doesn't return images, it returns OpenStreetMap data in a relatively raw form.</p>
<p>In general, you'd figure out how to process one location and then wrap that in some logic to repeat it for each location you are interested in, possibly with some rate limiting to ensure that you are respecting the <a href="https://dev.overpass-api.de/overpass-doc/en/preface/commons.html">resource limits</a> of the servers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jan '21, 01:40</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-78344" class="comments-container">
&#10;</div>
<div id="comment-tools-78344" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78344-form-container" class="comment-form-container">
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

