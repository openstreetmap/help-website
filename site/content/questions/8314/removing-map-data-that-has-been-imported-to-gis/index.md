+++
type = "question"
title = "Removing map data that has been imported to gis"
description = '''How can I remove map data that I&#x27;ve imported to the gis database? I&#x27;m working with a limited amount of space and when i tried to import new map data, it eventually failed due to lack of memory. Thanks in advance. -NDFobia1158'''
date = "2011-10-05T14:33:00Z"
lastmod = "2011-10-14T16:43:00Z"
weight = 8314
keywords = [ "remove" ]
aliases = [ "/questions/8314" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Removing map data that has been imported to gis](/questions/8314/removing-map-data-that-has-been-imported-to-gis)

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
<span id="post-8314-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8314-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8314-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I remove map data that I've imported to the gis database? I'm working with a limited amount of space and when i tried to import new map data, it eventually failed due to lack of memory. Thanks in advance.</p>
<p>-NDFobia1158</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-remove" rel="tag" title="see questions tagged &#39;remove&#39;">remove</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Oct '11, 14:33</strong></p>
<img src="https://secure.gravatar.com/avatar/48980c72ff56a285d3689c40bc272e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NDFobia1158&#39;s gravatar image" />
<p><span>NDFobia1158</span><br />
<span class="score" title="61 reputation points">61</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NDFobia1158 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Oct '11, 14:35</strong> </span></p>
</div>
</div>
<div id="comments-container-8314" class="comments-container">
<span id="8315"></span>
<div id="comment-8315" class="comment">
<div id="post-8315-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>What apps are you using?</p>
</div>
<div id="comment-8315-info" class="comment-info">
<span class="comment-age">(05 Oct '11, 14:47)</span> <span class="comment-user userinfo">Firefishy ♦♦</span>
</div>
</div>
<span id="8449"></span>
<div id="comment-8449" class="comment">
<div id="post-8449-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm using osm2pgsql</p>
</div>
<div id="comment-8449-info" class="comment-info">
<span class="comment-age">(14 Oct '11, 14:28)</span> <span class="comment-user userinfo">NDFobia1158</span>
</div>
</div>
</div>
<div id="comment-tools-8314" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8314-form-container" class="comment-form-container">
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

<span id="8327"></span>

<div id="answer-container-8327" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8327-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8327-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-8327-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="NDFobia1158 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I mention you are working with an PostGis DB and using a script to import OSM to the DB, somthing like Osm2pgsql or Osmosis.</p>
<p>You can filter the OSM-Data before importing by using Osmosis. eg:</p>
<pre><code>osmosis --read-xml city.osm --way-key-value keyValueList=&quot;railway.tram, railway.tram_stop&quot; -used-node idTrackerType=BitSet --write-xml city_tram.osm</code></pre>
<p>here are some examples: <a href="http://wiki.openstreetmap.org/wiki/Osmosis#Example_Usage">http://wiki.openstreetmap.org/wiki/Osmosis#Example_Usage</a></p>
<p>and the Usage: <a href="http://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage">http://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Oct '11, 10:21</strong></p>
<img src="https://secure.gravatar.com/avatar/db9d4c9ffd75f95f97122bbc97b90a64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="josias&#39;s gravatar image" />
<p><span>josias</span><br />
<span class="score" title="598 reputation points">598</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="josias has 3 accepted answers">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Oct '11, 10:22</strong> </span></p>
</div>
</div>
<div id="comments-container-8327" class="comments-container">
<span id="8457"></span>
<div id="comment-8457" class="comment">
<div id="post-8457-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It depends on what data you want to ignore. You can reduce the bbox or filter the data as josias has mentioned. You can also edit the input style file for osm2pgsql for limiting the data imported.</p>
</div>
<div id="comment-8457-info" class="comment-info">
<span class="comment-age">(14 Oct '11, 16:43)</span> <span class="comment-user userinfo">NicolasDumoulin</span>
</div>
</div>
</div>
<div id="comment-tools-8327" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8327-form-container" class="comment-form-container">
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

