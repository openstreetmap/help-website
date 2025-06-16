+++
type = "question"
title = "Hole after creating a multipolygon for a pedestrian highway with a fountain"
description = '''https://www.openstreetmap.org/relation/7184233 The fountain was not visible as it was covered by the highway=pedestrian. I created a multipolygon relation so that the fountain would be outside of the pedestrian area. But then it&#x27;s shown as a hole, showing the road below it. Is it a bug of the mapping...'''
date = "2017-04-24T13:48:00Z"
lastmod = "2017-04-24T19:51:00Z"
weight = 55812
keywords = [ "pedestrian", "hole", "fountain", "multipolygon" ]
aliases = [ "/questions/55812" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Hole after creating a multipolygon for a pedestrian highway with a fountain](/questions/55812/hole-after-creating-a-multipolygon-for-a-pedestrian-highway-with-a-fountain)

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
<span id="post-55812-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55812-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55812-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><a href="https://www.openstreetmap.org/relation/7184233">https://www.openstreetmap.org/relation/7184233</a></p>
<p>The fountain was not visible as it was covered by the highway=pedestrian. I created a multipolygon relation so that the fountain would be outside of the pedestrian area. But then it's shown as a hole, showing the road below it.</p>
<p>Is it a bug of the mapping engine or is it the wrong way to map it?</p>
<p><img src="/upfiles/Presse-papiers-1.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pedestrian" rel="tag" title="see questions tagged &#39;pedestrian&#39;">pedestrian</span> <span class="post-tag tag-link-hole" rel="tag" title="see questions tagged &#39;hole&#39;">hole</span> <span class="post-tag tag-link-fountain" rel="tag" title="see questions tagged &#39;fountain&#39;">fountain</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Apr '17, 13:48</strong></p>
<img src="https://secure.gravatar.com/avatar/e2b1857c1d017a9936d5e48d3621884e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="The%20RedBurn&#39;s gravatar image" />
<p><span>The RedBurn</span><br />
<span class="score" title="101 reputation points">101</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="The RedBurn has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Apr '17, 14:05</strong> </span></p>
</div>
</div>
<div id="comments-container-55812" class="comments-container">
&#10;</div>
<div id="comment-tools-55812" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55812-form-container" class="comment-form-container">
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

<span id="55818"></span>

<div id="answer-container-55818" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55818-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Don't create a hole if there isn't any. If the fountain is not visible then this is a rendering issue. This is no reason for changing the data (see <a href="https://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">tagging for the renderer</a>)! The first priority is always to keep the data correct. Creating an artificial hole will have a negative impact on routing.</p>
<p>Rendering issues can be reported at the <a href="https://github.com/gravitystorm/openstreetmap-carto/">openstreetmap-carto GitHub repo</a> after making sure that 1) the data is correct and 2) the tiles you are seeing are up to data and not coming from your browser cache.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Apr '17, 14:28</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-55818" class="comments-container">
<span id="55820"></span>
<div id="comment-55820" class="comment">
<div id="post-55820-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for the answer. Yes, I know about that wiki page.</p>
<p>I'm wondering however if the fountain should be kept inside the highway=pedestrian as we don't usually walk in it. So I don't actually see it as a hole and the previous state could be considered as "tagging for the renderer" if it's just to avoid the visual hole.</p>
<p>Elements - even buildings - are hidden by highway=pedestrian, but it may or may not be intended. Should an element override the highway=pedestrian container?</p>
</div>
<div id="comment-55820-info" class="comment-info">
<span class="comment-age">(24 Apr '17, 14:47)</span> <span class="comment-user userinfo">The RedBurn</span>
</div>
</div>
<span id="55822"></span>
<div id="comment-55822" class="comment">
<div id="post-55822-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think areas tagged with only amenity=fountain don't get a fill, they still just render with the fountain icon? Therefore if you create a fountain as an inner multipolygon of another area, it just cuts a hole in that area's rendering.</p>
</div>
<div id="comment-55822-info" class="comment-info">
<span class="comment-age">(24 Apr '17, 15:24)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="55824"></span>
<div id="comment-55824" class="comment">
<div id="post-55824-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>This is a good question. I guess this depends on the size of the fountain. It if is a really large one (i.e. diameter &gt; 20 m which seems to be true in your case) then it can be mapped as an own area. However I'm unsure if it is a good idea to exclude it from the pedestrian area. I wouldn't remove it from a leisure=park area however a pedestrian area might be different due to routing. Maybe this comes down to the question if routing engines capable of performing area routing are able to avoid this obstacle? Looks like I can't give a good advice here.</p>
</div>
<div id="comment-55824-info" class="comment-info">
<span class="comment-age">(24 Apr '17, 15:30)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="55831"></span>
<div id="comment-55831" class="comment">
<div id="post-55831-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>These areas have just a line on the edge, like (<a href="https://www.openstreetmap.org/#map=19/50.64490/5.57321).">https://www.openstreetmap.org/#map=19/50.64490/5.57321).</a> After the edit of mmahmud, I'm thinking that the highway=pedestrian shouldn't be opaque, which would explain why the fountain looked like a hole.</p>
</div>
<div id="comment-55831-info" class="comment-info">
<span class="comment-age">(24 Apr '17, 19:35)</span> <span class="comment-user userinfo">The RedBurn</span>
</div>
</div>
</div>
<div id="comment-tools-55818" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55818-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55813"></span>

<div id="answer-container-55813" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55813-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55813-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55813-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It appears like this to me ... seems ok with fountain seen, although with the highway number and one-way arrows... not perfect, but passable for me.</p>
<p><img src="/upfiles/Screen_Shot_2017-04-24_at_10.56.19_PM.png" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Apr '17, 14:01</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span></p>
</img>
</div>
</div>
<div id="comments-container-55813" class="comments-container">
<span id="55814"></span>
<div id="comment-55814" class="comment">
<div id="post-55814-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've added a screenshot. Did you look at that part of the map earlier and have still an old version in your cache? Or maybe is it that the map wasn't updated yet at all zoom levels.</p>
<p>Anyway, your screenshot is how it was before creating the multipolygon.</p>
</div>
<div id="comment-55814-info" class="comment-info">
<span class="comment-age">(24 Apr '17, 14:06)</span> <span class="comment-user userinfo">The RedBurn</span>
</div>
</div>
<span id="55816"></span>
<div id="comment-55816" class="comment">
<div id="post-55816-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, I just refreshed again and it still the same....interesting that we see it quite differently. Same on Firefox, Safari and Cliqz for me. Old image could be fed from my service provider I suppose?</p>
</div>
<div id="comment-55816-info" class="comment-info">
<span class="comment-age">(24 Apr '17, 14:16)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="55817"></span>
<div id="comment-55817" class="comment">
<div id="post-55817-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I guess the cache depends of the server you get the map from, and yours is still behind, probably because the edit didn't come from the same server.</p>
</div>
<div id="comment-55817-info" class="comment-info">
<span class="comment-age">(24 Apr '17, 14:20)</span> <span class="comment-user userinfo">The RedBurn</span>
</div>
</div>
<span id="55821"></span>
<div id="comment-55821" class="comment">
<div id="post-55821-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>My image has finally updated and is same as yours, with the hole.</p>
</div>
<div id="comment-55821-info" class="comment-info">
<span class="comment-age">(24 Apr '17, 14:55)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
</div>
<div id="comment-tools-55813" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55813-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55829"></span>

<div id="answer-container-55829" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55829-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55829-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55829-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, I think this is rendering correctly as it is showing the tunnel below with dotted lines and fountain in the middle with the pedestrian road around it. I used Layer = 1 on both the pedestrian road and fountain. But another thing, there is already a residential road drawn, is it necessary to draw the pedestrian one additionally or is it a separate road?</p>
<p><img src="/upfiles/Capture_9TqRKHm.PNG" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Apr '17, 18:21</strong></p>
<img src="https://secure.gravatar.com/avatar/c482180b767d07897d150d7b426ca4e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmahmud&#39;s gravatar image" />
<p><span>mmahmud</span><br />
<span class="score" title="638 reputation points">638</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmahmud has one accepted answer">3%</span></p>
</img>
</div>
</div>
<div id="comments-container-55829" class="comments-container">
<span id="55830"></span>
<div id="comment-55830" class="comment">
<div id="post-55830-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It's a plaza (<a href="https://wiki.openstreetmap.org/wiki/Tag:highway=pedestrian#Plazas),">https://wiki.openstreetmap.org/wiki/Tag:highway=pedestrian#Plazas),</a> so the whole area can be walked on except where the fountain is. So I think that the right way to map it is to use a polygon with area=yes. But your edit made me understand that the highway=pedestrian shouldn't be opaque, the road below it should be visible and that may explain why the fountain looked like a hole.</p>
</div>
<div id="comment-55830-info" class="comment-info">
<span class="comment-age">(24 Apr '17, 19:16)</span> <span class="comment-user userinfo">The RedBurn</span>
</div>
</div>
<span id="55832"></span>
<div id="comment-55832" class="comment">
<div id="post-55832-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Remember, the data is related to, but separate from, the rendering. It is most important to make sure the data is tagged correctly. If you don't like the rendering of the data, you can take that up with the renderer (in this case OSM Carto <a href="https://github.com/gravitystorm/openstreetmap-carto).">https://github.com/gravitystorm/openstreetmap-carto).</a> Really, the same rendering issues exist with the park and footways to the west and the underground road.</p>
</div>
<div id="comment-55832-info" class="comment-info">
<span class="comment-age">(24 Apr '17, 19:51)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
</div>
<div id="comment-tools-55829" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55829-form-container" class="comment-form-container">
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

