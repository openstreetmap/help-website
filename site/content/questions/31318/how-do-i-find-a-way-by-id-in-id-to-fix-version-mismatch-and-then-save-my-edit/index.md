+++
type = "question"
title = "How do I find a way by ID in iD to fix &quot;version mismatch&quot; and then save my edit"
description = '''I got the error &quot;Version mismatch&quot; today while trying to save. Is there a way for me to find a way by ID in the iD editor? Is there a way for me to get rid of this error so I can save my additions?'''
date = "2014-03-05T10:51:00Z"
lastmod = "2016-04-29T10:24:00Z"
weight = 31318
keywords = [ "ideditor", "conflicts", "mismatch", "id", "save-changes" ]
aliases = [ "/questions/31318" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How do I find a way by ID in iD to fix "version mismatch" and then save my edit](/questions/31318/how-do-i-find-a-way-by-id-in-id-to-fix-version-mismatch-and-then-save-my-edit)

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
<span id="post-31318-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31318-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-31318-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I got the <a href="http://imgur.com/TJxr4iE">error "Version mismatch" today while trying to save</a>.</p>
<p>Is there a way for me to find a way by ID in the iD editor? Is there a way for me to get rid of this error so I can save my additions?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-conflicts" rel="tag" title="see questions tagged &#39;conflicts&#39;">conflicts</span> <span class="post-tag tag-link-mismatch" rel="tag" title="see questions tagged &#39;mismatch&#39;">mismatch</span> <span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span> <span class="post-tag tag-link-save-changes" rel="tag" title="see questions tagged &#39;save-changes&#39;">save-changes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Mar '14, 10:51</strong></p>
<img src="https://secure.gravatar.com/avatar/5290f47440ef77fc3feb598142a95a11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ubuzen&#39;s gravatar image" />
<p><span>ubuzen</span><br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ubuzen has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Mar '14, 14:48</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-31318" class="comments-container">
<span id="31445"></span>
<div id="comment-31445" class="comment">
<div id="post-31445-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I also get the error: "Version mismatch: Provided 10, server had: 11 of Way 43318104". It looks like ID editor has screwed up as I have comitted the version 10 and 11 and continued my edits. Undo/redo didn't make sense as the conflict was exactly on the first object that was modified after the last save. So unless I undo one hour of my work I cannot get around this bug.</p>
<p>Why not to make ID editor to skip once there is a conflict with particular node and let user commit the rest of the features?</p>
<p>Now, these nasty bugs make lose lots of work although they affect maybe just one small object out of the whole changeset.</p>
</div>
<div id="comment-31445-info" class="comment-info">
<span class="comment-age">(11 Mar '14, 13:54)</span> <span class="comment-user userinfo">sauls</span>
</div>
</div>
<span id="31446"></span>
<div id="comment-31446" class="comment">
<div id="post-31446-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It is hard for the editor to determine of omitting a single object would cause just a minor or a major problem. For example omitting a way from a boundary relation or a coastline could cause more serious problems which aren't easy to spot, whereas omitting a bench or street lamp wouldn't cause any problems at all. In my opinion a better solution would be to display a warning in all editors if the user edited for more than 15 minutes without uploading his changes.</p>
</div>
<div id="comment-31446-info" class="comment-info">
<span class="comment-age">(11 Mar '14, 14:00)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="31448"></span>
<div id="comment-31448" class="comment">
<div id="post-31448-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you can remember what happened (perhaps on the <a href="http://api06.dev.openstreetmap.org/">dev server</a>) I'm sure the iD developers would be keen to investigate. The relevant live issue seems to be <a href="https://github.com/openstreetmap/iD/issues/1053">this one</a>.</p>
</div>
<div id="comment-31448-info" class="comment-info">
<span class="comment-age">(11 Mar '14, 14:40)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-31318" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31318-form-container" class="comment-form-container">
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

<span id="49473"></span>

<div id="answer-container-49473" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49473-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49473-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-49473-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I just ran across this issue and came up with a workaround. I was using Chrome at the time so the procedure is for Chrome. You’ll also need JOSM (or another tool which can open an <code>osc</code> file) and knowledge on how to resolve versioning conflicts. When I have some time I’ll try to find an equivalent workflow for Firefox.</p>
<ol>
<li>In Chrome, press F12 to display the Developer Tools window.</li>
<li>Go to the <strong>Network</strong> tab</li>
<li>Go back to the Chrome window where you have iD open and try to save the changeset again.</li>
<li>Go back to the Developer Tools window</li>
<li>A column titled <strong>Name</strong> will be on the left-hand pane. Find the request titled <strong>upload</strong> and click on it.</li>
<li>On the right-hand pane, select <strong>Headers</strong> and find the section titled <strong>Request Payload</strong></li>
<li>Highlight and copy all the text below it, starting with <code>&lt;</code>﻿<code>osmChange</code>﻿<code>&gt;</code> and ending with <code>&lt;</code>﻿<code>/osmChange</code>﻿<code>&gt;</code> inclusive</li>
<li>In a text editor, paste the text and save the file with a <code>*.osc</code> extension using UTF-8 encoding. (If that’s not the default for your text editor, perhaps it’d be a good idea to change the encoding <em>before</em> pasting the text).</li>
<li>In JOSM (or an editor which supports osc files), open the osc file you just saved. All objects which you changed should be there.</li>
<li>Either download data for the bounding box, or select <strong>File &gt; Update modified</strong>.</li>
<li>Resolve the conflict as needed,.</li>
<li>Upload the changeset.</li>
</ol>
<p>The benefit here is that, even if you don’t have JOSM installed on the system on which you made the changes, you can take the osc file and perform the rest of the steps later when you do have JOSM on hand.</p>
<p>Hope it helps and saves you from having to throw away your changeset!</p>
<p>PS: at a minimum, I think iD should provide the ability to download the <code>osc</code> file for the changeset when a version conflict is encountered (or even better, at any time in case one wishes to continue at a later point).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Apr '16, 17:02</strong></p>
<img src="https://secure.gravatar.com/avatar/8dfc06314659f45fae00cb945dae0de2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="carciofo&#39;s gravatar image" />
<p><span>carciofo</span><br />
<span class="score" title="91 reputation points">91</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="carciofo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Apr '16, 17:04</strong> </span></p>
</div>
</div>
<div id="comments-container-49473" class="comments-container">
&#10;</div>
<div id="comment-tools-49473" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49473-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="31319"></span>

<div id="answer-container-31319" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31319-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31319-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-31319-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>From memory I believe that you need to undo back past the point where you modified that way, and then save there. Unfortunately I can't find anything written down to back that statement up. The iD issues list has lots of discussion about <a href="https://github.com/openstreetmap/iD/search?q=save&amp;ref=cmdform&amp;type=Issues">how "save" should work</a>, but I can't immediately see your problem (which I presume is "another mapper has modified a way in the meantime") listed.</p>
<p>In a separate browser window, you can look at the history of the way concerned:</p>
<p><a href="http://www.openstreetmap.org/way/151789937/history">http://www.openstreetmap.org/way/151789937/history</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '14, 12:50</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Mar '14, 13:51</strong> </span></p>
</div>
</div>
<div id="comments-container-31319" class="comments-container">
<span id="31320"></span>
<div id="comment-31320" class="comment">
<div id="post-31320-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sounds like try and error, because iD doesn't tell you which change needs to be undone.</p>
</div>
<div id="comment-31320-info" class="comment-info">
<span class="comment-age">(05 Mar '14, 13:37)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="31323"></span>
<div id="comment-31323" class="comment">
<div id="post-31323-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks. I wasn't about to spend hours testing which change in the list was the culprit. I just undid all my changes. That'll teach me to make big sets of changes; lesson learned. /r/openstreetmap suggested JOSM, so I'll be using that from now on instead of iD.</p>
</div>
<div id="comment-31323-info" class="comment-info">
<span class="comment-age">(05 Mar '14, 14:35)</span> <span class="comment-user userinfo">ubuzen</span>
</div>
</div>
<span id="31326"></span>
<div id="comment-31326" class="comment">
<div id="post-31326-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Note that any editor can lead to that error. But JOSM makes it possible to identify the corresponding way and to resolve possible conflicts (which doesn't mean that resolving conflicts in JOSM is trivial, though).</p>
</div>
<div id="comment-31326-info" class="comment-info">
<span class="comment-age">(05 Mar '14, 15:18)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-31319" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31319-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="42194"></span>

<div id="answer-container-42194" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42194-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42194-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42194-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>April 2015: looks like ID saves all but the problematical node. It is not clear from the message and it looks like nothing was saved, but when I was comming to the PC one hour later, changes were on the map (maybe without one node, I don't know).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Apr '15, 12:18</strong></p>
<img src="https://secure.gravatar.com/avatar/393b16c0c58f077dc06c7378837d26ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zvolsky&#39;s gravatar image" />
<p><span>zvolsky</span><br />
<span class="score" title="55 reputation points">55</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zvolsky has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-42194" class="comments-container">
<span id="49495"></span>
<div id="comment-49495" class="comment">
<div id="post-49495-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That wasn't the case for me (Apr 2016). iD Showed the error without the possibility to do anything about it.</p>
</div>
<div id="comment-49495-info" class="comment-info">
<span class="comment-age">(29 Apr '16, 10:24)</span> <span class="comment-user userinfo">carciofo</span>
</div>
</div>
</div>
<div id="comment-tools-42194" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42194-form-container" class="comment-form-container">
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

