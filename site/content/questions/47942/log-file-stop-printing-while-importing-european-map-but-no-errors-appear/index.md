+++
type = "question"
title = "Log file stop printing while Importing european map but no errors appear"
description = '''Hi guys, I&#x27;m new here. I have installed nominatim on a centOS machine with 8 gb ram. I&#x27;m trying to import europan map and I follow step by step the wiki guide. Until yesterday all seems worked, but suddenly, after about 10 days of computation, the log file output is as below: Stopping table: planet_...'''
date = "2016-02-05T10:13:00Z"
lastmod = "2016-02-05T11:51:00Z"
weight = 47942
keywords = [ "nominatim", "data_import" ]
aliases = [ "/questions/47942" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Log file stop printing while Importing european map but no errors appear](/questions/47942/log-file-stop-printing-while-importing-european-map-but-no-errors-appear)

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
<span id="post-47942-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47942-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47942-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys, I'm new here. I have installed nominatim on a centOS machine with 8 gb ram. I'm trying to import europan map and I follow step by step the wiki guide.</p>
<p>Until yesterday all seems worked, but suddenly, after about 10 days of computation, the log file output is as below:</p>
<pre><code>Stopping table: planet_osm_nodes
Stopping table: planet_osm_rels
Stopped table: planet_osm_nodes in 0s
Building index on table: planet_osm_rels (fastupdate=off)
Stopping table: planet_osm_ways
Building index on table: planet_osm_ways (fastupdate=off)
Stopped table: planet_osm_rels in 710s</code></pre>
<p>And no error appear... The db keep growing (very slowly) and if I launch the command:</p>
<pre><code>select * from pg_stat_activity;</code></pre>
<p>I can see some activity. Even if I launch <em>ps -aux</em> command I can see my import process and other process depends on it. Do you think is everything ok?? The import process going on??</p>
<p>Thanks a lot G</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-data_import" rel="tag" title="see questions tagged &#39;data_import&#39;">data_import</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Feb '16, 10:13</strong></p>
<img src="https://secure.gravatar.com/avatar/8b8afc2fa4a72009fdf51409cd072c87?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="newbies&#39;s gravatar image" />
<p><span>newbies</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="newbies has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Feb '16, 10:18</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-47942" class="comments-container">
&#10;</div>
<div id="comment-tools-47942" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47942-form-container" class="comment-form-container">
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

<span id="47948"></span>

<div id="answer-container-47948" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47948-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47948-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47948-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is normal. The database is still building the index. It can easily take another day.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Feb '16, 11:51</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-47948" class="comments-container">
&#10;</div>
<div id="comment-tools-47948" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47948-form-container" class="comment-form-container">
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

