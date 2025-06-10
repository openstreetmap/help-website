+++
type = "question"
title = "Best practice on inner and outer."
description = '''I have come across a few mapping areas which have problems with inner and outer tags, and I am not sure what is considered to be best practice. So here is a scenario, Imagine a residential area, within that area is a golf course, on the golf course there are a number bunkers ( sand ) and a few areas...'''
date = "2016-07-28T14:18:00Z"
lastmod = "2016-07-29T09:07:00Z"
weight = 51149
keywords = [ "outer", "inner" ]
aliases = [ "/questions/51149" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Best practice on inner and outer.](/questions/51149/best-practice-on-inner-and-outer)

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
<span id="post-51149-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51149-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-51149-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have come across a few mapping areas which have problems with inner and outer tags, and I am not sure what is considered to be best practice.</p>
<p>So here is a scenario,</p>
<p>Imagine a residential area, within that area is a golf course, on the golf course there are a number bunkers ( sand ) and a few areas of woodland, also a lake and in the middle of the lake is an island which has a wood on it, and a pond and also more sand( bunkers ), I am not sure what the relationships on OSM are meant to be.</p>
<p>Any help or guidance would be appreciated.</p>
<p>Regards</p>
<p>Gary</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-outer" rel="tag" title="see questions tagged &#39;outer&#39;">outer</span> <span class="post-tag tag-link-inner" rel="tag" title="see questions tagged &#39;inner&#39;">inner</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jul '16, 14:18</strong></p>
<img src="https://secure.gravatar.com/avatar/1a48846e2865ba49198e0fb8e4064358?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rossendale%20Gary&#39;s gravatar image" />
<p><span>Rossendale Gary</span><br />
<span class="score" title="141 reputation points">141</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rossendale Gary has one accepted answer">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jul '16, 14:21</strong> </span></p>
</div>
</div>
<div id="comments-container-51149" class="comments-container">
&#10;</div>
<div id="comment-tools-51149" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51149-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="51152"></span>

<div id="answer-container-51152" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51152-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51152-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-51152-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First, "inner" and "outer" are not tags. They are <strong>roles</strong> of relation members. Each member of a multipolygon relation gets such a role, either "outer" for the ways making up the outer boundary of the area, or "inner" for the inner boundary.</p>
<p>So in your example the outermost area is the residential area. You create a multipolygon relation with the tags <em>type=multipolygon</em> and <em>landuse=residential</em>. The ways making up the boundaries of this area are untagged, but they get the roles "outer" and "inner" in the relation. Then you create another relation tagged <em>type=multipolygon</em> and <em>leisure=golf_course</em>. Its members are the ways you put in the residential area relation as "inner", but this time they are "outer". You add new "inner" ways to this relation for the holes in the golf course. And so on. So all the ways (except outermost and, possibly, innermost boundaries) do double duty as the inner boundary of the outer area and the outer boundary of the area nested inside of it.</p>
<p>Arguably the sand bunkers of a golf course are part of the golf course. They are not in holes in the golf course. So the golf course should probably tagged over all it contains with no inner holes. But the golf course is not part of the residential area, so a hole in the residential area makes sense. It is somewhat unclear what to do in each situation. Use your judgement.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jul '16, 14:50</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jul '16, 14:53</strong> </span></p>
</div>
</div>
<div id="comments-container-51152" class="comments-container">
&#10;</div>
<div id="comment-tools-51152" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51152-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="51165"></span>

<div id="answer-container-51165" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51165-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51165-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51165-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Gary, Did you notice the existance of these pages ? <a href="https://wiki.openstreetmap.org/wiki/Multipolygon_Examples">https://wiki.openstreetmap.org/wiki/Multipolygon_Examples</a> The complex ones could be the answer to your problem and question.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jul '16, 09:07</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-51165" class="comments-container">
&#10;</div>
<div id="comment-tools-51165" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51165-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="51150"></span>

<div id="answer-container-51150" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51150-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51150-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51150-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think I'd only use a multipolygon relation for the lake with a hole for the situation you describe with the lake tags on the relation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jul '16, 14:42</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-51150" class="comments-container">
<span id="51151"></span>
<div id="comment-51151" class="comment">
<div id="post-51151-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>can you point me to an example on OSM ?</p>
</div>
<div id="comment-51151-info" class="comment-info">
<span class="comment-age">(28 Jul '16, 14:45)</span> <span class="comment-user userinfo">Rossendale Gary</span>
</div>
</div>
</div>
<div id="comment-tools-51150" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51150-form-container" class="comment-form-container">
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

