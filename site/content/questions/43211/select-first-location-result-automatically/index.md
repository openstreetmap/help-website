+++
type = "question"
title = "Select first location result automatically"
description = '''When using location service from openstreetmap.org, we get a list of matching city/area/other from Nominatim and GeoNames.  Is there any special reason why the first result of this list (so probably the &quot;best matching proposition&quot;) is not automatically focused on map but user has to select it manual...'''
date = "2015-05-25T18:59:00Z"
lastmod = "2015-05-26T17:49:00Z"
weight = 43211
keywords = [ "routing" ]
aliases = [ "/questions/43211" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Select first location result automatically](/questions/43211/select-first-location-result-automatically)

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
<span id="post-43211-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43211-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43211-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When using location service from <a href="http://openstreetmap.org">openstreetmap.org</a>, we get a list of matching city/area/other from Nominatim and GeoNames.</p>
<p>Is there any special reason why the first result of this list (so probably the "best matching proposition") is not automatically focused on map but user has to select it manually?</p>
<p>Most of the other map services (Google Maps, Brouter, etc.) move map to the first result position which is most of the time the expected answer in my opinion. There might be a discussion around that somewhere but I could not spot it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 May '15, 18:59</strong></p>
<img src="https://secure.gravatar.com/avatar/36ec076e72becebf7e31b80da44ca05f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bagage&#39;s gravatar image" />
<p><span>bagage</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bagage has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 May '15, 20:04</strong> </span></p>
</div>
</div>
<div id="comments-container-43211" class="comments-container">
&#10;</div>
<div id="comment-tools-43211" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43211-form-container" class="comment-form-container">
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

<span id="43213"></span>

<div id="answer-container-43213" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43213-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43213-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-43213-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bagage has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are you sure about that? :)</p>
<p>On openstreetmap.org, if you click the 'routing' icon (two arrows), then enter values into each field, the "top result" is the only one available and is automatically selected - the remaining results are actually discarded.</p>
<p>On the standard (non-routing) search, the behaviour is more like what you describe.</p>
<p>It would be good to bring the two behaviours together, which would require moving the results parsing logic from Rails (as at present) to JavaScript. However, thus far, no developer has volunteered to do that. Maybe you could volunteer?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 May '15, 19:56</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 May '15, 19:57</strong> </span></p>
</div>
</div>
<div id="comments-container-43213" class="comments-container">
<span id="43214"></span>
<div id="comment-43214" class="comment">
<div id="post-43214-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>For clarity - I should point out that bagage's original question was "Select first routing result automatically" and "When using routing service from...", which was the context in which my answer was written. Slightly bad form to do a ninja edit without an accompanying comment, but hey.</p>
</div>
<div id="comment-43214-info" class="comment-info">
<span class="comment-age">(25 May '15, 21:26)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="43233"></span>
<div id="comment-43233" class="comment">
<div id="post-43233-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Hmm, you are right Richard, I edited my question after seeing correct technical terms in your answer and I did not thought a comment was worth the noise, my bad! I am not a web programmer at all, but I think I will take a look at it and see if I can do it. There is already an issue reported about that on github: <a href="https://github.com/openstreetmap/openstreetmap-website/issues/919">https://github.com/openstreetmap/openstreetmap-website/issues/919</a></p>
</div>
<div id="comment-43233-info" class="comment-info">
<span class="comment-age">(26 May '15, 17:49)</span> <span class="comment-user userinfo">bagage</span>
</div>
</div>
</div>
<div id="comment-tools-43213" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43213-form-container" class="comment-form-container">
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

