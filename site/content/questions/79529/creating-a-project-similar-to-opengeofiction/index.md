+++
type = "question"
title = "Creating a project similar to OpenGeofiction"
description = '''I want to set up a site similar to OpenGeofiction. I currently manage a world called Coruia which is a world based in modern times. It has a wiki (but it is private) But no interactive map for me to showcase publicly. I have a local copy of the map stored on my computer if this helps. The project wi...'''
date = "2021-04-04T05:47:00Z"
lastmod = "2021-04-04T12:20:00Z"
weight = 79529
keywords = [ "map", "clone", "fictional", "opengeofiction" ]
aliases = [ "/questions/79529" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Creating a project similar to OpenGeofiction](/questions/79529/creating-a-project-similar-to-opengeofiction)

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
<span id="post-79529-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79529-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79529-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to set up a site similar to OpenGeofiction. I currently manage a world called Coruia which is a world based in modern times. It has a wiki (but it is private) But no interactive map for me to showcase publicly. I have a local copy of the map stored on my computer if this helps.</p>
<p>The project will have the same features as OpenGeofiction.</p>
<p>If it is possible could I use WSL (Windows Subsystem for Linux) to set it up as I am using Windows 10?</p>
<p>Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-clone" rel="tag" title="see questions tagged &#39;clone&#39;">clone</span> <span class="post-tag tag-link-fictional" rel="tag" title="see questions tagged &#39;fictional&#39;">fictional</span> <span class="post-tag tag-link-opengeofiction" rel="tag" title="see questions tagged &#39;opengeofiction&#39;">opengeofiction</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Apr '21, 05:47</strong></p>
<img src="https://secure.gravatar.com/avatar/0c693556e62151ac34c5dc781ccfe107?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ColdFortune&#39;s gravatar image" />
<p><span>ColdFortune</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ColdFortune has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Apr '21, 13:24</strong> </span></p>
</div>
</div>
<div id="comments-container-79529" class="comments-container">
&#10;</div>
<div id="comment-tools-79529" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79529-form-container" class="comment-form-container">
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

<span id="79531"></span>

<div id="answer-container-79531" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79531-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79531-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79531-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you lack the infrastructure and skills to set up and operate the software, as you say, then your question boils down to "is there a project like OpenGeoFiction run by someone else where I can upload my stuff", and the answer to that is, no. Help with setting up the rails port and a tile server will be useless if you have nothing to set it up on, and lack the skills to operate it going forward.</p>
<p>I do not know what format your private map is in. If it is in OpenStreetMap data format then you could potentially use a standalone OpenStreetMap rendering software like Maperitive to load your file, render it into a map, and save it as map tiles. You can then upload these map tiles to a web server and have them displayed with OpenLayers or Leaflet which would give you a slippy map that users can pan and zoom. You can modify the map style in Maperitive to fit your needs. You would have to use an offline editor like JOSM to make edits to your map, and collaborative editing (with more than one user) would be difficult in this scenario - but on the plus side, it requires neither rails port nor tile server, it can all be run on your local computer, even using a non-Linux operating system.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Apr '21, 12:20</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-79531" class="comments-container">
&#10;</div>
<div id="comment-tools-79531" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79531-form-container" class="comment-form-container">
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

