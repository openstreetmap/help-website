+++
type = "question"
title = "Get way from location"
description = '''I&#x27;m writing IOS app that will warn users about exceeding speed limit while driving car. I&#x27;ll get location from GPS.  How can I find the WAY where I&#x27;m currently driving? I&#x27;ve notice that WAY object contains NODEs and NODEs contains coordinates. The only way I came up with is to connect all nodes from...'''
date = "2013-06-01T23:04:00Z"
lastmod = "2013-06-04T14:42:00Z"
weight = 22945
keywords = [ "overpass", "location", "way" ]
aliases = [ "/questions/22945" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Get way from location](/questions/22945/get-way-from-location)

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
<span id="post-22945-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22945-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22945-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm writing IOS app that will warn users about exceeding speed limit while driving car. I'll get location from GPS.</p>
<p>How can I find the <em>WAY</em> where I'm currently driving? I've notice that <em>WAY</em> object contains <em>NODEs</em> and <em>NODEs</em> contains coordinates. The only way I came up with is to connect all nodes from <em>WAY</em> and check if I am on this connected patch. Hope there is easiest way...</p>
<p>I've try Overpass API</p>
<p>Pawel</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-location" rel="tag" title="see questions tagged &#39;location&#39;">location</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jun '13, 23:04</strong></p>
<img src="https://secure.gravatar.com/avatar/83b555774018825d7b1999a2e2c473aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="psci&#39;s gravatar image" />
<p><span>psci</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="psci has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-22945" class="comments-container">
&#10;</div>
<div id="comment-tools-22945" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22945-form-container" class="comment-form-container">
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

<span id="22947"></span>

<div id="answer-container-22947" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22947-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-22947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Several options, all of which require that you set up your own server:</p>
<ul>
<li>load OSM data into PostGIS database with osm2pgsql (ideally configured to load only roads), then make ST_DWITHIN query to find all roads in the vicinity of your point and order them by ST_DISTANCE. This will give correct results even if your query point is a long distance between road nodes.</li>
<li>set up an instance of the Nominatim geocoder (also requires server with PostGIS etc) and have it reverse-geocode the position you are looking for; since this will occasionally not return the road itself but also POIs or houses, toy with the "zoom" parameter or modify the software to only return roads</li>
</ul>
<p>Options that do not require setting up your own server, but that will get you blocked on the respective servers very quickly if your app sends these queries every couple of seconds:</p>
<ul>
<li>use existing Nominatim servers and reverse geocode your location (of course the "modify the software" option is not available then)</li>
<li>use Overpass to request all "highway" type ways in a rectangle around your point, with their nodes; then, as you describe, compute the line segments between consecutive points in these ways, and find out which of these line segments is nearest to your position.</li>
</ul>
<p>Neither of these options will correctly find out whether you are on a bridge or under the same bridge - this is something that would require additional analysis on your part (I was there 10 seconds ago, now I am here, this means I cannot be traveling on that road, it must be this road...)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jun '13, 23:37</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-22947" class="comments-container">
&#10;</div>
<div id="comment-tools-22947" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22947-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="23006"></span>

<div id="answer-container-23006" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23006-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23006-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-23006-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Do you mean <a href="http://overpass-turbo.eu/s/id">such query</a>? <a href="https://www.openstreetmap.org/?mlat=48.21&amp;mlon=16.371&amp;zoom=18">The location</a> I assumed.</p>
<p>/al</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jun '13, 14:42</strong></p>
<img src="https://secure.gravatar.com/avatar/5501080a7333d6383d6c545f076eaeba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_al&#39;s gravatar image" />
<p><span>_al</span><br />
<span class="score" title="860 reputation points">860</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_al has one accepted answer">4%</span></p>
</div>
</div>
<div id="comments-container-23006" class="comments-container">
&#10;</div>
<div id="comment-tools-23006" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23006-form-container" class="comment-form-container">
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

