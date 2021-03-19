+++
type = "question"
title = "runtime error after changing the detail type of time field"
description = '''The wireshark version is &#x27;1.8.1&#x27;. After I changed the detail type of time field to &#x27;U-time..xxx&#x27; Whenever I open the file, runtime error occurs. The content of runtime error is following Runtime Error! Program:C&#92;Program Files&#92;Wireshark&#92;wireshark.exe This application has requested the Runtime to term...'''
date = "2012-12-17T17:50:00Z"
lastmod = "2012-12-17T23:14:00Z"
weight = 17000
keywords = [ "runtime" ]
aliases = [ "/questions/17000" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [runtime error after changing the detail type of time field](/questions/17000/runtime-error-after-changing-the-detail-type-of-time-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17000-score" class="post-score" title="current number of votes">0</div><span id="post-17000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The wireshark version is '1.8.1'.</p><p>After I changed the detail type of time field to 'U-time..xxx' Whenever I open the file, runtime error occurs.</p><p>The content of runtime error is following</p><p>Runtime Error! Program:C\Program Files\Wireshark\wireshark.exe This application has requested the Runtime to terminate it in an unusual way. Please contact the application's support team for more information.</p><p>I removed the wireshark and re-installed but the problem is remained, still.</p><p>Could you let me know the way how to resolve this problem?</p><p>From Lucy CHOI</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-runtime" rel="tag" title="see questions tagged &#39;runtime&#39;">runtime</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Dec '12, 17:50</strong></p><img src="https://secure.gravatar.com/avatar/1def5c4be5d224064ce687df570a5192?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lucychoi&#39;s gravatar image" /><p><span>lucychoi</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lucychoi has no accepted answers">0%</span></p></div></div><div id="comments-container-17000" class="comments-container"><span id="17002"></span><div id="comment-17002" class="comment"><div id="post-17002-score" class="comment-score"></div><div class="comment-text"><p>Given that a crash occurred, probably a bug.</p><p>Please file a bug report at <a href="http://bugs.wireshark.org">bugs.wireshark.org</a> with specific details as to how to create the problem.</p><p>Does this happen only with a specific file or with all capture files?</p><p>If the problem happens only with a specific file, please attach that file to the bug report if possible.</p><p>(You can mark the bug report as private. if necessary, so that only the Wireshark core developers wil have access to the capture file).</p><p>Thanks</p></div><div id="comment-17002-info" class="comment-info"><span class="comment-age">(17 Dec '12, 18:01)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="17003"></span><div id="comment-17003" class="comment"><div id="post-17003-score" class="comment-score"></div><div class="comment-text"><p>P.S. Are you changing the time format using 'View ! Time display Format ! UTC ...' from the toolbar.</p><p>I tried doing that with my version of Wireshark 1.8 (1.8.4) and did not have any problems.</p><p>Can you download 1.8.4 and see if the problem exists in that version?</p></div><div id="comment-17003-info" class="comment-info"><span class="comment-age">(17 Dec '12, 18:16)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="17007"></span><div id="comment-17007" class="comment"><div id="post-17007-score" class="comment-score"></div><div class="comment-text"><p>Thanks for you response. I updated the Wireshark 1.8.4 and the problem is solved.</p></div><div id="comment-17007-info" class="comment-info"><span class="comment-age">(17 Dec '12, 23:14)</span> <span class="comment-user userinfo">lucychoi</span></div></div></div><div id="comment-tools-17000" class="comment-tools"></div><div class="clear"></div><div id="comment-17000-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

