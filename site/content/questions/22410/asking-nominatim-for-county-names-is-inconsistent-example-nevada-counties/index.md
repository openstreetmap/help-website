+++
type = "question"
title = "Asking Nominatim for county names is inconsistent (example: Nevada counties)"
description = '''When asking Nominatim for a County – in some cases you must have the word “County” while in others you must NOT have it (in order to get polygons) For example in Nevada Counties  “Washoe County” works “Washoe” – doesn’t work “Churchill county” doesn’t work “Churchill” works  .1. http://nominatim.ope...'''
date = "2013-05-14T07:49:00Z"
lastmod = "2013-05-14T13:39:00Z"
weight = 22410
keywords = [ "county", "url", "nominatim", "polygon", "inconsistency" ]
aliases = [ "/questions/22410" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Asking Nominatim for county names is inconsistent (example: Nevada counties)](/questions/22410/asking-nominatim-for-county-names-is-inconsistent-example-nevada-counties)

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
<span id="post-22410-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22410-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22410-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When asking Nominatim for a County – in some cases you must have the word “County” while in others you must NOT have it (in order to get polygons)</p>
<p>For example in Nevada Counties</p>
<ol>
<li>“Washoe County” works</li>
<li>“Washoe” – doesn’t work</li>
<li>“Churchill county” doesn’t work</li>
<li>“Churchill” works</li>
</ol>
<p>.1. <a href="http://nominatim.openstreetmap.org/search.php?q=">http://nominatim.openstreetmap.org/search.php?q=</a><strong>COUNTY_NAME</strong>%2CUnited%20States&amp;addressdetails=1&amp;limit=10&amp;format=xml&amp;polygon_text=1&amp;email=<strong>MY_EMAIL</strong>&amp;countrycodes=USA&amp;bounded=1</p>
<p>Is it a known issue? Are there recommendations about how to request the data in a consistent way? Is there an open source code (preferably c#) that wrap these kind of calls and do the work-arounds?</p>
<p>=== Addition: ===</p>
<p>Is it possible that when searching for a name (w/o the "county" suffix or other pre/suffix) the results will include the the items with the suffix, and preferably ordered by higher to lower level (meaning New York will give New York state before New York city)</p>
<p>and from the other direction: If you have suffix - after results including the suffix - add results for same name w/o the suffix - for known words suce as State, Provice, County and so on</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-county" rel="tag" title="see questions tagged &#39;county&#39;">county</span> <span class="post-tag tag-link-url" rel="tag" title="see questions tagged &#39;url&#39;">url</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-inconsistency" rel="tag" title="see questions tagged &#39;inconsistency&#39;">inconsistency</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 May '13, 07:49</strong></p>
<img src="https://secure.gravatar.com/avatar/50ba179b54fcc54ff8e9be0f4d6b853f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dekel%20Israeli&#39;s gravatar image" />
<p><span>Dekel Israeli</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dekel Israeli has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 May '13, 14:33</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-22410" class="comments-container">
&#10;</div>
<div id="comment-tools-22410" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22410-form-container" class="comment-form-container">
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

<span id="22425"></span>

<div id="answer-container-22425" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22425-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22425-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-22425-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not sure it is an issue as such. Nominatim is finding the place names that are mapped: <a href="https://www.openstreetmap.org/browse/relation/166464">Churchill</a> and <a href="https://www.openstreetmap.org/browse/relation/166456">Washoe County</a>. A workaround would have to handle knowing what <a href="https://wiki.openstreetmap.org/wiki/Admin_level#10_admin_level_values_for_specific_countries">admin levels</a> mean and either removing or adding the extra word(s) (at the beginning or end as appropriate, in whatever language is determined relevant). Even admin_level 6 in USA alone isn't simple, being "Counties, parishes in Louisiana, boroughs in Alaska and also in New York City and the Independent cities (Virginia; Baltimore, MD; Carson City, NV; St. Louis, MO)".</p>
<p>The good news is that <a href="https://github.com/twain47/Nominatim">nominatim is already open source</a> (but not C#) so if you can come up with a way that works I'm sure it would be welcomed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 May '13, 13:39</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-22425" class="comments-container">
&#10;</div>
<div id="comment-tools-22425" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22425-form-container" class="comment-form-container">
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

