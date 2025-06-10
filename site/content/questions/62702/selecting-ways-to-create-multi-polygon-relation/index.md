+++
type = "question"
title = "Selecting ways to create multi-polygon relation"
description = '''I want to map a park in an urban area using a multi-polygon (relation). The question is which way should I use to meet community&#x27;s best practice? I can choose...  streets: but some object already mapped (fire_hydrant) will then appear as in the park while they are not. existing addr:interpolation wa...'''
date = "2018-03-16T20:28:00Z"
lastmod = "2018-03-17T18:55:00Z"
weight = 62702
keywords = [ "ways", "addr_interpolation", "bestpractice", "multipolygon" ]
aliases = [ "/questions/62702" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Selecting ways to create multi-polygon relation](/questions/62702/selecting-ways-to-create-multi-polygon-relation)

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
<span id="post-62702-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62702-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62702-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to map a park in an urban area using a multi-polygon (relation). The question is which way should I use to meet community's best practice? I can choose...</p>
<ul>
<li>streets: but some object already mapped (fire_hydrant) will then appear as in the park while they are not.</li>
<li>existing addr:interpolation ways: would be perfect but I will need to split some of them, which is not a good practice (I think).</li>
<li>create a new way overlapping existing addr:interpolation ways, which does not seem right either.</li>
</ul>
<p>Thank in advance, Daniel</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-addr_interpolation" rel="tag" title="see questions tagged &#39;addr_interpolation&#39;">addr_interpolation</span> <span class="post-tag tag-link-bestpractice" rel="tag" title="see questions tagged &#39;bestpractice&#39;">bestpractice</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Mar '18, 20:28</strong></p>
<img src="https://secure.gravatar.com/avatar/a504353df13461ace2c733906a99ce16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jfd553&#39;s gravatar image" />
<p><span>jfd553</span><br />
<span class="score" title="389 reputation points">389</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jfd553 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62702" class="comments-container">
<span id="62703"></span>
<div id="comment-62703" class="comment">
<div id="post-62703-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A couple of thoughts - one is that it's sometimes easier to understand a situation if you provide a link to it.</p>
<p>Another is that it might be helpful to map examples of the alternatives over on the dev site <a href="https://master.apis.dev.openstreetmap.org/">https://master.apis.dev.openstreetmap.org/</a> . There's no rendering from that but people will be able to see what you mean by looking in an editor.</p>
</div>
<div id="comment-62703-info" class="comment-info">
<span class="comment-age">(16 Mar '18, 21:26)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="62706"></span>
<div id="comment-62706" class="comment">
<div id="post-62706-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Good point! here is an example... <a href="https://www.openstreetmap.org/edit#map=18/46.14306/-60.17191">https://www.openstreetmap.org/edit#map=18/46.14306/-60.17191</a></p>
</div>
<div id="comment-62706-info" class="comment-info">
<span class="comment-age">(16 Mar '18, 21:51)</span> <span class="comment-user userinfo">jfd553</span>
</div>
</div>
</div>
<div id="comment-tools-62702" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62702-form-container" class="comment-form-container">
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

<span id="62717"></span>

<div id="answer-container-62717" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62717-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62717-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-62717-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jfd553 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Areas should usually be mapped using their own ways. Don't use unrelated ways as area boundaries, so no street or addr:interpolation ways. You should only share ways when they are actually closely related, so if the park boundary is a wall, you should re-use the way tagged as wall as (part of) the area boundary.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Mar '18, 18:55</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-62717" class="comments-container">
&#10;</div>
<div id="comment-tools-62717" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62717-form-container" class="comment-form-container">
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

