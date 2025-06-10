+++
type = "question"
title = "Understand the 8 points of encode polyline algorithm"
description = '''I must understand how encode polyline algorithm works and I follow this link: https://developers.google.com/maps/documentation/utilities/polylinealgorithm but I don&#x27;t understand the 8 points?  7)Place the 5-bit chunks into reverse order: 00001 11111 10000 01010 00010 00001 8)OR each value with 0x20 ...'''
date = "2014-10-22T18:16:00Z"
lastmod = "2014-10-23T07:57:00Z"
weight = 37878
keywords = [ "osrm", "polyline", "encoding" ]
aliases = [ "/questions/37878" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Understand the 8 points of encode polyline algorithm](/questions/37878/understand-the-8-points-of-encode-polyline-algorithm)

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
<span id="post-37878-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37878-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37878-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I must understand how encode polyline algorithm works and I follow this link:</p>
<p><a href="https://developers.google.com/maps/documentation/utilities/polylinealgorithm">https://developers.google.com/maps/documentation/utilities/polylinealgorithm</a></p>
<p>but I don't understand the 8 points?</p>
<ul>
<li>7)Place the 5-bit chunks into reverse order: 00001 11111 10000 01010 00010 00001</li>
<li>8)OR each value with 0x20 if another bit chunk follows: 100001 111111 110000 101010 100010 000001</li>
</ul>
<p>what do you mean?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-polyline" rel="tag" title="see questions tagged &#39;polyline&#39;">polyline</span> <span class="post-tag tag-link-encoding" rel="tag" title="see questions tagged &#39;encoding&#39;">encoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Oct '14, 18:16</strong></p>
<img src="https://secure.gravatar.com/avatar/3f61c27a1a925da107eb8c38d3392b6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scupetta18&#39;s gravatar image" />
<p><span>scupetta18</span><br />
<span class="score" title="-3 reputation points">-3</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scupetta18 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Oct '14, 13:34</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-37878" class="comments-container">
&#10;</div>
<div id="comment-tools-37878" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37878-form-container" class="comment-form-container">
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

<span id="37896"></span>

<div id="answer-container-37896" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37896-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37896-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-37896-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm assuming that you understand points 1-6; please say if not.</p>
<p>Point 7 means that you reverse the order of the bytes. In other words, the last should be first, the second-to-last should be second, and so on. A B C D E becomes E D C B A.</p>
<p>Point 8 means that you add 32 (the decimal representation of 0x20, which is a hex value) to all but the last value. This is used as a signal for 'another value follows'.</p>
<p>For most languages, there is a ready-made polylines library that you can use, so you don't have to worry about the intricacies of encoding/decoding yourself. For Ruby: <a href="https://github.com/joshuaclayton/polylines">https://github.com/joshuaclayton/polylines</a>. For JavaScript using Leaflet: <a href="https://github.com/jieter/Leaflet.encoded">https://github.com/jieter/Leaflet.encoded</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Oct '14, 07:57</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-37896" class="comments-container">
&#10;</div>
<div id="comment-tools-37896" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37896-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="37879"></span>

<div id="answer-container-37879" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37879-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37879-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37879-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is an OpenStreetMap help forum. The Google polyline encoding algorithm is not on topic here even if it should be used by some software in conjunction with OSM. <a href="http://gis.stackexchange.com/">GIS Stack Exchange</a> might be a better place to ask your question.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Oct '14, 18:40</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-37879" class="comments-container">
<span id="37895"></span>
<div id="comment-37895" class="comment">
<div id="post-37895-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It's perfectly on topic. Being able to work with the "Google polyline" algorithm is essential for the most popular OSM-based routing software. You may as well close down any questions about tile URLs because the scheme we use for that, too, was invented by Google.</p>
</div>
<div id="comment-37895-info" class="comment-info">
<span class="comment-age">(23 Oct '14, 07:46)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-37879" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37879-form-container" class="comment-form-container">
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

