+++
type = "question"
title = "What does the warning &quot;role reverse unknown - role verification problem&quot; mean in JOSM"
description = '''I get the warning &quot;role reverse unknown - role verification problem&quot; in JOSM but I am not sure what the issue is. The only thing I can think of is that I split a way included in this relation so I could change the layer of a particular segment. The relation ID is 3160902. The changeset that gave me ...'''
date = "2013-11-29T14:14:00Z"
lastmod = "2013-12-04T12:21:00Z"
weight = 28602
keywords = [ "josm", "warning", "relations", "validator" ]
aliases = [ "/questions/28602" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What does the warning "role reverse unknown - role verification problem" mean in JOSM](/questions/28602/what-does-the-warning-role-reverse-unknown-role-verification-problem-mean-in-josm)

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
<span id="post-28602-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28602-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-28602-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I get the warning "role reverse unknown - role verification problem" in JOSM but I am not sure what the issue is. The only thing I can think of is that I split a way included in this relation so I could change the layer of a particular segment. The relation ID is <a href="https://www.openstreetmap.org/browse/relation/3160902">3160902</a>. The changeset that gave me the error is <a href="https://www.openstreetmap.org/browse/changeset/19178806">that one</a>.</p>
<p>Cheers!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-warning" rel="tag" title="see questions tagged &#39;warning&#39;">warning</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-validator" rel="tag" title="see questions tagged &#39;validator&#39;">validator</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Nov '13, 14:14</strong></p>
<img src="https://secure.gravatar.com/avatar/19c111f5c672fdb25353073c835f6a38?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephane-guillou&#39;s gravatar image" />
<p><span>stephane-gui...</span><br />
<span class="score" title="585 reputation points">585</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephane-guillou has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-28602" class="comments-container">
&#10;</div>
<div id="comment-tools-28602" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28602-form-container" class="comment-form-container">
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

<span id="28604"></span>

<div id="answer-container-28604" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28604-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28604-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-28604-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="stephane-guillou has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The generic "role <em>something</em> unknown" error means that the relation contains members that have an unexpected role for the given relation type. In this case, josm doen't like the "reverse" role that some member ways have. Checking the wiki for the <a href="https://wiki.openstreetmap.org/wiki/Relation:route#Members">route relation</a> hints that "backward" is the expected role instead of reverse. Go fix the relation :)</p>
<p>Note that JOSM might warn you about errors that weren't caused by you, but you edit an object that already contained errors. Don't blame JOSM, blame the previous contributor :p</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Nov '13, 14:47</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-28604" class="comments-container">
<span id="28758"></span>
<div id="comment-28758" class="comment">
<div id="post-28758-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>And note that sometimes JOSM flags errors that do not exist at all (because JOSM's database of known roles of relation members is incomplete). Example: "site" type relations and its multiple possible members roles. Example 2: Power line end node flagged as untagged because the associated sub_station was not downloaded (end nodes of power lines do not have to have "power=tower/pole" if inside a sub_station). So, one has to be careful to see the whole picture when fixing JOSM's warnings.</p>
</div>
<div id="comment-28758-info" class="comment-info">
<span class="comment-age">(04 Dec '13, 12:21)</span> <span class="comment-user userinfo">MCPicoli</span>
</div>
</div>
</div>
<div id="comment-tools-28604" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28604-form-container" class="comment-form-container">
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

