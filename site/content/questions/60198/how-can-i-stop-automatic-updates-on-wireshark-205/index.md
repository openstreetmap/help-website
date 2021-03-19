+++
type = "question"
title = "How can I stop Automatic Updates on Wireshark 2.0.5?"
description = '''I have Wireshark 2.0.5 installed on ~80 Windows 10 machines and the Wireshark Automatic Updates are causing the machines to reboot after updating which causes other issues for me. I can manually manage the updates separately at a desired time so really I just want to stop Wireshark from checking for...'''
date = "2017-03-20T07:16:00Z"
lastmod = "2017-03-20T07:43:00Z"
weight = 60198
keywords = [ "windows", "updates" ]
aliases = [ "/questions/60198" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How can I stop Automatic Updates on Wireshark 2.0.5?](/questions/60198/how-can-i-stop-automatic-updates-on-wireshark-205)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60198-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60198-score" class="post-score" title="current number of votes">0</div><span id="post-60198-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have Wireshark 2.0.5 installed on ~80 Windows 10 machines and the Wireshark Automatic Updates are causing the machines to reboot after updating which causes other issues for me. I can manually manage the updates separately at a desired time so really I just want to stop Wireshark from checking for updates and prompting the users to install which triggers a reboot.</p><p>I have not been able to find an option to shut of the Wireshark Updates. Is there a simple check box somewhere I'm missing or can I set something in the registry of these machines to suppress updates?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-updates" rel="tag" title="see questions tagged &#39;updates&#39;">updates</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Mar '17, 07:16</strong></p><img src="https://secure.gravatar.com/avatar/9e89f55b0dcc001fa8875a63f81ad77e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Parking&#39;s gravatar image" /><p><span>Parking</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Parking has no accepted answers">0%</span></p></div></div><div id="comments-container-60198" class="comments-container"></div><div id="comment-tools-60198" class="comment-tools"></div><div class="clear"></div><div id="comment-60198-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60200"></span>

<div id="answer-container-60200" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60200-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60200-score" class="post-score" title="current number of votes">2</div><span id="post-60200-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Parking has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's in Preferences -&gt; Advanced, then search for gui.update.enabled. This can also be set in the preferences file, the preference uses the same name.</p><p>As an aside it seems odd that an update forces an OS reboot, I've never seen that, unless maybe you have some element of the wireshark suite running continuously.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '17, 07:26</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-60200" class="comments-container"><span id="60201"></span><div id="comment-60201" class="comment"><div id="post-60201-score" class="comment-score"></div><div class="comment-text"><p>Great. Thanks a lot! That looks like it will do the trick.</p><p>To your aside - I am finding these machines in a bad state after a reboot and reviewing the event logs to try and determine what caused the reboot. Entries I've found so far point to Wireshark so if I can disable the autoupdate that seems like an easy work around. Sanitized event log copied below as an example:</p><p>The process C:\Users\XXXXXXXXXXX\AppData\Local\Temp\Update-a6e2430d-1c59-4944-968b-d623cfefb4ca\Wireshark-win64-2.2.5.exe (XXXXXXXXX) has initiated the restart of computer XXXXXXXXX on behalf of user XXXXXXXXX\XXXXXXXXX for the following reason: Application: Installation (Planned) Reason Code: 0x80040002 Shutdown Type: restart Comment:</p></div><div id="comment-60201-info" class="comment-info"><span class="comment-age">(20 Mar '17, 07:43)</span> <span class="comment-user userinfo">Parking</span></div></div></div><div id="comment-tools-60200" class="comment-tools"></div><div class="clear"></div><div id="comment-60200-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

