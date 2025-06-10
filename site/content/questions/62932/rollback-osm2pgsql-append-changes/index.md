+++
type = "question"
title = "rollback osm2pgsql append changes"
description = '''I did create a self hosted map server with Mapnik and postgis. So i did append an OSM file which i created in josm. How i can delete those changes? I used --append switch when using osm2pgsql, Is it replace the old data with new one?'''
date = "2018-04-06T22:56:00Z"
lastmod = "2018-04-07T08:51:00Z"
weight = 62932
keywords = [ "rollback", "osm2pgsql" ]
aliases = [ "/questions/62932" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [rollback osm2pgsql append changes](/questions/62932/rollback-osm2pgsql-append-changes)

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
<span id="post-62932-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62932-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62932-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I did create a self hosted map server with <code>Mapnik</code> and <code>postgis</code>. So i did append an OSM file which i created in <code>josm</code>. How i can delete those changes? I used --append switch when using osm2pgsql, Is it replace the old data with new one?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rollback" rel="tag" title="see questions tagged &#39;rollback&#39;">rollback</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Apr '18, 22:56</strong></p>
<img src="https://secure.gravatar.com/avatar/976e165a9bd4b1aaf035f790545a0776?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cybercoder&#39;s gravatar image" />
<p><span>cybercoder</span><br />
<span class="score" title="36 reputation points">36</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cybercoder has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62932" class="comments-container">
&#10;</div>
<div id="comment-tools-62932" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62932-form-container" class="comment-form-container">
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

<span id="62934"></span>

<div id="answer-container-62934" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62934-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62934-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-62934-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The answer is probably "with difficulty", unfortunately. If your new file contains changes and deletes then you'll need to find out what the previous versions of those objects were.</p>
<p>If, however your appended file only contained creates, then you can programmatically create a file that deletes those additions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Apr '18, 00:07</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-62934" class="comments-container">
&#10;</div>
<div id="comment-tools-62934" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62934-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="62936"></span>

<div id="answer-container-62936" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62936-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62936-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62936-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One thing you could do is:</p>
<ul>
<li>create a list of all relations, ways, and nodes mentioned in the file that you created in JOSM.</li>
<li>download all these objects from the OSM API (e.g. with something like <code>wget -Omysfile.osm </code><a href="http://api.openstreetmap.org/api/0.6/nodes?nodes=1,2,3,4"><code>http://api.openstreetmap.org/api/0.6/nodes?nodes=1,2,3,4</code></a>)</li>
<li>using <code>--append</code> mode again, add this data to your database, overwriting any modifications you made with current data from OSM.</li>
</ul>
<p>This will not "go back" to whatever your data was before your modification, but instead "go forward" to whatever the current state is in OSM, but perhaps it helps?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Apr '18, 08:51</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-62936" class="comments-container">
&#10;</div>
<div id="comment-tools-62936" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62936-form-container" class="comment-form-container">
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

