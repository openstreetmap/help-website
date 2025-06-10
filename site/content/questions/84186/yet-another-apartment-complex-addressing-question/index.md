+++
type = "question"
title = "Yet another apartment complex addressing question."
description = '''Hi all, I&#x27;m trying to improve the address tagging for this apartment complex. Here are the facts on the ground:  The whole complex has one house number, 23411 Summerfield. Within the complex there are around 50 buildings, each with its own building number, e.g., Building 12 Apartments&#x27; postal addres...'''
date = "2022-04-15T20:02:00Z"
lastmod = "2022-04-17T13:57:00Z"
weight = 84186
keywords = [ "residential", "apartment", "tagging", "address" ]
aliases = [ "/questions/84186" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Yet another apartment complex addressing question.](/questions/84186/yet-another-apartment-complex-addressing-question)

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
<span id="post-84186-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84186-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84186-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all, I'm trying to improve the address tagging for <a href="https://www.openstreetmap.org/way/1050323409">this apartment complex</a>.</p>
<p>Here are the facts on the ground:</p>
<ul>
<li>The whole complex has one house number, 23411 Summerfield.</li>
<li>Within the complex there are around 50 buildings, each with its own building number, e.g., Building 12</li>
<li>Apartments' postal addresses are based on a building number and unit letter. So an example address would be 24311 Summerfield Apt. 42B.</li>
<li>Mail to the building management office is just addressed to 23411 Summerfield, with no unit number.</li>
<li>In most buildings, each unit has its own building entrance.</li>
<li>Many units have both a pedestrian entrance and a garage entrance. Some units have an assigned garage in a separate building.</li>
</ul>
<p>Currently we have ways for the complex as a whole and for each building, and I expect we'll want to add entrance nodes for apartments with private entrances. Also there are currently address tags on the buildings but they were imported and I claim they're incorrect.</p>
<p>So my questions are:</p>
<ul>
<li>What address tags, if any, should be populated on the landuse=resedential node linked above?</li>
<li>What address tags, if any, should be populated on the individual buildings? Note that with the exception of the management office, no building corresponds to a single postal delivery point.</li>
<li>What address tags, if any, should be populated on pedestrian apartment entrances?</li>
<li>What address tags, if any, should be populated on garage apartment entrances?</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-residential" rel="tag" title="see questions tagged &#39;residential&#39;">residential</span> <span class="post-tag tag-link-apartment" rel="tag" title="see questions tagged &#39;apartment&#39;">apartment</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Apr '22, 20:02</strong></p>
<img src="https://secure.gravatar.com/avatar/7c177865bd107a919938355fe93de93a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vectro&#39;s gravatar image" />
<p><span>vectro</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vectro has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Apr '22, 20:11</strong> </span></p>
</div>
</div>
<div id="comments-container-84186" class="comments-container">
&#10;</div>
<div id="comment-tools-84186" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84186-form-container" class="comment-form-container">
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

<span id="84192"></span>

<div id="answer-container-84192" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84192-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84192-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84192-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="vectro has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The addr:* scheme of OSM is technically only directed at postal addresses, so applying this principle rigorously reduces the problem: neither the buildings themselves, nor the garages have postal addresses. So from an addressing perspective, I would ignore these two aspects right now (how to tag the house number on a separately located garage is an intricate question in itself). I see no reason why you cannot tag the buildings with a name tag, or alternatively a ref tag (depending on how they are marked on the ground).</p>
<p>For the standard apartment units I'd use addr:flats or addr:unit (usage differs between US &amp; Europe where unit tends to be used for business premises) together with the street address, and map these to the doors (pedestrian entrances).</p>
<p>The management office can then have the standard street address.</p>
<p>You will notice that this does not solve the complete problem, but as I don't believe these have been solved for OSM as a whole, it's rather easier than trying to create a new scheme.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Apr '22, 13:57</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-84192" class="comments-container">
&#10;</div>
<div id="comment-tools-84192" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84192-form-container" class="comment-form-container">
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

