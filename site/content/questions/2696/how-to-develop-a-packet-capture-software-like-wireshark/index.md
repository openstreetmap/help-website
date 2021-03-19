+++
type = "question"
title = "how to develop a packet capture software like wireshark?"
description = '''Resently, i want to develop a software just like wireshark. but i do not have much knowledge about GTK/PYTHON, i am a windows user. I wonder to know how thoese technology assemble together in wireshark. i want to do this in VS2010 and use sharppcap, but there is not much parse, can some one give me ...'''
date = "2011-03-07T06:46:00Z"
lastmod = "2011-03-07T18:24:00Z"
weight = 2696
keywords = [ "sharppcap", "vs2010" ]
aliases = [ "/questions/2696" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to develop a packet capture software like wireshark?](/questions/2696/how-to-develop-a-packet-capture-software-like-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2696-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Resently, i want to develop a software just like wireshark. but i do not have much knowledge about GTK/PYTHON, i am a windows user. I wonder to know how thoese technology assemble together in wireshark. i want to do this in VS2010 and use sharppcap, but there is not much parse, can some one give me some advice about how to develop such a software in windows? thanks very much.</p></div><div id="question-tags" class="tags-container tags">sharppcap vs2010</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Mar '11, 06:46</strong></p><img src="https://secure.gravatar.com/avatar/b22011c3ec8b4ad641f57045ce47aa80?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="underwater0909&#39;s gravatar image" /><p>underwater0909<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="underwater0909 has no accepted answers">0%</span></p></div></div><div id="comments-container-2696" class="comments-container"></div><div id="comment-tools-2696" class="comment-tools"></div><div class="clear"></div><div id="comment-2696-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2704"></span>

<div id="answer-container-2704" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2704-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to write something just like Wireshark, the first thing to do is to find enough time to write about 2.8 million lines of code. You might be able to reduce the number of lines of code to write if you develop code to read protocol description languages such as ASN.1, one of the DCE RPC interface description languages (OSF's IDL, Microsoft's MIDL, or Samba's PIDL), rpcgen, and perhaps a language for protocols not natively described in such a language, and dissect those protocols by reading a description of the protocol.</p><p>I.e., writing software "just like Wireshark" is not an easy task. It would take many pages worth of answer here just to give you enough advice to be useful at all. The GUI part is probably one of the easier parts - there may be a lot of code to write, but it's probably pretty mechanical. Writing code to dissect packets and to display the results is the hard part.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Mar '11, 18:24</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-2704" class="comments-container"></div><div id="comment-tools-2704" class="comment-tools"></div><div class="clear"></div><div id="comment-2704-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

