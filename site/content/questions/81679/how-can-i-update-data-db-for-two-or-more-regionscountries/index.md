+++
type = "question"
title = "How can I update data (db) for two or more regions/countries?"
description = '''Hi, I deployed osm tile server (using docker https://github.com/Overv/openstreetmap-tile-server) for Europe and Asia regions (made a merge from two .pbf files) but I can&#x27;t update my db, I see an errors:  [2021-09-08 05:51:01] 12808 downloading diff [2021-09-08 05:51:29] 12808 filtering diff Tracebac...'''
date = "2021-09-08T07:22:00Z"
lastmod = "2021-09-08T07:22:00Z"
weight = 81679
keywords = [ "replication", "docker" ]
aliases = [ "/questions/81679" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can I update data (db) for two or more regions/countries?](/questions/81679/how-can-i-update-data-db-for-two-or-more-regionscountries)

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
<span id="post-81679-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81679-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81679-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I deployed osm tile server (using docker <a href="https://github.com/Overv/openstreetmap-tile-server)">https://github.com/Overv/openstreetmap-tile-server)</a> for Europe and Asia regions (made a merge from two .pbf files) but I can't update my db, I see an errors:</p>
<p><code> [2021-09-08 05:51:01] 12808 downloading diff [2021-09-08 05:51:29] 12808 filtering diff Traceback (most recent call last): File "/home/renderer/src/regional/trim_osc.py", line 129, in &lt;module&gt; cur.execute(q1, (nodesM,)) psycopg2.errors.UndefinedTable: relation "planet_osm_nodes" does not exist LINE 1: select id from planet_osm_nodes where id = ANY(ARRAY[2503040... ^</code></p>
<code> </code>
<p><code>[2021-09-08 05:51:31] 12808 [error] Trim_osc error [2021-09-08 05:51:31] 12808 resetting state </code></p>
<p>How can I update data (db) for two or more regions/countries?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-replication" rel="tag" title="see questions tagged &#39;replication&#39;">replication</span> <span class="post-tag tag-link-docker" rel="tag" title="see questions tagged &#39;docker&#39;">docker</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Sep '21, 07:22</strong></p>
<img src="https://secure.gravatar.com/avatar/cae81fe201b2f189673e0170fd0fbcd3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="makcbc&#39;s gravatar image" />
<p><span>makcbc</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="makcbc has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Sep '21, 07:26</strong> </span></p>
</div>
</div>
<div id="comments-container-81679" class="comments-container">
&#10;</div>
<div id="comment-tools-81679" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81679-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

