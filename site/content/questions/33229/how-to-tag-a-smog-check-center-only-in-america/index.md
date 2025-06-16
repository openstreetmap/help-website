+++
type = "question"
title = "How to tag a Smog Check Center only, in America?"
description = '''Other than using car_repair, in America what is the best practice for tagging a business that only deals with Smog Center&#x27;s? I was thinking about using smog_center. Thanks'''
date = "2014-05-16T10:30:00Z"
lastmod = "2016-03-24T14:51:00Z"
weight = 33229
keywords = [ "smog", "car_repair", "smog_center" ]
aliases = [ "/questions/33229" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag a Smog Check Center only, in America?](/questions/33229/how-to-tag-a-smog-check-center-only-in-america)

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
<span id="post-33229-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33229-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33229-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Other than using <a href="https://wiki.openstreetmap.org/wiki/Tag:shop%3Dcar_repair">car_repair</a>, in America what is the best practice for tagging a business that only deals with Smog Center's? I was thinking about using smog_center. Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-smog" rel="tag" title="see questions tagged &#39;smog&#39;">smog</span> <span class="post-tag tag-link-car_repair" rel="tag" title="see questions tagged &#39;car_repair&#39;">car_repair</span> <span class="post-tag tag-link-smog_center" rel="tag" title="see questions tagged &#39;smog_center&#39;">smog_center</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 May '14, 10:30</strong></p>
<img src="https://secure.gravatar.com/avatar/c592fa30e4ddc999332a3ebf440e1d81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frankthetankk&#39;s gravatar image" />
<p><span>frankthetankk</span><br />
<span class="score" title="106 reputation points">106</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frankthetankk has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 May '14, 10:31</strong> </span></p>
</div>
</div>
<div id="comments-container-33229" class="comments-container">
<span id="48821"></span>
<div id="comment-48821" class="comment">
<div id="post-48821-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>See also <a href="https://github.com/gravitystorm/openstreetmap-carto/pull/2096">https://github.com/gravitystorm/openstreetmap-carto/pull/2096</a></p>
</div>
<div id="comment-48821-info" class="comment-info">
<span class="comment-age">(24 Mar '16, 14:51)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-33229" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33229-form-container" class="comment-form-container">
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

<span id="33230"></span>

<div id="answer-container-33230" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33230-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33230-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-33230-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><strong>Emission tests</strong>, which is what I presume you mean by a Smog Center, are a standard part of having a road-legal vehicle in many countries. In the UK they are included in the MoT test, and I know the Swiss standards are fairly stringent. Usually these are part of a suite of tests, so something like <code>amenity=vehicle_test_centre</code> (note OSM standard is to use British English) would seem appropriate.</p>
<p>Many car repair/service garages will also offer these tests, in which case shop=car_repair with vehicle_test_centre=yes, would enable garages which also do tests to be separated out. Some in fact specialise in performing the test, with car servicing as a sideline, in which case one could use car_repair=yes. (AFAIK we dont distinguish between places which service cars &amp; those which deal with accident damage repair).</p>
<p>If the facility only carries out one kind of test then use either <code>vehicle_test_centre=emission</code> or perhaps 'namespace' it with <code>vehicle_test_centre:type=emission</code>.</p>
<p>None of these suggested tags are in use, although there are several well-established precedents in similar areas. My main point would be to try and use a tag which works across different countries &amp; jurisdictions: firstly it is likely to get better take-up, and secondly it will make life easier for anyone who wants to use it downstream</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 May '14, 11:16</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-33230" class="comments-container">
&#10;</div>
<div id="comment-tools-33230" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33230-form-container" class="comment-form-container">
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

