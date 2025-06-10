+++
type = "question"
title = "How to tag a building with multiple materials?"
description = '''I have data from a ground survey which collected information on the structure of buildings. The options are wood, concrete or semi-concrete and wood. I now want to upload this information along with some other information to OSM. How would I tag the semi-concrete and wood ones? I&#x27;ve read the OSM wik...'''
date = "2021-01-22T11:49:00Z"
lastmod = "2021-01-23T10:43:00Z"
weight = 78447
keywords = [ "multiple", "tagging" ]
aliases = [ "/questions/78447" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag a building with multiple materials?](/questions/78447/how-to-tag-a-building-with-multiple-materials)

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
<span id="post-78447-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78447-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78447-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have data from a ground survey which collected information on the structure of buildings. The options are wood, concrete or semi-concrete and wood. I now want to upload this information along with some other information to OSM. How would I tag the semi-concrete and wood ones? I've read the OSM wiki on using multiple tags, but I'm still not quite sure, so any help would be appreciated.</p>
<p>The solution I came up with was to use the following tags/values if I have a building with mixed material:</p>
<p>building:material:wood=yes</p>
<p>building:material:concrete=yes</p>
<p>or could I use building:material=wood;concrete</p>
<p>as this is not a top level tag?</p>
<p>Many thanks for your help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jan '21, 11:49</strong></p>
<img src="https://secure.gravatar.com/avatar/6518b530412c69b4e8573e8ef7826c25?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="katlore&#39;s gravatar image" />
<p><span>katlore</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="katlore has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78447" class="comments-container">
<span id="78451"></span>
<div id="comment-78451" class="comment">
<div id="post-78451-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Do you mean a wall would have both wood and concrete? If they are on separate parts, <code>building:part=</code> can be used.</p>
</div>
<div id="comment-78451-info" class="comment-info">
<span class="comment-age">(23 Jan '21, 06:12)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
<span id="78452"></span>
<div id="comment-78452" class="comment">
<div id="post-78452-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/16887/kovoschiz"></a><a href="https://help.openstreetmap.org/users/16887/kovoschiz">@Kovoschiz</a>, yes exactly, the buildings are built with wood and concrete. Many thanks for the tip with building:part, I didn't know that existed. That is super useful. I just looked it up but I think I probably shouldn't be using it in my case. The building information I'm uploadin at the moment are only point locations ( I should have stated that in my question), but according to the wiki building:part should only be used on polygons, I might go with what <a href="https://help.openstreetmap.org/users/3443/hendrikklaas"></a><a href="https://help.openstreetmap.org/users/3443/hendrikklaas">@Hendrikklaas</a> suggested below.</p>
</div>
<div id="comment-78452-info" class="comment-info">
<span class="comment-age">(23 Jan '21, 10:43)</span> <span class="comment-user userinfo">katlore</span>
</div>
</div>
</div>
<div id="comment-tools-78447" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78447-form-container" class="comment-form-container">
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

<span id="78448"></span>

<div id="answer-container-78448" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78448-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78448-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78448-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, you should make a choice for instance the first floor or basement, that is what you see at first. But your own suggestion wood:concrete is a good one. It is not populair.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jan '21, 13:58</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-78448" class="comments-container">
&#10;</div>
<div id="comment-tools-78448" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78448-form-container" class="comment-form-container">
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

