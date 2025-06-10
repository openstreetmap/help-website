+++
type = "question"
title = "Routing in pedestrian areas"
description = '''It seems that routing does not work on pedestrian areas, as I can see it in this place https://www.openstreetmap.org/directions?engine=fossgis_osrm_foot&amp;amp;route=43.18409%2C-2.47186%3B43.18343%2C-2.47295#map=19/43.18349/-2.47138   So, how should we be tagging so that tracking works in these areas?'''
date = "2019-05-28T13:12:00Z"
lastmod = "2020-06-26T17:48:00Z"
weight = 69349
keywords = [ "pedestrian", "routing", "area" ]
aliases = [ "/questions/69349" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Routing in pedestrian areas](/questions/69349/routing-in-pedestrian-areas)

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
<span id="post-69349-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69349-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69349-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>It seems that routing does not work on pedestrian areas, as I can see it in this place <a href="https://www.openstreetmap.org/directions?engine=fossgis_osrm_foot&amp;route=43.18409%2C-2.47186%3B43.18343%2C-2.47295#map=19/43.18349/-2.47138">https://www.openstreetmap.org/directions?engine=fossgis_osrm_foot&amp;route=43.18409%2C-2.47186%3B43.18343%2C-2.47295#map=19/43.18349/-2.47138</a></p>
<p><img src="https://help.openstreetmap.org/upfiles/routing.png" alt="Routing not working through pedestrian area" /></p>
<p>So, how should we be tagging so that tracking works in these areas?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pedestrian" rel="tag" title="see questions tagged &#39;pedestrian&#39;">pedestrian</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 May '19, 13:12</strong></p>
<img src="https://secure.gravatar.com/avatar/65427ff1b06518873c149787d6928a21?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="garaolaza&#39;s gravatar image" />
<p><span>garaolaza</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="garaolaza has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-69349" class="comments-container">
&#10;</div>
<div id="comment-tools-69349" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69349-form-container" class="comment-form-container">
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

<span id="69356"></span>

<div id="answer-container-69356" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69356-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69356-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-69356-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>Note: Most pedestrian routing algorithms do not currently route (correctly) across area features, tending to route around the edge or not at all (especially in case of multipolygons). Do not alter your mapping to accommodate such routers.</p>
</blockquote>
<p>Source: <a href="https://wiki.openstreetmap.org/wiki/Key:area">https://wiki.openstreetmap.org/wiki/Key:area</a></p>
<p>So I think, we will need to wait routers to be fixed. Have you consider creating issues on routers trackers?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 May '19, 22:16</strong></p>
<img src="https://secure.gravatar.com/avatar/4c64a7804404d4c69c2e57c24e438714?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Binnette&#39;s gravatar image" />
<p><span>Binnette</span><br />
<span class="score" title="86 reputation points">86</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Binnette has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69356" class="comments-container">
<span id="69359"></span>
<div id="comment-69359" class="comment">
<div id="post-69359-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There are issues already. It’s just a hard problem to solve (and one with comparatively little financial reward, so unlikely to be prioritised by paid developers).</p>
</div>
<div id="comment-69359-info" class="comment-info">
<span class="comment-age">(29 May '19, 09:40)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-69356" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69356-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69351"></span>

<div id="answer-container-69351" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69351-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69351-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-69351-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Ideally the various routers should be able to route through an area. But, with what little I know of routing algorithms, this seems to be very hard to do and I am not aware of any router that uses OSM data that does this.</p>
<p>Some mappers figure that a map that actually works for people is preferable to one that doesn't and add "virtual footways" through the pedestrian area aligned with common or logical ways that people usually walk through the area. This allows existing routers to do the right thing. Or at least closer to the right thing than if it is only mapped as an area.</p>
<p>However other mappers are adamant that adding "virtual footways" is tagging for the renderer and should not be done.</p>
<p>Fortunately for me, there are very few pedestrian areas near me so I don't have to get too involved with either school of mapping and can just sit on the side and watch the arguments that haven't changed in the years I've been mapping.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 May '19, 18:48</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-69351" class="comments-container">
<span id="69353"></span>
<div id="comment-69353" class="comment">
<div id="post-69353-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I feel mapping "virtual footways" is ok as a temporary workaround for routers' shortcomings. However, using <em>the same tag</em> for "virtual footways" as for real footways is not, because doing so negatively affects correctly-written software. This is precisely what the rules against <a href="https://wiki.openstreetmap.org/wiki/Mapping_for_the_renderer">"mapping for the renderer"</a> intend to prevent. (The data would be indistinguishable from the case where there's actually a visibly different path crossing the plaza on the ground.)</p>
<p>It would be utterly trivial for routers which do not support routing across polygons to at least at support ways with some newly made-up tag like <code>routing_hint:highway=footway</code>, allowing the creation of virtual footways that do not interfere with other uses of the data.</p>
<p>(This comment is about actual plazas. There's also a separate problem where mappers incorrectly map pedestrianized streets as highway=pedestrian + area=yes despite being clearly linear.)</p>
</div>
<div id="comment-69353-info" class="comment-info">
<span class="comment-age">(28 May '19, 20:37)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-69351" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69351-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75440"></span>

<div id="answer-container-75440" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75440-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75440-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75440-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Open Trip Planner does area routing,</p>
<p>If you look at the guidelines they also list how to do area routing for other routing engines:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Guidelines_for_pedestrian_navigation">https://wiki.openstreetmap.org/wiki/Guidelines_for_pedestrian_navigation</a></p>
<p>As you see here it is quite okay to mark the main linear features of an area, while it won't yield as good an answer as an area router (unless you went mad and added all possible movements!)</p>
<p><a href="https://wiki.openstreetmap.org/wiki/File:Line_area_connection-EN.png">https://wiki.openstreetmap.org/wiki/File:Line_area_connection-EN.png</a></p>
<p>For the above example it would be quite okay to add a "F" shaped set of links within the area, while you shouldn't tag for the renderer it seems like the renders know not to render pedetrian ways within an area, that or it's invisible.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '20, 17:48</strong></p>
<img src="https://secure.gravatar.com/avatar/e4a3b88a2d65ba17d20b29c06c10f0d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DevonshireBoy42&#39;s gravatar image" />
<p><span>DevonshireBoy42</span><br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DevonshireBoy42 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75440" class="comments-container">
&#10;</div>
<div id="comment-tools-75440" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75440-form-container" class="comment-form-container">
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

