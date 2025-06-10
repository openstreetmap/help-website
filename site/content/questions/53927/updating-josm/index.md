+++
type = "question"
title = "Updating JOSM"
description = '''Hi, After updating JOSM from 11223 into 11427 the program can’t find old files, saved for security reasons ? It is an automated (Windows local update) and it’s not the first time ? Why are the old files not visible ? Is there a way to search in the menu of the PC with JOSM ? Or do I something wrong ...'''
date = "2017-01-08T20:45:00Z"
lastmod = "2017-01-10T21:45:00Z"
weight = 53927
keywords = [ "files", "josm", "update" ]
aliases = [ "/questions/53927" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Updating JOSM](/questions/53927/updating-josm)

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
<span id="post-53927-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53927-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53927-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, After updating JOSM from 11223 into 11427 the program can’t find old files, saved for security reasons ? It is an automated (Windows local update) and it’s not the first time ? Why are the old files not visible ? Is there a way to search in the menu of the PC with JOSM ? Or do I something wrong ? And yes I know too much questions, but they all belong to an update JOSM and its files ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-files" rel="tag" title="see questions tagged &#39;files&#39;">files</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jan '17, 20:45</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-53927" class="comments-container">
<span id="53931"></span>
<div id="comment-53931" class="comment">
<div id="post-53931-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Can you explain what "the program can't find old files" means? Do you mean JOSM .jar files, plugins, or other files?</p>
<p>Also how are you running JOSM? Various options are available ranging from "just running the .jar file" to an installation.</p>
</div>
<div id="comment-53931-info" class="comment-info">
<span class="comment-age">(08 Jan '17, 21:26)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="53935"></span>
<div id="comment-53935" class="comment">
<div id="post-53935-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The program runs smoothly, but the command file, sub 3 in the upper left corner stays blank after the update. Those files are made by choosing Ctrl S or Ctrl shift S. The menu file gives you the choice Open recent file.</p>
</div>
<div id="comment-53935-info" class="comment-info">
<span class="comment-age">(08 Jan '17, 22:55)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="53936"></span>
<div id="comment-53936" class="comment">
<div id="post-53936-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The menu choice File&gt;Open Recent might have been affected by that Windows Update. The lists of recent files are usually kept in the Windows Registry but JOSM keeps the list internally. Go to Preferences and then click the last entry in the left side settings menu, the one with the wrench, and search for "file-". You should see your file history and the maximum number of file names to save. If there are names present, I suspect the Windows Update is the culprit. Otherwise it's some sort of weird bug in JOSM that somebody else might know more about.</p>
<p>Cheers,</p>
<p>Dave</p>
</div>
<div id="comment-53936-info" class="comment-info">
<span class="comment-age">(08 Jan '17, 23:43)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="53971"></span>
<div id="comment-53971" class="comment">
<div id="post-53971-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I dont get it, the Windows installer is or has been created by the JOSM programmers as well. So the program should not loose its files from yesterday or archived ones, is not it ? I recon Ill have to send the "bug" to the programmers.</p>
</div>
<div id="comment-53971-info" class="comment-info">
<span class="comment-age">(10 Jan '17, 21:45)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
</div>
<div id="comment-tools-53927" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53927-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

