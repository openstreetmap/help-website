+++
type = "question"
title = "How do I &quot;find&quot; a relation by giving the relation number?"
description = '''Trying to save changes to changeset in Potlatch 2, I receive the error &quot;...server said: Version Mismatch. Provided 38; server had 40 of Relation 2382578&quot;. Seems to me that in order to fix this problem, I need to first find out what Relation 2382578 is. But I can find no way to do this in Potlatch 2,...'''
date = "2013-06-25T02:56:00Z"
lastmod = "2013-06-25T14:39:00Z"
weight = 23654
keywords = [ "potlatch2", "mismatch", "version", "relation", "number" ]
aliases = [ "/questions/23654" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do I "find" a relation by giving the relation number?](/questions/23654/how-do-i-find-a-relation-by-giving-the-relation-number)

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
<span id="post-23654-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23654-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-23654-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Trying to save changes to changeset in Potlatch 2, I receive the error "...server said: Version Mismatch. Provided 38; server had 40 of Relation 2382578". Seems to me that in order to fix this problem, I need to first find out what Relation 2382578 is. But I can find no way to do this in Potlatch 2, nor could I find any previous q&amp;a here that answers my question. I assume this means that I deleted 2 ways that belonged to Relation 2382578 (which originally had 40 ways). But how to find the relation given just its number???</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-potlatch2" rel="tag" title="see questions tagged &#39;potlatch2&#39;">potlatch2</span> <span class="post-tag tag-link-mismatch" rel="tag" title="see questions tagged &#39;mismatch&#39;">mismatch</span> <span class="post-tag tag-link-version" rel="tag" title="see questions tagged &#39;version&#39;">version</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-number" rel="tag" title="see questions tagged &#39;number&#39;">number</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jun '13, 02:56</strong></p>
<img src="https://secure.gravatar.com/avatar/d52dc9111ac1bab71d8dadb2506610d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yourvillagemaps&#39;s gravatar image" />
<p><span>yourvillagemaps</span><br />
<span class="score" title="95 reputation points">95</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yourvillagemaps has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-23654" class="comments-container">
&#10;</div>
<div id="comment-tools-23654" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23654-form-container" class="comment-form-container">
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

<span id="23661"></span>

<div id="answer-container-23661" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23661-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23661-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-23661-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If a Potlatch 2 upload fails, it's possible to save the OSC file, and remove the failing item from it with a text editor, and then upload it with <a href="http://wiki.openstreetmap.org/wiki/Upload.py">upload.py</a>. If you don't already have it, you'll need to <a href="http://www.python.org/download/releases/">install Python</a> first.</p>
<p>If this sounds complicated, you might consider mentioning the problem on the #osm IRC channel - someone will be able to help.</p>
<p>The best way to avoid the problem in P2 the first place is to "save early, save often" so that if you do get a clash with another editor, you'll lose less work.<br />
</p>
<p>It's also helpful to try and avoid using huge multipolygons covering half a state...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jun '13, 07:57</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></p>
</div>
</div>
<div id="comments-container-23661" class="comments-container">
<span id="23676"></span>
<div id="comment-23676" class="comment">
<div id="post-23676-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>meta: I don't get it - the main question is <em>not</em> answered in this answer but this answer is has 4 usefulness vote points and mine 1. I'd like to understand that.</p>
</div>
<div id="comment-23676-info" class="comment-info">
<span class="comment-age">(25 Jun '13, 14:23)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="23677"></span>
<div id="comment-23677" class="comment">
<div id="post-23677-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@aseerel4c26</span>: It's intended to help avoid the underlying problem rather than fix the particular symptom, and provide a workaround if the symptom should occur again in the future.<br />
</p>
<p>Once you've hit the problem in P2 you can't solve the problem there, hence the cludgy upload.py workaround. Even if if you can locate the relation number (which is visible in advenced mode and from there you can get to the web history page) you can't do anything useful with it at that stage.</p>
</div>
<div id="comment-23677-info" class="comment-info">
<span class="comment-age">(25 Jun '13, 14:31)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="23678"></span>
<div id="comment-23678" class="comment">
<div id="post-23678-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@SomeoneElse</span>: Sure, but the question is titled quite differently. Someone arriving here searching for an answer to the title question will not be helped by your answer. I am not mainly addressing you but the crowd here.</p>
<p>Well, we could change the title, then the situation is different. Well, however...</p>
</div>
<div id="comment-23678-info" class="comment-info">
<span class="comment-age">(25 Jun '13, 14:39)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-23661" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23661-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="23656"></span>

<div id="answer-container-23656" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23656-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23656-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-23656-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>you can view an objects info by opening that page: <a href="http://www.openstreetmap.org/browse/relation/NUMBERHERE">http://www.openstreetmap.org/browse/relation/NUMBERHERE</a> - there you also can see the object history and version numbers</p>
<p>So, in <em>your example</em> it is: <a href="http://www.openstreetmap.org/browse/relation/2382578">http://www.openstreetmap.org/browse/relation/2382578</a> It seems that someone else edited that relation while you also did (it is currently version 40 and was 38 until <em>before</em> 25. June 2013, 00:18 UTC). I <em>guess</em> that means (since there does not seem to be a <a href="/questions/17006/what-to-do-when-changesets-overlap">conflict resolution</a> built in Potlatch2) that you either have to trash your edit (you seem not be able to save it) or use the undo function to go back to a step in your edit session where you did not touch that relation. You might be able to save the raw edit in an text editor if Potlatch2 displays it (in osm xml format) which you (or someone else) may be able to (maybe with hand editing) <span>upload manually</span>/with <span>JOSM</span>(?) later.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jun '13, 03:25</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jun '13, 03:38</strong> </span></p>
</div>
</div>
<div id="comments-container-23656" class="comments-container">
&#10;</div>
<div id="comment-tools-23656" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23656-form-container" class="comment-form-container">
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

