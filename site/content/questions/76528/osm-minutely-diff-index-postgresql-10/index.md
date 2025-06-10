+++
type = "question"
title = "OSM Minutely Diff Index Postgresql 10"
description = '''I previously was able to load a large .pbf file into the APIDB and then use osmosis to do minutely extraction. I would like to test this with postgresql 10, but it seems the previous index on xid (system column) is no longer supported in postgresql 10. Just wondering if something has changed in the ...'''
date = "2020-09-09T14:52:00Z"
lastmod = "2020-09-11T12:17:00Z"
weight = 76528
keywords = [ "index", "postgresql" ]
aliases = [ "/questions/76528" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM Minutely Diff Index Postgresql 10](/questions/76528/osm-minutely-diff-index-postgresql-10)

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
<span id="post-76528-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76528-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76528-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I previously was able to load a large .pbf file into the APIDB and then use osmosis to do minutely extraction. I would like to test this with postgresql 10, but it seems the previous index on xid (system column) is no longer supported in postgresql 10. Just wondering if something has changed in the indexing on postgresql 10.</p>
<p>Previous index command:</p>
<p><code>CREATE INDEX nodes_xmin_idx ON nodes USING btree (xid_to_int4(xmin))</code></p>
<p>Error:</p>
<p><code>index creation on system columns is not supported</code></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-index" rel="tag" title="see questions tagged &#39;index&#39;">index</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Sep '20, 14:52</strong></p>
<img src="https://secure.gravatar.com/avatar/943c484e8c04680902357de8f080dcc0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cellington&#39;s gravatar image" />
<p><span>Cellington</span><br />
<span class="score" title="216 reputation points">216</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cellington has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Sep '20, 14:53</strong> </span></p>
</div>
</div>
<div id="comments-container-76528" class="comments-container">
&#10;</div>
<div id="comment-tools-76528" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76528-form-container" class="comment-form-container">
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

<span id="76530"></span>

<div id="answer-container-76530" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76530-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76530-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76530-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I see, potentially moving on from osmosis.</p>
<p>Reference:</p>
<p><a href="https://github.com/openstreetmap/operations/issues/438">https://github.com/openstreetmap/operations/issues/438</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Sep '20, 16:16</strong></p>
<img src="https://secure.gravatar.com/avatar/943c484e8c04680902357de8f080dcc0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cellington&#39;s gravatar image" />
<p><span>Cellington</span><br />
<span class="score" title="216 reputation points">216</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cellington has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76530" class="comments-container">
<span id="76557"></span>
<div id="comment-76557" class="comment">
<div id="post-76557-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This should really only be required if you intend to create diffs from your APIDB, so the issue could perceivably be addressed by adding a flag that indicates if you want this or not (naturally on PG 10 this would not be possible).</p>
</div>
<div id="comment-76557-info" class="comment-info">
<span class="comment-age">(11 Sep '20, 12:17)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-76530" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76530-form-container" class="comment-form-container">
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

