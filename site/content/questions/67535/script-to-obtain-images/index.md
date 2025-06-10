+++
type = "question"
title = "Script to obtain images"
description = '''We have a list of specific lat/lon coordinates in a spreadsheet that we&#x27;d like to have images for. We have the OpenStreetMap query strings ready to go, but need a more automated way to pull the images rather than manually. Anyone else tackled this yet? Perhaps with a script? The images would need to...'''
date = "2019-01-10T19:13:00Z"
lastmod = "2019-01-10T19:48:00Z"
weight = 67535
keywords = [ "lat", "lon", "image", "export", "png" ]
aliases = [ "/questions/67535" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Script to obtain images](/questions/67535/script-to-obtain-images)

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
<span id="post-67535-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67535-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67535-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We have a list of specific lat/lon coordinates in a spreadsheet that we'd like to have images for. We have the OpenStreetMap query strings ready to go, but need a more automated way to pull the images rather than manually. Anyone else tackled this yet? Perhaps with a script?</p>
<p>The images would need to be available offline, so we need static PNGs (or similar) that would look OK on mobile. Specific locations are landmarks that don't change often, so real-time not critical. Not stuck on specific size yet, so that's flexible. 1200 x 900 to start?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-lat" rel="tag" title="see questions tagged &#39;lat&#39;">lat</span> <span class="post-tag tag-link-lon" rel="tag" title="see questions tagged &#39;lon&#39;">lon</span> <span class="post-tag tag-link-image" rel="tag" title="see questions tagged &#39;image&#39;">image</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-png" rel="tag" title="see questions tagged &#39;png&#39;">png</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jan '19, 19:13</strong></p>
<img src="https://secure.gravatar.com/avatar/bdec27d1a17b2a5c6f46761308967183?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jjdeprisco&#39;s gravatar image" />
<p><span>jjdeprisco</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jjdeprisco has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jan '19, 19:30</strong> </span></p>
</div>
</div>
<div id="comments-container-67535" class="comments-container">
<span id="67536"></span>
<div id="comment-67536" class="comment">
<div id="post-67536-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Could you explain in a little more detail what you're trying to do? What size "images" do you want?</p>
<p>One approach to creating OpenStreetMap maps is to create a server that can create lots of small images and then display them together, so <a href="https://www.openstreetmap.org/#map=4/52.32/-7.52">this screen</a> contains <a href="https://a.tile.openstreetmap.org/4/7/5.png">this image</a> among many others. There are instructions for setting up such a tile server <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">here</a>.</p>
</div>
<div id="comment-67536-info" class="comment-info">
<span class="comment-age">(10 Jan '19, 19:26)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="67537"></span>
<div id="comment-67537" class="comment">
<div id="post-67537-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sure, see edit.</p>
</div>
<div id="comment-67537-info" class="comment-info">
<span class="comment-age">(10 Jan '19, 19:30)</span> <span class="comment-user userinfo">jjdeprisco</span>
</div>
</div>
</div>
<div id="comment-tools-67535" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67535-form-container" class="comment-form-container">
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

<span id="67538"></span>

<div id="answer-container-67538" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67538-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67538-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-67538-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OK, I'd start with <a href="https://wiki.openstreetmap.org/wiki/OSM_on_Paper">OSM on paper</a> and the links from there.</p>
<p>If you want to fetch map tiles from an OSM server, make sure you follow the <a href="https://operations.osmfoundation.org/policies/tiles/">tile usage policy</a> so that you don't get blocked.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jan '19, 19:48</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-67538" class="comments-container">
&#10;</div>
<div id="comment-tools-67538" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67538-form-container" class="comment-form-container">
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

