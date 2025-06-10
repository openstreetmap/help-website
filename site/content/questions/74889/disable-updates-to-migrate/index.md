+++
type = "question"
title = "disable updates to migrate"
description = '''Hello , Before doing the migration, should I disable something to do it? 3.3.0 -&amp;gt; 3.4.0 Reorganisation of location_area_country table The table location_area_country has been optimized. You need to switch to the new format when you run updates. While updates are disabled, run the following SQL co...'''
date = "2020-05-18T18:17:00Z"
lastmod = "2020-05-18T22:13:00Z"
weight = 74889
keywords = [ "nominatim", "migration", "version", "update" ]
aliases = [ "/questions/74889" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [disable updates to migrate](/questions/74889/disable-updates-to-migrate)

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
<span id="post-74889-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74889-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74889-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello , Before doing the migration, should I disable something to do it?</p>
<p>3.3.0 -&gt; 3.4.0 Reorganisation of location_area_country table The table location_area_country has been optimized. You need to switch to the new format when you run updates. While updates are disabled, run the following SQL commands:</p>
<p>CREATE TABLE location_area_country_new AS SELECT place_id, country_code, geometry FROM location_area_country; DROP TABLE location_area_country; ALTER TABLE location_area_country_new RENAME TO location_area_country; CREATE INDEX idx_location_area_country_geometry ON location_area_country USING GIST (geometry); CREATE INDEX idx_location_area_country_place_id ON location_area_count</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-migration" rel="tag" title="see questions tagged &#39;migration&#39;">migration</span> <span class="post-tag tag-link-version" rel="tag" title="see questions tagged &#39;version&#39;">version</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 May '20, 18:17</strong></p>
<img src="https://secure.gravatar.com/avatar/224322734ba5aec7f8c1b96e32946ca1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edderantonio&#39;s gravatar image" />
<p><span>edderantonio</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edderantonio has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74889" class="comments-container">
&#10;</div>
<div id="comment-tools-74889" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74889-form-container" class="comment-form-container">
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

<span id="74892"></span>

<div id="answer-container-74892" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74892-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74892-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74892-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://nominatim.org/release-docs/latest/admin/Migration/">https://nominatim.org/release-docs/latest/admin/Migration/</a> Disable anything that writes to the database. That's the update script (<a href="http://nominatim.org/release-docs/latest/admin/Import-and-Update/#updates),">http://nominatim.org/release-docs/latest/admin/Import-and-Update/#updates),</a> if you haven't installed the update script, then nothing needs to be disabled.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 May '20, 21:08</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-74892" class="comments-container">
<span id="74893"></span>
<div id="comment-74893" class="comment">
<div id="post-74893-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thank you!</p>
</div>
<div id="comment-74893-info" class="comment-info">
<span class="comment-age">(18 May '20, 21:36)</span> <span class="comment-user userinfo">edderantonio</span>
</div>
</div>
<span id="74895"></span>
<div id="comment-74895" class="comment">
<div id="post-74895-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>but it doesn't come in the documentation how to disable</p>
</div>
<div id="comment-74895-info" class="comment-info">
<span class="comment-age">(18 May '20, 22:10)</span> <span class="comment-user userinfo">edderantonio</span>
</div>
</div>
<span id="74897"></span>
<div id="comment-74897" class="comment">
<div id="post-74897-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If the script is running kill the process. <a href="https://www.linux.com/topic/desktop/how-kill-process-command-line/">https://www.linux.com/topic/desktop/how-kill-process-command-line/</a> If the script is not running, then nothing needs to be done. Make sure the cronjob is disabled so it doesn't start automatically.</p>
</div>
<div id="comment-74897-info" class="comment-info">
<span class="comment-age">(18 May '20, 22:13)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-74892" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74892-form-container" class="comment-form-container">
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

