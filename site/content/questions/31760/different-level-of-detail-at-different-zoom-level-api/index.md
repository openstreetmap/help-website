+++
type = "question"
title = "Different Level of detail at different zoom level - API"
description = '''My problem: If I want to draw a map of Switzerland, I don&#x27;t need Information about some Recycling station in Zurich. Or put differently: Is there any API that allows to retrieve OSM XML data, but only useful things considering the current zoom level?'''
date = "2014-03-22T14:35:00Z"
lastmod = "2015-12-22T13:56:00Z"
weight = 31760
keywords = [ "api", "level_of_detail", "vector", "zoomlevel" ]
aliases = [ "/questions/31760" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Different Level of detail at different zoom level - API](/questions/31760/different-level-of-detail-at-different-zoom-level-api)

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
<span id="post-31760-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31760-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31760-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My problem: If I want to draw a map of Switzerland, I don't need Information about some Recycling station in Zurich. Or put differently: Is there any API that allows to retrieve OSM XML data, but only useful things considering the current zoom level?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-level_of_detail" rel="tag" title="see questions tagged &#39;level_of_detail&#39;">level_of_detail</span> <span class="post-tag tag-link-vector" rel="tag" title="see questions tagged &#39;vector&#39;">vector</span> <span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Mar '14, 14:35</strong></p>
<img src="https://secure.gravatar.com/avatar/2e1f608951d1a9ab4737e30a993d3d28?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="allestuetsmerweh&#39;s gravatar image" />
<p><span>allestuetsme...</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="allestuetsmerweh has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Mar '14, 14:36</strong> </span></p>
</div>
</div>
<div id="comments-container-31760" class="comments-container">
&#10;</div>
<div id="comment-tools-31760" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31760-form-container" class="comment-form-container">
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

<span id="31761"></span>

<div id="answer-container-31761" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31761-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31761-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-31761-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="allestuetsmerweh has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The answer is essentially: no. Not only would you never find agreement on "useful things considering the current zoom level", we don't have an API that is cabable of returning data (even filtered) for such large areas either (forgeting about the fact that the OSM API is for editing only in any case).</p>
<p>But there is still hope :-)</p>
<p>The correct way to solve your problem is to either to query an XAPI or Overpass API server for the objects that you are actually interested in (assuming that is only a tiny bit of the available data), or get a country level extract of the OSM data from, for example, planet.osm.ch and filter that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Mar '14, 16:51</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Mar '14, 16:54</strong> </span></p>
</div>
</div>
<div id="comments-container-31761" class="comments-container">
<span id="31767"></span>
<div id="comment-31767" class="comment">
<div id="post-31767-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>… of course nothing stops anyone building such an API (maybe there even is somewhere such a thing). And if there would be only one person deciding what to output for each zoomlevel there is no agreement problem.</p>
</div>
<div id="comment-31767-info" class="comment-info">
<span class="comment-age">(22 Mar '14, 19:51)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-31761" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31761-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47265"></span>

<div id="answer-container-47265" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47265-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47265-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47265-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use Maperitive and edit the rendering rules to exclude anything you don't want and to include anything you do want that isn't in the default set of rules.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Dec '15, 13:56</strong></p>
<img src="https://secure.gravatar.com/avatar/7a788e73077afb9faaaa2aec729f2c65?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="apm-wa&#39;s gravatar image" />
<p><span>apm-wa</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="apm-wa has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47265" class="comments-container">
&#10;</div>
<div id="comment-tools-47265" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47265-form-container" class="comment-form-container">
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

