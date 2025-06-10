+++
type = "question"
title = "Combining coastlines for rendering"
description = '''I&#x27;m writing simple rendering for OSM maps, and I have found that lands border is not one polygon but multiple coastline ways. So my question is how to combine them to one path for rendering? Is there some criteria for combining ways or it is done through relations?'''
date = "2011-10-05T14:49:00Z"
lastmod = "2011-10-05T16:58:00Z"
weight = 8316
keywords = [ "rendering", "osm", "coastline" ]
aliases = [ "/questions/8316" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Combining coastlines for rendering](/questions/8316/combining-coastlines-for-rendering)

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
<span id="post-8316-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8316-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-8316-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm writing simple rendering for OSM maps, and I have found that lands border is not one polygon but multiple coastline ways. So my question is how to combine them to one path for rendering? Is there some criteria for combining ways or it is done through relations?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-coastline" rel="tag" title="see questions tagged &#39;coastline&#39;">coastline</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Oct '11, 14:49</strong></p>
<img src="https://secure.gravatar.com/avatar/c641464433b86cbb086405dbf04d3af1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pastorgluk&#39;s gravatar image" />
<p><span>pastorgluk</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pastorgluk has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Oct '11, 17:53</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/b1d217a3a6e04cf4654372068beef20d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonas_&#39;s gravatar image" />
<p><span>Jonas_</span><br />
<span class="score" title="662 reputation points">662</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span></p>
</div>
</div>
<div id="comments-container-8316" class="comments-container">
&#10;</div>
<div id="comment-tools-8316" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8316-form-container" class="comment-form-container">
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

<span id="8321"></span>

<div id="answer-container-8321" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8321-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8321-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-8321-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I strongly recommend these wiki pages:<br />
<a href="http://wiki.openstreetmap.org/wiki/Coastline">http://wiki.openstreetmap.org/wiki/Coastline</a><br />
<a href="http://wiki.openstreetmap.org/wiki/Coastline_error_checker">http://wiki.openstreetmap.org/wiki/Coastline_error_checker</a></p>
<p>It's explaining how coastline rendering works, why we need special tools to monitor them in OSM and the different type of errors we can find.<br />
But two simple rules to remind : coastlines are not assembled with 'relations' and ways tagged with "<a href="http://wiki.openstreetmap.org/wiki/Tag:natural%3Dcoastline">natural=coastline</a>" have the "water on the right". You may find many coastlines being part of relations but this is mostly for administrative boundaries, never for the coastline itself.<br />
Saying that, the solution for you will depend on which zoom level(s) your simple renderer works. You might also have a look on how the application <a href="http://wiki.openstreetmap.org/wiki/Mkgmap">mkgmap</a> (converting OSM data to Garmin GPS) is <a href="http://wiki.openstreetmap.org/wiki/Mkgmap/help/usage#Sea_generation_options">generating sea polygons</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Oct '11, 16:58</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Oct '11, 16:59</strong> </span></p>
</div>
</div>
<div id="comments-container-8321" class="comments-container">
&#10;</div>
<div id="comment-tools-8321" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8321-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8320"></span>

<div id="answer-container-8320" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8320-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8320-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8320-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One starting point can be here in the OSM wiki:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Coastline">Coastline</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Oct '11, 16:56</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span> </br></br></p>
</div>
</div>
<div id="comments-container-8320" class="comments-container">
&#10;</div>
<div id="comment-tools-8320" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8320-form-container" class="comment-form-container">
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

