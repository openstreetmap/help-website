+++
type = "question"
title = "Interface OSM with Excel"
description = '''Bonjour I am a student and I am doing a project about city logistics and I have the next question: Is it possible to write two addresses or coordinates in Excel and get the routing distance between those points from OSM, if yes, how I can do it? '''
date = "2018-12-06T18:28:00Z"
lastmod = "2018-12-06T19:52:00Z"
weight = 67086
keywords = [ "interface", "excel", "routing" ]
aliases = [ "/questions/67086" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Interface OSM with Excel](/questions/67086/interface-osm-with-excel)

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
<span id="post-67086-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67086-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67086-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Bonjour I am a student and I am doing a project about city logistics and I have the next question:</p>
<p>Is it possible to write two addresses or coordinates in Excel and get the routing distance between those points from OSM, if yes, how I can do it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span> <span class="post-tag tag-link-excel" rel="tag" title="see questions tagged &#39;excel&#39;">excel</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Dec '18, 18:28</strong></p>
<img src="https://secure.gravatar.com/avatar/3df5448a409bd28e2b9289284004df52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jrangel&#39;s gravatar image" />
<p><span>Jrangel</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jrangel has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Dec '18, 19:53</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-67086" class="comments-container">
&#10;</div>
<div id="comment-tools-67086" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67086-form-container" class="comment-form-container">
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

<span id="67089"></span>

<div id="answer-container-67089" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67089-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-67089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The most simple way: I guess you could use VBA to query a online routing service (based on OSM).</p>
<ul>
<li>For HTTP requests in VBA see e.g. (just found by simple web search): <a href="http://excelerator.solutions/2017/08/28/excel-http-get-request/">http://excelerator.solutions/2017/08/28/excel-http-get-request/</a></li>
<li>For routing based on OSM see <a href="https://wiki.openstreetmap.org/wiki/Routing">https://wiki.openstreetmap.org/wiki/Routing</a> and <a href="https://wiki.openstreetmap.org/wiki/Develop">https://wiki.openstreetmap.org/wiki/Develop</a> . E.g. use the (for small use) free (of cost) routing API of <a href="https://www.graphhopper.com">https://www.graphhopper.com</a> (which is free software, too, so you could deploy it to your own server)</li>
</ul>
<p>In case you need to convert an address to coordinates (but I guess most Routing APIs can do that for you), have a look at <a href="https://wiki.openstreetmap.org/w/index.php?title=Geocoding">geocoding</a> (this is how it is called).</p>
<p>By the way, nearly everything is possible with OSM - because our data is <a href="https://www.openstreetmap.org/copyright">free</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Dec '18, 19:52</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Dec '18, 20:10</strong> </span></p>
</div>
</div>
<div id="comments-container-67089" class="comments-container">
&#10;</div>
<div id="comment-tools-67089" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67089-form-container" class="comment-form-container">
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

