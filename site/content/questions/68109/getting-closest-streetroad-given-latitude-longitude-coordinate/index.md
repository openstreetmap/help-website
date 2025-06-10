+++
type = "question"
title = "Getting closest street/road given latitude longitude coordinate"
description = '''I&#x27;ve set up my own instance of Nominatim. Trying to to create a reverse geocoding query for the closest road/street to a coordinate but not sure how to. I&#x27;ve used the &quot;around&quot; query when using the OSM API but unable to do so on my own instance of Nominatim. '''
date = "2019-02-22T08:15:00Z"
lastmod = "2019-02-27T16:46:00Z"
weight = 68109
keywords = [ "reversegeocoding", "nominatim", "around" ]
aliases = [ "/questions/68109" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Getting closest street/road given latitude longitude coordinate](/questions/68109/getting-closest-streetroad-given-latitude-longitude-coordinate)

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
<span id="post-68109-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68109-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68109-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've set up my own instance of Nominatim. Trying to to create a reverse geocoding query for the closest road/street to a coordinate but not sure how to. I've used the "around" query when using the OSM API but unable to do so on my own instance of Nominatim.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-around" rel="tag" title="see questions tagged &#39;around&#39;">around</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Feb '19, 08:15</strong></p>
<img src="https://secure.gravatar.com/avatar/f8530252a39bc017965730eaca4c806b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hellu&#39;s gravatar image" />
<p><span>hellu</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hellu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68109" class="comments-container">
&#10;</div>
<div id="comment-tools-68109" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68109-form-container" class="comment-form-container">
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

<span id="68114"></span>

<div id="answer-container-68114" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68114-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68114-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68114-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hellu has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use <code>/reverse</code> which on our machine might be <code>/nominatim/reverse</code> or <code>/nominatim/reverse.php</code> and set the <code>lat</code> and <code>lon</code> parameters. Setting <code>zoom</code> to 16 will skip building and return streets. <a href="http://nominatim.org/release-docs/latest/api/Reverse/">http://nominatim.org/release-docs/latest/api/Reverse/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Feb '19, 11:39</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-68114" class="comments-container">
<span id="68171"></span>
<div id="comment-68171" class="comment">
<div id="post-68171-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>will try that thank you!</p>
</div>
<div id="comment-68171-info" class="comment-info">
<span class="comment-age">(27 Feb '19, 03:02)</span> <span class="comment-user userinfo">hellu</span>
</div>
</div>
<span id="68172"></span>
<div id="comment-68172" class="comment">
<div id="post-68172-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>a follow up, im only looking for highway of type 'roads' and 'link roads' but this returns me 'pedestrian'. can I specify highway type?</p>
</div>
<div id="comment-68172-info" class="comment-info">
<span class="comment-age">(27 Feb '19, 04:08)</span> <span class="comment-user userinfo">hellu</span>
</div>
</div>
<span id="68176"></span>
<div id="comment-68176" class="comment">
<div id="post-68176-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><code>highway=roads</code> "If you do know the road type, do not use this value, instead use one of the more specific highway=* values." https://wiki.openstreetmap.org/wiki/Key:highway Nominatim doesn't have tag filters in the reverse search. In the forwards search it would also only be able to filter one road type, not many.</p>
</div>
<div id="comment-68176-info" class="comment-info">
<span class="comment-age">(27 Feb '19, 10:51)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="68181"></span>
<div id="comment-68181" class="comment">
<div id="post-68181-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you only care about specific highway tags, just filter out everything else before loading the data in to nominatim.</p>
</div>
<div id="comment-68181-info" class="comment-info">
<span class="comment-age">(27 Feb '19, 16:46)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-68114" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68114-form-container" class="comment-form-container">
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

