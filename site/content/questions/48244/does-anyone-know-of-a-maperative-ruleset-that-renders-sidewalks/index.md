+++
type = "question"
title = "Does anyone know of a Maperative ruleset that renders sidewalks?"
description = '''I&#x27;m looking for a way of rendering highway=*, sidewalk=left/right/both using Maperative. We have quite a few villages on &quot;main&quot; roads that do/don&#x27;t have sidewalks and I would like to render a map so I can check where they have been added etc.'''
date = "2016-02-20T20:54:00Z"
lastmod = "2016-02-22T13:40:00Z"
weight = 48244
keywords = [ "sidewalk", "maperative" ]
aliases = [ "/questions/48244" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Does anyone know of a Maperative ruleset that renders sidewalks?](/questions/48244/does-anyone-know-of-a-maperative-ruleset-that-renders-sidewalks)

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
<span id="post-48244-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48244-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48244-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm looking for a way of rendering highway=*, sidewalk=left/right/both using Maperative. We have quite a few villages on "main" roads that do/don't have sidewalks and I would like to render a map so I can check where they have been added etc.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-sidewalk" rel="tag" title="see questions tagged &#39;sidewalk&#39;">sidewalk</span> <span class="post-tag tag-link-maperative" rel="tag" title="see questions tagged &#39;maperative&#39;">maperative</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Feb '16, 20:54</strong></p>
<img src="https://secure.gravatar.com/avatar/2ecce75f34e449d0ced44bf7aa6d6e06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dud1&#39;s gravatar image" />
<p><span>dud1</span><br />
<span class="score" title="401 reputation points">401</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dud1 has 3 accepted answers">30%</span></p>
</div>
</div>
<div id="comments-container-48244" class="comments-container">
&#10;</div>
<div id="comment-tools-48244" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48244-form-container" class="comment-form-container">
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

<span id="48291"></span>

<div id="answer-container-48291" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48291-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48291-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-48291-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I haven't tried in Maperitive, but I have created experimental sidewalk rendering rules in CartoCSS. The basic idea is to have additional rules for left &amp; right sidewalks (with sidewalk=both triggering both rules) which have the effect of adding an additional casing to a standard highway.</p>
<p>Typically rendering tools such as Maperitive and Mapnik use the Painter's Algorithm to show casings on roads. First you draw a broader line in the colour of the casing &amp; then a narrower line on top in the colour of the fill of the highway. For sidewalks the initial casing should represent the absence of sidewalks. Each rule needs a suitable <a href="http://maperitive.net/docs/Properties/LineOffset.html">line-offset</a>.</p>
<p>In summary the basic rules are:</p>
<ul>
<li>Initial casing, say 10 pixels in light grey</li>
<li>Left sidewalk say 6 pixels in black offset 2 pixels to left (sidewalk=both or sidewalk=left)</li>
<li>Right sidewalk say 6 pixels in black offset 2 pixels to right</li>
<li>Fill, 6 pixels in white.</li>
</ul>
<p>This ought to give a 10 pixel width line with 2 pixel casing on either side, with sidewalks shown in black, and absent sidewalks in grey. You will have to experiment with the precise details of line widths, colours and offsets for various zoom levels.</p>
<p>In my experiments I found that for residential roads I preferred to only show those which lack a pavement (using a red casing to highlight that these might be dangerous). The total number of rules gets very large when combined with other CartoCSS rules.</p>
<p>One other example of sidewalk rendering is described by Tom Change in his <a href="http://tomchance.org/2014/07/15/bringing-pedestrian-maps-to-crystal-palace/">blog</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Feb '16, 13:40</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-48291" class="comments-container">
&#10;</div>
<div id="comment-tools-48291" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48291-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48267"></span>

<div id="answer-container-48267" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48267-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48267-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48267-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I can't help you about Maperitive, but if your goal is to check for completeness of sidewalk tagging, maybe this map by ITO World could be good enough: <a href="http://product.itoworld.com/map/126">http://product.itoworld.com/map/126</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Feb '16, 11:38</strong></p>
<img src="https://secure.gravatar.com/avatar/b75c397321b010a8a70f44ab78e7bb44?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alecs01&#39;s gravatar image" />
<p><span>Alecs01</span><br />
<span class="score" title="1371 reputation points"><span>1.4k</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alecs01 has 6 accepted answers">25%</span></p>
</div>
</div>
<div id="comments-container-48267" class="comments-container">
&#10;</div>
<div id="comment-tools-48267" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48267-form-container" class="comment-form-container">
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

