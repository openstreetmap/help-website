+++
type = "question"
title = "How can I convert a location to lat/long in jquery?"
description = '''HI, I want to convert location to lat/long in jquery. Thanks, Vivek'''
date = "2010-10-28T13:14:00Z"
lastmod = "2010-10-31T23:22:00Z"
weight = 1350
keywords = [ "latitude" ]
aliases = [ "/questions/1350" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I convert a location to lat/long in jquery?](/questions/1350/how-can-i-convert-a-location-to-latlong-in-jquery)

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
<span id="post-1350-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1350-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1350-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>HI,</p>
<p>I want to convert location to lat/long in jquery.</p>
<p>Thanks, Vivek</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-latitude" rel="tag" title="see questions tagged &#39;latitude&#39;">latitude</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Oct '10, 13:14</strong></p>
<img src="https://secure.gravatar.com/avatar/af488a6cddd21b91f3f2bee3c2e842e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vivek%20Kumar&#39;s gravatar image" />
<p><span>Vivek Kumar</span><br />
<span class="score" title="15 reputation points">15</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vivek Kumar has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Nov '10, 23:06</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span></p>
</div>
</div>
<div id="comments-container-1350" class="comments-container">
<span id="1351"></span>
<div id="comment-1351" class="comment">
<div id="post-1351-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Can you detail your need and your context, please.</p>
</div>
<div id="comment-1351-info" class="comment-info">
<span class="comment-age">(28 Oct '10, 15:52)</span> <span class="comment-user userinfo">frodrigo</span>
</div>
</div>
<span id="1352"></span>
<div id="comment-1352" class="comment">
<div id="post-1352-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, I have two text box called from and to and I am inserting location in it. Suppose from text box has France and to text box england, now I want to convert from location to latitude /longitude and as well as to location to latitude and longitude. how we can do that.</p>
<p>I want to do in j query. Thanks for your reply.</p>
</div>
<div id="comment-1352-info" class="comment-info">
<span class="comment-age">(28 Oct '10, 16:57)</span> <span class="comment-user userinfo">Vivek Kumar</span>
</div>
</div>
</div>
<div id="comment-tools-1350" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1350-form-container" class="comment-form-container">
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

<span id="1390"></span>

<div id="answer-container-1390" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1390-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1390-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-1390-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="http://nroets.dev.openstreetmap.org/demo/?lat=52.32796&amp;lon=5.62046&amp;zoom=17&amp;layers=B000FTFT"></a><a href="http://Osm.org"></a><a href="http://Osm.org">Osm.org</a> Routing Demo does exactly this by sending a JSONP request to Nominatim. You can grab a <a href="http://nroets.dev.openstreetmap.org/">tarball</a> and look in yours.js.</p>
<p>If Nominatim returns more than one result, the first one is used. It has a number of drawbacks. For example, when searching for a large city, the first result may be a border that is quite far from the actual city center.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '10, 23:22</strong></p>
<img src="https://secure.gravatar.com/avatar/d25927545eb18b4d577280081df5ce6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nic%20Roets&#39;s gravatar image" />
<p><span>Nic Roets</span><br />
<span class="score" title="583 reputation points">583</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nic Roets has one accepted answer">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Nov '10, 00:37</strong> </span></p>
</div>
</div>
<div id="comments-container-1390" class="comments-container">
&#10;</div>
<div id="comment-tools-1390" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1390-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1354"></span>

<div id="answer-container-1354" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1354-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1354-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1354-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your problem is called <a href="http://en.wikipedia.org/wiki/Geocoding">geocoding</a> and there are various tools and APIs which can help you with that. You could use Nominatim, I guess, or see e.g. <a href="http://developer.yahoo.com/geo/placefinder/">Yahoo! PlaceFinder</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Oct '10, 17:13</strong></p>
<img src="https://secure.gravatar.com/avatar/0fd8741b4be6c04afa858c936e62b499?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mormegil&#39;s gravatar image" />
<p><span>Mormegil</span><br />
<span class="score" title="30 reputation points">30</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mormegil has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1354" class="comments-container">
<span id="1359"></span>
<div id="comment-1359" class="comment">
<div id="post-1359-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi ,thanks for the reply</p>
<p>Do you have any example related to open layer.</p>
</div>
<div id="comment-1359-info" class="comment-info">
<span class="comment-age">(29 Oct '10, 10:21)</span> <span class="comment-user userinfo">Vivek Kumar</span>
</div>
</div>
</div>
<div id="comment-tools-1354" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1354-form-container" class="comment-form-container">
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

