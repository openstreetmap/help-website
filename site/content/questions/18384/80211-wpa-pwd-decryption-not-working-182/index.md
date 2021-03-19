+++
type = "question"
title = "802.11 wpa-pwd decryption not working 1.8.2"
description = '''I have been searching around for someone else who has had the same issue for a little while and have given up. I was attempting to decrypt the traffic on my network which is using WPA (Personal) with Wireshark&#x27;s built-in decryption key&#x27;s tool and have been unsuccessful so far. I then tried decryptin...'''
date = "2013-02-06T20:30:00Z"
lastmod = "2013-02-06T21:20:00Z"
weight = 18384
keywords = [ "decryption", "802.11" ]
aliases = [ "/questions/18384" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [802.11 wpa-pwd decryption not working 1.8.2](/questions/18384/80211-wpa-pwd-decryption-not-working-182)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18384-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have been searching around for someone else who has had the same issue for a little while and have given up. I was attempting to decrypt the traffic on my network which is using WPA (Personal) with Wireshark's built-in decryption key's tool and have been unsuccessful so far.</p><p>I then tried decrypting the <em>wpa-Induction.pcap</em> (<a href="http://wiki.wireshark.org/HowToDecrypt802.11)">http://wiki.wireshark.org/HowToDecrypt802.11)</a> capture file and had <em>no luck</em>. Before I revert to a previous version of Wireshark where decryption was working (according to other posts here), does anyone have any suggestions to resolve this issue?<br />
</p><p>Thanks</p><p><strong>about/version information:</strong></p><pre><code>Version 1.8.2

Compiled (32-bit) with GTK+ 2.24.13, with Cairo 1.12.2, with Pango 1.30.1, with GLib 2.34.0, with libpcap, with libz 1.2.7, with POSIX capabilities (Linux), with SMI 0.4.8, with c-ares
1.9.1, with Lua 5.1, without Python, with GnuTLS
2.12.14, with Gcrypt 1.5.0, with MIT Kerberos, with GeoIP, with PortAudio V19-devel (built Oct  8 2012 16:25:16), with AirPcap.

Running on Linux 3.5.0-17-generic, with locale en_US.UTF-8, with libpcap version
1.3.0, with libz 1.2.7, GnuTLS 2.12.14, Gcrypt 1.5.0, without AirPcap.

Built using gcc 4.7.2.</code></pre></div><div id="question-tags" class="tags-container tags">decryption 802.11</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Feb '13, 20:30</strong></p><img src="https://secure.gravatar.com/avatar/f603f1eb37ddf2a5906384d784edbdac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="phelanx&#39;s gravatar image" /><p>phelanx<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="phelanx has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-18384" class="comments-container"><span id="18388"></span><div id="comment-18388" class="comment"><div id="post-18388-score" class="comment-score">1</div><div class="comment-text"><p>While the current maintenance release of stable branch would be sufficient, as this was fixed in 1.8.4 through <a href="http://anonsvn.wireshark.org/viewvc?revision=45696&amp;view=revision">r45696</a>.</p></div><div id="comment-18388-info" class="comment-info"><span class="comment-age">(06 Feb '13, 22:18)</span> Jaap ♦</div></div><span id="18395"></span><div id="comment-18395" class="comment"><div id="post-18395-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jaap. I figured it was a minor bug in the handling of the key, but a cursory search of bugzilla didn't show much.</p></div><div id="comment-18395-info" class="comment-info"><span class="comment-age">(07 Feb '13, 05:12)</span> phelanx</div></div></div><div id="comment-tools-18384" class="comment-tools"></div><div class="clear"></div><div id="comment-18384-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18385"></span>

<div id="answer-container-18385" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18385-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I've resolved my issue by moving to the bleeding edge -- Version 1.9.0 (SVN Rev 47530 from /trunk)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Feb '13, 21:20</strong></p><img src="https://secure.gravatar.com/avatar/f603f1eb37ddf2a5906384d784edbdac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="phelanx&#39;s gravatar image" /><p>phelanx<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="phelanx has no accepted answers">0%</span></p></div></div><div id="comments-container-18385" class="comments-container"></div><div id="comment-tools-18385" class="comment-tools"></div><div class="clear"></div><div id="comment-18385-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

