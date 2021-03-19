+++
type = "question"
title = "Why multiple files cannot be open simultaneously using Wireshark Portable on Windows?"
description = '''I would like to make sure that, can I open some Wireshark window at the same time for opening some packet files. I want to confront some packet files. I searched how to open some Wireshark window, but I could not find. Could anyone please tell me?'''
date = "2016-07-28T22:39:00Z"
lastmod = "2016-07-29T00:05:00Z"
weight = 54428
keywords = [ "instances", "portable" ]
aliases = [ "/questions/54428" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why multiple files cannot be open simultaneously using Wireshark Portable on Windows?](/questions/54428/why-multiple-files-cannot-be-open-simultaneously-using-wireshark-portable-on-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54428-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to make sure that, can I open some Wireshark window at the same time for opening some packet files. I want to confront some packet files. I searched how to open some Wireshark window, but I could not find.</p><p>Could anyone please tell me?</p></div><div id="question-tags" class="tags-container tags">instances portable</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jul '16, 22:39</strong></p><img src="https://secure.gravatar.com/avatar/318b7b62e2c158d79d648bc55130725b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shinya&#39;s gravatar image" /><p>Shinya<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shinya has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Jul '16, 02:14</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-54428" class="comments-container"></div><div id="comment-tools-54428" class="comment-tools"></div><div class="clear"></div><div id="comment-54428-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54429"></span>

<div id="answer-container-54429" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54429-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Not sure I've got your question right, but I'll try:</p><p>If you have a MAC as I suspect, the answer to <a href="https://ask.wireshark.org/questions/54036/open-multiple-captures-on-mac">this question</a> is what you look for. On other OSes, double-clicking on a capture file in a file list opens it in its own separate instance of Wireshark, i.e. in a separate window.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jul '16, 00:05</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-54429" class="comments-container"><span id="54434"></span><div id="comment-54434" class="comment"><div id="post-54434-score" class="comment-score"></div><div class="comment-text"><p>My environment is</p><ul><li>Windows 7 pro 64bit</li><li>Wireshark 2.0.5 portable</li></ul><p>If I open a packet file and I double-click another packet file, I see an error message. The message is "Another instance of Wireshark is already running. Please close other instances of Wireshark before launching Wireshark Portable". I can understand from the message that I cannot open another packet file if I open a packet file. But if there is a workaround, I want to know.</p><p>If I use the Wireshark (not portable version), can I open the packet file?</p></div><div id="comment-54434-info" class="comment-info"><span class="comment-age">(29 Jul '16, 02:06)</span> Shinya</div></div><span id="54435"></span><div id="comment-54435" class="comment"><div id="post-54435-score" class="comment-score"></div><div class="comment-text"><p>Wireshark portable is quite new so I have no experience with it. But I can confirm that the installed 2.0.5 on Windows (10 in my case) can run in multiple instances like it always could on Windows and Linux, i.e. you can open several files at the same time.</p><p>Let's wait for someone from the development team to shed some light. The wording of the error message suggests that the behaviour is intentional, not a bug.</p></div><div id="comment-54435-info" class="comment-info"><span class="comment-age">(29 Jul '16, 02:12)</span> sindy</div></div></div><div id="comment-tools-54429" class="comment-tools"></div><div class="clear"></div><div id="comment-54429-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

