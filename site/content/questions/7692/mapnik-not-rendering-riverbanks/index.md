+++
type = "question"
title = "Mapnik not rendering riverbanks"
description = '''The banks of part of the Chao Phraya River flowing through Bangkok, Thailand are missing from the Mapnik rendering (https://www.openstreetmap.org/?lat=13.6671&amp;amp;lon=100.5497&amp;amp;zoom=13&amp;amp;layers=M ). Map tiles older than August still show the proper rendering and they seem fine in Osmarender. The...'''
date = "2011-09-06T18:47:00Z"
lastmod = "2011-09-07T11:43:00Z"
weight = 7692
keywords = [ "rendering", "riverbank", "mapnik" ]
aliases = [ "/questions/7692" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Mapnik not rendering riverbanks](/questions/7692/mapnik-not-rendering-riverbanks)

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
<span id="post-7692-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7692-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-7692-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The banks of part of the Chao Phraya River flowing through Bangkok, Thailand are missing from the Mapnik rendering (<a href="https://www.openstreetmap.org/?lat=13.6671&amp;lon=100.5497&amp;zoom=13&amp;layers=M">https://www.openstreetmap.org/?lat=13.6671&amp;lon=100.5497&amp;zoom=13&amp;layers=M</a> ). Map tiles older than August still show the proper rendering and they seem fine in Osmarender. The ways/areas are tagged only with waterway=riverbank. What could be causing this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-riverbank" rel="tag" title="see questions tagged &#39;riverbank&#39;">riverbank</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Sep '11, 18:47</strong></p>
<img src="https://secure.gravatar.com/avatar/3e4de1232f3377cc783012d889d0375c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul_012&#39;s gravatar image" />
<p><span>Paul_012</span><br />
<span class="score" title="686 reputation points">686</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul_012 has one accepted answer">33%</span></p>
</div>
</div>
<div id="comments-container-7692" class="comments-container">
<span id="7695"></span>
<div id="comment-7695" class="comment">
<div id="post-7695-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Try adding natural=water</p>
</div>
<div id="comment-7695-info" class="comment-info">
<span class="comment-age">(06 Sep '11, 23:47)</span> <span class="comment-user userinfo">LM_1</span>
</div>
</div>
<span id="7699"></span>
<div id="comment-7699" class="comment">
<div id="post-7699-score" class="comment-score">
3
</div>
<div class="comment-text">
<blockquote>
<p>Try adding natural=water</p>
</blockquote>
<p>natural=water is for lakes. It is incorrect to use it for river banks.</p>
</div>
<div id="comment-7699-info" class="comment-info">
<span class="comment-age">(07 Sep '11, 08:29)</span> <span class="comment-user userinfo">kolen</span>
</div>
</div>
<span id="7702"></span>
<div id="comment-7702" class="comment">
<div id="post-7702-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>rivers are natural water bodies and this is even mentioned on riverbank wiki article <a href="https://wiki.openstreetmap.org/wiki/Tag:waterway%3Driverbank">https://wiki.openstreetmap.org/wiki/Tag:waterway%3Driverbank</a></p>
</div>
<div id="comment-7702-info" class="comment-info">
<span class="comment-age">(07 Sep '11, 10:16)</span> <span class="comment-user userinfo">LM_1</span>
</div>
</div>
<span id="7709"></span>
<div id="comment-7709" class="comment">
<div id="post-7709-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The reason why natural=water would usually not be used is that there is the specific riverbank tag for mapping riverbanks. Riverbanks do render without natural=water on them and the tag does convey more information then natural=water. So natural=water might not be strictly "incorrect" but it is unnecessary and not the usual way to do it.</p>
</div>
<div id="comment-7709-info" class="comment-info">
<span class="comment-age">(07 Sep '11, 11:43)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
</div>
<div id="comment-tools-7692" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7692-form-container" class="comment-form-container">
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

<span id="7696"></span>

<div id="answer-container-7696" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7696-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7696-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-7696-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you look carefully the <a href="https://www.openstreetmap.org/browse/way/23060205">way 23060205</a>, you may notice that the polyline is self-intersecting in the right upper corner. Such geometry errors can disturb software applications trying to convert closed ways to polygons like osm2pgsql/Mapnik. Fix the self-intersecting way and problem should be solved.</p>
<p>Note that <a href="https://wiki.openstreetmap.org/wiki/Quality_Assurance">some quality assurance tools</a> can report such errors.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Sep '11, 00:22</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Sep '11, 10:40</strong> </span></p>
</div>
</div>
<div id="comments-container-7696" class="comments-container">
&#10;</div>
<div id="comment-tools-7696" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7696-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7697"></span>

<div id="answer-container-7697" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7697-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7697-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7697-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are several broken multipolygon relations in that area, though I'm not sure if they would affect rendering of the river.</p>
<p>See for example <a href="https://www.openstreetmap.org/browse/relation/1171990">Relation 1171990</a> and <a href="https://www.openstreetmap.org/browse/relation/1171991">Relation 1171991</a>. Both of these contain several ways which don't make closed areas, plus the parts with role inner are actually outside the polygon. Loading the area in JOSM and running the validator highlights these problems (plus more errors in that area).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Sep '11, 01:18</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-7697" class="comments-container">
&#10;</div>
<div id="comment-tools-7697" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7697-form-container" class="comment-form-container">
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

