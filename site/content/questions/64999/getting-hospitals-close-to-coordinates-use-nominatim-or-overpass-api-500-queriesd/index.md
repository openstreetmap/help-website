+++
type = "question"
title = "getting hospitals close to coordinates: use Nominatim or Overpass API (&lt;500 queries/d)?"
description = '''I&#x27;ve been reading about using openstreetmap to get hospitals near GPS coordinates but I have become a little confused. It looks like there is the Nominatim and the Overpass API. I&#x27;m not sure which one I should be using. Right now I am doing about 100 queries a day, the most I expect in a day is 500....'''
date = "2018-07-29T09:33:00Z"
lastmod = "2020-10-29T14:29:00Z"
weight = 64999
keywords = [ "usage", "query", "hospital", "coordinates", "poi" ]
aliases = [ "/questions/64999" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [getting hospitals close to coordinates: use Nominatim or Overpass API (\<500 queries/d)?](/questions/64999/getting-hospitals-close-to-coordinates-use-nominatim-or-overpass-api-500-queriesd)

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
<span id="post-64999-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64999-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64999-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been reading about using openstreetmap to get hospitals near GPS coordinates but I have become a little confused. It looks like there is the Nominatim and the Overpass API. I'm not sure which one I should be using.</p>
<p>Right now I am doing about 100 queries a day, the most I expect in a day is 500.</p>
<p>Should I be using Nominatim or Overpass API for my task?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-usage" rel="tag" title="see questions tagged &#39;usage&#39;">usage</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-hospital" rel="tag" title="see questions tagged &#39;hospital&#39;">hospital</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jul '18, 09:33</strong></p>
<img src="https://secure.gravatar.com/avatar/4f6e295d4a3e0e24268e948e79eae3fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dave4784&#39;s gravatar image" />
<p><span>Dave4784</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dave4784 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jul '18, 21:38</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-64999" class="comments-container">
&#10;</div>
<div id="comment-tools-64999" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64999-form-container" class="comment-form-container">
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

<span id="65002"></span>

<div id="answer-container-65002" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65002-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65002-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-65002-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Dave4784 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Both may suit your task, it really depends what type of information you want.</p>
<p>Nominatim returns an object with a hierarchy of location information; Overpass will give you the basic OSM objects as they are tagged.</p>
<p>Both are volunteer maintained services run on OSMF or other non-profit servers, so you should make no assumptions about likely service levels. Availability for uses such as yours entirely depends on whether servers are overloaded or not.</p>
<p>Note that around 150k objects have been mapped as hospitals on OSM, but many of these, particularly in poorer parts of the world, may be other health care facilties (clinics, general practices etc) rather than hospitals with in-patient facilities, and specialist surgeons and physicians.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jul '18, 12:08</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-65002" class="comments-container">
&#10;</div>
<div id="comment-tools-65002" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65002-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="77311"></span>

<div id="answer-container-77311" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77311-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77311-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77311-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>hi there</p>
<p>by the way iin openstreetmap-solutions it is like so:</p>
<ul>
<li>to construct a query, that helps to get "hospitals" which is a special phrase according to this link</li>
</ul>
<p>Here's an example Overpass-API query that returns hospitals within a 10 Km radius of that location.</p>
<pre><code>[out:json][timeout:25];
nwr(around:10000,40.40,-79.93)[&quot;amenity&quot;=&quot;hospital&quot;];
out center;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Oct '20, 14:29</strong></p>
<img src="https://secure.gravatar.com/avatar/600fc90e36ff81dfaba666708cf91dc5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tagtheworld&#39;s gravatar image" />
<p><span>tagtheworld</span><br />
<span class="score" title="0 reputation points">0</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tagtheworld has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77311" class="comments-container">
&#10;</div>
<div id="comment-tools-77311" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77311-form-container" class="comment-form-container">
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

