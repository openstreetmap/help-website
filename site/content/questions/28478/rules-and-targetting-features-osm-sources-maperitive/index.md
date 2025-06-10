+++
type = "question"
title = "Rules and targetting features / OSM sources / Maperitive"
description = '''A new user to Maperitive and OSM, I&#x27;m looking to render a map based on a custom ruleset, I understand how to create the ruleset based on tutorials from other blogs but do not appear to get results i expect so want to check i have this workflow / process correct. Brief introduction: My understanding ...'''
date = "2013-11-26T11:50:00Z"
lastmod = "2013-11-26T17:23:00Z"
weight = 28478
keywords = [ "rules", "rendering", "xapi", "maperitive", "overpass" ]
aliases = [ "/questions/28478" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Rules and targetting features / OSM sources / Maperitive](/questions/28478/rules-and-targetting-features-osm-sources-maperitive)

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
<span id="post-28478-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28478-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28478-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A new user to Maperitive and OSM,</p>
<p>I'm looking to render a map based on a custom ruleset, I understand how to create the ruleset based on tutorials from other blogs but do not appear to get results i expect so want to check i have this workflow / process correct.</p>
<p>Brief introduction: My understanding of the process required to render a map based on custom rules</p>
<ol>
<li>Define approximate area of interest on maperative via geometry bounds</li>
<li>Create the ruleset; testing on a very simple one which pulls in roads and universities/hospitals only based on tags <em>roads</em> amenity *healthcare</li>
<li>Download OSM data, maperitive pulls in data for tags <em>roads</em> amenity *healthcare and renders them to colours widths defined:</li>
<li>Generate and render map; rendered map should be returned showing only items that have been tagged as road amenity healthcare</li>
</ol>
<p>Is that understanding right, am new to code generally so feeling quite overwhelmed on the learning curve required just to create the ruleset! My end map would ideally have the city with all buildings/roads/features but universities picked out in a separate bright red colour based on my ruleset which has turned off all the other labels and colours to focus the map on just those facilities. All/any help really greatfully appreciated</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rules" rel="tag" title="see questions tagged &#39;rules&#39;">rules</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-xapi" rel="tag" title="see questions tagged &#39;xapi&#39;">xapi</span> <span class="post-tag tag-link-maperitive" rel="tag" title="see questions tagged &#39;maperitive&#39;">maperitive</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Nov '13, 11:50</strong></p>
<img src="https://secure.gravatar.com/avatar/36aa2b875ec68892cba01c4b95e246f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dominijk&#39;s gravatar image" />
<p><span>dominijk</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dominijk has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Nov '13, 12:40</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-28478" class="comments-container">
&#10;</div>
<div id="comment-tools-28478" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28478-form-container" class="comment-form-container">
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

<span id="28498"></span>

<div id="answer-container-28498" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28498-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28498-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-28498-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Some hints are also inside the OSM wiki about <a href="http://wiki.openstreetmap.org/wiki/Maperitive">Maperitive</a> ... there are links to a HowTo etc.</p>
<p>For detailed questions I would recommend the Maperitive googlegroup mailinglist.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Nov '13, 17:23</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-28498" class="comments-container">
&#10;</div>
<div id="comment-tools-28498" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28498-form-container" class="comment-form-container">
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

