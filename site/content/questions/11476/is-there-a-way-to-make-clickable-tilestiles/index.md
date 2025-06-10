+++
type = "question"
title = "Is there a way to make clickable tiles/tiles?"
description = '''Hi there! Is there a way to make clickable tiles? I understand how the Markers work, but what I would like to see is something like an html imagemap, stored in tiles.  For example, for transport map, associate to each bus stop the link to the schedule page.  Is that possible? Thanks!'''
date = "2012-03-23T14:26:00Z"
lastmod = "2013-12-10T15:01:00Z"
weight = 11476
keywords = [ "layers", "clickable", "tiles", "development" ]
aliases = [ "/questions/11476" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a way to make clickable tiles/tiles?](/questions/11476/is-there-a-way-to-make-clickable-tilestiles)

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
<span id="post-11476-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11476-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-11476-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there!</p>
<p>Is there a way to make clickable tiles? I understand how the Markers work, but what I would like to see is something like an html imagemap, stored in tiles.</p>
<p>For example, for transport map, associate to each bus stop the link to the schedule page.</p>
<p>Is that possible?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-layers" rel="tag" title="see questions tagged &#39;layers&#39;">layers</span> <span class="post-tag tag-link-clickable" rel="tag" title="see questions tagged &#39;clickable&#39;">clickable</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Mar '12, 14:26</strong></p>
<img src="https://secure.gravatar.com/avatar/9beb8b503d707bf34136cd4fd51fc49b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="berguina&#39;s gravatar image" />
<p><span>berguina</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="berguina has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Dec '13, 23:09</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-11476" class="comments-container">
&#10;</div>
<div id="comment-tools-11476" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11476-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="11502"></span>

<div id="answer-container-11502" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11502-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11502-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11502-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The easiest solution is to use OpenLayers vectorial features. You can add a marker (even transparent) on each bus stop node, and associated an event to the click on this marker.</p>
<p>So, yes, that is possible :-)</p>
<p>For example, you can try and see the code of <a href="http://pld.dumoulin63.net/">this (so beautifull) map</a>. Each marker is clickable and will display additionnal informations.</p>
<p>Feel free to precise what do you want.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Mar '12, 13:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Mar '12, 09:35</strong> </span></p>
</div>
</div>
<div id="comments-container-11502" class="comments-container">
&#10;</div>
<div id="comment-tools-11502" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11502-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11492"></span>

<div id="answer-container-11492" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11492-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11492-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11492-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As far as I know you cannot store additional information in tile files, because that are just bitmap graphics.</p>
<p>You need an additional source of information when you want to click an object on a tile based map and display information thet is associated with that object.</p>
<p>Have a look for example at the <a href="http://tools.geofabrik.de/osmi/">OSM Inspector</a> by geofabrik.de ... zoom to a smaller area and choose one of the inspector's layers. There you can click on any marked object, and some data is displayed on the right side of the map.</p>
<p>Does that come near your aim? If yes, ask the developers there how they did their work to display that.</p>
<p>Or have a look at <a href="http://www.openstreetbrowser.org">openstreetbrowser</a> .. there you can also click map objects.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Mar '12, 16:32</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Mar '12, 16:33</strong> </span></p>
</div>
</div>
<div id="comments-container-11492" class="comments-container">
&#10;</div>
<div id="comment-tools-11492" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11492-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="28961"></span>

<div id="answer-container-28961" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28961-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28961-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28961-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There was a renderer for Mapnik 2.0, called <a href="https://github.com/mapnik/mapnik/wiki/MetaWriter">Metawriter</a> that would give you the positions of a all labels and POIs enabling you to have a <a href="http://r2d2.stefanm.com/mapnik/demo.html">clickable map (see demo here)</a>. Remember that clickable vector features on the map doesn't have to be visible, you can let the image map tiles be the visual information, and handle the interaction with vector information.</p>
<p>So sorry can't give you a solution that seems viable at the moment, but mapnik 2.0 isn't that old so I hope you have the time to see if metawriter is an option to you..</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Dec '13, 15:01</strong></p>
<img src="https://secure.gravatar.com/avatar/dd3858f5f89f5a6b738f9dbe59824440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emj&#39;s gravatar image" />
<p><span>emj</span><br />
<span class="score" title="2024 reputation points"><span>2.0k</span></span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emj has 11 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Dec '13, 15:07</strong> </span></p>
</div>
</div>
<div id="comments-container-28961" class="comments-container">
&#10;</div>
<div id="comment-tools-28961" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28961-form-container" class="comment-form-container">
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

