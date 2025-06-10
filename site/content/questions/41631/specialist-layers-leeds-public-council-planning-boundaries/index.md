+++
type = "question"
title = "Specialist layers (Leeds public council planning boundaries)"
description = '''Hi, I&#x27;ve recently signed up and added/edited a few public amenities in my area. I&#x27;m writing an app that will show all of Leeds City Council&#x27;s Site Allocations sites, and I wanted to make this data available publicly here. How might I go about adding areas that won&#x27;t render on a &#x27;normal&#x27; map but can ...'''
date = "2015-03-11T09:12:00Z"
lastmod = "2015-03-16T07:00:00Z"
weight = 41631
keywords = [ "layers", "specialist", "planning", "openlayers", "council" ]
aliases = [ "/questions/41631" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Specialist layers (Leeds public council planning boundaries)](/questions/41631/specialist-layers-leeds-public-council-planning-boundaries)

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
<span id="post-41631-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41631-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-41631-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I've recently signed up and added/edited a few public amenities in my area.</p>
<p>I'm writing an app that will show all of Leeds City Council's Site Allocations sites, and I wanted to make this data available publicly here. How might I go about adding areas that won't render on a 'normal' map but can be viewed by interested parties? Is this something I <em>should</em> add to OpenStreetMap at all in the first place, or should I maintain these sites in my app and superimpose them on an embedded map?</p>
<p>Many thanks,</p>
<p>Russell</p>
<p>EDIT: for clarity, the data is at <a href="https://github.com/rgarner/lcc-site-allocations-data/">https://github.com/rgarner/lcc-site-allocations-data/</a> - these are real sites, identified as possible candidates for city building. The app attempts to increase public engagement with the process, so these areas have a shelf life - but the consultation that decides what sites get allocated is this year. My first thought was to have these live specifically within the app, but they may have wider interest in this period.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-layers" rel="tag" title="see questions tagged &#39;layers&#39;">layers</span> <span class="post-tag tag-link-specialist" rel="tag" title="see questions tagged &#39;specialist&#39;">specialist</span> <span class="post-tag tag-link-planning" rel="tag" title="see questions tagged &#39;planning&#39;">planning</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-council" rel="tag" title="see questions tagged &#39;council&#39;">council</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Mar '15, 09:12</strong></p>
<img src="https://secure.gravatar.com/avatar/31c27078e3ee6e6332b5a7f14607975e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rgarner&#39;s gravatar image" />
<p><span>rgarner</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rgarner has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Mar '15, 10:13</strong> </span></p>
</div>
</div>
<div id="comments-container-41631" class="comments-container">
&#10;</div>
<div id="comment-tools-41631" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41631-form-container" class="comment-form-container">
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

<span id="41729"></span>

<div id="answer-container-41729" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41729-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41729-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-41729-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rgarner has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap doesn't usually collect data that is not verifiable <a href="http://wiki.openstreetmap.org/wiki/Verifiability">(wiki link)</a> on the ground. There are some exceptions - for example, we do have administrative boundaries, but we certainly draw the line at land parcels. It is hard for me to say where your site allocation data falls but my hunch is that it is not something we'd like to see in OSM.</p>
<p>In that case, probably the best technology would be using <a href="http://umap.openstreetmap.fr">uMap</a> where you can draw things (or have things drawn) on top of an OpenStreetMap basemap while still keeping both data sets separate - or, of course, superimpose things on top of OSM in your app.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Mar '15, 06:49</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Mar '15, 06:51</strong> </span></p>
</div>
</div>
<div id="comments-container-41729" class="comments-container">
<span id="41730"></span>
<div id="comment-41730" class="comment">
<div id="post-41730-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>That's an excellent answer. Thank you Frederik.</p>
</div>
<div id="comment-41730-info" class="comment-info">
<span class="comment-age">(16 Mar '15, 07:00)</span> <span class="comment-user userinfo">rgarner</span>
</div>
</div>
</div>
<div id="comment-tools-41729" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41729-form-container" class="comment-form-container">
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

