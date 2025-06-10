+++
type = "question"
title = "Floor parking around bike stands"
description = '''Seattle has started designating floor parking areas around bike stands to accommodate dockless bike shares:  How should these be tagged? One node for bicycle_parking=stands and a second node (or area?) for bicycle_parking=floor?'''
date = "2019-11-12T01:11:00Z"
lastmod = "2019-11-12T14:04:00Z"
weight = 71585
keywords = [ "bicycle_parking", "tagging" ]
aliases = [ "/questions/71585" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Floor parking around bike stands](/questions/71585/floor-parking-around-bike-stands)

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
<span id="post-71585-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71585-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71585-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Seattle,_Washington">Seattle</a> has started designating floor parking areas around bike stands to accommodate <a href="https://en.wikipedia.org/wiki/Bicycle-sharing_system#Dockless_bikes">dockless bike shares</a>:</p>
<p><img src="https://help.openstreetmap.org/upfiles/IMG_1391_kCEPnjO.jpg" style="width:33.0%" alt="floor parking around bike stands on sidewalk" /><img src="https://help.openstreetmap.org/upfiles/IMG_1392.jpg" style="width:33.0%" alt="floor parking around bike stands in street parking lane" /><img src="https://help.openstreetmap.org/upfiles/IMG_1450.jpg" style="width:33.0%" alt="floor parking around bike stands in intersection" /></p>
<p>How should these be tagged? One node for <code>bicycle_parking=stands</code> and a second node (or area?) for <code>bicycle_parking=floor</code>?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bicycle_parking" rel="tag" title="see questions tagged &#39;bicycle_parking&#39;">bicycle_parking</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Nov '19, 01:11</strong></p>
<img src="https://secure.gravatar.com/avatar/c1950a9357df3658d5473fdc05cb317a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrew%20Kvalheim&#39;s gravatar image" />
<p><span>Andrew Kvalheim</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrew Kvalheim has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-71585" class="comments-container">
&#10;</div>
<div id="comment-tools-71585" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71585-form-container" class="comment-form-container">
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

<span id="71590"></span>

<div id="answer-container-71590" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71590-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71590-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-71590-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This looks like a single bicycle parking amenity. As these usually have only had a single style parking there does not seem to be very much usage for areas with different kinds of parking.</p>
<p>By analogy with similar situations, I'd tentatively suggest:</p>
<ul>
<li>Map the area delineated by the white line as amenity=bicycle_parking, covered=no, capacity=10 (my estimate)</li>
<li>Use something like <code>bicycle_parking:stands=6</code> or <code>bicycle_parking:stands=yes</code> with <code>capacity:stands=6</code></li>
<li>Something similar for the floor parking (although this tag does not seem to be in use, <code>bicycle_parking=surface</code> seems the closest of in-use tags).</li>
<li>Also it may be possible to use something like <code>bicycle_parking=mixe</code>d to show that there are multiple types; or just <code>stands;surface</code>.</li>
</ul>
<p>I would suggest perhaps doing a more detailed consultation on the tagging mailing list: there are people there much more familiar with these tagging patterns.</p>
<p>If the free/surface/floor parking is <strong>only for bike share</strong> then I'd fall back to your original suggestion, but tag the free parking as <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dbicycle_rental"><code>amenity=bicycle_rental</code></a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Nov '19, 14:04</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</img>
</div>
</div>
<div id="comments-container-71590" class="comments-container">
&#10;</div>
<div id="comment-tools-71590" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71590-form-container" class="comment-form-container">
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

