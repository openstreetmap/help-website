+++
type = "question"
title = "JOSM: is there a way to automatically add a tag to new road segments ?"
description = '''Is there a way in JOSM to automatically add an extra tag to new road segments? Context: we are asking a corporate organization that does mass addition of new road segments using imagery only to include an additional custom tag, so we can identify those at a later stage. If there is no automatic way ...'''
date = "2022-02-05T03:24:00Z"
lastmod = "2022-02-05T17:06:00Z"
weight = 83347
keywords = [ "josm", "tag", "automatic" ]
aliases = [ "/questions/83347" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [JOSM: is there a way to automatically add a tag to new road segments ?](/questions/83347/josm-is-there-a-way-to-automatically-add-a-tag-to-new-road-segments)

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
<span id="post-83347-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83347-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83347-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way in JOSM to automatically add an extra tag to new road segments?</p>
<p>Context: we are asking a corporate organization that does mass addition of new road segments using imagery only to include an additional custom tag, so we can identify those at a later stage. If there is no automatic way to do this, they might be less inclined to do it as it will require more manual efforts from their side.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-tag" rel="tag" title="see questions tagged &#39;tag&#39;">tag</span> <span class="post-tag tag-link-automatic" rel="tag" title="see questions tagged &#39;automatic&#39;">automatic</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Feb '22, 03:24</strong></p>
<img src="https://secure.gravatar.com/avatar/e3f994b2488e2182c63a7c44a5028ff6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmoffroad&#39;s gravatar image" />
<p><span>cmoffroad</span><br />
<span class="score" title="205 reputation points">205</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmoffroad has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83347" class="comments-container">
&#10;</div>
<div id="comment-tools-83347" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83347-form-container" class="comment-form-container">
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

<span id="83352"></span>

<div id="answer-container-83352" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83352-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83352-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-83352-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cmoffroad has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think the best way to do it is through the use of custom presets. Each person in the organization would use the same presets which would help insure uniformity of tagging and would include the special tag import=yes, or grabimport=yes, or some other tag that everyone agrees on.</p>
<p>I use such presets in much of my tagging. A preset for highways should include choices for highway class, i.e, trunk, tertiary, primary, secondary, unclassified, etc., surface, smoothness, lanes, a checkbox for oneway, and additional attributes to be determined by consensus. While the attributes I mentioned would involve choices the import=yes tag would be automatically applied in every case.</p>
<p>There are many examples of how to construct these presets in the Wiki and also by inspecting the presets that are built into JOSM by its designers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Feb '22, 10:28</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-83352" class="comments-container">
&#10;</div>
<div id="comment-tools-83352" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83352-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83357"></span>

<div id="answer-container-83357" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83357-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83357-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83357-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could also apply the needed tag just before upload, by using a search like "<code>new highway=* type:way</code>". Still a manual operation, but only once by changeset.</p>
<p>On the other hand, custom tags for internal use are frowned upon. Other mapper might delete them, if they don't understand what it means. You'll have to clean them all at some point...</p>
<p>I think a more secure approach would be to ask the corporate mappers to use each a dedicated user for your job, and then review the changes based on usernames. <a href="https://osmcha.org/about#filters">Osmcha.org filters</a> might be a good solution for this. They also offer a <a href="https://github.com/mapbox/osmcha-frontend/wiki/Mapping-Teams">mapping team</a> functionality which might suit your case.</p>
<p>You should also be aware of the <a href="https://wiki.openstreetmap.org/wiki/Organised_Editing_Guidelines">Organised Editing Guidelines</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Feb '22, 14:41</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-83357" class="comments-container">
<span id="83365"></span>
<div id="comment-83365" class="comment">
<div id="post-83365-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Osmcha filters will not be sufficient, because when ways are split into multiple segments (often the case), the original history is lost.</p>
<p>This is a temporary tag, meant to be removed once local mappers do verification on the ground. Another company used similar approach many years ago.</p>
</div>
<div id="comment-83365-info" class="comment-info">
<span class="comment-age">(05 Feb '22, 16:26)</span> <span class="comment-user userinfo">cmoffroad</span>
</div>
</div>
<span id="83370"></span>
<div id="comment-83370" class="comment">
<div id="post-83370-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Osmcha filter changesets, so no trouble here. It's meant to review each and every changeset.</p>
<p>For what I understand of your use-case, manual check of the ways on the ground, I guess <code>source=armchair</code>, or <code>fixme=check on the ground</code> might be best indeed.</p>
<p>But the ever best would be to go on the ground before. And map from aerials only what is clearly visible, no guesswork.</p>
<p>Well, it's only my opinion, I map mostly in already well-mapped areas. Except for HOT activation, where I map conservatively, even if it means to leave gaps...</p>
</div>
<div id="comment-83370-info" class="comment-info">
<span class="comment-age">(05 Feb '22, 17:06)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-83357" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83357-form-container" class="comment-form-container">
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

