+++
type = "question"
title = "How should a farm be tagged?"
description = '''The wiki entry for farm suggests that the main farm buildings should be tagged with landuse=farmyard with the surrounding fields tagged as landuse=farm or landuse=farmland  However I see that there is a place=farm tag suggested in the wiki so when should this be used? Experimenting shows that Mapnik...'''
date = "2010-07-30T10:58:00Z"
lastmod = "2010-08-03T16:17:00Z"
weight = 504
keywords = [ "best-practise", "tagging" ]
aliases = [ "/questions/504" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How should a farm be tagged?](/questions/504/how-should-a-farm-be-tagged)

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
<span id="post-504-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-504-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-504-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The <a href="http://wiki.openstreetmap.org/wiki/Farm" title="Farm - OpenSteetMap Wiki">wiki entry for farm</a> suggests that the main farm buildings should be tagged with <code>landuse=farmyard</code> with the surrounding fields tagged as <code>landuse=farm</code> or <code>landuse=farmland</code></p>
<p><img src="http://wiki.openstreetmap.org/w/images/thumb/8/86/Landuse%3Dfarmyard.jpg/500px-Landuse%3Dfarmyard.jpg" alt="Farmward depiction from Wiki" /></p>
<p>However I see that there is a <a href="http://wiki.openstreetmap.org/wiki/Tag:place%3Dfarm"><code>place=farm</code> tag suggested in the wiki</a> so when should this be used?</p>
<p>Experimenting shows that Mapnik does not render <code>place=farm</code>, but Osmarender does. Both render <code>landuse=farmyard</code> and display a name at close zoom levels.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-best-practise" rel="tag" title="see questions tagged &#39;best-practise&#39;">best-practise</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jul '10, 10:58</strong></p>
<img src="https://secure.gravatar.com/avatar/f61876d1f1d2de794259119cdd596316?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GrahamS&#39;s gravatar image" />
<p><span>GrahamS</span><br />
<span class="score" title="3635 reputation points"><span>3.6k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="45 badges"><span class="silver">●</span><span class="badgecount">45</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GrahamS has 7 accepted answers">28%</span></p>
</img>
</div>
</div>
<div id="comments-container-504" class="comments-container">
&#10;</div>
<div id="comment-tools-504" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-504-form-container" class="comment-form-container">
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

<span id="537"></span>

<div id="answer-container-537" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-537-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-537-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-537-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="GrahamS has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use <a href="http://wiki.openstreetmap.org/wiki/Tag:landuse%3Dfarmyard">landuse=farmyard</a> with a polygon around the general area of the clutch of buildings making up a farm. You might then also do a few building=yes polygons for individual buildings if you have a way of mapping those accurately. That's pretty similar to how we map several buildings making up a school or a hospital.</p>
<p>place=farm is confusing (and I must say I disagreed with its addition in the first place) but it's part of the family of tags on <a href="http://wiki.openstreetmap.org/wiki/Key:place">Key:place</a> which are for naming an area. So for example an area is known by the locals as "Upperknowle Farm". In fact there doesn't necessarily need to be an active farm there, or any buildings whatsoever. These can be labels for bits of moorland traced from old out of copyright maps for example, and maybe that's the best time to use it.</p>
<p>If you have an active visible farm with a particular name, I'd say it's better to tag it landuse=farmyard, name=x ...and forget about the place tag.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Aug '10, 12:52</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Aug '10, 14:26</strong> </span></p>
</div>
</div>
<div id="comments-container-537" class="comments-container">
<span id="550"></span>
<div id="comment-550" class="comment">
<div id="post-550-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah, from my experimenting I'd have to agree. Thanks Harry.</p>
</div>
<div id="comment-550-info" class="comment-info">
<span class="comment-age">(03 Aug '10, 10:29)</span> <span class="comment-user userinfo">GrahamS</span>
</div>
</div>
</div>
<div id="comment-tools-537" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-537-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="505"></span>

<div id="answer-container-505" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-505-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-505-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-505-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If I understand that wiki page correctly <code>place=farm</code> is used to mark a farm that is considered it's own - well - place like a village or hamlet. I'd use it (additionally to <code>landuse=farmyard</code>) if it has a name that is also used as it's address.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jul '10, 11:07</strong></p>
<img src="https://secure.gravatar.com/avatar/c8367f123240268431ceae261af0dac9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RoToRa&#39;s gravatar image" />
<p><span>RoToRa</span><br />
<span class="score" title="88 reputation points">88</span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RoToRa has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-505" class="comments-container">
<span id="506"></span>
<div id="comment-506" class="comment">
<div id="post-506-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The OS OpenData in the UK usually has farm names on it and it is very common for these to be used as the farm address. But if I tag a node place=farm AND mark the area as landuse=farmyward, and give them both names, then they will both be rendered in Osmarender which doesn't look right.</p>
</div>
<div id="comment-506-info" class="comment-info">
<span class="comment-age">(30 Jul '10, 11:15)</span> <span class="comment-user userinfo">GrahamS</span>
</div>
</div>
<span id="508"></span>
<div id="comment-508" class="comment">
<div id="post-508-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I actually thought to tag the area with both and not add an additional node.</p>
</div>
<div id="comment-508-info" class="comment-info">
<span class="comment-age">(30 Jul '10, 11:38)</span> <span class="comment-user userinfo">RoToRa</span>
</div>
</div>
<span id="509"></span>
<div id="comment-509" class="comment">
<div id="post-509-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okay I've just tried tagging the same area with place=farm and landuse=farmyard. That looks okay in Mapnik, but in Osmarender it renders the name twice. Once in large black text and again in smaller blue text, with the blue text rendered directly on top of the black.</p>
</div>
<div id="comment-509-info" class="comment-info">
<span class="comment-age">(30 Jul '10, 12:18)</span> <span class="comment-user userinfo">GrahamS</span>
</div>
</div>
<span id="554"></span>
<div id="comment-554" class="comment">
<div id="post-554-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>That would be a bug in Osmarender then.</p>
</div>
<div id="comment-554-info" class="comment-info">
<span class="comment-age">(03 Aug '10, 16:17)</span> <span class="comment-user userinfo">RoToRa</span>
</div>
</div>
</div>
<div id="comment-tools-505" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-505-form-container" class="comment-form-container">
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

