+++
type = "question"
title = "[closed] How to show elevation contours in JOSM?"
description = '''I generated an OSM elevation contours file (using srtm2osm, from SRTM data), and want to use that in JOSM as a guide to mapping rivers, but can&#x27;t find any way to make JOSM show the contours. Using JOSM, I downloaded the relevant region from OSM, created a new layer, opened the contours file (which t...'''
date = "2011-01-22T16:24:00Z"
lastmod = "2011-01-26T21:35:00Z"
weight = 2367
keywords = [ "josm", "elevation", "contours", "srtm" ]
aliases = [ "/questions/2367" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] How to show elevation contours in JOSM?](/questions/2367/how-to-show-elevation-contours-in-josm)

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
<span id="post-2367-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2367-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-2367-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I generated an OSM elevation contours file (using srtm2osm, from SRTM data), and want to use that in JOSM as a guide to mapping rivers, but can't find any way to make JOSM show the contours.</p>
<p>Using JOSM, I downloaded the relevant region from OSM, created a new layer, opened the contours file (which took a while to open, because it's a big file) but I can't find any way to make the contours visible. The contours file does appear to be correct, as I successfully used mkgmap to show its contents on my GPS.</p>
<p>So, am I missing something? Or does JOSM deliberately not show elevation contours?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-elevation" rel="tag" title="see questions tagged &#39;elevation&#39;">elevation</span> <span class="post-tag tag-link-contours" rel="tag" title="see questions tagged &#39;contours&#39;">contours</span> <span class="post-tag tag-link-srtm" rel="tag" title="see questions tagged &#39;srtm&#39;">srtm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jan '11, 16:24</strong></p>
<img src="https://secure.gravatar.com/avatar/a8992ad9a83eacdd6388ed265d3f6921?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tongro&#39;s gravatar image" />
<p><span>tongro</span><br />
<span class="score" title="701 reputation points">701</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tongro has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>22 Jan '11, 18:22</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span></p>
</div>
</div>
<div id="comments-container-2367" class="comments-container">
<span id="2465"></span>
<div id="comment-2465" class="comment">
<div id="post-2465-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It's really a Java issue, affecting any Java program, not just JOSM. You specify the memory allocation in the Java command. To allow up to 1GB you would do something like: java -Xmx1000M /usr/share/josm/josm.jar</p>
</div>
<div id="comment-2465-info" class="comment-info">
<span class="comment-age">(26 Jan '11, 21:35)</span> <span class="comment-user userinfo">tongro</span>
</div>
</div>
</div>
<div id="comment-tools-2367" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2367-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "User solved his own issue" by Richard 22 Jan '11, 18:22

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2370"></span>

<div id="answer-container-2370" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2370-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2370-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-2370-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Apologies, it turned out to be a memory issue. The file opening was failing silently. Increasing the Java memory allocation worked.</p>
<p>Matter closed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jan '11, 17:29</strong></p>
<img src="https://secure.gravatar.com/avatar/a8992ad9a83eacdd6388ed265d3f6921?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tongro&#39;s gravatar image" />
<p><span>tongro</span><br />
<span class="score" title="701 reputation points">701</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tongro has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-2370" class="comments-container">
&#10;</div>
<div id="comment-tools-2370" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2370-form-container" class="comment-form-container">
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

