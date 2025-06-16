+++
type = "question"
title = "How to calculate area of polygons in overpass"
description = '''Is there a way to calculate the area of a polygon (i.e. a relation) based on the results I receive from a query? I have a query that finds the &quot;landuse&quot; of the area around a certain radius. I planned to calculate the area of the of each type of landuse that was returned by the API. But I am unable t...'''
date = "2018-11-23T07:44:00Z"
lastmod = "2018-11-30T15:34:00Z"
weight = 66892
keywords = [ "overpassapi", "calculation", "overpass-turbo", "area" ]
aliases = [ "/questions/66892" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to calculate area of polygons in overpass](/questions/66892/how-to-calculate-area-of-polygons-in-overpass)

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
<span id="post-66892-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66892-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66892-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to calculate the area of a polygon (i.e. a relation) based on the results I receive from a query?</p>
<p>I have a query that finds the "landuse" of the area around a certain radius. I planned to calculate the area of the of each type of landuse that was returned by the API. But I am unable to find any resource for something like this.</p>
<p>This is my query: <code>relation(around:600,28.595262,77.240308)["landuse"];</code></p>
<p><img src="/upfiles/overpass_turbo.png" alt="overpass turbo screenshot" /></p>
<p>So how can I calculate those areas, if its possible?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-calculation" rel="tag" title="see questions tagged &#39;calculation&#39;">calculation</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Nov '18, 07:44</strong></p>
<img src="https://secure.gravatar.com/avatar/9af0fae46628599857039aa4e0e0b9c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="imsubkrishd&#39;s gravatar image" />
<p><span>imsubkrishd</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="imsubkrishd has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Nov '18, 14:56</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-66892" class="comments-container">
<span id="66896"></span>
<div id="comment-66896" class="comment">
<div id="post-66896-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Hi. I don't think this is something you can get directly as an output from Overpass. You can run your Overpass query through JOSM or QGIS where it is easy to measure the area once you get your data in.</p>
</div>
<div id="comment-66896-info" class="comment-info">
<span class="comment-age">(24 Nov '18, 08:52)</span> <span class="comment-user userinfo">Privatemajory</span>
</div>
</div>
<span id="66951"></span>
<div id="comment-66951" class="comment">
<div id="post-66951-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is there a way to extract that data given by the plugin? I see values, but I don't see a way to export them.</p>
</div>
<div id="comment-66951-info" class="comment-info">
<span class="comment-age">(28 Nov '18, 08:26)</span> <span class="comment-user userinfo">imsubkrishd</span>
</div>
</div>
<span id="66954"></span>
<div id="comment-66954" class="comment">
<div id="post-66954-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Which plugin? overpass turbo has an export button.</p>
</div>
<div id="comment-66954-info" class="comment-info">
<span class="comment-age">(28 Nov '18, 08:38)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="66956"></span>
<div id="comment-66956" class="comment">
<div id="post-66956-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As <a href="https://help.openstreetmap.org/users/14163/privatemajory">@Privatemajory</a> suggested I ran the query through JOSM using the measurement plugin to get the area of the polygons. I want to extract those values for each polygon that I get as part of my query. Is there a way to do this?</p>
</div>
<div id="comment-66956-info" class="comment-info">
<span class="comment-age">(28 Nov '18, 08:43)</span> <span class="comment-user userinfo">imsubkrishd</span>
</div>
</div>
</div>
<div id="comment-tools-66892" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66892-form-container" class="comment-form-container">
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

<span id="66960"></span>

<div id="answer-container-66960" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66960-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66960-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-66960-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="imsubkrishd has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want to just extract the areas, in JOSM:</p>
<ol>
<li>Make sure utilsplugin2 is enabled. If so, you should have in the main menu <em>Data &gt; Tag multiple objects</em></li>
<li>Download the data with your Overpass query</li>
<li>Select your polygons</li>
<li>Press ctrl+T or go through the menu <em>Data &gt; Tag multiple objects</em></li>
<li>On the table that shows up, you have the objects tags with an <em>area</em> column in the end. You can select all cells (click on one cell then ctrl+A) - or just those you need - copy them and paste them into a spreadsheet.</li>
</ol>
<p>But for a cleaner method and if you want to go further with your data I'd suggest doing things in a GIS software like QGIS (for e.g download the data through QuickOSM and generate the areas as new column).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Nov '18, 11:42</strong></p>
<img src="https://secure.gravatar.com/avatar/15d45a99f101e06c9e79916af33f8336?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Privatemajory&#39;s gravatar image" />
<p><span>Privatemajory</span><br />
<span class="score" title="1125 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Privatemajory has 4 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-66960" class="comments-container">
<span id="66983"></span>
<div id="comment-66983" class="comment">
<div id="post-66983-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have tried both methods and as you suggested the QGIS method is much more cleaner and straightforward. But one thing I want to know is that can I automate this process but creating a Python script? I have multiple points that I want to check for.</p>
</div>
<div id="comment-66983-info" class="comment-info">
<span class="comment-age">(29 Nov '18, 06:52)</span> <span class="comment-user userinfo">imsubkrishd</span>
</div>
</div>
<span id="67010"></span>
<div id="comment-67010" class="comment">
<div id="post-67010-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>QGIS has python and an overpass I/f so it may be possible to do this from within QGIS.</p>
</div>
<div id="comment-67010-info" class="comment-info">
<span class="comment-age">(30 Nov '18, 15:34)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-66960" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66960-form-container" class="comment-form-container">
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

