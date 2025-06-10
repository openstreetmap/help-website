+++
type = "question"
title = "Osmium - filter by bounding box"
description = '''Hi there, I am wondering if Osmium would be a good tool to use to filter by bounding box? I had a poke around in the documentation but it seems more geared up for tag filtering and I could not find any examples. Stephen'''
date = "2015-09-10T16:51:00Z"
lastmod = "2021-12-16T18:56:00Z"
weight = 45175
keywords = [ "osmium", "filter", "bounding-polygon" ]
aliases = [ "/questions/45175" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Osmium - filter by bounding box](/questions/45175/osmium-filter-by-bounding-box)

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
<span id="post-45175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45175-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-45175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there,</p>
<p>I am wondering if Osmium would be a good tool to use to filter by bounding box? I had a poke around in the documentation but it seems more geared up for tag filtering and I could not find any examples.</p>
<p>Stephen</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-bounding-polygon" rel="tag" title="see questions tagged &#39;bounding-polygon&#39;">bounding-polygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Sep '15, 16:51</strong></p>
<img src="https://secure.gravatar.com/avatar/201c52faa380da64ae76e493d12c0f1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stev&#39;s gravatar image" />
<p><span>stev</span><br />
<span class="score" title="51 reputation points">51</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stev has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-45175" class="comments-container">
&#10;</div>
<div id="comment-tools-45175" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45175-form-container" class="comment-form-container">
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

<span id="45177"></span>

<div id="answer-container-45177" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45177-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45177-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-45177-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="stev has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Osmium is first an foremost a library and not a tool; there's a couple command-line programs (notably osmium-tool) that make use of some of Osmium's capabilities but mostly Osmium is for programmers. You could implement a bounding box filter with Osmium - but why not use what is already there, namely Osmosis (written in Java), osmconvert (in C), or osm-history-splitter (C++ and based on the older version of Osmium).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Sep '15, 19:37</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-45177" class="comments-container">
<span id="45221"></span>
<div id="comment-45221" class="comment">
<div id="post-45221-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK, thanks, just checking that I hadn't missed something. I wanted to use a "best-in-class" tool (performance-wise) to compare with what I'm doing on scaling out with Hadoop etc. And I think Osmium could be that but I'll take a look at the older tools. Thanks.</p>
</div>
<div id="comment-45221-info" class="comment-info">
<span class="comment-age">(13 Sep '15, 11:19)</span> <span class="comment-user userinfo">stev</span>
</div>
</div>
</div>
<div id="comment-tools-45177" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45177-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82855"></span>

<div id="answer-container-82855" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82855-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82855-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82855-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The other answer ist by a bit outdated. Osmium tool provides an "extract" command which will filter by bounding box (or polygon).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Dec '21, 18:56</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-82855" class="comments-container">
&#10;</div>
<div id="comment-tools-82855" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82855-form-container" class="comment-form-container">
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

