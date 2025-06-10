+++
type = "question"
title = "Maidenhead Locator"
description = '''Does OSM include the Maidenhead locator system anywhere? It is basically a n approximation to Lat/Long: https://en.wikipedia.org/wiki/Maidenhead_Locator_System If not, might it be added? It would publicise OSM to a world-wide community (radio amateurs) who have GPS gadgets &amp;amp; technical capability...'''
date = "2015-06-19T18:56:00Z"
lastmod = "2015-06-20T16:37:00Z"
weight = 43653
keywords = [ "latitude", "locator", "maidenhead", "longitude", "qra" ]
aliases = [ "/questions/43653" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Maidenhead Locator](/questions/43653/maidenhead-locator)

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
<span id="post-43653-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43653-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43653-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Does OSM include the Maidenhead locator system anywhere? It is basically a n approximation to Lat/Long: <a href="https://en.wikipedia.org/wiki/Maidenhead_Locator_System">https://en.wikipedia.org/wiki/Maidenhead_Locator_System</a></p>
<p>If not, might it be added? It would publicise OSM to a world-wide community (radio amateurs) who have GPS gadgets &amp; technical capability.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-latitude" rel="tag" title="see questions tagged &#39;latitude&#39;">latitude</span> <span class="post-tag tag-link-locator" rel="tag" title="see questions tagged &#39;locator&#39;">locator</span> <span class="post-tag tag-link-maidenhead" rel="tag" title="see questions tagged &#39;maidenhead&#39;">maidenhead</span> <span class="post-tag tag-link-longitude" rel="tag" title="see questions tagged &#39;longitude&#39;">longitude</span> <span class="post-tag tag-link-qra" rel="tag" title="see questions tagged &#39;qra&#39;">qra</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jun '15, 18:56</strong></p>
<img src="https://secure.gravatar.com/avatar/22127c793f2bd130848cb89f7b55871f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wickerwatter&#39;s gravatar image" />
<p><span>wickerwatter</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wickerwatter has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43653" class="comments-container">
&#10;</div>
<div id="comment-tools-43653" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43653-form-container" class="comment-form-container">
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

<span id="43661"></span>

<div id="answer-container-43661" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43661-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43661-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-43661-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Maidenhead Locator system is another co-ordinate system (it is for instance available on my Garmin). OSM uses WGS84 internally, and Spherical Mercator (EPSG:3857) for slippy maps. It is perfectly possible to transform OSM data to other co-ordinate systems using tools such as ogr2ogr or osm2pgsql. However, the Maidenhead system appears to encode WGS84 lat/lon in an alphanumeric code which is not compatible with these programs.</p>
<p>If OSM wants strong publicity it is in non-technical communities. OSM is very strong in people with a technical background, many of us see this as possible deterrent to people without such a background joining us. I therefore doubt that there is interest in work to make OSM look more techy than it already is.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jun '15, 11:51</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jun '15, 16:40</strong> </span></p>
</div>
</div>
<div id="comments-container-43661" class="comments-container">
&#10;</div>
<div id="comment-tools-43661" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43661-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43666"></span>

<div id="answer-container-43666" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43666-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43666-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-43666-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't know much about the Maidenhead system, but wikipedia tells me that it appears to be another way to write down lat/lon locations, right? When it comes to storing locations, the OSM database just uses regular latitude and longitude.</p>
<p>However there's nothing stopping you (or anyone) from somehow building a map that uses OSM and does something with Maidenhead locations. What exactly did you have in mind by "adding Maidenhead"?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jun '15, 16:37</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jun '15, 08:12</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-43666" class="comments-container">
&#10;</div>
<div id="comment-tools-43666" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43666-form-container" class="comment-form-container">
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

