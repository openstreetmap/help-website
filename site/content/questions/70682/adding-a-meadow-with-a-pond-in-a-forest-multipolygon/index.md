+++
type = "question"
title = "Adding a meadow with a pond in a forest - Multipolygon"
description = '''Hello everyone,  In many cases, forest surfaces described by polygons of more or less complex shapes, also contain other surfaces not currently described in OSM. This may be for example a meadow in the middle of the forest which may in some cases include another surface such as a small pond. An exam...'''
date = "2019-09-08T10:37:00Z"
lastmod = "2019-09-09T10:22:00Z"
weight = 70682
keywords = [ "surface", "multipolygon" ]
aliases = [ "/questions/70682" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Adding a meadow with a pond in a forest - Multipolygon](/questions/70682/adding-a-meadow-with-a-pond-in-a-forest-multipolygon)

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
<span id="post-70682-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70682-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-70682-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone,</p>
<p>In many cases, forest surfaces described by polygons of more or less complex shapes, also contain other surfaces not currently described in OSM. This may be for example a meadow in the middle of the forest which may in some cases include another surface such as a small pond.</p>
<p>An example showing grasslands not yet represented in OSM within the forest, is given below.</p>
<p><a href="https://www.openstreetmap.org/edit#map=17/48.74253/2.07390">https://www.openstreetmap.org/edit#map=17/48.74253/2.07390</a></p>
<p>I wonder, however, about the best procedure for mapping these areas: I noticed that, in some cases, grasslands, or even water surfaces in these grasslands, were simply added to the surface of the forest (Link to case 1 below). In fact the surfaces are added to each other.</p>
<p><a href="https://www.openstreetmap.org/#map=18/48.72057/2.02757">https://www.openstreetmap.org/#map=18/48.72057/2.02757</a></p>
<p>Is this procedure acceptable? if this procedure is not correct, what is the best way to correct the case 1. Should not we rather use Multipolygon especially when these small areas are numerous? Or use separate small individual polygons to describe each surface?</p>
<p>Regards,<br />
Gerard C.<br />
FRANCE</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-surface" rel="tag" title="see questions tagged &#39;surface&#39;">surface</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Sep '19, 10:37</strong></p>
<img src="https://secure.gravatar.com/avatar/0988e493aea326d0b812364f41b1fc43?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Woinic&#39;s gravatar image" />
<p><span>Woinic</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Woinic has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-70682" class="comments-container">
&#10;</div>
<div id="comment-tools-70682" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70682-form-container" class="comment-form-container">
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

<span id="70687"></span>

<div id="answer-container-70687" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70687-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70687-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-70687-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Good question, but not easily unanswerable, at least not without debate. If you search the mailing lists and forums you will find endless debates around it. Maybe a few facts:</p>
<p>Actually, there are (at least) three different tags to describe landscapes: landuse=*, landcover=* and natural=*. In their strict meaning the former two are orthogonal and could be both used on the same object. In tagging practice landuse often also carries a landcover meaning. On top landcover is ignored by most renderers today and hence not very popular among mappers.</p>
<p>Now, should a pond as an example be part of a forest? Some argue it is part of the forest and hence we just draw it and a forest around it. Some say, where the pond is forest must end and create a multipolygon for the forest with the pond as an inner. You could also have a large forest (in the meaning: This is an area where mainly trees grow that are used for timber) and somewhere in there there is a patch with landcover=grass (where the game comes out to feed and keeps new trees from growing).</p>
<p>I'd say both practices were quite common until a few years ago when the standard map on openstreetmap.org changed the rendering. At that time they started drawing little trees on top of the water if the pond was not cut out of the forest. Since then mappers are more favoring the multipolygon approach.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Sep '19, 08:06</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Sep '19, 10:22</strong> </span></p>
</div>
</div>
<div id="comments-container-70687" class="comments-container">
&#10;</div>
<div id="comment-tools-70687" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70687-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="70689"></span>

<div id="answer-container-70689" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70689-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70689-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70689-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi woinic, Did you read these lines <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon">https://wiki.openstreetmap.org/wiki/Relation:multipolygon</a> ? Its is getting complicated when the wet area has no border to the surroundings and is embedded. Just start a new Multi. And dont choose a way just to get it visual, as far as I can remember "dont map for the renderer" !</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Sep '19, 09:38</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-70689" class="comments-container">
<span id="70692"></span>
<div id="comment-70692" class="comment">
<div id="post-70692-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi,<br />
I have so far only consulted the information given below.<br />
<a href="https://wiki.openstreetmap.org/wiki/Multipolygon_Examples">https://wiki.openstreetmap.org/wiki/Multipolygon_Examples</a></p>
<p>I will read this other information.</p>
<p>Regards,<br />
Gerard C.</p>
</div>
<div id="comment-70692-info" class="comment-info">
<span class="comment-age">(09 Sep '19, 10:22)</span> <span class="comment-user userinfo">Woinic</span>
</div>
</div>
</div>
<div id="comment-tools-70689" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70689-form-container" class="comment-form-container">
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

