+++
type = "question"
title = "How to tag a business closing time of &quot;late&quot;?"
description = '''What is the best way to tag a business&#x27; opening hours when they officially close &quot;late&quot;? On the door, it will show something like &quot;5pm-late&quot;. This is very common in New Zealand, for example. The wiki entry for opening_hours doesn&#x27;t seem to cover that case and seems to require putting in a specific t...'''
date = "2017-01-18T23:39:00Z"
lastmod = "2018-07-30T17:45:00Z"
weight = 54153
keywords = [ "opening_hours", "tagging", "newzealand" ]
aliases = [ "/questions/54153" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag a business closing time of "late"?](/questions/54153/how-to-tag-a-business-closing-time-of-late)

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
<span id="post-54153-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54153-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-54153-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What is the best way to tag a business' opening hours when they officially close "late"?</p>
<p>On the door, it will show something like "5pm-late". This is very common in New Zealand, for example.</p>
<p>The <a href="https://wiki.openstreetmap.org/wiki/Key:opening_hours">wiki entry for <code>opening_hours</code></a> doesn't seem to cover that case and seems to require putting in a specific time in the time ranges.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-opening_hours" rel="tag" title="see questions tagged &#39;opening_hours&#39;">opening_hours</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-newzealand" rel="tag" title="see questions tagged &#39;newzealand&#39;">newzealand</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jan '17, 23:39</strong></p>
<img src="https://secure.gravatar.com/avatar/0110e86fdb31486c22dd381326d99de9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fmarier&#39;s gravatar image" />
<p><span>fmarier</span><br />
<span class="score" title="211 reputation points">211</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fmarier has one accepted answer">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jan '17, 23:41</strong> </span></p>
</div>
</div>
<div id="comments-container-54153" class="comments-container">
&#10;</div>
<div id="comment-tools-54153" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54153-form-container" class="comment-form-container">
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

<span id="65027"></span>

<div id="answer-container-65027" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65027-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65027-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65027-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The best we can do with the current approved syntax would be:</p>
<p><code>opening_hours=17:00+ "closes late"</code></p>
<p>But what I do is ask someone, "how late are you usually open?" Sometimes there's not a satisfying answer, but you might get an answer like "usually until 10:30 or 11, but sometimes after midnight if we're busy." Then you can confidently tag as <code>opening_hours=17:00-22:30+</code> which conveys a lot more information.</p>
<p>If you do this, add something like "closing time from conversation with bartender" to the source tag or changeset comment, to make it clear that this info is not from a written hours sign.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jul '18, 17:45</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Jun '19, 20:10</strong> </span></p>
</div>
</div>
<div id="comments-container-65027" class="comments-container">
&#10;</div>
<div id="comment-tools-65027" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65027-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="54154"></span>

<div id="answer-container-54154" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54154-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54154-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54154-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the wiki doesn't cater for a real world case, it's the wiki that's wrong, not the real world. In cases such as this I'd just make sure that enough information is captured so that if in the future the "opening hours format" can cater for it, it can be adjusted.</p>
<p>I suspect I've used "late" in opening hours in the UK (perhaps with a note expaining the circumstances in more detail).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jan '17, 23:54</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-54154" class="comments-container">
&#10;</div>
<div id="comment-tools-54154" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54154-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="54159"></span>

<div id="answer-container-54159" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54159-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54159-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54159-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The opening_hours wiki page mentions the following example:</p>
<pre><code>Su 10:00+
Sunday from 10:00 to an unknown or unspecified closing time.</code></pre>
<p>I believe this syntax should be applicable to your use case. Support by end user software may vary, of course.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jan '17, 12:20</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-54159" class="comments-container">
<span id="54160"></span>
<div id="comment-54160" class="comment">
<div id="post-54160-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I feel that the tag 10:00+ conveys little useful information in comparison to using 'late'.<br />
If I was informed by the map that the shop closed late, I would be confident that it would be still open in the early evening whereas 10:00+ would prompt me to get there before midday.<br />
I would be in favour of adding 'late' to the closing time options if that is what the sign displays.</p>
</div>
<div id="comment-54160-info" class="comment-info">
<span class="comment-age">(19 Jan '17, 12:46)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
</div>
<div id="comment-tools-54159" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54159-form-container" class="comment-form-container">
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

