+++
type = "question"
title = "Error in exporting roads"
description = '''Hello all, I want to extract all types of roads of an area. But whenever I am trying to export them, it shows the following error: This site can’t be reached The web page at http://api.openstreetmap.org/api/0.6/map?bbox=77.2312,28.5188,77.3184,28.5645 might be temporarily down or it may have moved p...'''
date = "2016-11-29T09:22:00Z"
lastmod = "2016-11-29T09:28:00Z"
weight = 53164
keywords = [ "roads", "extract", "error" ]
aliases = [ "/questions/53164" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error in exporting roads](/questions/53164/error-in-exporting-roads)

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
<span id="post-53164-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53164-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53164-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello all,</p>
<p>I want to extract all types of roads of an area. But whenever I am trying to export them, it shows the following error:</p>
<p>This site can’t be reached</p>
<p>The web page at <a href="http://api.openstreetmap.org/api/0.6/map?bbox=77.2312,28.5188,77.3184,28.5645">http://api.openstreetmap.org/api/0.6/map?bbox=77.2312,28.5188,77.3184,28.5645</a> might be temporarily down or it may have moved permanently to a new web address. ERR_INVALID_RESPONSE</p>
<p>Could anyone please tell me why it is showing this error? Is it server problem or I need to go to some new website of OSM. Any help would be much appreciated.</p>
<p>Thanks &amp; Regards Akanksha</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-roads" rel="tag" title="see questions tagged &#39;roads&#39;">roads</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Nov '16, 09:22</strong></p>
<img src="https://secure.gravatar.com/avatar/9e4edfbdd4e491c40bae098749e107cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AkankshaBalha&#39;s gravatar image" />
<p><span>AkankshaBalha</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AkankshaBalha has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53164" class="comments-container">
&#10;</div>
<div id="comment-tools-53164" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53164-form-container" class="comment-form-container">
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

<span id="53165"></span>

<div id="answer-container-53165" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53165-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53165-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53165-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please do not use the editing API for such downloads, as the name says it is mainly intended for editing.</p>
<p>To export a subset of OSM data for a area you should either use an <a href="http://planet.openstreetmap.org/">extract of the area</a> in question and filter to obtain (please have a look at the <a href="http://wiki.openstreetmap.org">wiki</a> for descriptions of the many tools available) the data that you want or, if the area in question is not too large, use the <a href="http://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Nov '16, 09:28</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Nov '16, 09:37</strong> </span></p>
</div>
</div>
<div id="comments-container-53165" class="comments-container">
&#10;</div>
<div id="comment-tools-53165" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53165-form-container" class="comment-form-container">
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

