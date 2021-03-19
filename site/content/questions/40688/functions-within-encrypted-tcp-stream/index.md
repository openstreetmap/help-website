+++
type = "question"
title = "Functions within encrypted TCP stream"
description = '''Following an encrypted GET request stream of a downloaded file and find these functions in the body;  GetLocaleInfo SetCurrentDirectory FileTimeToLocalFileTime GetVolumePathName VirtualAllocEx DeleteFile GetStdHandle SetConsoleTitle GetProcessHeap CreateEvent DllUnregisterServer DllRegisterServer Dl...'''
date = "2015-03-19T08:07:00Z"
lastmod = "2015-03-19T14:16:00Z"
weight = 40688
keywords = [ "function", "stream", "string", "tcp" ]
aliases = [ "/questions/40688" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Functions within encrypted TCP stream](/questions/40688/functions-within-encrypted-tcp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40688-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Following an encrypted GET request stream of a downloaded file and find these functions in the body;</p><p>GetLocaleInfo SetCurrentDirectory FileTimeToLocalFileTime GetVolumePathName VirtualAllocEx DeleteFile GetStdHandle SetConsoleTitle GetProcessHeap CreateEvent DllUnregisterServer DllRegisterServer DllCanUnloadNow DllGetClassObject</p><p>I understand what each function does i.e. dllregisterserver will add a registry entry for the preceding dll but are these functions that are being executed on the system by the download or am I missing something?</p><p>Any advice will be appreciated, Thanks</p></div><div id="question-tags" class="tags-container tags">function stream string tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Mar '15, 08:07</strong></p><img src="https://secure.gravatar.com/avatar/0171ce5254e9e29367abc0d223242948?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="froggy101&#39;s gravatar image" /><p>froggy101<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="froggy101 has no accepted answers">0%</span></p></div></div><div id="comments-container-40688" class="comments-container"></div><div id="comment-tools-40688" class="comment-tools"></div><div class="clear"></div><div id="comment-40688-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40696"></span>

<div id="answer-container-40696" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40696-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>these functions that are being executed on the system by the download or am I missing something?</p></blockquote><p>Most certainly they are not executed by simply downloading the file. Based on your brief description, this could be almost anything, from a text file containing those string up to a binary with debug symbols showing the strings.</p><p>So, (most certainly) no reason to worry.</p><p>If you want a more detailed analysis, please upload the capture file somewhere (google drive, dropbox, cloudshark.org) and post the link here. <strong>However</strong>, as you've mentioned an encrypted connection, I guess the capture file won't help, unless you are able to post the key as well. If that's not possible, you can try to upload whatever you see with "Follow TCP Stream" (ASCII or screenshot), so we can have a look at that.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Mar '15, 14:16</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Mar '15, 14:17</p></div></div><div id="comments-container-40696" class="comments-container"></div><div id="comment-tools-40696" class="comment-tools"></div><div class="clear"></div><div id="comment-40696-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

