+++
type = "question"
title = "River Rendering problem"
description = '''Sorry, I am a newbie to posting so this question might not turn out right. My question concerns the proper rendering of a river. On the OSM web page this river renders correctly at all zoom levels. By that I mean that it is represented as the full river width. But in Garmin BaseCamp (and my Oregon G...'''
date = "2012-07-07T08:47:00Z"
lastmod = "2012-07-08T10:15:00Z"
weight = 14059
keywords = [ "rendering", "riverbank" ]
aliases = [ "/questions/14059" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [River Rendering problem](/questions/14059/river-rendering-problem)

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
<span id="post-14059-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14059-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-14059-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Sorry, I am a newbie to posting so this question might not turn out right. My question concerns the proper rendering of a river. On the OSM web page this river renders correctly at all zoom levels. By that I mean that it is represented as the full river width. But in Garmin BaseCamp (and my Oregon GPSr) when the image is zoomed out the river is just what I would call a schematic rendering just to show the river route. When the image is zoomed in the river is shown at its full width. My question is: "Is this a problem which needs to be corrected in the conversion of the OSM data to GARMIN format or is this a problem that needs to be corrected in the OSM data". In the OSM data there are ways for the riverbanks and they are tagged as Waterway=riverbank but not all of them are closed polygons. I understand from reading other questions that this can cause problems. I Don't have the skills or knowledge (yet) to fix this problem or even to know if it really is a problem. Where would I start? I am using JOSM as an editor.</p>
<p><img src="/upfiles/BCZOUT.JPG" alt="RiverZoomedOUT" /> <img src="/upfiles/BCZIN_1.JPG" alt="RiverZoomedIN" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-riverbank" rel="tag" title="see questions tagged &#39;riverbank&#39;">riverbank</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jul '12, 08:47</strong></p>
<img src="https://secure.gravatar.com/avatar/1e7b4863ad5aaebc818ab4f1056d7d8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sejofgville&#39;s gravatar image" />
<p><span>sejofgville</span><br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sejofgville has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jul '12, 08:49</strong> </span></p>
</div>
</div>
<div id="comments-container-14059" class="comments-container">
&#10;</div>
<div id="comment-tools-14059" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14059-form-container" class="comment-form-container">
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

<span id="14070"></span>

<div id="answer-container-14070" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14070-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14070-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14070-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Based on my experience with Garmin Nuvis and MapSource (... I don't have BaseCamp) it seems to me quite clearly that Garmi renders different stuff even more "liberally" than the tile renderings we see in web maps.</p>
<p>Waterway=riverbanks would all need to be closed polygons and that may (or may not) be part of the problem (perhaps not, because you say that the river delta/ bay area is rendering ok in higher zoom levels.</p>
<p>The thin river is probably just the waterway=river that is supposed to run through the *=riverbank area.</p>
<p>I wouldn't worry about this so long as things show up in either higher zoom levels or/and the Garmin search -- but I would fix the *=riverbank polygons.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jul '12, 03:41</strong></p>
<img src="https://secure.gravatar.com/avatar/280f61ca58a2e8c3d7bc877ed8a3def2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jaakkoh&#39;s gravatar image" />
<p><span>jaakkoh</span><br />
<span class="score" title="548 reputation points">548</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jaakkoh has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-14070" class="comments-container">
&#10;</div>
<div id="comment-tools-14070" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14070-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="14075"></span>

<div id="answer-container-14075" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14075-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14075-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14075-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I like your clear and illustrated question. My Vista HCX and Nuvi 1310t both show the riverbank polygons at all levels.The maps I get for my garmin are of GB from Talkytoaster as I have not managed to render my own yet. Polygons must be joined up,this is what happens when they are broken. <a href="/questions/14009/some-bays-missing-at-zoome-level-6-in-australia">https://help.openstreetmap.org/questions/14009/some-bays-missing-at-zoome-level-6-in-australia</a> I have drawn a lot of the river Great Ouse between Bedford and Ely,I usually create polygons of short sections otherwise edits would take hours and one break will make it all disappear. The old river way line is also required for routing so that must be left in and separate . The rendering you have on your garmin can only show what was downloaded and rendered at that time of course.When drawing a polygon I avoid using the riverbank twice or more times for example riverbank and riverside park polygon as fixing faults are hard, but I find after drawing the riverbank I can then turn off bing and then at high magnifications I can then draw a very close separate line for the park polygon. Hope this is of help.<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jul '12, 10:15</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span> </br></p>
</div>
</div>
<div id="comments-container-14075" class="comments-container">
&#10;</div>
<div id="comment-tools-14075" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14075-form-container" class="comment-form-container">
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

