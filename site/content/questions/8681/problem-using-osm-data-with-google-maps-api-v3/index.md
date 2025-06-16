+++
type = "question"
title = "Problem using OSM data with Google Maps API V3"
description = '''I&#x27;m using the method which is described here to add OSM data to an application which uses various mapping APIs, including Google Maps V2 and V3. The code supplied works perfectly with the Google Maps API V2. However, with V3 (I&#x27;m using the first V3 example, which is the second example on the page si...'''
date = "2011-10-27T09:59:00Z"
lastmod = "2012-04-20T15:19:00Z"
weight = 8681
keywords = [ "api", "google", "slippymap", "v3", "overlay" ]
aliases = [ "/questions/8681" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Problem using OSM data with Google Maps API V3](/questions/8681/problem-using-osm-data-with-google-maps-api-v3)

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
<span id="post-8681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8681-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm using the method which is described <a href="https://wiki.openstreetmap.org/wiki/Google_Maps_Example">here</a> to add OSM data to an application which uses various mapping APIs, including Google Maps V2 and V3.</p>
<p>The code supplied works perfectly with the Google Maps API V2. However, with V3 (I'm using the first V3 example, which is the second example on the page since there is one V2 example before it), although the OSM tiles load correctly, I no longer see the Google Maps scale controls ("drag to zoom").</p>
<p>The issue seems to be caused by this call:</p>
<p><code>map.setMapTypeId('OpenStreetMap');</code></p>
<p>If I comment that out, the scale controls appear, and work. Is there any reason why this call is necessary? Everything else seems to work, at first glance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-google" rel="tag" title="see questions tagged &#39;google&#39;">google</span> <span class="post-tag tag-link-slippymap" rel="tag" title="see questions tagged &#39;slippymap&#39;">slippymap</span> <span class="post-tag tag-link-v3" rel="tag" title="see questions tagged &#39;v3&#39;">v3</span> <span class="post-tag tag-link-overlay" rel="tag" title="see questions tagged &#39;overlay&#39;">overlay</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Oct '11, 09:59</strong></p>
<img src="https://secure.gravatar.com/avatar/6140a0027334e18d6e3c52f62c915df7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sTeamTraen&#39;s gravatar image" />
<p><span>sTeamTraen</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sTeamTraen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8681" class="comments-container">
&#10;</div>
<div id="comment-tools-8681" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8681-form-container" class="comment-form-container">
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

<span id="12201"></span>

<div id="answer-container-12201" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12201-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12201-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12201-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are you still using your Google V3 api format with this code commented out? Would you be willing to discuss the switch complexity, or not, with me?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Apr '12, 15:19</strong></p>
<img src="https://secure.gravatar.com/avatar/335a796dc9f5ff4cd289e77dd457413e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lanyon&#39;s gravatar image" />
<p><span>Lanyon</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lanyon has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12201" class="comments-container">
&#10;</div>
<div id="comment-tools-12201" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12201-form-container" class="comment-form-container">
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

