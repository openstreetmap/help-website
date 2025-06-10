+++
type = "question"
title = "[closed] Why does iD keep undoing my name changes?"
description = '''I&#x27;m trying to use iD to edit the names of some tracks (old forest roads that are also part of a trail system). I select way #1, change the name, and either click off it or press Enter or click on the checkmark. The new name appears on the map in the editor. Then I click on the next one, way #2. As s...'''
date = "2016-03-12T03:13:00Z"
lastmod = "2016-03-15T00:07:00Z"
weight = 48637
keywords = [ "ideditor", "bug" ]
aliases = [ "/questions/48637" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [\[closed\] Why does iD keep undoing my name changes?](/questions/48637/why-does-id-keep-undoing-my-name-changes)

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
<span id="post-48637-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48637-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48637-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to use iD to edit the names of some tracks (old forest roads that are also part of a trail system). I select way #1, change the name, and either click off it or press Enter or click on the checkmark. The new name appears on the map in the editor. Then I click on the next one, way #2. As soon as I start typing a non-space character to edit the name of way #2, the name of way #1 reverts to what it was before my edit. The new name for way #2 appears on the map, but way #1 is back at its original name. If I click on way #1, it shows the old name tag value, while way #2 shows the new name tag value.</p>
<p>The first time this happened, I had gone through a series of about 6 of them, then went back to check before saving my changes. Only the last change 'took'. All the others had reverted, one at a time, as I was working. It's completely repeatable too.</p>
<p>I did find two work-arounds: (1) Rather than edit the names, delete the existing name (with the trash icon) and then enter it back with corrections. (2) Edit the name under All Tags, rather than at the top of the sidebar (under All fields). (Perhaps these will help track down the problem.)</p>
<p>Can anyone confirm this? (P.S. in reference to my previous question, I would be happy to open a github issue for this, but I want confirmation of the problem first, to make sure it isn't some error on my part.)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-bug" rel="tag" title="see questions tagged &#39;bug&#39;">bug</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Mar '16, 03:13</strong></p>
<img src="https://secure.gravatar.com/avatar/c1e98ded2982cd352d4c77075aa0cd74?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ljb_nj&#39;s gravatar image" />
<p><span>ljb_nj</span><br />
<span class="score" title="659 reputation points">659</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ljb_nj has one accepted answer">12%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>15 Mar '16, 06:46</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-48637" class="comments-container">
<span id="48659"></span>
<div id="comment-48659" class="comment">
<div id="post-48659-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Odd. I tried to reproduce it on the dev server and was unable to (<a href="http://api06.dev.openstreetmap.org/changeset/76511">http://api06.dev.openstreetmap.org/changeset/76511</a> ). That was with Windows 7, The browser was SeaMonkey 2.39.</p>
</div>
<div id="comment-48659-info" class="comment-info">
<span class="comment-age">(14 Mar '16, 20:06)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="48667"></span>
<div id="comment-48667" class="comment">
<div id="post-48667-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tried it again, same problem. I tried both Seamonkey-2.39 and Firefox-38.7ESR (both on Linux) with the same results.</p>
<p>At the bottom right corner, iD says it is version 1.9.1 for me. Is that the same as on your development server (which I assume I have no access to)?</p>
<p>To clarify, here is exactly how I reproduce it. In iD, click on a track, footpath, or other named way. At the top of the left sidebar, under Name, click at the end, and add a suffix. For example, edit "Main Street" to be "Main Street 2". As soon as I type the 2, the Save button on the toolbar lights up, the change counter goes to 1, and the edited name appears on the map.</p>
<p>Now click on another named way (track, footpath, etc). Then click at the end of the Name field in the sidebar, and add a suffix. As soon as I type a non-space character there, the first name I edited changes back to its original value on the map. The name of the currently selected way changes to the new value on the map, but the change counter at the top is still 1. The first change was undone by the second change.</p>
<p>(Then I undo and don't save anything to OSM. There is no need to save changes to demonstrate the problem I'm having.)</p>
</div>
<div id="comment-48667-info" class="comment-info">
<span class="comment-age">(14 Mar '16, 21:45)</span> <span class="comment-user userinfo">ljb_nj</span>
</div>
</div>
<span id="48669"></span>
<div id="comment-48669" class="comment">
<div id="post-48669-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Yes - I can reproduce it, but only when both suffixes I add start with a space. So if I (in my example) change "Main Street" to "Main Street 2" and "b2" to "b2 b", I see the problem. If either of the two suffices don't start with a space, I don't see the problem.</p>
<p>And yes, the dev server (which you can create an account on if you want) is running iD 1.9.1.</p>
</div>
<div id="comment-48669-info" class="comment-info">
<span class="comment-age">(14 Mar '16, 21:58)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="48670"></span>
<div id="comment-48670" class="comment">
<div id="post-48670-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Wow, OK. That is very weird and I'm not even sure how to write it up. What I'm seeing is that any name edit with leading space is undoing the previous name edit (whether it had a leading space or not). I think I'll write up an issue for the iD tracker with what I have. Maybe we'll be lucky and a developer will look at it and immediately know what's going on.</p>
<p>Thanks for confirming this.</p>
</div>
<div id="comment-48670-info" class="comment-info">
<span class="comment-age">(14 Mar '16, 22:17)</span> <span class="comment-user userinfo">ljb_nj</span>
</div>
</div>
</div>
<div id="comment-tools-48637" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48637-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Problem is fixed (see github link)" by aseerel4c26 15 Mar '16, 06:46

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48675"></span>

<div id="answer-container-48675" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48675-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48675-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-48675-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ljb_nj has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks for the report, I opened an issue on the iD issue tracker. <a href="https://github.com/openstreetmap/iD/issues/3035">https://github.com/openstreetmap/iD/issues/3035</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Mar '16, 00:07</strong></p>
<img src="https://secure.gravatar.com/avatar/5372740989fdca18458f194a285fcb3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bhousel&#39;s gravatar image" />
<p><span>bhousel</span><br />
<span class="score" title="2089 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bhousel has 13 accepted answers">38%</span></p>
</div>
</div>
<div id="comments-container-48675" class="comments-container">
&#10;</div>
<div id="comment-tools-48675" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48675-form-container" class="comment-form-container">
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

