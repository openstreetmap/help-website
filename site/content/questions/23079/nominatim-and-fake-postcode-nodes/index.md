+++
type = "question"
title = "Nominatim and fake postcode nodes"
description = '''How do I get rid the http://nominatim.openstreetmap.org/details.php?place_id=98286334 ? This node introduces postal code 12 on all underlying streets. I&#x27;ve tried using is_in, postal_code tags on the administrative boundaries and on associatedStreet relation to no avail. On house level it seems to wo...'''
date = "2013-06-06T17:33:00Z"
lastmod = "2013-06-07T14:02:00Z"
weight = 23079
keywords = [ "nominatim", "postcode" ]
aliases = [ "/questions/23079" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim and fake postcode nodes](/questions/23079/nominatim-and-fake-postcode-nodes)

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
<span id="post-23079-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23079-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23079-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do I get rid the <a href="http://nominatim.openstreetmap.org/details.php?place_id=98286334">http://nominatim.openstreetmap.org/details.php?place_id=98286334</a> ? This node introduces postal code 12 on all underlying streets. I've tried using is_in, postal_code tags on the administrative boundaries and on associatedStreet relation to no avail.</p>
<p>On house level it seems to work, but this is not what I want. I want to be able to search for "Steenweg op Waarloos" and see post code 2840 on all segments.</p>
<p>Marc</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-postcode" rel="tag" title="see questions tagged &#39;postcode&#39;">postcode</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jun '13, 17:33</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-23079" class="comments-container">
&#10;</div>
<div id="comment-tools-23079" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23079-form-container" class="comment-form-container">
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

<span id="23099"></span>

<div id="answer-container-23099" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23099-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23099-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-23099-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="escada has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>These fake postcodes have been created during initial database import and are completely static at the moment. You can override them on street or house level but completely removing needs to be done by hand in the Nominatim database. I've deleted that number 12 now as it is quite obviously bogus.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '13, 13:46</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-23099" class="comments-container">
<span id="23100"></span>
<div id="comment-23100" class="comment">
<div id="post-23100-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks for removing the bogus node</p>
</div>
<div id="comment-23100-info" class="comment-info">
<span class="comment-age">(07 Jun '13, 14:02)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-23099" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23099-form-container" class="comment-form-container">
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

