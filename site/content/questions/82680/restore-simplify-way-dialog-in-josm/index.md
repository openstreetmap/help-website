+++
type = "question"
title = "Restore Simplify Way dialog in JOSM"
description = '''In JOSM, I have accidentally checked &quot;Do not ask again&quot; setting when doing a Simplify Way (CTRL+Y) on a way. Now it always simplifies using the last used maximum error setting (0.25 meters). How do I restore the dialog so that it displays? I cannot find the needed settings in the preferences or any ...'''
date = "2021-11-25T09:19:00Z"
lastmod = "2021-11-26T22:00:00Z"
weight = 82680
keywords = [ "josm", "simplify_way", "dialog" ]
aliases = [ "/questions/82680" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Restore Simplify Way dialog in JOSM](/questions/82680/restore-simplify-way-dialog-in-josm)

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
<span id="post-82680-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82680-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82680-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In JOSM, I have accidentally checked "<code>Do not ask again</code>" setting when doing a Simplify Way (CTRL+Y) on a way. Now it always simplifies using the last used maximum error setting (0.25 meters). How do I restore the dialog so that it displays? I cannot find the needed settings in the preferences or any information on how to do this.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-simplify_way" rel="tag" title="see questions tagged &#39;simplify_way&#39;">simplify_way</span> <span class="post-tag tag-link-dialog" rel="tag" title="see questions tagged &#39;dialog&#39;">dialog</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Nov '21, 09:19</strong></p>
<img src="https://secure.gravatar.com/avatar/fb34d7bed35464f64bba89dba8f34f95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JAT86&#39;s gravatar image" />
<p><span>JAT86</span><br />
<span class="score" title="240 reputation points">240</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JAT86 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82680" class="comments-container">
&#10;</div>
<div id="comment-tools-82680" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82680-form-container" class="comment-form-container">
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

<span id="82682"></span>

<div id="answer-container-82682" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82682-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82682-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-82682-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JAT86 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can restore the previous behavior in the Advanced Preferences. Go to Preferences - tick Expert Mode at the bottom - scroll to and select Advanced Preferences in the left panel. In the search line on the top right type "simplify". The key <code>simplify-way.remember</code> appears. Change it from <em>yes</em> to <em>no</em>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Nov '21, 10:01</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-82682" class="comments-container">
&#10;</div>
<div id="comment-tools-82682" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82682-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82681"></span>

<div id="answer-container-82681" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82681-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi. There is no such dialog box, but you can access the two variables associated with "simplify-way" from the preferences (<code>F12</code>, or <code>Edit→Preferences</code>).</p>
<ul>
<li>Select the "Advanced Preferences" tab (only visible in Expert Mode).</li>
<li>Look for <code>simplify-way.</code> among the configured variables.</li>
<li>You will find both the the numerical value at <code>simplify-way.max-error</code> and your boolean setting at <code>simplify-way.remember</code>.</li>
<li>Now decide if you want to change the latter from <code>yes</code> to <code>no</code>, or if all you wanted was just to be able to edit the numerical value you had entered.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Nov '21, 09:32</strong></p>
<img src="https://secure.gravatar.com/avatar/482a09a1d3540beaa18993d358753a34?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mariotomo&#39;s gravatar image" />
<p><span>mariotomo</span><br />
<span class="score" title="300 reputation points">300</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mariotomo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Nov '21, 13:40</strong> </span></p>
</div>
</div>
<div id="comments-container-82681" class="comments-container">
<span id="82684"></span>
<div id="comment-82684" class="comment">
<div id="post-82684-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>the other answer is definitely more complete, but I don't understand the downvoting. my intention was to help the OP while on my phone, and to come back here and complete my answer. I'm surprised by the downvoting.</p>
</div>
<div id="comment-82684-info" class="comment-info">
<span class="comment-age">(25 Nov '21, 13:32)</span> <span class="comment-user userinfo">mariotomo</span>
</div>
</div>
<span id="82685"></span>
<div id="comment-82685" class="comment">
<div id="post-82685-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Your first answer was formulated a bit ambiguously. One could have read it as "what you ask for is not possible".</p>
</div>
<div id="comment-82685-info" class="comment-info">
<span class="comment-age">(25 Nov '21, 15:49)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="82700"></span>
<div id="comment-82700" class="comment">
<div id="post-82700-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>very possibly so. I understand that you are not the downvoter. you see … a downvote without any comment is just like an error report limited to the words "it doesn't work": one can't learn from it.</p>
</div>
<div id="comment-82700-info" class="comment-info">
<span class="comment-age">(26 Nov '21, 22:00)</span> <span class="comment-user userinfo">mariotomo</span>
</div>
</div>
</div>
<div id="comment-tools-82681" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82681-form-container" class="comment-form-container">
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

