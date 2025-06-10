+++
type = "question"
title = "getting place names from nominatim"
description = '''The web tool at https://www.openstreetmap.org/search?query=... shows a great variety of alternate / non-english place names, eg for cities; how would I find those thru the nominatim API ? I cannot seem to find documentation on how to find tags by ID.  I tried  https://nominatim.openstreetmap.org/loo...'''
date = "2018-12-17T12:34:00Z"
lastmod = "2018-12-22T13:21:00Z"
weight = 67247
keywords = [ "names", "geonames" ]
aliases = [ "/questions/67247" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [getting place names from nominatim](/questions/67247/getting-place-names-from-nominatim)

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
<span id="post-67247-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67247-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67247-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The web tool at <a href="https://www.openstreetmap.org/search?query=..."><code>https://www.openstreetmap.org/search?query=...</code></a> shows a great variety of alternate / non-english place names, eg for cities; how would I find those thru the nominatim API ? I cannot seem to find documentation on how to find tags by ID.</p>
<p>I tried</p>
<pre><code>https://nominatim.openstreetmap.org/lookup?osm_ids=R1382494&amp;format=json</code></pre>
<p>but don't see the alternate names info I am after in the response.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-names" rel="tag" title="see questions tagged &#39;names&#39;">names</span> <span class="post-tag tag-link-geonames" rel="tag" title="see questions tagged &#39;geonames&#39;">geonames</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Dec '18, 12:34</strong></p>
<img src="https://secure.gravatar.com/avatar/5bd846e085c1f9700973dce3003f9e10?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jeremy%20rutman&#39;s gravatar image" />
<p><span>jeremy rutman</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jeremy rutman has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Dec '18, 17:21</strong> </span></p>
</div>
</div>
<div id="comments-container-67247" class="comments-container">
&#10;</div>
<div id="comment-tools-67247" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67247-form-container" class="comment-form-container">
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

<span id="67320"></span>

<div id="answer-container-67320" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67320-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67320-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67320-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can add <code>namedetails=1</code> to your search query to get the full list of available names, e.g. <a href="https://nominatim.openstreetmap.org/lookup?osm_ids=R1382494&amp;format=json&amp;namedetails=1">https://nominatim.openstreetmap.org/lookup?osm_ids=R1382494&amp;format=json&amp;namedetails=1</a>.</p>
<p>For a full description of the lookup API, see the <a href="http://nominatim.org/release-docs/develop/api/Lookup/">documentation on nominatim.org</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Dec '18, 13:21</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-67320" class="comments-container">
&#10;</div>
<div id="comment-tools-67320" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67320-form-container" class="comment-form-container">
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

