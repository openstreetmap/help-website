+++
type = "question"
title = "Getting complete roads/streets instead of multiple ways per road"
description = '''I&#x27;m currently using the following query to retrieve all the streets/roads within distance of a lat, long location: [out:json]; way[&quot;highway&quot;](around:${distance},${lat},${long}); out;; However instead of getting a single record for each Street/road, I&#x27;m getting back multiple records (ways). Is there ...'''
date = "2018-05-06T02:10:00Z"
lastmod = "2018-05-06T18:56:00Z"
weight = 63337
keywords = [ "ways", "street", "road" ]
aliases = [ "/questions/63337" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Getting complete roads/streets instead of multiple ways per road](/questions/63337/getting-complete-roadsstreets-instead-of-multiple-ways-per-road)

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
<span id="post-63337-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63337-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63337-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm currently using the following query to retrieve all the streets/roads within distance of a lat, long location:</p>
<p><code>[out:json]; way["highway"](around:${distance},${lat},${long}); out;</code>;</p>
<p>However instead of getting a single record for each Street/road, I'm getting back multiple records (ways). Is there a way to get one record per real world road/Street?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 May '18, 02:10</strong></p>
<img src="https://secure.gravatar.com/avatar/d00b1ea630627f7b854f40b08890e708?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mkhalila&#39;s gravatar image" />
<p><span>mkhalila</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mkhalila has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63337" class="comments-container">
&#10;</div>
<div id="comment-tools-63337" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63337-form-container" class="comment-form-container">
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

<span id="63342"></span>

<div id="answer-container-63342" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63342-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63342-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-63342-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No, there is not; you will have to write code yourself that combines objects, because for every use case, the definition of what should be one object is different:</p>
<ul>
<li>A street may have "side arms" with the same name as the street, therefore it cannot be combined into one linear geometry.</li>
<li>A street may consist of several disjunct parts, e.g. if the street is cut in two by a small plaza or a large other street, and therefore also not be representable as one linear geometry.</li>
<li>Even where various OSM ways with the same street name <em>are</em> connected and could therefore be combine into one geometry, they will often have different attributes, e.g. one part could be highway=secondary and the other highway=residential, or one part could have a different surface or speed limit. Overpass cannot know what your conditions are for connecting the bits, and if bits were connected, which of the several highway type, or surface, or maxspeed values it should return for the combined object.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 May '18, 09:12</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-63342" class="comments-container">
<span id="63349"></span>
<div id="comment-63349" class="comment">
<div id="post-63349-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for that answer Frederick, that clarifies whether it's possible or not.</p>
<p>I suspected I'd have to do it myself. Which is what I've been attempting to do last few weeks but I'm struggling to come up with a way of combining ways into a street whilst maintaining the integrity of the data.</p>
<p>I can't just go via the name because two cities may have roads with the same name. I've tried going via ref of the way but that also only covers a small minority of the ways since in certain areas, only a few ways have a ref defined.</p>
<p>I could take a request and break it down into tiny requests spanning a tiny region and then join all the data together. That would maintain integrity of data mostly, however it'll create a ridiculous amount of overpass query requests.</p>
<p>Is there a way of getting the area/city a way belongs to given the ID and/or name of the way? I can use this to group ways with the same name that belong to the same area.</p>
</div>
<div id="comment-63349-info" class="comment-info">
<span class="comment-age">(06 May '18, 18:56)</span> <span class="comment-user userinfo">mkhalila</span>
</div>
</div>
<span id="63350"></span>
<div id="comment-63350" class="comment">
<div id="post-63350-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Continued:</p>
<p>Alternatively, is there a way of getting the lat, long location of a way given its ID and/or name? I could use this location to also group ways with the same name. Or even better, is there a way of modifying the above query to also retrieve the location of that way?</p>
<p>Another alternatively, in the above query I'm getting all ways within a certain distance of a lat, long location. At the moment it returns the ways but doesn't return the exact distance they are from the lat,long location. Is there a way of getting that?</p>
<p>Apologies for the brain dump, I've thought about possible solutions for months but I'm unsure of how to achieve this within the QL.</p>
<p>Any help is always appreciated. Thanks in advance.</p>
</div>
<div id="comment-63350-info" class="comment-info">
<span class="comment-age">(06 May '18, 18:56)</span> <span class="comment-user userinfo">mkhalila</span>
</div>
</div>
</div>
<div id="comment-tools-63342" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63342-form-container" class="comment-form-container">
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

