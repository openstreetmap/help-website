+++
type = "question"
title = "Internal error when merging files"
description = '''I have an issue with windows 7 64 Bit when trying to use the merge function in Wireshark Version 1.12.1 (v1.12.1-0-g01b65bf from master-1.12) I get an internal error when it tries to read the file from my local temporary files directory. It&#x27;s 32 bit wireshark. I tried opening Wireshark as Admin. I t...'''
date = "2014-09-17T06:43:00Z"
lastmod = "2014-09-17T13:52:00Z"
weight = 36405
keywords = [ "files", "merging" ]
aliases = [ "/questions/36405" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Internal error when merging files](/questions/36405/internal-error-when-merging-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36405-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an issue with windows 7 64 Bit when trying to use the merge function in Wireshark Version 1.12.1 (v1.12.1-0-g01b65bf from master-1.12) I get an internal error when it tries to read the file from my local temporary files directory. It's 32 bit wireshark.</p><p>I tried opening Wireshark as Admin. I tried mergecap.exe from command prompt, also as admin I updated wireshark this morning There is no errors in application logs on computer management</p></div><div id="question-tags" class="tags-container tags">files merging</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Sep '14, 06:43</strong></p><img src="https://secure.gravatar.com/avatar/f10b85b5d1ecabfe557a84e76ea907af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MrComputerSaint&#39;s gravatar image" /><p>MrComputerSaint<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MrComputerSaint has no accepted answers">0%</span></p></div></div><div id="comments-container-36405" class="comments-container"><span id="36417"></span><div id="comment-36417" class="comment"><div id="post-36417-score" class="comment-score"></div><div class="comment-text"><p>What is the exact text of the error message?</p></div><div id="comment-36417-info" class="comment-info"><span class="comment-age">(17 Sep '14, 12:19)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-36405" class="comment-tools"></div><div class="clear"></div><div id="comment-36405-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36424"></span>

<div id="answer-container-36424" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36424-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>In most cases merging fails when there are more than one capture interface present in the files that are being merged. This is only relevant for PCAPng files though. You can check how many interfaces a file has by opening the summary statistics - if you see more than one interface in the table in the middle of the dialog you can't merge the files with Wireshark or mergecap at this time.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '14, 13:52</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-36424" class="comments-container"><span id="36522"></span><div id="comment-36522" class="comment"><div id="post-36522-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper, it does indeed have 2 interfaces.</p><p>Kind regards, Andrew</p></div><div id="comment-36522-info" class="comment-info"><span class="comment-age">(23 Sep '14, 07:16)</span> MrComputerSaint</div></div><span id="45382"></span><div id="comment-45382" class="comment"><div id="post-45382-score" class="comment-score"></div><div class="comment-text"><p>Hi guys - is there any workaround for this?</p></div><div id="comment-45382-info" class="comment-info"><span class="comment-age">(26 Aug '15, 23:30)</span> Scott Harman</div></div><span id="45385"></span><div id="comment-45385" class="comment"><div id="post-45385-score" class="comment-score">1</div><div class="comment-text"><p>Try the top of trunk version there has been fixes made to the merge code, if it still fails opening a bug and attaching the two files would help to get it fixed.</p></div><div id="comment-45385-info" class="comment-info"><span class="comment-age">(27 Aug '15, 00:32)</span> Anders ♦</div></div><span id="45391"></span><div id="comment-45391" class="comment"><div id="post-45391-score" class="comment-score"></div><div class="comment-text"><p>You can also try to use TraceWrangler if you're running Windows. Add your files, create a "Merge" task and let it run. If it doesn't work let me know.</p><p><a href="https://www.tracewrangler.com">https://www.tracewrangler.com</a></p></div><div id="comment-45391-info" class="comment-info"><span class="comment-age">(27 Aug '15, 02:23)</span> Jasper ♦♦</div></div></div><div id="comment-tools-36424" class="comment-tools"></div><div class="clear"></div><div id="comment-36424-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

