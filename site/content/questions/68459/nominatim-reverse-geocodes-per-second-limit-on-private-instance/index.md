+++
type = "question"
title = "Nominatim - reverse geocodes per second limit on private instance"
description = '''Hi All Considering I have a private instance of the world with 96gb ram Is there a theoretical limit per second on how many reverse geocodes per second (with road speed) is possible? I saw a limit of around 25/sec with 48gb ram, and i&#x27;m wondering if with whatever spec I can scale to 500 per second I...'''
date = "2019-03-23T00:32:00Z"
lastmod = "2019-03-25T11:33:00Z"
weight = 68459
keywords = [ "nominatim" ]
aliases = [ "/questions/68459" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim - reverse geocodes per second limit on private instance](/questions/68459/nominatim-reverse-geocodes-per-second-limit-on-private-instance)

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
<span id="post-68459-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68459-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68459-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All Considering I have a private instance of the world with 96gb ram</p>
<p>Is there a theoretical limit per second on how many reverse geocodes per second (with road speed) is possible?</p>
<p>I saw a limit of around 25/sec with 48gb ram, and i'm wondering if with whatever spec I can scale to 500 per second</p>
<p>Is this a figure that is just unrealistic on one server? or possible? Does anyone have any approx figures of what might be possible per sec?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Mar '19, 00:32</strong></p>
<img src="https://secure.gravatar.com/avatar/629c67b24fafaf747f4410cfbc7f1fc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mark%20Davies1664&#39;s gravatar image" />
<p><span>Mark Davies1664</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mark Davies1664 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68459" class="comments-container">
&#10;</div>
<div id="comment-tools-68459" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68459-form-container" class="comment-form-container">
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

<span id="68460"></span>

<div id="answer-container-68460" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68460-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68460-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68460-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Many systems that have requirements like that are badly designed - for example, I have seen in-car location trackers that would transmit their location every second and a backend that would reverse geocode them all even if the location had only changed by 3 centimetres since the last transmission, or it would geocode them all even if nobody was looking. In many cases, a clever re-design can bring down the number of reverse geocoding queries by a factor of 10 or even 100 without any UI degradation.</p>
<p>I haven't yet build a 500 query/second server but if I wanted to, I would probably build a machine that holds the complete database in RAM, and take steps to minimize the size of the database - not only to save $$$ on RAM but also for increased performance. For example, import only data for areas you will actually be using. If you know that 95% of your queries will be within country A but you want to support world-wide queries nonetheless, then build a super-fast RAM-only server serving only the rectangle that contains country A, and forward queries outside to a slower, world-wide server. If you don't need house numbers, don't import them, and so on.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Mar '19, 10:04</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-68460" class="comments-container">
<span id="68471"></span>
<div id="comment-68471" class="comment">
<div id="post-68471-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks, that is an interesting reply in regarding to caching. I'm already discarding geocoding if the movement is less than 10 meters to limit the amount of requests. I've also seen another geocoder called photon which claims to be faster.</p>
<p>my application is vehicle tracking, and i need just roadnames and roadspeed so not sure if there is any other data in the DB that is bloating the data set that I can safely remove, I'm using roadspeed data on every lookup to check for incidents of overspeeding so if i move it to UI based rather than data import, I lose that functionality.</p>
</div>
<div id="comment-68471-info" class="comment-info">
<span class="comment-age">(25 Mar '19, 05:29)</span> <span class="comment-user userinfo">Mark Davies1664</span>
</div>
</div>
<span id="68472"></span>
<div id="comment-68472" class="comment">
<div id="post-68472-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Nominatim contains buildings and address points which would seem useless to you. I'm not sure if simply deleting them is a good way forward, as it is likely to first search for a building/address point and only if that is not found will it fall back to searching for a street, so even if you delete buildings there'll be some time wasted here. Perhaps it makes sense for you to dive a bit deeper into the source and try to eliminate checking for buildings in the first place. -- Having said that, a geocoder is not the best tool for your task since it will give you the nearest road to the GPS fix, rather than the road most likely travelled on. You will have many false alerts when e.g. a fast road is used and your GPS is just a little off near an intersection and you'll match the slower road. More reliable/stable results can be had from a routing engine's track matching feature.</p>
</div>
<div id="comment-68472-info" class="comment-info">
<span class="comment-age">(25 Mar '19, 07:00)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="68480"></span>
<div id="comment-68480" class="comment">
<div id="post-68480-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Frederik, can you suggest some areas for me to start looking for a routing engine?</p>
</div>
<div id="comment-68480-info" class="comment-info">
<span class="comment-age">(25 Mar '19, 11:33)</span> <span class="comment-user userinfo">Mark Davies1664</span>
</div>
</div>
</div>
<div id="comment-tools-68460" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68460-form-container" class="comment-form-container">
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

