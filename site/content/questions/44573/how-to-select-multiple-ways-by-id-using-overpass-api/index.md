+++
type = "question"
title = "How to select multiple ways by id using Overpass API?"
description = '''How can I select multiple ways by their OSM id using the overpass API? [out:json];way(104178011);way(18916837);out tags;  The above query only includes the data about the second way. Link.'''
date = "2015-07-31T16:07:00Z"
lastmod = "2023-04-10T08:03:00Z"
weight = 44573
keywords = [ "overpassapi", "overpass-ql" ]
aliases = [ "/questions/44573" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to select multiple ways by id using Overpass API?](/questions/44573/how-to-select-multiple-ways-by-id-using-overpass-api)

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
<span id="post-44573-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44573-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-44573-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I select multiple ways by their OSM id using the overpass API?</p>
<pre><code>[out:json];way(104178011);way(18916837);out tags;</code></pre>
<p>The above query only includes the data about the second way. <a href="http://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%3Bway%28104178011%29%3Bway%2818916837%29%3Bout%20tags%3B%0A">Link.</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Jul '15, 16:07</strong></p>
<img src="https://secure.gravatar.com/avatar/887e8dcd0dc913a9516e6ad0f5ab5a56?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CrazyDave2345&#39;s gravatar image" />
<p><span>CrazyDave2345</span><br />
<span class="score" title="55 reputation points">55</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CrazyDave2345 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-44573" class="comments-container">
&#10;</div>
<div id="comment-tools-44573" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44573-form-container" class="comment-form-container">
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

<span id="64860"></span>

<div id="answer-container-64860" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64860-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64860-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-64860-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For those arriving here via an internet search, this is a quicker way to do it now:</p>
<pre><code> [out:json];way(id:104178011,18916837);out tags;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jul '18, 14:16</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Apr '23, 11:48</strong> </span></p>
</div>
</div>
<div id="comments-container-64860" class="comments-container">
&#10;</div>
<div id="comment-tools-64860" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64860-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44574"></span>

<div id="answer-container-44574" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44574-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44574-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44574-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Found it for myself this way: [out:json];way(104178011);out tags;way(18916837);out tags;</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jul '15, 16:36</strong></p>
<img src="https://secure.gravatar.com/avatar/887e8dcd0dc913a9516e6ad0f5ab5a56?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CrazyDave2345&#39;s gravatar image" />
<p><span>CrazyDave2345</span><br />
<span class="score" title="55 reputation points">55</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CrazyDave2345 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-44574" class="comments-container">
<span id="44575"></span>
<div id="comment-44575" class="comment">
<div id="post-44575-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Another solution is to use a union, using parentheses:</p>
<p>(way(104178011);way(18916837););</p>
<p>Not important for simple output, but unions are useful for more complicated scripts.</p>
</div>
<div id="comment-44575-info" class="comment-info">
<span class="comment-age">(31 Jul '15, 17:59)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="44576"></span>
<div id="comment-44576" class="comment">
<div id="post-44576-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>@macerickson Yeah its more formal and stuff.</p>
</div>
<div id="comment-44576-info" class="comment-info">
<span class="comment-age">(31 Jul '15, 22:16)</span> <span class="comment-user userinfo">CrazyDave2345</span>
</div>
</div>
</div>
<div id="comment-tools-44574" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44574-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87091"></span>

<div id="answer-container-87091" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87091-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87091-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87091-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To get the result shown in UI, run this query:</p>
<pre><code>[out:json];
way(id:104178011,18916837);
out body;
&gt;;
out skel qt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Apr '23, 08:03</strong></p>
<img src="https://secure.gravatar.com/avatar/c28ac242106e3ef8aaa62f576fe2fbf0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mappist&#39;s gravatar image" />
<p><span>Mappist</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mappist has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Apr '23, 08:04</strong> </span></p>
</div>
</div>
<div id="comments-container-87091" class="comments-container">
&#10;</div>
<div id="comment-tools-87091" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87091-form-container" class="comment-form-container">
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

