+++
type = "question"
title = "Address verification"
description = '''Can we use open street map service for address verification in commerical product? if yes then do we have limit per day?'''
date = "2012-12-04T15:31:00Z"
lastmod = "2012-12-04T17:00:00Z"
weight = 18192
keywords = [ "nominatim" ]
aliases = [ "/questions/18192" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Address verification](/questions/18192/address-verification)

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
<span id="post-18192-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18192-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18192-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can we use open street map service for address verification in commerical product? if yes then do we have limit per day?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Dec '12, 15:31</strong></p>
<img src="https://secure.gravatar.com/avatar/099251d8aeec067b14a8e7af525f6f3b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Venkat&#39;s gravatar image" />
<p><span>Venkat</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Venkat has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18192" class="comments-container">
&#10;</div>
<div id="comment-tools-18192" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18192-form-container" class="comment-form-container">
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

<span id="18195"></span>

<div id="answer-container-18195" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18195-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18195-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-18195-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is unlikely that you will be able to use OSM data for address <strong>verification</strong> since the absence of an address does not guarantee that that address doesn't exist. I do not believe there are any countries for which OSM has a complete and definitive list of addresses.</p>
<p>You can use OSM data to geocode addresses - i.e. covert an address to a latitude and longitude. See the nominatim <a href="https://wiki.openstreetmap.org/wiki/Nominatim">API</a> and usage <a href="https://wiki.openstreetmap.org/wiki/Nominatim_usage_policy">policy</a> but even for this purpose you are not guaranteed to get a valid location for all addresses and how suitable it is will depend on your usage.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Dec '12, 17:00</strong></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twain has 15 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-18195" class="comments-container">
&#10;</div>
<div id="comment-tools-18195" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18195-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="18193"></span>

<div id="answer-container-18193" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18193-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18193-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-18193-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please see the <a href="https://wiki.openstreetmap.org/wiki/Nominatim_usage_policy">Nominatim usage policy</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Dec '12, 15:34</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-18193" class="comments-container">
<span id="18194"></span>
<div id="comment-18194" class="comment">
<div id="post-18194-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Note that you can install Nominatim locally in order to run as much queries as you want. And there are also other Nonimatin instances with different usage policies like the one hosted by <a href="http://open.mapquestapi.com/nominatim/">MapQuest</a>.</p>
</div>
<div id="comment-18194-info" class="comment-info">
<span class="comment-age">(04 Dec '12, 16:43)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-18193" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18193-form-container" class="comment-form-container">
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

