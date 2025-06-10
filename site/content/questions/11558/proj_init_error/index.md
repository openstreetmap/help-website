+++
type = "question"
title = "proj_init_error"
description = '''Hey guys!  When rendering from PostgreSQL/PostGIS database by Python/Mapnik  I receice the following ERROR:  proj_init_error:failed to initialize projection with: &#x27;+init=epsg:4326&#x27;  I took the steps like in http://switch2osm.org/serving-tiles/manually-building-a-tile-server/ My OS is Windows. I impo...'''
date = "2012-03-28T14:50:00Z"
lastmod = "2012-12-18T22:38:00Z"
weight = 11558
keywords = [ "rendering", "projection", "mapnik", "database" ]
aliases = [ "/questions/11558" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [proj_init_error](/questions/11558/proj_init_error)

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
<span id="post-11558-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11558-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11558-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey guys! When rendering from PostgreSQL/PostGIS database by Python/Mapnik I receice the following ERROR:</p>
<pre><code>proj_init_error:failed to initialize projection with: &#39;+init=epsg:4326&#39;</code></pre>
<p>I took the steps like in <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server/">http://switch2osm.org/serving-tiles/manually-building-a-tile-server/</a></p>
<p>My OS is Windows.</p>
<p>I imported my africa.osm by osm2pgsql to my database.</p>
<p>Is it possible, that the whole thing only works with the whole planet_latest.osm?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-projection" rel="tag" title="see questions tagged &#39;projection&#39;">projection</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Mar '12, 14:50</strong></p>
<img src="https://secure.gravatar.com/avatar/cc0198a02af3c41ad04b61e028c3b126?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MHein&#39;s gravatar image" />
<p><span>MHein</span><br />
<span class="score" title="141 reputation points">141</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MHein has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11558" class="comments-container">
&#10;</div>
<div id="comment-tools-11558" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11558-form-container" class="comment-form-container">
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

<span id="11647"></span>

<div id="answer-container-11647" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11647-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11647-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-11647-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi,</p>
<p>Did you install the proj library? Usually you get this kind of error if the library cannot be found by programs. If you're not using a package like OSGeo4W, you need to set the environment variables correctly.</p>
<p>From the Windows proj4 README.txt:<br />
PATH=%PATH%;C:\PROJ\BIN<br />
PROJ_LIB=C:\Software\PROJ\NAD</p>
<p>The mapnik installation guide for windows also mentions the proj4 library if you're planning on using epsg codes</p>
<p>HTH Frank</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Mar '12, 15:46</strong></p>
<img src="https://secure.gravatar.com/avatar/30b87850d86c99d1c4f1f72c9abaeb52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frabron&#39;s gravatar image" />
<p><span>frabron</span><br />
<span class="score" title="361 reputation points">361</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frabron has 2 accepted answers">16%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Mar '12, 17:21</strong> </span></p>
</div>
</div>
<div id="comments-container-11647" class="comments-container">
<span id="11648"></span>
<div id="comment-11648" class="comment">
<div id="post-11648-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm guessing that there should be some backslashes in that?</p>
</div>
<div id="comment-11648-info" class="comment-info">
<span class="comment-age">(30 Mar '12, 16:10)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="11652"></span>
<div id="comment-11652" class="comment">
<div id="post-11652-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Um, yes, of course. I saw them in the editor preview, but the actual view somehow ate them. I escaped them now ...</p>
</div>
<div id="comment-11652-info" class="comment-info">
<span class="comment-age">(30 Mar '12, 17:22)</span> <span class="comment-user userinfo">frabron</span>
</div>
</div>
<span id="12858"></span>
<div id="comment-12858" class="comment">
<div id="post-12858-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thx.. got bored looking at blank maps</p>
</div>
<div id="comment-12858-info" class="comment-info">
<span class="comment-age">(22 May '12, 08:24)</span> <span class="comment-user userinfo">ronzulu</span>
</div>
</div>
</div>
<div id="comment-tools-11647" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11647-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="18578"></span>

<div id="answer-container-18578" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18578-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18578-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-18578-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>@frabon is right in that this error is related to mapnik not seeing the Proj4 libraries.</p>
<p>I was able to fix this problem by creating an Environment Variable, <code>PROJ_LIB</code>, and pointing it to my GDAL installation's grid shift files. On my system it's <code>C:\Program Files\GDAL\projlib</code>.</p>
<p>I thought using the GDAL proj stuff was better than creating a redundant install. Of course, since I'm using true-blue WinXP32, I still needed to logout/login or reboot to apply the change. It definitely did the trick, though.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Dec '12, 22:38</strong></p>
<img src="https://secure.gravatar.com/avatar/0bda1cf1a41b6d91ad2f3c5a88d059a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="elrobis&#39;s gravatar image" />
<p><span>elrobis</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="elrobis has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18578" class="comments-container">
&#10;</div>
<div id="comment-tools-18578" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18578-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11645"></span>

<div id="answer-container-11645" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11645-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11645-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11645-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not sure about your problem, maybe you have to load the projection strings into your db (see Postgis docu for this). For your second question: I can confirm that osm2pgsql as well as the rest of the rendering stack works also with extracts, no need to use the whole planet.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Mar '12, 14:52</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
</div>
<div id="comments-container-11645" class="comments-container">
&#10;</div>
<div id="comment-tools-11645" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11645-form-container" class="comment-form-container">
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

