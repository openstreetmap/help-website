+++
type = "question"
title = "Solaris 10 tshark &quot;bus error&quot; when reading some pcap files"
description = '''Can anyone provide me some insight what is the root cause of the following problem &amp;amp; how to fix it? (ie. Do it need to recompile tshark or just have the dependence updated?) The version of tshark and its dependency are from the sunfreeware.com. # uname -a SunOS daisy 5.10 Generic_127127-11 sun4u...'''
date = "2011-12-02T10:12:00Z"
lastmod = "2011-12-02T10:32:00Z"
weight = 7742
keywords = [ "10", "solaris", "tshark" ]
aliases = [ "/questions/7742" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Solaris 10 tshark "bus error" when reading some pcap files](/questions/7742/solaris-10-tshark-bus-error-when-reading-some-pcap-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7742-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can anyone provide me some insight what is the root cause of the following problem &amp; how to fix it? (ie. Do it need to recompile tshark or just have the dependence updated?)</p><p>The version of tshark and its dependency are from the sunfreeware.com.</p><pre><code># uname -a
SunOS daisy 5.10 Generic_127127-11 sun4u sparc SUNW,Sun-Blade-1500 Solaris
# 
# tshark -r dhcp.pcap</code></pre><p>...</p><pre><code>229 159.632917 MasterIn_16:74:3c -&gt; Broadcast    ARP 68 Who has 192.168.150.150?  Tell 192.168.150.192
230 160.003917 Cisco_51:01:db -&gt; Spanning-tree-(for-bridges)_00 STP 64 RST. Root = 8192/152/00:11:bc:c3:94:00  Cost = 4  Port = 0x80cc
Bus Error (core dumped)</code></pre><p>gdb indicate there is a Illegal instruction in the libcrypto.so.1.0.0</p><pre><code>#0  0xfd4be44c in ?? () from /usr/local/lib/libwireshark.so.1
(gdb) r
Starting program: /usr/local/bin/tshark 
[New LWP    1        ]
warning: Lowest section in /usr/lib/libpthread.so.1 is .dynamic at 00000074
warning: Lowest section in /usr/lib/libthread.so.1 is .dynamic at 00000074
warning: Lowest section in /lib/libdl.so.1 is .hash at 000000b4

Program received signal SIGILL, Illegal instruction.
0xfc0cbd3c in _sparcv9_fmadd_probe () from /usr/local/ssl/lib/libcrypto.so.1.0.0
(gdb)

# tshark -v
TShark 1.6.4 (SVN Rev Unknown from unknown)

Copyright 1998-2011 Gerald Combs &lt;[email protected]&gt; and contributors.
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Compiled (32-bit) with GLib 2.25.13, with libpcap 1.2.0, with libz 1.2.5,
without POSIX capabilities, without libpcre, without SMI, without c-ares, with
ADNS, without Lua, without Python, with GnuTLS 2.8.6, with Gcrypt 1.4.6, without
Kerberos, with GeoIP.

Running on SunOS 5.10, with libpcap version 1.2.0, with libz 1.2.5.

Built using gcc 3.4.6.
#</code></pre></div><div id="question-tags" class="tags-container tags">10 solaris tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '11, 10:12</strong></p><img src="https://secure.gravatar.com/avatar/7a0fa4cb1fc619a850c20cbac30e13b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kelvin%20Lee&#39;s gravatar image" /><p>Kelvin Lee<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kelvin Lee has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Dec '11, 10:27</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-7742" class="comments-container"></div><div id="comment-tools-7742" class="comment-tools"></div><div class="clear"></div><div id="comment-7742-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7743"></span>

<div id="answer-container-7743" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7743-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The root cause of the problem is probably that SPARC is the one remaining processor out there (or, at least, the one remaining processor used in general-purpose computers) that traps on unaligned accesses rather than supporting unaligned accesses, most people develop code on other processors and may not realize that you can't blithely dereference unaligned pointers, and some compilers don't warn about those dereferences (either because they're generating code for other processors and don't bother to do the check or don't bother to do the check at all) and even for the ones that do we aren't checking for those warnings. :-)</p><p>I.e., this is a Wireshark bug, it's just one that doesn't show up on most machines.</p><p>(That's probably different from the SIGILL problem, which is some other issue, perhaps an issue with gdb.)</p><p>Do you have a stack trace of the "bus error" crash? I'll see whether there are any alignment warnings coughed up by, for example, the Clang static analyzer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '11, 10:32</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-7743" class="comments-container"></div><div id="comment-tools-7743" class="comment-tools"></div><div class="clear"></div><div id="comment-7743-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

