+++
type = "question"
title = "Incorrect city on border street causing missing packages and deliveries"
description = '''My address is on a street in another city from the one in which I live. Our entire building is in Cambridge, MA, but the street we live on is within Somerville, MA. Therefore our address is XX Russell Street, Cambridge, MA 02140. However, Russell Street is tagged as Somerville, MA. Some applications...'''
date = "2021-07-09T15:50:00Z"
lastmod = "2021-07-09T16:58:00Z"
weight = 80905
keywords = [ "border", "zipcodes" ]
aliases = [ "/questions/80905" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Incorrect city on border street causing missing packages and deliveries](/questions/80905/incorrect-city-on-border-street-causing-missing-packages-and-deliveries)

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
<span id="post-80905-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80905-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80905-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My address is on a street in another city from the one in which I live. Our entire building is in Cambridge, MA, but the street we live on is within Somerville, MA. Therefore our address is XX Russell Street, Cambridge, MA 02140. However, Russell Street is tagged as Somerville, MA. Some applications do not let me select "Cambridge" as my city because of this discrepancy. This has cause several of our deliveries to end up at Russell Road, Somerville, MA instead. I did some searching and found <a href="https://help.openstreetmap.org/questions/17995/zip-code-may-be-prevent-locating-address">this thread</a> where the answer was to tag the street with the correct city. However, houses on the north side of the street are Somerville addresses while houses on the south side of the street are Cambridge addresses.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-border" rel="tag" title="see questions tagged &#39;border&#39;">border</span> <span class="post-tag tag-link-zipcodes" rel="tag" title="see questions tagged &#39;zipcodes&#39;">zipcodes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jul '21, 15:50</strong></p>
<img src="https://secure.gravatar.com/avatar/e6d9f59de6bbeb158372f69c5e826015?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smlevorse&#39;s gravatar image" />
<p><span>smlevorse</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smlevorse has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80905" class="comments-container">
&#10;</div>
<div id="comment-tools-80905" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80905-form-container" class="comment-form-container">
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

<span id="80906"></span>

<div id="answer-container-80906" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80906-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-80906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="smlevorse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>How unfortunate to be an edge case!</p>
<p>I see you have added addr:city to the relevant houses, which is probably the best response one can manage within OpenStreetMap itself. You can see what the native search engine on OSM returns <a href="https://nominatim.openstreetmap.org/ui/search.html?q=40+russell+street+cambridge+ma">here</a>. The only other thing which occurs to me is to extend the zipcode to a full 9-digit one.</p>
<p>However, this may not resolve the issue. Many logistics companies whilst using OSM for things like routing may not use it for finding the location of a specific address (geocoding). This is for often simple reasons such as many addresses missing (Massachusetts is unusual in having all addresses on OSM). Some will use hybrid approaches to search (first OSM, then another, more expensive, source).</p>
<p>One other thing. Often the data will be updated on something like a monthly schedule, so changes on OSM will not immediately be used by third-parties.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jul '21, 16:58</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-80906" class="comments-container">
&#10;</div>
<div id="comment-tools-80906" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80906-form-container" class="comment-form-container">
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

