+++
type = "question"
title = "Plot Maps using OSRM&#x27;s route API response"
description = '''Hi, I want to plot detailed map of OSRM&#x27;s route api response and then compare it with Google Maps. How can I plot the map? I see steps has details of the lat-longs but it&#x27;s plotting incorrectly. What will be the correct way to plot the map? The &quot;geometry&quot; fields in the response look like this: &quot;kjpf...'''
date = "2021-02-08T21:26:00Z"
lastmod = "2021-02-08T23:14:00Z"
weight = 78734
keywords = [ "osrm" ]
aliases = [ "/questions/78734" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Plot Maps using OSRM's route API response](/questions/78734/plot-maps-using-osrms-route-api-response)

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
<span id="post-78734-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78734-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78734-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I want to plot detailed map of OSRM's route api response and then compare it with Google Maps. How can I plot the map? I see steps has details of the lat-longs but it's plotting incorrectly. What will be the correct way to plot the map?</p>
<p>The "geometry" fields in the response look like this: "kjpfG~{dtL?BDUwAKcLfy@cC|PuAbKy@vHa@rEIhAEz@KpBCz@ErA".</p>
<p>I am calling API like this - {{host}}/route/v1/driving/-71.628324,43.178769;-71.979512,43.390553?steps=true</p>
<p>I am attacheding OSRM's map and Google Maps Images. It looks OSRM is not plotting it correctly. Can somebody tell me if there is any issue in OSRM server itself or I am not plotting correctly.</p>
<p><img src="/upfiles/OSRM_Map_5vVW4AH.png" alt="alt text" /> <img src="/upfiles/Google_Map_Hnot35P.png" alt="alt text" /></p>
<p>Edit - After Frederik Ramm's comment, I plotted the lat-long using OSRM's route API. I see the issue, it's plotting on the wrong side of the road after some time. Need help in understanding what is the exact issue here. Here is the screenshot. <img src="/upfiles/OSRM.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Feb '21, 21:26</strong></p>
<img src="https://secure.gravatar.com/avatar/7996417a96c5227404f348e863457405?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mukul2990&#39;s gravatar image" />
<p><span>Mukul2990</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mukul2990 has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Feb '21, 23:07</strong> </span></p>
</div>
</div>
<div id="comments-container-78734" class="comments-container">
&#10;</div>
<div id="comment-tools-78734" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78734-form-container" class="comment-form-container">
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

<span id="78735"></span>

<div id="answer-container-78735" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78735-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78735-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78735-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The geometry in the "geometry" response field is encoded using Google's polyline format. You will need to decode that to get coordinates. There are libraries out there for various programming languages to accomplish that. Alternatively, as per <a href="http://project-osrm.org/docs/v5.23.0/api/">http://project-osrm.org/docs/v5.23.0/api/</a> you can specify "coordinates=geojson" to receive the coordinates in a GeoJSON format instead.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Feb '21, 21:35</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</img>
</div>
</div>
<div id="comments-container-78735" class="comments-container">
<span id="78738"></span>
<div id="comment-78738" class="comment">
<div id="post-78738-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I can't find geometry field with value "kjpfG~{dtL?BDUwAKcLfy@cC|PuAbKy@vHa@rEIhAEz@KpBCz@ErA" in my response. My response has 11 geometry fields. Which level field of geometry can be used?</p>
<p>I tried this - <a href="https://developers.google.com/maps/documentation/utilities/polylineutility">https://developers.google.com/maps/documentation/utilities/polylineutility</a></p>
<p>but it's returning incorrect route if compared to Google Maps route for the same lat-long</p>
</div>
<div id="comment-78738-info" class="comment-info">
<span class="comment-age">(08 Feb '21, 22:04)</span> <span class="comment-user userinfo">Mukul2990</span>
</div>
</div>
<span id="78739"></span>
<div id="comment-78739" class="comment">
<div id="post-78739-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry for the confusion, you had posted a very long API response that was unreadable, and I reduced that to what I thought was key. For a best-precision result, try passing in the parameter <code>overview=full</code>. Then in the response, check for an array called <code>routes</code>, choose the first element of that, and in there you will find a <code>geometry</code> field. Use that.</p>
</div>
<div id="comment-78739-info" class="comment-info">
<span class="comment-age">(08 Feb '21, 22:15)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="78740"></span>
<div id="comment-78740" class="comment">
<div id="post-78740-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for the quick response. I have updated some details in the question. I am still getting wrong path if I plot using geometry field.</p>
</div>
<div id="comment-78740-info" class="comment-info">
<span class="comment-age">(08 Feb '21, 22:34)</span> <span class="comment-user userinfo">Mukul2990</span>
</div>
</div>
<span id="78741"></span>
<div id="comment-78741" class="comment">
<div id="post-78741-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Try dropping the <code>steps=true</code>, and add an <code>overview=full</code>. Try the <code>geometries=geojson</code> just to avoid any potential problems with the polyline encoding.</p>
</div>
<div id="comment-78741-info" class="comment-info">
<span class="comment-age">(08 Feb '21, 22:39)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="78742"></span>
<div id="comment-78742" class="comment">
<div id="post-78742-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Frederik, I plotted the map, it's going on the wrong side of the highway after lat-long 271. Please check the attached image in the question. Do you know what's wrong here?</p>
</div>
<div id="comment-78742-info" class="comment-info">
<span class="comment-age">(08 Feb '21, 23:09)</span> <span class="comment-user userinfo">Mukul2990</span>
</div>
</div>
<span id="78743"></span>
<div id="comment-78743" class="comment not_top_scorer">
<div id="post-78743-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't know what is wrong but is this still with the polyline, or with GeoJSON? Because polyline AFAIK uses a differential encoding which, if there's a bug, can lead to funny results like the one you have - route somehow jumps to a wrong place, but then continues "as if" on a road. That's why I recommended GeoJSON just to make sure the bug isn't in the polyline decoding.</p>
</div>
<div id="comment-78743-info" class="comment-info">
<span class="comment-age">(08 Feb '21, 23:13)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="78744"></span>
<div id="comment-78744" class="comment not_top_scorer">
<div id="post-78744-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I plotted this path using geojson as you suggested. Is there other way to validate the lat-longs?</p>
</div>
<div id="comment-78744-info" class="comment-info">
<span class="comment-age">(08 Feb '21, 23:14)</span> <span class="comment-user userinfo">Mukul2990</span>
</div>
</div>
</div>
<div id="comment-tools-78735" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-78735-form-container" class="comment-form-container">
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

