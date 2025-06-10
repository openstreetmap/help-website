+++
type = "question"
title = "User Id vs registration timestamps"
description = '''I am looking at some users&#x27; profiles using the API. From time to time I find what seem to me discrepancies between Ids and registration timestamps. For instance, if we look at the above records...  user id=&quot;2302718&quot; ... account_created=&quot;2014-08-31T21:44:43Z&quot; user id=&quot;2302719&quot; ... account_created=&quot;20...'''
date = "2017-02-16T16:45:00Z"
lastmod = "2017-02-17T09:49:00Z"
weight = 54679
keywords = [ "profile", "timestamps", "users", "registration" ]
aliases = [ "/questions/54679" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [User Id vs registration timestamps](/questions/54679/user-id-vs-registration-timestamps)

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
<span id="post-54679-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54679-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-54679-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am looking at some users' profiles using the API. From time to time I find what seem to me discrepancies between Ids and registration timestamps. For instance, if we look at the above records...</p>
<ul>
<li>user id="2302718" ... account_created="2014-08-31T21:44:43Z"</li>
<li>user id="2302719" ... account_created="2014-08-31T21:44:01Z"</li>
</ul>
<p>the first user (2302718) has registered 42 seconds after the second one (2302719) while, according to the timestamps, I was expecting the first one to have registered prior to the second one. In some instances there are hours between them.</p>
<p>Any explanation?</p>
<p>PS - I have been told that users' ids are unique and auto-increment in sequence when users register to the project</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-profile" rel="tag" title="see questions tagged &#39;profile&#39;">profile</span> <span class="post-tag tag-link-timestamps" rel="tag" title="see questions tagged &#39;timestamps&#39;">timestamps</span> <span class="post-tag tag-link-users" rel="tag" title="see questions tagged &#39;users&#39;">users</span> <span class="post-tag tag-link-registration" rel="tag" title="see questions tagged &#39;registration&#39;">registration</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Feb '17, 16:45</strong></p>
<img src="https://secure.gravatar.com/avatar/a504353df13461ace2c733906a99ce16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jfd553&#39;s gravatar image" />
<p><span>jfd553</span><br />
<span class="score" title="389 reputation points">389</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jfd553 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Feb '17, 16:46</strong> </span></p>
</div>
</div>
<div id="comments-container-54679" class="comments-container">
&#10;</div>
<div id="comment-tools-54679" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54679-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="54684"></span>

<div id="answer-container-54684" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54684-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54684-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-54684-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jfd553 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I tested a bit with a local installation and am fairly sure (contrary to my original thoughts) that such inconsistencies are due to the rails frontends being out of sync time-wise which has historically happened now and then.</p>
<p>If you are seeing such behaviour with newly created accounts, please report them to the operations working group.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Feb '17, 23:45</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-54684" class="comments-container">
<span id="54690"></span>
<div id="comment-54690" class="comment">
<div id="post-54690-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yep, I understand the discrepancies may origin from multiple operations made either on the database and/or the rails frontends when someone register. Thank Simon.</p>
</div>
<div id="comment-54690-info" class="comment-info">
<span class="comment-age">(17 Feb '17, 09:43)</span> <span class="comment-user userinfo">jfd553</span>
</div>
</div>
</div>
<div id="comment-tools-54684" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54684-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="54687"></span>

<div id="answer-container-54687" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54687-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54687-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-54687-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the id and the creation date are not assigned in the same atomic operation, multiple threads can always create those "inconsistencies'. This could happen e.g. when the creation date is assigned by the software and the id by the database.</p>
<p>Can you explain why you think this is a problem ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Feb '17, 08:19</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-54687" class="comments-container">
<span id="54691"></span>
<div id="comment-54691" class="comment">
<div id="post-54691-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Right, as now understand that the process results from multiple treads or operations which may result in such inconsistencies. BTW, I do not think these inconsistencies are a problem, I was just curious to understand where they come from :-)</p>
</div>
<div id="comment-54691-info" class="comment-info">
<span class="comment-age">(17 Feb '17, 09:49)</span> <span class="comment-user userinfo">jfd553</span>
</div>
</div>
</div>
<div id="comment-tools-54687" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54687-form-container" class="comment-form-container">
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

