+++
type = "question"
title = "Possible to bring building shape in from vector file?"
description = '''I have a KML file that shows buildings as a shapes. If I alt-click the buildings, I only see an option to define it as a road. Is it then possible to convert a trail to a shape or building? What is the best way to do this?'''
date = "2012-10-03T13:22:00Z"
lastmod = "2012-10-05T09:49:00Z"
weight = 16634
keywords = [ "building", "kml" ]
aliases = [ "/questions/16634" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Possible to bring building shape in from vector file?](/questions/16634/possible-to-bring-building-shape-in-from-vector-file)

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
<span id="post-16634-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16634-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16634-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a KML file that shows buildings as a shapes. If I alt-click the buildings, I only see an option to define it as a road. Is it then possible to convert a trail to a shape or building? What is the best way to do this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-kml" rel="tag" title="see questions tagged &#39;kml&#39;">kml</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Oct '12, 13:22</strong></p>
<img src="https://secure.gravatar.com/avatar/dbfd254d01aacd89ae20e01353b564d0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="1HealthPlz&#39;s gravatar image" />
<p><span>1HealthPlz</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="1HealthPlz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16634" class="comments-container">
<span id="16675"></span>
<div id="comment-16675" class="comment">
<div id="post-16675-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Are you using the online editor (Potlatch) or are you using JOSM?</p>
</div>
<div id="comment-16675-info" class="comment-info">
<span class="comment-age">(04 Oct '12, 20:53)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
<span id="16676"></span>
<div id="comment-16676" class="comment">
<div id="post-16676-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Firstly, perhaps the answers to <a href="/questions/7174/how-to-import-kml-files-into-openstreetmap">this previous question</a> may help?</p>
<p>Secondly, if you've already fixed this (as <a href="/questions/16642/problems-with-way-100-184003779-building-not-shaded-options-not-selectable">this question</a> suggests) it might be worth mentioning what you did.</p>
</div>
<div id="comment-16676-info" class="comment-info">
<span class="comment-age">(04 Oct '12, 21:18)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-16634" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16634-form-container" class="comment-form-container">
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

<span id="16689"></span>

<div id="answer-container-16689" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16689-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16689-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-16689-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This will be because the building isn't "closed" - in other words, the shape doesn't start and end with the same node. Most probably it starts and ends with two different nodes at the same point.</p>
<p>If Potlatch 2 sees a shape that isn't closed, it won't offer the tagging choices associated with closed shapes, of which buildings are one.</p>
<p>I have a feeling this might have been a Potlatch 2 issue with certain KML files, but I've just <a href="https://github.com/systemed/potlatch2/commit/2ed961dda87afc45bcf09b6376a847425cfb9a2a">committed a fix</a> which will be live next time the osm.org site code is updated (usually in a couple of days).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Oct '12, 09:49</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Oct '12, 10:11</strong> </span></p>
</div>
</div>
<div id="comments-container-16689" class="comments-container">
&#10;</div>
<div id="comment-tools-16689" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16689-form-container" class="comment-form-container">
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

