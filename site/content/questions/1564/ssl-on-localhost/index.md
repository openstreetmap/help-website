+++
type = "question"
title = "ssl on localhost"
description = '''I am running a jetty server on my local machine using ssl. I have the p12 files from the server imported using 127.0.0.1,8443,http,&amp;lt;path&amp;gt;,&amp;lt;password&amp;gt;. Files show as being read by the ssldebug file. When I connect to my server using https://localhost:8443/ I get no traffic in wireshark. '''
date = "2010-12-31T17:54:00Z"
lastmod = "2011-01-01T10:01:00Z"
weight = 1564
keywords = [ "ssl" ]
aliases = [ "/questions/1564" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [ssl on localhost](/questions/1564/ssl-on-localhost)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1564-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am running a jetty server on my local machine using ssl. I have the p12 files from the server imported using 127.0.0.1,8443,http,&lt;path&gt;,&lt;password&gt;. Files show as being read by the ssldebug file. When I connect to my server using https://localhost:8443/ I get no traffic in wireshark.</p></div><div id="question-tags" class="tags-container tags">ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Dec '10, 17:54</strong></p><img src="https://secure.gravatar.com/avatar/e2b2fc1bf99c884583f60a5ea01a3b8b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jetaber&#39;s gravatar image" /><p>jetaber<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jetaber has no accepted answers">0%</span></p></div></div><div id="comments-container-1564" class="comments-container"></div><div id="comment-tools-1564" class="comment-tools"></div><div class="clear"></div><div id="comment-1564-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1565"></span>

<div id="answer-container-1565" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1565-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you running on Windows? If so localhost (also known as loopback interface) capture is not supported by Wireshark (or specifically the WinPcap library) out of the box. There are workarounds explained in <a href="http://wiki.wireshark.org/CaptureSetup/Loopback">link text</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Dec '10, 23:47</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p>martyvis<br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 Dec '10, 23:48</p></div></div><div id="comments-container-1565" class="comments-container"></div><div id="comment-tools-1565" class="comment-tools"></div><div class="clear"></div><div id="comment-1565-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1574"></span>

<div id="answer-container-1574" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1574-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you running on something other than Windows - i.e., Linux, Solaris, *BSD, Mac OS X, or some other UN*X? If so, you have to capture on the loopback interface, rather than on an Ethernet or Wi-Fi or... interface. The loopback interface is named either "lo0" (*BSD, Mac OS X, some other UN*Xes) or "lo" (Linux, possibly some other UN*Xes). Most versions of Solaris don't support capturing on the loopback interface.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jan '11, 10:01</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-1574" class="comments-container"></div><div id="comment-tools-1574" class="comment-tools"></div><div class="clear"></div><div id="comment-1574-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

