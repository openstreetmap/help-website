+++
type = "question"
title = "How to edit OSM maps using JOSM on a local tile server"
description = '''I did everything like eyemax in the question &quot;Set RailsPort and JOSM to use local tile server&quot;, and changed files according to spirea&#x27;s advice. I was able to download maps, edit them and upload. But i have two questions:  http://localhost:3000 doesn&#x27;t show me any maps only grey background, but i kno...'''
date = "2015-10-23T10:01:00Z"
lastmod = "2015-11-03T12:22:00Z"
weight = 46073
keywords = [ "josm", "railsport" ]
aliases = [ "/questions/46073" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to edit OSM maps using JOSM on a local tile server](/questions/46073/how-to-edit-osm-maps-using-josm-on-a-local-tile-server)

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
<span id="post-46073-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46073-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46073-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I did everything like eyemax in the question "<a href="/questions/36946/">Set RailsPort and JOSM to use local tile server</a>", and changed files according to <a href="/questions/36946/set-railsport-and-josm-to-use-local-tile-server/42127">spirea's advice</a>. I was able to download maps, edit them and upload. But i have two questions:</p>
<ol>
<li><a href="http://localhost:3000">http://localhost:3000</a> doesn't show me any maps only grey background, but i know they are changed because i see my changes in changelog. Do i need some styles like CartoCSS, or maybe renderd should do something here?</li>
<li>While downloading maps using JOSM, global maps (a.tile.openstreetmap.org) are visible, and local (localhost) are downloaded, thats weird, how can i force JOSM to show me maps from my server?</li>
</ol>
<p>And another question related to whole idea: I have tile server which uses gis database, nominatim geocoding which uses nominatim database and rails port which uses openstreetmap database. Migrating changes from one database to another is pain in the ass, and not very elegant way.</p>
<p>Are there other ways of editing maps on local server?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-railsport" rel="tag" title="see questions tagged &#39;railsport&#39;">railsport</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Oct '15, 10:01</strong></p>
<img src="https://secure.gravatar.com/avatar/016ab1463a1f9187246270165f1a0a25?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jorax&#39;s gravatar image" />
<p><span>jorax</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jorax has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Oct '15, 19:38</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-46073" class="comments-container">
<span id="46233"></span>
<div id="comment-46233" class="comment">
<div id="post-46233-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>question 1 is not related to JOSM, is it? If it is not, please ask it as a separate question.</p>
</div>
<div id="comment-46233-info" class="comment-info">
<span class="comment-age">(29 Oct '15, 19:32)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="46362"></span>
<div id="comment-46362" class="comment">
<div id="post-46362-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yup its not, it is related to railsport, and tags are for josm and railsport as well. I've managed to fix it however. The URL to tile server was wrong. Solution is here: <a href="/questions/36946/set-railsport-and-josm-to-use-local-tile-">https://help.openstreetmap.org/questions/36946/set-railsport-and-josm-to-use-local-tile-</a></p>
</div>
<div id="comment-46362-info" class="comment-info">
<span class="comment-age">(03 Nov '15, 12:22)</span> <span class="comment-user userinfo">jorax</span>
</div>
</div>
</div>
<div id="comment-tools-46073" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46073-form-container" class="comment-form-container">
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

<span id="46207"></span>

<div id="answer-container-46207" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46207-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46207-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46207-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Ad 2. how to change visible layer in JOSM: use blue '+' button on right border of screen.</p>
<p><img src="/upfiles/Untitled_kHiamIu.png" alt="screenshot of JOSM&#39;s download area selection window" /></p>
<p>Concerning synchronizing databases this is the solution: <a href="https://wiki.openstreetmap.org/wiki/Minutely_Mapnik">https://wiki.openstreetmap.org/wiki/Minutely_Mapnik</a></p>
<p>Basically the idea is to set osmosis to download replication files from given server and then osm2pgsql should upload those changes to gis. But i use both manually through terminal.</p>
<p>How can I execute them automatically?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Oct '15, 08:42</strong></p>
<img src="https://secure.gravatar.com/avatar/016ab1463a1f9187246270165f1a0a25?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jorax&#39;s gravatar image" />
<p><span>jorax</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jorax has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Oct '15, 19:03</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-46207" class="comments-container">
&#10;</div>
<div id="comment-tools-46207" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46207-form-container" class="comment-form-container">
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

