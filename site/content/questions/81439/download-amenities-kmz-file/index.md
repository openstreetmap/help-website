+++
type = "question"
title = "Download amenities kmz file"
description = '''Hello, I would like to download amenities of a certain type and area, preferably in kmz format. For example I would like to have a kmz file of amenity=drinking_water in Berlin (more or less).  How to do it?'''
date = "2021-08-24T12:35:00Z"
lastmod = "2021-10-28T10:16:00Z"
weight = 81439
keywords = [ "download", "export", "amenities", "kmz" ]
aliases = [ "/questions/81439" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Download amenities kmz file](/questions/81439/download-amenities-kmz-file)

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
<span id="post-81439-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81439-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81439-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I would like to download amenities of a certain type and area, preferably in kmz format. For example I would like to have a kmz file of amenity=drinking_water in Berlin (more or less). How to do it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-amenities" rel="tag" title="see questions tagged &#39;amenities&#39;">amenities</span> <span class="post-tag tag-link-kmz" rel="tag" title="see questions tagged &#39;kmz&#39;">kmz</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Aug '21, 12:35</strong></p>
<img src="https://secure.gravatar.com/avatar/386324e20ac13480668e97a44cc1228f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Leszek&#39;s gravatar image" />
<p><span>Leszek</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Leszek has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81439" class="comments-container">
<span id="82396"></span>
<div id="comment-82396" class="comment">
<div id="post-82396-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm still looking for the answer.</p>
</div>
<div id="comment-82396-info" class="comment-info">
<span class="comment-age">(28 Oct '21, 09:08)</span> <span class="comment-user userinfo">Leszek</span>
</div>
</div>
</div>
<div id="comment-tools-81439" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81439-form-container" class="comment-form-container">
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

<span id="82397"></span>

<div id="answer-container-82397" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82397-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82397-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82397-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo">overpass turbo</a> to retrieve specific POIs from OSM.</p>
<p>The following query will search for all drinking water POIs in the currently visible area:</p>
<pre><code>[out:json][timeout:25];
// gather results
(
  nwr[&quot;amenity&quot;=&quot;drinking_water&quot;]({{bbox}});
  nwr[&quot;drinking_water&quot;=&quot;yes&quot;]({{bbox}});
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
<p>You can run it <a href="https://overpass-turbo.eu/s/1ctM">here</a>. Hit run. Then go to Export -&gt; Save as KML.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Oct '21, 10:11</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-82397" class="comments-container">
<span id="82398"></span>
<div id="comment-82398" class="comment">
<div id="post-82398-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much!</p>
</div>
<div id="comment-82398-info" class="comment-info">
<span class="comment-age">(28 Oct '21, 10:16)</span> <span class="comment-user userinfo">Leszek</span>
</div>
</div>
</div>
<div id="comment-tools-82397" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82397-form-container" class="comment-form-container">
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

