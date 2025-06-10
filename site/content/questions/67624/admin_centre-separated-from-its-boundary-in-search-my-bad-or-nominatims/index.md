+++
type = "question"
title = "Admin_centre separated from its boundary in search - my bad or Nominatim&#x27;s?"
description = '''I&#x27;ve been entering level-8 (village) administrative boundaries in northern Serbia recently, using admin_centre/administrative boundary relations. On testing my changes, however, I noticed inconsistent behavior of Nominatim search: For &quot;good&quot; ones, search immediately returns only one result: the rela...'''
date = "2019-01-17T10:58:00Z"
lastmod = "2019-01-22T11:35:00Z"
weight = 67624
keywords = [ "boundaries", "search", "nominatim", "admin_boundary" ]
aliases = [ "/questions/67624" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Admin_centre separated from its boundary in search - my bad or Nominatim's?](/questions/67624/admin_centre-separated-from-its-boundary-in-search-my-bad-or-nominatims)

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
<span id="post-67624-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67624-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67624-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been entering level-8 (village) administrative boundaries in northern Serbia recently, using admin_centre/administrative boundary relations. On testing my changes, however, I noticed inconsistent behavior of Nominatim search:</p>
<p>For "good" ones, search immediately returns only one result: the relation containing both the village and its boundaries, e.g.:<br />
<a href="https://nominatim.openstreetmap.org/search.php?q=Lipar">Lipar</a><br />
<a href="https://nominatim.openstreetmap.org/search.php?q=Stapar">Stapar</a><br />
For "bad" ones, search returns the village (point) separately from the boundary relation it belongs to, which is redundant and confusing:<br />
<a href="https://nominatim.openstreetmap.org/search.php?q=Nova+Crvenka">Nova Crvenka</a> (just 4 members)<br />
<a href="https://nominatim.openstreetmap.org/search.php?q=Crvenka">Crvenka</a></p>
<p>I can't figure out if I'm doing anything wrong, or is it a bug/feature on Nominatim's side. All those relations seem to have identical structure member-wise and tag-wise, and I can't explain different behavior. There's a <a href="https://wiki.openstreetmap.org/wiki/Nominatim/FAQ#Where_have_all_the_place.2Fcity.2Fcountry_nodes_gone.3F">hint in FAQ</a> that it might be due to some heuristics in Nominatim's algorithm (so I shouldn't worry), but I'd like to get a sanity check if I'm doing anything wrong first, if anyone feels like looking into it. Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-admin_boundary" rel="tag" title="see questions tagged &#39;admin_boundary&#39;">admin_boundary</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jan '19, 10:58</strong></p>
<img src="https://secure.gravatar.com/avatar/82883dda6a3f6ad7a7c74d15cfd24e43?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Duja&#39;s gravatar image" />
<p><span>Duja</span><br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Duja has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-67624" class="comments-container">
&#10;</div>
<div id="comment-tools-67624" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67624-form-container" class="comment-form-container">
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

<span id="67625"></span>

<div id="answer-container-67625" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67625-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67625-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-67625-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The tagging with role admin_centre looks good, Nominatim should've linked those together and returned only a single result. Can you add that to <a href="https://github.com/openstreetmap/Nominatim/issues">https://github.com/openstreetmap/Nominatim/issues</a> ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jan '19, 15:08</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span> </br></br></p>
</div>
</div>
<div id="comments-container-67625" class="comments-container">
&#10;</div>
<div id="comment-tools-67625" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67625-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="67675"></span>

<div id="answer-container-67675" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67675-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67675-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67675-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I seem to have figured it out. The problem was caused by naming: villages had canonical name in Serbian Cyrillic, while I populated the relations' names in Serbian Latin, as it was more convenient for me. I didn't think the relation names mattered. When I populated the whole set of transliterations for the boundary (Serbian Cyrillic, Serbian Latin, English), it started working as expected... although using just Cyrillic name seems to work as well</p>
<p>I'm still not sure how Nominatim did the "right" thing with the "good" relations, although their names were only in Latin all the way. Possibly has to do with transliterations, or who knows what. For example, when I populated Nova Crvenka in Cyrillic, adjacent Crvenka also started behaving, although I didn't touch it. Go figure...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jan '19, 11:35</strong></p>
<img src="https://secure.gravatar.com/avatar/82883dda6a3f6ad7a7c74d15cfd24e43?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Duja&#39;s gravatar image" />
<p><span>Duja</span><br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Duja has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-67675" class="comments-container">
&#10;</div>
<div id="comment-tools-67675" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67675-form-container" class="comment-form-container">
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

