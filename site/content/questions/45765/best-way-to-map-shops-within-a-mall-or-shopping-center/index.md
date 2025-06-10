+++
type = "question"
title = "Best way to map shops within a mall or shopping center?"
description = '''I have an ongoing debate with a friend and I want to get some additional input on this question... For a shopping center or mall, my friend insists on mapping the shops inside by guessing the outline of the shops, drawing them as individual areas, and then piecing them all together to form the outli...'''
date = "2015-10-06T22:39:00Z"
lastmod = "2015-11-19T20:57:00Z"
weight = 45765
keywords = [ "shop", "perimeter", "mall", "point", "area" ]
aliases = [ "/questions/45765" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Best way to map shops within a mall or shopping center?](/questions/45765/best-way-to-map-shops-within-a-mall-or-shopping-center)

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
<span id="post-45765-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45765-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-45765-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have an ongoing debate with a friend and I want to get some additional input on this question...</p>
<p>For a shopping center or mall, my friend insists on mapping the shops inside by guessing the outline of the shops, drawing them as individual areas, and then piecing them all together to form the outline of the larger building.</p>
<p>I've been insisting, on the other hand, that one should never make up data like this (or even make educated guesses with such frequency), and that, instead, the best thing to do is to draw the known outline of the building and then place points within the building area in the approximate locations where the shops are.</p>
<p>My friend has countered my approach by saying that this violates the "one feature, one element" rule, since a commercial building area with several points inside would be several elements for a single feature. However, I believe this is a misinterpretation of the rule.</p>
<p>As a sort of compromise solution, my friend proposed making each shop a node on the perimeter of the area of the building, thus associating the shop information with the larger building building.</p>
<p>What do you think?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shop" rel="tag" title="see questions tagged &#39;shop&#39;">shop</span> <span class="post-tag tag-link-perimeter" rel="tag" title="see questions tagged &#39;perimeter&#39;">perimeter</span> <span class="post-tag tag-link-mall" rel="tag" title="see questions tagged &#39;mall&#39;">mall</span> <span class="post-tag tag-link-point" rel="tag" title="see questions tagged &#39;point&#39;">point</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Oct '15, 22:39</strong></p>
<img src="https://secure.gravatar.com/avatar/2f18176174223793d67f25a8503d49c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ox2015&#39;s gravatar image" />
<p><span>ox2015</span><br />
<span class="score" title="51 reputation points">51</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ox2015 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Oct '15, 22:42</strong> </span></p>
</div>
</div>
<div id="comments-container-45765" class="comments-container">
&#10;</div>
<div id="comment-tools-45765" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45765-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="45769"></span>

<div id="answer-container-45769" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45769-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45769-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-45769-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First, your friend is misinterpreting the <a href="http://wiki.openstreetmap.org/wiki/One_feature,_one_OSM_element">One feature, one OSM element</a> principle. That principle basically says that any one real-world feature shouldn't have multiple OSM elements to represent it. As an example, don't tag both a building way and a node inside that way with an amenity=restaurant tag. If a mall contains many shops, there's nothing wrong with mapping each of those shops, as long as there is only one element representing each individual shop, and one for the overall mall.</p>
<p>As for how exactly to map the shops, neither method is wrong. If you have a rough idea of how much space a given shop covers, feel free to map it as an area (a closed way). This gives a more useful representation of how much space the shop uses than a simple node, so I'd say this would be the preferred method (if possible). An educated guess is fine, because it can be treated as a starting point that future mappers (or yourselves) can improve on in the future.</p>
<p>If the boundaries of the different shops are unknown, simply map them as a node in the rough location. That way the shop information is there, and someone else can come along later and add information to it.</p>
<p>Can you give us examples of malls that you and your friend have mapped using the two different methods?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Oct '15, 00:27</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-45769" class="comments-container">
&#10;</div>
<div id="comment-tools-45769" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45769-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="45767"></span>

<div id="answer-container-45767" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45767-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45767-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-45767-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi ox2015, please read these lines <a href="http://wiki.openstreetmap.org/wiki/Tag:shop%3Dmall">http://wiki.openstreetmap.org/wiki/Tag:shop%3Dmall</a> and to specify the levels or floors read these as well. And yes it’s a lot. Ps take a look at some of the malls in your region, country or elsewhere. (search for a large parking space with a building in the centre or nearby. For instance this one <a href="http://www.openstreetmap.org/#map=17/39.14759/-84.44688">http://www.openstreetmap.org/#map=17/39.14759/-84.44688</a> You cannot draw the outline of a shop without knowing the outer lines. The backside of a shop is or could be unclear. And you don’t get the knowledge or an invitation to look around. So try to add a tag as close to the shop area as possible, count steps or some alike from a welknown point.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Oct '15, 23:21</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Oct '15, 23:33</strong> </span></p>
</div>
</div>
<div id="comments-container-45767" class="comments-container">
&#10;</div>
<div id="comment-tools-45767" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45767-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="46726"></span>

<div id="answer-container-46726" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46726-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46726-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46726-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I answered a similar question here:-</p>
<p><a href="https://help.openstreetmap.org/questions/24814/mapping-shops-in-a-retail-building-with-more-than-one-entrance?page=1&amp;focusedAnswerId=46725#46725">link text</a></p>
<p>With specific regard to this question you could aproach it from a different approach if you can visit the site you could try indoor mapping the rooms you do know a lot about like the main sales floors for customers, the fitting rooms escalaters, stairs, lifts and corridors etc. and place these inside the shell of the building outline. This can give a very useful mall map and shows were things are still to be found out by someone else later. Try looking or asking staff about evacuation routes and any emergancy maps about to check as these can relate outside doors to inside shops. Using bing's bird view for a clear slanted view of building sidewalls and entrancesis helpful in getting the geometry right when stareing at rooftops in the editors.</p>
<p>You can definatly add nodes for sub-features into a larger defined area without a problem the problems begin for some system when you duplicate a feature as both an area and line or a node becuse it can be shown as two seperate things instead of one on the render {there are speacial tagging treatments for highways that are defined as areas too}.</p>
<p>putting nodes around the edge of an area rather than close to were the feature actually is is very wrong (if its actually just a door [entrance tagged] that really is on the outside wall then maybe, but not just shop tags that should float in the middle of the known shop.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Nov '15, 20:57</strong></p>
<img src="https://secure.gravatar.com/avatar/30d90feb3a40fa6255767f95a8cd7943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Govanus&#39;s gravatar image" />
<p><span>Govanus</span><br />
<span class="score" title="154 reputation points">154</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Govanus has one accepted answer">3%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Nov '15, 20:59</strong> </span></p>
</div>
</div>
<div id="comments-container-46726" class="comments-container">
&#10;</div>
<div id="comment-tools-46726" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46726-form-container" class="comment-form-container">
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

