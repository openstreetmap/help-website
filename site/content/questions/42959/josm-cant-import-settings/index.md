+++
type = "question"
title = "JOSM Can&#x27;t import settings"
description = '''Josm 8227 Win 7 x64 I reinstalled my Windows and before doing so, I made a backup in JOSM -&amp;gt; Preferences -&amp;gt; Advanced Preferences (selected all items, Export selected items) Now when I try to import them back (Read from file) I get the following error: Error: initializing script engine: null --...'''
date = "2015-05-08T15:41:00Z"
lastmod = "2015-05-09T11:54:00Z"
weight = 42959
keywords = [ "josm", "settings", "import" ]
aliases = [ "/questions/42959" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM Can't import settings](/questions/42959/josm-cant-import-settings)

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
<span id="post-42959-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42959-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-42959-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Josm 8227 Win 7 x64</p>
<p>I reinstalled my Windows and before doing so, I made a backup in JOSM -&gt; Preferences -&gt; Advanced Preferences (selected all items, Export selected items) Now when I try to import them back (Read from file) I get the following error:</p>
<p>Error: initializing script engine: null -- Reading custom preferences from D:\BACKUP 2015\josmprefs.xml -- Error reading custom preferences: null</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-settings" rel="tag" title="see questions tagged &#39;settings&#39;">settings</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 May '15, 15:41</strong></p>
<img src="https://secure.gravatar.com/avatar/af25b14055c51c8dff210afa47ae7c4a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="diversik&#39;s gravatar image" />
<p><span>diversik</span><br />
<span class="score" title="86 reputation points">86</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="diversik has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-42959" class="comments-container">
<span id="42975"></span>
<div id="comment-42975" class="comment">
<div id="post-42975-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>for the next time: I would suggest to just copy (and copy back from the backup) your full josm settings directory (under Linux it is <code>~/.josm</code>; under Windows maybe <code>%APPDATA%\JOSM</code>)</p>
</div>
<div id="comment-42975-info" class="comment-info">
<span class="comment-age">(08 May '15, 21:08)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-42959" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42959-form-container" class="comment-form-container">
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

<span id="42979"></span>

<div id="answer-container-42979" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42979-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42979-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-42979-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks for all the answers.</p>
<p>Installing the scripting plugin didn't help, same message. Installing some of the other plugins didn't help either (although I don't remember exactly which plugins I had before, could be one or two missing in the present install). I didn't thought about the plugins when I did the backup, I expected the list for the current installed plugins would be contained inside the exported xml and at the time of the import JOSM would download them again.</p>
<p>I managed to solve the problem by copy/pasting the proper data from the exported .xml into %APPDATA%\JOSM\preferences.xml</p>
<p>It was the same version for josm and OS, same permissions as before.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 May '15, 09:00</strong></p>
<img src="https://secure.gravatar.com/avatar/af25b14055c51c8dff210afa47ae7c4a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="diversik&#39;s gravatar image" />
<p><span>diversik</span><br />
<span class="score" title="86 reputation points">86</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="diversik has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-42979" class="comments-container">
<span id="42983"></span>
<div id="comment-42983" class="comment">
<div id="post-42983-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>meta: could you please add the stuff about the scripting plugin as a separate comment, so that your actual solution is alone? This way someone with the same problem would not need to read all the stuff which does not work. :-)</p>
</div>
<div id="comment-42983-info" class="comment-info">
<span class="comment-age">(09 May '15, 10:58)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="42985"></span>
<div id="comment-42985" class="comment">
<div id="post-42985-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd have thought that "what was tried but didn't work" was pretty relevant as part of an answer that describes clearly "what did work"?</p>
</div>
<div id="comment-42985-info" class="comment-info">
<span class="comment-age">(09 May '15, 11:20)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="42987"></span>
<div id="comment-42987" class="comment">
<div id="post-42987-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>: hmm, I would rather have it near the initial suggestions (maybe as a "comment" to mmd's suggestion which could be an "answer" too). In any case and whereever, "what did not work" is a very useful info. Okay... maybe delete our comments when read. ;-)</p>
</div>
<div id="comment-42987-info" class="comment-info">
<span class="comment-age">(09 May '15, 11:54)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-42979" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42979-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="42974"></span>

<div id="answer-container-42974" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42974-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42974-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42974-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>i think <a href="https://josm.openstreetmap.de/newticket">josm trac</a> is the better place for this question.</p>
<p>i'm using ubuntu so far. i could only speculate: same josm version? correct permission settings? and so on.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 May '15, 19:52</strong></p>
<img src="https://secure.gravatar.com/avatar/28022acb1185a8e23ba0147486b02479?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harald%20Hartmann&#39;s gravatar image" />
<p><span>Harald Hartmann</span><br />
<span class="score" title="111 reputation points">111</span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harald Hartmann has one accepted answer">33%</span></p>
</div>
</div>
<div id="comments-container-42974" class="comments-container">
&#10;</div>
<div id="comment-tools-42974" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42974-form-container" class="comment-form-container">
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

