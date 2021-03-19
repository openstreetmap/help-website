+++
type = "question"
title = "MAPI Unknown Operation 10 &amp; 11 Request / Response"
description = '''Hi Guys, I&#x27;m trying to diagnose some performance issues on my network and I have captured a heap of unknown packets using WireShark. Google didn&#x27;t reveal much apart from &quot;Wireshark might not know how to decode those packets&quot; I did the capture on both the source and destination server to rule out cor...'''
date = "2013-11-21T15:29:00Z"
lastmod = "2013-11-21T17:02:00Z"
weight = 27244
keywords = [ "unknown", "mapi", "opperation" ]
aliases = [ "/questions/27244" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [MAPI Unknown Operation 10 & 11 Request / Response](/questions/27244/mapi-unknown-operation-10-11-request-response)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27244-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Guys, I'm trying to diagnose some performance issues on my network and I have captured a heap of unknown packets using WireShark. Google didn't reveal much apart from "Wireshark might not know how to decode those packets"</p><p>I did the capture on both the source and destination server to rule out corrupted packets. Source server has wireshark 1.10.3 and Destination server has wireshark 1.10.2 and both contain the same thing.</p><p>2162 18.498010000 10.2.2.16 10.2.2.3 MAPI 246 Unknown operation 11 request</p><p>I see request and response for Operation type 10,11 and 14 The overall network utilisation is quite low so this is probably not a problem. I'm more curious now why WireShark doesn't know how to decode them.</p><p>I know the application what is causing the traffic. It synchronises Exchange mailboxes with a SQL Database. The traffic stops when I turn it off.</p><p>Any Ideas what is going on?</p><p>Thanks David</p></div><div id="question-tags" class="tags-container tags">unknown mapi opperation</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '13, 15:29</strong></p><img src="https://secure.gravatar.com/avatar/c8e6284b397d1855ef412a8d1abfe11b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="The%20Dog%20Master&#39;s gravatar image" /><p>The Dog Master<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="The Dog Master has no accepted answers">0%</span></p></div></div><div id="comments-container-27244" class="comments-container"></div><div id="comment-tools-27244" class="comment-tools"></div><div class="clear"></div><div id="comment-27244-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27246"></span>

<div id="answer-container-27246" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27246-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I'm more curious now why WireShark doesn't know how to decode them.</p></blockquote><p>Because nobody's contributed code to decode them; when the MAPI dissector was originally written, I'm not sure Microsoft had published any documents describing the MAPI protocol, so whoever wrote the dissector for it made it handle what they and other people had seen and reverse-engineered.</p><p>The <a href="http://msdn.microsoft.com/en-us/library/cc425493(v=exchg.80).aspx">[MS-OXCRPC]</a> document shows operation 10 as <a href="http://msdn.microsoft.com/en-us/library/ee200938(v=exchg.80).aspx">EcDoConnectEx</a>, operation 11 as <a href="http://msdn.microsoft.com/en-us/library/ee178527(v=exchg.80).aspx">EcDoRpcExt2</a>, and operation 14 as <a href="http://msdn.microsoft.com/en-us/library/ee203537(v=exchg.80).aspx">EcDoAsyncConnectEx</a>. However, nobody's taken the time to add those to the mapi.idl file in the Wireshark source and rebuild the dissector.</p><p>Expecting Wireshark (or any network analyzer) to fully dissect every protocol you see on a network is unrealistic, given that 1) not all protocols are publicly documented and 2) developers' time is limited.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Nov '13, 17:02</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Nov '13, 17:05</p></div></div><div id="comments-container-27246" class="comments-container"><span id="27248"></span><div id="comment-27248" class="comment"><div id="post-27248-score" class="comment-score"></div><div class="comment-text"><p>Hi Guy, That explains it and that was my hunch. Maybe someone will pick that job up one day. I did a quick search for MAPI documentation and as with all Microsoft products if it isn't Marketing Material it is all over the place. Thanks for the Answer. David</p></div><div id="comment-27248-info" class="comment-info"><span class="comment-age">(21 Nov '13, 20:50)</span> The Dog Master</div></div><span id="27307"></span><div id="comment-27307" class="comment"><div id="post-27307-score" class="comment-score"></div><div class="comment-text"><p>I've updated the answer to refer to the Microsoft documentation on the over-the-wire MAPI protocol.</p></div><div id="comment-27307-info" class="comment-info"><span class="comment-age">(23 Nov '13, 17:05)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-27246" class="comment-tools"></div><div class="clear"></div><div id="comment-27246-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

