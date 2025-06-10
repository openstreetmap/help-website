+++
type = "question"
title = "postgres error while import planet data"
description = '''https://github.com/openstreetmap/Nominatim/issues/409 I met the same error in postgres_10.3 and my server details: CentOS7.4, 128GB RAM, 3TB HD. As suggested using following cmd to indexing: ./utils/setup.php --index --create-search-indices How to fix the same permenently? Is there any postgres conf...'''
date = "2018-10-08T11:52:00Z"
lastmod = "2018-10-12T11:12:00Z"
weight = 66211
keywords = [ "import", "postgresql" ]
aliases = [ "/questions/66211" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [postgres error while import planet data](/questions/66211/postgres-error-while-import-planet-data)

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
<span id="post-66211-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66211-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66211-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><a href="https://github.com/openstreetmap/Nominatim/issues/409">https://github.com/openstreetmap/Nominatim/issues/409</a></p>
<p>I met the same error in postgres_10.3 and my server details: CentOS7.4, 128GB RAM, 3TB HD.</p>
<p>As suggested using following cmd to indexing: ./utils/setup.php --index --create-search-indices</p>
<p>How to fix the same permenently? Is there any postgres config to solve the same?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Oct '18, 11:52</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Oct '18, 11:55</strong> </span></p>
</div>
</div>
<div id="comments-container-66211" class="comments-container">
&#10;</div>
<div id="comment-tools-66211" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66211-form-container" class="comment-form-container">
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

<span id="66214"></span>

<div id="answer-container-66214" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66214-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66214-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66214-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Error "buffer 82340 is not owned by resource owner"</p>
<p>That issue also came up in <a href="https://github.com/openstreetmap/Nominatim/issues/1168">https://github.com/openstreetmap/Nominatim/issues/1168</a> again. See my answer there. Root cause is still a mystery. Restarting the import with less threads seems to work.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Oct '18, 12:51</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-66214" class="comments-container">
<span id="66216"></span>
<div id="comment-66216" class="comment">
<div id="post-66216-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/150/mtmail"></a><a href="https://help.openstreetmap.org/users/150/mtmail">@mtmail</a>: Thanks for your answer. 1 doubt: i just running ./utils/setup.php --index --create-search-indices after met that err. Is it enough?</p>
<p>OR Need to run ./utils/setup.php --index --create-country-names --index-noanalyse (From Lonvia's reply in that thread #1168) ?</p>
</div>
<div id="comment-66216-info" class="comment-info">
<span class="comment-age">(08 Oct '18, 14:22)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
<span id="66217"></span>
<div id="comment-66217" class="comment">
<div id="post-66217-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Depends at which step our import failed. See <a href="http://nominatim.org/release-docs/latest/admin/Faq/#can-a-stoppedkilled-import-process-be-resumed">http://nominatim.org/release-docs/latest/admin/Faq/#can-a-stoppedkilled-import-process-be-resumed</a></p>
</div>
<div id="comment-66217-info" class="comment-info">
<span class="comment-age">(08 Oct '18, 15:17)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="66237"></span>
<div id="comment-66237" class="comment">
<div id="post-66237-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/150/mtmail"></a><a href="https://help.openstreetmap.org/users/150/mtmail">@mtmail</a> Thanks &amp; sorry for asking again. My initial import failed while indexing 30th rank. now i am running ./utils/setup.php --index --create-search-indices Is it enough? or need to run ./utils/setup.php --index --create-country-names --index-noanalyse again ?</p>
<p>Note: Its running for more than 6+ hrs. Checked my old setup logs(import planet data few weeks before), Create Search indices takes less than 3 hrs only</p>
</div>
<div id="comment-66237-info" class="comment-info">
<span class="comment-age">(09 Oct '18, 06:04)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
<span id="66255"></span>
<div id="comment-66255" class="comment">
<div id="post-66255-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>(7h later) Is the index creation still running, do you see CPU (top) and disc access (iotop). Do you see index related queries blocked by other sessions in <code>select pid, usename, pg_blocking_pids(pid) as blocked_by, query as blocked_query from pg_stat_activity where cardinality(pg_blocking_pids(pid)) &gt; 0;</code>?</p>
</div>
<div id="comment-66255-info" class="comment-info">
<span class="comment-age">(09 Oct '18, 13:33)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="66309"></span>
<div id="comment-66309" class="comment">
<div id="post-66309-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Reason for slowness is drop index is waiting for autovacuum completion.</p>
<p>blocked_pid | blocked_user | blocking_pid | blocking_user | blocked_statement | current_statement_in_blocking_process<br />
-------------+--------------+--------------+---------------+----------------------------------------------+------------------------------------------------------------------ 721 | nomiuser | 6839 | | DROP INDEX IF EXISTS idx_placex_rank_search; | autovacuum: VACUUM ANALYZE public.placex (to prevent wraparound)</p>
</div>
<div id="comment-66309-info" class="comment-info">
<span class="comment-age">(12 Oct '18, 09:11)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
<span id="66313"></span>
<div id="comment-66313" class="comment not_top_scorer">
<div id="post-66313-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can kill the autovacuum. It runs regularly in the background (well, foreground in this case it seems) and will restart automatically. <a href="https://blog.sleeplessbeastie.eu/2014/07/23/how-to-terminate-postgresql-sessions/">https://blog.sleeplessbeastie.eu/2014/07/23/how-to-terminate-postgresql-sessions/</a></p>
</div>
<div id="comment-66313-info" class="comment-info">
<span class="comment-age">(12 Oct '18, 11:12)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-66214" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-66214-form-container" class="comment-form-container">
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

