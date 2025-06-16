+++
type = "question"
title = "Updating Speed Limits - how quickly will it appear?"
description = '''I noticed some errors in the speed limits in the API which I&#x27;m using for my app. I know the real speed limits of the roads. If I go to the OSM website and update them, how quickly will that update in the API? '''
date = "2016-12-08T20:14:00Z"
lastmod = "2016-12-09T06:51:00Z"
weight = 53392
keywords = [ "speedlimit", "api" ]
aliases = [ "/questions/53392" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Updating Speed Limits - how quickly will it appear?](/questions/53392/updating-speed-limits-how-quickly-will-it-appear)

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
<span id="post-53392-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53392-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53392-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I noticed some errors in the speed limits in the API which I'm using for my app. I know the real speed limits of the roads. If I go to the OSM website and update them, how quickly will that update in the API?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-speedlimit" rel="tag" title="see questions tagged &#39;speedlimit&#39;">speedlimit</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Dec '16, 20:14</strong></p>
<img src="https://secure.gravatar.com/avatar/82502ec5d41c294a75319774761d4ae9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wand&#39;s gravatar image" />
<p><span>Wand</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wand has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53392" class="comments-container">
<span id="53395"></span>
<div id="comment-53395" class="comment">
<div id="post-53395-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>what is "the API" for you? E.g. which URL?</p>
</div>
<div id="comment-53395-info" class="comment-info">
<span class="comment-age">(08 Dec '16, 21:14)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-53392" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53392-form-container" class="comment-form-container">
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

<span id="53394"></span>

<div id="answer-container-53394" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53394-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53394-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53394-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If your app is pulling directly from OSM, the changes should be visible immediately.</p>
<p>But if your app is pulling directly from OSM you might also be treading on thin ice with respect to the terms of service.</p>
<p>If you host your own server then you will have several options on how often that server updates to reflect current OSM data.</p>
<p>For myself, I generate things that I use off line. And I pull from the files at <a href="http://download.geofabrik.de">http://download.geofabrik.de</a> which are updated once a day with the data from what appears to be around 00:00 hrs UTC and it takes about 5 or so hours to get done with the files I normally use.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Dec '16, 21:02</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-53394" class="comments-container">
<span id="53402"></span>
<div id="comment-53402" class="comment">
<div id="post-53402-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Why "treading on the ice"? What terms will I violate?</p>
</div>
<div id="comment-53402-info" class="comment-info">
<span class="comment-age">(08 Dec '16, 23:53)</span> <span class="comment-user userinfo">Wetitpig0</span>
</div>
</div>
<span id="53404"></span>
<div id="comment-53404" class="comment">
<div id="post-53404-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Assuming your app is going to be used by a number of people, you may fall under the "heavy user" category of the terms of use and if so your app may be blocked. See <a href="https://wiki.openstreetmap.org/wiki/API_usage_policy">https://wiki.openstreetmap.org/wiki/API_usage_policy</a></p>
</div>
<div id="comment-53404-info" class="comment-info">
<span class="comment-age">(08 Dec '16, 23:56)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="53405"></span>
<div id="comment-53405" class="comment">
<div id="post-53405-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh! As I always use direct HTTP, I don't realise there are a lot of users using the same app.</p>
</div>
<div id="comment-53405-info" class="comment-info">
<span class="comment-age">(08 Dec '16, 23:59)</span> <span class="comment-user userinfo">Wetitpig0</span>
</div>
</div>
<span id="53423"></span>
<div id="comment-53423" class="comment">
<div id="post-53423-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The editing API is meant for apps to edit OSM, not for apps that only wants to query data Those apps should use e.g. the Overpass API</p>
</div>
<div id="comment-53423-info" class="comment-info">
<span class="comment-age">(09 Dec '16, 06:44)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="53424"></span>
<div id="comment-53424" class="comment">
<div id="post-53424-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I edit by writing the osmChange document manually. That is OK, right?</p>
</div>
<div id="comment-53424-info" class="comment-info">
<span class="comment-age">(09 Dec '16, 06:51)</span> <span class="comment-user userinfo">Wetitpig0</span>
</div>
</div>
</div>
<div id="comment-tools-53394" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53394-form-container" class="comment-form-container">
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

