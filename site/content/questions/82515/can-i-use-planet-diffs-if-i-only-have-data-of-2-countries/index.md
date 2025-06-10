+++
type = "question"
title = "Can I use &quot;planet diffs&quot; if I only have data of 2 countries?"
description = '''I&#x27;m currently running my own nominatim server with data of just a couple of countries. Nominatim supports automatic updates, and it uses the &quot;planet diffs&quot; by default, according to their manual. Is it any problem that it uses all diffs of the planet if it only hasthe data of a couple of countries? W...'''
date = "2021-11-08T10:48:00Z"
lastmod = "2021-11-09T07:18:00Z"
weight = 82515
keywords = [ "planet", "diffs", "nominatim" ]
aliases = [ "/questions/82515" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can I use "planet diffs" if I only have data of 2 countries?](/questions/82515/can-i-use-planet-diffs-if-i-only-have-data-of-2-countries)

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
<span id="post-82515-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82515-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82515-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm currently running my own nominatim server with data of just a couple of countries. Nominatim supports automatic updates, and it uses the "planet diffs" by default, according to their <a href="https://nominatim.org/release-docs/latest/admin/Update/">manual</a>.</p>
<p>Is it any problem that it uses all diffs of the planet if it only hasthe data of a couple of countries? Will it somehow add the diffs of like Australia while I don't have any data of Australia to begin with?</p>
<p>If that's not possible, how can I setup Nominatim to only listen to diffs of the countries it has the data of?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-diffs" rel="tag" title="see questions tagged &#39;diffs&#39;">diffs</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Nov '21, 10:48</strong></p>
<img src="https://secure.gravatar.com/avatar/04175cc004ecad1e262fad8e94f86d62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KoenMlt&#39;s gravatar image" />
<p><span>KoenMlt</span><br />
<span class="score" title="42 reputation points">42</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KoenMlt has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82515" class="comments-container">
&#10;</div>
<div id="comment-tools-82515" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82515-form-container" class="comment-form-container">
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

<span id="82519"></span>

<div id="answer-container-82519" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82519-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82519-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-82519-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="KoenMlt has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim version 4 has this covered in <a href="https://www.nominatim.org/release-docs/latest/admin/Advanced-Installations/#importing-multiple-regions-with-updates">https://www.nominatim.org/release-docs/latest/admin/Advanced-Installations/#importing-multiple-regions-with-updates</a> You'd need to check/test if previous versions have the same instructions <a href="https://www.nominatim.org/release-docs/">https://www.nominatim.org/release-docs/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Nov '21, 14:03</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-82519" class="comments-container">
<span id="82528"></span>
<div id="comment-82528" class="comment">
<div id="post-82528-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you!</p>
</div>
<div id="comment-82528-info" class="comment-info">
<span class="comment-age">(09 Nov '21, 07:18)</span> <span class="comment-user userinfo">KoenMlt</span>
</div>
</div>
</div>
<div id="comment-tools-82519" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82519-form-container" class="comment-form-container">
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

