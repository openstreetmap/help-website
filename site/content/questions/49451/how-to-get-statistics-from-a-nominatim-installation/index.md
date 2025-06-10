+++
type = "question"
title = "How to get statistics from a Nominatim installation?"
description = '''Hi,  What is the easiest way to get statistics from a Nominatim server? What I need is some statistics on number of successful/failed requests in a web page similar to mod_tile (http://hostname/mod_tile).'''
date = "2016-04-27T10:22:00Z"
lastmod = "2018-08-06T11:10:00Z"
weight = 49451
keywords = [ "statistics", "nominatim" ]
aliases = [ "/questions/49451" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to get statistics from a Nominatim installation?](/questions/49451/how-to-get-statistics-from-a-nominatim-installation)

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
<span id="post-49451-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49451-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49451-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, What is the easiest way to get statistics from a Nominatim server? What I need is some statistics on number of successful/failed requests in a web page similar to mod_tile (<a href="http://hostname/mod_tile).">http://hostname/mod_tile).</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Apr '16, 10:22</strong></p>
<img src="https://secure.gravatar.com/avatar/ca009706fa6df2b33eb931f781ff57f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="khamooshi&#39;s gravatar image" />
<p><span>khamooshi</span><br />
<span class="score" title="146 reputation points">146</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="khamooshi has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-49451" class="comments-container">
&#10;</div>
<div id="comment-tools-49451" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49451-form-container" class="comment-form-container">
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

<span id="49452"></span>

<div id="answer-container-49452" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49452-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49452-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-49452-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="khamooshi has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="https://en.wikipedia.org/wiki/Munin_%28software%29" title="Munin">Munin</a> graph plugins <a href="https://github.com/twain47/Nominatim/tree/master/munin">https://github.com/twain47/Nominatim/tree/master/munin</a> query the Nominatim database every 5 minutes. The <code>new_query_logs</code> table also has a column <code>results</code> (integer) which you can use to find those that didn't return results. This shows you how to query, you'll still need to create a page (.php file).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Apr '16, 13:36</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-49452" class="comments-container">
<span id="65103"></span>
<div id="comment-65103" class="comment">
<div id="post-65103-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The table new_query_log is empty on our servers. Is there a config file for logging requests?</p>
</div>
<div id="comment-65103-info" class="comment-info">
<span class="comment-age">(03 Aug '18, 13:05)</span> <span class="comment-user userinfo">khamooshi</span>
</div>
</div>
<span id="65151"></span>
<div id="comment-65151" class="comment">
<div id="post-65151-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/11673/khamooshi">@khamooshi</a> You can see those config values in build/settings/settings.php and overwrite them in build/settings/local.php One is for logging into the database (new_query_log table), another setting is for logging into a file on disk.</p>
</div>
<div id="comment-65151-info" class="comment-info">
<span class="comment-age">(06 Aug '18, 11:10)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-49452" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49452-form-container" class="comment-form-container">
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

