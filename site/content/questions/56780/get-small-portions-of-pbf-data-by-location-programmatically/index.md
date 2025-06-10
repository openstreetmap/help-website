+++
type = "question"
title = "Get small portions of PBF data by location programmatically"
description = '''I am building a mobile Android app with use of geodata. I wouldn&#x27;t like to setup my own server for geodata but rather to use an existing and preferably free of charge service. I am estimating the feasibility of OpenStreetMap data usage.  The app shall request POI(some specific tag or group of tags) ...'''
date = "2017-06-27T18:47:00Z"
lastmod = "2017-07-04T16:57:00Z"
weight = 56780
keywords = [ "mobile", "android", "pbf", "api" ]
aliases = [ "/questions/56780" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Get small portions of PBF data by location programmatically](/questions/56780/get-small-portions-of-pbf-data-by-location-programmatically)

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
<span id="post-56780-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56780-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-56780-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am building a mobile Android app with use of geodata. I wouldn't like to setup my own server for geodata but rather to use an existing and preferably free of charge service. I am estimating the feasibility of OpenStreetMap data usage.</p>
<p>The app shall request POI(some specific tag or group of tags) or raw data for about 100 pre-saved GPS (longitude/latitude) locations in batch mode once/twice a year for different geolocations spanning from a city to a few countries. All the data processing is planned to happen on the mobile device and thus the size of the downloaded geodata should be as small as possible to cover the processing needs.</p>
<p>Google Places would be good but they only provide POI data for current location of the app and don't allow/have tools for batch POI download.</p>
<p>As far as I could conclude from the Wiki, PBF fileblocks contain 8M OSM entities, which could match my app needs being these files retrievable on files granularity but I was unable to apprehend if this is the state and if yes, whether there is any provider and API which provide this functionality.</p>
<p>Will be grateful for direction.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mobile" rel="tag" title="see questions tagged &#39;mobile&#39;">mobile</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jun '17, 18:47</strong></p>
<img src="https://secure.gravatar.com/avatar/75be6e34ae07f5150969ae5ff7b96879?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chainastole&#39;s gravatar image" />
<p><span>Chainastole</span><br />
<span class="score" title="33 reputation points">33</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chainastole has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jun '17, 17:05</strong> </span></p>
</div>
</div>
<div id="comments-container-56780" class="comments-container">
<span id="56785"></span>
<div id="comment-56785" class="comment">
<div id="post-56785-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Take a look at Overpass API.</p>
</div>
<div id="comment-56785-info" class="comment-info">
<span class="comment-age">(28 Jun '17, 10:16)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-56780" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56780-form-container" class="comment-form-container">
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

<span id="56880"></span>

<div id="answer-container-56880" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56880-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56880-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-56880-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ul>
<li>Please do not use answers to expand or comment on questions.</li>
<li>Your fixation on PBF format for transferring data from your proposed servers is misguided (that is the polite version), using geojosn, OSM xml or other far simpler formats makes a lot more sense. PARTICULARLY if you are a "beginner level hobby programmer on the base of spare time".</li>
<li>a simple way of achieving what you want to do (without the PBF bit) would be to use queries to one of the public <a href="http://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API servers</a>, but naturally there are many ways to skin a cat.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jul '17, 16:57</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jul '17, 22:25</strong> </span></p>
</div>
</div>
<div id="comments-container-56880" class="comments-container">
&#10;</div>
<div id="comment-tools-56880" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56880-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="56853"></span>

<div id="answer-container-56853" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56853-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56853-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56853-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't think you should look at blocks in the PBF file. You can use your own server and import the OSM data into a database and then write your own API which can then return whatever you want.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jul '17, 14:37</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-56853" class="comments-container">
&#10;</div>
<div id="comment-tools-56853" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56853-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="56879"></span>

<div id="answer-container-56879" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56879-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56879-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56879-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is exactly what I wouldn't like to do. I am looking for ways to make stand-alone mobile app with all external services provided by others. I am a beginner level hobby programmer on the base of spare time and would like to start from one operational system - one language project to be able to finish at least something. I thought there is a way to get some specific data from OpenStreetMap already implemented.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jul '17, 15:09</strong></p>
<img src="https://secure.gravatar.com/avatar/75be6e34ae07f5150969ae5ff7b96879?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chainastole&#39;s gravatar image" />
<p><span>Chainastole</span><br />
<span class="score" title="33 reputation points">33</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chainastole has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jul '17, 15:09</strong> </span></p>
</div>
</div>
<div id="comments-container-56879" class="comments-container">
&#10;</div>
<div id="comment-tools-56879" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56879-form-container" class="comment-form-container">
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

