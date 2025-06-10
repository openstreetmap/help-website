+++
type = "question"
title = "OSM calculation tolerance"
description = '''Good afternoon. I am working with OpenStreetMaps and I would like to know what is the tolerance for measuring distances between coordinates with OSM. Is there any article or website where I could find this tolerance specification? Thanks in advance.'''
date = "2021-10-26T14:37:00Z"
lastmod = "2021-10-27T09:58:00Z"
weight = 82376
keywords = [ "distance", "measure" ]
aliases = [ "/questions/82376" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [OSM calculation tolerance](/questions/82376/osm-calculation-tolerance)

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
<span id="post-82376-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82376-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82376-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Good afternoon.</p>
<p>I am working with OpenStreetMaps and I would like to know what is the tolerance for measuring distances between coordinates with OSM. Is there any article or website where I could find this tolerance specification?</p>
<p>Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span> <span class="post-tag tag-link-measure" rel="tag" title="see questions tagged &#39;measure&#39;">measure</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Oct '21, 14:37</strong></p>
<img src="https://secure.gravatar.com/avatar/eacc3f06e856ac0f1329214b0ff3b7eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Migueltm_22&#39;s gravatar image" />
<p><span>Migueltm_22</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Migueltm_22 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82376" class="comments-container">
&#10;</div>
<div id="comment-tools-82376" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82376-form-container" class="comment-form-container">
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

<span id="82386"></span>

<div id="answer-container-82386" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82386-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82386-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-82386-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are numerous published studies going back over 10 years (for instance, <a href="https://www.ucl.ac.uk/~ucfamha/OSM%20data%20analysis%20070808_web_orig.pdf)">https://www.ucl.ac.uk/~ucfamha/OSM%20data%20analysis%20070808_web_orig.pdf)</a> comparing OSM road networks with alternative (usually official) sources. For Western Europe it's probably reasonable to assume highways are within 10 m of their true location. It's entirely possible that most may be within 5 m or better. I don't have a feel for other parts of the world: imagery offsets in places like Africa may result in quite large discrepancies.</p>
<p>Less attention has been paid to other data such as buildings. I did look at one set of boundaries <a href="http://sk53-osm.blogspot.com/2015/12/how-accurately-have-townlands-in.html">http://sk53-osm.blogspot.com/2015/12/how-accurately-have-townlands-in.html</a> using a fairly simple approach.</p>
<p>Broadly OSM prizes topological accuracy above spatial accuracy, and for users of consumer grade GPS 5-10m discrepancies are not usually noticeable.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Oct '21, 09:58</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-82386" class="comments-container">
&#10;</div>
<div id="comment-tools-82386" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82386-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82377"></span>

<div id="answer-container-82377" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82377-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82377-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-82377-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Generally it's whatever the contributor feels like, refined iteratively by subsequent contributors. There is no "specification" as such - you can't specify what volunteers might or might not want to do.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Oct '21, 15:15</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-82377" class="comments-container">
&#10;</div>
<div id="comment-tools-82377" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82377-form-container" class="comment-form-container">
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

