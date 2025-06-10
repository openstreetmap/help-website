+++
type = "question"
title = "Building footprints"
description = '''Hi, This may be a basic task, but I&#x27;m unfamiliar with OSM. I would like to export 2D building footprints from OSM so I can eventually convert them to 3D in GRASS. But I&#x27;m not seeing any footprints? '''
date = "2013-07-14T15:31:00Z"
lastmod = "2013-07-15T01:05:00Z"
weight = 24229
keywords = [ "2d", "footprints", "buildings" ]
aliases = [ "/questions/24229" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Building footprints](/questions/24229/building-footprints)

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
<span id="post-24229-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24229-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24229-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, This may be a basic task, but I'm unfamiliar with OSM. I would like to export 2D building footprints from OSM so I can eventually convert them to 3D in GRASS. But I'm not seeing any footprints?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-2d" rel="tag" title="see questions tagged &#39;2d&#39;">2d</span> <span class="post-tag tag-link-footprints" rel="tag" title="see questions tagged &#39;footprints&#39;">footprints</span> <span class="post-tag tag-link-buildings" rel="tag" title="see questions tagged &#39;buildings&#39;">buildings</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jul '13, 15:31</strong></p>
<img src="https://secure.gravatar.com/avatar/f2eac8911e5803edfa456affcb2a2347?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pilbeam&#39;s gravatar image" />
<p><span>Pilbeam</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pilbeam has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24229" class="comments-container">
<span id="24233"></span>
<div id="comment-24233" class="comment">
<div id="post-24233-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You could draw them yourself. The Bing images need to be good enough in the area in question though. The wiki will give you some help on how to do it. sorry I have not tried to export building footprints so can't help on that.</p>
</div>
<div id="comment-24233-info" class="comment-info">
<span class="comment-age">(14 Jul '13, 17:35)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-24229" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24229-form-container" class="comment-form-container">
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

<span id="24241"></span>

<div id="answer-container-24241" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24241-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24241-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-24241-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You cannot export what is not in the OSM database! So, if you can't see the building outlines in your area of interest, no one drew them yet. As said by "andy mackey" in one of the comments, you could draw them yourself. I did this for some neighbourhoods in São Paulo, Brazil and São Bernardo do Campo, Brazil, and I can say it is very, very tedious to do. Please see also <a href="http://wiki.openstreetmap.org/wiki/Simple_3D_Buildings">Simple 3D Buildings</a></p>
<p>After the buildings are on the map you could extract the area of interest, filtering by the building=* tag, for example, using <a href="http://wiki.openstreetmap.org/wiki/Osmfilter">osmfilter</a>, and then do other steps as neeeded.</p>
<p>Another way would be importing the complete extract of the area of interest into a PostGIS database and then filtering (via SQL query) by the desired tags. This approach has the advantage of returning geometry objects that (maybe) other software can use directly.</p>
<p>Please note that very few buildings have info on height, ceiling type, etc., complicating things even more.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jul '13, 01:05</strong></p>
<img src="https://secure.gravatar.com/avatar/94b019f273c04cd88bc1c8dd0a8f2161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MCPicoli&#39;s gravatar image" />
<p><span>MCPicoli</span><br />
<span class="score" title="2172 reputation points"><span>2.2k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MCPicoli has 10 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-24241" class="comments-container">
&#10;</div>
<div id="comment-tools-24241" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24241-form-container" class="comment-form-container">
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

