+++
type = "question"
title = "What to tag this very minor road as?"
description = '''There is a road near my house that is a very minor route, not maintained by the local council, that is mostly used for access to houses. It can be divided into 3 distinct sections: North: This section is paved, easily passable and has several driveways connecting to it.  Centre: This section has a d...'''
date = "2020-12-30T14:33:00Z"
lastmod = "2020-12-30T21:45:00Z"
weight = 78127
keywords = [ "roads", "classification", "tagging" ]
aliases = [ "/questions/78127" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What to tag this very minor road as?](/questions/78127/what-to-tag-this-very-minor-road-as)

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
<span id="post-78127-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78127-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78127-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There is a road near my house that is a very minor route, not maintained by the local council, that is mostly used for access to houses. It can be divided into 3 distinct sections: North: This section is paved, easily passable and has several driveways connecting to it. Centre: This section has a dirt surface and would likely be difficult to drive in an ordinary car, although definitely passable on foot, on a bike or in a tractor, and probably reasonably easy to drive in an SUV. South: This section has a gravel surface but is still easily passable by most vehicles. Also has driveways connecting to it.</p>
<p>What is the correct way to tag this road as? Should it be tagged as one road, or should each section have a different classification?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-roads" rel="tag" title="see questions tagged &#39;roads&#39;">roads</span> <span class="post-tag tag-link-classification" rel="tag" title="see questions tagged &#39;classification&#39;">classification</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Dec '20, 14:33</strong></p>
<img src="https://secure.gravatar.com/avatar/058bfdf7b3a47008bb34336a8eacc4d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="computerfan0&#39;s gravatar image" />
<p><span>computerfan0</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="computerfan0 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78127" class="comments-container">
&#10;</div>
<div id="comment-tools-78127" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78127-form-container" class="comment-form-container">
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

<span id="78134"></span>

<div id="answer-container-78134" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78134-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78134-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78134-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Firstly, based on what you've said, each section should have a different classification, as there will be different tags needed on the different sections.</p>
<p>It sounds as if each section might be "highway=service" or perhaps even "highway=residential" - have a look at how other similar roads are mapped in your country. Also make sure that the "access" tags are correct - this will also vary depending on what country you are in.</p>
<p>For the northern section, use an appropriate "paved" surface tag - see <a href="https://taginfo.openstreetmap.org/keys/surface#values">taginfo</a> for a list. Perhaps also add a <a href="https://taginfo.openstreetmap.org/keys/smoothness#values">smoothness</a> tag - see <a href="https://wiki.openstreetmap.org/wiki/Key%3Asmoothness">here</a> for a description of those.</p>
<p>For the middle and southern sections, use an appropriate "unpaved" surface tag and perhaps also a smoothness tag. Also consider a <a href="https://taginfo.openstreetmap.org/keys/tracktype#values">tracktype</a> value between grade1 and grade5 (see <a href="https://wiki.openstreetmap.org/wiki/Key%3Atracktype">here</a> for more information).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Dec '20, 17:36</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Dec '20, 18:43</strong> </span></p>
</div>
</div>
<div id="comments-container-78134" class="comments-container">
<span id="78150"></span>
<div id="comment-78150" class="comment">
<div id="post-78150-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This definitely doesn't sound like unclassified (which would normally be a council-maintained road). The N &amp; S sections sound very much like service roads (shared driveways) &amp; the middle section either a much degraded service road or track. Using track would strongly discourage routers from sending people along the whole route. I wouldn't worry too much about the precise value of service or track, the other tags mentioned by SomeoneElse are probably more useful.</p>
</div>
<div id="comment-78150-info" class="comment-info">
<span class="comment-age">(30 Dec '20, 21:45)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-78134" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78134-form-container" class="comment-form-container">
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

