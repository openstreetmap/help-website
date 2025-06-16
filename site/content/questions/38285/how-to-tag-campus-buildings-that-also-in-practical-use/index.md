+++
type = "question"
title = "How to tag campus buildings that also in practical use?"
description = '''For example we have a medical university campus where there are buildings that are hospital buildings (too). I would map the university buildings as building=university and the hospital buildings as building=hospital, but what should I do with the amenity they are in? Should it be amenity=university...'''
date = "2014-11-03T16:17:00Z"
lastmod = "2014-11-04T17:28:00Z"
weight = 38285
keywords = [ "university", "hospital", "mapping", "campus" ]
aliases = [ "/questions/38285" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to tag campus buildings that also in practical use?](/questions/38285/how-to-tag-campus-buildings-that-also-in-practical-use)

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
<span id="post-38285-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38285-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-38285-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For example we have a medical university campus where there are buildings that are hospital buildings (too). I would map the university buildings as <code>building=university</code> and the hospital buildings as <code>building=hospital</code>, but what should I do with the amenity they are in? Should it be <code>amenity=university</code> or <code>amenity=hospital</code>? Or should I use one for mapping the area and the other one on a node in the middle of the area?</p>
<p>Are there good mapping examples in this topic?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-university" rel="tag" title="see questions tagged &#39;university&#39;">university</span> <span class="post-tag tag-link-hospital" rel="tag" title="see questions tagged &#39;hospital&#39;">hospital</span> <span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span> <span class="post-tag tag-link-campus" rel="tag" title="see questions tagged &#39;campus&#39;">campus</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Nov '14, 16:17</strong></p>
<img src="https://secure.gravatar.com/avatar/a9715d60e31c91a442c2dacefdc1dae9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="UntaggedWay&#39;s gravatar image" />
<p><span>UntaggedWay</span><br />
<span class="score" title="576 reputation points">576</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="UntaggedWay has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38285" class="comments-container">
&#10;</div>
<div id="comment-tools-38285" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38285-form-container" class="comment-form-container">
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

<span id="38290"></span>

<div id="answer-container-38290" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38290-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38290-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-38290-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="UntaggedWay has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ul>
<li>For the <em>building</em> type: use the type which is the most characteristic one for this building. Tag it as university building if it looks like all other university buildings around. I guess the building type will matter for much less data users than the amenity tags.</li>
<li><em>amenity</em> (<span>schematic example image</span>):
<ul>
<li>The <em>university</em> amenity tag <span>should exist only one time</span> for the whole university. So, likely this will be on an area (closed way) or even a multipolygon.</li>
<li>And, yes, the <em>hospital</em> amenity tag is additional to the university then (there is an university <em>and</em> an hospital and you can easily map it what way). Map the hospital amenity area inside the university amenity area (sorry, I cannot find a good example). You do not need to cut out the hospital areas from the university area, since the hospitals belong to the university too. Depending on how big the hospital area is, use it on an area (maybe simply the hospital building or as a new way if there are multiple buildings and places forming the hospital) or is it just a small part of the building which is an hospital, then maybe a node would be the best way.</li>
</ul></li>
</ul>
<p>Also see our docu wiki for those tags: <span>hospital</span> and <span>university</span>, of course.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Nov '14, 18:21</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Nov '14, 00:06</strong> </span></p>
</div>
</div>
<div id="comments-container-38290" class="comments-container">
<span id="38294"></span>
<div id="comment-38294" class="comment">
<div id="post-38294-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/9939/totymedli"></a><a href="https://help.openstreetmap.org/users/9939/totymedli">@totymedli</a>: thanks, I have tried to clarify. Maybe someone else finds a good example. The ones I have found are university hospitals but are neither inside the general university area nor associated with one by a relation (<span>example</span>, which also has many amenity=hospital, which is not really according to one feature, one element). However, that's not a rule. As there are very few "rules" in the OSM world in general.</p>
<p>I have added a drawing, hope that helps. If not … maybe I have understood your question wrongly.</p>
</div>
<div id="comment-38294-info" class="comment-info">
<span class="comment-age">(03 Nov '14, 22:08)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="38310"></span>
<div id="comment-38310" class="comment">
<div id="post-38310-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm not sure if this is what aseerel4c26 is saying or not, but in the case of a university hospital that is separated from the rest of the university campus, you could tag the way amenity=hospital, then add that way to a amenity=university relation</p>
</div>
<div id="comment-38310-info" class="comment-info">
<span class="comment-age">(04 Nov '14, 14:17)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="38313"></span>
<div id="comment-38313" class="comment">
<div id="post-38313-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/595/neuhausr"></a><a href="https://help.openstreetmap.org/users/595/neuhausr">@neuhausr</a>: Thank you. That's nearly what I am saying or, at least, meaning, yes. Contrary to your assumption, I assumed (see my image) that the hospital campus is not separate from the rest of the university campus. The geographic constellation is not that clear in the question.</p>
</div>
<div id="comment-38313-info" class="comment-info">
<span class="comment-age">(04 Nov '14, 17:28)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-38290" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38290-form-container" class="comment-form-container">
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

