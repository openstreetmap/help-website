+++
type = "question"
title = "OSM Minutely Diffs process"
description = '''I&#x27;m curious if anyone knows where proper documentation lives that walks through how osm manages to pull minutely diff files from the API database? I know the documentation states that they use osmosis --read-apid. Warning this gets a little in the weeds, but I am trying to find the proper channel to...'''
date = "2017-02-15T16:06:00Z"
lastmod = "2017-02-15T17:14:00Z"
weight = 54653
keywords = [ "diffs", "apidb", "osmosis" ]
aliases = [ "/questions/54653" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM Minutely Diffs process](/questions/54653/osm-minutely-diffs-process)

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
<span id="post-54653-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54653-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-54653-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm curious if anyone knows where proper documentation lives that walks through how osm manages to pull minutely diff files from the API database?</p>
<p>I know the documentation states that they use osmosis --read-apid. Warning this gets a little in the weeds, but I am trying to find the proper channel to ask my question.</p>
<p>Looking at osmosis source code, this is the query passed to the DB:</p>
<p>(CREATE TEMPORARY TABLE tmp_nodes ON COMMIT DROP AS SELECT node_id, version FROM nodes WHERE (((xid_to_int4(xmin) &gt;= ## AND xid_to_int4(xmin) &lt;= ##))) AND redaction_id IS NULL;)</p>
<p>I don't see how osm is able to read the nodes table and filter down by transation IDs in &lt; 1 minute. Scaling up from my small API db it would seem that the nodes table in osm production API db would have to be around 350GB alone.</p>
<p>Looking here - <a href="https://hardware.openstreetmap.org/servers/katla.openstreetmap.org/">https://hardware.openstreetmap.org/servers/katla.openstreetmap.org/</a></p>
<p>The data shows that the Main server housing the APIdb has 252 GB RAM. This wouldn't be enough to read the entire nodes table in to RAM, so I must be missing something.</p>
<p>If anyone has an idea how this is accomplished or where it is documented, I would be really interested in hearing about it.</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-diffs" rel="tag" title="see questions tagged &#39;diffs&#39;">diffs</span> <span class="post-tag tag-link-apidb" rel="tag" title="see questions tagged &#39;apidb&#39;">apidb</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Feb '17, 16:06</strong></p>
<img src="https://secure.gravatar.com/avatar/943c484e8c04680902357de8f080dcc0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cellington&#39;s gravatar image" />
<p><span>Cellington</span><br />
<span class="score" title="216 reputation points">216</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cellington has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54653" class="comments-container">
&#10;</div>
<div id="comment-tools-54653" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54653-form-container" class="comment-form-container">
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

<span id="54654"></span>

<div id="answer-container-54654" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54654-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54654-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-54654-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That's easy, we have an extra index on the <code>nodes</code> table, defined as follows:</p>
<pre><code>CREATE INDEX nodes_xmin_idx ON nodes USING btree (xid_to_int4(xmin))</code></pre>
<p>There are also equivalent indexes on the <code>ways</code> and <code>relations</code> tables.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Feb '17, 16:51</strong></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomH has 9 accepted answers">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Feb '17, 16:57</strong> </span></p>
</div>
</div>
<div id="comments-container-54654" class="comments-container">
<span id="54655"></span>
<div id="comment-54655" class="comment">
<div id="post-54655-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah an additional index, that makes sense. Thanks <a href="https://help.openstreetmap.org/users/1/tomh">@TomH</a></p>
</div>
<div id="comment-54655-info" class="comment-info">
<span class="comment-age">(15 Feb '17, 17:14)</span> <span class="comment-user userinfo">Cellington</span>
</div>
</div>
</div>
<div id="comment-tools-54654" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54654-form-container" class="comment-form-container">
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

