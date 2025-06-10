+++
type = "question"
title = "Adding paths to roads"
description = '''Hello, Is there a way to add pavements/paths to the sides of roads? I use OSM to create courses in Garmin Connect and found a difference between the course distance and the actual run distance for a race I ran (e.g. course in OSM showed 5.1km so thought I&#x27;d run 5.1km and set a 5km PB to find I&#x27;d onl...'''
date = "2020-07-22T10:14:00Z"
lastmod = "2020-07-22T13:12:00Z"
weight = 75847
keywords = [ "course", "pavement", "routing", "road", "paths" ]
aliases = [ "/questions/75847" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Adding paths to roads](/questions/75847/adding-paths-to-roads)

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
<span id="post-75847-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75847-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75847-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>Is there a way to add pavements/paths to the sides of roads?</p>
<p>I use OSM to create courses in Garmin Connect and found a difference between the course distance and the actual run distance for a race I ran (e.g. course in OSM showed 5.1km so thought I'd run 5.1km and set a 5km PB to find I'd only ran 4.9km). I understand GPS accuracy and accuracy of OSM will have contributed to the difference but I also spotted that OSM assumes I travel down the centre of the road rather than to the side of the road, e.g. on a pavement. Running the same stretch of road several times as part of a planned course amplifies the difference between OSM and the reality of running on the side of a road.</p>
<p>If it is not currently possible to add paths/pavements to roads in OSM, it would be a good addition so that OSM safely routes different users accordingly and so that planned courses/distances better match the real run/walk/hike.</p>
<p>Any advice appreciated.</p>
<p>thanks,</p>
<p>nick</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-course" rel="tag" title="see questions tagged &#39;course&#39;">course</span> <span class="post-tag tag-link-pavement" rel="tag" title="see questions tagged &#39;pavement&#39;">pavement</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-paths" rel="tag" title="see questions tagged &#39;paths&#39;">paths</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jul '20, 10:14</strong></p>
<img src="https://secure.gravatar.com/avatar/ad9dea05b4d843abfa3aa5ef30e8056c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nicholas_rubin&#39;s gravatar image" />
<p><span>Nicholas_rubin</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nicholas_rubin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75847" class="comments-container">
&#10;</div>
<div id="comment-tools-75847" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75847-form-container" class="comment-form-container">
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

<span id="75851"></span>

<div id="answer-container-75851" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75851-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75851-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75851-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yours is an interesting addition to the various use-cases for mapping pavements (en-GB)/ sidewalks (en-US) separately. Most others relate to access for those with limited sight or mobility. However, for a range of reasons many prefer to attach information about the properties of sidewalks to the way representing the road centreline.</p>
<p>You could using a GIS tool create additional ways parallel to the roads offset by the distance between the centreline and the centre of the sidewalk, and use these for calculating actual distance. In principle this could be done of a large scale, but it always tends to run into the fact that correctly connecting ways in OSM's joined up data model is not readily automatable (see Richard Fairhurst's recent paper on OSM for data owners). It might actually be easier just to calculate a parameter to scale the distance for each route segment.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jul '20, 13:12</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-75851" class="comments-container">
&#10;</div>
<div id="comment-tools-75851" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75851-form-container" class="comment-form-container">
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

