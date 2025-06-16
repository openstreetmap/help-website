+++
type = "question"
title = "Help me map an abandoned road on public land?"
description = '''I would appreciate your advice on how to map this place.  Believe it or not, this is the entrance to a public land, but the city is required by regulations to have this gate closed and locked in front of it. It is trivial for bikes and pedestrians to walk around the gate, although it is impassible b...'''
date = "2016-08-22T13:17:00Z"
lastmod = "2016-08-22T21:48:00Z"
weight = 51642
keywords = [ "abandoned", "tagging" ]
aliases = [ "/questions/51642" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Help me map an abandoned road on public land?](/questions/51642/help-me-map-an-abandoned-road-on-public-land)

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
<span id="post-51642-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51642-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51642-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would appreciate your advice on how to map this place. <img src="/upfiles/fence.jpeg" alt="alt text" /> Believe it or not, this is the entrance to a public land, but the city is required by regulations to have this gate closed and locked in front of it. It is trivial for bikes and pedestrians to walk around the gate, although it is impassible by cars. Behind the gate is an abandoned road, which leads to hiking trails.</p>
<p>Would I use abandoned:highway=* for the road? Or should the highway=footway since it is only closed to vehicles? Do you recommend barrier=gate or I was thinking barrier=fence ; fence=chain_link since the gate is always closed.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-abandoned" rel="tag" title="see questions tagged &#39;abandoned&#39;">abandoned</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Aug '16, 13:17</strong></p>
<img src="https://secure.gravatar.com/avatar/cb68523a12e3580728c6bee495ae602e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtc&#39;s gravatar image" />
<p><span>mtc</span><br />
<span class="score" title="411 reputation points">411</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtc has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Aug '16, 00:52</strong> </span></p>
</div>
</div>
<div id="comments-container-51642" class="comments-container">
&#10;</div>
<div id="comment-tools-51642" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51642-form-container" class="comment-form-container">
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

<span id="51656"></span>

<div id="answer-container-51656" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51656-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51656-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-51656-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mtc has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The lifecycle prefix <span><code>abandoned:</code></span> works by prepending it to the tag's key which the feature would have had before it was abandoned. I do not know what this one was/is. Maybe a <code>highway=service</code> or <code>highway=track</code>. Depends on its use. However, is this road really abandoned, or just used by few city vehicles? It also looks like it is in a reasonable state, so I would just use the normal highway tag (not abandoned:). For example: <code>highway=track</code> + <code>tracktype=grade1</code> + <code>surface=asphalt</code>. If it was a "unclassified" road before it was "abanoned" (but if it is still in a good state for such a road) you may add <code>disused:highway=unclassified</code>.</p>
<p>Regarding <span>access</span> tags: apparently everything except some people are forbidden to use this road. I would go for <code>access=private</code>. In addition, if is is well known and somehow obvious that it is tolerated by the city if someone gets around/through the gate, then also use <code>foot=permissive</code> + <code>bicycle=permissive</code> on the way. I would map it as gate - not as fence. It still can be opened by some people!</p>
<p>Map the gate as node of the way. Apply the same access tags to the gate as you used for the way. Maybe also add this tag: <code>description=gate, which is an entrance to a public land, but the city is required by regulations to have this gate closed and locked in front of it. It is trivial for bikes and pedestrians to walk around the gate, although it is impassible by cars.</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Aug '16, 21:48</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Aug '16, 23:29</strong> </span></p>
</div>
</div>
<div id="comments-container-51656" class="comments-container">
&#10;</div>
<div id="comment-tools-51656" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51656-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="51643"></span>

<div id="answer-container-51643" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51643-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51643-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51643-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi mtc, leave the road tagging untouched or ad access=no and ad the fence surrounding the area, with the barrier=gate tag on the road. That the gate is passable (illegally) is not that important, it’s closed or locked access=no. And ad any tag you consider to be usable.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Aug '16, 13:45</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-51643" class="comments-container">
&#10;</div>
<div id="comment-tools-51643" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51643-form-container" class="comment-form-container">
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

