+++
type = "question"
title = "could anyone explain this to me ... Leaflet"
description = '''hello I was using leaflet to get map from openstreet map and came across this.  http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png could anyone explain it to me? I got the map but not in the right position and the right portion that i wanted thank you'''
date = "2012-06-20T04:03:00Z"
lastmod = "2012-06-20T12:10:00Z"
weight = 13645
keywords = [ "leaflet", "api" ]
aliases = [ "/questions/13645" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [could anyone explain this to me ... Leaflet](/questions/13645/could-anyone-explain-this-to-me-leaflet)

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
<span id="post-13645-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13645-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13645-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hello</p>
<p>I was using leaflet to get map from openstreet map and came across this.</p>
<p>http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png</p>
<p>could anyone explain it to me? I got the map but not in the right position and the right portion that i wanted</p>
<p>thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jun '12, 04:03</strong></p>
<img src="https://secure.gravatar.com/avatar/e2a5920f142e0990758006633db064f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frensforall&#39;s gravatar image" />
<p><span>frensforall</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frensforall has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jun '12, 17:11</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span></p>
</div>
</div>
<div id="comments-container-13645" class="comments-container">
&#10;</div>
<div id="comment-tools-13645" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13645-form-container" class="comment-form-container">
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

<span id="13658"></span>

<div id="answer-container-13658" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13658-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13658-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-13658-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Leaflet displays a map by displaying a series of tiles across the page. It needs to know where to get these tiles from and how the tiles are stored in a directory structure. The statement you quote shows leaflet how the OSM tiles are structured. If you used tiles from another source the structure would be different.</p>
<p>Leaflet has fairly good documentation, the part describing how the tiles are structured is here: <a href="http://leaflet.cloudmade.com/reference.html#tilelayer">http://leaflet.cloudmade.com/reference.html#tilelayer</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jun '12, 12:10</strong></p>
<img src="https://secure.gravatar.com/avatar/b906204accce0fd58bc408b22bae01f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChrisH&#39;s gravatar image" />
<p><span>ChrisH</span><br />
<span class="score" title="4075 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="42 badges"><span class="silver">●</span><span class="badgecount">42</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChrisH has 11 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-13658" class="comments-container">
&#10;</div>
<div id="comment-tools-13658" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13658-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13650"></span>

<div id="answer-container-13650" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13650-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13650-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-13650-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That line looks like the placeholder string for the url to the tiles that make up the standard layer. Leaflet will replace all the strings in curly braces '{}' to get the url for the tile it wants.</p>
<p>For instance <a href="http://b.tile.openstreetmap.org/8/127/85.png">http://b.tile.openstreetmap.org/8/127/85.png</a> will give you a nice tile covering the south of england.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jun '12, 07:11</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-13650" class="comments-container">
&#10;</div>
<div id="comment-tools-13650" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13650-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13654"></span>

<div id="answer-container-13654" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13654-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13654-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-13654-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The tile layer definition has z, x, and y in it. They're replaced with actual values whenever Leaflet needs to fetch a tile. If you've got a working map, but it's centered on the wrong, you probably just need to tell Leaflet where to centre the map.<br />
</p>
<p>If you look at <a href="http://switch2osm.org/using-tiles/getting-started-with-leaflet/">this</a> example, you'll see that it contains:</p>
<pre><code>map.setView(new L.LatLng(51.3, 0.7),9);</code></pre>
<p>It's that function call that tells Leaflet where to centre the map and at what zoom level. If you replace "51.3" with the latitude you want, "0.7" with the longitude, and 9 with the zoom level, you'll get a map centred wherever you want it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jun '12, 09:36</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></p>
</div>
</div>
<div id="comments-container-13654" class="comments-container">
&#10;</div>
<div id="comment-tools-13654" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13654-form-container" class="comment-form-container">
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

