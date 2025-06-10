+++
type = "question"
title = "address search results unsatisfactory"
description = '''I have been noticing frequent address searches that do not give a satisfactory answer. Example: &quot;Harris Place, Seaton, SA, Australia&quot; the street appears to exist and is labelled on the map but does not return a result in the search. In face searching any street name within Seaton seems to return a n...'''
date = "2011-08-29T08:15:00Z"
lastmod = "2011-08-30T01:05:00Z"
weight = 7413
keywords = [ "search", "nominatim", "problem" ]
aliases = [ "/questions/7413" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [address search results unsatisfactory](/questions/7413/address-search-results-unsatisfactory)

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
<span id="post-7413-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7413-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-7413-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been noticing frequent address searches that do not give a satisfactory answer.</p>
<p>Example: "Harris Place, Seaton, SA, Australia" the street appears to exist and is labelled on the map but does not return a result in the search. In face searching any street name within Seaton seems to return a negative search result, even the main roads bordering it. The only time I get a result is by limiting the search to the suburb name "seaton, sa" (and state, etc.) only.</p>
<p>Is the database of these names not being indexed or cataloged properly for searching?</p>
<p>I do not understand why the search nominated above gives partially matching results for other states when I have clearly nominated the state. For example, I am given &gt;40,000 finds which link to places like "Seaton Road, Highett, VIC". If seaton is a known suburb name, why does it become a street name in the search results? The problem I have with this is that giving more than 10 or 20 search result options is pointless because you cannot possibly check through a list that long. I don't understand why they are all obviously nowhere near the intended search but showing up as a search result.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-problem" rel="tag" title="see questions tagged &#39;problem&#39;">problem</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Aug '11, 08:15</strong></p>
<img src="https://secure.gravatar.com/avatar/2cd52c0a4d2e49b0707e288e1810d79d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wbdeejay&#39;s gravatar image" />
<p><span>wbdeejay</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wbdeejay has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Aug '11, 08:31</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span></p>
</div>
</div>
<div id="comments-container-7413" class="comments-container">
&#10;</div>
<div id="comment-tools-7413" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7413-form-container" class="comment-form-container">
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

<span id="7419"></span>

<div id="answer-container-7419" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7419-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7419-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-7419-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wbdeejay has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the examples you have given you are using codes for Australian states. I am not aware of Nominatim having the ability to recognise such codes (or indeed those for US states).</p>
<p>Searching for "Harris Place, Seaton" returns an immediate result, as does "Harris Place, South Australia". I therefore suspect that adding state codes is throwing the Nominatim search.</p>
<p>There are a number of reasons why Nominatim does not try to match such codes:</p>
<ul>
<li>Overlapping codes in different countries and codes for internal states/districts/regions which clash with country codes (e.g., is DE Delaware or ISO country code for Germany).</li>
<li>Absence of abbreviated codes in OSM. The OSM philosophy is not to store abbreviations, and Nominatim mainly uses core OSM data.</li>
<li>Available people to code and maintain the software.</li>
</ul>
<p>Additionally, Nominatim is aimed at finding short search terms rather than full address strings. It is rare for OSM data to contain full address information and often this is derived from boundary and other geographical information in OSM (often with problems when boundaries are accidentally broken or place information is inconsistently or incompletely mapped, see other questions on this site related to Nominatim).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Aug '11, 12:16</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-7419" class="comments-container">
<span id="7428"></span>
<div id="comment-7428" class="comment">
<div id="post-7428-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the explanation. That helps me out a lot and and answers my queries perfectly.</p>
</div>
<div id="comment-7428-info" class="comment-info">
<span class="comment-age">(30 Aug '11, 01:05)</span> <span class="comment-user userinfo">wbdeejay</span>
</div>
</div>
</div>
<div id="comment-tools-7419" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7419-form-container" class="comment-form-container">
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

