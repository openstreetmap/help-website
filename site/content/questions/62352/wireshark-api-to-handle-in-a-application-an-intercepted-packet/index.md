+++
type = "question"
title = "WireShark API to handle in a application an intercepted packet ?"
description = '''Hello everybody. I m going to attend a Security Project where, in the very first part, I have to check that on my architecture (IOT) some message packets goes on plaintext and also other security problems, related both to communication security and authentication (very simple security problems). Dur...'''
date = "2017-06-28T01:10:00Z"
lastmod = "2017-06-28T06:47:00Z"
weight = 62352
keywords = [ "test", "security", "api", "wireshark" ]
aliases = [ "/questions/62352" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [WireShark API to handle in a application an intercepted packet ?](/questions/62352/wireshark-api-to-handle-in-a-application-an-intercepted-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62352-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everybody. I m going to attend a Security Project where, in the very first part, I have to check that on my architecture (IOT) some message packets goes on plaintext and also other security problems, related both to communication security and authentication (very simple security problems). During a little software selection, I m evaluating to use wireshark to sniff those "unsafe" packets, but I was wondering if there are some particular API that could be helpful to me in order to pick these data and handle it on my business logic application, in order to automatizing vulnerabilities' checking in a test driven development way (iff the test pass, I know that the vulnerabilities' are fixed). Example of test: intercept an ID (of an authorized device) and try a connection with the same ID from a "malicious" device, ndr. Everything could helping me, thank a lot.</p></div><div id="question-tags" class="tags-container tags">test security api wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jun '17, 01:10</strong></p><img src="https://secure.gravatar.com/avatar/342095c9657e13e6e8a5c607af6c2771?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ciandro92&#39;s gravatar image" /><p>ciandro92<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ciandro92 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Jun '17, 01:58</p></div></div><div id="comments-container-62352" class="comments-container"></div><div id="comment-tools-62352" class="comment-tools"></div><div class="clear"></div><div id="comment-62352-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62358"></span>

<div id="answer-container-62358" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62358-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Would piping of tshark textual output to the input of your business logic application do?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jun '17, 06:47</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-62358" class="comments-container"><span id="62360"></span><div id="comment-62360" class="comment"><div id="post-62360-score" class="comment-score"></div><div class="comment-text"><p>Exact, I need the body of the message (i think that a txt format is enough). Is possible on wireshark without using other API from other languages? My application need to use the body of the intercepted message to get some information for a test. e.g. if in a message I send a plain ID for an authorization phase, the test could use this ID to connect, and if the connection goes on, the test send me a notification for this vulnerability, until i repair it. I found a library in pyhthon (name pyshark) that represent a "wrapper" for wireshark application component: could it be useful? anyone have used this library to do some kind of operation (like I described)? Thanks</p></div><div id="comment-62360-info" class="comment-info"><span class="comment-age">(28 Jun '17, 07:35)</span> ciandro92</div></div><span id="62367"></span><div id="comment-62367" class="comment"><div id="post-62367-score" class="comment-score">1</div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-62367-info" class="comment-info"><span class="comment-age">(28 Jun '17, 08:23)</span> Jaap ♦</div></div></div><div id="comment-tools-62358" class="comment-tools"></div><div class="clear"></div><div id="comment-62358-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

