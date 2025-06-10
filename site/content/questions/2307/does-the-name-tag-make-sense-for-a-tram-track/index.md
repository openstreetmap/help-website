+++
type = "question"
title = "Does the &quot;name=*&quot; tag make sense for a tram track?"
description = '''As a related question to What is the proper way to tag tram tracks embedded in a street? : Does the name=* tag make sense for a tram track? On Tag:railway=tram , the Wiki proposes to use name=* to tag the &quot;Line numbers&quot;. This seems ill-advised, because:  often several lines share a track usually a l...'''
date = "2011-01-19T23:33:00Z"
lastmod = "2011-01-20T14:46:00Z"
weight = 2307
keywords = [ "tram", "public-transport", "tagging" ]
aliases = [ "/questions/2307" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Does the "name=\*" tag make sense for a tram track?](/questions/2307/does-the-name-tag-make-sense-for-a-tram-track)

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
<span id="post-2307-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2307-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-2307-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>As a related question to <a href="http://help.openstreetmap.org/questions/2306/what-is-the-proper-way-to-tag-tram-tracks-embedded-in-a-street">What is the proper way to tag tram tracks embedded in a street?</a> : Does the <code>name=*</code> tag make sense for a tram track?</p>
<p>On <a href="http://wiki.openstreetmap.org/wiki/Tag:railway=tram">Tag:railway=tram</a> , the Wiki proposes to use <code>name=*</code> to tag the "Line numbers". This seems ill-advised, because:</p>
<ul>
<li>often several lines share a track</li>
<li>usually a line will consist of many ways (because of length); tagging them all by line number will make it difficult to find the whole length of a line (it would have to be joined by searching for the name)</li>
<li><code>name</code> is not meant for designations, but real names, so even disregarding the above, <code>ref=</code> would seem more natural</li>
<li>If a street and a tram track share a single way (see my other question linked above), the <code>name=</code> tags will conflict</li>
<li>Finally, there is already a way to tag public transport lines using relations, which solves all these problems, so tagging the line no. as the name is redundant, and likely to become wrong soon when it is not updated together with the relation.</li>
</ul>
<p>So is there any good reason for this recommendation? Or can it be deleted?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tram" rel="tag" title="see questions tagged &#39;tram&#39;">tram</span> <span class="post-tag tag-link-public-transport" rel="tag" title="see questions tagged &#39;public-transport&#39;">public-transport</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jan '11, 23:33</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jan '11, 23:35</strong> </span></p>
</div>
</div>
<div id="comments-container-2307" class="comments-container">
&#10;</div>
<div id="comment-tools-2307" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2307-form-container" class="comment-form-container">
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

<span id="2314"></span>

<div id="answer-container-2314" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2314-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2314-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-2314-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sleske has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>AFAIK, name=* is used in infrastructure when a way or a junction is generally well known with a name. Like "Tsarigradsko shose" street (have it written on street plates) or "Trainstation circle" roundabout (officially not named, but well known by all residents).</p>
<p>ref=* would more likely stand for some official naming like E85 (but still could be "Tsarigardsko shose" as long as it is official name).</p>
<p>I think the same rules could apply for tram tracks.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jan '11, 08:27</strong></p>
<img src="https://secure.gravatar.com/avatar/ca446edd75e87c48db5dd850d9f394a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ivanatora&#39;s gravatar image" />
<p><span>ivanatora</span><br />
<span class="score" title="2740 reputation points"><span>2.7k</span></span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="55 badges"><span class="silver">●</span><span class="badgecount">55</span></span><span title="68 badges"><span class="bronze">●</span><span class="badgecount">68</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ivanatora has one accepted answer">7%</span></p>
</div>
</div>
<div id="comments-container-2314" class="comments-container">
<span id="2315"></span>
<div id="comment-2315" class="comment">
<div id="post-2315-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ref=* is clearly more consistent with the rest of OSM and I've corrected the page.</p>
</div>
<div id="comment-2315-info" class="comment-info">
<span class="comment-age">(20 Jan '11, 10:44)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="2322"></span>
<div id="comment-2322" class="comment">
<div id="post-2322-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Like the rest of OSM, both are possible (ref and/or name)</p>
</div>
<div id="comment-2322-info" class="comment-info">
<span class="comment-age">(20 Jan '11, 14:46)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-2314" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2314-form-container" class="comment-form-container">
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

