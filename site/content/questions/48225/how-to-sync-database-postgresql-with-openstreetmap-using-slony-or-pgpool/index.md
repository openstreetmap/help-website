+++
type = "question"
title = "How to sync database postgresql with openstreetmap using slony or pgpool."
description = '''I&#x27;m new in domain openstreetmap i would like you help me to resolve a problom. I would wish to sync my database postgresql with openstreetmap using slony or Pgpool. But i don&#x27;t know how to do it, or whether it is possible to do it. I ensure you i have already done some research, but unfortunately i ...'''
date = "2016-02-19T16:05:00Z"
lastmod = "2016-02-19T16:29:00Z"
weight = 48225
keywords = [ "openstreetmap", "postgresql", "sync", "slony", "pgpool" ]
aliases = [ "/questions/48225" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to sync database postgresql with openstreetmap using slony or pgpool.](/questions/48225/how-to-sync-database-postgresql-with-openstreetmap-using-slony-or-pgpool)

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
<span id="post-48225-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48225-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48225-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm new in domain openstreetmap i would like you help me to resolve a problom. I would wish to sync my database postgresql with openstreetmap using slony or Pgpool. But i don't know how to do it, or whether it is possible to do it. I ensure you i have already done some research, but unfortunately i have not found some responses that answering my needs. If someone have some ideas please help me. thank you in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-sync" rel="tag" title="see questions tagged &#39;sync&#39;">sync</span> <span class="post-tag tag-link-slony" rel="tag" title="see questions tagged &#39;slony&#39;">slony</span> <span class="post-tag tag-link-pgpool" rel="tag" title="see questions tagged &#39;pgpool&#39;">pgpool</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Feb '16, 16:05</strong></p>
<img src="https://secure.gravatar.com/avatar/cc907eaebc2b384f9234262825ac0ea7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Abou&#39;s gravatar image" />
<p><span>Abou</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Abou has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48225" class="comments-container">
<span id="48227"></span>
<div id="comment-48227" class="comment">
<div id="post-48227-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>crossposts: <a href="https://gis.stackexchange.com/questions/181471/how-to-sync-database-postgresql-with-openstreetmap-using-slony-or-pgpool,">https://gis.stackexchange.com/questions/181471/how-to-sync-database-postgresql-with-openstreetmap-using-slony-or-pgpool,</a> <a href="https://stackoverflow.com/questions/35508842/how-to-sync-database-postgresql-with-openstreetmap-using-slony-or-pgpool">https://stackoverflow.com/questions/35508842/how-to-sync-database-postgresql-with-openstreetmap-using-slony-or-pgpool</a></p>
</div>
<div id="comment-48227-info" class="comment-info">
<span class="comment-age">(19 Feb '16, 16:29)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48225" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48225-form-container" class="comment-form-container">
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

<span id="48226"></span>

<div id="answer-container-48226" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48226-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48226-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48226-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want to have a local postgresql database that has regular updates from the main openstreeetmap.org database/api, you can't use slony, and instead must use the osmosis replication procedure. You can keep a local database updated to practically the minute this way, and it's how everyone does it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Feb '16, 16:10</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-48226" class="comments-container">
&#10;</div>
<div id="comment-tools-48226" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48226-form-container" class="comment-form-container">
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

