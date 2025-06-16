+++
type = "question"
title = "mountain pass not showing on map"
description = '''Hi! I&#x27;m new in OSM even if I have heard about it previously as an open source supporter. Today I made my first edit but I have a question. I edited the mountain pass at this point of the map: https://www.openstreetmap.org/edit#map=17/43.11804/-3.70322 My intention was to change the real name of the m...'''
date = "2013-10-21T02:29:00Z"
lastmod = "2013-10-21T11:54:00Z"
weight = 27370
keywords = [ "mountain", "pass" ]
aliases = [ "/questions/27370" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [mountain pass not showing on map](/questions/27370/mountain-pass-not-showing-on-map)

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
<span id="post-27370-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27370-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-27370-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi! I'm new in OSM even if I have heard about it previously as an open source supporter. Today I made my first edit but I have a question.</p>
<p>I edited the mountain pass at this point of the map: <a href="https://www.openstreetmap.org/edit#map=17/43.11804/-3.70322">https://www.openstreetmap.org/edit#map=17/43.11804/-3.70322</a></p>
<p>My intention was to change the real name of the mountain pass, but in addition to that, I removed the <strong>tourism=attraction</strong> tag as I guessed that the more precise <strong>mountain_pass=yes</strong> tag was enough. However, now I can't see the point in the map (but I know it is saved because the real name can be used in the search box and it appears when you try to edit the point).</p>
<p>I know that the classic OSM map doesn't show all the information. If I want, as it was before, a mountain pass to appear on this map, must it be tagged as a tourist attraction, even if in reality it's not anything for tourists but quite interesting for this region of the map where there's not too much information at all (it's the countryside)?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mountain" rel="tag" title="see questions tagged &#39;mountain&#39;">mountain</span> <span class="post-tag tag-link-pass" rel="tag" title="see questions tagged &#39;pass&#39;">pass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Oct '13, 02:29</strong></p>
<img src="https://secure.gravatar.com/avatar/dc4468fcb31a40c6ac8b6aca5a0b33c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AnderOSM&#39;s gravatar image" />
<p><span>AnderOSM</span><br />
<span class="score" title="71 reputation points">71</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AnderOSM has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-27370" class="comments-container">
&#10;</div>
<div id="comment-tools-27370" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27370-form-container" class="comment-form-container">
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

<span id="27371"></span>

<div id="answer-container-27371" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27371-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27371-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-27371-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AnderOSM has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Adding tourism=attraction to render it is called <a href="https://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">tagging for the renderer</a> and not done on OSM. The cycle map layer wil eventually show those mountain passes or you can make another <a href="https://trac.openstreetmap.org/ticket/2140">request</a> to render it on the mapnik layer (it has been asked 4 yrs ago but nothing has happened). Another "trick" that I have seen often is adding <a href="https://www.openstreetmap.org/browse/node/80033715">place=locality</a>, this will render on the Mapnik layer.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Oct '13, 08:45</strong></p>
<img src="https://secure.gravatar.com/avatar/0f5ffc3756c4662b9dfad80b7665ac6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ligfietser&#39;s gravatar image" />
<p><span>ligfietser</span><br />
<span class="score" title="2894 reputation points"><span>2.9k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="27 badges"><span class="silver">●</span><span class="badgecount">27</span></span><span title="57 badges"><span class="bronze">●</span><span class="badgecount">57</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ligfietser has 8 accepted answers">11%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Oct '13, 08:50</strong> </span></p>
</div>
</div>
<div id="comments-container-27371" class="comments-container">
<span id="27372"></span>
<div id="comment-27372" class="comment">
<div id="post-27372-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>In case you want to open a bug report then <a href="https://github.com/gravitystorm/openstreetmap-carto/issues">openstreetmap-carto on github</a> would be the correct place.</p>
</div>
<div id="comment-27372-info" class="comment-info">
<span class="comment-age">(21 Oct '13, 09:25)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="27380"></span>
<div id="comment-27380" class="comment">
<div id="post-27380-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Scai, does this mean that reporting bugs on trac.openstreetmap.org is deprecated?</p>
</div>
<div id="comment-27380-info" class="comment-info">
<span class="comment-age">(21 Oct '13, 11:19)</span> <span class="comment-user userinfo">ligfietser</span>
</div>
</div>
<span id="27381"></span>
<div id="comment-27381" class="comment">
<div id="post-27381-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><span></span><span>@ligfietser</span> Not at all. But the new CartoCSS-based stylesheet is hosted on GitHub and the developer prefer to use GitHub's issue tracker. Unfortunately this doesn't work with your regular OSM account.</p>
</div>
<div id="comment-27381-info" class="comment-info">
<span class="comment-age">(21 Oct '13, 11:54)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-27371" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27371-form-container" class="comment-form-container">
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

