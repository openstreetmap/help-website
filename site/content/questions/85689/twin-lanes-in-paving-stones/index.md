+++
type = "question"
title = "Twin lanes in paving stones"
description = '''Hi There is a surface value concrete:lanes but what about if the lanes are made out of paving stones or any other pavement ?  Use paving-stones:lanes ? And what for the surface in between the lanes ?'''
date = "2022-09-22T13:02:00Z"
lastmod = "2022-09-23T07:27:00Z"
weight = 85689
keywords = [ "lanes", "surface" ]
aliases = [ "/questions/85689" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Twin lanes in paving stones](/questions/85689/twin-lanes-in-paving-stones)

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
<span id="post-85689-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85689-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85689-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi There is a surface value concrete:lanes but what about if the lanes are made out of paving stones or any other pavement ? Use paving-stones:lanes ? And what for the surface in between the lanes ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-lanes" rel="tag" title="see questions tagged &#39;lanes&#39;">lanes</span> <span class="post-tag tag-link-surface" rel="tag" title="see questions tagged &#39;surface&#39;">surface</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Sep '22, 13:02</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-85689" class="comments-container">
&#10;</div>
<div id="comment-tools-85689" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85689-form-container" class="comment-form-container">
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

<span id="85691"></span>

<div id="answer-container-85691" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85691-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85691-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85691-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li><code>=paving_stones</code> is different situation because <code>paving_stones:*=</code> is used. It won't be bad to use <code>=paving_stones:lanes</code> for now. Ideally <code>=concrete:*</code> should be replaced, then that can be added in <code>paving_stones:*=</code>. Aside from recent discussions about <code>=concrete:plates</code>, seems the difference from <code>=paving_stones</code> can be unclear. <a href="https://discord.com/channels/413070382636072960/782593988611014676/1002643941436424212">https://discord.com/channels/413070382636072960/782593988611014676/1002643941436424212</a> has question about large <code>=paving_stones</code> pieces vs <code>=concrete</code>. <a href="https://wiki.openstreetmap.org/wiki/Tag:surface=paving_stones#See_also">https://wiki.openstreetmap.org/wiki/Tag:surface=paving_stones#See_also</a> has mixed wording with "concrete paving stones" as <code>=concrete:lanes</code>. (Of course growing to something as long as <code>=concrete:plate:lanes</code> won't work. It's not scalable)</li>
<li><code>surface:middle=</code> was suggested. <a href="https://community.openstreetmap.org/t/track-grading-and-surfacing/2130/2">https://community.openstreetmap.org/t/track-grading-and-surfacing/2130/2</a></li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Sep '22, 07:27</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-85691" class="comments-container">
&#10;</div>
<div id="comment-tools-85691" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85691-form-container" class="comment-form-container">
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

