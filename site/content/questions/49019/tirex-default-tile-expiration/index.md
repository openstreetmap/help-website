+++
type = "question"
title = "Tirex default tile expiration"
description = '''I just passed a tirex-batch job to my tirex-master without passing the expiration argument. I just took a brief look into the tirex source but couldn&#x27;t find anything regarding the default tile expiration time. So how does tirex handle this case? Is there a fixed/default tile lifespan for batch rende...'''
date = "2016-04-04T16:36:00Z"
lastmod = "2016-04-04T18:29:00Z"
weight = 49019
keywords = [ "tirex" ]
aliases = [ "/questions/49019" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Tirex default tile expiration](/questions/49019/tirex-default-tile-expiration)

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
<span id="post-49019-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49019-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-49019-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I just passed a tirex-batch job to my tirex-master without passing the expiration argument. I just took a brief look into the tirex source but couldn't find anything regarding the default tile expiration time. So how does tirex handle this case? Is there a fixed/default tile lifespan for batch rendered tiles, or does tirex check the database for changes and decides wheter to rerender the tiles at each time a new request comes in?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tirex" rel="tag" title="see questions tagged &#39;tirex&#39;">tirex</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Apr '16, 16:36</strong></p>
<img src="https://secure.gravatar.com/avatar/1d65bc251f62664c2af0a1b6cd0f2170?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ltsstar&#39;s gravatar image" />
<p><span>ltsstar</span><br />
<span class="score" title="66 reputation points">66</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ltsstar has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49019" class="comments-container">
&#10;</div>
<div id="comment-tools-49019" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49019-form-container" class="comment-form-container">
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

<span id="49021"></span>

<div id="answer-container-49021" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49021-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49021-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-49021-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ltsstar has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a misunderstanding. The tirex-batch "expire" option,</p>
<pre><code>   -e, --expire=TIME
           Expire time (seconds since epoch) for jobs. If it starts with &#39;+&#39;,
           number of seconds added to current time.</code></pre>
<p>specifies at what time a job should be removed from the queue if it hasn't been executed yet. It has nothing to do with the lifetime of a tile on disk. The default expire time is "never".</p>
<p>How long a tile is kept on disk is not something that Tirex decides; Tirex renders tiles when told so, full stop. Whether or not Tirex is told to render a tile, in a standard tileserver setup, is controlled by mod_tile, the Apache module responsible for delivering tiles. In a normal setup, a tile that is older than the last full planet import will be considered "old" and queued for re-rendering; in the absence of a file indicating the time of the last planet import, a tile older than 3 days will be considered "old". This is hard-coded here: <a href="https://github.com/openstreetmap/mod_tile/blob/6b9611aaf763f4f776d1fd363433aac7e25cb34b/src/store_file.c#L41">https://github.com/openstreetmap/mod_tile/blob/6b9611aaf763f4f776d1fd363433aac7e25cb34b/src/store_file.c#L41</a></p>
<p>There are various ways to handle tile expiry. One option is setting the "last full import" timestamp to something last year, and then using the "dirty tile list" that osm2pgsql can produce to change the timestamp of every tile that needs re-rendering to 1970-01-01. This will then cause mod_tile to trigger a re-render if such a tile is reuquested. Alternatively, the re-render can be triggered immediately from the osm2pgsql output, but that would mean that even tiles that are rarely ever looked at but change often, would also be computed often.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Apr '16, 18:11</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-49021" class="comments-container">
<span id="49023"></span>
<div id="comment-49023" class="comment">
<div id="post-49023-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>excellent answer.</p>
</div>
<div id="comment-49023-info" class="comment-info">
<span class="comment-age">(04 Apr '16, 18:29)</span> <span class="comment-user userinfo">ltsstar</span>
</div>
</div>
</div>
<div id="comment-tools-49021" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49021-form-container" class="comment-form-container">
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

