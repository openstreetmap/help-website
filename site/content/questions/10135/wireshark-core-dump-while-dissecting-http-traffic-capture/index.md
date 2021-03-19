+++
type = "question"
title = "Wireshark core dump while dissecting http traffic capture"
description = '''Hi all, I&#x27;m using wireshark to decode traffic captures in order to login requests/answers from a web service. My current version is: bash-3.00$ /usr/local/bin/tshark -v TShark 1.6.4 (SVN Rev Unknown from unknown) Copyright 1998-2011 Gerald Combs gerald@wireshark.org and contributors. This is free so...'''
date = "2012-04-13T11:00:00Z"
lastmod = "2012-05-11T03:23:00Z"
weight = 10135
keywords = [ "core", "snoop", "http", "tshark", "dump" ]
aliases = [ "/questions/10135" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark core dump while dissecting http traffic capture](/questions/10135/wireshark-core-dump-while-dissecting-http-traffic-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10135-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10135-score" class="post-score" title="current number of votes">0</div><span id="post-10135-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I'm using wireshark to decode traffic captures in order to login requests/answers from a web service.</p><p>My current version is:</p><p>bash-3.00$ /usr/local/bin/tshark -v TShark 1.6.4 (SVN Rev Unknown from unknown)</p><p>Copyright 1998-2011 Gerald Combs <span><span class="__cf_email__" data-cfemail="50373522313c341027392235233831223b7e3f2237">[email protected]</span></span> and contributors. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p><p>Compiled (32-bit) with GLib 2.25.13, with libpcap 1.1.1, with libz 1.2.5, without POSIX capabilities, without libpcre, without SMI, without c-ares, with ADNS, without Lua, without Python, with GnuTLS 2.8.6, with Gcrypt 1.4.6, without Kerberos, with GeoIP.</p><p>Running on SunOS 5.10, with libpcap version 1.1.1, with libz 1.2.3.</p><p>Built using gcc 3.4.6.</p><h6 id="section"></h6><p>The core dump occurs for most of my capture files (snoop on solaris 10).</p><p>For example:</p><p>bash-3.00$ /usr/local/bin/tshark -o tcp.check_checksum:false -r teste.cap -V -d tcp.port==10010,http</p><p>(Ultra cool dissecting for some thousands http posts)</p><p>And then:</p><p>[Malformed Packet: T.38] [Expert Info (Error/Malformed): Malformed Packet (Exception occurred)] [Message: Malformed Packet (Exception occurred)] [Severity level: Error] [Group: Malformed]</p><p>Bus Error (core dumped)</p><p>Anyone has any ideas on how to try to solve this problem? Even if the dump contains some malformed packets, is it possible to ignore and continue?</p><p>Thanks!</p><p>BR AJ</p></h6></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-core" rel="tag" title="see questions tagged &#39;core&#39;">core</span> <span class="post-tag tag-link-snoop" rel="tag" title="see questions tagged &#39;snoop&#39;">snoop</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-dump" rel="tag" title="see questions tagged &#39;dump&#39;">dump</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Apr '12, 11:00</strong></p><img src="https://secure.gravatar.com/avatar/f3952635b49029b48a74a96cad030dfe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alexandre%20Vieira&#39;s gravatar image" /><p><span>Alexandre Vi...</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alexandre Vieira has no accepted answers">0%</span></p></div></div><div id="comments-container-10135" class="comments-container"></div><div id="comment-tools-10135" class="comment-tools"></div><div class="clear"></div><div id="comment-10135-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10138"></span>

<div id="answer-container-10138" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10138-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10138-score" class="post-score" title="current number of votes">1</div><span id="post-10138-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The core dump means there's a bug in that version of TShark. TShark doesn't deliberately panic when it sees malformed packets; there's probably code that's not being sufficiently cautious about the packet data it's parsing.</p><p>If you have a debugger (gdb or dbx or lldb or...), try running the debugger with the TShark binary and the core dump file, and get a stack trace from the crash. Then file a bug on <a href="http://bugs.wireshark.org/">the Wireshark bugzilla</a>, and attach the stack trace. (Do <em>NOT</em> attach the core dump file - it's large and won't be useful except on a Solaris 10 machine with the same instruction set architecture and the same binary of TShark, and most of us probably won't have that.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Apr '12, 11:38</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-10138" class="comments-container"></div><div id="comment-tools-10138" class="comment-tools"></div><div class="clear"></div><div id="comment-10138-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10926"></span>

<div id="answer-container-10926" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10926-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10926-score" class="post-score" title="current number of votes">0</div><span id="post-10926-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In most of the cases I use tcpdump, tshark or wireshark. But these tools were not sufficient in all cases. So I looked out for other tools and it seems I found a very cool console based network sniffer for analyzing HTTP traffic on linux: <a href="http://justniffer.sourceforge.net/">justniffer</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '12, 03:23</strong></p><img src="https://secure.gravatar.com/avatar/2a6419136ef0f70985f546bb82a39036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Augustyn2&#39;s gravatar image" /><p><span>Augustyn2</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Augustyn2 has no accepted answers">0%</span></p></div></div><div id="comments-container-10926" class="comments-container"></div><div id="comment-tools-10926" class="comment-tools"></div><div class="clear"></div><div id="comment-10926-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

