+++
type = "question"
title = "Running renderd for the first time ubuntu18.04"
description = '''Mapnik LOG&amp;gt; 2020-07-22 22:14:57: warning: unable to find face-name &#x27;HanaMinB Regular&#x27; in FontSet &#x27;fontset-2&#x27; Mapnik LOG&amp;gt; 2020-07-22 22:14:57: warning: unable to find face-name &#x27;unifont Medium&#x27; in FontSet &#x27;fontset-2&#x27; renderd[23757]: An error occurred while loading the map layer &#x27;ajt&#x27;: Postgis P...'''
date = "2020-07-23T02:38:00Z"
lastmod = "2020-07-24T06:48:00Z"
weight = 75855
keywords = [ "building", "tile", "renderd", "server" ]
aliases = [ "/questions/75855" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Running renderd for the first time ubuntu18.04](/questions/75855/running-renderd-for-the-first-time-ubuntu1804)

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
<span id="post-75855-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75855-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-75855-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<pre><code>Mapnik LOG&gt; 2020-07-22 22:14:57: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2020-07-22 22:14:57: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-2&#39;
renderd[23757]: An error occurred while loading the map layer &#39;ajt&#39;: Postgis Plugin: ERROR:  relation &quot;icesheet_polygons&quot; does not exist
LINE 1: SELECT ST_SRID(&quot;way&quot;) AS srid FROM icesheet_polygons WHERE &quot;...
                                           ^
in executeQuery Full sql was: &#39;SELECT ST_SRID(&quot;way&quot;) AS srid FROM icesheet_polygons WHERE &quot;way&quot; IS NOT NULL LIMIT 1;&#39;
  encountered during parsing of layer &#39;icesheet-poly&#39; in Layer at line 5895 of &#39;/home/xj/src/openstreetmap-carto/mapnik.xml&#39;
renderd[23757]: An error occurred while loading the map layer &#39;ajt&#39;: Postgis Plugin: ERROR:  relation &quot;icesheet_polygons&quot; does not exist
LINE 1: SELECT ST_SRID(&quot;way&quot;) AS srid FROM icesheet_polygons WHERE &quot;...
                                           ^
in executeQuery Full sql was: &#39;SELECT ST_SRID(&quot;way&quot;) AS srid FROM icesheet_polygons WHERE &quot;way&quot; IS NOT NULL LIMIT 1;&#39;
  encountered during parsing of layer &#39;icesheet-poly&#39; in Layer at line 5895 of &#39;/home/xj/src/openstreetmap-carto/mapnik.xml&#39;
renderd[23757]: An error occurred while loading the map layer &#39;ajt&#39;: Postgis Plugin: ERROR:  relation &quot;icesheet_polygons&quot; does not exist
LINE 1: SELECT ST_SRID(&quot;way&quot;) AS srid FROM icesheet_polygons WHERE &quot;...
                                           ^
in executeQuery Full sql was: &#39;SELECT ST_SRID(&quot;way&quot;) AS srid FROM icesheet_polygons WHERE &quot;way&quot; IS NOT NULL LIMIT 1;&#39;
  encountered during parsing of layer &#39;icesheet-poly&#39; in Layer at line 5895 of &#39;/home/xj/src/openstreetmap-carto/mapnik.xml&#39;
renderd[23757]: An error occurred while loading the map layer &#39;ajt&#39;: Postgis Plugin: ERROR:  relation &quot;icesheet_polygons&quot; does not exist
LINE 1: SELECT ST_SRID(&quot;way&quot;) AS srid FROM icesheet_polygons WHERE &quot;...
                                           ^
in executeQuery Full sql was: &#39;SELECT ST_SRID(&quot;way&quot;) AS srid FROM icesheet_polygons WHERE &quot;way&quot; IS NOT NULL LIMIT 1;&#39;
  encountered during parsing of layer &#39;icesheet-poly&#39; in Layer at line 5895 of &#39;/home/xj/src/openstreetmap-carto/mapnik.xml&#39;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-tile" rel="tag" title="see questions tagged &#39;tile&#39;">tile</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jul '20, 02:38</strong></p>
<img src="https://secure.gravatar.com/avatar/4637c543421eb586aa1807010f43b39d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="%E5%BC%A0%E6%B2%BB%E9%9F%B3&#39;s gravatar image" />
<p><span>张治音</span><br />
<span class="score" title="90 reputation points">90</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="张治音 has 2 accepted answers">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jul '20, 06:44</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-75855" class="comments-container">
&#10;</div>
<div id="comment-tools-75855" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75855-form-container" class="comment-form-container">
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

<span id="75872"></span>

<div id="answer-container-75872" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75872-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75872-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75872-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="scai has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have solved the problem. Because I can not download the shapefiles.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jul '20, 03:23</strong></p>
<img src="https://secure.gravatar.com/avatar/4637c543421eb586aa1807010f43b39d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="%E5%BC%A0%E6%B2%BB%E9%9F%B3&#39;s gravatar image" />
<p><span>张治音</span><br />
<span class="score" title="90 reputation points">90</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="张治音 has 2 accepted answers">100%</span></p>
</div>
</div>
<div id="comments-container-75872" class="comments-container">
<span id="75873"></span>
<div id="comment-75873" class="comment">
<div id="post-75873-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The question regarding shapefile download is here: <a href="https://help.openstreetmap.org/questions/75856/when-building-tile-server-can-not-download-shapefile">https://help.openstreetmap.org/questions/75856/when-building-tile-server-can-not-download-shapefile</a></p>
</div>
<div id="comment-75873-info" class="comment-info">
<span class="comment-age">(24 Jul '20, 06:48)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-75872" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75872-form-container" class="comment-form-container">
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

