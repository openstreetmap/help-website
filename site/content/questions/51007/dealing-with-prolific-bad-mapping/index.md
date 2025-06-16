+++
type = "question"
title = "Dealing with prolific bad mapping"
description = '''While dealing with errors reported by Osmose, I&#x27;ve come across a no-longer-active mapper who added a great deal of bad data to the local map. I don&#x27;t believe this is malicious; rather, something about the user&#x27;s workflow results in picking up tags from one thing he&#x27;s touched, and adding them to ever...'''
date = "2016-07-21T04:31:00Z"
lastmod = "2016-07-21T12:27:00Z"
weight = 51007
keywords = [ "quality_assurance" ]
aliases = [ "/questions/51007" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dealing with prolific bad mapping](/questions/51007/dealing-with-prolific-bad-mapping)

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
<span id="post-51007-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51007-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-51007-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>While dealing with errors reported by Osmose, I've come across a no-longer-active mapper who added a great deal of bad data to the local map.</p>
<p>I don't believe this is malicious; rather, something about the user's workflow results in picking up tags from one thing he's touched, and adding them to everything else he touches in that editing session, sometimes cumulatively. See, for example, <a href="https://www.openstreetmap.org/way/13922679">way #13922679</a> -- this is tagged simultaneously as a stream, a mineshaft, a Forest Service road, and an urban road.</p>
<p>Sometimes these errors are obvious (an open way running along a mountainside tagged as a lake and a track) and QA tools easily pick them up. Other times, however, they're subtle (a driveway tagged with three or four names, all wrong). Other than going through all 1500 edits, examining every object touched for errors, is there any way to find these problems?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-quality_assurance" rel="tag" title="see questions tagged &#39;quality_assurance&#39;">quality_assurance</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jul '16, 04:31</strong></p>
<img src="https://secure.gravatar.com/avatar/313c7f1fb7839c95ba6bb396791f56f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Carnildo&#39;s gravatar image" />
<p><span>Carnildo</span><br />
<span class="score" title="831 reputation points">831</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Carnildo has 2 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-51007" class="comments-container">
&#10;</div>
<div id="comment-tools-51007" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51007-form-container" class="comment-form-container">
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

<span id="51020"></span>

<div id="answer-container-51020" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51020-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51020-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-51020-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Potentially, there are three issues here. One is that the user may be unaware of the problems, and may be creating more of them. The others are the question you asked above - how to detect and fix them?</p>
<p>Taking the first one first, if you haven't already, to try adding a changeset discussion to one of the problematical changesets. If they haven't been active for a while you may not get an answer, but its worth a try. As you say above it's likely not malicious; perhaps in this case a workflow issue with an unfamiliar editor. A changeset discussion comment is public, so other users will know that you've tried to raise the issue.</p>
<p>Beyond the usual list of <a href="https://wiki.openstreetmap.org/wiki/Quality_assurance">QA sites</a>, isn't an easy answer to "detecting problems". As you've already found, when looking at a problematical changeset where one problem has been detected, you'll often find other errors too. Sometimes you can get a feel for the sort of objects that you need to check for to detect problems in changesets - if someone's incorrectly merging ways then it might be "some deleted ways and semicolons in values". The QA site list above links to various places, including changeset-based ones, that might be useful. See also the links from <a href="https://wiki.openstreetmap.org/wiki/Changeset#Changeset_Dump">here</a>.</p>
<p>Fixing is generally either changeset-based or problem-based. Changeset-based approaches (such as full or partial reverts) tend to work well where someone has made a whole bunch of invalid changes relatively recently and other users haven't touched the objects in the mean time, but unfortunately that doesn't apply here. That then leaves you with what you're already doing, which is detecting invalid objects, trying to look at other cases of the same problem, and trying to fix on an object-by-object basis.</p>
<p>As an aside, I completely agree with your comment <a href="https://www.openstreetmap.org/changeset/40909243">here</a> about partial fixes to data where it's clear that the fixer hasn't really thought through what they were doing at all, and is simplying acting like some kind of "mechanical turk". Personally, I find that these sorts of changes tend to mask real problems from QA sites and as such are actually <em>detrimental</em> to the quality of OSM data. <a href="https://www.openstreetmap.org/changeset/40530425">This</a> is another similar example. Unfortunately we don't have a good answer yet to this sort of "persistent bad fixing" - but at least it's identifiable by changeset comments such as "#to-fix" followed a geometrical rather than a geographical statement.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jul '16, 12:27</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-51020" class="comments-container">
&#10;</div>
<div id="comment-tools-51020" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51020-form-container" class="comment-form-container">
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

