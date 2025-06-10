+++
type = "question"
title = "Maps not showing streets in Production"
description = '''We are using the openstreetmap.org in our web application. The maps are working fine on the windows computer. We have recently tried to open the app on the microsoft surface pros and the maps are not showing the street details. What I found strange is the maps are working fine in the QA environment ...'''
date = "2021-05-07T14:21:00Z"
lastmod = "2021-05-07T18:08:00Z"
weight = 80051
keywords = [ "maps" ]
aliases = [ "/questions/80051" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Maps not showing streets in Production](/questions/80051/maps-not-showing-streets-in-production)

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
<span id="post-80051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80051-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We are using the openstreetmap.org in our web application. The maps are working fine on the windows computer. We have recently tried to open the app on the microsoft surface pros and the maps are not showing the street details. What I found strange is the maps are working fine in the QA environment on the Surface pro but the streets are missing in the Production. Do we need to add an API key or do we need to change any setting on the surface pro?Any help is appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-maps" rel="tag" title="see questions tagged &#39;maps&#39;">maps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 May '21, 14:21</strong></p>
<img src="https://secure.gravatar.com/avatar/5e3b15f8455ff9ecc7ceecf0fa24760a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SwathiNimas&#39;s gravatar image" />
<p><span>SwathiNimas</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SwathiNimas has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80051" class="comments-container">
<span id="80054"></span>
<div id="comment-80054" class="comment">
<div id="post-80054-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You'll need to provide more information about how you're using the OSM data. Are you rendering a map background? If so, vector or raster? Which software package?</p>
</div>
<div id="comment-80054-info" class="comment-info">
<span class="comment-age">(07 May '21, 17:00)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="80055"></span>
<div id="comment-80055" class="comment">
<div id="post-80055-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Alester, we are rendering the map in the background of the application. It is a .net application. We are using the vector images.</p>
</div>
<div id="comment-80055-info" class="comment-info">
<span class="comment-age">(07 May '21, 17:07)</span> <span class="comment-user userinfo">SwathiNimas</span>
</div>
</div>
<span id="80056"></span>
<div id="comment-80056" class="comment">
<div id="post-80056-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/20181/swathinimas">@SwathiNimas</a> That doesn't really help.</p>
<p>Where do you get these "vector images" from (what exact URL)? What error do you get when you try and retrieve them?</p>
</div>
<div id="comment-80056-info" class="comment-info">
<span class="comment-age">(07 May '21, 17:19)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="80057"></span>
<div id="comment-80057" class="comment">
<div id="post-80057-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>We are getting the maps from the <a href="https://www.openstreetmap.org/.">https://www.openstreetmap.org/.</a> The streets are not showing up. I can see the assests(vector images) but not the street names.</p>
</div>
<div id="comment-80057-info" class="comment-info">
<span class="comment-age">(07 May '21, 17:48)</span> <span class="comment-user userinfo">SwathiNimas</span>
</div>
</div>
<span id="80058"></span>
<div id="comment-80058" class="comment">
<div id="post-80058-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>We are getting the maps from the <a href="https://www.openstreetmap.org/">https://www.openstreetmap.org/</a> .</p>
</blockquote>
<p>Can you give the <em>exact</em> URL of what you are trying to display, and how your are accessing that URL? What error do you get when you try and retrieve them? What is different between where it works and where it does not work?</p>
<p>As an aside, if you are using raster map tiles served by OpenStreetMap then you'll need to follow <a href="https://operations.osmfoundation.org/policies/tiles/">https://operations.osmfoundation.org/policies/tiles/</a> . I've no idea if that's relevant though as there's really not enough information to tell yet.</p>
</div>
<div id="comment-80058-info" class="comment-info">
<span class="comment-age">(07 May '21, 18:08)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-80051" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80051-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

