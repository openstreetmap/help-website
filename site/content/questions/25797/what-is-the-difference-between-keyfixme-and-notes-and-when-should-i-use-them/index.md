+++
type = "question"
title = "What is the difference between key:fixme and notes and when should I use them?"
description = '''I like the new ideditor and how easily it lets anyone put notes on the map. Although I can see the potential for added noise, I can also appreciate how easier it is to add notes instead of using key:fixme on existing features, which can lead to more errors (eg. moving a path without noticing) for be...'''
date = "2013-08-26T10:52:00Z"
lastmod = "2014-03-25T16:09:00Z"
weight = 25797
keywords = [ "bug_reporting", "notes", "bestpractice" ]
aliases = [ "/questions/25797" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [What is the difference between key:fixme and notes and when should I use them?](/questions/25797/what-is-the-difference-between-keyfixme-and-notes-and-when-should-i-use-them)

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
<span id="post-25797-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25797-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-25797-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I like the new ideditor and how easily it lets anyone put notes on the map.</p>
<p>Although I can see the potential for added noise, I can also appreciate how easier it is to add notes instead of using key:fixme on existing features, which can lead to more errors (eg. moving a path without noticing) for beginners.</p>
<p>It also seems like OSM bugs are more detailed and advanced problems that only more advanced users could fix (at least the few I've found), compared to notes.</p>
<p>What would be the best practice when using Notes vs. key:fixme?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bug_reporting" rel="tag" title="see questions tagged &#39;bug_reporting&#39;">bug_reporting</span> <span class="post-tag tag-link-notes" rel="tag" title="see questions tagged &#39;notes&#39;">notes</span> <span class="post-tag tag-link-bestpractice" rel="tag" title="see questions tagged &#39;bestpractice&#39;">bestpractice</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Aug '13, 10:52</strong></p>
<img src="https://secure.gravatar.com/avatar/0c12497903c6f3b2dd9f4d87deb127de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MagicFab&#39;s gravatar image" />
<p><span>MagicFab</span><br />
<span class="score" title="935 reputation points">935</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MagicFab has one accepted answer">20%</span></p>
</div>
</div>
<div id="comments-container-25797" class="comments-container">
&#10;</div>
<div id="comment-tools-25797" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25797-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="25801"></span>

<div id="answer-container-25801" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25801-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25801-score" class="post-score" title="current number of votes">
12
</div>
<span id="post-25801-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MagicFab has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>"<span>Notes</span>" are <em>not</em> associated to an <span>OSM object</span> but only to a location. Even not logged-in users can add "notes". There can be comments by other users to notes (with email notifications) although discussions should not happen there. "Notes" are am (improved) version of the former OpenStreetBugs.</p>
<p>Tags using the <span>key <code>fixme</code></span> <em>are</em> associated with an object. For example that means that if an object is moved the attached fixme tag also moves. That also means that you see the affected/related area or extent to which the fixme tag applies. Please also see <a href="/questions/23398/">how-to-mark-things-that-are-still-to-do?</a>!</p>
<p>I (others may have a different opinion/assessment) never use "notes" (or the former OpenStreetBugs). I regard "notes" (such an unfortunate name …) as a good option for "outsiders" or newbies to report errors or problems. The fixme key is rather mapper to mapper (even to yourself for later surveys) communication.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Aug '13, 13:05</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Mar '14, 23:03</strong> </span></p>
</div>
</div>
<div id="comments-container-25801" class="comments-container">
&#10;</div>
<div id="comment-tools-25801" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25801-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="25881"></span>

<div id="answer-container-25881" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25881-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25881-score" class="post-score" title="current number of votes">
11
</div>
<span id="post-25881-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would like to give a differing opinion to aseerel4c26. I prefer the external "notes" to the use of a fixme tag.</p>
<p>Notes are like a ticket system for source code. It lives outside and provides extra information and capabilities for tracking its completion/progress.</p>
<p>The fixme tag on the other hand, it is like writing // FIXME: in the source code. IDEs and tools will try to surface the information, but ultimately these get lost/ignored and usually only valuable when actively working in a section of code or no ticket system is setup.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Aug '13, 04:53</strong></p>
<img src="https://secure.gravatar.com/avatar/7e77c05737bf455a5bf99c0f17ac19d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="he_the_great&#39;s gravatar image" />
<p><span>he_the_great</span><br />
<span class="score" title="1175 reputation points"><span>1.2k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="he_the_great has 3 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-25881" class="comments-container">
<span id="31891"></span>
<div id="comment-31891" class="comment">
<div id="post-31891-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Regarding fixmes getting lost, fixme tags are highlighted prominently in at least two of the OSM QA tools: OSM Inspector and KeepRight.</p>
</div>
<div id="comment-31891-info" class="comment-info">
<span class="comment-age">(25 Mar '14, 15:29)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
</div>
<div id="comment-tools-25881" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25881-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="31893"></span>

<div id="answer-container-31893" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31893-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31893-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-31893-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here's another personal opinion (and only that!) - I use both "notes" and "fixme" tags, but tend to use them for different things. In addition I also use "notes to self" in the form of Garmin waypoints; if I'm going walking somewhere I'll extract the area where I'm planning to be from a big file of GPX waypoints so that I know what to look for.</p>
<p>I tend to use "notes" for one of two things - either "I've been to this place on the map, and what's currently in OSM doesn't match my recollection of it" or "I've never been here, but what's here isn't feasible" (such as a bus route that jumps from one road to another missing out the road in the middle, or a footpath that stops just short of joining a road).</p>
<p>Fixmes I mostly use for and "notes to like minded mappers", things like "There's a footpath here, or something that looks like it might be one, and at some time I need to walk it to see where it goes". Adding all these as notes would make the standard with-notes view of some areas of England very disconcerting to city-dwellers</p>
<p>The Garmin waypoint "notes to self" I use for things like "There's a new pub opening here in a month or so. Must map it when it does". There's no point in adding a fixme or note for that because there's nothing to fix yet.</p>
<p>Similarly notes or fixmes that say "this area needs mapping better" can be a bit problematical - it may well have been that an area was mapped with the best tools available a few years ago, but better tools are available now. The widespread addition of things like "fixme - check if $item has $feature" don't help much, either.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Mar '14, 16:09</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Aug '14, 10:18</strong> </span></p>
</div>
</div>
<div id="comments-container-31893" class="comments-container">
&#10;</div>
<div id="comment-tools-31893" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31893-form-container" class="comment-form-container">
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

