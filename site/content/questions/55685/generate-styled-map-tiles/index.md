+++
type = "question"
title = "Generate styled Map Tiles"
description = '''&#x27;m trying to create an app that contains a small map that should always work without internet connection for four different zoom levels. To do this i know that i have to generate map tiles in png (or similar) to be used later on by Leaflet (or Open Layer/Mapbox GL JS) . This is no issue, because usi...'''
date = "2017-04-18T19:38:00Z"
lastmod = "2017-04-19T15:26:00Z"
weight = 55685
keywords = [ "openstreetmap", "tiles", "mapbox" ]
aliases = [ "/questions/55685" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Generate styled Map Tiles](/questions/55685/generate-styled-map-tiles)

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
<span id="post-55685-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55685-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55685-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>'m trying to create an app that contains a small map that should always work without internet connection for four different zoom levels. To do this i know that i have to generate map tiles in png (or similar) to be used later on by Leaflet (or Open Layer/Mapbox GL JS) . This is no issue, because using Maperitive i can generate map tiles with given bounds and min and max zoom levels.</p>
<p>My problem is that i need to use a different style for roads, buildings, etc. To edit this style i used Mapbox Studio online editor and generated a JSON file with my custom styles.</p>
<p>What i need to do is <strong>apply this style before generating the resulting tiles</strong>, but i don't know how to do this. Below there's a diagram for what i'm thinking about.</p>
<p><img src="https://i.stack.imgur.com/T7PAY.png" alt="Diagram" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-mapbox" rel="tag" title="see questions tagged &#39;mapbox&#39;">mapbox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Apr '17, 19:38</strong></p>
<img src="https://secure.gravatar.com/avatar/50c99d55b9f176ad72182e194c79390c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rr%20alves&#39;s gravatar image" />
<p><span>rr alves</span><br />
<span class="score" title="30 reputation points">30</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rr alves has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-55685" class="comments-container">
<span id="55686"></span>
<div id="comment-55686" class="comment">
<div id="post-55686-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>crosspost: <a href="https://gis.stackexchange.com/questions/237132/generate-styled-map-tiles">https://gis.stackexchange.com/questions/237132/generate-styled-map-tiles</a></p>
</div>
<div id="comment-55686-info" class="comment-info">
<span class="comment-age">(18 Apr '17, 21:04)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-55685" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55685-form-container" class="comment-form-container">
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

<span id="55695"></span>

<div id="answer-container-55695" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55695-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55695-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55695-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rr alves has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Mapbox Studio style json is used to visually render <a href="https://www.mapbox.com/vector-tiles/">Mapbox vector tiles</a> in the browser using <a href="https://www.mapbox.com/mapbox-gl-js/api/">Mapbox GL JS</a>. There is no mechanism to convert these into the png tiles that you are expecting unfortunately.</p>
<p>Your best bet might be to create multiple maperitive styles and generate the tiles.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Apr '17, 08:58</strong></p>
<img src="https://secure.gravatar.com/avatar/f2fe6e2598a7e82fe4f83297274c60c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PlaneMad&#39;s gravatar image" />
<p><span>PlaneMad</span><br />
<span class="score" title="282 reputation points">282</span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PlaneMad has 2 accepted answers">33%</span></p>
</div>
</div>
<div id="comments-container-55695" class="comments-container">
<span id="55696"></span>
<div id="comment-55696" class="comment">
<div id="post-55696-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the reply. I'll follow Maperitive documentation.</p>
</div>
<div id="comment-55696-info" class="comment-info">
<span class="comment-age">(19 Apr '17, 09:05)</span> <span class="comment-user userinfo">rr alves</span>
</div>
</div>
<span id="55699"></span>
<div id="comment-55699" class="comment">
<div id="post-55699-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It worked. It's a bit harder to style than Mapbox but works.</p>
</div>
<div id="comment-55699-info" class="comment-info">
<span class="comment-age">(19 Apr '17, 15:26)</span> <span class="comment-user userinfo">rr alves</span>
</div>
</div>
</div>
<div id="comment-tools-55695" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55695-form-container" class="comment-form-container">
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

