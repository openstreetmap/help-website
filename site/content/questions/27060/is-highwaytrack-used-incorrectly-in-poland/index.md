+++
type = "question"
title = "Is highway=track used incorrectly in Poland?"
description = '''The definition of a track states it&#x27;s a road used for agricultural and forestry purposes. I infer this means whenever a road is the only means to access a residential building it shouldn&#x27;t be tagged as a track. In Poland on the countryside there are many such ways that are tagged as a track (based o...'''
date = "2013-10-10T01:29:00Z"
lastmod = "2013-10-10T13:23:00Z"
weight = 27060
keywords = [ "track", "unclassified", "tagging", "rural" ]
aliases = [ "/questions/27060" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Is highway=track used incorrectly in Poland?](/questions/27060/is-highwaytrack-used-incorrectly-in-poland)

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
<span id="post-27060-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27060-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-27060-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The definition of a track states it's a road used for agricultural and forestry purposes. I infer this means whenever a road is the only means to access a residential building it shouldn't be tagged as a track. In Poland on the countryside there are many such ways that are tagged as a track (based on physical appearance such as band of grass in the middle), even though they lead to a house or a few. Examples: <a href="http://osm.org/go/0LVUQapy--">first</a> and <a href="http://osm.org/go/0OtD4eTJ-">second</a></p>
<p>Should they be tagged as unclassified + unpaved instead? Should I split them into unclassified and track where residence ends? My question pertains mainly to tracing aerial imagery in locations which due to their low population density are unlikely to be surveyed in the near future.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-track" rel="tag" title="see questions tagged &#39;track&#39;">track</span> <span class="post-tag tag-link-unclassified" rel="tag" title="see questions tagged &#39;unclassified&#39;">unclassified</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-rural" rel="tag" title="see questions tagged &#39;rural&#39;">rural</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Oct '13, 01:29</strong></p>
<img src="https://secure.gravatar.com/avatar/b68bcf9f1c4a7921aeee1bb35b0e2784?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RicoElectrico&#39;s gravatar image" />
<p><span>RicoElectrico</span><br />
<span class="score" title="371 reputation points">371</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RicoElectrico has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-27060" class="comments-container">
<span id="27079"></span>
<div id="comment-27079" class="comment">
<div id="post-27079-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am not sure about tagging some of these ways as driveways: they often lead to a (small - like 5 to a two dozen houses) settlement which is a village anyway. They are also recognized officially as "municipal road" (droga gminna). The main problem with a track is that many (most?) routing engines outright reject it, even it is the last or the first "hop" on the route. Would adding access=destination (which enables routability in OSRM) be correct? Still, they are likely to be a non-destination road for pedestrian and cycle traffic.</p>
<p>My concern on tagging roads based their usage is that it cannot be verified even by survey. There is simply too small a traffic. (Also, it is quite inconsequential that down to tertiary it is the local importance that matters and below it's their usage.)</p>
</div>
<div id="comment-27079-info" class="comment-info">
<span class="comment-age">(10 Oct '13, 12:34)</span> <span class="comment-user userinfo">RicoElectrico</span>
</div>
</div>
<span id="27080"></span>
<div id="comment-27080" class="comment">
<div id="post-27080-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If they are minor public roads leading to a village or connecting two more important roads together then they should be tagged as <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dunclassified">unclassified</a> roads. Most routers should handle them correctly.</p>
</div>
<div id="comment-27080-info" class="comment-info">
<span class="comment-age">(10 Oct '13, 13:23)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-27060" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27060-form-container" class="comment-form-container">
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

<span id="27067"></span>

<div id="answer-container-27067" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27067-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27067-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-27067-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think that we have to recognise here that different OSM communities around the world map things in different ways. <span>@scai</span>'s answer and the wiki reflect the view (common in Germany, and also elsewhere) that there simply has to be one simple classification of highways and all we have to do is to do is to fit things into that and everything's good.</p>
<p>However, it simply isn't like this everywhere. In England**, a primary differentiator of different kinds of roads is what they looks like - something that's a gravel track simply wouldn't be considered a road, even if there are houses at the end of it. I spent 18 years living at the end of one and would never have referred to the thing outside the front door as a "road".</p>
<p>Another English complication is that there are plenty of examples of what would even in Germany be considered "tracks" that are legally part of the normal road network, but are no more than dirt tracks, and aren't used by normal motor traffic because they're impassable. Sometimes the existence of these can cause drivers blindly following commercial satnavs to drive to places that are legally accessible but physically not, resulting in the usual hilarious newspaper headlines.</p>
<p>However, as <span>@stf</span> has said, this idea of "what's a track and what's a road" isn't universal, so whereas normal OSM tries to use "the British English meaning" of something, here you're really best off asking other local Polish mappers. <a href="https://wiki.openstreetmap.org/wiki/Duck_tagging">If they consider something a track, it's probably a track</a>. Don't read to much into e.g. "agricultural and forestry" in the wiki - that says a lot of things, many of them contradictory.</p>
<p>** Strictly "England and Wales" - the legal system in Scotland is different and I've no great experience of the vaguaries that may exist there (or in Northern Ireland).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Oct '13, 09:53</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-27067" class="comments-container">
&#10;</div>
<div id="comment-tools-27067" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27067-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="27064"></span>

<div id="answer-container-27064" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27064-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27064-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-27064-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>We have a similar situation in the western parts of the United States. Most of the driveways where my folks live look like tracks on the satellite photos but the people there consider them driveways so that is how I tag them (highway=service, service=driveway).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Oct '13, 04:01</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-27064" class="comments-container">
<span id="27076"></span>
<div id="comment-27076" class="comment">
<div id="post-27076-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think "service=driveway" needs an "access=private", no ?</p>
</div>
<div id="comment-27076-info" class="comment-info">
<span class="comment-age">(10 Oct '13, 12:14)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="27078"></span>
<div id="comment-27078" class="comment">
<div id="post-27078-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span>@Pieren</span> Not necessarily all of them have such a restriction. But probably most of the driveways leading to a residence do.</p>
</div>
<div id="comment-27078-info" class="comment-info">
<span class="comment-age">(10 Oct '13, 12:19)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-27064" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27064-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="27066"></span>

<div id="answer-container-27066" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27066-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27066-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27066-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is an excellent question and you are right that <em>track</em> is often misused. This is not only a problem of Poland but seems to exist everywhere. People tend to tag roads how they <em>look</em> like which is often wrong because the different highway classes should reflect what and for whom the road is <em>used</em> for.</p>
<p>If the road leads to a single residence then it is often a driveway and should be tagged with <em>highway=service, service=driveway</em> as correctly explained by <a href="https://help.openstreetmap.org/users/5918/stf"><span><span>@stf</span></span></a>. And as you have correctly stated, <em>highway=unclassified</em> is also often the better tag for wrongly tagged tracks. It should be used for roads which have <em>lower importance in the road network than tertiary roads, and are not residential streets or agricultural tracks</em>. See the <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dunclassified">wiki</a> for a full explanation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Oct '13, 06:28</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Oct '13, 10:09</strong> </span></p>
</div>
</div>
<div id="comments-container-27066" class="comments-container">
&#10;</div>
<div id="comment-tools-27066" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27066-form-container" class="comment-form-container">
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

