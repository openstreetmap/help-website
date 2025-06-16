+++
type = "question"
title = "How to make the Mac &quot;delete&quot; button work in JOSM?"
description = '''When running JOSM on Mac (either on MacOS directly, or in a VM), there is no actual &quot;delete&quot; button - the one that is labeled &quot;delete&quot; on the keyboard is actually backspace. &quot;Delete&quot; operation for map objects in the edit mode can be achieved by pressing &quot;Fn + delete&quot;, but this is rather inconvenient...'''
date = "2019-03-25T11:34:00Z"
lastmod = "2019-03-25T11:34:00Z"
weight = 68481
keywords = [ "josm", "mac", "keyboard", "delete" ]
aliases = [ "/questions/68481" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to make the Mac "delete" button work in JOSM?](/questions/68481/how-to-make-the-mac-delete-button-work-in-josm)

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
<span id="post-68481-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68481-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68481-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When running JOSM on Mac (either on MacOS directly, or in a VM), there is no actual "delete" button - the one that is labeled "delete" on the keyboard is actually backspace.</p>
<p>"Delete" operation for map objects in the edit mode can be achieved by pressing "Fn + delete", but this is rather inconvenient.</p>
<p>How can one reconfigure JOSM so that the hardware "delete" button removes selected objects in the map view?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-keyboard" rel="tag" title="see questions tagged &#39;keyboard&#39;">keyboard</span> <span class="post-tag tag-link-delete" rel="tag" title="see questions tagged &#39;delete&#39;">delete</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Mar '19, 11:34</strong></p>
<img src="https://secure.gravatar.com/avatar/ba4d3e91f235ed21dacc1766b94e26a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richlv&#39;s gravatar image" />
<p><span>Richlv</span><br />
<span class="score" title="1740 reputation points"><span>1.7k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richlv has 5 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-68481" class="comments-container">
&#10;</div>
<div id="comment-tools-68481" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68481-form-container" class="comment-form-container">
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

<span id="68482"></span>

<div id="answer-container-68482" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68482-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68482-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68482-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><strong>When running JOSM in a Linux VM</strong></p>
<ul>
<li>Go to Edit -&gt; Preferences (or press F12), switch to the keyboard tab (7th from the top) and enter "delete" in the "Search" field.</li>
<li>Select "Edit: Delete" and choose "Backspace" in the "Key" dropdown (usually near the top; you can also sequentially type "backs..." to jump to the correct entry).</li>
<li>Click "OK"</li>
</ul>
<p><img src="/upfiles/josm-delete-linux_.png" alt="JOSM preferences on Linux" /></p>
<p><strong>When running JOSM directly in MacOS</strong></p>
<ul>
<li>Go to Main -&gt; Preferences (or press command + ,), switch to the keyboard tab (at the time of this writing, the tiny icons on the left - 7th from the top) and enter "delete" in the "Search" field.</li>
<li>Select "Edit: Delete" and choose the arrow-like object that points to the left with an X on it in the "Key" dropdown (usually near the top; there does not seem to be an easy way to jump to it).</li>
<li>Click "OK"</li>
</ul>
<p><img src="/upfiles/josm-delete-macos.png" alt="JOSM preferences on MacOS" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Mar '19, 11:34</strong></p>
<img src="https://secure.gravatar.com/avatar/ba4d3e91f235ed21dacc1766b94e26a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richlv&#39;s gravatar image" />
<p><span>Richlv</span><br />
<span class="score" title="1740 reputation points"><span>1.7k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richlv has 5 accepted answers">22%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Mar '19, 11:46</strong> </span></p>
</div>
</div>
<div id="comments-container-68482" class="comments-container">
&#10;</div>
<div id="comment-tools-68482" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68482-form-container" class="comment-form-container">
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

