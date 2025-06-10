+++
type = "question"
title = "adding an address range to a street"
description = '''How do I add an address range for a given street?'''
date = "2014-06-23T21:40:00Z"
lastmod = "2014-06-24T13:30:00Z"
weight = 34264
keywords = [ "ranges", "geocoding", "address" ]
aliases = [ "/questions/34264" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [adding an address range to a street](/questions/34264/adding-an-address-range-to-a-street)

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
<span id="post-34264-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34264-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-34264-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do I add an address range for a given street?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ranges" rel="tag" title="see questions tagged &#39;ranges&#39;">ranges</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jun '14, 21:40</strong></p>
<img src="https://secure.gravatar.com/avatar/c09aa0898a0757f05cec9d0fe244caba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aitkingis&#39;s gravatar image" />
<p><span>aitkingis</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aitkingis has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-34264" class="comments-container">
&#10;</div>
<div id="comment-tools-34264" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34264-form-container" class="comment-form-container">
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

<span id="34265"></span>

<div id="answer-container-34265" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34265-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34265-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-34265-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In OSM, addresses are never the property of a street. They are independent features.</p>
<p>The most common way to add addresses is to have individual buildings or, failing that, address points, each tagged with a house number and a street name (and potentially city name, zip code, and country name as well but most processing software will guess these).</p>
<p>It is possible to have so-called "interpolation ways" where you add an address point for the first and last house number on each side of the street and then connect the first and last number with a line (invisible on the map) marked as an interpolation line; this will then synthesize house numbers running from the lower to the higher.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jun '14, 21:58</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-34265" class="comments-container">
&#10;</div>
<div id="comment-tools-34265" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34265-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="34275"></span>

<div id="answer-container-34275" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34275-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34275-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-34275-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is the so called Karlsruhe Schema for tagging addresses. Have a look <a href="http://wiki.openstreetmap.org/wiki/Karlsruhe_Schema">at the wiki</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jun '14, 13:30</strong></p>
<img src="https://secure.gravatar.com/avatar/7651f7a3094f0a39b51630214fe9c94d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alex_AddisMap&#39;s gravatar image" />
<p><span>Alex_AddisMap</span><br />
<span class="score" title="189 reputation points">189</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alex_AddisMap has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-34275" class="comments-container">
&#10;</div>
<div id="comment-tools-34275" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34275-form-container" class="comment-form-container">
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

