+++
type = "question"
title = "What&#x27;s wrong with openstreetmap.org tile_logs"
description = '''Hi,  There is an useful tile_log for OSM website: https://planet.openstreetmap.org/tile_logs/ However I noticed recently the log size decreased dramatically from around 10MB to less than 1KB. Is there something wrong?'''
date = "2021-01-21T22:55:00Z"
lastmod = "2021-01-22T00:59:00Z"
weight = 78445
keywords = [ "osm.org", "log" ]
aliases = [ "/questions/78445" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What's wrong with openstreetmap.org tile_logs](/questions/78445/whats-wrong-with-openstreetmaporg-tile_logs)

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
<span id="post-78445-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78445-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78445-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>There is an useful tile_log for OSM website: <a href="https://planet.openstreetmap.org/tile_logs/">https://planet.openstreetmap.org/tile_logs/</a></p>
<p>However I noticed recently the log size decreased dramatically from around 10MB to less than 1KB. Is there something wrong?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm.org" rel="tag" title="see questions tagged &#39;osm.org&#39;">osm.org</span> <span class="post-tag tag-link-log" rel="tag" title="see questions tagged &#39;log&#39;">log</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jan '21, 22:55</strong></p>
<img src="https://secure.gravatar.com/avatar/e39830800041c01c0ad201916e2c4065?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="strongwillow&#39;s gravatar image" />
<p><span>strongwillow</span><br />
<span class="score" title="65 reputation points">65</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="strongwillow has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78445" class="comments-container">
&#10;</div>
<div id="comment-tools-78445" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78445-form-container" class="comment-form-container">
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

<span id="78446"></span>

<div id="answer-container-78446" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78446-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78446-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78446-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="strongwillow has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM recently switched all remaining served countries from their tile cdn based on donated servers to an external commercial cdn (fastly). The logs you mentioned were produced out of the old tile cdn that is not in use anymore, therefor the numbers are drastically reduced.</p>
<p>It's already discussed in the OWG here :<a href="https://github.com/openstreetmap/operations/issues/485">https://github.com/openstreetmap/operations/issues/485</a></p>
<p>Traffic metrics of the new cdn can be seen here: <a href="https://prometheus.openstreetmap.org/d/3yhv0DtGz/tile-cdn?orgId=1&amp;refresh=1m">https://prometheus.openstreetmap.org/d/3yhv0DtGz/tile-cdn?orgId=1&amp;refresh=1m</a> but that probably won't help if you interested in statistical analysis (e.g. highly requested areas, etc.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jan '21, 00:59</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-78446" class="comments-container">
&#10;</div>
<div id="comment-tools-78446" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78446-form-container" class="comment-form-container">
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

