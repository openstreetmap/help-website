+++
type = "question"
title = "Text to PCAP, no option to save native trace in PCAP format!"
description = '''Hello, Does anyone know how to convert a text file to a PCAP? This is not a hex dump, it is a raw text file of what would be in a typical PCAP. The device im capturing from (ASR5000) displays the trace output in window with no ability to write it to a file so I have no ability to specify like i woul...'''
date = "2016-07-01T16:24:00Z"
lastmod = "2016-07-01T17:51:00Z"
weight = 53779
keywords = [ "text", "pcap", "help" ]
aliases = [ "/questions/53779" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Text to PCAP, no option to save native trace in PCAP format!](/questions/53779/text-to-pcap-no-option-to-save-native-trace-in-pcap-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53779-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Does anyone know how to convert a text file to a PCAP? This is not a hex dump, it is a raw text file of what would be in a typical PCAP. The device im capturing from (ASR5000) displays the trace output in window with no ability to write it to a file so I have no ability to specify like i would in a normal tcpdump. I need to be able to get this file into a PCAP or other format that is usable in Wireshark. The customer is having a really hard time with the text file since they are not used to traces looking like this.</p><p>A small example excerpt is below, any help is greatly appreciated.</p><p>Friday July 01 2016 INBOUND&gt;&gt;&gt;&gt;&gt; 22:10:04:544 Eventid:87730(18)</p><p>===&gt; Radio Access Network Application Part (RANAP) (54 bytes) RANAP PDU | 0... .... | Ext bit : 0 | .00. .... | Choice index : Initiating Message (0) Procedure Code : id-Direct Transfer (20)</p></div><div id="question-tags" class="tags-container tags">text pcap help</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jul '16, 16:24</strong></p><img src="https://secure.gravatar.com/avatar/5094ee61e9d0b5a41687be712158651b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dave16&#39;s gravatar image" /><p>Dave16<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dave16 has no accepted answers">0%</span></p></div></div><div id="comments-container-53779" class="comments-container"></div><div id="comment-tools-53779" class="comment-tools"></div><div class="clear"></div><div id="comment-53779-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53780"></span>

<div id="answer-container-53780" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53780-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately, I know of no tools that "undo" the formatting and attempt to figure out what the raw binary data is; that's what would be needed here. Unless there's some command that I missed in a quick search of the <a href="http://www.cisco.com/c/dam/en/us/td/docs/wireless/asr_5000/12_1/OL-25190_CLI_Referencex.pdf">command line reference</a>, you may be completely out of luck here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '16, 17:51</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-53780" class="comments-container"><span id="53781"></span><div id="comment-53781" class="comment"><div id="post-53781-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply, I went through the CLI reference also. This is the only NE I have ever worked with that behaves like this when tracing.</p><p>found this also which i found pretty funny <a href="https://bst.cloudapps.cisco.com/bugsearch/bug/CSCuq69977">https://bst.cloudapps.cisco.com/bugsearch/bug/CSCuq69977</a></p></div><div id="comment-53781-info" class="comment-info"><span class="comment-age">(01 Jul '16, 21:51)</span> Dave16</div></div></div><div id="comment-tools-53780" class="comment-tools"></div><div class="clear"></div><div id="comment-53780-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

