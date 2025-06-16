+++
type = "question"
title = "How to tag a restricted access road"
description = '''A local road has the sign, (at each end) of a red circle with a motor cycle over a car . Underneath is an additional square sign saying &quot; Except for access&quot;. Buses, taxis, cycles and horses are permitted to travel the whole length of the road, by the fact that there is no restriction. I have tagged ...'''
date = "2011-12-01T21:02:00Z"
lastmod = "2011-12-02T00:48:00Z"
weight = 9306
keywords = [ "access", "destination" ]
aliases = [ "/questions/9306" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag a restricted access road](/questions/9306/how-to-tag-a-restricted-access-road)

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
<span id="post-9306-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9306-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-9306-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A local road has the sign, (at each end) of a red circle with a motor cycle over a car . Underneath is an additional square sign saying " Except for access". Buses, taxis, cycles and horses are permitted to travel the whole length of the road, by the fact that there is no restriction. I have tagged this road <em>restriction=access</em> and <em>motor_vehicle = destination</em> but I am not 100% sure that this would be interpreted right by anyone or anything not knowing the area.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-destination" rel="tag" title="see questions tagged &#39;destination&#39;">destination</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Dec '11, 21:02</strong></p>
<img src="https://secure.gravatar.com/avatar/28fda147dcff4f9b5bb79055319a761b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gumpa&#39;s gravatar image" />
<p><span>gumpa</span><br />
<span class="score" title="732 reputation points">732</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gumpa has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9306" class="comments-container">
&#10;</div>
<div id="comment-tools-9306" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9306-form-container" class="comment-form-container">
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

<span id="9309"></span>

<div id="answer-container-9309" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9309-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9309-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-9309-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Assuming you are in the UK: the sign with "a red circle with a motor cycle over a car" does mean "no motor vehicles". The "Except for access" bit means you can use it for access to places alongside the road, where there is no other route.</p>
<p>The "no motor vehicles" sign does apply to buses and taxis, unless there is an exemption specifically for them, or a separate bus lane etc. So they would not be permitted to travel along that road, unless they were going to somewhere along that road.</p>
<p>The correct way to tag this in OSM would <code>motor_vehicle=destination</code>. There is no need for any sort of <code>restriction=</code> tag.</p>
<p>You could also tag <code>bicycle=yes</code>, <code>foot=yes</code>, <code>horse=yes</code>, to specify explicitly that they are allowed. Though this is usually implied by the highway tag, so isn't really necessary.</p>
<p>You could also check the wiki page for <a href="https://wiki.openstreetmap.org/wiki/Road_signs_in_the_United_Kingdom">Road signs in the United Kingdom</a> (though it doesn't currently have an example of "except for access").</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Dec '11, 00:48</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-9309" class="comments-container">
&#10;</div>
<div id="comment-tools-9309" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9309-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9308"></span>

<div id="answer-container-9308" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9308-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9308-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-9308-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>restriction=access isn't the tag you're looking for. access=yes, motor_vehicle=destination is better. Are motorcycles allowed? Not quite clear if you meant bicycles or motorcycles.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Dec '11, 22:54</strong></p>
<img src="https://secure.gravatar.com/avatar/666698a7b13e402aba7e1e0f6de7c1d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baloo%20Uriza&#39;s gravatar image" />
<p><span>Baloo Uriza</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baloo Uriza has 12 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-9308" class="comments-container">
&#10;</div>
<div id="comment-tools-9308" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9308-form-container" class="comment-form-container">
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

