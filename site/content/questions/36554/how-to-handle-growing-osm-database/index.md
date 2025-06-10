+++
type = "question"
title = "how to handle growing OSM database"
description = '''We are using 1.5TB hard disk and 128GB RAM machine for storing map data using nominatim. Now the OSM data is growing faster. If it needs more than 2TB means,how can it be handled? How it will affect the performance?'''
date = "2014-09-03T13:54:00Z"
lastmod = "2014-09-28T22:32:00Z"
weight = 36554
keywords = [ "nominatim" ]
aliases = [ "/questions/36554" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to handle growing OSM database](/questions/36554/how-to-handle-growing-osm-database)

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
<span id="post-36554-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36554-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36554-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We are using 1.5TB hard disk and 128GB RAM machine for storing map data using nominatim. Now the OSM data is growing faster. If it needs more than 2TB means,how can it be handled? How it will affect the performance?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Sep '14, 13:54</strong></p>
<img src="https://secure.gravatar.com/avatar/d995f3125278c5457aeea5269ef875a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vjaikrishnan&#39;s gravatar image" />
<p><span>vjaikrishnan</span><br />
<span class="score" title="40 reputation points">40</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vjaikrishnan has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-36554" class="comments-container">
<span id="36583"></span>
<div id="comment-36583" class="comment">
<div id="post-36583-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How to do RAID configuration for a machine with 128GB RAM and more than 4TB hard disk? will it affect I/O performance?</p>
</div>
<div id="comment-36583-info" class="comment-info">
<span class="comment-age">(04 Sep '14, 06:20)</span> <span class="comment-user userinfo">vjaikrishnan</span>
</div>
</div>
</div>
<div id="comment-tools-36554" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36554-form-container" class="comment-form-container">
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

<span id="37094"></span>

<div id="answer-container-37094" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37094-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37094-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-37094-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In Postgres you can move each table and index to a so called 'tablespace', which is a path in the file system. <a href="http://www.postgresql.org/docs/9.3/static/manage-ag-tablespaces.html">http://www.postgresql.org/docs/9.3/static/manage-ag-tablespaces.html</a></p>
<p>This way you can split the database onto several harddrives. The largest tables (planet_osm_ways, planet_osm_nodes, place) are all below 100GB.</p>
<p>I/O performance will probably be slightly better by using two harddrives.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Sep '14, 22:32</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-37094" class="comments-container">
&#10;</div>
<div id="comment-tools-37094" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37094-form-container" class="comment-form-container">
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

