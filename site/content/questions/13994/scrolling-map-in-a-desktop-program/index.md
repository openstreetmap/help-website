+++
type = "question"
title = "Scrolling map in a desktop program"
description = '''I&#x27;m just starting to look at openstreetmap to see if it is possible to add a scrolling map to an existing Windows desktop program. The map would look something like the bottom-right window here http://www.youtube.com/watch?feature=player_embedded&amp;amp;v=r4rwMV7hhaY#at=840 which shows the current posi...'''
date = "2012-07-05T16:49:00Z"
lastmod = "2012-07-07T11:19:00Z"
weight = 13994
keywords = [ "windows", "openstreetmap", "gps", "desktop" ]
aliases = [ "/questions/13994" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Scrolling map in a desktop program](/questions/13994/scrolling-map-in-a-desktop-program)

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
<span id="post-13994-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13994-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13994-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm just starting to look at openstreetmap to see if it is possible to add a scrolling map to an existing Windows desktop program. The map would look something like the bottom-right window here</p>
<p><a href="http://www.youtube.com/watch?feature=player_embedded&amp;v=r4rwMV7hhaY#at=840">http://www.youtube.com/watch?feature=player_embedded&amp;v=r4rwMV7hhaY#at=840</a></p>
<p>which shows the current position of a moving vehicle. A "current" set of GPS coordinates would somehow be passed to the map which would have a central marker to show the current position, and the map would scroll slowly so that the marker was always in the center.</p>
<p>The example in the video clip seems to be using Google Maps, but this is very expensive to use even for a small commercial program. Has anyone written a similar module for openstreetmap?</p>
<p>Also, the map images would have to be fetched from a server as it scrolled. I believe that openstreetmap has servers which provide the images, but what are the restrictions on using these in a commercial program? Would a user of such a program get "cut off" from the openstreetmap image server if they were using it too heavily?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span> <span class="post-tag tag-link-desktop" rel="tag" title="see questions tagged &#39;desktop&#39;">desktop</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jul '12, 16:49</strong></p>
<img src="https://secure.gravatar.com/avatar/2490c8727d1986e5bba4fd38250500ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="appleton&#39;s gravatar image" />
<p><span>appleton</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="appleton has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jul '12, 16:56</strong> </span></p>
</div>
</div>
<div id="comments-container-13994" class="comments-container">
&#10;</div>
<div id="comment-tools-13994" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13994-form-container" class="comment-form-container">
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

<span id="13998"></span>

<div id="answer-container-13998" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13998-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13998-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-13998-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="appleton has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are numerous libraries that provide some sort of tile-based map display like OpenLayers does in a browser; you can usually find them by searching for "OpenLayers clone in &lt;programming language&gt;" or so. If you're thinking of a .NET program then <a href="https://wiki.openstreetmap.org/wiki/OpenStreetMapViewer">OpenStreetMapViewer</a> might be suitable for you. Similar code exists for Java, Flash, and other environments.</p>
<p>You are right about the map images ("tiles"). It is ok to load them from OSM for testing and there is no "non-commercial" restriction, however if your application starts to produce noticeable traffic then you are expected to set up your own tile server or use a commercial offering. See switch2osm.org for further information.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jul '12, 18:48</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-13998" class="comments-container">
<span id="14038"></span>
<div id="comment-14038" class="comment">
<div id="post-14038-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Frederik. I have a lot to read up on. :)</p>
</div>
<div id="comment-14038-info" class="comment-info">
<span class="comment-age">(06 Jul '12, 16:48)</span> <span class="comment-user userinfo">appleton</span>
</div>
</div>
<span id="14043"></span>
<div id="comment-14043" class="comment">
<div id="post-14043-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>If you're thinking of a .NET program then OpenStreetMapViewer might be suitable for you. Similar code exists for Java, Flash, and other environments.</p>
</blockquote>
<p>Is there existing code for C++ ?</p>
</div>
<div id="comment-14043-info" class="comment-info">
<span class="comment-age">(06 Jul '12, 18:29)</span> <span class="comment-user userinfo">appleton</span>
</div>
</div>
<span id="14047"></span>
<div id="comment-14047" class="comment">
<div id="post-14047-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://www.google.co.uk/search?q=OpenLayers+c%2B%2B">Yes.</a></p>
</div>
<div id="comment-14047-info" class="comment-info">
<span class="comment-age">(06 Jul '12, 19:28)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-13998" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13998-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="14063"></span>

<div id="answer-container-14063" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14063-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14063-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14063-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>(Disclaimer: I'm the author of Maperitive).</p>
<p><a href="http://maperitive.net/">Maperitive</a> uses its own WinForms control for displaying both the web and vector maps (written in C#). Given your use case you should consider drawing vector maps (using OSM data) instead of downloading tiles - this way you can have all the necessary data pre-loaded on the desktop, without the need for a web connection. There are some other benefits:</p>
<ol>
<li>Continuous zoom - you're not restricted to web map zoom levels.</li>
<li>You can change the map styling, what gets rendered etc. interactively.</li>
</ol>
<p>If you're interested, the map control is available for <a href="http://maperitive.net/docs/manual/FAQ.html#Commercial%20use">commercial use</a>, too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jul '12, 11:19</strong></p>
<img src="https://secure.gravatar.com/avatar/591340f954c00c8208d5ffe668f50a05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Breki&#39;s gravatar image" />
<p><span>Breki</span><br />
<span class="score" title="2040 reputation points"><span>2.0k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Breki has 5 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-14063" class="comments-container">
&#10;</div>
<div id="comment-tools-14063" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14063-form-container" class="comment-form-container">
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

