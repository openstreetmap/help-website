+++
type = "question"
title = "Buildings with more than one amenity."
description = '''How should I tag building that has more than one amenity? For example: in my neighbourhood there is one building used for dentist, veterinarian and pharmacy. I&#x27;m sure that all those amenities shouldn&#x27;t be mixed up in tags for one building because tags like &quot;phone&quot;, &quot;opening_hours&quot;, or &quot;website&quot; (and...'''
date = "2013-09-23T00:43:00Z"
lastmod = "2020-01-09T07:53:00Z"
weight = 26625
keywords = [ "buildings", "multiple", "amenity" ]
aliases = [ "/questions/26625" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Buildings with more than one amenity.](/questions/26625/buildings-with-more-than-one-amenity)

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
<span id="post-26625-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26625-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-26625-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How should I tag building that has more than one amenity? For example: in my neighbourhood there is one building used for dentist, veterinarian and pharmacy. I'm sure that all those amenities shouldn't be mixed up in tags for one building because tags like "phone", "opening_hours", or "website" (and many others) would be inaccurate.</p>
<p>So.. my idea was to tag building only with address and "building=yes", and to put separate nodes of these amenities on it with specified data about them.</p>
<p>But there is another question. What to do with addresses? Should I tag all those separate amenities with addresses or the one made for building will suffice? Or my whole idea is wrong? Please help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-buildings" rel="tag" title="see questions tagged &#39;buildings&#39;">buildings</span> <span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Sep '13, 00:43</strong></p>
<img src="https://secure.gravatar.com/avatar/08f475a8bb3c347e3b9860776eacada8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KoyotGamma&#39;s gravatar image" />
<p><span>KoyotGamma</span><br />
<span class="score" title="193 reputation points">193</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KoyotGamma has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26625" class="comments-container">
<span id="51090"></span>
<div id="comment-51090" class="comment">
<div id="post-51090-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>While not directly applicable to this question specifically, if a building has more than one entrance and each entrance is associated with a different amenity, then I would tag each entrance with the information for the amenity and just leave the building as building:yes with the address information (assuming the address for all parts of the building is the same).</p>
</div>
<div id="comment-51090-info" class="comment-info">
<span class="comment-age">(25 Jul '16, 22:07)</span> <span class="comment-user userinfo">zellfaze</span>
</div>
</div>
</div>
<div id="comment-tools-26625" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26625-form-container" class="comment-form-container">
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

<span id="51214"></span>

<div id="answer-container-51214" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51214-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51214-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-51214-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'll split this answer into two parts: How to map the amenities, and how to map the addresses.</p>
<h2 id="mapping-multiple-amenities-in-a-building">Mapping multiple amenities in a building</h2>
<p>The easiest and most common solution is to create <strong>one node per amenity</strong>. As you noticed yourself, using only one element for all of them would cause conflicts between their attributes. Therefore, using one node, way, or relation for each "thing" – no more, no less – is a common principle in OSM tagging known as <a href="https://wiki.openstreetmap.org/wiki/One_feature,_one_OSM_element">one feature, one OSM element</a>.</p>
<p>If you want to add more detail, though, you might be interested in concepts from <strong>indoor mapping</strong>. With a tagging style such as <a href="https://wiki.openstreetmap.org/wiki/Simple_Indoor_Tagging">Simple Indoor Tagging</a> (see the <a href="https://wiki.openstreetmap.org/wiki/Indoor_Mapping">overview</a> for alternatives), this can be as simple as adding level tags to each amenity. On the other end of the spectrum, you might see amenities mapped as areas which represent their share of the floor, together with hallways, staircases and other features.</p>
<h2 id="mapping-multiple-amenities-with-the-same-address">Mapping multiple amenities with the same address</h2>
<p>Adding the shared address to the <strong>building outline</strong> is a good start. Not only does it avoid duplication, it's also entirely possible for programs to find out which amenities are inside the building outline, and conclude that they share the building's address. In practice, however, not many programs actually support that feature, so mappers often decide to tag the <strong>address on the amenities</strong> as well as the building outline. If there is already a consensus among mappers in your area, it's best to stick to that.</p>
<p>Every now and then, other approaches have been proposed, usually using <strong>relations</strong>. Those would be able to express very complex address situations. However, they tend to be strongly rejected in votes (<a href="https://wiki.openstreetmap.org/wiki/Proposed_features/AssociatedAddress_(new)#Voting">example</a>), and none of them has been mature enough to gain significant support yet.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Aug '16, 18:46</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-51214" class="comments-container">
&#10;</div>
<div id="comment-tools-51214" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51214-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="26632"></span>

<div id="answer-container-26632" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26632-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26632-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26632-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, A good question which I hoped someone else might answer before me as I have a similar problem with this building which is a health centre accommodating doctors, dentist, pharmacy &amp; physiotherapist all having different opening hours and contact details <a href="https://www.openstreetmap.org/browse/way/223249817">https://www.openstreetmap.org/browse/way/223249817</a></p>
<p>The multiple values in the amenity tag don't really work and I think I will replace them with the single value 'clinic' https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dclinic This would apply to the building which would continue to be tagged with the name Hillcrest Healthcare. I'd also delete the tag 'dispensing=yes' which only applies to the pharmacy part of the clinic.</p>
<p>I'd then put on separate nodes for each of the amenities with specified data about them as you suggest. I'm not sure what to do about addresses – just one for the building or individual ones for each amenity? Perhaps someone can advise.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Sep '13, 08:03</strong></p>
<img src="https://secure.gravatar.com/avatar/0b78593a39b9f71b9697697876327c6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NZGraham&#39;s gravatar image" />
<p><span>NZGraham</span><br />
<span class="score" title="1814 reputation points"><span>1.8k</span></span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="49 badges"><span class="bronze">●</span><span class="badgecount">49</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NZGraham has 7 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-26632" class="comments-container">
<span id="26642"></span>
<div id="comment-26642" class="comment">
<div id="post-26642-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Following the principle "<a href="https://wiki.openstreetmap.org/wiki/One_feature,_one_OSM_element">one feature, one OSM element</a>", I tag the address only once on the building polyogon or on a node attached to the facade. But some people don't think that address is a feature and repeats the same information on all POI's. It's a point of view question : if you are interrested by the dentist, you like to see immediatly his adress attached to its node. If you are interrested by addresses, you don't like unnecessary duplicates.</p>
</div>
<div id="comment-26642-info" class="comment-info">
<span class="comment-age">(23 Sep '13, 14:31)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-26632" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26632-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="26635"></span>

<div id="answer-container-26635" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26635-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26635-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-26635-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In my city ( <a href="https://www.openstreetmap.org/#map=17/50.06186/19.93749">https://www.openstreetmap.org/#map=17/50.06186/19.93749</a> ) I see two methods: ignore less important places (Sukiennice are filled with multiple shops, none is marked) or mark amenity as point objects (some buildings have 5 or more amenities).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Sep '13, 09:59</strong></p>
<img src="https://secure.gravatar.com/avatar/fd2f7303e92334ed1eef75268aed7611?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bulwersator&#39;s gravatar image" />
<p><span>Bulwersator</span><br />
<span class="score" title="468 reputation points">468</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bulwersator has one accepted answer">14%</span></p>
</div>
</div>
<div id="comments-container-26635" class="comments-container">
<span id="26646"></span>
<div id="comment-26646" class="comment">
<div id="post-26646-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>A feature should not get ignored only because there is a more important one next to it.</p>
</div>
<div id="comment-26646-info" class="comment-info">
<span class="comment-age">(23 Sep '13, 14:58)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="72452"></span>
<div id="comment-72452" class="comment">
<div id="post-72452-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How should I tag building that has more than one amenity? The one building used for rice_mill,corn_grinding and carpenter work with diesel generator.Should I try to tag more amenities on it with specified data about them? Please help.</p>
</div>
<div id="comment-72452-info" class="comment-info">
<span class="comment-age">(09 Jan '20, 05:35)</span> <span class="comment-user userinfo">chaw myat</span>
</div>
</div>
<span id="72453"></span>
<div id="comment-72453" class="comment">
<div id="post-72453-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/17687/chaw-myat">@chaw myat</a>: please create a new question if the answers on this question do not apply to your situation.</p>
</div>
<div id="comment-72453-info" class="comment-info">
<span class="comment-age">(09 Jan '20, 07:53)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-26635" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26635-form-container" class="comment-form-container">
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

