+++
type = "question"
title = "SVG map with markers"
description = '''Hi, I’m preparing some city maps for a travel guide book, and I need to add markers (arrows, circles, numbers) for sights. Since the map clip and the lists of sights are always changing, I’d like to automate that task, i.e. read the locations from a spreadsheet and put markers on the map with a Pyth...'''
date = "2015-07-28T08:38:00Z"
lastmod = "2015-07-29T05:06:00Z"
weight = 44463
keywords = [ "marker", "maperitive", "osm" ]
aliases = [ "/questions/44463" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [SVG map with markers](/questions/44463/svg-map-with-markers)

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
<span id="post-44463-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44463-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-44463-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I’m preparing some city maps for a travel guide book, and I need to add markers (arrows, circles, numbers) for sights. Since the map clip and the lists of sights are always changing, I’d like to automate that task, i.e. read the locations from a spreadsheet and put markers on the map with a Python script. I’m as far as converting OSM to SVG with Maperitive and to PDF with Inkscape, that works well.</p>
<p>As far as I understand, it’s not possible to add elements in Maperitive, only style what’s in the OSM data. Or is there a way, maybe via GPX?</p>
<p>So I should probably try to modify the SVG via Inkscape’s API? Do you know any examples for that? (Of course I’ll gladly provide mine, if I accomplish the task.) I also don’t understand how to "convert" from geo location coordinates to SVG coordinates. Any hints?</p>
<p>Thanks in advance! Hraban</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-maperitive" rel="tag" title="see questions tagged &#39;maperitive&#39;">maperitive</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jul '15, 08:38</strong></p>
<img src="https://secure.gravatar.com/avatar/5a39f1335b6eff433673ed987859fb24?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hraban&#39;s gravatar image" />
<p><span>Hraban</span><br />
<span class="score" title="186 reputation points">186</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hraban has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jul '15, 05:07</strong> </span></p>
</div>
</div>
<div id="comments-container-44463" class="comments-container">
&#10;</div>
<div id="comment-tools-44463" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44463-form-container" class="comment-form-container">
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

<span id="44470"></span>

<div id="answer-container-44470" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44470-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44470-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-44470-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Hraban has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think you can use more than one OSM file with Maperitive. There is no reason why you should not convert your markers to OSM style XML and create specific rules in Maperitive to style this data. Just make sure you don't upload this file to OSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jul '15, 14:27</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-44470" class="comments-container">
<span id="44493"></span>
<div id="comment-44493" class="comment">
<div id="post-44493-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, I got a similar answer in Maperitive’s Google Group, and it works for me. I didn’t think of OSM as a simple format that I can write myself.</p>
<p>I’d still like to understand the conversion of geographical map coordinates to geometrical SVG coordinates, but will open a new thread for that.</p>
</div>
<div id="comment-44493-info" class="comment-info">
<span class="comment-age">(29 Jul '15, 05:06)</span> <span class="comment-user userinfo">Hraban</span>
</div>
</div>
</div>
<div id="comment-tools-44470" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44470-form-container" class="comment-form-container">
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

