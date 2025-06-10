+++
type = "question"
title = "[closed] looking for an algorithm to walk on new paths"
description = '''I am looking for an algorithm. I want to start at a certain point in a map, then follow a path on my gps-device, which starts and ends at the same point while always having a distance of about distance. I want to - if possible - always go on new streets. Finally I should have a set of tracks that ha...'''
date = "2013-12-18T06:43:00Z"
lastmod = "2013-12-18T10:19:00Z"
weight = 29152
keywords = [ "development", "routing", "algorithm" ]
aliases = [ "/questions/29152" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] looking for an algorithm to walk on new paths](/questions/29152/looking-for-an-algorithm-to-walk-on-new-paths)

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
<span id="post-29152-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29152-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29152-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am looking for an algorithm.</p>
<p>I want to start at a certain point in a map, then follow a path on my gps-device, which starts and ends at the same point while always having a distance of about <code>distance</code>. I want to - if possible - always go on new streets. Finally I should have a set of tracks that have every street covered around a starting point while trying to not walk the same street twice.</p>
<p>Idea:</p>
<ol>
<li>I get a vector map and start at point <code>Start</code> programmatically.</li>
<li>Then I loop through north, east, south, west and in between with 1° resolution, ie 360°.</li>
<li>In this loop I walk to the first crossing, turn right, to the next, turn right and then aim at <code>Start</code>, finding the closest way to <code>Start</code> using this method.</li>
</ol>
<p>Here I want inspiration...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-algorithm" rel="tag" title="see questions tagged &#39;algorithm&#39;">algorithm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Dec '13, 06:43</strong></p>
<img src="https://secure.gravatar.com/avatar/5c8b04e788827b80d1072692d055b226?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lutz%20Gregor&#39;s gravatar image" />
<p><span>Lutz Gregor</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lutz Gregor has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Dec '13, 12:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-29152" class="comments-container">
<span id="29157"></span>
<div id="comment-29157" class="comment">
<div id="post-29157-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Note to interested ones: the discussion is now there: <a href="http://forum.openstreetmap.org/viewtopic.php?id=23583">http://forum.openstreetmap.org/viewtopic.php?id=23583</a></p>
</div>
<div id="comment-29157-info" class="comment-info">
<span class="comment-age">(18 Dec '13, 10:19)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-29152" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29152-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by Frederik Ramm 18 Dec '13, 07:13

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29153"></span>

<div id="answer-container-29153" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29153-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29153-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-29153-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your idea is interesting but it is not suitable for this medium. help.openstreetmap.org is not a discussion forum - it isn't suited technically. I would recommend that you check out the "dev" or "routing" mailing lists (see <a href="https://lists.openstreetmap.org/listinfo">https://lists.openstreetmap.org/listinfo</a> ), or if you prefer, a suitable forum (see <a href="http://forum.openstreetmap.org">http://forum.openstreetmap.org</a>).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Dec '13, 07:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Dec '13, 10:18</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-29153" class="comments-container">
&#10;</div>
<div id="comment-tools-29153" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29153-form-container" class="comment-form-container">
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

