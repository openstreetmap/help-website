+++
type = "question"
title = "How to obtain a bounding box for use with OSM tools"
description = '''There are a few sites out there (e.g. http://osm.duschmarke.de/bbox.html and http://bboxfinder.com/) that allow the selection and display of a bounding box. The main OSM site itself used to do this (see trac here), but no longer does - and since routing went live, the last OSM dev site that supporte...'''
date = "2015-02-20T12:29:00Z"
lastmod = "2022-09-04T22:53:00Z"
weight = 41173
keywords = [ "bbox" ]
aliases = [ "/questions/41173" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to obtain a bounding box for use with OSM tools](/questions/41173/how-to-obtain-a-bounding-box-for-use-with-osm-tools)

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
<span id="post-41173-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41173-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-41173-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There are a few sites out there (e.g. <a href="http://osm.duschmarke.de/bbox.html">http://osm.duschmarke.de/bbox.html</a> and <a href="http://bboxfinder.com/">http://bboxfinder.com/</a>) that allow the selection and display of a bounding box.</p>
<p>The main OSM site itself used to do this (see trac <a href="https://trac.openstreetmap.org/ticket/5055">here</a>), but no longer does - and since routing went live, the last OSM dev site that supported it has gone away.</p>
<p>What I'm looking for is:</p>
<ul>
<li>Something to create a bounding box, that works across platforms and across window managers</li>
<li>Something to display a bounding box in the "usual" OSM format (as used by the API etc.)</li>
</ul>
<p>It'd be nice if it also allowed the display of different tiles too - either layers available on osm.org or elsewhere.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bbox" rel="tag" title="see questions tagged &#39;bbox&#39;">bbox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Feb '15, 12:29</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-41173" class="comments-container">
<span id="85562"></span>
<div id="comment-85562" class="comment">
<div id="post-85562-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There’s now a section addressing this on the wiki: <a href="https://wiki.openstreetmap.org/wiki/Bounding_Box#Visually_defining_a_bounding_box">Visually defining a bounding box</a></p>
</div>
<div id="comment-85562-info" class="comment-info">
<span class="comment-age">(04 Sep '22, 22:53)</span> <span class="comment-user userinfo">Andrew Kvalheim</span>
</div>
</div>
</div>
<div id="comment-tools-41173" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41173-form-container" class="comment-form-container">
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

<span id="41174"></span>

<div id="answer-container-41174" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41174-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41174-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-41174-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I can offer <a href="http://tools.geofabrik.de/calc/#type=geofabrik_standard&amp;bbox=5.538062,47.236312,15.371071,54.954937&amp;tab=1">http://tools.geofabrik.de/calc/#type=geofabrik_standard&amp;bbox=5.538062,47.236312,15.371071,54.954937&amp;tab=1</a> but it's not perfect either.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Feb '15, 12:39</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-41174" class="comments-container">
&#10;</div>
<div id="comment-tools-41174" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41174-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="41178"></span>

<div id="answer-container-41178" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41178-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-41178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Mine is <a href="http://norbertrenner.de/osm/bbox.html">http://norbertrenner.de/osm/bbox.html</a>, but no display.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Feb '15, 13:13</strong></p>
<img src="https://secure.gravatar.com/avatar/f92748c8fa508a936bcf2169b30cabf6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ikonor&#39;s gravatar image" />
<p><span>ikonor</span><br />
<span class="score" title="1286 reputation points"><span>1.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ikonor has 4 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-41178" class="comments-container">
&#10;</div>
<div id="comment-tools-41178" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41178-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="42758"></span>

<div id="answer-container-42758" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42758-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42758-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42758-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Another one:</p>
<p><a href="http://harrywood.co.uk/maps/uixapi/xapi.html">http://harrywood.co.uk/maps/uixapi/xapi.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Apr '15, 18:24</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-42758" class="comments-container">
&#10;</div>
<div id="comment-tools-42758" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42758-form-container" class="comment-form-container">
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

