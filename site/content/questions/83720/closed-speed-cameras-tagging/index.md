+++
type = "question"
title = "[Closed] Speed cameras tagging"
description = '''I&#x27;m updating speed cameras. They all have a enforcement relation type Relation tags: enforcement=maxspeed maxspeed= name= type=enforcement Members: from= to= device=* But some of the speed cameras also have on the device node, set name, maxspeed and highway=speed_camera. Are these tags on the device...'''
date = "2022-03-07T07:53:00Z"
lastmod = "2022-03-07T16:03:00Z"
weight = 83720
keywords = [ "relations" ]
aliases = [ "/questions/83720" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [\[Closed\] Speed cameras tagging](/questions/83720/closed-speed-cameras-tagging)

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
<span id="post-83720-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83720-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83720-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm updating speed cameras. They all have a enforcement relation type</p>
<p>Relation tags: enforcement=maxspeed maxspeed= <em>name=</em> type=enforcement</p>
<p>Members: from= <em>to=</em> device=*</p>
<p>But some of the speed cameras also have on the device node, set name, maxspeed and highway=speed_camera. Are these tags on the device node needed?</p>
<p>Also all roads with speed cameras, has maxspeed set/tag. Is still the maxspeed needed on the device-node or relation?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Mar '22, 07:53</strong></p>
<img src="https://secure.gravatar.com/avatar/7fbbe44e24bdb695025fddb0879817a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Msiipola&#39;s gravatar image" />
<p><span>Msiipola</span><br />
<span class="score" title="227 reputation points">227</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Msiipola has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Mar '22, 08:07</strong> </span></p>
</div>
</div>
<div id="comments-container-83720" class="comments-container">
&#10;</div>
<div id="comment-tools-83720" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83720-form-container" class="comment-form-container">
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

<span id="83738"></span>

<div id="answer-container-83738" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83738-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83738-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83738-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Msiipola has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Tagging the speed camera itself with all the details is the older way to do it. Enforcement relations have been added later (albeit already a long time ago). So repeating the information may assist backward capability. It is not wrong. <code>highway=speed_camera</code> I would tag in any case to give the node a purpose.</p>
<p>Even if the maxspeed is tagged to the road you need to give the max_speed details on the relation (and on the node if you like). Depending on situation it is not always easy to derive the speed limit relevant for the camera and I doubt many data consumers are even trying.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Mar '22, 15:14</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-83738" class="comments-container">
<span id="83741"></span>
<div id="comment-83741" class="comment">
<div id="post-83741-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for answer and info.</p>
<p>I have seen the tag "highway=speed_camera" on some camera/device-nodes, but not all. But your suggestion of giving the node a purpose with a such tag, sounds good.</p>
</div>
<div id="comment-83741-info" class="comment-info">
<span class="comment-age">(07 Mar '22, 16:03)</span> <span class="comment-user userinfo">Msiipola</span>
</div>
</div>
</div>
<div id="comment-tools-83738" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83738-form-container" class="comment-form-container">
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

