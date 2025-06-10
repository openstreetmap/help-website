+++
type = "question"
title = "Zip code boundary"
description = '''Hi everyone! I need to plot a map of the boundaries of france divided by zip code. something similar to this: http://www.youtube.com/watch?v=sZ6PNAYFqxU but in france any idea how to get it? thanks a lot in advance!'''
date = "2012-03-28T17:36:00Z"
lastmod = "2012-03-28T18:51:00Z"
weight = 11568
keywords = [ "boundary", "code", "zip" ]
aliases = [ "/questions/11568" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Zip code boundary](/questions/11568/zip-code-boundary)

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
<span id="post-11568-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11568-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11568-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone!</p>
<p>I need to plot a map of the boundaries of france divided by zip code. something similar to this: <a href="http://www.youtube.com/watch?v=sZ6PNAYFqxU">http://www.youtube.com/watch?v=sZ6PNAYFqxU</a></p>
<p>but in france</p>
<p>any idea how to get it?</p>
<p>thanks a lot in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-code" rel="tag" title="see questions tagged &#39;code&#39;">code</span> <span class="post-tag tag-link-zip" rel="tag" title="see questions tagged &#39;zip&#39;">zip</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Mar '12, 17:36</strong></p>
<img src="https://secure.gravatar.com/avatar/15d8349c5774d9702b147a72c3b9fdf9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aruizga7&#39;s gravatar image" />
<p><span>aruizga7</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aruizga7 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11568" class="comments-container">
&#10;</div>
<div id="comment-tools-11568" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11568-form-container" class="comment-form-container">
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

<span id="11572"></span>

<div id="answer-container-11572" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11572-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11572-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11572-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look in the OSM wiki at <a href="http://wiki.openstreetmap.org/wiki/MapCSS/Examples">MapCSS/Examples</a>.</p>
<p>First, download the raw OSM data from one of the mentioned sources.</p>
<p>Then, do a filtering via osmfilter by choosing --keep="postal_code="</p>
<p>Finally adapt the mentiones CSS stylefile to display the postalcode within each area.</p>
<p>You can also try any other <a href="http://wiki.openstreetmap.org/wiki/Rendering">rendering Software</a> to produce an optical output.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Mar '12, 18:17</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Mar '12, 18:18</strong> </span></p>
</div>
</div>
<div id="comments-container-11572" class="comments-container">
&#10;</div>
<div id="comment-tools-11572" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11572-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11573"></span>

<div id="answer-container-11573" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11573-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11573-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11573-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Layers.osm.fr also has <a href="http://layers.openstreetmap.fr/?zoom=7&amp;lat=47.66513&amp;lon=2.7523&amp;layers=B0000FFFFFFFFFFTFFFFFFF">a layer showing town-level boundaries</a> if you just want to see the data (not work with it) and if you do not mind the approximation of postcode=* &lt;-&gt; adminlevel=8.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Mar '12, 18:51</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-11573" class="comments-container">
&#10;</div>
<div id="comment-tools-11573" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11573-form-container" class="comment-form-container">
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

