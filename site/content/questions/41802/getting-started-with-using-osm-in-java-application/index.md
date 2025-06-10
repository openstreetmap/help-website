+++
type = "question"
title = "Getting started with using OSM in Java Application"
description = '''Hey Guys I hope I got the right forum and all! I want to program a small application for my motorcycle. The goal is to have a mapview which displays the current position. It shall run on linux on a raspberry pi, but this goal is far away;) In a further step, it would be nice to have routing and trac...'''
date = "2015-03-19T22:43:00Z"
lastmod = "2015-07-02T15:54:00Z"
weight = 41802
keywords = [ "development", "java" ]
aliases = [ "/questions/41802" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Getting started with using OSM in Java Application](/questions/41802/getting-started-with-using-osm-in-java-application)

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
<span id="post-41802-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41802-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41802-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey Guys</p>
<p>I hope I got the right forum and all!</p>
<p>I want to program a small application for my motorcycle. The goal is to have a mapview which displays the current position. It shall run on linux on a raspberry pi, but this goal is far away;) In a further step, it would be nice to have routing and tracking functionalities, but for the start I am stuck with displaying a map.</p>
<p>I do not have problems with java programming and am somewhat experienced, I only have problems with the map-stuff.</p>
<p>I started with trying to get mapsforge running in a java project but figured out, that it is just too complicated, because it is intended for use with android.</p>
<p>Unfortunately I have to admit that the whole project is not particularly well documented. Many of the related libraries and projects do not have nice getting started sites or things like that. so it is really hard to orientate and know where to start...</p>
<p>So, my easy question: When I want to display an (interactive) map in java. And later I want to add routing functionalities (so it would be nescesary to colour the active street and such things), what would be a good starting point for a library for use with java?</p>
<p>Regards Me</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Mar '15, 22:43</strong></p>
<img src="https://secure.gravatar.com/avatar/e0484132810de5d633453570c2b67c4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="itsmeagain&#39;s gravatar image" />
<p><span>itsmeagain</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="itsmeagain has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Mar '15, 23:20</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-41802" class="comments-container">
&#10;</div>
<div id="comment-tools-41802" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41802-form-container" class="comment-form-container">
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

<span id="41809"></span>

<div id="answer-container-41809" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41809-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41809-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-41809-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://wiki.openstreetmap.org/wiki/JMapViewer">JMapViewer</a> might be a starting point. Unlike Mapsforge though, this is based on bitmap tiles, i.e. you can't download a large map for offline use, instead it loads individual map tiles (PNGs) from the server as needed. Also JMapViewer has limited options of displaying vector data on top of the map, AFAIK it only supports markers (not highlighted streets etc) but that is something that you could probably add given some Java knowledge.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Mar '15, 07:26</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-41809" class="comments-container">
<span id="43915"></span>
<div id="comment-43915" class="comment">
<div id="post-43915-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Does any of you know how is possible to download a bigger area? Always when i am trying to do this it says that the data includes too many information.</p>
</div>
<div id="comment-43915-info" class="comment-info">
<span class="comment-age">(02 Jul '15, 11:14)</span> <span class="comment-user userinfo">madalina_ias...</span>
</div>
</div>
<span id="43916"></span>
<div id="comment-43916" class="comment">
<div id="post-43916-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/11170/madalina_iasmina">@madalina_iasmina</a> It is not clear what you mean. Try asking a new question with more words explaining what you are trying to do. You can ask in whatever language you want</p>
<p>(guessing)</p>
<p>Nu este clar ce vrei să spui. Încercați pune o nouă întrebare cu mai multe cuvinte explica ceea ce încercăm să facem. Puteți solicita în orice limbă doriți</p>
</div>
<div id="comment-43916-info" class="comment-info">
<span class="comment-age">(02 Jul '15, 11:18)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="43919"></span>
<div id="comment-43919" class="comment">
<div id="post-43919-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As vrea sa pot incarca intregul oras in Java OpenSteetMap, dar de fiecare data cand incerc sa fac asta imi spune ca suprafata este prea mare si trebuie sa reduc din ea. In momentul in care aleg o suprafata mai mica functioneaza, dar as preafera sa pot avea tot orasul .</p>
</div>
<div id="comment-43919-info" class="comment-info">
<span class="comment-age">(02 Jul '15, 15:54)</span> <span class="comment-user userinfo">madalina_ias...</span>
</div>
</div>
</div>
<div id="comment-tools-41809" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41809-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="41859"></span>

<div id="answer-container-41859" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41859-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41859-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-41859-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at <a href="http://wiki.openstreetmap.org/wiki/Atlas_(navigation_application)">Atlas</a> ... it is written in Java for desktop PC and is based on mapsforge.</p>
<p>Unfortunately it is closed source by user emux (see github about mapsforge, he is one of the core developers of mapsforge)</p>
<p>But maybe he can give you the right entry point in the mapsforge mailing list how to get started more easily with mapsforge in Java / PC. Read the mailing list before, maybe there has been already a similar question.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Mar '15, 15:57</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-41859" class="comments-container">
&#10;</div>
<div id="comment-tools-41859" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41859-form-container" class="comment-form-container">
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

