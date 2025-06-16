+++
type = "question"
title = "Underlay accuracy: Bing aerial vs MapBox satellite imagery"
description = '''Greetings! Relative noob to OSM here, but long-time mapping and digital cartography enthusiast... I recently got involved in OSM as part of a Red Cross volunteer effort to map the capital of Malawi and its environs - and I&#x27;ve been continuing to flesh out that area on my own time, as they have VERY l...'''
date = "2016-10-18T20:52:00Z"
lastmod = "2016-10-21T07:55:00Z"
weight = 52594
keywords = [ "aerial_imagery", "satellite", "accuracy", "bing", "mapbox" ]
aliases = [ "/questions/52594" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Underlay accuracy: Bing aerial vs MapBox satellite imagery](/questions/52594/underlay-accuracy-bing-aerial-vs-mapbox-satellite-imagery)

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
<span id="post-52594-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52594-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52594-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Greetings!<br />
Relative noob to OSM here, but long-time mapping and digital cartography enthusiast...<br />
I recently got involved in OSM as part of a Red Cross volunteer effort to map the capital of Malawi and its environs - and I've been continuing to flesh out that area on my own time, as they have VERY little GPS-equipped ground surveying.<br />
The original volunteer effort was unfortunately using outdated Bing imagery as its base - I've since found that it's at least 5-6 years out of date. The MapBox satellite imagery is much more recent... But there's a bit of skew between both sources (I assume because of low rate of image sampling), and I don't see guidelines on which source to default to (if any) when there are very few GPS traces available to use.<br />
It's clear that this skew is purely local - but knowing that one source tends to sample far more heavily than the other would lead me to choose that imagery source as the more authoritative one.</p>
<p>Thx in advance...<br />
GR</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-aerial_imagery" rel="tag" title="see questions tagged &#39;aerial_imagery&#39;">aerial_imagery</span> <span class="post-tag tag-link-satellite" rel="tag" title="see questions tagged &#39;satellite&#39;">satellite</span> <span class="post-tag tag-link-accuracy" rel="tag" title="see questions tagged &#39;accuracy&#39;">accuracy</span> <span class="post-tag tag-link-bing" rel="tag" title="see questions tagged &#39;bing&#39;">bing</span> <span class="post-tag tag-link-mapbox" rel="tag" title="see questions tagged &#39;mapbox&#39;">mapbox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Oct '16, 20:52</strong></p>
<img src="https://secure.gravatar.com/avatar/31ab4a3a30ec105540eb6d56c8ad98c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GregRetro&#39;s gravatar image" />
<p><span>GregRetro</span><br />
<span class="score" title="354 reputation points">354</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GregRetro has 3 accepted answers">50%</span> </br></br></p>
</div>
</div>
<div id="comments-container-52594" class="comments-container">
<span id="52596"></span>
<div id="comment-52596" class="comment">
<div id="post-52596-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Jeez. Just realized my question was missing an important point... By "skew", I mean that Mapbox and Bing data doesn't line up identically when using them as background. Sometimes the OSM data lines up with Bing, sometimes MapBox, sometimes neither. Hopefully that helps.</p>
<p>GR</p>
</div>
<div id="comment-52596-info" class="comment-info">
<span class="comment-age">(18 Oct '16, 23:53)</span> <span class="comment-user userinfo">GregRetro</span>
</div>
</div>
</div>
<div id="comment-tools-52594" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52594-form-container" class="comment-form-container">
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

<span id="52597"></span>

<div id="answer-container-52597" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52597-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52597-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-52597-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="GregRetro has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Using JOSM, I downloaded the gps traces and loaded the Strava Heatmap imagery for the Lilongwe area. The shift between Bing and Mapbox was only a few metres for areas I checked which seems to be the same as in the areas I normally map. If there is a particular area that is badly affected, you could contact the local Red Cross and ask if they could upload local gpx traces to sort out which imagery is better located. I know of no other method to align the satellite imagery other than using local gps traces and the Strava Heatmap. JOSM allows the downloading of a much bigger area if you choose to download only the 'Raw GPS data', then add the imagery to discern which of Bing and Mapbox is best locally. You can also right-click the satellite layer to realign each of them to a best fit with the gps and Strava data before downloading the osm data to begin mapping. <img src="/upfiles/Screen_Shot_2016-10-19_at_12.14.55_PM.png" alt="Screen Image" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Oct '16, 03:40</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span> </br></br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Oct '16, 06:10</strong> </span></p>
</div>
</div>
<div id="comments-container-52597" class="comments-container">
<span id="52625"></span>
<div id="comment-52625" class="comment">
<div id="post-52625-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks very much, nevw...<br />
Realized there were more GPS traces there than I thought - just none where I was working. (in the NW of the screenshotted map).<br />
I've also started finding traces there that are so far removed from either aerial source that I'm suspecting that the generating device was mis-calibrated or something. Yay fun.<br />
I'm looking forward to working in JOSM, where it sounds like much of this issue is easier resolved. Thx again for your time!</p>
<p>GR</p>
</div>
<div id="comment-52625-info" class="comment-info">
<span class="comment-age">(21 Oct '16, 07:55)</span> <span class="comment-user userinfo">GregRetro</span>
</div>
</div>
</div>
<div id="comment-tools-52597" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52597-form-container" class="comment-form-container">
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

