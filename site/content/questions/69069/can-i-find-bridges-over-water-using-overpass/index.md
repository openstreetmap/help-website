+++
type = "question"
title = "Can I find bridges over water using Overpass?"
description = '''It seems bridges are tagged bridge=*. I&#x27;m interested in what the bridge is crossing. Specifically, I&#x27;m trying to find a way to query Overpass for bridges that cross certain waterways (not railways or other streets). Is this possible using the Overpass API? What keys/tags would I be looking for?'''
date = "2019-05-03T19:42:00Z"
lastmod = "2019-05-03T21:56:00Z"
weight = 69069
keywords = [ "overpass", "waterway", "bridge" ]
aliases = [ "/questions/69069" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can I find bridges over water using Overpass?](/questions/69069/can-i-find-bridges-over-water-using-overpass)

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
<span id="post-69069-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69069-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69069-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>It seems bridges are tagged <code>bridge=*</code>. I'm interested in <strong>what the bridge is crossing.</strong></p>
<p>Specifically, I'm trying to find a way to query Overpass for bridges that cross certain waterways (not railways or other streets).</p>
<p>Is this possible using the Overpass API? What keys/tags would I be looking for?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-waterway" rel="tag" title="see questions tagged &#39;waterway&#39;">waterway</span> <span class="post-tag tag-link-bridge" rel="tag" title="see questions tagged &#39;bridge&#39;">bridge</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 May '19, 19:42</strong></p>
<img src="https://secure.gravatar.com/avatar/2270d703967bfebb9cb555f85b3bb56b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="awendt&#39;s gravatar image" />
<p><span>awendt</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="awendt has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69069" class="comments-container">
&#10;</div>
<div id="comment-tools-69069" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69069-form-container" class="comment-form-container">
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

<span id="69076"></span>

<div id="answer-container-69076" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69076-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69076-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-69076-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="awendt has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suggest <a href="https://overpass-turbo.eu/s/IG9">this query</a>:</p>
<pre><code>way[waterway][tunnel!=yes]({{bbox}});
nwr(around:0)[bridge];
out geom;</code></pre>
<p>The <code>[tunnel!=yes]</code> might come on surprise. A test in London did otherwise found a street bridge over another street where conincidentially also is an underground channel in the map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 May '19, 21:56</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-69076" class="comments-container">
&#10;</div>
<div id="comment-tools-69076" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69076-form-container" class="comment-form-container">
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

