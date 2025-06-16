+++
type = "question"
title = "How are underground features such as telecommunication cables or water supply pipes represented in OSM base maps?"
description = '''An underground pipeline or cable will sometimes have an access road,which will be represented as a surface feature, but if there is no surface feature, how will it show on the OSM map? Are there Presets for either underground water pipelines, or telecommunication cables?'''
date = "2014-07-23T01:06:00Z"
lastmod = "2014-07-23T05:53:00Z"
weight = 35092
keywords = [ "underground", "pipeline", "telecommunication" ]
aliases = [ "/questions/35092" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How are underground features such as telecommunication cables or water supply pipes represented in OSM base maps?](/questions/35092/how-are-underground-features-such-as-telecommunication-cables-or-water-supply-pipes-represented-in-osm-base-maps)

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
<span id="post-35092-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35092-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35092-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>An underground pipeline or cable will sometimes have an access road,which will be represented as a surface feature, but if there is no surface feature, how will it show on the OSM map? Are there Presets for either underground water pipelines, or telecommunication cables?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-underground" rel="tag" title="see questions tagged &#39;underground&#39;">underground</span> <span class="post-tag tag-link-pipeline" rel="tag" title="see questions tagged &#39;pipeline&#39;">pipeline</span> <span class="post-tag tag-link-telecommunication" rel="tag" title="see questions tagged &#39;telecommunication&#39;">telecommunication</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jul '14, 01:06</strong></p>
<img src="https://secure.gravatar.com/avatar/d9a3d0a3a33f6d86b30b1ea2795bda3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Robert%20Copithorne&#39;s gravatar image" />
<p><span>Robert Copit...</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Robert Copithorne has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jul '14, 01:25</strong> </span></p>
</div>
</div>
<div id="comments-container-35092" class="comments-container">
&#10;</div>
<div id="comment-tools-35092" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35092-form-container" class="comment-form-container">
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

<span id="35093"></span>

<div id="answer-container-35093" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35093-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35093-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-35093-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Key:location">location=underground</a> would seem to be the choice unless in a self supporting structure such as a <a href="https://wiki.openstreetmap.org/wiki/Key:tunnel">tunnel</a>. <a href="https://wiki.openstreetmap.org/wiki/Tag:man_made%3Dpipeline">Tag:man_made=pipeline</a> suggests using location for 'underground', 'underwater' or 'overground' pipes.<br />
<a href="http://taginfo.openstreetmap.org/keys/location#values">Taginfo</a> shows location=underground to be popular.<br />
In special situations <a href="https://wiki.openstreetmap.org/wiki/Key:covered">the key covered</a> may be suitable</p>
<p>How it looks on a map will depend on the rendering scheme used. eg the underground rail shows well on the <a href="https://www.openstreetmap.org/#map=17/-27.46558/153.02422&amp;layers=T">openstreetmap transport layer</a>. I couldn't find an example of comms cables underground.</p>
<p>Note that the <a href="https://wiki.openstreetmap.org/wiki/Key:layer">key layer</a> -1 does not indicate undergound, but instead layer indicates relative position to other objects.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jul '14, 05:53</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jul '14, 06:11</strong> </span></p>
</div>
</div>
<div id="comments-container-35093" class="comments-container">
&#10;</div>
<div id="comment-tools-35093" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35093-form-container" class="comment-form-container">
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

