+++
type = "question"
title = "Is it possible to highlight a particular landuse or amenity?"
description = '''Currently seeking cemeteries and graveyards around London. Is it possible to make them stand out more so that they are easier to spot, or make everything else dimmer? Otherwise only visible at high magnification.'''
date = "2017-06-28T17:10:00Z"
lastmod = "2017-06-29T22:21:00Z"
weight = 56794
keywords = [ "amenity", "landuse", "cemetery", "graveyard" ]
aliases = [ "/questions/56794" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to highlight a particular landuse or amenity?](/questions/56794/is-it-possible-to-highlight-a-particular-landuse-or-amenity)

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
<span id="post-56794-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56794-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56794-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Currently seeking cemeteries and graveyards around London. Is it possible to make them stand out more so that they are easier to spot, or make everything else dimmer? Otherwise only visible at high magnification.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span> <span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span> <span class="post-tag tag-link-cemetery" rel="tag" title="see questions tagged &#39;cemetery&#39;">cemetery</span> <span class="post-tag tag-link-graveyard" rel="tag" title="see questions tagged &#39;graveyard&#39;">graveyard</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jun '17, 17:10</strong></p>
<img src="https://secure.gravatar.com/avatar/93b6505600d886cacbdffd435b9a24cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GrahamTD&#39;s gravatar image" />
<p><span>GrahamTD</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GrahamTD has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56794" class="comments-container">
<span id="56804"></span>
<div id="comment-56804" class="comment">
<div id="post-56804-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, don't get any results for amenity=graveyard, so presume it's all landuse=cemetery. Like the way one has to first enter GreaterLondon without a space in the Wizard, and then need to add space in code for query to run.</p>
</div>
<div id="comment-56804-info" class="comment-info">
<span class="comment-age">(29 Jun '17, 16:57)</span> <span class="comment-user userinfo">GrahamTD</span>
</div>
</div>
<span id="56806"></span>
<div id="comment-56806" class="comment">
<div id="post-56806-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If the location has a space in it, you can wrap it in quotes like "Greater London" and the wizard will then handle it properly.</p>
</div>
<div id="comment-56806-info" class="comment-info">
<span class="comment-age">(29 Jun '17, 22:21)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-56794" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56794-form-container" class="comment-form-container">
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

<span id="56795"></span>

<div id="answer-container-56795" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56795-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56795-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-56795-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use Overpass Turbo &amp; <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo/MapCSS">MapCSS</a> to highlight them. Simple example <a href="http://overpass-turbo.eu/s/q3y">here</a>.</p>
<p>Or you can extract them and upload to umap where you have more styling options, but it's <a href="http://www.mappa-mercia.org/2014/09/creating-an-always-up-to-date-map.html">a bit trickier</a> to do an automatically updated map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jun '17, 17:36</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jun '17, 17:42</strong> </span></p>
</div>
</div>
<div id="comments-container-56795" class="comments-container">
&#10;</div>
<div id="comment-tools-56795" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56795-form-container" class="comment-form-container">
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

