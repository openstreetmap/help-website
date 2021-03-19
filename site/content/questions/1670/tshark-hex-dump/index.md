+++
type = "question"
title = "tshark hex dump"
description = '''Using tshark 1.2.11 to get a hex dump of packet data gives an error: /opt/exp/sbin/tshark -r binary_gold -x &amp;gt; text_gold_new ** ERROR:print.c:794:print_hex_data: assertion failed: (edt-&amp;gt;pi.data_src) /opt/exp/sbin/tshark[5]: 2259 Abort(coredump) Is this a known bug in 1.2.11, and is it fixed in ...'''
date = "2011-01-07T08:09:00Z"
lastmod = "2011-01-07T08:09:00Z"
weight = 1670
keywords = [ "tshark" ]
aliases = [ "/questions/1670" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark hex dump](/questions/1670/tshark-hex-dump)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1670-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Using tshark 1.2.11 to get a hex dump of packet data gives an error:</p><p>/opt/exp/sbin/tshark -r binary_gold -x &gt; text_gold_new ** ERROR:print.c:794:print_hex_data: assertion failed: (edt-&gt;pi.data_src) /opt/exp/sbin/tshark[5]: 2259 Abort(coredump)</p><p>Is this a known bug in 1.2.11, and is it fixed in later versions?</p><p>Here is my version info:</p><p>$ /opt/exp/sbin/tshark -v TShark 1.2.11</p><p>Copyright 1998-2010 Gerald Combs [email protected] and contributors. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p><p>Compiled (32-bit) with GLib 2.17.7, with libpcap 1.1.1, with libz 1.2.3, without POSIX capabilities, without libpcre, without SMI, without c-ares, with ADNS, without Lua, without GnuTLS, with Gcrypt 1.2.2, without Kerberos, without GeoIP.</p><p>Running on Linux 2.6.33.3-85.fc13.i686.PAE, with libpcap version 1.1.1, Gcrypt 1.2.2.</p><p>Built using gcc 3.4.6.</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jan '11, 08:09</strong></p><img src="https://secure.gravatar.com/avatar/19a9302f956142a0f0bdccf1b31b734c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmcgahan&#39;s gravatar image" /><p>mmcgahan<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmcgahan has no accepted answers">0%</span></p></div></div><div id="comments-container-1670" class="comments-container"><span id="1675"></span><div id="comment-1675" class="comment"><div id="post-1675-score" class="comment-score">2</div><div class="comment-text"><p>Bugs should be reported on <a href="http://bugs.wireshark.org">the Wireshark bugzilla site</a>.</p></div><div id="comment-1675-info" class="comment-info"><span class="comment-age">(07 Jan '11, 12:15)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-1670" class="comment-tools"></div><div class="clear"></div><div id="comment-1670-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

