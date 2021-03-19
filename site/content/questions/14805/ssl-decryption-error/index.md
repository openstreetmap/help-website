+++
type = "question"
title = "SSL Decryption Error"
description = '''I keep getting a [Can&#x27;t load private key from filename.pem. Any idea what the problem is and how to resolve it? Walter'''
date = "2012-10-09T00:57:00Z"
lastmod = "2012-10-09T10:06:00Z"
weight = 14805
keywords = [ "ssl", "error", "decryption" ]
aliases = [ "/questions/14805" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SSL Decryption Error](/questions/14805/ssl-decryption-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14805-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I keep getting a [Can't load private key from <em>filename.pem</em>.</p><p>Any idea what the problem is and how to resolve it?</p><p>Walter</p></div><div id="question-tags" class="tags-container tags">ssl error decryption</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '12, 00:57</strong></p><img src="https://secure.gravatar.com/avatar/08ceaa93ec93bcecf429815ccc39e803?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Walter%20Benton&#39;s gravatar image" /><p>Walter Benton<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Walter Benton has no accepted answers">0%</span></p></div></div><div id="comments-container-14805" class="comments-container"><span id="14808"></span><div id="comment-14808" class="comment"><div id="post-14808-score" class="comment-score"></div><div class="comment-text"><p>My current Wireshark version info is a follows:</p><p>Version 1.8.2 (SVN Rev 44520 from /trunk-1.8)</p><p>Copyright 1998-2012 Gerald Combs [email protected] and contributors. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p><p>Compiled (32-bit) with GTK+ 2.24.10, with Cairo 1.10.2, with Pango 1.30.0, with GLib 2.32.2, with WinPcap (4_1_2), with libz 1.2.5, without POSIX capabilities, with SMI 0.4.8, with c-ares 1.7.1, with Lua 5.1, without Python, with GnuTLS 2.12.18, with Gcrypt 1.4.6, with MIT Kerberos, with GeoIP, with PortAudio V19-devel (built Aug 15 2012), with AirPcap.</p><p>Running on 32-bit Windows 7 Service Pack 1, build 7601, with WinPcap version 4.1.2 (packet.dll version 4.1.0.2001), based on libpcap version 1.0 branch 1_0_rel0b (20091008), GnuTLS 2.12.18, Gcrypt 1.4.6, without AirPcap.</p><p>Built using Microsoft Visual C++ 10.0 build 40219</p><p>Wireshark is Open Source Software released under the GNU General Public License.</p><p>Check the man page and <a href="http://www.wireshark.org">http://www.wireshark.org</a> for more information.</p><p>Walter</p></div><div id="comment-14808-info" class="comment-info"><span class="comment-age">(09 Oct '12, 01:47)</span> Walter Benton</div></div></div><div id="comment-tools-14805" class="comment-tools"></div><div class="clear"></div><div id="comment-14805-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14820"></span>

<div id="answer-container-14820" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14820-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Probably a wrong key format in the file. Either an encrypted key with the wrong passphrase or an invalid PEM encoding (char/line missing), etc. Please take a look at the SSL debug file. It will tell you more about the problem.</p><blockquote><p><code>Edit -&gt; Preferences -&gt; Protocols -&gt; SSL -&gt; SSL debug file</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Oct '12, 10:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-14820" class="comments-container"></div><div id="comment-tools-14820" class="comment-tools"></div><div class="clear"></div><div id="comment-14820-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

