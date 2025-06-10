+++
type = "question"
title = "Why is my map returning &quot;invalid&quot; coordinates?"
description = '''So what i&#x27;m trying to do is a web-application to calculate routes between two coordinates. I&#x27;ve set up a map with leafletjs with the first tile server in the list on this page. I set up a function which returns the coordinates where I click on the map. The thing, that is irritating to me, is that th...'''
date = "2021-11-29T10:47:00Z"
lastmod = "2021-11-30T10:27:00Z"
weight = 82713
keywords = [ "leaflet", "crs", "openrouteservice", "routing" ]
aliases = [ "/questions/82713" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why is my map returning "invalid" coordinates?](/questions/82713/why-is-my-map-returning-invalid-coordinates)

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
<span id="post-82713-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82713-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82713-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>So what i'm trying to do is a web-application to calculate routes between two coordinates. I've set up a map with <a href="https://leafletjs.com/">leafletjs</a> with the first tile server in the list on <a href="https://wiki.openstreetmap.org/wiki/Tile_servers">this page</a>. I set up a function which returns the coordinates where I click on the map. The thing, that is irritating to me, is that the coordinates that my map returns are not the same as other web-maps return (for example <a href="https://maps.openrouteservice.org/">openrouteservice-map</a>) for the exact same position. Here's an example:</p>
<p>These are the coordinates from my map: 85327.45845973487,46.94840207976996 (long, lat). These are the coordinates from the openrouteservice-map: 7.457968, 46.948518 (long, lat) for the exact same position.</p>
<p>The longitude value is very different between the two.</p>
<p>So my question is, why are the coordinates that my map returns, different than what other maps return? And also, if I use the coordinates of my map for the route calculation, they don't work.</p>
<p>I have aready tried changing the CRS (Coordinate Reference System), but that didn't do a difference.</p>
<p>Any help or hint is very appreciated, thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-crs" rel="tag" title="see questions tagged &#39;crs&#39;">crs</span> <span class="post-tag tag-link-openrouteservice" rel="tag" title="see questions tagged &#39;openrouteservice&#39;">openrouteservice</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Nov '21, 10:47</strong></p>
<img src="https://secure.gravatar.com/avatar/7a68ab86b12b8ce3031b64acf0ee7245?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nicolabaechi&#39;s gravatar image" />
<p><span>nicolabaechi</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nicolabaechi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82713" class="comments-container">
<span id="82715"></span>
<div id="comment-82715" class="comment">
<div id="post-82715-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Add a link to your (dev) site where we can check what you are doing. Sth. is either wrong here: "I set up a function which returns the coordinates where I click on the map" or you just scrolled "endlessly" to the right before clicking on the map and by that got that crazy long coordinate. You may also set a bounding box for your map in leaflet to disable the option of endless scrolling in any direction, so your long will be between -180 and 180 (and lat between -90 and 90).</p>
</div>
<div id="comment-82715-info" class="comment-info">
<span class="comment-age">(29 Nov '21, 14:39)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="82716"></span>
<div id="comment-82716" class="comment">
<div id="post-82716-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hey, I set up this <a href="https://codesandbox.io/s/0jwmz">codesandbox</a>. Don't know if it works in the environment, maybe pull it locally. Yes what you said could be, but what would cause this behaviour?</p>
</div>
<div id="comment-82716-info" class="comment-info">
<span class="comment-age">(29 Nov '21, 15:27)</span> <span class="comment-user userinfo">nicolabaechi</span>
</div>
</div>
</div>
<div id="comment-tools-82713" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82713-form-container" class="comment-form-container">
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

<span id="82717"></span>

<div id="answer-container-82717" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82717-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82717-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-82717-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I managed to solve my issue by setting a <a href="https://leafletjs.com/reference.html#map-maxbounds">boundingbox</a> as <a href="https://help.openstreetmap.org/users/17439/spiekerooger">@Spiekerooger</a> suggested, thank you :).</p>
<p>I did that like this:</p>
<p><code>// setting the corners of the bounding box var corner1 = L.latLng(47.86108855623179, 5.883178710937501); var corner2 = L.latLng(45.77901739936284, 10.5743408203125); var bounds = L.latLngBounds(corner1, corner2);</code> <code>// adding it as a property to the map this.map = L.map('map', { ..., maxBounds: bounds, });</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '21, 10:27</strong></p>
<img src="https://secure.gravatar.com/avatar/7a68ab86b12b8ce3031b64acf0ee7245?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nicolabaechi&#39;s gravatar image" />
<p><span>nicolabaechi</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nicolabaechi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82717" class="comments-container">
&#10;</div>
<div id="comment-tools-82717" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82717-form-container" class="comment-form-container">
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

