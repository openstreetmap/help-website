+++
type = "question"
title = "man_made=spoil_heap not rendering on std OSM"
description = '''Hi all, I&#x27;ve noticed that &quot;man_made=spoil_heap&quot; is not displayed with the std OSM rendering..! This is a very common feature affecting the landscape in many parts of the globe. The rendering of spoil heaps is fundamental to conveying a &quot;texture&quot; to the landscape and is helpful during navigation. Any...'''
date = "2022-04-13T09:28:00Z"
lastmod = "2022-04-13T11:22:00Z"
weight = 84167
keywords = [ "rendering", "spoil_heap" ]
aliases = [ "/questions/84167" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [man_made=spoil_heap not rendering on std OSM](/questions/84167/man_madespoil_heap-not-rendering-on-std-osm)

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
<span id="post-84167-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84167-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84167-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all, I've noticed that "man_made=spoil_heap" is not displayed with the std OSM rendering..!</p>
<p>This is a very common feature affecting the landscape in many parts of the globe. The rendering of spoil heaps is fundamental to conveying a "texture" to the landscape and is helpful during navigation.</p>
<p>Any ideas how to get this feature incorporated into std OSM rendering? Sorry I'm so naive about the mechanisms of how OSM rendering works.</p>
<p>Cheer, Larry</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-spoil_heap" rel="tag" title="see questions tagged &#39;spoil_heap&#39;">spoil_heap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Apr '22, 09:28</strong></p>
<img src="https://secure.gravatar.com/avatar/f73e9e14154d304e29bf7929313828d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CartogLarry&#39;s gravatar image" />
<p><span>CartogLarry</span><br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CartogLarry has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Apr '22, 11:04</strong> </span></p>
</div>
</div>
<div id="comments-container-84167" class="comments-container">
&#10;</div>
<div id="comment-tools-84167" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84167-form-container" class="comment-form-container">
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

<span id="84169"></span>

<div id="answer-container-84169" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84169-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84169-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84169-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://github.com/gravitystorm/openstreetmap-carto/issues/2421">https://github.com/gravitystorm/openstreetmap-carto/issues/2421</a> rejected at the time of 1st ticket a few years ago. See a few sections of threads discussing <code>landuse=landfill</code> in <a href="https://wiki.openstreetmap.org/wiki/Talk:Tag:man_made=spoil_heap"><code>https://wiki.openstreetmap.org/wiki/Talk:Tag:man_made=spoil_heap</code></a> about <code>disused=yes</code> vs <code>disused:*=</code> , and <code>landfill:waste=</code> (not mentioned directly) for what's disposed there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Apr '22, 10:27</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Apr '22, 10:31</strong> </span></p>
</div>
</div>
<div id="comments-container-84169" class="comments-container">
<span id="84170"></span>
<div id="comment-84170" class="comment">
<div id="post-84170-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Kovoschiz, Thanks for the very useful links :)</p>
<p>I will use man_made=spoil_heap + landuse=landfill (with or without disused=yes).</p>
<p>As the discussions in the links allude to man_made=spoil_heap duplicates the landuse=landfill tag somewhat.</p>
<p>Perhaps man_made=spoil_heap should be deprecated/discouraged or, if not, then combined tagging with landuse=landfill needs to be added to the man_made=spoil_heap page on the OSM Wiki guidance...</p>
<p>Cheers, Larry</p>
</div>
<div id="comment-84170-info" class="comment-info">
<span class="comment-age">(13 Apr '22, 11:22)</span> <span class="comment-user userinfo">CartogLarry</span>
</div>
</div>
</div>
<div id="comment-tools-84169" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84169-form-container" class="comment-form-container">
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

