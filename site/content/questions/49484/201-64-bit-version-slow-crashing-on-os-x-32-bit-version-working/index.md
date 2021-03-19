+++
type = "question"
title = "2.0.1 64 bit version slow, crashing on OS X; 32 bit version working"
description = '''The 32 bit version of wireshark runs smoothly on my system, the 64 bit version barely runs at all and frequently crashes. Wireshark: Version 2.0.1 (v2.0.1-0-g59ea380 from master-2.0) Here are the differences between the 32 and 64 bit builds: ----Compiled (32-bit) with Qt 4.8.6, with libpcap, without...'''
date = "2016-01-23T09:17:00Z"
lastmod = "2016-01-23T12:56:00Z"
weight = 49484
keywords = [ "macosx", "crash" ]
aliases = [ "/questions/49484" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [2.0.1 64 bit version slow, crashing on OS X; 32 bit version working](/questions/49484/201-64-bit-version-slow-crashing-on-os-x-32-bit-version-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49484-score" class="post-score" title="current number of votes">0</div><span id="post-49484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The 32 bit version of wireshark runs smoothly on my system, the 64 bit version barely runs at all and frequently crashes.</p><p>Wireshark: Version 2.0.1 (v2.0.1-0-g59ea380 from master-2.0)</p><p>Here are the differences between the 32 and 64 bit builds:</p><p>----Compiled (32-bit) with Qt 4.8.6, with libpcap, without POSIX capabilities, with libz 1.2.3, with GLib 2.16.3, with SMI 0.4.8, without c-ares, without ADNS, with Lua 5.2, with GnuTLS 2.12.19, with Gcrypt 1.4.3, with MIT Kerberos, with GeoIP, with QtMultimedia, without AirPcap.</p><p>Running on Mac OS X 10.11.2, build 15C50 (Darwin 15.2.0), with locale C, with libpcap version 1.5.3 - Apple version 54, with libz 1.2.5, with GnuTLS 2.12.19, with Gcrypt 1.4.3.</p><p>Built using gcc 4.2.1 (Apple Inc. build 5666) (dot 3).</p><p>----Compiled (64-bit) with Qt 5.3.2, with libpcap, without POSIX capabilities, with libz 1.2.5, with GLib 2.36.0, with SMI 0.4.8, without c-ares, without ADNS, with Lua 5.2, with GnuTLS 2.12.19, with Gcrypt 1.5.0, with MIT Kerberos, with GeoIP, with QtMultimedia, without AirPcap.</p><p>Running on Mac OS X 10.11.2, build 15C50 (Darwin 15.2.0), with locale C, with libpcap version 1.5.3 - Apple version 54, with libz 1.2.5, with GnuTLS 2.12.19, with Gcrypt 1.5.0. Intel(R) Core(TM) i7-4790K CPU @ 4.00GHz (with SSE4.2)</p><p>Built using llvm-gcc 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2336.9.00).</p><hr /><p>Here is a sample of the crashes:</p><p>Crashed Thread: 0 Dispatch queue: com.apple.main-thread</p><p>Exception Type: EXC_BAD_ACCESS (SIGSEGV) Exception Codes: EXC_I386_GPFLT Exception Note: EXC_CORPSE_NOTIFY</p><p>Crashed Thread: 0 Dispatch queue: com.apple.main-thread</p><p>Exception Type: EXC_BAD_ACCESS (SIGSEGV) Exception Codes: KERN_INVALID_ADDRESS at 0x00007fd200000021 Exception Note: EXC_CORPSE_NOTIFY</p><p>Crashed Thread: 0 Dispatch queue: com.apple.main-thread</p><p>Exception Type: EXC_BAD_ACCESS (SIGSEGV) Exception Codes: KERN_INVALID_ADDRESS at 0x0000000000000000 Exception Note: EXC_CORPSE_NOTIFY</p><p>Crashed Thread: 0 Dispatch queue: com.apple.main-thread</p><p>Exception Type: EXC_BAD_ACCESS (SIGSEGV) Exception Codes: KERN_INVALID_ADDRESS at 0x0000000000000128 Exception Note: EXC_CORPSE_NOTIFY</p><p>Crashed Thread: 0 Dispatch queue: com.apple.main-thread</p><p>Exception Type: EXC_BAD_ACCESS (SIGSEGV) Exception Codes: EXC_I386_GPFLT</p><p>Crashed Thread: 0 Dispatch queue: com.apple.main-thread</p><p>Exception Type: EXC_BAD_ACCESS (SIGSEGV) Exception Codes: EXC_I386_GPFLT Exception Note: EXC_CORPSE_NOTIFY</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-macosx" rel="tag" title="see questions tagged &#39;macosx&#39;">macosx</span> <span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jan '16, 09:17</strong></p><img src="https://secure.gravatar.com/avatar/bab883c021da12a1d595a4fa62581be2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brachygraphic&#39;s gravatar image" /><p><span>brachygraphic</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brachygraphic has no accepted answers">0%</span></p></div></div><div id="comments-container-49484" class="comments-container"></div><div id="comment-tools-49484" class="comment-tools"></div><div class="clear"></div><div id="comment-49484-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49485"></span>

<div id="answer-container-49485" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49485-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49485-score" class="post-score" title="current number of votes">0</div><span id="post-49485-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="brachygraphic has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please file a bug report on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>, and give the <em>full</em> contents of the crash reports, not just the summary; the stack report is <em>extremely</em> important for debugging purposes. Please attach to the bug all the different crash reports ("different" as in "have different stack traces" or "have different exception types".)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jan '16, 12:56</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-49485" class="comments-container"></div><div id="comment-tools-49485" class="comment-tools"></div><div class="clear"></div><div id="comment-49485-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

