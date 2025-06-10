+++
type = "question"
title = "osmosis - extract via bbox or poly - which is faster?"
description = '''Hello - I am extracting continent data from planet.osm.pbf (for further processing) and am wondering which is faster - using bounding boxes or .poly files. And is there a subsequent extract performance impact? While I can run a series of tests if someone knows the answer it would be more time effici...'''
date = "2014-12-11T15:59:00Z"
lastmod = "2015-01-19T20:31:00Z"
weight = 39221
keywords = [ "bounding", "polygon", "osmosis" ]
aliases = [ "/questions/39221" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [osmosis - extract via bbox or poly - which is faster?](/questions/39221/osmosis-extract-via-bbox-or-poly-which-is-faster)

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
<span id="post-39221-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39221-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-39221-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello -</p>
<p>I am extracting continent data from planet.osm.pbf (for further processing) and am wondering which is faster - using bounding boxes or .poly files. And is there a subsequent extract performance impact?</p>
<p>While I can run a series of tests if someone knows the answer it would be more time efficient. I also understand "history splitter" is faster but compiling is a bit beyond my current skill set. Or future :)</p>
<p>Thanks, pitney</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bounding" rel="tag" title="see questions tagged &#39;bounding&#39;">bounding</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Dec '14, 15:59</strong></p>
<img src="https://secure.gravatar.com/avatar/92443a39a30b5e613ce00de446845b9e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pitney&#39;s gravatar image" />
<p><span>pitney</span><br />
<span class="score" title="44 reputation points">44</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pitney has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-39221" class="comments-container">
&#10;</div>
<div id="comment-tools-39221" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39221-form-container" class="comment-form-container">
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

<span id="39253"></span>

<div id="answer-container-39253" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39253-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39253-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-39253-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pitney has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Checking if a point is inside a polygon is usually (much) more expensive than a simple bbox check, i.e. bbox will be faster in general. However, if you plan to use poly files, be sure to use as few points as possible, while still retaining close enough resemblance to the original geometry. That really cuts down the overall processing time.</p>
<p>Maybe you want to get in touch with Frederik Ramm on this or use some of the existing Geofabrik poly files.</p>
<p>Btw: what do you mean with 'history splitter' is faster? Planet files don't include any version history so this is not really relevant.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Dec '14, 07:55</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Dec '14, 09:33</strong> </span></p>
</div>
</div>
<div id="comments-container-39253" class="comments-container">
<span id="39261"></span>
<div id="comment-39261" class="comment">
<div id="post-39261-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>mmd, thank you once again.<br />
I am using Geofabrik's .poly files, I did not mention it because I am try not to write essays here. "history splitter" is <a href="https://github.com/MaZderMind/osm-history-splitter">https://github.com/MaZderMind/osm-history-splitter</a> which I have read is faster. and I just! discovered that the "check mark" let's one accept an answer. wwk? pitney</p>
</div>
<div id="comment-39261-info" class="comment-info">
<span class="comment-age">(13 Dec '14, 14:50)</span> <span class="comment-user userinfo">pitney</span>
</div>
</div>
</div>
<div id="comment-tools-39253" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39253-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40483"></span>

<div id="answer-container-40483" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40483-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40483-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40483-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I ran tests contrasting .poly files from geofabrik and bounding boxes</p>
<p>poly = 5 hours</p>
<p>bbox = 4 hours</p>
<p>(16 gb ram, dual quad cores, --tee=6, --workers=7)</p>
<p>pitney</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jan '15, 20:31</strong></p>
<img src="https://secure.gravatar.com/avatar/92443a39a30b5e613ce00de446845b9e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pitney&#39;s gravatar image" />
<p><span>pitney</span><br />
<span class="score" title="44 reputation points">44</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pitney has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-40483" class="comments-container">
&#10;</div>
<div id="comment-tools-40483" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40483-form-container" class="comment-form-container">
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

