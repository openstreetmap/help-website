+++
type = "question"
title = "osmosis cannot fit even a small pbf in memory"
description = '''Hi, I am working on optimizing the process of converting pbf files to Postgres ingestion files with osmosis --write-pgsql-dump. In my case, Osmosis cannot complete the writing of dump files for Europe even in 5 days so I was looking for different options to speed it up and I found the nodeLocationSt...'''
date = "2022-02-11T10:18:00Z"
lastmod = "2022-02-11T10:18:00Z"
weight = 83451
keywords = [ "performance", "osmosis", "memory" ]
aliases = [ "/questions/83451" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [osmosis cannot fit even a small pbf in memory](/questions/83451/osmosis-cannot-fit-even-a-small-pbf-in-memory)

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
<span id="post-83451-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83451-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83451-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am working on optimizing the process of converting pbf files to Postgres ingestion files with osmosis --write-pgsql-dump. In my case, Osmosis cannot complete the writing of dump files for Europe even in 5 days so I was looking for different options to speed it up and I found the nodeLocationStoreType=InMemory parameter which will read the nodes in memory and thus speed up the process significantly. However, it seems that this is not possible even with a small pbf for Albania for example (43MB) with a machine with 64GB of ram. I get an OutofmemoryError: Java heap space and I have allocated 55GB RAM to JVM with JAVACMD_OPTIONS="-Xmx55G". I don't understand how is this possible and if I am missing something. The command that i use is: osmosis -v --read-pbf-fast file="albania-latest.osm.pbf" --log-progress interval=60 --used-node --write-pgsql-dump enableBboxBuilder=yes enableLinestringBuilder=yes directory=/home keepInvalidWays=no nodeLocationStoreType=InMemory</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-memory" rel="tag" title="see questions tagged &#39;memory&#39;">memory</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Feb '22, 10:18</strong></p>
<img src="https://secure.gravatar.com/avatar/e1f88b5309d38cefd8e5c9c328002848?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LiliaAngelova&#39;s gravatar image" />
<p><span>LiliaAngelova</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LiliaAngelova has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83451" class="comments-container">
&#10;</div>
<div id="comment-tools-83451" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83451-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

