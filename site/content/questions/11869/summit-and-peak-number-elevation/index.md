+++
type = "question"
title = "Summit and Peak Number (Elevation?)"
description = '''The summit icon will often have a number after it. I assume this number is elevation (in meters?). Can someone confirm? This is not explained in the map key (It shows the icon with the description &quot;Summit and Peak&quot;) -- perhaps that should be added? This number is also not documented here: http://wik...'''
date = "2012-04-10T14:10:00Z"
lastmod = "2012-04-11T19:34:00Z"
weight = 11869
keywords = [ "summit", "elevation", "hill", "peak" ]
aliases = [ "/questions/11869" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Summit and Peak Number (Elevation?)](/questions/11869/summit-and-peak-number-elevation)

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
<span id="post-11869-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11869-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11869-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The summit icon will often have a number after it. I assume this number is elevation (in meters?). Can someone confirm? This is not explained in the map key (It shows the icon with the description "Summit and Peak") -- perhaps that should be added?</p>
<p>This number is also not documented here: <a href="https://wiki.openstreetmap.org/wiki/Map_Features#Natural">https://wiki.openstreetmap.org/wiki/Map_Features#Natural</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-summit" rel="tag" title="see questions tagged &#39;summit&#39;">summit</span> <span class="post-tag tag-link-elevation" rel="tag" title="see questions tagged &#39;elevation&#39;">elevation</span> <span class="post-tag tag-link-hill" rel="tag" title="see questions tagged &#39;hill&#39;">hill</span> <span class="post-tag tag-link-peak" rel="tag" title="see questions tagged &#39;peak&#39;">peak</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Apr '12, 14:10</strong></p>
<img src="https://secure.gravatar.com/avatar/141915d97652b4f6c57d12a70f09f9ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pjdevitt&#39;s gravatar image" />
<p><span>pjdevitt</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pjdevitt has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Apr '12, 14:26</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-11869" class="comments-container">
&#10;</div>
<div id="comment-tools-11869" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11869-form-container" class="comment-form-container">
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

<span id="11871"></span>

<div id="answer-container-11871" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11871-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11871-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11871-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As a general point, please make sure to say exactly which map (and layer) you are looking at, because each may have a totally different rendering!</p>
<p>If you are talking about the "default" layer on www.openstreetmap.org, this is governed by <a href="http://svn.openstreetmap.org/applications/rendering/mapnik/osm.xml">this XML stylesheet</a> which contains the section</p>
<pre><code>&lt;Rule&gt;
  &lt;Filter&gt;[natural] = &#39;peak&#39; and not [name] != &#39;&#39;&lt;/Filter&gt;
  &amp;maxscale_zoom14;
  &lt;TextSymbolizer size=&quot;9&quot; fill=&quot;brown&quot; dy=&quot;6&quot; fontset-name=&quot;oblique-fonts&quot; halo-radius=&quot;1&quot; placement=&quot;interior&quot;&gt;[ele]&lt;/TextSymbolizer&gt;
&lt;/Rule&gt;</code></pre>
<p>so yes, indeed, it is the contents of the "ele" tag that are written next to the peak symbol.</p>
<p>It is possible that someone who works on the map key reads this and makes a change directly; otherwise, the best way to request additions to the map key is by submitting a ticket to trac.openstreetmap.org, our bug tracker.<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Apr '12, 14:29</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span> </br></p>
</div>
</div>
<div id="comments-container-11871" class="comments-container">
&#10;</div>
<div id="comment-tools-11871" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11871-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11919"></span>

<div id="answer-container-11919" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11919-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, the elevation listed is in meters.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Apr '12, 19:34</strong></p>
<img src="https://secure.gravatar.com/avatar/666698a7b13e402aba7e1e0f6de7c1d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baloo%20Uriza&#39;s gravatar image" />
<p><span>Baloo Uriza</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baloo Uriza has 12 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-11919" class="comments-container">
&#10;</div>
<div id="comment-tools-11919" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11919-form-container" class="comment-form-container">
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

