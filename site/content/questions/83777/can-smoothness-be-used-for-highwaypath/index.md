+++
type = "question"
title = "can smoothness be used for highway=path ?"
description = '''smoothness is well-documented for roads and focuses mostly on the suitability of 4-wheel motor vehicles, but could the tag be also used for highway=path with a focus on 2-wheel motor vehicles? A 4-wheel vehicle will find the smoothness tag sufficient to find out what road may or may not be suitable,...'''
date = "2022-03-10T07:04:00Z"
lastmod = "2022-03-12T16:32:00Z"
weight = 83777
keywords = [ "path", "smoothness", "motorcycle" ]
aliases = [ "/questions/83777" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [can smoothness be used for highway=path ?](/questions/83777/can-smoothness-be-used-for-highwaypath)

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
<span id="post-83777-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83777-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83777-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>smoothness is well-documented for roads and focuses mostly on the suitability of 4-wheel motor vehicles, but could the tag be also used for highway=path with a focus on 2-wheel motor vehicles?</p>
<p>A 4-wheel vehicle will find the smoothness tag sufficient to find out what road may or may not be suitable, so why not use smoothness on highway=path for motorcycle riders?</p>
<p>e.g. very_bad = high clearance (adventure), horrible = heavy-duty off-road (dual sport), very_horrible = specialized off-road (trial), impassable (on foot only)</p>
<p>Context: still looking for a better way to distinguish the suitability of paths for motorcycles in regions where motorcycles are the most common path users:</p>
<ul>
<li>motorcycle:scale is too broad (includes on-road) and too alpine/European centric</li>
<li>mtb:scale could be a good fit for the first few levels but afraid my perception of surface conditions on a motorcycle will not match those of a mountain bike. Any off-road motorcycle riders relying on mtb:scale ?</li>
<li>want to reuse an existing tag supported by outdoor renderers (e.g. tracktype, mtb:scale, sac_scale, and possibly smoothness)</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-path" rel="tag" title="see questions tagged &#39;path&#39;">path</span> <span class="post-tag tag-link-smoothness" rel="tag" title="see questions tagged &#39;smoothness&#39;">smoothness</span> <span class="post-tag tag-link-motorcycle" rel="tag" title="see questions tagged &#39;motorcycle&#39;">motorcycle</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Mar '22, 07:04</strong></p>
<img src="https://secure.gravatar.com/avatar/e3f994b2488e2182c63a7c44a5028ff6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmoffroad&#39;s gravatar image" />
<p><span>cmoffroad</span><br />
<span class="score" title="205 reputation points">205</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmoffroad has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83777" class="comments-container">
&#10;</div>
<div id="comment-tools-83777" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83777-form-container" class="comment-form-container">
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

<span id="83788"></span>

<div id="answer-container-83788" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83788-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83788-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-83788-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Of course you can do that. I do it all the time. And also the <a href="https://wiki.openstreetmap.org/wiki/Key:smoothness">wiki encourages you to do so</a>: <em>The tag can be applied to all drivable ways and areas: highway=</em>, parking areas, beaches, etc.*</p>
<p>Rating a path is of course very subjective but the guidelines on the wiki should give you a rough direction. Just make sure you apply the rules universally to all ways. Don't evaluate smoothly differently on a motorway and a forest trail.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Mar '22, 12:20</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-83788" class="comments-container">
<span id="83803"></span>
<div id="comment-83803" class="comment">
<div id="post-83803-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great. how do you tag a path that is not passable by any 2-wheels? smoothness=impassable ?</p>
</div>
<div id="comment-83803-info" class="comment-info">
<span class="comment-age">(11 Mar '22, 07:59)</span> <span class="comment-user userinfo">cmoffroad</span>
</div>
</div>
<span id="83821"></span>
<div id="comment-83821" class="comment">
<div id="post-83821-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I agree that the wiki is not exactly clear about 2-wheels vehicles, but it does say <code>smoothness=impassable : No wheeled vehicle</code>.</p>
</div>
<div id="comment-83821-info" class="comment-info">
<span class="comment-age">(12 Mar '22, 16:22)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-83788" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83788-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83822"></span>

<div id="answer-container-83822" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83822-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83822-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83822-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I guess you can use <code>smoothness=impassable</code> for your need, but I'm not sure about the router support you'll get.</p>
<p>The <a href="https://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Access_restrictions">default access page</a> (which has no Thailand section, you might want to add one) says that by default motorcycle are not allowed on path. I'm not sure router will support routing motor_vehicles through <code>highway=path</code> in all cases.</p>
<p>Anyway, I feel you might want to invent a new tag, something like <code>passable</code>, with the same structure that of <code>access</code> tags. Of course it's quite a long process to get a new tag approved and then supported, but it might prove better in the long run.</p>
<p>It's always been a problem that the <code>access</code> tags only convey the legal restrictions and not also the physical IMHO. A new way around that would prove useful I think.</p>
<p>Best regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Mar '22, 16:32</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-83822" class="comments-container">
&#10;</div>
<div id="comment-tools-83822" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83822-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83790"></span>

<div id="answer-container-83790" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83790-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83790-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83790-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Or a forest path used as bridleway, for a pedestrian it is bad but for horses, it does not matter.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Mar '22, 13:06</strong></p>
<img src="https://secure.gravatar.com/avatar/f367bf86ca89f96671e410e642a3664b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Teek&#39;s gravatar image" />
<p><span>Teek</span><br />
<span class="score" title="63 reputation points">63</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Teek has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83790" class="comments-container">
&#10;</div>
<div id="comment-tools-83790" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83790-form-container" class="comment-form-container">
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

