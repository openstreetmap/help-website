+++
type = "question"
title = "HOW TO download a &quot;large area&quot; and use it in JOSM ??"
description = '''I&#x27;m discovering OpenMap and related applications.. So, I&#x27;m trying to download a big part of Chicago in order to edit the map (with JOSM, or other, i&#x27;m open to every proposal). The objective is having a real Chicago map that I could use in a Role Playing Game (Fallout). Because we are many years afte...'''
date = "2011-01-13T18:25:00Z"
lastmod = "2011-05-27T09:29:00Z"
weight = 2178
keywords = [ "download", "edit", "how-to", "josm" ]
aliases = [ "/questions/2178" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [HOW TO download a "large area" and use it in JOSM ??](/questions/2178/how-to-download-a-large-area-and-use-it-in-josm)

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
<span id="post-2178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2178-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-2178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm discovering OpenMap and related applications..</p>
<p>So, I'm trying to download a big part of Chicago in order to edit the map <em>(with JOSM, or other, i'm open to every proposal).</em><br />
The objective is having a real Chicago map that I could use in a Role Playing Game (Fallout).<br />
Because we are many years after a Nuclear War, in a real city, I'd like to edit that map to make it match with the intersets of the game <em>(rename some places, blocking some road acces or bridges, put scenaristics POI, etc..)</em></p>
<p>My problem?</p>
<p>I just don't understand how to download a map!!!<br />
Seriously, I tried to download from OpenMap and from OSM serveur with JOSM, but it just doesn't work. I can download a map but I can't use it, or I just can't download because of the size<br />
I probably missed something.</p>
<p>Thanx for help, SkaL</p>
<p>(edit : does anybody knows about Gosmore?? gonna try this.. )</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-edit" rel="tag" title="see questions tagged &#39;edit&#39;">edit</span> <span class="post-tag tag-link-how-to" rel="tag" title="see questions tagged &#39;how-to&#39;">how-to</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jan '11, 18:25</strong></p>
<img src="https://secure.gravatar.com/avatar/378ab582f2eecfcee4a67c0546a71d0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SkaL&#39;s gravatar image" />
<p><span>SkaL</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SkaL has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jan '11, 19:01</strong> </span></p>
</div>
</div>
<div id="comments-container-2178" class="comments-container">
&#10;</div>
<div id="comment-tools-2178" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2178-form-container" class="comment-form-container">
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

<span id="5408"></span>

<div id="answer-container-5408" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5408-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5408-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-5408-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://download.geofabrik.de/osm/">http://download.geofabrik.de/osm/</a> is a good source for planet.osm extracts. Basically you are downloading the osm data for a large region of the planet so you will want to look through the folders and find the smallest area which will contain Chicago, there are state sized regions.</p>
<p>I would recommend picking the bzip version to download since this is an xml format which every openstreetmap tool can use.</p>
<p>Now you have a large area of osm data which is too big, so you can use a tool called osmosis to cut out a square. You can find <a href="http://wiki.openstreetmap.org/wiki/Osmosis#Extracting_bounding_boxes">instructions on the wiki</a>. (You can use the export tab to get the bounding box coordinates).</p>
<p>After that you should have a .osm file covering chicago. I just tested josm with an 80mb extract (Cambridgeshire in the UK, which is probably a bit larger than Chicago), it does slow down a bit but once you zoom in it seems to work reasonably, it used almost 700mb of memory.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 May '11, 09:29</strong></p>
<img src="https://secure.gravatar.com/avatar/7bb4d30bb6d40cf9b3644ff4f453e5bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="quantumstate&#39;s gravatar image" />
<p><span>quantumstate</span><br />
<span class="score" title="455 reputation points">455</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="quantumstate has 3 accepted answers">30%</span> </br></br></p>
</div>
</div>
<div id="comments-container-5408" class="comments-container">
&#10;</div>
<div id="comment-tools-5408" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5408-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2179"></span>

<div id="answer-container-2179" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2179-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-2179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First of all, you must be aware that what you will be downloading, or editing in your editor, is raw data, not "a map". You will have a line tagged as "this is a road", another line tagged as "this is a building", but it is not a WYSIWYG editor. After you are done editing, you will have to create a map from your data, a process we call rendering. You will be using a different piece of software for that (Maperitive, Mapnik, Osmarender, Mapgen.pl or something).</p>
<p>Now you didn't say why downloading with JOSM didn't work for you. My suspicion is that you might have tried to download a too large area. Try a city block first, to see if it works in principle. If it is really the size limit that is your problem, you will either have to use the <a href="http://wiki.openstreetmap.org/wiki/Xapi">XAPI</a> service (which is reportedly a bit flaky at the moment), or you should download a suitable <a href="http://wiki.openstreetmap.org/wiki/Planet.osm">Planet.osm extract</a> and cut out your area of interest with a suitable program like <a href="http://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jan '11, 18:48</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-2179" class="comments-container">
&#10;</div>
<div id="comment-tools-2179" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2179-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2222"></span>

<div id="answer-container-2222" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2222-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2222-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-2222-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>wow...</p>
<p>a lot of info for just a question...! Thank you very much ;)</p>
<p>But if I' understand correctly : JOSM is not build to modify existing map (make "another" chicago for eg) by drawing.. I can modify "raw data" (i guess raw is all those little things that makes a map.. roads, parks, bulding, lake, scale,...) with JOSM but I guess I need to know how works raw data...</p>
<p>And you are right, my problem is mostly about the data size I try to DL.. I've downloaded many large areas (heavy files) on Windows (NaviMapper) with no issues.. just a long wait ! This is why it seems weird to me that I cannot DL such as areas with the solutions I've find by my own.</p>
<p>About XAPI and/or Planet.osm... i don't understand how it works... either what it is :) ! Open Map advised me to use Planet.OSM.. i just found a repertory with many files and I don't know what to with them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jan '11, 22:31</strong></p>
<img src="https://secure.gravatar.com/avatar/378ab582f2eecfcee4a67c0546a71d0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SkaL&#39;s gravatar image" />
<p><span>SkaL</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SkaL has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-2222" class="comments-container">
&#10;</div>
<div id="comment-tools-2222" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2222-form-container" class="comment-form-container">
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

