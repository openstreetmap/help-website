+++
type = "question"
title = "Nominatim update error has no None column"
description = '''I have successfully installed nominatim ver 3.0.1 on centOs 7.3. Set CONST_Pyosmium_Binary, CONST_Replication_Url, CONST_Replication_Update_Interval and CONST_Replication_Recheck_Interval. When I am trying to update manually via command ./utils/update.php --init-updates I am getting error: PHP Warni...'''
date = "2017-08-28T13:46:00Z"
lastmod = "2017-08-29T19:40:00Z"
weight = 58848
keywords = [ "nominatim", "update" ]
aliases = [ "/questions/58848" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim update error has no None column](/questions/58848/nominatim-update-error-has-no-none-column)

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
<span id="post-58848-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58848-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-58848-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have successfully installed nominatim ver 3.0.1 on centOs 7.3. Set CONST_Pyosmium_Binary, CONST_Replication_Url, CONST_Replication_Update_Interval and CONST_Replication_Recheck_Interval. When I am trying to update manually via command ./utils/update.php --init-updates I am getting error:</p>
<p><strong>PHP Warning: pg_query(): Query failed: ERROR: column "none" does not exist LINE 1: ...quence_id, indexed) VALUES('2017-08-21T20:34:32Z' ,None, true... in &lt;nominatim home=""&gt;/Nominatim/build/utils/update.php on line 87 ERROR: Could not enter sequence into database. Could not enter sequence into database.</strong></p>
<p>How to deal with it?</p>
<p>And two more little questions: 1) How to know datetime of my last update? 2) When database will be updated if I have CONST_Replication_Update_Interval = 86400? Is nominatim trying to update after system startup or since 86400 from startup or since wich event?</p>
<p>Thanks for your attention.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Aug '17, 13:46</strong></p>
<img src="https://secure.gravatar.com/avatar/d2d51d4ac4f36d821d8ec0bf48ea985b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gsv91&#39;s gravatar image" />
<p><span>gsv91</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gsv91 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-58848" class="comments-container">
&#10;</div>
<div id="comment-tools-58848" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58848-form-container" class="comment-form-container">
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

<span id="58851"></span>

<div id="answer-container-58851" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58851-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58851-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-58851-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gsv91 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For some reason, pyosmium could not correctly connect to the server with the update. It should return a proper error message in that case. If you see this message about 'None' then you have found a bug in the update code. Please report it over on <a href="https://github.com/openstreetmap/Nominatim/issues">github</a>.</p>
<p>Nominatim determines the appropriate date where to start the updates from the data you imported. If the initialisation runs through, it reports it at the end of the process. The date is also reported after each update start. Furthermore, you can check the current status anytime in the <code>import_status</code> table in your database.</p>
<p>The update interval is computed from the last time the database was updated. You can safely shut down your system for a while and it will pick up exactly where it left.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Aug '17, 20:44</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-58851" class="comments-container">
<span id="58856"></span>
<div id="comment-58856" class="comment">
<div id="post-58856-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My import_status table is empty. With what it can be connected?</p>
</div>
<div id="comment-58856-info" class="comment-info">
<span class="comment-age">(29 Aug '17, 09:23)</span> <span class="comment-user userinfo">gsv91</span>
</div>
</div>
<span id="58858"></span>
<div id="comment-58858" class="comment">
<div id="post-58858-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>import_status was truncated by the init-updates command before it errored out. It will be filled appropriately again once init-updates has run successfully.</p>
</div>
<div id="comment-58858-info" class="comment-info">
<span class="comment-age">(29 Aug '17, 19:40)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
</div>
<div id="comment-tools-58851" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58851-form-container" class="comment-form-container">
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

