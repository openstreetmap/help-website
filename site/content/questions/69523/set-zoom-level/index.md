+++
type = "question"
title = "Set zoom level"
description = '''When I rendered local OSM tiles for India data. It&#x27;s showing the output as below. How can I change the zoom level![alt text][1] such that India map is show clearly. https://imgur.com/87wcKnP Here&#x27;s the link for image'''
date = "2019-06-07T12:14:00Z"
lastmod = "2019-06-07T14:23:00Z"
weight = 69523
keywords = [ "zoom" ]
aliases = [ "/questions/69523" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Set zoom level](/questions/69523/set-zoom-level)

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
<span id="post-69523-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69523-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69523-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I rendered local OSM tiles for India data. It's showing the output as below. How can I change the zoom level![alt text][1] such that India map is show clearly.</p>
<p><a href="https://imgur.com/87wcKnP">https://imgur.com/87wcKnP</a></p>
<p>Here's the link for image</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoom" rel="tag" title="see questions tagged &#39;zoom&#39;">zoom</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jun '19, 12:14</strong></p>
<img src="https://secure.gravatar.com/avatar/8310002871cb38b24453e184d4afa3d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Puranjay&#39;s gravatar image" />
<p><span>Puranjay</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Puranjay has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69523" class="comments-container">
&#10;</div>
<div id="comment-tools-69523" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69523-form-container" class="comment-form-container">
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

<span id="69526"></span>

<div id="answer-container-69526" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69526-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69526-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-69526-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You load the tile /0/0/0.png. Tiles are sorted into folders and names like this: {z}/{x}/{y}.png. So if you change your query to /1/0/0.png you will go one zoom level up.</p>
<p>Maybe you are looking for a real frontend to draw a map and zoom with your mouse? Check out Leaflet or Open Layers. It's also documented on the <a href="https://switch2osm.org/using-tiles/">swith2osm site</a> you are following.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '19, 12:35</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-69526" class="comments-container">
<span id="69527"></span>
<div id="comment-69527" class="comment">
<div id="post-69527-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So is there any way to figure out values of {X}, {y} and {z} to see entire map or it's just hit and trial.</p>
</div>
<div id="comment-69527-info" class="comment-info">
<span class="comment-age">(07 Jun '19, 12:40)</span> <span class="comment-user userinfo">Puranjay</span>
</div>
</div>
<span id="69529"></span>
<div id="comment-69529" class="comment">
<div id="post-69529-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://imgur.com/XM9EHBb">https://imgur.com/XM9EHBb</a></p>
<p>I have changed url to 'localhost/hot/{z}/{x}/{y}.png' and some images are not loading as showing in console.</p>
</div>
<div id="comment-69529-info" class="comment-info">
<span class="comment-age">(07 Jun '19, 13:07)</span> <span class="comment-user userinfo">Puranjay</span>
</div>
</div>
<span id="69530"></span>
<div id="comment-69530" class="comment">
<div id="post-69530-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You might have hit a timeout if the tiles weren't already rendered. Try refreshing to see if they are now available.</p>
</div>
<div id="comment-69530-info" class="comment-info">
<span class="comment-age">(07 Jun '19, 13:31)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="69531"></span>
<div id="comment-69531" class="comment">
<div id="post-69531-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you want to work out x, y and z values, see <a href="https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames">https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames</a></p>
</div>
<div id="comment-69531-info" class="comment-info">
<span class="comment-age">(07 Jun '19, 13:34)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-69526" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69526-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69534"></span>

<div id="answer-container-69534" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69534-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69534-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69534-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In a comment on an answer to your other question, I mentioned that <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/manually-building-a-tile-server-18-04-lts/</a> suggests "In order to see tiles, we’ll cheat and use an html file “<code>sample_leaflet.html</code>” in mod_tile’s “extras” folder".</p>
<p>That's an HTML file that uses Leaflet (a Javascript library) to fetch the appropriate tiles so that you can view a full map. It's probably the easiest way to achieve what you want, but it would help if you explained what you want a map <em>for</em> - do you want to embed something in a web site, print it out, something else?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '19, 14:23</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-69534" class="comments-container">
&#10;</div>
<div id="comment-tools-69534" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69534-form-container" class="comment-form-container">
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

