+++
type = "question"
title = "Getting extents of pbf file using osmosis"
description = '''Is there a way to obtain the extents of a pbf file (top, bottom, left, right) using osmosis or similar tool?'''
date = "2018-10-30T14:35:00Z"
lastmod = "2018-10-31T12:33:00Z"
weight = 66559
keywords = [ "osmosis" ]
aliases = [ "/questions/66559" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Getting extents of pbf file using osmosis](/questions/66559/getting-extents-of-pbf-file-using-osmosis)

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
<span id="post-66559-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66559-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66559-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to obtain the extents of a pbf file (top, bottom, left, right) using <code>osmosis</code> or similar tool?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Oct '18, 14:35</strong></p>
<img src="https://secure.gravatar.com/avatar/23d42f5f532e8b985b9f0815c7897079?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="awa5114&#39;s gravatar image" />
<p><span>awa5114</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="awa5114 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66559" class="comments-container">
&#10;</div>
<div id="comment-tools-66559" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66559-form-container" class="comment-form-container">
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

<span id="66596"></span>

<div id="answer-container-66596" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66596-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66596-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-66596-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="awa5114 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="https://wiki.openstreetmap.org/wiki/Osmconvert#Retrieving_Statistical_Data">osmconvert --out-statistics</a> option returns lat/lon min/max values:</p>
<pre><code>osmconvert liechtenstein.osm.pbf --out-statistics</code></pre>
<p>osmconvert <a href="https://wiki.openstreetmap.org/wiki/Osmconvert#Binaries">binaries</a> are also available for Windows.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '18, 10:55</strong></p>
<img src="https://secure.gravatar.com/avatar/f92748c8fa508a936bcf2169b30cabf6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ikonor&#39;s gravatar image" />
<p><span>ikonor</span><br />
<span class="score" title="1286 reputation points"><span>1.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ikonor has 4 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-66596" class="comments-container">
<span id="66600"></span>
<div id="comment-66600" class="comment">
<div id="post-66600-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Excellent, I knew there had to be a way through the regular tools!</p>
</div>
<div id="comment-66600-info" class="comment-info">
<span class="comment-age">(31 Oct '18, 12:33)</span> <span class="comment-user userinfo">awa5114</span>
</div>
</div>
</div>
<div id="comment-tools-66596" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66596-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="66560"></span>

<div id="answer-container-66560" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66560-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66560-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-66560-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This can be done with the <code>osmium</code> command line tool from <a href="https://github.com/osmcode/osmium-tool">https://github.com/osmcode/osmium-tool</a> (also present in recent Linux distributions):</p>
<pre><code>% osmium fileinfo -eg data.bbox myfile.osm.pbf
[======================================================================] 100% 
(6.0807,47.4811,9.74985,50.3178)</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Oct '18, 14:56</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-66560" class="comments-container">
&#10;</div>
<div id="comment-tools-66560" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66560-form-container" class="comment-form-container">
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

