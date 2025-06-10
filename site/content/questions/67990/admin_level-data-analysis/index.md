+++
type = "question"
title = "[closed] admin_level data analysis"
description = '''Hi, We try to tune the rendering of admin_level data in OSM Carto: https://github.com/gravitystorm/openstreetmap-carto/issues/3678 but we need some stats about specific admin level distribution in the world (it&#x27;s important for us to have global data, since rendering on OSMF servers covers the whole ...'''
date = "2019-02-12T23:22:00Z"
lastmod = "2019-02-17T00:15:00Z"
weight = 67990
keywords = [ "code", "admin_level", "statistics", "analysis", "script" ]
aliases = [ "/questions/67990" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [\[closed\] admin_level data analysis](/questions/67990/admin_level-data-analysis)

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
<span id="post-67990-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67990-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67990-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>We try to tune the rendering of admin_level data in OSM Carto:</p>
<p><a href="https://github.com/gravitystorm/openstreetmap-carto/issues/3678">https://github.com/gravitystorm/openstreetmap-carto/issues/3678</a></p>
<p>but we need some stats about specific admin level distribution in the world (it's important for us to have global data, since rendering on OSMF servers covers the whole planet). How could we create a spreadsheet showing the size (area) or length of each admin level polygons? Unfortunately I'm not a coder.</p>
<p>Probably PBF analysis would be more convenient and versatile, but maybe a script using PostgreSQL/PostGIS features might be easier to write. I guess Overpass online is too limited for such queries, since many times I get errors about too much used memory, but maybe I'm wrong.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-code" rel="tag" title="see questions tagged &#39;code&#39;">code</span> <span class="post-tag tag-link-admin_level" rel="tag" title="see questions tagged &#39;admin_level&#39;">admin_level</span> <span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span> <span class="post-tag tag-link-script" rel="tag" title="see questions tagged &#39;script&#39;">script</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Feb '19, 23:22</strong></p>
<img src="https://secure.gravatar.com/avatar/e228dd20b7da2a6c8f559e2118ce08d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kocio&#39;s gravatar image" />
<p><span>kocio</span><br />
<span class="score" title="2054 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kocio has 14 accepted answers">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>17 Feb '19, 00:13</strong> </span></p>
</div>
</div>
<div id="comments-container-67990" class="comments-container">
&#10;</div>
<div id="comment-tools-67990" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67990-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Resolved" by kocio 17 Feb '19, 00:13

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="68031"></span>

<div id="answer-container-68031" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68031-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68031-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68031-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kocio has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Why don't you ask Walter to produce such numbers? <a href="https://wambachers-osm.website/index.php/projekte/internationale-administrative-grenzen/boundaries-map-4-3-english">https://wambachers-osm.website/index.php/projekte/internationale-administrative-grenzen/boundaries-map-4-3-english</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Feb '19, 11:15</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-68031" class="comments-container">
&#10;</div>
<div id="comment-tools-68031" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68031-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="68034"></span>

<div id="answer-container-68034" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68034-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68034-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68034-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>of course i can help.</p>
<p>just contaced carto team.</p>
<p>walter</p>
<p><a href="https://github.com/gravitystorm/openstreetmap-carto/issues/3678">https://github.com/gravitystorm/openstreetmap-carto/issues/3678</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Feb '19, 00:15</strong></p>
<img src="https://secure.gravatar.com/avatar/9b27b1be8215e118d8bdb679e7732771?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wambacher&#39;s gravatar image" />
<p><span>wambacher</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wambacher has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68034" class="comments-container">
&#10;</div>
<div id="comment-tools-68034" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68034-form-container" class="comment-form-container">
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

