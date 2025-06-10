+++
type = "question"
title = "How are the replication diffs created?"
description = '''Osmosis is executed to generate the replication diffs. What is it doing exactly?'''
date = "2010-07-14T15:54:00Z"
lastmod = "2013-03-03T11:07:00Z"
weight = 192
keywords = [ "technical", "diff", "osmosis" ]
aliases = [ "/questions/192" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How are the replication diffs created?](/questions/192/how-are-the-replication-diffs-created)

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
<span id="post-192-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-192-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-192-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Osmosis is executed to generate the replication diffs. What is it doing exactly?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-technical" rel="tag" title="see questions tagged &#39;technical&#39;">technical</span> <span class="post-tag tag-link-diff" rel="tag" title="see questions tagged &#39;diff&#39;">diff</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jul '10, 15:54</strong></p>
<img src="https://secure.gravatar.com/avatar/5c9aa062fed08c7962c88bd21cc62f93?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emka&#39;s gravatar image" />
<p><span>emka</span><br />
<span class="score" title="95 reputation points">95</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emka has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> retagged <strong>14 Jul '10, 16:29</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span></p>
</div>
</div>
<div id="comments-container-192" class="comments-container">
<span id="194"></span>
<div id="comment-194" class="comment">
<div id="post-194-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is <a href="http://help.openstreetmap.org">help.openstreetmap.org</a> really the place for in-depth technical discussions? The answer to this question would have to go into details of PostgreSQL transactions and the like, to a degree where anyone who can understand the answer can also read and understand the source code. IMHO we should keep <a href="http://help.openstreetmap.org">help.openstreetmap.org</a> end-user facing, not technical-geek-facing.</p>
</div>
<div id="comment-194-info" class="comment-info">
<span class="comment-age">(14 Jul '10, 16:17)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="197"></span>
<div id="comment-197" class="comment">
<div id="post-197-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Where would you draw the border?</p>
<p>Have a look at the first two questions for example: <a href="http://help.openstreetmap.org/questions/1">http://help.openstreetmap.org/questions/1</a> <a href="http://help.openstreetmap.org/questions/2">http://help.openstreetmap.org/questions/2</a></p>
<p>An answer containing the SQL commands would already help, reading a huge bunch of Java source code is too much for me right now.</p>
</div>
<div id="comment-197-info" class="comment-info">
<span class="comment-age">(14 Jul '10, 16:30)</span> <span class="comment-user userinfo">emka</span>
</div>
</div>
<span id="199"></span>
<div id="comment-199" class="comment">
<div id="post-199-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Careful with the first few questions - they were half-serious and half-just testing the system.</p>
<p>As for whether this is the place for in-depth technical discussion? No, certainly not. But ideally the documentation should exist somewhere, for example the wiki, and then the answer here can simply point towards it and provide a summary. It's not supposed to be that the answers here will be canonical, it's fine to have links for further reading.</p>
</div>
<div id="comment-199-info" class="comment-info">
<span class="comment-age">(14 Jul '10, 17:45)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
<span id="20459"></span>
<div id="comment-20459" class="comment">
<div id="post-20459-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm interested in the answer as well. How are the transaction-id's taken from?</p>
</div>
<div id="comment-20459-info" class="comment-info">
<span class="comment-age">(03 Mar '13, 11:07)</span> <span class="comment-user userinfo">bibstha</span>
</div>
</div>
</div>
<div id="comment-tools-192" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-192-form-container" class="comment-form-container">
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

<span id="195"></span>

<div id="answer-container-195" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-195-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-195-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-195-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The replication diffs are created using <a href="http://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a>. The option used is <a href="http://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.36#--replicate-apidb_.28--repa.29">'--replicate-apidb'</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jul '10, 16:22</strong></p>
<img src="https://secure.gravatar.com/avatar/e79628d44a15e95c607f8c5007d0ccd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Firefishy&#39;s gravatar image" />
<p><span>Firefishy ♦♦</span><br />
<span class="score" title="1296 reputation points"><span>1.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="36 badges"><span class="silver">●</span><span class="badgecount">36</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Firefishy has 14 accepted answers">29%</span></p>
</div>
</div>
<div id="comments-container-195" class="comments-container">
&#10;</div>
<div id="comment-tools-195" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-195-form-container" class="comment-form-container">
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

