+++
type = "question"
title = "Is there a map using live data?"
description = '''I&#x27;ve noticed that there is a delay with Mapnik on the OpenStreetMap website and also that it doesn&#x27;t always actually re-render tiles. I&#x27;ve already run into a number of spots where a few hours later I had to tell it the tile was dirty to get it to re-render. Is there a OpenStreetMap based map applica...'''
date = "2014-11-01T13:14:00Z"
lastmod = "2014-11-01T13:34:00Z"
weight = 38229
keywords = [ "live", "data", "mapnik" ]
aliases = [ "/questions/38229" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Is there a map using live data?](/questions/38229/is-there-a-map-using-live-data)

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
<span id="post-38229-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38229-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38229-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've noticed that there is a delay with Mapnik on the OpenStreetMap website and also that it doesn't always actually re-render tiles. I've already run into a number of spots where a few hours later I had to tell it the tile was dirty to get it to re-render.</p>
<p>Is there a OpenStreetMap based map application that displays live data from OpenStreetMap's database in a Mapnik style aesthetic? I know that any of the editors will use live data, but I just want to be able to survey the work that I've done every now and then to look for mistakes, things I missed, or things that just don't look quite right.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-live" rel="tag" title="see questions tagged &#39;live&#39;">live</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Nov '14, 13:14</strong></p>
<img src="https://secure.gravatar.com/avatar/f0a0bbd14f78f8e0a40873cc6c769c33?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zellfaze&#39;s gravatar image" />
<p><span>zellfaze</span><br />
<span class="score" title="141 reputation points">141</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zellfaze has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38229" class="comments-container">
<span id="38230"></span>
<div id="comment-38230" class="comment">
<div id="post-38230-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also worth noting that I know that Mapnik is supposed to re-render every minute. It just doesn't always, so I am looking for an alternative to it.</p>
</div>
<div id="comment-38230-info" class="comment-info">
<span class="comment-age">(01 Nov '14, 13:15)</span> <span class="comment-user userinfo">zellfaze</span>
</div>
</div>
</div>
<div id="comment-tools-38229" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38229-form-container" class="comment-form-container">
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

<span id="38232"></span>

<div id="answer-container-38232" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38232-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38232-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-38232-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="zellfaze has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>"Mapnik" is just a piece of software; how fast or slowly it runs depends entirely on the environment that it runs in. OpenStreetMap's "standard" tiles have been slower than normal recently for a couple of reasons - a recent style update, and previous to that a problem with a disk on one of the servers.</p>
<p>It's worth bearing in mind that there are 4 sets of tiles available on OpenStreetMap.org - you may find that another set is updated before the "standard" ones are. If that doesn't work, the simplest answer is probably just to select the data layer - if you've moved something, that's the easiest way of seeing where you've moved it to.</p>
<p>Another option is to <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">set up your own tile server</a>. Depending on size of the area that you're interested in and the hardware you have available, you may find that your own rendering server is actually significantly faster than osm.org's "standard" tiles. I find that a virtual machine using only some of the resources of a desktop PC is able to render tiles faster in the (small**) area that I'm interested in, mainly because there's only one person requesting tiles (me). You can even, with a bit of browser externsion magic, make your tiles appear to you on <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Your_tiles_from_osm.org">osm.org</a>.</p>
<p>** essentially England and Wales between southwestern South Wales and northeastern North Yorkshire</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '14, 13:34</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-38232" class="comments-container">
&#10;</div>
<div id="comment-tools-38232" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38232-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="38231"></span>

<div id="answer-container-38231" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38231-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38231-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-38231-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No, there is no such map that is publicly accessible. It is relatively simple to set one up however, by forgoing tile caching altogether and re-calculating each tile every time it is viewed. Offering that publicly however would very quickly bring down even the fastest server.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '14, 13:32</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-38231" class="comments-container">
&#10;</div>
<div id="comment-tools-38231" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38231-form-container" class="comment-form-container">
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

