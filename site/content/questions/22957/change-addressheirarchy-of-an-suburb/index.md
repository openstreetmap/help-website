+++
type = "question"
title = "Change address/heirarchy of an suburb"
description = '''When I search for &#x27;Kondapur&#x27; I see results as &quot;Kondapur, Srila Park Pride, Rangareddy, India&quot;. However, the actual area has simple name &#x27;Kondapur, Hyderabad&#x27;. How do I change the address mentioned in the search results. The current result should be &#x27;Kondapur, Hyderabad&#x27; not &#x27;Kondapur, Srila Park Pri...'''
date = "2013-06-02T18:17:00Z"
lastmod = "2013-06-03T03:42:00Z"
weight = 22957
keywords = [ "suburb", "address" ]
aliases = [ "/questions/22957" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Change address/heirarchy of an suburb](/questions/22957/change-addressheirarchy-of-an-suburb)

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
<span id="post-22957-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22957-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22957-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I search for 'Kondapur' I see results as "Kondapur, Srila Park Pride, Rangareddy, India". However, the actual area has simple name 'Kondapur, Hyderabad'. How do I change the address mentioned in the search results. The current result should be 'Kondapur, Hyderabad' not 'Kondapur, Srila Park Pride, Rangareddy, India'</p>
<p>Looks like the search result is this: <a href="http://nominatim.openstreetmap.org/details.php?place_id=5986067105">http://nominatim.openstreetmap.org/details.php?place_id=5986067105</a></p>
<p>How do I change parent to Hyderabad city?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-suburb" rel="tag" title="see questions tagged &#39;suburb&#39;">suburb</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jun '13, 18:17</strong></p>
<img src="https://secure.gravatar.com/avatar/56790c3bee2fd6cd119d34cc9a7545ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ankit%20Jain&#39;s gravatar image" />
<p><span>Ankit Jain</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ankit Jain has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-22957" class="comments-container">
&#10;</div>
<div id="comment-tools-22957" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22957-form-container" class="comment-form-container">
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

<span id="22959"></span>

<div id="answer-container-22959" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22959-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22959-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-22959-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim does not use explicitly coded "parent" relationships; instead it checks the administrative regions. In your case, the point in question lies clearly outside the Hyderabad relation</p>
<p><a href="http://www.openstreetmap.org/browse/relation/2022211">http://www.openstreetmap.org/browse/relation/2022211</a></p>
<p>and inside the Rangareddy relation</p>
<p><a href="http://www.openstreetmap.org/browse/relation/2022214">http://www.openstreetmap.org/browse/relation/2022214</a></p>
<p>so you would have to change these relations, more specifically change this way</p>
<p><a href="http://www.openstreetmap.org/browse/way/45674000">http://www.openstreetmap.org/browse/way/45674000</a></p>
<p>which is used by both relations.</p>
<p>Please make sure that you only change the boundary if it really is wrong; do not change the boundary just to achive a desired effect in reverse geocoding. When you do change the boundary, be sure to place a proper changeset comment that explains why you made the change and what your sources for the change are.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jun '13, 19:10</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-22959" class="comments-container">
<span id="22970"></span>
<div id="comment-22970" class="comment">
<div id="post-22970-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, this answers my question partly. I want to remove 'Srila Park Pride' and just use 'Kondapur, Hyderabad'. Srila Park Pride is a hamlet outside kondapur.</p>
</div>
<div id="comment-22970-info" class="comment-info">
<span class="comment-age">(03 Jun '13, 03:42)</span> <span class="comment-user userinfo">Ankit Jain</span>
</div>
</div>
</div>
<div id="comment-tools-22959" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22959-form-container" class="comment-form-container">
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

