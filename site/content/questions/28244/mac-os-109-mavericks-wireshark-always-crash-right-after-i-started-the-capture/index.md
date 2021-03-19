+++
type = "question"
title = "Mac OS 10.9 Mavericks: Wireshark always crash right after I started the capture"
description = '''Hello everyone, I&#x27;ve been desperate trying to start my Wireshark app (1.10.4) on my macbook air (mid 2012 model) with no luck in the past one month. Before upgrading my OS, my wireshark has been working great with Mac OS 10.8 (mountain lion). I already updated my X11 to the latest 2.7.5 and using th...'''
date = "2013-12-18T02:58:00Z"
lastmod = "2013-12-18T13:07:00Z"
weight = 28244
keywords = [ "crash", "mavericks", "wireshark" ]
aliases = [ "/questions/28244" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Mac OS 10.9 Mavericks: Wireshark always crash right after I started the capture](/questions/28244/mac-os-109-mavericks-wireshark-always-crash-right-after-i-started-the-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28244-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone, I've been desperate trying to start my Wireshark app (1.10.4) on my macbook air (mid 2012 model) with no luck in the past one month.</p><p>Before upgrading my OS, my wireshark has been working great with Mac OS 10.8 (mountain lion).</p><p>I already updated my X11 to the latest 2.7.5 and using the stable wireshark 1.10.4 build. I kept getting this crash report below. Any help and tips on how can i get my wireshark to fine again with this Maverick? Thanks in advance.</p><pre><code>Process:         wireshark-bin [1088]
Path:            /Applications/Wireshark.app/Contents/Resources/bin/wireshark-bin
Identifier:      wireshark-bin
Version:         ???
Code Type:       X86-64 (Native)
Parent Process:  Wireshark [1086]
Responsible:     Wireshark [1086]
User ID:         501

Date/Time:       2013-12-18 02:49:27.418 -0800
OS Version:      Mac OS X 10.9 (13A603)
Report Version:  11
Anonymous UUID:  54F7A740-4C2F-21DE-DDDF-5E227B204FE6

Crashed Thread:  0  Dispatch queue: com.apple.main-thread

Exception Type:  EXC_BAD_ACCESS (SIGSEGV)
Exception Codes: KERN_INVALID_ADDRESS at 0x0000000000000004

VM Regions Near 0x4:
--&gt; __TEXT                 0000000100000000-00000001001e1000 [ 1924K] r-x/rwx SM=COW  /Applications/Wireshark.app/Contents/Resources/bin/wireshark-bin

Thread 0 Crashed:: Dispatch queue: com.apple.main-thread
0   libwireshark.3.dylib            0x00000001006fce25 dissect_ieee80211_common + 9589
1   libwireshark.3.dylib            0x00000001006ed188 dissect_ieee80211 + 40
2   libwireshark.3.dylib            0x0000000100390ea2 call_dissector_work + 322
3   libwireshark.3.dylib            0x0000000100390ff2 call_dissector_with_data + 50
4   libwireshark.3.dylib            0x00000001006e5319 dissect_radiotap + 9113
5   libwireshark.3.dylib            0x0000000100390ea2 call_dissector_work + 322
6   libwireshark.3.dylib            0x0000000100391d90 dissector_try_uint + 96
7   libwireshark.3.dylib            0x0000000100623761 dissect_frame + 3665
8   libwireshark.3.dylib            0x0000000100390ea2 call_dissector_work + 322
9   libwireshark.3.dylib            0x0000000100390ff2 call_dissector_with_data + 50
10  libwireshark.3.dylib            0x0000000100392966 dissect_packet + 486
11  libwireshark.3.dylib            0x00000001003868f1 epan_dissect_run_with_taps + 65
12  wireshark-bin                   0x0000000100015329 add_packet_to_packet_list + 249
13  wireshark-bin                   0x00000001000169ee read_packet + 382
14  wireshark-bin                   0x0000000100016b87 cf_continue_tail + 375
15  wireshark-bin                   0x000000010000e989 capture_input_new_packets + 57
16  wireshark-bin                   0x000000010000bd7d sync_pipe_input_cb + 509
17  wireshark-bin                   0x000000010006446d pipe_input_cb + 29
18  libglib-2.0.0.dylib             0x00000001057cdbe6 g_io_unix_dispatch + 182
19  libglib-2.0.0.dylib             0x000000010575ef70 g_main_dispatch + 496
20  libglib-2.0.0.dylib             0x000000010575fe94 g_main_context_dispatch + 52
21  libglib-2.0.0.dylib             0x0000000105760100 g_main_context_iterate + 592
22  libglib-2.0.0.dylib             0x0000000105760688 g_main_loop_run + 568
23  libgtk-x11-2.0.0.dylib          0x0000000104b7dc3f gtk_main + 255
24  wireshark-bin                   0x000000010006c498 main + 5656
25  wireshark-bin                   0x0000000100001f54 start + 52</code></pre></div><div id="question-tags" class="tags-container tags">crash mavericks wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Dec '13, 02:58</strong></p><img src="https://secure.gravatar.com/avatar/6cca6ae7bf84f9b38ccd111e43f8a4d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ajlearning&#39;s gravatar image" /><p>ajlearning<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ajlearning has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Dec '13, 12:59</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-28244" class="comments-container"></div><div id="comment-tools-28244" class="comment-tools"></div><div class="clear"></div><div id="comment-28244-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28274"></span>

<div id="answer-container-28274" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28274-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like a crash in the 802.11 dissector (and probably not Mavericks-specific, except to the extent that Mavericks might be sending traffic that happens to trigger the bug).</p><p>If, right after Wireshark crashes, you open up a Terminal window and do</p><pre><code>ls -lt $TMPDIR/wireshark* | head -1</code></pre><p>and make a copy of the file that shows up in that list (using the <code>cp</code> command, for example</p><pre><code>cp /var/folders/r6/7c10vwy92374jygh41f9d1k00000gn/T//wireshark_pcapng_en0_20131218130228_0jnr9Z ~/Desktop/crashes.pcapng</code></pre><p>Note that the command must be all on one command line. That command will put a copy of the file on your desktop, named <code>crashes.pcapng</code>), and then try to open the capture in Wireshark, it'll probably crash Wireshark.</p><p>If it crashes Wireshark, then submit a bug at <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>, and attach the capture file; you can mark it as "private" if you don't want anybody other than the core Wireshark developers to be able to see the capture file (and the packets in it).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Dec '13, 13:07</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-28274" class="comments-container"><span id="28283"></span><div id="comment-28283" class="comment"><div id="post-28283-score" class="comment-score"></div><div class="comment-text"><p>Thank you a bunch, Guy for the tips. I just filed my issue here at the Wireshark Bugzilla and attached the suggested file. <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9582">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9582</a></p></div><div id="comment-28283-info" class="comment-info"><span class="comment-age">(18 Dec '13, 23:54)</span> ajlearning</div></div></div><div id="comment-tools-28274" class="comment-tools"></div><div class="clear"></div><div id="comment-28274-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

