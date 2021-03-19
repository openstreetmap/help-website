+++
type = "question"
title = "wireshark and dct3trace of LAPDm stored in xml"
description = '''Ocasionaly I use wireshark to decode LAPDm sent in GSM in call setup, reception etc. I use gammu for this purpose and the dump is stored in the xml file. Unfortunately, wireshark does no longer properly interpret this file and shows XML contents instead of separated packets as it worked previously. ...'''
date = "2016-03-26T23:20:00Z"
lastmod = "2016-03-27T13:09:00Z"
weight = 51220
keywords = [ "xml", "lapdm", "gsm" ]
aliases = [ "/questions/51220" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark and dct3trace of LAPDm stored in xml](/questions/51220/wireshark-and-dct3trace-of-lapdm-stored-in-xml)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51220-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Ocasionaly I use wireshark to decode LAPDm sent in GSM in call setup, reception etc. I use gammu for this purpose and the dump is stored in the xml file. Unfortunately, wireshark does no longer properly interpret this file and shows XML contents instead of separated packets as it worked previously. The sample dump from wireshark's page "gsm_call_1525.xml" is also improperly interpreted. I've tested Ubuntu 15.10, PPA and windows versions. All of them behave the same way. As I can recall, the version from Ubuntu 14.04 worked fine. Can somebody help/advice me to get things working back?</p></div><div id="question-tags" class="tags-container tags">xml lapdm gsm</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Mar '16, 23:20</strong></p><img src="https://secure.gravatar.com/avatar/759c0a717a5e340747a060298e195777?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pz2372901&#39;s gravatar image" /><p>pz2372901<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pz2372901 has no accepted answers">0%</span></p></div></div><div id="comments-container-51220" class="comments-container"></div><div id="comment-tools-51220" class="comment-tools"></div><div class="clear"></div><div id="comment-51220-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="51222"></span>

<div id="answer-container-51222" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51222-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As Wireshark 2.x has the ability to read and display XML files directly, the file type has to be explicitly set to be a Gammu DCT3 trace to be dissected accordingly.</p><p>This is done in the "Open Capture file" dialog, by changing the droplist that appears just below "Read Filter:" from the default of "Automatic" to "Gammu DCT3 trace".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '16, 11:05</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-51222" class="comments-container"><span id="51224"></span><div id="comment-51224" class="comment"><div id="post-51224-score" class="comment-score"></div><div class="comment-text"><p>That's not new in 2.x; I just built 1.12 from source and it also fails to identify the file as a Gammu dump.</p></div><div id="comment-51224-info" class="comment-info"><span class="comment-age">(27 Mar '16, 12:51)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-51222" class="comment-tools"></div><div class="clear"></div><div id="comment-51222-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="51225"></span>

<div id="answer-container-51225" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51225-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is a bug. I've checked a fix into the master, 2.0, and 1.12 branches, so the fix should show up in the next 2.0.x and 1.12.x releases.</p><p>We don't determine whether, or when, they're picked up by distributions, so we don't know whether or when the fix will show up in Ubuntu's repositories. The PPA might pick up the next release when it comes out; if you want something for Ubuntu sooner, you'll have to build from source.</p><p>For Windows, if you want something sooner than when the release comes out, you'd have to pick up one of the <a href="https://www.wireshark.org/download/automated/win32/">32-bit</a> or <a href="https://www.wireshark.org/download/automated/win64/">64-bit</a> automatic builds. The 2.0.x Windows builds are currently in progress; when they finish, new "2.0.3rc0" builds should show up in those directories. Don't get the gd6ea557 builds, those are the current ones which don't have the fix; wait for a newer one to appear.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '16, 13:09</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-51225" class="comments-container"><span id="51227"></span><div id="comment-51227" class="comment"><div id="post-51227-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot for both answers as they resolve the issue. I can live with manual selection of dump type although automagic recognition is welcomed. In the near future I'm going to upgrade to Ubuntu LTS 16.*. I hope that developers pick up the corrected version. Thanks to grahamb and Guy Harris one more time.</p></div><div id="comment-51227-info" class="comment-info"><span class="comment-age">(27 Mar '16, 22:45)</span> pz2372901</div></div></div><div id="comment-tools-51225" class="comment-tools"></div><div class="clear"></div><div id="comment-51225-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

