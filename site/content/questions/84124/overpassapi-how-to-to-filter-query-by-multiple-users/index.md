+++
type = "question"
title = "OverPassAPI: how to to filter query by multiple users ?"
description = '''I know how to filter an OverPass query for a given user, including how to use a negative condition: https://help.openstreetmap.org/questions/83153/how-to-filter-by-user-in-overpass-turbo But how can I filter the results based on a list of multiple users without duplicating the query statement? '''
date = "2022-04-08T06:54:00Z"
lastmod = "2022-04-11T15:40:00Z"
weight = 84124
keywords = [ "filter", "overpass", "multiple", "users" ]
aliases = [ "/questions/84124" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [OverPassAPI: how to to filter query by multiple users ?](/questions/84124/overpassapi-how-to-to-filter-query-by-multiple-users)

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
<span id="post-84124-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84124-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84124-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I know how to filter an OverPass query for a given user, including how to use a negative condition: <a href="https://help.openstreetmap.org/questions/83153/how-to-filter-by-user-in-overpass-turbo">https://help.openstreetmap.org/questions/83153/how-to-filter-by-user-in-overpass-turbo</a></p>
<p>But how can I filter the results based on a list of multiple users without duplicating the query statement?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-users" rel="tag" title="see questions tagged &#39;users&#39;">users</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Apr '22, 06:54</strong></p>
<img src="https://secure.gravatar.com/avatar/e3f994b2488e2182c63a7c44a5028ff6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmoffroad&#39;s gravatar image" />
<p><span>cmoffroad</span><br />
<span class="score" title="205 reputation points">205</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmoffroad has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84124" class="comments-container">
&#10;</div>
<div id="comment-tools-84124" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84124-form-container" class="comment-form-container">
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

<span id="84131"></span>

<div id="answer-container-84131" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84131-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84131-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-84131-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cmoffroad has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<pre><code>(if:user()!=&#39;DaveF&#39; &amp;&amp; user()!=&#39;cmoffroad&#39;);</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Apr '22, 17:06</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-84131" class="comments-container">
<span id="84157"></span>
<div id="comment-84157" class="comment">
<div id="post-84157-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>thank you!</p>
</div>
<div id="comment-84157-info" class="comment-info">
<span class="comment-age">(11 Apr '22, 15:40)</span> <span class="comment-user userinfo">cmoffroad</span>
</div>
</div>
</div>
<div id="comment-tools-84131" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84131-form-container" class="comment-form-container">
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

