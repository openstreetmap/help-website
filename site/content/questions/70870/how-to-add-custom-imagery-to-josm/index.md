+++
type = "question"
title = "How to add custom imagery to JOSM?"
description = '''I&#x27;d like to add the tile layer behind map.atownsend.org.uk to JOSM. I believe that the resulting string should be: tms[24]:https://map.atownsend.org.uk/hot/{zoom}/{x}/{y}.png  Unfortunately, JOSM never sends requests for high zoom levels to the tile server. The problem isn&#x27;t at the tile server end, ...'''
date = "2019-09-21T12:11:00Z"
lastmod = "2019-09-29T18:42:00Z"
weight = 70870
keywords = [ "josm" ]
aliases = [ "/questions/70870" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to add custom imagery to JOSM?](/questions/70870/how-to-add-custom-imagery-to-josm)

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
<span id="post-70870-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70870-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70870-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'd like to add the tile layer behind <a href="https://map.atownsend.org.uk">map.atownsend.org.uk</a> to JOSM. I believe that the resulting string should be:</p>
<pre><code>tms[24]:https://map.atownsend.org.uk/hot/{zoom}/{x}/{y}.png</code></pre>
<p>Unfortunately, JOSM never sends requests for high zoom levels to the tile server. The problem isn't at the tile server end, as a request such as <a href="https://map.atownsend.org.uk/maps/map/map.html#zoom=24&amp;lat=54.04597259&amp;lon=-0.99491842">this</a> gets back tiles such as <a href="https://map.atownsend.org.uk/hot/24/8342241/5383209.png">https://map.atownsend.org.uk/hot/24/8342241/5383209.png</a>. What I get back instead is a black screen for tiles from zoom levels 21/22 and up. Oddly it sometimes requests zoom 22 tiles but mostly not. it doesn't matter if the required tile is already rendered or not.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Sep '19, 12:11</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Sep '19, 18:29</strong> </span></p>
</div>
</div>
<div id="comments-container-70870" class="comments-container">
<span id="70887"></span>
<div id="comment-70887" class="comment">
<div id="post-70887-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>1 extra bit of info: I'm using JOSM 14945 (which is quite old). However, another user is also testing (presumably after seeing this help question) with JOSM 15322 and seeing the same effect (or at least, they're not sending me requests for zooms &gt; 22 from JOSM).</p>
</div>
<div id="comment-70887-info" class="comment-info">
<span class="comment-age">(22 Sep '19, 16:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-70870" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70870-form-container" class="comment-form-container">
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

<span id="70871"></span>

<div id="answer-container-70871" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70871-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70871-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70871-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you go into imagery preferences and look at the settings tab there is a Panel for TMS settings where you can set max and min zoom.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Sep '19, 15:07</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-70871" class="comments-container">
<span id="70872"></span>
<div id="comment-70872" class="comment">
<div id="post-70872-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There are (at a rough guess) 1000 preferences in there and about 30 of those match the search word "zoom". Which one(s) should be changed? I did try changing one (imagery.tms.max_zoom_lvl) before asking the question but it didn't seem to have any effect.</p>
<p>Edit: It appears that the button that I was pressing to get to that list is actually "advanced preferences", despite it being next to a label that says "imagery preferences". JOSM is (how can I put this tactfully) "somewhat unclear" at indicating what user actions will have what effect.</p>
</div>
<div id="comment-70872-info" class="comment-info">
<span class="comment-age">(21 Sep '19, 15:24)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="70873"></span>
<div id="comment-70873" class="comment">
<div id="post-70873-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It'll probably end up there, but this is in the main imagery preferences area one tab right of the list of sources.</p>
</div>
<div id="comment-70873-info" class="comment-info">
<span class="comment-age">(21 Sep '19, 16:32)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="70885"></span>
<div id="comment-70885" class="comment">
<div id="post-70885-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, that doesn't fix it. I went into "JOSM / Imagery / Imagery preferences / settings" and in "TMS Settings" changed "Max zoom level" from 20 to 24.</p>
<p>On the server I can see tile requests for zoom 22:</p>
<pre><code>Sep 22 15:26:31 map renderd[1810]: DEBUG: START TILE ajt 22 2084208-2084215 1344664-1344671, new metatile</code></pre>
<p>but not for zoom level 23, and just a black screen in JOSM.</p>
</div>
<div id="comment-70885-info" class="comment-info">
<span class="comment-age">(22 Sep '19, 14:29)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="70888"></span>
<div id="comment-70888" class="comment">
<div id="post-70888-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>JOSM seems to be acting rather oddly at these zooms.</p>
<p>For your example URL it seems I can get the scale in the top left to go down as far as 1.0m. <em>OS OpenData StreetView</em> and <em>NLS - Bartholomew Half inch, 1897-1907</em> seems to (over)zoom down to between 0.5m and 0.01m depending on exactly where I look on the map. JOSM also doesn't like switching layers or panning when the zoom slider is 'against the stop'.</p>
<p>The <em>Kartverket Address Overlay</em> (WMS) seems to work OK at zoom 24 when looking at a random part of Oslo.</p>
<p>I think you may have found a bug.</p>
</div>
<div id="comment-70888-info" class="comment-info">
<span class="comment-age">(22 Sep '19, 16:27)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="70961"></span>
<div id="comment-70961" class="comment">
<div id="post-70961-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've logged this at <a href="https://josm.openstreetmap.de/ticket/18184#ticket">https://josm.openstreetmap.de/ticket/18184#ticket</a></p>
<p>Actually, one tile request for "23/0/0.png" and "24/0/0.png" is sent, and after the latter it crashes (details on the ticket, along with the conversion function that's failing with a "Not a Number" error.</p>
</div>
<div id="comment-70961-info" class="comment-info">
<span class="comment-age">(29 Sep '19, 18:42)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-70871" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70871-form-container" class="comment-form-container">
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

