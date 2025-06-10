+++
type = "question"
title = "GEO tracking on Android APP&#x27;s in China - Known issues with Google Play services location API&#x27;s in china?"
description = '''Hi, Does anyone know if any known issues with location tracking using Android&#x27;s in china?  We will be implementing OpenStreetMap API. Android OS will track user location and send the info to the map. We are not sure if there are specific restrictions in China region regarding location tracking using...'''
date = "2017-12-07T01:11:00Z"
lastmod = "2017-12-07T09:58:00Z"
weight = 61061
keywords = [ "services", "android", "google", "china", "play" ]
aliases = [ "/questions/61061" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [GEO tracking on Android APP's in China - Known issues with Google Play services location API's in china?](/questions/61061/geo-tracking-on-android-apps-in-china-known-issues-with-google-play-services-location-apis-in-china)

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
<span id="post-61061-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61061-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61061-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Does anyone know if any known issues with location tracking using Android's in china?</p>
<p>We will be implementing OpenStreetMap API. Android OS will track user location and send the info to the map. We are not sure if there are specific restrictions in China region regarding location tracking using Google Play services location APIs (which is Android OS location tracking service).</p>
<p>Any comments would be appreciated!</p>
<p>Thank you</p>
<p>Johnathan</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-services" rel="tag" title="see questions tagged &#39;services&#39;">services</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-google" rel="tag" title="see questions tagged &#39;google&#39;">google</span> <span class="post-tag tag-link-china" rel="tag" title="see questions tagged &#39;china&#39;">china</span> <span class="post-tag tag-link-play" rel="tag" title="see questions tagged &#39;play&#39;">play</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Dec '17, 01:11</strong></p>
<img src="https://secure.gravatar.com/avatar/6292a0569fc283fb3e0ff566d55d0eb4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lindero&#39;s gravatar image" />
<p><span>Lindero</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lindero has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61061" class="comments-container">
&#10;</div>
<div id="comment-tools-61061" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61061-form-container" class="comment-form-container">
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

<span id="61065"></span>

<div id="answer-container-61065" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61065-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61065-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-61065-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You likely need to ask on an Android developers forum or google themselves for a proper answer, it could well be that due to the government required warping of location information in China that anything officially sanctioned will not really work with OSM data.</p>
<p>Note: while google wants you to use the google play services to obtain location information (for obvious reasons). You don't actually have to and can simply use <a href="https://developer.android.com/reference/android/location/package-summary.html">https://developer.android.com/reference/android/location/package-summary.html</a> The disadvantage is that you wont have access to the bells and whistles, but on the other hand wont be giving google your users data and wont be dependent on them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Dec '17, 09:58</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-61065" class="comments-container">
&#10;</div>
<div id="comment-tools-61065" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61065-form-container" class="comment-form-container">
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

