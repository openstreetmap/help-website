+++
type = "question"
title = "How to grant different privileges to users?"
description = '''I&#x27;m using a private osm server. I want to make myself as administrator and grant other users different privileges. How can that be achieved? I noticed there is a file called user_roles_controller.rb so i had a guess that i can access the users and edit them by going to localhost/users. But then i ge...'''
date = "2011-11-23T13:19:00Z"
lastmod = "2011-11-23T13:33:00Z"
weight = 9206
keywords = [ "privileges", "administrator", "railsport" ]
aliases = [ "/questions/9206" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to grant different privileges to users?](/questions/9206/how-to-grant-different-privileges-to-users)

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
<span id="post-9206-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9206-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-9206-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm using a private osm server. I want to make myself as administrator and grant other users different privileges. How can that be achieved?</p>
<p>I noticed there is a file called user_roles_controller.rb so i had a guess that i can access the users and edit them by going to localhost/users. But then i get an error message:You need to be an administrator to perform that action.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-privileges" rel="tag" title="see questions tagged &#39;privileges&#39;">privileges</span> <span class="post-tag tag-link-administrator" rel="tag" title="see questions tagged &#39;administrator&#39;">administrator</span> <span class="post-tag tag-link-railsport" rel="tag" title="see questions tagged &#39;railsport&#39;">railsport</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Nov '11, 13:19</strong></p>
<img src="https://secure.gravatar.com/avatar/dc9b01669c0702f230fa57c384b947a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexz&#39;s gravatar image" />
<p><span>alexz</span><br />
<span class="score" title="225 reputation points">225</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jul '18, 10:47</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-9206" class="comments-container">
&#10;</div>
<div id="comment-tools-9206" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9206-form-container" class="comment-form-container">
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

<span id="9207"></span>

<div id="answer-container-9207" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9207-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9207-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-9207-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="alexz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Rails_port#Giving_administrator.2Fmoderator_permissions">RTFM</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Nov '11, 13:22</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-9207" class="comments-container">
<span id="9209"></span>
<div id="comment-9209" class="comment">
<div id="post-9209-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thx, but that was mean.</p>
</div>
<div id="comment-9209-info" class="comment-info">
<span class="comment-age">(23 Nov '11, 13:33)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
</div>
<div id="comment-tools-9207" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9207-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9208"></span>

<div id="answer-container-9208" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9208-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9208-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-9208-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have to add an initial administrator manually, either from the rails console, or from an SQL command line.</p>
<p>After that the initial administrator can grant further people moderator or administrator powers through the web site by clicking the star icons on a user's user page.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Nov '11, 13:29</strong></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomH has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-9208" class="comments-container">
&#10;</div>
<div id="comment-tools-9208" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9208-form-container" class="comment-form-container">
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

