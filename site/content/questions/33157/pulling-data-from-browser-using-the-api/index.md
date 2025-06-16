+++
type = "question"
title = "pulling data from browser using the API"
description = '''I am trying to pull data for a single city bounded by two lat-long pairs with:  https://www.openstreetmap.org/api/0.6/map?bbox=-76.7237091,39.19714109,-76.5273285,39.385794515  I am currently logged in to OSM (my browser has a cookie).  It doesn&#x27;t work. When I try the diagnostic:  http://www.openstre...'''
date = "2014-05-13T23:30:00Z"
lastmod = "2014-05-14T08:13:00Z"
weight = 33157
keywords = [ "api", "data", "bbox" ]
aliases = [ "/questions/33157" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [pulling data from browser using the API](/questions/33157/pulling-data-from-browser-using-the-api)

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
<span id="post-33157-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33157-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33157-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to pull data for a single city bounded by two lat-long pairs with:</p>
<blockquote>
<p><a href="https://www.openstreetmap.org/api/0.6/map?bbox=-76.7237091,39.19714109,-76.5273285,39.385794515">https://www.openstreetmap.org/api/0.6/map?bbox=-76.7237091,39.19714109,-76.5273285,39.385794515</a></p>
</blockquote>
<p>I am currently logged in to OSM (my browser has a cookie).</p>
<p>It doesn't work. When I try the diagnostic:</p>
<blockquote>
<p><a href="https://www.openstreetmap.org/api/0.6/permissions">https://www.openstreetmap.org/api/0.6/permissions</a></p>
</blockquote>
<p>I get a response of an empty set of permissions.</p>
<p>What do I need to do?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-bbox" rel="tag" title="see questions tagged &#39;bbox&#39;">bbox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 May '14, 23:30</strong></p>
<img src="https://secure.gravatar.com/avatar/92c443d5ff9cd4d637081fa65be3335d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="borbash&#39;s gravatar image" />
<p><span>borbash</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="borbash has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33157" class="comments-container">
&#10;</div>
<div id="comment-tools-33157" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33157-form-container" class="comment-form-container">
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

<span id="33158"></span>

<div id="answer-container-33158" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33158-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33158-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-33158-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="borbash has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The api is designed for editing the openstreetmap data. It has a limit how big an area you are allowed to download at once. The whole of Baltimore is certainly too much.</p>
<p>Clicking on the <a href="https://www.openstreetmap.org/export#map=12/39.2915/-76.6255">export button</a> at the top of the the openstreetmap main page list some alternatives if the export from the api fails, because the area is too big. E.g.: <a href="http://overpass-api.de/api/map?bbox=-76.7237,39.1971,-76.5273,39.3858">http://overpass-api.de/api/map?bbox=-76.7237,39.1971,-76.5273,39.3858</a> and <a href="http://metro.teczno.com/#dc-baltimore">http://metro.teczno.com/#dc-baltimore</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 May '14, 01:12</strong></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cartinus has 35 accepted answers">27%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 May '14, 01:13</strong> </span></p>
</div>
</div>
<div id="comments-container-33158" class="comments-container">
<span id="33161"></span>
<div id="comment-33161" class="comment">
<div id="post-33161-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The overpass API worked immediately. Thanks! A followup: I wanted the data only to check for the existence of a certain tag, namely "highway=speed_camera". Is there a way to ask for only those tags within a bounding box?</p>
</div>
<div id="comment-33161-info" class="comment-info">
<span class="comment-age">(14 May '14, 04:11)</span> <span class="comment-user userinfo">borbash</span>
</div>
</div>
<span id="33165"></span>
<div id="comment-33165" class="comment">
<div id="post-33165-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#By_exact_name_and_rough_location">there is</a> (just replace the <em>name</em> with your <em>highway</em> tag). Even better: you can visualize the result using <a href="http://overpass-turbo.eu/s/3no">overpass turbo</a> where the result can also be <em>exported</em> (hint: use the <em>wizard</em> for creating new queries).</p>
</div>
<div id="comment-33165-info" class="comment-info">
<span class="comment-age">(14 May '14, 08:12)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="33166"></span>
<div id="comment-33166" class="comment">
<div id="post-33166-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://overpass-turbo.eu/">http://overpass-turbo.eu/</a> makes it easy to design queries</p>
</div>
<div id="comment-33166-info" class="comment-info">
<span class="comment-age">(14 May '14, 08:13)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-33158" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33158-form-container" class="comment-form-container">
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

