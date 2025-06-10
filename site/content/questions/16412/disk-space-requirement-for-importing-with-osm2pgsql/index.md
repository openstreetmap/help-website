+++
type = "question"
title = "Disk space requirement for importing with OSM2PGSQL"
description = '''How much disk space is required for importing the current OpenstreetMap binary data of the whole planet to PostgreSQL database with OSM2Pqsql? RAM size would be 32 GB.'''
date = "2012-09-24T12:02:00Z"
lastmod = "2012-09-24T15:54:00Z"
weight = 16412
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/16412" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Disk space requirement for importing with OSM2PGSQL](/questions/16412/disk-space-requirement-for-importing-with-osm2pgsql)

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
<span id="post-16412-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16412-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-16412-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How much disk space is required for importing the current OpenstreetMap binary data of the whole planet to PostgreSQL database with OSM2Pqsql?</p>
<p>RAM size would be 32 GB.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Sep '12, 12:02</strong></p>
<img src="https://secure.gravatar.com/avatar/7651f7a3094f0a39b51630214fe9c94d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alex_AddisMap&#39;s gravatar image" />
<p><span>Alex_AddisMap</span><br />
<span class="score" title="189 reputation points">189</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alex_AddisMap has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Sep '12, 12:54</strong> </span></p>
</div>
</div>
<div id="comments-container-16412" class="comments-container">
&#10;</div>
<div id="comment-tools-16412" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16412-form-container" class="comment-form-container">
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

<span id="16416"></span>

<div id="answer-container-16416" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16416-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16416-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-16416-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>About 230 GB if you use the new "flatnode" storage, or about 300 GB otherwise. Numbers are for 64bit IDs and "slim" mode which is the only mode available for that amount of memory. If you don't need updates, the temporary storage space is the same, but you can drop a lot of data afterwards, leaving you with only about 80 GB for the full planet.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Sep '12, 13:06</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-16416" class="comments-container">
<span id="16417"></span>
<div id="comment-16417" class="comment">
<div id="post-16417-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What data can I drop? And is there no way to exclude that data needed for updates?</p>
</div>
<div id="comment-16417-info" class="comment-info">
<span class="comment-age">(24 Sep '12, 13:29)</span> <span class="comment-user userinfo">Alex_AddisMap</span>
</div>
</div>
<span id="16427"></span>
<div id="comment-16427" class="comment">
<div id="post-16427-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>osm2pgsql takes the standard OpenStreetMap model of nodes ways and relations and turns them into geometries (points, lines, polygons). For diff imports it still needs the node way and relation info, so it needs to store it on disk. Likewise, if you don't have enough ram to keep them in memory during the import it needs to temporarily store the info in the database and then delete it in the end if you don't need it for diff import anymore. Osm2pgsql will do this automatically with the --drop option</p>
</div>
<div id="comment-16427-info" class="comment-info">
<span class="comment-age">(24 Sep '12, 15:54)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
</div>
<div id="comment-tools-16416" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16416-form-container" class="comment-form-container">
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

