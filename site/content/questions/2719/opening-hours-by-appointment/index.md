+++
type = "question"
title = "opening hours by appointment?"
description = '''Some shops around here are only open &quot;by appointment.&quot; Sometimes they have specific hours for weekdays, but are open Saturday and Sunday by appointment only. Other times, the shop never has regular opening hours, but is only open by appointment. Is there any way to indicate this with the link:openin...'''
date = "2011-02-04T17:59:00Z"
lastmod = "2015-06-16T17:43:00Z"
weight = 2719
keywords = [ "opening_hours", "tagging" ]
aliases = [ "/questions/2719" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [opening hours by appointment?](/questions/2719/opening-hours-by-appointment)

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
<span id="post-2719-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2719-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-2719-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Some shops around here are only open "by appointment." Sometimes they have specific hours for weekdays, but are open Saturday and Sunday by appointment only. Other times, the shop never has regular opening hours, but is only open by appointment. Is there any way to indicate this with the link:<a href="http://wiki.openstreetmap.org/wiki/Key:opening_hours">opening_hours</a> tag?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-opening_hours" rel="tag" title="see questions tagged &#39;opening_hours&#39;">opening_hours</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Feb '11, 17:59</strong></p>
<img src="https://secure.gravatar.com/avatar/22748312961cdceb5419decc3cc5faad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peter%20Dobratz&#39;s gravatar image" />
<p><span>Peter Dobratz</span><br />
<span class="score" title="311 reputation points">311</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peter Dobratz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-2719" class="comments-container">
&#10;</div>
<div id="comment-tools-2719" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2719-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="2894"></span>

<div id="answer-container-2894" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2894-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2894-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-2894-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Based on the available information and what seems to make sense, I'm going to use</p>
<pre><code>opening_hours=by_appointment</code></pre>
<p>for retail shops only open by appointment.</p>
<p>For regular opening hours and additional days by appointment, I'll use, for example</p>
<pre><code>opening_hours=Mo-Fr 10:00-16:00;Sa-Su by_appoinment</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Feb '11, 17:00</strong></p>
<img src="https://secure.gravatar.com/avatar/22748312961cdceb5419decc3cc5faad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peter%20Dobratz&#39;s gravatar image" />
<p><span>Peter Dobratz</span><br />
<span class="score" title="311 reputation points">311</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peter Dobratz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-2894" class="comments-container">
<span id="2910"></span>
<div id="comment-2910" class="comment">
<div id="post-2910-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I prefer this a lot more: <code>opening_hours:by_appointment=Sa-Su</code></p>
</div>
<div id="comment-2910-info" class="comment-info">
<span class="comment-age">(10 Feb '11, 21:18)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
</div>
<div id="comment-tools-2894" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2894-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2731"></span>

<div id="answer-container-2731" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2731-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2731-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-2731-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I wasn't able to find anything documented on <a href="http://taginfo.openstreetmap.de/search?q=by+appointment#keys">taginfo</a> to offer you guidance. A discussion took place on the <a href="http://wiki.openstreetmap.org/wiki/Talk:Key:opening_hours#Museum_opens_only_on_request">opening_hours talk page</a> last year, but has not reached a conclusion. I've started a thread on this topic on the <a href="http://lists.openstreetmap.org/pipermail/tagging/2011-February/006762.html">tagging mailing list</a>, perhaps you'll enjoy participating in that conversation?</p>
<p>We can update this answer after some discussion on the list.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Feb '11, 13:41</strong></p>
<img src="https://secure.gravatar.com/avatar/d90ea04df82d77f534659f08894dd889?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard%20Weait&#39;s gravatar image" />
<p><span>Richard Weait</span><br />
<span class="score" title="3044 reputation points"><span>3.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="34 badges"><span class="silver">●</span><span class="badgecount">34</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard Weait has 8 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-2731" class="comments-container">
&#10;</div>
<div id="comment-tools-2731" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2731-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43588"></span>

<div id="answer-container-43588" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43588-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43588-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43588-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://wiki.openstreetmap.org/wiki/Key:opening_hours">opening_hours</a> syntax has been updated to allow for a fallback rule in quotes.</p>
<pre><code>opening_hours=Mo-Fr 10:00-16:00 || &quot;Saturday and Sunday by appointment&quot;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jun '15, 17:43</strong></p>
<img src="https://secure.gravatar.com/avatar/22748312961cdceb5419decc3cc5faad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peter%20Dobratz&#39;s gravatar image" />
<p><span>Peter Dobratz</span><br />
<span class="score" title="311 reputation points">311</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peter Dobratz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43588" class="comments-container">
&#10;</div>
<div id="comment-tools-43588" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43588-form-container" class="comment-form-container">
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

