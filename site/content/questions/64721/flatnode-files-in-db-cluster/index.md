+++
type = "question"
title = "Flatnode files in DB cluster"
description = '''Hi I have setup Postgres as cluster model (master &amp;amp; slave). Imported planet data with Flatnode_File config in master server &amp;amp; DB data will sync to slave(not flatnode file) Now I want to query(geocode/reverse) in both master &amp;amp; slave. Is there any problem(performance/data related) will arr...'''
date = "2018-07-14T15:55:00Z"
lastmod = "2018-07-15T09:24:00Z"
weight = 64721
keywords = [ "clustering", "query", "nominatim", "flatnode" ]
aliases = [ "/questions/64721" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Flatnode files in DB cluster](/questions/64721/flatnode-files-in-db-cluster)

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
<span id="post-64721-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64721-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64721-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I have setup Postgres as cluster model (master &amp; slave). Imported planet data with Flatnode_File config in master server &amp; DB data will sync to slave(not flatnode file) Now I want to query(geocode/reverse) in both master &amp; slave. Is there any problem(performance/data related) will arrive while querying in slave?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-clustering" rel="tag" title="see questions tagged &#39;clustering&#39;">clustering</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-flatnode" rel="tag" title="see questions tagged &#39;flatnode&#39;">flatnode</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jul '18, 15:55</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span></p>
</div>
</div>
<div id="comments-container-64721" class="comments-container">
&#10;</div>
<div id="comment-tools-64721" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64721-form-container" class="comment-form-container">
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

<span id="64724"></span>

<div id="answer-container-64724" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64724-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64724-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64724-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You only need the flatnode file on the master. It is used during import and data update, not querying. Master/slave should work. The slave database cannot be written to directly so make sure you keep the <code>@define('CONST_Log_DB', false);</code> (settings.php).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jul '18, 18:21</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-64724" class="comments-container">
<span id="64728"></span>
<div id="comment-64728" class="comment">
<div id="post-64728-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/150/mtmail">@mtmail</a>: Thank you</p>
</div>
<div id="comment-64728-info" class="comment-info">
<span class="comment-age">(14 Jul '18, 20:19)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
<span id="64730"></span>
<div id="comment-64730" class="comment">
<div id="post-64730-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Note that if you use a syncing mechanism that can do per-table sync (like e.g. slony), you only need to replicate a subset of all tables for geocoding to work. The list of required tables is here: <a href="https://github.com/openstreetmap/Nominatim/blob/master/utils/setup.php#L658-L672">https://github.com/openstreetmap/Nominatim/blob/master/utils/setup.php#L658-L672</a></p>
</div>
<div id="comment-64730-info" class="comment-info">
<span class="comment-age">(15 Jul '18, 09:24)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-64724" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64724-form-container" class="comment-form-container">
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

