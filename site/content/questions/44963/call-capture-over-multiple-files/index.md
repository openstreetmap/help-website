+++
type = "question"
title = "Call capture over multiple files"
description = '''Writing out files every 5 minutes. Trying to trace a VOIP call that was over 15 minutes in length. Only getting 1st 5 minutes. How do I find the rest of the call ??'''
date = "2015-08-11T09:15:00Z"
lastmod = "2015-08-13T14:40:00Z"
weight = 44963
keywords = [ "multiple", "voip" ]
aliases = [ "/questions/44963" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Call capture over multiple files](/questions/44963/call-capture-over-multiple-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44963-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Writing out files every 5 minutes. Trying to trace a VOIP call that was over 15 minutes in length. Only getting 1st 5 minutes. How do I find the rest of the call ??</p></div><div id="question-tags" class="tags-container tags">multiple voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Aug '15, 09:15</strong></p><img src="https://secure.gravatar.com/avatar/a59daf47d0093a7b43be280547540279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rtorrey&#39;s gravatar image" /><p>rtorrey<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rtorrey has no accepted answers">0%</span></p></div></div><div id="comments-container-44963" class="comments-container"></div><div id="comment-tools-44963" class="comment-tools"></div><div class="clear"></div><div id="comment-44963-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="44964"></span>

<div id="answer-container-44964" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44964-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If your problem is, that the call has been splitted into 3 files, then you could use the tool mergecap to merge these files into one. Mergecap is part of the wireshark package. After you have merged the tracefiles you should be able to find the rest of the call.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Aug '15, 09:54</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Aug '15, 14:42</p></div></div><div id="comments-container-44964" class="comments-container"></div><div id="comment-tools-44964" class="comment-tools"></div><div class="clear"></div><div id="comment-44964-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="45081"></span>

<div id="answer-container-45081" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45081-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>use <strong>mergecap</strong>. It will merge separeted pcap file into one big pcap, and than open by wireshark.</p><p>SYNOPSIS mergecap [ -a ] [ -F &lt;file format=""&gt; ] [ -h ] [ -s &lt;snaplen&gt; ] [ -T &lt;encapsulation type=""&gt; ] [ -v ] -w &lt;outfile&gt;|- &lt;infile&gt; [&lt;infile&gt; ...]</p><p>mergecap -w result.pcap 1_part.pcap 2_part.pcap 3_part.pcap ...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '15, 14:40</strong></p><img src="https://secure.gravatar.com/avatar/0319823751d2656828f8f21f22b90b05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sindar&#39;s gravatar image" /><p>Sindar<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sindar has no accepted answers">0%</span></p></div></div><div id="comments-container-45081" class="comments-container"></div><div id="comment-tools-45081" class="comment-tools"></div><div class="clear"></div><div id="comment-45081-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

