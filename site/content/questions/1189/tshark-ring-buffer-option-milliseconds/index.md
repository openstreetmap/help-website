+++
type = "question"
title = "tshark ring buffer option: milliseconds"
description = '''Hi,  i need to know how can i use ring buffer option with a duration in milliseconds in the help menu there is only the possibility to listen for seconds  if it is not possible to do it in this version can you do it for me or at least give an hence how to do it and i will try to change it on the cod...'''
date = "2010-12-01T05:33:00Z"
lastmod = "2010-12-01T11:09:00Z"
weight = 1189
keywords = [ "buffer", "ring", "tshark", "milliseconds", "option" ]
aliases = [ "/questions/1189" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark ring buffer option: milliseconds](/questions/1189/tshark-ring-buffer-option-milliseconds)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1189-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>i need to know how can i use ring buffer option with a duration in milliseconds in the help menu there is only the possibility to listen for seconds if it is not possible to do it in this version can you do it for me or at least give an hence how to do it and i will try to change it on the code.</p></div><div id="question-tags" class="tags-container tags">buffer ring tshark milliseconds option</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '10, 05:33</strong></p><img src="https://secure.gravatar.com/avatar/3f02de51a4a84a398abe4365fbcc6135?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yassine&#39;s gravatar image" /><p>yassine<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yassine has no accepted answers">0%</span></p></div></div><div id="comments-container-1189" class="comments-container"><span id="1192"></span><div id="comment-1192" class="comment"><div id="post-1192-score" class="comment-score"></div><div class="comment-text"><p>Why would you want to capture only for milliseconds? Do you have a capture scenario where a second long ring buffer is too large? I never heard of that :-)</p><p>Or are you talking about the desired time resolution of the frame timestamps?</p></div><div id="comment-1192-info" class="comment-info"><span class="comment-age">(01 Dec '10, 09:40)</span> Jasper ♦♦</div></div><span id="1224"></span><div id="comment-1224" class="comment"><div id="post-1224-score" class="comment-score"></div><div class="comment-text"><p>it's not the problem of how long a ring buffer is during 1 second or more but i just need a scope of the network traffic of some milliseconds (300 or 500mseconds) to get an instantaneous overview of throughput to get some decisions afterwards.</p></div><div id="comment-1224-info" class="comment-info"><span class="comment-age">(03 Dec '10, 02:27)</span> yassine</div></div></div><div id="comment-tools-1189" class="comment-tools"></div><div class="clear"></div><div id="comment-1189-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1193"></span>

<div id="answer-container-1193" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1193-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It is not possible to select subsecond rotate intervals. It would be possible to add this to the source, but it needs to be done in several places. At least in the following locations:</p><pre><code>$ srcfgrep has_file_duration *
capture_opts.c
capture_opts.h
capture_sync.c
dumpcap.c
gtk/capture_dlg.c
gtk/main.c
tshark.c
$</code></pre><p>For the moment, you might want to use dumpcap to make capture slices of 1 second and use "editcap -c" to split into files with a certain amount of packets (editcap -i also uses whole seconds unfortunately).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Dec '10, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1193" class="comments-container"></div><div id="comment-tools-1193" class="comment-tools"></div><div class="clear"></div><div id="comment-1193-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

