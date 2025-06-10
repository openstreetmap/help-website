+++
type = "question"
title = "Tiles does not render properly after attempt to correct self-intersecting polygon"
description = '''I am fairly new to OSM, have used IDeditor, and was trying out registering av path with Vespucci for Android, then suddenly tiles in a large area (relation 8234032)turned white in OSM standard layer. OSM inspector found a possible problem where I had managed to place a path over an already self-inte...'''
date = "2021-11-11T18:36:00Z"
lastmod = "2021-11-15T18:26:00Z"
weight = 82542
keywords = [ "self-intersection", "tiles", "natural", "render" ]
aliases = [ "/questions/82542" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tiles does not render properly after attempt to correct self-intersecting polygon](/questions/82542/tiles-does-not-render-properly-after-attempt-to-correct-self-intersecting-polygon)

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
<span id="post-82542-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82542-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82542-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am fairly new to OSM, have used IDeditor, and was trying out registering av path with Vespucci for Android, then suddenly tiles in a <a href="https://www.openstreetmap.org/#map=14/58.0808/7.7316">large area</a> (relation <a href="http://osm.org/relation/8234032">8234032</a>)turned white in OSM standard layer.</p>
<p>OSM inspector found a possible problem where I had managed to place a path over an already <a href="https://overpass-api.de/achavi/?changeset=113575629&amp;relations=true">self-intersecting polygon</a> for wetland, that i have corrected.</p>
<p>I dont know if this really caused it, because a few hours later the same area (relation 8234032)turned blue, and the same day someone had <a href="https://overpass-api.de/achavi/?changeset=113553592&amp;relations=true">corrected the Natural key</a> for this area from Wood to Water.</p>
<p>I <a href="https://overpass-api.de/achavi/?changeset=113578729&amp;relations=true">corrected the key back</a> to Wood.</p>
<p>This helped, now at least some of the zoom levels render correct, but still a lot of tiles are either white or blue for some reason.</p>
<p>Its been several days, i have tried to register a lot of the tiles "dirty", and have loaded maps in different devices/browsers. The tiles are still not rendering correct with OSM standard layer in various zoomlevels.</p>
<p>Can someone help me to find the problem here?</p>
<p>Thank you som much for your help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-self-intersection" rel="tag" title="see questions tagged &#39;self-intersection&#39;">self-intersection</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-natural" rel="tag" title="see questions tagged &#39;natural&#39;">natural</span> <span class="post-tag tag-link-render" rel="tag" title="see questions tagged &#39;render&#39;">render</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Nov '21, 18:36</strong></p>
<img src="https://secure.gravatar.com/avatar/8805b016a4eddedd583f2b46de1ee6d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="oyha&#39;s gravatar image" />
<p><span>oyha</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="oyha has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Nov '21, 19:08</strong> </span></p>
</div>
</div>
<div id="comments-container-82542" class="comments-container">
&#10;</div>
<div id="comment-tools-82542" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82542-form-container" class="comment-form-container">
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

<span id="82544"></span>

<div id="answer-container-82544" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82544-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82544-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82544-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The mapping looks OK, the tiles render OK at different zoom levels.</p>
<p>Patience? Or try clearing your browser cache?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Nov '21, 07:56</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-82544" class="comments-container">
<span id="82581"></span>
<div id="comment-82581" class="comment">
<div id="post-82581-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for checking here, but 9 days is a long time to wait, do I have to wait even longer? I have cleared coocies and cache, tried several browsers and devices, same problem. This is very strange...</p>
<p>An example is this blue squared area here in zoomlevel 15 and 17 that is present in multiple devices: <a href="https://osm.org/go/0SZr_TEp--">https://osm.org/go/0SZr_TEp--</a> and <a href="https://osm.org/go/0SZr8SDQw-">https://osm.org/go/0SZr8SDQw-</a></p>
<p>Any tips here is much appreciated.</p>
</div>
<div id="comment-82581-info" class="comment-info">
<span class="comment-age">(15 Nov '21, 18:26)</span> <span class="comment-user userinfo">oyha</span>
</div>
</div>
</div>
<div id="comment-tools-82544" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82544-form-container" class="comment-form-container">
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

