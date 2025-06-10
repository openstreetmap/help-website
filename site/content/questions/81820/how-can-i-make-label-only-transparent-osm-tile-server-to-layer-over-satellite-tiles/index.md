+++
type = "question"
title = "How can I make label-only transparent OSM tile server to layer over satellite tiles?"
description = '''I currently have a satellite tile server based on an mbtiles file, and I also have a normal openstreetmap tile server with the normal carto styling. But I want to make my openstreetmap tiles as a layer over my satellite layer. So I guess I need to change the style.css of my osm tile server so it onl...'''
date = "2021-09-20T14:05:00Z"
lastmod = "2021-09-20T15:36:00Z"
weight = 81820
keywords = [ "openstreetmap-carto", "layers", "satellite", "mbtiles" ]
aliases = [ "/questions/81820" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How can I make label-only transparent OSM tile server to layer over satellite tiles?](/questions/81820/how-can-i-make-label-only-transparent-osm-tile-server-to-layer-over-satellite-tiles)

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
<span id="post-81820-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81820-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81820-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I currently have a satellite tile server based on an mbtiles file, and I also have a normal openstreetmap tile server with the normal carto styling.</p>
<p>But I want to make my openstreetmap tiles as a layer over my satellite layer. So I guess I need to change the style.css of my osm tile server so it only contains labels so I can use it as a layer over my satellite layer.</p>
<p>However, I can't really find any concrete examples and I can't find my way in the carto styling as it really is complex.</p>
<p>So are there any carto styling "templates" which I could use so that my tile server only offers transparent label-only tiles? Or is there another (easy) way to just have "label" tiles?</p>
<p>My satellite tile server is running with <a href="https://github.com/maptiler/tileserver-php">https://github.com/maptiler/tileserver-php</a>.</p>
<p>My OSM tile server is setup using the following tutorial: <a href="https://www.linuxbabe.com/ubuntu/openstreetmap-tile-server-ubuntu-20-04-osm">How to Set Up OpenStreetMap Tile Server on Ubuntu 20.04</a>.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap-carto" rel="tag" title="see questions tagged &#39;openstreetmap-carto&#39;">openstreetmap-carto</span> <span class="post-tag tag-link-layers" rel="tag" title="see questions tagged &#39;layers&#39;">layers</span> <span class="post-tag tag-link-satellite" rel="tag" title="see questions tagged &#39;satellite&#39;">satellite</span> <span class="post-tag tag-link-mbtiles" rel="tag" title="see questions tagged &#39;mbtiles&#39;">mbtiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Sep '21, 14:05</strong></p>
<img src="https://secure.gravatar.com/avatar/04175cc004ecad1e262fad8e94f86d62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KoenMlt&#39;s gravatar image" />
<p><span>KoenMlt</span><br />
<span class="score" title="42 reputation points">42</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KoenMlt has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81820" class="comments-container">
&#10;</div>
<div id="comment-tools-81820" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81820-form-container" class="comment-form-container">
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

<span id="81821"></span>

<div id="answer-container-81821" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81821-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81821-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81821-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="KoenMlt has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>See <a href="https://www.openstreetmap.org/user/SomeoneElse/diary/47007">here</a> for a bit more detail, but the important information is:</p>
<p>"... Next the style needed to be changed so that boundaries were displayed over transparent tiles. This was done by changing water-color and land-color in style.mss to “rgba(0,0,0,0)” in each case."</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Sep '21, 14:43</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-81821" class="comments-container">
<span id="81823"></span>
<div id="comment-81823" class="comment">
<div id="post-81823-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I've never set up a tile server myself but what SomeoneElse describes in his blog and the example page he links to from there looks exactly like what you are asking for. So I wonder why you voted down the answer, <a href="https://help.openstreetmap.org/users/20674/koenmlt">@KoenMlt</a>, not even leaving a comment.</p>
</div>
<div id="comment-81823-info" class="comment-info">
<span class="comment-age">(20 Sep '21, 15:18)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="81826"></span>
<div id="comment-81826" class="comment">
<div id="post-81826-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Oh crap my bad, thank you for letting me know. Was a bit too quick and missed the "Mark as answer" button. I corrected it.</p>
</div>
<div id="comment-81826-info" class="comment-info">
<span class="comment-age">(20 Sep '21, 15:36)</span> <span class="comment-user userinfo">KoenMlt</span>
</div>
</div>
</div>
<div id="comment-tools-81821" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81821-form-container" class="comment-form-container">
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

