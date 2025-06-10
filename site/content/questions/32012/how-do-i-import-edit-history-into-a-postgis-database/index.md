+++
type = "question"
title = "How do I Import edit history into a PostGIS database?"
description = '''I need to store the editing history of a region in a PostGIS database for statistical analysis. Correct me if I am wrong, but my understanding is Osmosis only writes the current versions to the database and does not include the history of the elements. Is there any other tool that can help me store ...'''
date = "2014-03-31T01:06:00Z"
lastmod = "2014-03-31T12:59:00Z"
weight = 32012
keywords = [ "osmosis", "data", "postgis", "analysis", "history" ]
aliases = [ "/questions/32012" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I Import edit history into a PostGIS database?](/questions/32012/how-do-i-import-edit-history-into-a-postgis-database)

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
<span id="post-32012-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32012-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32012-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to store the editing history of a region in a PostGIS database for statistical analysis. Correct me if I am wrong, but my understanding is Osmosis only writes the current versions to the database and does not include the history of the elements. Is there any other tool that can help me store the necessary information to a database?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span> <span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Mar '14, 01:06</strong></p>
<img src="https://secure.gravatar.com/avatar/ce2105c628f0492c916ba08fab8455d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vr3690&#39;s gravatar image" />
<p><span>vr3690</span><br />
<span class="score" title="66 reputation points">66</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vr3690 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-32012" class="comments-container">
<span id="32016"></span>
<div id="comment-32016" class="comment">
<div id="post-32016-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Your question assumes you will be able to do the analysis you need in PostGIS, but it's far from clear that this is possible. Perhaps rephrase your question to include what your goal is, rather than just one step of your process?</p>
</div>
<div id="comment-32016-info" class="comment-info">
<span class="comment-age">(31 Mar '14, 10:55)</span> <span class="comment-user userinfo">Jonathan Ben...</span>
</div>
</div>
</div>
<div id="comment-tools-32012" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32012-form-container" class="comment-form-container">
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

<span id="32019"></span>

<div id="answer-container-32019" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32019-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32019-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-32019-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you don't need relations, try Peter Körner's <a href="https://github.com/MaZderMind/osm-history-renderer">history tools</a>. The history importer creates a full-history database in an osm2pgsql-like format that is already quite useful for some kinds of statistical analysis.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Mar '14, 12:59</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-32019" class="comments-container">
&#10;</div>
<div id="comment-tools-32019" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32019-form-container" class="comment-form-container">
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

