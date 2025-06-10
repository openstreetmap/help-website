+++
type = "question"
title = "planet data replicate 2 or 3 hours data only"
description = '''Wants to update nominatim DB daily(1 day data at a time). My local.php: @define(&#x27;CONST_Replication_Url&#x27;, &#x27;https://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/replication/hour&#x27;); @define(&#x27;CONST_Replication_Update_Interval&#x27;, &#x27;86400&#x27;); @define(&#x27;CONST_Replication_Recheck_Interval&#x27;, &#x27;360...'''
date = "2018-10-25T06:38:00Z"
lastmod = "2018-10-26T06:50:00Z"
weight = 66455
keywords = [ "replication", "nominatim", "update", "settings", "mirror" ]
aliases = [ "/questions/66455" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [planet data replicate 2 or 3 hours data only](/questions/66455/planet-data-replicate-2-or-3-hours-data-only)

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
<span id="post-66455-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66455-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66455-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Wants to update nominatim DB daily(1 day data at a time).</p>
<p>My local.php:</p>
<p>@define('CONST_Replication_Url', 'https://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/replication/hour'); @define('CONST_Replication_Update_Interval', '<strong>86400</strong>'); @define('CONST_Replication_Recheck_Interval', '3600');</p>
<p>But, Updating 2 or 3 hrs data only everytime.</p>
<p>select * from import_osmosis_log ;</p>
<p>batchend       | batchseq | batchsize |      starttime      |       endtime       | event   ---------------------+----------+-----------+---------------------+---------------------+--------</p>
<p>2018-10-01 03:59:02 |    53037 |  92005726 | 2018-10-25 05:10:19 | 2018-10-25 05:13:00 | import  <strong>2018-10-01 03:59:02 |    53037</strong> |  92005726 | 2018-10-25 05:13:00 | 2018-10-25 05:15:56 | index  2018-10-01 06:58:49 |    53040 |  90095798 | 2018-10-25 05:16:08 | 2018-10-25 05:18:16 | import  <strong>2018-10-01 06:58:49 |    53040</strong> |  90095798 | 2018-10-25 05:18:16 | 2018-10-25 05:25:14 | index</p>
<p>Is there any config issue ?</p>
<p>Also tried to update 4 days replication data as: <a href="https://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/replication/">https://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/replication/</a><strong>day</strong> &amp; CONST_Replication_Update_Interval <strong>345600</strong>. But still 1 day data only updating.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-replication" rel="tag" title="see questions tagged &#39;replication&#39;">replication</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-settings" rel="tag" title="see questions tagged &#39;settings&#39;">settings</span> <span class="post-tag tag-link-mirror" rel="tag" title="see questions tagged &#39;mirror&#39;">mirror</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Oct '18, 06:38</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Oct '18, 15:20</strong> </span></p>
</div>
</div>
<div id="comments-container-66455" class="comments-container">
&#10;</div>
<div id="comment-tools-66455" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66455-form-container" class="comment-form-container">
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

<span id="66468"></span>

<div id="answer-container-66468" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66468-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>CONST_Replication_Update_Interval value is in seconds. So 3600 = 1 hour. 86400 = 24 hours. 345600 = 4 days. You probably want to use /replication/day and 86400. The CONST_Replication_Recheck_Interval should be smaller, could even be 900 (<a href="http://nominatim.org/release-docs/latest/admin/Import-and-Update/#updates).">http://nominatim.org/release-docs/latest/admin/Import-and-Update/#updates).</a> With <code>./utils/update.php --import-osmosis</code> only one day will be updated. Using <code>./utils/update.php --import-osmosis-all</code> it will run several updates in a loop until there are no longer updates available.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '18, 19:33</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-66468" class="comments-container">
<span id="66479"></span>
<div id="comment-66479" class="comment">
<div id="post-66479-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/150/mtmail"></a><a href="https://help.openstreetmap.org/users/150/mtmail">@mtmail</a>: Thanks!</p>
<p>In old Nominatim versions, I can update more than 1 day data at a time. But Now(in 3.1.0) only 1 day data updating in every loop though i given CONST_Replication_Update_Interval for 4 days(345600).</p>
</div>
<div id="comment-66479-info" class="comment-info">
<span class="comment-age">(26 Oct '18, 06:50)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
</div>
<div id="comment-tools-66468" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66468-form-container" class="comment-form-container">
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

