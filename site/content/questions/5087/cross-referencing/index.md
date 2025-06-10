+++
type = "question"
title = "Cross referencing"
description = '''Silly question perhaps - is there any obvious way to map between an OS MasterMap TOID and an OSM building equivilant i.e. removing the need for using licenced content?'''
date = "2011-05-10T10:19:00Z"
lastmod = "2011-05-10T10:50:00Z"
weight = 5087
keywords = [ "mastermap" ]
aliases = [ "/questions/5087" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Cross referencing](/questions/5087/cross-referencing)

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
<span id="post-5087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5087-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-5087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Silly question perhaps - is there any obvious way to map between an OS MasterMap TOID and an OSM building equivilant i.e. removing the need for using licenced content?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mastermap" rel="tag" title="see questions tagged &#39;mastermap&#39;">mastermap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 May '11, 10:19</strong></p>
<img src="https://secure.gravatar.com/avatar/2c31e1f9d35b1947c23d5a5b1d20f8aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Angusmac&#39;s gravatar image" />
<p><span>Angusmac</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Angusmac has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-5087" class="comments-container">
&#10;</div>
<div id="comment-tools-5087" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5087-form-container" class="comment-form-container">
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

<span id="5089"></span>

<div id="answer-container-5089" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5089-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-5089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Simple answer NO</p>
<p>The longer answer is much more involved, complex, and intriguing. So I can't do it justice here, just a few salient points.</p>
<p>I doubt if anyone has tagged an object in OSM with a <a href="http://en.wikipedia.org/wiki/TOID">TOID</a>, and as OSM contains data sourced from or derived from Ordnance Survey Open Data it's not clear that the conditions of the <a href="http://www.dnf.org/images/uploads/guides/TOID_royalty_free_use_policy_v101.pdf">royalty-free usage policy</a> can be met.</p>
<p>It might be possible to keep a separate database relating OSM object ids to TOIDs. The main problem is that the OSM object ids are not persistent.</p>
<p>Most people rely on spatial location for relating entities from different systems. There is a small amount about this on the <a href="http://wiki.openstreetmap.org/wiki/Conflation">OSM wiki</a></p>
<p>External IDs have been retained for objects in other parts of the world (e.g., <a href="http://wiki.openstreetmap.org/wiki/TIGER">TIGER</a> Line, <a href="http://wiki.openstreetmap.org/wiki/NHD">NHD</a> reach codes), but it is not entirely clear whether this policy was useful. In fact for the TIGER data it is pretty clear that it wasn't. In general I think this has been done "so that we can update the data in the future", whereas the main valid usage is to be able to link the OSM geographical data set with other data (e.g., rainfall, water levels, flow rates, train timetables, traffic volumes etc).</p>
<p>It's conceivable that someone might develop a system for persistent OSM IDs, perhaps for an easily managed subset such as road data. Given OSM's freeform tagging the hard bit is deciding what primitives should be used. The mechanism to manage the persistent IDs (even though that will probably require some manual intervention) is a lot easier to conceive.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 May '11, 10:50</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-5089" class="comments-container">
&#10;</div>
<div id="comment-tools-5089" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5089-form-container" class="comment-form-container">
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

