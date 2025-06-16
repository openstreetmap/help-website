+++
type = "question"
title = "Problem hidding a maritime border with mapnik"
description = '''Hi, I&#x27;m new to osm and mapnik, i finally found a way to hide the borders tagged as maritime through mapnik but there is a border, also tagged as maritime on which my rules are not applied. Only belgium data are imported but a border of Netherlands is showing on the map: Click here for screenshot You...'''
date = "2014-06-16T13:26:00Z"
lastmod = "2014-11-12T10:55:00Z"
weight = 34000
keywords = [ "border", "maritime", "mapnik" ]
aliases = [ "/questions/34000" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Problem hidding a maritime border with mapnik](/questions/34000/problem-hidding-a-maritime-border-with-mapnik)

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
<span id="post-34000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34000-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-34000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm new to osm and mapnik, i finally found a way to hide the borders tagged as maritime through mapnik but there is a border, also tagged as maritime on which my rules are not applied.</p>
<p>Only belgium data are imported but a border of Netherlands is showing on the map: <a href="https://dl.dropboxusercontent.com/u/23590261/mapnik-maritime-border.png">Click here for screenshot</a></p>
<p>You can see that the maritime borders of Belgium are correctly hidden but there is one remaining in front of the Netherlands. The data were downloaded this morning from geofabrik. If you follow <a href="https://www.openstreetmap.org/edit#map=16/51.8667/3.4583">this link</a> you can see how that border is tagged, it has admin_level=2 and maritime=yes.</p>
<p>Can anyone explain why my rules are not applied on that border? And why it is in the Belgium data extract whereas it's related to the Netherlands?</p>
<p>Here is my mapnik config from <a href="https://dl.dropboxusercontent.com/u/23590261/layer-admin.xml.inc">layer-admin.xml.inc from dropbox</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-border" rel="tag" title="see questions tagged &#39;border&#39;">border</span> <span class="post-tag tag-link-maritime" rel="tag" title="see questions tagged &#39;maritime&#39;">maritime</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jun '14, 13:26</strong></p>
<img src="https://secure.gravatar.com/avatar/b44013ba375d2dabc6fdcbd7a9a3cd6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="QuentP&#39;s gravatar image" />
<p><span>QuentP</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="QuentP has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jun '14, 13:28</strong> </span></p>
</div>
</div>
<div id="comments-container-34000" class="comments-container">
<span id="38424"></span>
<div id="comment-38424" class="comment">
<div id="post-38424-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Me too having having same problem. i followed the instruction given in <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/">http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/</a> in planet_osm_roads i cant find any attributes with name maritime. in planet_osm_line i have find only few row for condition "boundary" = 'maritime'</p>
<p>Can u explain how did u import the data to postgres ?</p>
</div>
<div id="comment-38424-info" class="comment-info">
<span class="comment-age">(10 Nov '14, 11:31)</span> <span class="comment-user userinfo">Arun kmp</span>
</div>
</div>
<span id="38492"></span>
<div id="comment-38492" class="comment">
<div id="post-38492-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I simply followed this : <a href="https://wiki.openstreetmap.org/wiki/PostGIS">https://wiki.openstreetmap.org/wiki/PostGIS</a></p>
</div>
<div id="comment-38492-info" class="comment-info">
<span class="comment-age">(12 Nov '14, 08:26)</span> <span class="comment-user userinfo">QuentP</span>
</div>
</div>
</div>
<div id="comment-tools-34000" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34000-form-container" class="comment-form-container">
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

<span id="38497"></span>

<div id="answer-container-38497" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38497-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-38497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>At a very rough guess I'd suggest looking at the relations which include that way. You could try a PostGIS query to find which linestrings in your database intersect this area, and examine their tags.</p>
<p>Personally I have chosen to change the ordering of my rendering thus:</p>
<ol>
<li>(bottom) Land</li>
<li>Borders</li>
<li>(top) Sea</li>
</ol>
<p>such that the sea always appears above these accursed fugly maritime boundaries.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Nov '14, 10:55</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Nov '14, 10:55</strong> </span></p>
</div>
</div>
<div id="comments-container-38497" class="comments-container">
&#10;</div>
<div id="comment-tools-38497" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38497-form-container" class="comment-form-container">
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

