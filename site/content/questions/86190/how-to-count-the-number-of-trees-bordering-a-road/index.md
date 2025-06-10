+++
type = "question"
title = "How to count the number of trees bordering a road ?"
description = '''Hello!  What I would like to do is to write a script that would be able to tell me how many trees border each road in a small area. I&#x27;m using overpass-turbo, and I managed to get a list of roads with trees bordering them, with this script. However, I&#x27;m unable to count the trees. I then tried using t...'''
date = "2022-11-19T16:13:00Z"
lastmod = "2022-11-25T12:24:00Z"
weight = 86190
keywords = [ "count", "counting", "overpass-turbo", "counter" ]
aliases = [ "/questions/86190" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to count the number of trees bordering a road ?](/questions/86190/how-to-count-the-number-of-trees-bordering-a-road)

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
<span id="post-86190-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86190-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86190-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello! What I would like to do is to write a script that would be able to tell me how many trees border each road in a small area. I'm using overpass-turbo, and I managed to get a list of roads with trees bordering them, with <a href="https://overpass-turbo.eu/s/1nWB">this script</a>. However, I'm unable to count the trees. I then tried using <a href="https://overpass-turbo.eu/s/1nWC">this script</a>, but all it does is count the number of roads with trees bordering them and not the number of trees bordering each road. Please let me know if you have any idea how I could do that. Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-count" rel="tag" title="see questions tagged &#39;count&#39;">count</span> <span class="post-tag tag-link-counting" rel="tag" title="see questions tagged &#39;counting&#39;">counting</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-counter" rel="tag" title="see questions tagged &#39;counter&#39;">counter</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Nov '22, 16:13</strong></p>
<img src="https://secure.gravatar.com/avatar/441b32ce26bf729c73797ea667c6f47a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AloysP&#39;s gravatar image" />
<p><span>AloysP</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AloysP has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86190" class="comments-container">
&#10;</div>
<div id="comment-tools-86190" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86190-form-container" class="comment-form-container">
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

<span id="86192"></span>

<div id="answer-container-86192" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86192-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86192-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86192-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi AloysP, It depends on the accuraty of the mapper, if he chooses for natural=tree_line it is not possible since there is no accurate data. If the trees are tagged natural=tree you should be able to define and select the area of the way with the surrounding natural=trees in a certain area. Due to these variable values I dont expect to find a solution than counting them yourself.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Nov '22, 22:58</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-86192" class="comments-container">
&#10;</div>
<div id="comment-tools-86192" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86192-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86226"></span>

<div id="answer-container-86226" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86226-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86226-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86226-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Okay, thank you for your answer, I'll try another way</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Nov '22, 12:24</strong></p>
<img src="https://secure.gravatar.com/avatar/441b32ce26bf729c73797ea667c6f47a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AloysP&#39;s gravatar image" />
<p><span>AloysP</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AloysP has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86226" class="comments-container">
&#10;</div>
<div id="comment-tools-86226" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86226-form-container" class="comment-form-container">
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

