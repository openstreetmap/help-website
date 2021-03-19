+++
type = "question"
title = "tshark &amp; etherXXXX files under /tmp directory"
description = '''Hello, I am running tshark on a virtual machine running centOS, the version info is as below: sudo /usr/sbin/tshark -v TShark 1.0.15  Copyright 1998-2010 Gerald Combs &amp;lt;gerald@wireshark.org&amp;gt; and contributors. This is free software; see the source for copying conditions. There is NO warranty; no...'''
date = "2011-01-21T14:57:00Z"
lastmod = "2011-01-22T01:52:00Z"
weight = 1866
keywords = [ "tmp", "directory", "disc", "wireshark", "space" ]
aliases = [ "/questions/1866" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark & etherXXXX files under /tmp directory](/questions/1866/tshark-etherxxxx-files-under-tmp-directory)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1866-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am running tshark on a virtual machine running centOS, the version info is as below:</p><pre><code>sudo /usr/sbin/tshark -v
TShark 1.0.15

Copyright 1998-2010 Gerald Combs &lt;[email protected]&gt; and contributors.
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Compiled with GLib 2.12.3, with libpcap 0.9.4, with libz 1.2.3, without POSIX
capabilities, with libpcre 6.6, with SMI 0.4.5, without ADNS, without Lua, with
GnuTLS 1.4.1, with Gcrypt 1.4.4, with MIT Kerberos.

Running on Linux 2.6.18-194.26.1.el5, with libpcap version 0.9.4.

Built using gcc 4.1.2 20080704 (Red Hat 4.1.2-48).</code></pre><p>I run tshark as below:</p><pre><code>sudo /usr/sbin/tshark -i eth0
Running as user &quot;root&quot; and group &quot;root&quot;. This could be dangerous.

Capturing on eth0
  0.000000 192.168.179.1 -&gt; 192.168.179.128 ICMP Echo (ping) request
  0.000031 192.168.179.128 -&gt; 192.168.179.1 ICMP Echo (ping) reply

2 packets captured

ls -l /tmp/ether*
-rw------- 1 root root 152248 Jan 21 14:34 /tmp/etherXXXX2swaYE
-rw------- 1 root root     24 Jan 21 14:48 /tmp/etherXXXX9YWKQw
-rw------- 1 root root    924 Jan 21 14:49 /tmp/etherXXXXE4GGXo
-rw------- 1 root root     24 Jan 21 14:35 /tmp/etherXXXXUMJJll
-rw------- 1 root root     24 Jan 21 14:26 /tmp/etherXXXXvCdj8e</code></pre><p>tshark creates these temporary files that are not getting deleted automatically, eventually I run out of space on that partition.</p><p>Is there any way to run tshark to dump packets on the "standard output" without these files getting created ??</p><p>Any help / advice is greatly appreciated.</p><p>Thanks /R</p></div><div id="question-tags" class="tags-container tags">tmp directory disc wireshark space</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jan '11, 14:57</strong></p><img src="https://secure.gravatar.com/avatar/c2f093aae48ae803c3409e8eb2b2eb39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ramesh&#39;s gravatar image" /><p>Ramesh<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ramesh has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jan '11, 01:41</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-1866" class="comments-container"></div><div id="comment-tools-1866" class="comment-tools"></div><div class="clear"></div><div id="comment-1866-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1872"></span>

<div id="answer-container-1872" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1872-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>These temporary files are needed, but you can have them automatically removed on longer running captures. Look into the tshark man page and look at the -b option, the capture file ring buffer.</p><p>For the rest it's up to your system to clean up /tmp, which it does at reboot.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '11, 01:52</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-1872" class="comments-container"></div><div id="comment-tools-1872" class="comment-tools"></div><div class="clear"></div><div id="comment-1872-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

