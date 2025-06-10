+++
type = "question"
title = "Fetch Mapnik or Osmarender Image given bounding box"
description = '''Hi, I want to get the mapnik image or osmarender image given the bounding box, just like the export feature of openstreetmaps. I have an application that should automatically fetch that image given the box coordinates. Is that possible? How? If not, any suggestions? Thank you for reading, and of cou...'''
date = "2011-07-30T08:26:00Z"
lastmod = "2011-07-30T12:11:00Z"
weight = 6710
keywords = [ "development", "export", "osmarender", "mapnik" ]
aliases = [ "/questions/6710" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Fetch Mapnik or Osmarender Image given bounding box](/questions/6710/fetch-mapnik-or-osmarender-image-given-bounding-box)

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
<span id="post-6710-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6710-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-6710-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I want to get the mapnik image or osmarender image given the bounding box, just like the export feature of openstreetmaps. I have an application that should automatically fetch that image given the box coordinates.</p>
<p>Is that possible? How? If not, any suggestions?</p>
<p>Thank you for reading, and of course answering my question. :D</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-osmarender" rel="tag" title="see questions tagged &#39;osmarender&#39;">osmarender</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jul '11, 08:26</strong></p>
<img src="https://secure.gravatar.com/avatar/09c53c06e6f8073f66b588f3257dbd56?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jplaras&#39;s gravatar image" />
<p><span>jplaras</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jplaras has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-6710" class="comments-container">
&#10;</div>
<div id="comment-tools-6710" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6710-form-container" class="comment-form-container">
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

<span id="6715"></span>

<div id="answer-container-6715" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6715-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-6715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jplaras has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Getting a Mapnik image from the export tab means that the image has to be prepared from raw data especially for you; this is relatively expensive in terms of computing time and it is therefore not allowed to use that in any automated fashion.</p>
<p>Check out the Wiki page <a href="http://wiki.openstreetmap.org/wiki/Static_map_images">Static map images</a> for possible solutions to your problem. Many of the services listed there use pre-rendered tiles to create the map image and thus cause less load on the servers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jul '11, 10:11</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-6715" class="comments-container">
&#10;</div>
<div id="comment-tools-6715" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6715-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="6716"></span>

<div id="answer-container-6716" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6716-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6716-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-6716-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For example the <a href="http://openstreetmap.gryph.de/bigmap.cgi">bigmap script</a> allows you to get images of any size which are assembled from the standard tiles thereby not requiring extra rendering.</p>
<p>Otherwise you would have to install your own rendering chain to render these maps on demand (with the advantage that you can apply any changes to the style hence controlling what and how is displayed). There are tools which create maps of custom size like <a href="http://wiki.openstreetmap.org/wiki/Mapnik_Example">nik2img.py</a> for mapnik. Alternatives could be <a href="http://wiki.openstreetmap.org/wiki/Osmarender/Howto">osmarender</a>, <a href="http://wiki.openstreetmap.org/wiki/Maperitive">maperitive</a> or the recently released <a href="http://wiki.openstreetmap.org/wiki/Mapweaver">mapweaver</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jul '11, 12:11</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
</div>
<div id="comments-container-6716" class="comments-container">
&#10;</div>
<div id="comment-tools-6716" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6716-form-container" class="comment-form-container">
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

