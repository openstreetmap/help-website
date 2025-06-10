+++
type = "question"
title = "Postcode boundarys export to SVG"
description = '''Hi folks, I came across OpenStreetMap a couple of weeks ago when looking for an alternative to Google Maps etc. Yesterday, while working on an internal work project I stumbled across the Random Junk post codes map site. This is great as it contains exactly the area detail I need for this project. Ho...'''
date = "2011-12-14T09:42:00Z"
lastmod = "2011-12-14T12:56:00Z"
weight = 9517
keywords = [ "svg", "postcode" ]
aliases = [ "/questions/9517" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Postcode boundarys export to SVG](/questions/9517/postcode-boundarys-export-to-svg)

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
<span id="post-9517-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9517-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-9517-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi folks,</p>
<p>I came across OpenStreetMap a couple of weeks ago when looking for an alternative to Google Maps etc.</p>
<p>Yesterday, while working on an internal work project I stumbled across the <a href="http://random.dev.openstreetmap.org/postcodes/">Random Junk post codes map site</a>. This is great as it contains exactly the area detail I need for this project. However, for the project I'm working on, ideally I need to be able to produce my own mashup of this to produce a heat map of where our staff are located.</p>
<p>Is there any (easy) way to export this data from the site in something like SVG? (As this is a short-term project I won't have access to any fancy editing tools and the like so, painful as it might be to edit, SVG would probably be the best way for me)</p>
<p>thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-svg" rel="tag" title="see questions tagged &#39;svg&#39;">svg</span> <span class="post-tag tag-link-postcode" rel="tag" title="see questions tagged &#39;postcode&#39;">postcode</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Dec '11, 09:42</strong></p>
<img src="https://secure.gravatar.com/avatar/3385d86b4e5e3374d591283915b4abd4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cerebros&#39;s gravatar image" />
<p><span>cerebros</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cerebros has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Dec '11, 12:46</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/dd3858f5f89f5a6b738f9dbe59824440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emj&#39;s gravatar image" />
<p><span>emj</span><br />
<span class="score" title="2024 reputation points"><span>2.0k</span></span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span></p>
</div>
</div>
<div id="comments-container-9517" class="comments-container">
&#10;</div>
<div id="comment-tools-9517" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9517-form-container" class="comment-form-container">
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

<span id="9524"></span>

<div id="answer-container-9524" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9524-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9524-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9524-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suspect these are not the real postcode areas but rather interpolated from the freely available data, so these vectors are most probably not available in Openstreetmap.</p>
<p>Well he does <a href="http://random.dev.openstreetmap.org/postcodes/postcode-code.tar.gz">publish the source code (in python)</a> and you can get SVG from mapnik, or just change the source to generate SVG directly, instead of shapefiles.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Dec '11, 12:56</strong></p>
<img src="https://secure.gravatar.com/avatar/dd3858f5f89f5a6b738f9dbe59824440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emj&#39;s gravatar image" />
<p><span>emj</span><br />
<span class="score" title="2024 reputation points"><span>2.0k</span></span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emj has 11 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Dec '11, 21:37</strong> </span></p>
</div>
</div>
<div id="comments-container-9524" class="comments-container">
&#10;</div>
<div id="comment-tools-9524" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9524-form-container" class="comment-form-container">
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

