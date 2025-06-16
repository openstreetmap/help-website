+++
type = "question"
title = "How to tag streets with reversed lanes?"
description = '''In Brazil at least, the vehicles drive on the right side of the road. &quot;Right&quot; as in &quot;opposite of left&quot;, let me be clear... :) However there are a few places here where that, for some reason, the lanes of a two-way street are reversed. It means that in this place, vehicles drive on the &quot;left&quot; side of...'''
date = "2013-10-20T00:10:00Z"
lastmod = "2013-10-21T14:24:00Z"
weight = 27342
keywords = [ "reversed", "lanes", "tagging", "oneway" ]
aliases = [ "/questions/27342" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to tag streets with reversed lanes?](/questions/27342/how-to-tag-streets-with-reversed-lanes)

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
<span id="post-27342-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27342-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-27342-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In Brazil at least, the vehicles drive on the right side of the road. "Right" as in "opposite of left", let me be clear... :) However there are a few places here where that, for some reason, the lanes of a two-way street are reversed. It means that in this place, vehicles drive on the "left" side of the road.</p>
<p>How do I tag these streets? If they were wide enough, I would draw them as separate ways, but they are roads with only one lane in each direction, and there is no separator between them. Obviously, the way is "oneway=no", but with "sides" exchanged.</p>
<p>The "lanes" key, with the "forward"/"backward" subkeys seem not to address this issue, nor the "oneway" key, as per their documentation.</p>
<p>Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversed" rel="tag" title="see questions tagged &#39;reversed&#39;">reversed</span> <span class="post-tag tag-link-lanes" rel="tag" title="see questions tagged &#39;lanes&#39;">lanes</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-oneway" rel="tag" title="see questions tagged &#39;oneway&#39;">oneway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Oct '13, 00:10</strong></p>
<img src="https://secure.gravatar.com/avatar/94b019f273c04cd88bc1c8dd0a8f2161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MCPicoli&#39;s gravatar image" />
<p><span>MCPicoli</span><br />
<span class="score" title="2172 reputation points"><span>2.2k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MCPicoli has 10 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-27342" class="comments-container">
<span id="27374"></span>
<div id="comment-27374" class="comment">
<div id="post-27374-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>That's obviously a case where reallity has it wrong, and the local authority should sober up and restore normality.&lt;/joke&gt;</p>
</div>
<div id="comment-27374-info" class="comment-info">
<span class="comment-age">(21 Oct '13, 10:14)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-27342" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27342-form-container" class="comment-form-container">
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

<span id="27375"></span>

<div id="answer-container-27375" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27375-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27375-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-27375-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MCPicoli has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>While it's normally used on a country-wide boundary, you should probably add <a href="https://wiki.openstreetmap.org/wiki/Key:driving_side">driving_side=left/right</a> to the way itself. I doubt if this tag is used by any routing engine or other data consumer, however.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Oct '13, 10:18</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Oct '13, 13:47</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span></p>
</div>
</div>
<div id="comments-container-27375" class="comments-container">
<span id="27382"></span>
<div id="comment-27382" class="comment">
<div id="post-27382-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Great find, I didn't know that one - and I bet many others didn't either.</p>
</div>
<div id="comment-27382-info" class="comment-info">
<span class="comment-age">(21 Oct '13, 13:50)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
<span id="27383"></span>
<div id="comment-27383" class="comment">
<div id="post-27383-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Seems to be <a href="http://taginfo.openstreetmap.org/keys/driving_side#combinations">currently used on 13 highway-tagged objects</a>. Most are in Rio de Janeiro, Brazil (e.g. <a href="https://www.openstreetmap.org/browse/way/93268229">way 93268229</a> and some short turnlanes). Not sure if that are mistakes or real examples. One example is in Graz, Austria (<a href="https://www.openstreetmap.org/browse/way/4100061">way 4100061</a> which I guess is not really correct as the note comment suggests that it only applies to the buses).</p>
</div>
<div id="comment-27383-info" class="comment-info">
<span class="comment-age">(21 Oct '13, 14:24)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-27375" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27375-form-container" class="comment-form-container">
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

