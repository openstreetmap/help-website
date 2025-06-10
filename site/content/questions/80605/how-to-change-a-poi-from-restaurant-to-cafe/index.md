+++
type = "question"
title = "How to change a POI from Restaurant to Cafe"
description = '''If an amenity is predominantly a Cafe, but also contains restaurant / bar facilities and is currently appearing as a restaurant - should new tags be added, or can the category be changed from Restaurant to Cafe ?'''
date = "2021-06-17T12:49:00Z"
lastmod = "2021-06-17T15:04:00Z"
weight = 80605
keywords = [ "pois", "cafe", "restaurant" ]
aliases = [ "/questions/80605" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to change a POI from Restaurant to Cafe](/questions/80605/how-to-change-a-poi-from-restaurant-to-cafe)

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
<span id="post-80605-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80605-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80605-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If an amenity is predominantly a Cafe, but also contains restaurant / bar facilities and is currently appearing as a restaurant - should new tags be added, or can the category be changed from Restaurant to Cafe ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pois" rel="tag" title="see questions tagged &#39;pois&#39;">pois</span> <span class="post-tag tag-link-cafe" rel="tag" title="see questions tagged &#39;cafe&#39;">cafe</span> <span class="post-tag tag-link-restaurant" rel="tag" title="see questions tagged &#39;restaurant&#39;">restaurant</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jun '21, 12:49</strong></p>
<img src="https://secure.gravatar.com/avatar/4f016ab33182be69e371d71e34337123?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bigwol&#39;s gravatar image" />
<p><span>Bigwol</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bigwol has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80605" class="comments-container">
&#10;</div>
<div id="comment-tools-80605" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80605-form-container" class="comment-form-container">
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

<span id="80607"></span>

<div id="answer-container-80607" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80607-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80607-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80607-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If it's predominantly a cafe, then go ahead and change the tag from <code>amenity=restaurant</code> to <code>amenity=cafe</code>.</p>
<p>As far as adding new tags, yes, you can add a lot to give additional details. You can indicate the food options using <a href="https://wiki.openstreetmap.org/wiki/Key:cuisine"><code>cuisine=*</code></a> and <a href="https://wiki.openstreetmap.org/wiki/Key:diet"><code>diet:*=*</code></a> tags, and you can indicate the drink options (coffee, alcohol, and others) using <a href="https://wiki.openstreetmap.org/wiki/Key:drink"><code>drink:*=*</code></a> tags.</p>
<p>If the establishment operates in different modes at different times of day, you can describe that with the <a href="https://wiki.openstreetmap.org/wiki/Key:opening_hours"><code>opening_hours</code></a> tag, eg, <strong><code>opening_hours=Mo-Sa 07:00-14:00 "cafe"||Mo-Sa 14:00-23:00 "bar"</code></strong>. There's also <a href="https://wiki.openstreetmap.org/wiki/Key:opening_hours:kitchen"><code>opening_hours:kitchen</code></a> to indicate when food is served, if that differs from the general opening hours.</p>
<p>The tag <a href="https://wiki.openstreetmap.org/wiki/Key:bar"><code>bar=yes</code></a> is often used to indicate that a feature includes a bar. It's most often used with restaurants and hotels, but it could be used with cafes too.</p>
<p>It would also possible to tag <code>restaurant=yes</code>, though it's not as common and not documented. Personally I don't think it's necessary, especially if the food options are indicated by other tags.</p>
<p>...</p>
<p>Note that distinction between cafe &amp; restaurant is somewhat fuzzy across the globe. The <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dcafe">amenity=cafe wiki page</a> shows a picture from Austria with white tablecloths and a uniformed waiter. This is a traditional European cafe, but I believe that many mappers, just looking at the picture, would call it a restaurant. (The waiter's only carrying drinks, though!)</p>
<p>Ultimately it comes down to how the most prominent use of the particular amenity compares with the general understanding of restaurant/cafe in that region.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jun '21, 15:04</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-80607" class="comments-container">
&#10;</div>
<div id="comment-tools-80607" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80607-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="80606"></span>

<div id="answer-container-80606" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80606-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80606-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80606-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>or can the category be changed from Restaurant to Cafe</p>
</blockquote>
<p>Yes, it does make sense to change it in a case when it was previously predominantly a restaurant and is now predominantly a cafe.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jun '21, 14:14</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-80606" class="comments-container">
&#10;</div>
<div id="comment-tools-80606" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80606-form-container" class="comment-form-container">
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

