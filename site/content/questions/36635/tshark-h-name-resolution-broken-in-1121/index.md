+++
type = "question"
title = "tshark -H name resolution broken in 1.12.1 ?"
description = '''Can anybody confirm that with 1.12.1 the host name resolution doesn&#x27;t work anymore?  hosts file: # Name Resolution with wireshark / tshark  10.55.56.168 net1.host1 10.49.50.61 net2.host2  Command  Z:&#92;traces&amp;gt;tshark -r trace.ee.cap -H hosts -w trace.ee.pcapng -v -W n (tshark.exe:3900): GLib-CRITICA...'''
date = "2014-09-26T07:23:00Z"
lastmod = "2014-09-26T09:35:00Z"
weight = 36635
keywords = [ "resolution", "hostname", "hosts", "tshark", "name" ]
aliases = [ "/questions/36635" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [tshark -H name resolution broken in 1.12.1 ?](/questions/36635/tshark-h-name-resolution-broken-in-1121)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36635-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can anybody confirm that with 1.12.1 the host name resolution doesn't work anymore?</p><p>hosts file:</p><pre><code># Name Resolution with wireshark / tshark  
10.55.56.168 net1.host1
10.49.50.61  net2.host2</code></pre><p>Command</p><pre><code>Z:\traces&gt;tshark -r trace.ee.cap -H hosts -w trace.ee.pcapng -v -W n
(tshark.exe:3900): GLib-CRITICAL **: g_hash_table_lookup: assertion &#39;hash_table != NULL&#39; failed
(tshark.exe:3900): GLib-CRITICAL **: g_hash_table_insert_internal: assertion &#39;hash_table != NULL&#39; failed
(tshark.exe:3900): GLib-CRITICAL **: g_hash_table_lookup: assertion &#39;hash_table != NULL&#39; failed
(tshark.exe:3900): GLib-CRITICAL **: g_hash_table_insert_internal: assertion &#39;hash_table != NULL&#39; failed
TShark 1.12.1 (v1.12.1-0-g01b65bf from master-1.12)
Copyright 1998-2014 Gerald Combs &lt;[email protected]&gt; and contributors.
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
Compiled (64-bit) with GLib 2.38.0, with WinPcap (4_1_3), with libz 1.2.5, with
SMI 0.4.8, with c-ares 1.9.1, with Lua 5.2, without Python, with GnuTLS 3.1.22,
with Gcrypt 1.6.0, without Kerberos, with GeoIP.
Running on 64-bit Windows 7 Service Pack 1, build 7601, without WinPcap.
Intel Xeon E312xx (Sandy Bridge), with 3558MB of physical memory.
Built using Microsoft Visual C++ 10.0 build 40219</code></pre><hr /><p>Edit:</p><p>I submitted Bug 10507 for this problem</p></div><div id="question-tags" class="tags-container tags">resolution hostname hosts tshark name</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '14, 07:23</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Sep '14, 12:58</p></div></div><div id="comments-container-36635" class="comments-container"></div><div id="comment-tools-36635" class="comment-tools"></div><div class="clear"></div><div id="comment-36635-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36639"></span>

<div id="answer-container-36639" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36639-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, the assertions should be removed but are harmless. In your command line I can see that you give -v option. Did you mean -V instead?</p><p>EDIT: I confirm the issue (resolution results are not stored in pcapng file). Could you please fill a bug to <a href="http://bugs.wireshark.org">http://bugs.wireshark.org</a>?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '14, 09:35</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Sep '14, 11:13</p></div></div><div id="comments-container-36639" class="comments-container"><span id="36643"></span><div id="comment-36643" class="comment"><div id="post-36643-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Bug 10507 Submitted</p></div><div id="comment-36643-info" class="comment-info"><span class="comment-age">(26 Sep '14, 12:59)</span> mrEEde</div></div><span id="37121"></span><div id="comment-37121" class="comment"><div id="post-37121-score" class="comment-score"></div><div class="comment-text"><p>Fixed in 1.12.1</p></div><div id="comment-37121-info" class="comment-info"><span class="comment-age">(16 Oct '14, 22:52)</span> mrEEde</div></div></div><div id="comment-tools-36639" class="comment-tools"></div><div class="clear"></div><div id="comment-36639-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

