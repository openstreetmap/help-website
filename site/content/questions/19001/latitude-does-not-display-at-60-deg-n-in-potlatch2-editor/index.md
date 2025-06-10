+++
type = "question"
title = "Latitude does not display at 60 deg N in Potlatch2 editor"
description = '''This problem has been bothering me for some time. I was hoping it would just cure itself but it has not. For several weeks, when working in the neighborhood of 60N,151W (Homer, Alaska), only the longitude displays in the coordinates box when Options&amp;gt;Show Mouse Lat/Lon is selected. Even stranger i...'''
date = "2013-01-12T11:05:00Z"
lastmod = "2013-01-12T23:21:00Z"
weight = 19001
keywords = [ "potlatch2", "latitude", "error" ]
aliases = [ "/questions/19001" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Latitude does not display at 60 deg N in Potlatch2 editor](/questions/19001/latitude-does-not-display-at-60-deg-n-in-potlatch2-editor)

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
<span id="post-19001-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19001-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19001-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This problem has been bothering me for some time. I was hoping it would just cure itself but it has not.</p>
<p>For several weeks, when working in the neighborhood of 60N,151W (Homer, Alaska), only the longitude displays in the coordinates box when Options&gt;Show Mouse Lat/Lon is selected. Even stranger is that the longitude displays in the bottom box, the opposite of when I am working in Thailand, the eastern hemisphere. Both coordinates display and are correct in Thailand.</p>
<p>I checked a spot in Texas and sure enough, everything works there. Brownsville, Texas, is at about 25N, 98W, and the values are arranged as in Thailand with lat on top, lon on bottom</p>
<p>What's going on?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-potlatch2" rel="tag" title="see questions tagged &#39;potlatch2&#39;">potlatch2</span> <span class="post-tag tag-link-latitude" rel="tag" title="see questions tagged &#39;latitude&#39;">latitude</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jan '13, 11:05</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-19001" class="comments-container">
&#10;</div>
<div id="comment-tools-19001" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19001-form-container" class="comment-form-container">
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

<span id="19008"></span>

<div id="answer-container-19008" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19008-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19008-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19008-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I can reproduce this problem (Firefox on Linux, with Flash plugin 10.3 r183).</p>
<p>The problem seems to occur whenever the longitude has three digits and a minus sign (i.e. if it is &lt; -100). You can nicely see it by going to e.g. 50N,99.5W (enter "50 -99.5" in the search box on the main page), then scrolling to the left. Once the longitude hits -100, the coordinate display is messed up.</p>
<p>This looks like a bug in Potlach. Please file a bug at <a href="https://trac.openstreetmap.org/">https://trac.openstreetmap.org/</a> (for component "potlatch2").</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jan '13, 17:13</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-19008" class="comments-container">
<span id="19010"></span>
<div id="comment-19010" class="comment">
<div id="post-19010-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the info about Trac. The bug has already been reported: <a href="https://trac.openstreetmap.org/ticket/4356">https://trac.openstreetmap.org/ticket/4356</a></p>
<p>It was first reported 9 months ago. AFAIK, nothing has been done about it to date.</p>
</div>
<div id="comment-19010-info" class="comment-info">
<span class="comment-age">(12 Jan '13, 23:21)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-19008" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19008-form-container" class="comment-form-container">
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

