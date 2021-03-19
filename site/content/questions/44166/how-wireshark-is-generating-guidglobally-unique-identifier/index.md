+++
type = "question"
title = "How wireshark is generating GUID(Globally unique identifier)?"
description = '''I created one plugin in lua. now i am making installer for that using NSIS At the time of uninstallation of my plugin i want to check if wireshark is running than donot uninstall it. I got logic todo that from wireshark.nsi(logic is defined in common.nsh) file.But in that logic there is mentioned on...'''
date = "2015-07-15T02:42:00Z"
lastmod = "2015-07-16T20:29:00Z"
weight = 44166
keywords = [ "uninstall", "nsis", "guid", "wireshark" ]
aliases = [ "/questions/44166" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How wireshark is generating GUID(Globally unique identifier)?](/questions/44166/how-wireshark-is-generating-guidglobally-unique-identifier)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44166-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44166-score" class="post-score" title="current number of votes">0</div><span id="post-44166-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I created one plugin in lua. now i am making installer for that using NSIS At the time of uninstallation of my plugin i want to check if wireshark is running than donot uninstall it. I got logic todo that from wireshark.nsi(logic is defined in common.nsh) file.But in that logic there is mentioned one GUID Number {<strong>9CA78EEA-EA4D-4490-9240-FC01FCEF464B</strong>}. The logic of that file is mentioned below</p><pre><code>${Do}

System::Call &#39;kernel32::OpenMutex(i 0x100000, b 0, t &quot;Global\${PROGRAM_NAME}-is-running-{9CA78EEA-EA4D-4490-9240-FC01FCEF464B}&quot;) i .R0&#39;
    IntCmp $R0 0 checkRunningSession
    System::Call &#39;kernel32::CloseHandle(i $R0)&#39;
    Goto isRunning

checkRunningSession:
System::Call &#39;kernel32::OpenMutex(i 0x100000, b 0, t &quot;${PROGRAM_NAME}-is-running-{9CA78EEA-EA4D-4490-9240-FC01FCEF464B}&quot;) i .R0&#39;
    IntCmp $R0 0 notRunning
    System::Call &#39;kernel32::CloseHandle(i $R0)&#39;

isRunning:
; You&#39;d better go catch it.
MessageBox MB_RETRYCANCEL|MB_ICONEXCLAMATION &quot;${PROGRAM_NAME} or one of its associated programs is running.$\r$\nPlease close it first.&quot; /SD IDCANCEL IDRETRY continueChecking
Quit

notRunning:
${ExitDo}</code></pre><p>I want to this GUID no is constant for wireshark?I mean is it same for platforms? If it so how it is integrated with Wireshark? Is it mentioned in wireshark source code?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-uninstall" rel="tag" title="see questions tagged &#39;uninstall&#39;">uninstall</span> <span class="post-tag tag-link-nsis" rel="tag" title="see questions tagged &#39;nsis&#39;">nsis</span> <span class="post-tag tag-link-guid" rel="tag" title="see questions tagged &#39;guid&#39;">guid</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '15, 02:42</strong></p><img src="https://secure.gravatar.com/avatar/8efce51fbbf3dbd6c9b9132056f45eb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ankit&#39;s gravatar image" /><p><span>ankit</span><br />
<span class="score" title="65 reputation points">65</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ankit has one accepted answer">25%</span></p></div></div><div id="comments-container-44166" class="comments-container"></div><div id="comment-tools-44166" class="comment-tools"></div><div class="clear"></div><div id="comment-44166-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44168"></span>

<div id="answer-container-44168" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44168-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44168-score" class="post-score" title="current number of votes">0</div><span id="post-44168-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ankit has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes it's a constant for all versions of Wireshark running on Windows and is defined in wsutil\file_util.c:</p><p><code>#define WIRESHARK_IS_RUNNING_UUID "9CA78EEA-EA4D-4490-9240-FC01FCEF464B"</code></p><p>arguably it should be in a header so it can be picked up by wireshark.nsi instead of being hard-coded, but it's unlikely to ever change.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '15, 03:42</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-44168" class="comments-container"><span id="44169"></span><div id="comment-44169" class="comment"><div id="post-44169-score" class="comment-score"></div><div class="comment-text"><p>Thanks <span>@grahamb</span> for quick reply.May be my next question to you is not specific to wireshark. but i am just curious to know that how you guys generated this ID and integrated with wireshark? because as far as i know about GUID. it is generated by system itself randomly or by GUIDgen tool</p></div><div id="comment-44169-info" class="comment-info"><span class="comment-age">(15 Jul '15, 04:00)</span> <span class="comment-user userinfo">ankit</span></div></div><span id="44171"></span><div id="comment-44171" class="comment"><div id="post-44171-score" class="comment-score"></div><div class="comment-text"><p>Probably via a tool. The commit message is <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commit;h=3ba2c108f13e513cab2b46566e35d2c3f0d24091">here</a>.</p><p>Generating and using a GUID in this manner is perfectly safe, what's your concern?</p></div><div id="comment-44171-info" class="comment-info"><span class="comment-age">(15 Jul '15, 05:39)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="44225"></span><div id="comment-44225" class="comment"><div id="post-44225-score" class="comment-score"></div><div class="comment-text"><p>Actually we have our own tool which is developed in Qt same as wireshark and it has problem like when the tool is open user can uninstall that but ideally it should not happen. then i have referred wireshark code to implement same logic to generate GUID. that's why i was asking. But now i get idea how to do that from your previous answer. Thanks again <span>@grahamb</span></p></div><div id="comment-44225-info" class="comment-info"><span class="comment-age">(16 Jul '15, 20:29)</span> <span class="comment-user userinfo">ankit</span></div></div></div><div id="comment-tools-44168" class="comment-tools"></div><div class="clear"></div><div id="comment-44168-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

