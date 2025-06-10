+++
type = "question"
title = "How to detect intersection of ways"
description = '''Hey there, I&#x27;m new with the OSM API and I am trying to work with the data retrieved via GetMapData and a BoundingBox. There are &amp;lt;way&amp;gt; Elements in the retrieved data that describe streets - so far so clear. The question according to my title: How can I detect which roads intersect, or rather ho...'''
date = "2011-12-05T21:01:00Z"
lastmod = "2011-12-06T16:22:00Z"
weight = 9344
keywords = [ "intersection" ]
aliases = [ "/questions/9344" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to detect intersection of ways](/questions/9344/how-to-detect-intersection-of-ways)

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
<span id="post-9344-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9344-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9344-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey there,</p>
<p>I'm new with the OSM API and I am trying to work with the data retrieved via GetMapData and a BoundingBox. There are &lt;way&gt; Elements in the retrieved data that describe streets - so far so clear.</p>
<p>The question according to my title: How can I detect which roads intersect, or rather how to get the points where they intersect? I tried to search for common nodes, but that didn't work. So I wonder if there is anything I haven't found yet to do this job..</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-intersection" rel="tag" title="see questions tagged &#39;intersection&#39;">intersection</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Dec '11, 21:01</strong></p>
<img src="https://secure.gravatar.com/avatar/c6f13d9344db49df4f8f09a7bd6f9589?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="raveNOSM&#39;s gravatar image" />
<p><span>raveNOSM</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="raveNOSM has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9344" class="comments-container">
&#10;</div>
<div id="comment-tools-9344" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9344-form-container" class="comment-form-container">
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

<span id="9345"></span>

<div id="answer-container-9345" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9345-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9345-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-9345-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First of all, the API queries - and GetMapData seems to make use of one of those - are mainly meant for editing. So if you are doing an application that does any kind of data analysis, or rendering, or something else, and especially if you believe that you will make many such queries, then this API call is not for you. You'll have to download an OSM excerpt or a "planet file" and analyse that.</p>
<p>OSM data does generally have a topology, so your approach of looking for nodes shared by more than one way should work. Of course, one street might consist of several way objcts. Ways will of course not share a node when there's a bridge or tunnel, or when one is e.g. a boundary line and the other a railway.</p>
<p>If two streets intersect and neither of them is a bridge or tunnel, then they should have an intersection node; editors and validators will complain if they haven't.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Dec '11, 21:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-9345" class="comments-container">
<span id="9347"></span>
<div id="comment-9347" class="comment">
<div id="post-9347-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your fast answer - good to know that my approach must work, so I just have to check that again.</p>
<p>But what is an OSM excerpt? I am doing such an API call only once, and then work with this data, so I thought that was the correct way..</p>
</div>
<div id="comment-9347-info" class="comment-info">
<span class="comment-age">(06 Dec '11, 07:58)</span> <span class="comment-user userinfo">raveNOSM</span>
</div>
</div>
<span id="9348"></span>
<div id="comment-9348" class="comment">
<div id="post-9348-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@raveNOSM</span>: "Excerpt" refers to an OSM data extract that you can download directly (rather than fetch via the API). Downloading an extract causes much less load on the servers than using the API; the API is not suitable for mass data retrieval. See <a href="http://wiki.openstreetmap.org/wiki/Downloading_data">http://wiki.openstreetmap.org/wiki/Downloading_data</a> for details.</p>
</div>
<div id="comment-9348-info" class="comment-info">
<span class="comment-age">(06 Dec '11, 11:04)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
<span id="9350"></span>
<div id="comment-9350" class="comment">
<div id="post-9350-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you're downloading this only once then don't worry. We're all easily frightened because every now and then someone writes an app that is then used by 1000s of people who download data wherever they go or so ;)</p>
</div>
<div id="comment-9350-info" class="comment-info">
<span class="comment-age">(06 Dec '11, 16:22)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-9345" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9345-form-container" class="comment-form-container">
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

