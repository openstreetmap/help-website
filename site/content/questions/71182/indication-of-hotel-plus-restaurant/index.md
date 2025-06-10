+++
type = "question"
title = "Indication of hotel plus restaurant"
description = '''I saw a location where a hotel (blue bed) was indicated in the map. As I know there is a good restaurant there, too, I wanted to add that information. When I selected the hotel I found out, that the restaurant was part of the hotel, to be precise an amenity of it. That is correct, but looking at the...'''
date = "2019-10-15T18:56:00Z"
lastmod = "2019-10-25T17:13:00Z"
weight = 71182
keywords = [ "hotel", "restaurant", "icon" ]
aliases = [ "/questions/71182" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Indication of hotel plus restaurant](/questions/71182/indication-of-hotel-plus-restaurant)

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
<span id="post-71182-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71182-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71182-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I saw a location where a hotel (blue bed) was indicated in the map. As I know there is a good restaurant there, too, I wanted to add that information. When I selected the hotel I found out, that the restaurant was part of the hotel, to be precise an amenity of it.</p>
<p>That is correct, but looking at the map I cannot distinguish between locations where is only a hotel or a hotel plus a restaurant.</p>
<p>I would prefer to be able to see in the map where I can have a dinner for example.</p>
<p>Should that be done by adding a seperate item nearby? Or what about to add another icon for a hotel plus a restaurant? That would be my proposal. That would lead to a type of building "restaurant/hotel".</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hotel" rel="tag" title="see questions tagged &#39;hotel&#39;">hotel</span> <span class="post-tag tag-link-restaurant" rel="tag" title="see questions tagged &#39;restaurant&#39;">restaurant</span> <span class="post-tag tag-link-icon" rel="tag" title="see questions tagged &#39;icon&#39;">icon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Oct '19, 18:56</strong></p>
<img src="https://secure.gravatar.com/avatar/7c8cd6797f89510b4c9a7c6686e6a859?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bergmaus&#39;s gravatar image" />
<p><span>Bergmaus</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bergmaus has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71182" class="comments-container">
&#10;</div>
<div id="comment-tools-71182" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71182-form-container" class="comment-form-container">
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

<span id="71183"></span>

<div id="answer-container-71183" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71183-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71183-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-71183-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Bergmaus,</p>
<p>Both techniques are quite common -- tagging a single feature as both a hotel and a restaurant (<code>tourism=hotel</code> + <code>amenity=restaurant</code>) and mapping them as two separate features.</p>
<p>If you'd like to add a separate feature for the restaurant itself, go for it! This is especially useful if it has a different name/opening hours/contact info/website etc than the hotel. (If you do this you should remove the <code>amenity=restaurant</code> tag from the hotel, though.)</p>
<p>But note that even at the highest zoom of the openstreetmap.org map there's limited space for icons, so not everything that's mapped will appear on the screen. So there's no guarantee that the restaurant icon will show up. (Or it might show up, but the blue bed for the hotel may be gone!)</p>
<p>Don't get hung up on exactly how things look on the map. The online map at openstreetmap.org is only one view of the map data, really just a demo. The goal of OSM is to get the correct data in the database, so it can be used for any kind of project, not just for a particular map rendering.</p>
<p>If you want to use OSM data to make a map that emphasises the restaurants, or that shows a different icon for hotels that include a restaurant, you can do that -- but it takes some programming skill. Alternately you can use a tool like Overpass Turbo: <a href="https://overpass-turbo.eu/s/Naj">https://overpass-turbo.eu/s/Naj</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Oct '19, 19:45</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Oct '19, 19:52</strong> </span></p>
</div>
</div>
<div id="comments-container-71183" class="comments-container">
<span id="71184"></span>
<div id="comment-71184" class="comment">
<div id="post-71184-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would even go so far to say that putting more than one real world object (hotel and restaurant) is bad practice albeit it being done so often. Name, opening hours, phone number, outdoor seating etc. are very unlikely to be exactly the same for both, nor do they occupy the exact same space. Creating two objects (e. g. building or grounds for the hotel and node within for the restaurant) is <a href="https://wiki.openstreetmap.org/wiki/One_feature,_one_OSM_element#One_feature_per_OSM_element">better tagging practice</a>.</p>
</div>
<div id="comment-71184-info" class="comment-info">
<span class="comment-age">(15 Oct '19, 20:13)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="71187"></span>
<div id="comment-71187" class="comment">
<div id="post-71187-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For most hotel restaurants I'd agree with you, and I almost always map them that way. In fact I was a little astonished to see how frequently hotel and restaurant are mapped as a single element -- over 11000 uses.</p>
<p>I have, though, seen establishments that are both hotel and restaurant but still feel like a single "real world object" -- small places where the hotel proprietor is also the bartender, and the spouse is in the kitchen. Barring any tag conflicts, I'd probably map those as a single feature.</p>
</div>
<div id="comment-71187-info" class="comment-info">
<span class="comment-age">(15 Oct '19, 23:44)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
</div>
<div id="comment-tools-71183" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71183-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71330"></span>

<div id="answer-container-71330" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71330-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71330-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71330-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks jmapb for the answer.</p>
<p>In fact, the restaurant part always has different opening hours: you can reach the hotel late night or enter your room during a time where the restaurant is closed.</p>
<p>A database must be seen as like a model and the reason of existence is solely to answer certain questions. If that is not given, the database does not have any sense.</p>
<p>This means: On one hand as a guest of the hotel you want to know if there is a restarant as amenity. But on the other - not interested in a hotel, but searching a restaurant, the map should allow me to find them. Currently I only see hotel icons and some may have a restaurant but most not.</p>
<p>Your argument that there is limited space for icons is very true. And therefore I do not believe adding a second item very close to the hotel to stand for the restaurant is not a good solution. And that leads to the proposal to add a different icon so allow to distinguish between hotels with and without restaurant. (and use that trivial common approach without coding needed)</p>
<p>Coming to TZorns comment: Even having one Item, there is no problem to store a second telephone number or opening hours for the amenity restaurant. In fact they occopy the same space, just the bedrooms are maybe some levels above. For practical reasons it is one location (reaching, parking). Often even the entry is the same. The granularity is limited, remark the point that icon space is limited even in highest zoom level.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '19, 17:13</strong></p>
<img src="https://secure.gravatar.com/avatar/7c8cd6797f89510b4c9a7c6686e6a859?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bergmaus&#39;s gravatar image" />
<p><span>Bergmaus</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bergmaus has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71330" class="comments-container">
&#10;</div>
<div id="comment-tools-71330" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71330-form-container" class="comment-form-container">
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

