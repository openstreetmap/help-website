+++
type = "question"
title = "Apps for GSM packet analysis"
description = '''Hi, i wanted to know if these apps &quot;Shark for Root&quot; and &quot;Microsoft Network Analyzer&quot; are able to perform GSM packets capture on a cell phone? later to be transferred to a computer and analyzed on Wireshark.'''
date = "2013-09-27T00:02:00Z"
lastmod = "2013-09-27T06:39:00Z"
weight = 25301
keywords = [ "android", "gsm", "wireshark" ]
aliases = [ "/questions/25301" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Apps for GSM packet analysis](/questions/25301/apps-for-gsm-packet-analysis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25301-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, i wanted to know if these apps "Shark for Root" and "Microsoft Network Analyzer" are able to perform GSM packets capture on a cell phone? later to be transferred to a computer and analyzed on Wireshark.</p></div><div id="question-tags" class="tags-container tags">android gsm wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Sep '13, 00:02</strong></p><img src="https://secure.gravatar.com/avatar/c01b9ea5bdb1f901e98f9698393240ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arslan&#39;s gravatar image" /><p>Arslan<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arslan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted 27 Sep '13, 00:10</p></div></div><div id="comments-container-25301" class="comments-container"></div><div id="comment-tools-25301" class="comment-tools"></div><div class="clear"></div><div id="comment-25301-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25316"></span>

<div id="answer-container-25316" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25316-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Already answered in another thread but here it is again:</p><p>The standard packet capture tools won't allow you to capture "GSM" packets.</p><p>On an Android phone, once the cellular modem establishes a data session with the network, it will create an interface (rmnet0 or rmnet_usb0 for example). That interface is what the Android OS uses to exchange packets from the OS to the cellular modem in the phone.</p><p>Once it reaches the cellular modem, packets get encapsulated in GTP (for user data). The control packets (non-access stratum signalling for example) is generated at the cellular modem itself.</p><p>In order to capture these messages directly from the phone, you will need specialized equipment of software capable of connecting and interpreting the Qualcomm diagnostic monitor (DM) port on the phone. QXDM, TEMS Investigation and Swissqual are examples of tools capable of doing that.</p><p>I don't know of any free tool capable of interfacing correctly with the DM port but I'd be interested in one exist.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Sep '13, 06:39</strong></p><img src="https://secure.gravatar.com/avatar/266ce8d554380aab282c11e3cb821a28?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kiloohm&#39;s gravatar image" /><p>Kiloohm<br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kiloohm has no accepted answers">0%</span></p></div></div><div id="comments-container-25316" class="comments-container"></div><div id="comment-tools-25316" class="comment-tools"></div><div class="clear"></div><div id="comment-25316-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

