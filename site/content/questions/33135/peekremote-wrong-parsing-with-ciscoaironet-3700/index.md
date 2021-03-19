+++
type = "question"
title = "PEEKREMOTE wrong parsing with CiscoAironet 3700"
description = '''Hi, I am using a Cisco Aironet 3700 running autonomous version and configured to work in monitor mode(all wireless traffic send to remote host) my problem is that using wireshark PEEKREMOTE decoding the packet sent from my AP are not parsed correctly. See the following capture: https://drive.google....'''
date = "2014-05-28T05:16:00Z"
lastmod = "2014-05-28T23:28:00Z"
weight = 33135
keywords = [ "peekremote", "airopeek" ]
aliases = [ "/questions/33135" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [PEEKREMOTE wrong parsing with CiscoAironet 3700](/questions/33135/peekremote-wrong-parsing-with-ciscoaironet-3700)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33135-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am using a Cisco Aironet 3700 running autonomous version and configured to work in monitor mode(all wireless traffic send to remote host) my problem is that using wireshark PEEKREMOTE decoding the packet sent from my AP are not parsed correctly.</p><p>See the following capture:</p><p><a href="https://drive.google.com/file/d/0B0ta7zFvYqzxRlh5ZVBjRWJwT0U/edit?usp=sharing">https://drive.google.com/file/d/0B0ta7zFvYqzxRlh5ZVBjRWJwT0U/edit?usp=sharing</a></p><p>Did anyone encounter with such issue? Many Thanks</p></div><div id="question-tags" class="tags-container tags">peekremote airopeek</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 May '14, 05:16</strong></p><img src="https://secure.gravatar.com/avatar/dfea62d34ba9a0ef9be275e7966503e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pavel%20Bonder&#39;s gravatar image" /><p>Pavel Bonder<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pavel Bonder has no accepted answers">0%</span></p></div></div><div id="comments-container-33135" class="comments-container"><span id="33145"></span><div id="comment-33145" class="comment"><div id="post-33145-score" class="comment-score"></div><div class="comment-text"><p>Those packets look very different from the PEEKREMOTE packets in other captures; they don't look like packets with either the 20-byte legacy header or the 55-byte 802.11n header. By "configured to work in monitor mode" do you mean that you put the 3700 into "Sniffer" mode, as Cisco calls it, and configured it to send packets to port 6666? Does AiroPeek or OmniPeek correctly dissect those packets?</p></div><div id="comment-33145-info" class="comment-info"><span class="comment-age">(28 May '14, 19:54)</span> Guy Harris ♦♦</div></div><span id="47606"></span><div id="comment-47606" class="comment"><div id="post-47606-score" class="comment-score"></div><div class="comment-text"><p>Even i am facing the same issue, Is there a solution for this or any workarounds.</p><p>Thanks, Jagadeesh</p></div><div id="comment-47606-info" class="comment-info"><span class="comment-age">(14 Nov '15, 10:20)</span> Jagadeesh Yc</div></div><span id="47607"></span><div id="comment-47607" class="comment"><div id="post-47607-score" class="comment-score"></div><div class="comment-text"><p>Read the answer to this question. If that doesn't solve your problem, ask <em>another</em> question; just because you see similar symptoms, that doesn't mean it's the same issue.</p></div><div id="comment-47607-info" class="comment-info"><span class="comment-age">(14 Nov '15, 10:28)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-33135" class="comment-tools"></div><div class="clear"></div><div id="comment-33135-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33148"></span>

<div id="answer-container-33148" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33148-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>...and that's because it's <strong><em>NOT</em></strong> PEEKREMOTE traffic, it's CWIDS (Cisco Wireless Intrusion Detection System) traffic. Try dissecting it as CWIDS instead.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 May '14, 23:28</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-33148" class="comments-container"><span id="33154"></span><div id="comment-33154" class="comment"><div id="post-33154-score" class="comment-score"></div><div class="comment-text"><p>In order to configure AP in monitor mode I set the wireless interface to "#station-role scanner", and configure monitor to any host and port I want "#monitor frames endpoint ip address 192.168.1.10 port 6666"</p><p>Decoding this as CWIDS also do not parse the packet correctly, each packet is parsed with multiple CWIDS and IEE802.11 headers in same packet.</p><p>I do no have OmniPeek for comparison.</p><p>Many Thanks</p></div><div id="comment-33154-info" class="comment-info"><span class="comment-age">(29 May '14, 02:13)</span> Pavel Bonder</div></div><span id="33156"></span><div id="comment-33156" class="comment"><div id="post-33156-score" class="comment-score"></div><div class="comment-text"><blockquote><p>each packet is parsed with multiple CWIDS and IEE802.11 headers in same packet</p></blockquote><p>That's not a bug, that's a feature. As <a href="http://www.cisco.com/c/en/us/td/docs/wireless/access_point/12-3_7_JA/configuration/guide/i1237sc/s37roamg.html#wp1069159">Cisco's documentation</a> says, "Multiple captured frames can be combined into one UDP packet to conserve network bandwidth."</p></div><div id="comment-33156-info" class="comment-info"><span class="comment-age">(29 May '14, 02:26)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-33148" class="comment-tools"></div><div class="clear"></div><div id="comment-33148-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

