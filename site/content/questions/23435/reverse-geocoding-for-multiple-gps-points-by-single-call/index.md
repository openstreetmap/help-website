+++
type = "question"
title = "Reverse Geocoding for multiple gps points by single call"
description = '''Hi all, Is there any way to get multiple gps addresses by &#x27;n&#x27; different lat lon values in a single call to OSM Regards, Kiran V'''
date = "2013-06-17T07:33:00Z"
lastmod = "2013-06-17T10:11:00Z"
weight = 23435
keywords = [ "openstreetmap", "openlayers", "osm" ]
aliases = [ "/questions/23435" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Reverse Geocoding for multiple gps points by single call](/questions/23435/reverse-geocoding-for-multiple-gps-points-by-single-call)

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
<span id="post-23435-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23435-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23435-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>Is there any way to get multiple gps addresses by 'n' different lat lon values in a single call to OSM</p>
<p>Regards, Kiran V</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jun '13, 07:33</strong></p>
<img src="https://secure.gravatar.com/avatar/b804f5576f3607b83d68f3f9dd1f4676?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amkiranv&#39;s gravatar image" />
<p><span>amkiranv</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amkiranv has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-23435" class="comments-container">
&#10;</div>
<div id="comment-tools-23435" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23435-form-container" class="comment-form-container">
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

<span id="23441"></span>

<div id="answer-container-23441" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23441-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23441-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23441-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at this page: <a href="https://wiki.openstreetmap.org/wiki/Nominatim#Reverse_Geocoding_.2F_Address_lookup">https://wiki.openstreetmap.org/wiki/Nominatim#Reverse_Geocoding_.2F_Address_lookup</a> . Nominatim is handling only single query for reverse geocoding. Therefore, it doesn't seem possible.</p>
<p>Lucas</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jun '13, 09:09</strong></p>
<img src="https://secure.gravatar.com/avatar/4015aaa7dcb688fc988901e4caaac771?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kalu06&#39;s gravatar image" />
<p><span>Kalu06</span><br />
<span class="score" title="140 reputation points">140</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kalu06 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-23441" class="comments-container">
<span id="23443"></span>
<div id="comment-23443" class="comment">
<div id="post-23443-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Lucas,</p>
<p>I have a scenario where i have to show address for all gps points. Nominatim is handling only single query for reverse geocoding there fore the response time to display all addresses is taking time. is there any way to solve this. Any suggestion?</p>
<p>Regards, Kiran</p>
</div>
<div id="comment-23443-info" class="comment-info">
<span class="comment-age">(17 Jun '13, 09:32)</span> <span class="comment-user userinfo">amkiranv</span>
</div>
</div>
<span id="23446"></span>
<div id="comment-23446" class="comment">
<div id="post-23446-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Kiran,</p>
<p>You don't control the process <code>reverse.php</code> is doing. So, a solution would be to implement your own reverse.php based on Nominatim's. However I'm pretty sure you won't be able to execute it without being on the same server than the DB's.</p>
<p>Good luck</p>
<p>Cheers, Lucas</p>
</div>
<div id="comment-23446-info" class="comment-info">
<span class="comment-age">(17 Jun '13, 09:45)</span> <span class="comment-user userinfo">Kalu06</span>
</div>
</div>
</div>
<div id="comment-tools-23441" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23441-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="23445"></span>

<div id="answer-container-23445" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23445-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23445-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23445-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can query nominatim maximum 1 request per second, but <a href="https://wiki.openstreetmap.org/wiki/Nominatim_usage_policy#Bulk_Geocoding">Nominatim usage policy</a> frowns upon bulk reverse geocoding. So you are very likely to be blocked if you constantly do one per second.</p>
<p>There are <a href="http://gis.stackexchange.com/questions/21382/bulk-geocode-20-million-records">other solutions</a>, but they will cost you in time and money.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jun '13, 09:44</strong></p>
<img src="https://secure.gravatar.com/avatar/dd3858f5f89f5a6b738f9dbe59824440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emj&#39;s gravatar image" />
<p><span>emj</span><br />
<span class="score" title="2024 reputation points"><span>2.0k</span></span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emj has 11 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-23445" class="comments-container">
<span id="23451"></span>
<div id="comment-23451" class="comment">
<div id="post-23451-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>(for the avoidance of doubt) that Nominatim usage policy doesn't apply if you're making calls to a locally hosted copy of Nominatim using locally imported data, of course!</p>
</div>
<div id="comment-23451-info" class="comment-info">
<span class="comment-age">(17 Jun '13, 10:11)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-23445" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23445-form-container" class="comment-form-container">
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

