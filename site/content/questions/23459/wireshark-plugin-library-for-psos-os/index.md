+++
type = "question"
title = "Wireshark plugin / library for pSoS OS."
description = '''Like Wireshark has plugins developed for Windows / linux etc, do we have Wireshark library support for pSoS OS also ? If so, where can I get the source code to start integration ? Else can someone suggest any other free tool using which I can have a packet capture on embedded systems running pSoS OS...'''
date = "2013-07-31T00:12:00Z"
lastmod = "2013-07-31T01:37:00Z"
weight = 23459
keywords = [ "capture", "wireshark", "rtos", "psos", "plugin" ]
aliases = [ "/questions/23459" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark plugin / library for pSoS OS.](/questions/23459/wireshark-plugin-library-for-psos-os)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23459-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23459-score" class="post-score" title="current number of votes">0</div><span id="post-23459-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Like Wireshark has plugins developed for Windows / linux etc, do we have Wireshark library support for pSoS OS also ? If so, where can I get the source code to start integration ?</p><p>Else can someone suggest any other free tool using which I can have a packet capture on embedded systems running pSoS OS ?</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-rtos" rel="tag" title="see questions tagged &#39;rtos&#39;">rtos</span> <span class="post-tag tag-link-psos" rel="tag" title="see questions tagged &#39;psos&#39;">psos</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jul '13, 00:12</strong></p><img src="https://secure.gravatar.com/avatar/1ca51727acd79fa3acbca4545d8d2cab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="peardropz&#39;s gravatar image" /><p><span>peardropz</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="peardropz has no accepted answers">0%</span></p></div></div><div id="comments-container-23459" class="comments-container"></div><div id="comment-tools-23459" class="comment-tools"></div><div class="clear"></div><div id="comment-23459-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23460"></span>

<div id="answer-container-23460" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23460-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23460-score" class="post-score" title="current number of votes">1</div><span id="post-23460-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark doesn't actually do packet capture, that is done by the appropriate mechanism for the host OS, e.g. WinPCap for Windows, libpcap for Linux etc.</p><p>I haven't used pSos for 2 decades, but I would think that libpcap would be your best starting point. I don't know if there have been ports to other embedded OS's, e.g. VxWorks that might be useful references.</p><p>The project site for libpcap is <a href="http://www.tcpdump.org/">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jul '13, 01:18</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-23460" class="comments-container"><span id="23463"></span><div id="comment-23463" class="comment"><div id="post-23463-score" class="comment-score">1</div><div class="comment-text"><p>That's "libpcap for UN*Xes of all sorts, including but not limited to Linux, WinPcap for Windows, and either somebody's third-party port of libpcap, directly using whatever pSoS provides, or nothing for pSOS".</p><p>There is <em>no</em> support for OSes other than *BSD, OS X (and iOS if you jailbreak; the OS X code <em>should</em> work, but porting and cross-building is left as an exercise for the reader), Linux, SunOS 3.x (may suffer from bitrot), SunOS 4.x (may suffer from bitrot), SunOS 5.x, HP-UX, AIX, Tru64 UNIX (may suffer from bitrot), IRIX (may suffer from bitrot), and MS-DOS in libpcap as distributed by tcpdump.org.</p><p>A quick Google search for</p><pre><code>&quot;psos&quot; libpcap</code></pre><p>didn't show anything immediately obvious.</p></div><div id="comment-23463-info" class="comment-info"><span class="comment-age">(31 Jul '13, 01:37)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-23460" class="comment-tools"></div><div class="clear"></div><div id="comment-23460-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

