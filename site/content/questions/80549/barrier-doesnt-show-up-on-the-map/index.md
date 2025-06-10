+++
type = "question"
title = "Barrier doesn&#x27;t show up on the map"
description = '''Hi, I&#x27;m trying to add barriers on a path but they don&#x27;t show up on the map: https://www.openstreetmap.org/node/8812448665 https://www.openstreetmap.org/node/8812448662 Any reason why?'''
date = "2021-06-13T18:23:00Z"
lastmod = "2021-06-13T20:57:00Z"
weight = 80549
keywords = [ "barrier" ]
aliases = [ "/questions/80549" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Barrier doesn't show up on the map](/questions/80549/barrier-doesnt-show-up-on-the-map)

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
<span id="post-80549-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80549-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80549-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm trying to add barriers on a path but they don't show up on the map:</p>
<p><a href="https://www.openstreetmap.org/node/8812448665">https://www.openstreetmap.org/node/8812448665</a></p>
<p><a href="https://www.openstreetmap.org/node/8812448662">https://www.openstreetmap.org/node/8812448662</a></p>
<p>Any reason why?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-barrier" rel="tag" title="see questions tagged &#39;barrier&#39;">barrier</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jun '21, 18:23</strong></p>
<img src="https://secure.gravatar.com/avatar/080710b0dbc03a34bc0792a1e29ed5ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nryc&#39;s gravatar image" />
<p><span>nryc</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nryc has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80549" class="comments-container">
&#10;</div>
<div id="comment-tools-80549" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80549-form-container" class="comment-form-container">
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

<span id="80551"></span>

<div id="answer-container-80551" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80551-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80551-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80551-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello,</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Tag:barrier%3Dwall">barrier=wall</a> is meant for ways (lines). Like when a wall enclose a garden, or anything.</p>
<p>To mark a barrier on a path, you have to look at <a href="https://wiki.openstreetmap.org/wiki/Key:barrier#Access_control_on_highways_.28e.g._for_blocking_a_path_or_road.29">this list</a> of point barriers to find one that match the ground.</p>
<p>For 8812448665, I see a barrier=chain, and for 8812448662 I can't see anything, except signage.</p>
<p>Also, from what I see, it's not access=no, but more like motor_vehicle=no (already specified on the ways) and bicycle=no (which is contrary to what's specified on the ways). So you should also modify the ways, so the routers know about the restriction.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jun '21, 19:23</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-80551" class="comments-container">
<span id="80552"></span>
<div id="comment-80552" class="comment">
<div id="post-80552-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It's a temporary wall, around 3 meters high, as wide as the path, made of sheet metal that prevents access from anyone (pedestrians included).</p>
<p>Should I go with <code>barrier=block</code>?</p>
</div>
<div id="comment-80552-info" class="comment-info">
<span class="comment-age">(13 Jun '21, 19:43)</span> <span class="comment-user userinfo">nryc</span>
</div>
</div>
<span id="80554"></span>
<div id="comment-80554" class="comment">
<div id="post-80554-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Alright, I get it now. ;-)</p>
<p>I'm afraid I've got no better idea, only barrier=yes, simple and unspecific... You could add material=metal, just for fun.</p>
<p>You should also add a note or description tag, so that other mappers (note) or users (description) will understand that it's a temporary measure, and recent so not visible on imagery and such.</p>
</div>
<div id="comment-80554-info" class="comment-info">
<span class="comment-age">(13 Jun '21, 20:18)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="80556"></span>
<div id="comment-80556" class="comment">
<div id="post-80556-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Unfortunately, <code>barrier=yes</code> is still not showing up on the map.</p>
</div>
<div id="comment-80556-info" class="comment-info">
<span class="comment-age">(13 Jun '21, 20:32)</span> <span class="comment-user userinfo">nryc</span>
</div>
</div>
<span id="80558"></span>
<div id="comment-80558" class="comment">
<div id="post-80558-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, it seems to be on purpose (<a href="https://www.gitmemory.com/issue/gravitystorm/openstreetmap-carto/4229/718939078).">https://www.gitmemory.com/issue/gravitystorm/openstreetmap-carto/4229/718939078).</a></p>
<p>You could map the wall as a line, few meters long, across the path. It would display as a thick line. But I'm not sure it will block routers though. Or you just cut the path under the wall...</p>
<p>Maybe barrier=block is the best option, even if it could be called tagging for the renderer.</p>
<p>Or you could relaunch the discussion on the subject of barrier=wall on node objects, but I'm sure I've read it several times before, with no good conclusion... ;-)</p>
<p>Sorry for the lack of good options.</p>
</div>
<div id="comment-80558-info" class="comment-info">
<span class="comment-age">(13 Jun '21, 20:57)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-80551" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80551-form-container" class="comment-form-container">
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

