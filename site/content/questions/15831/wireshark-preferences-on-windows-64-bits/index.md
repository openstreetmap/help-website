+++
type = "question"
title = "Wireshark Preferences on windows 64 Bits"
description = '''Hi, I&#x27;m using Wireshark 1.8.3 on Windows 7 64 Bits. I&#x27;m trying to specify Kerberos keytab file in the Wireshark--&amp;gt;Edit--&amp;gt;Preferences--&amp;gt;Protocols--&amp;gt;krb5. But the Wireshark GUI does not show the keytab filename path or parameter; I just see Reassemble Kerberos over TCP parameter. following...'''
date = "2012-11-12T11:00:00Z"
lastmod = "2012-11-12T12:45:00Z"
weight = 15831
keywords = [ "preferences_krb5" ]
aliases = [ "/questions/15831" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Preferences on windows 64 Bits](/questions/15831/wireshark-preferences-on-windows-64-bits)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15831-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm using Wireshark 1.8.3 on Windows 7 64 Bits. I'm trying to specify Kerberos keytab file in the Wireshark--&gt;Edit--&gt;Preferences--&gt;Protocols--&gt;krb5. But the Wireshark GUI does not show the keytab filename path or parameter; I just see Reassemble Kerberos over TCP parameter.</p><p>following the wiki, It should be possible to specify a keytab : "Specifying the keytab file to use You can specify the filename of the keytab file to use in the KRB5 preferences."</p><p>Any Idea how to specify a keytab in the GUI?</p><p>Thank you for your help.</p><p>Vincent.</p></div><div id="question-tags" class="tags-container tags">preferences_krb5</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Nov '12, 11:00</strong></p><img src="https://secure.gravatar.com/avatar/7d148db476cec967e4a714948f3426b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vincenth&#39;s gravatar image" /><p>vincenth<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vincenth has no accepted answers">0%</span></p></div></div><div id="comments-container-15831" class="comments-container"></div><div id="comment-tools-15831" class="comment-tools"></div><div class="clear"></div><div id="comment-15831-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="15835"></span>

<div id="answer-container-15835" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15835-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Help -&gt; About dialog for the 64-bit Windows version of 1.8.3 says:</p><pre><code>Compiled (64-bit) with GTK+ 2.24.10, with Cairo 1.10.2, with Pango 1.30.0, with
GLib 2.32.2, with WinPcap (4_1_2), with libz 1.2.5, without POSIX capabilities,
with SMI 0.4.8, with c-ares 1.7.1, with Lua 5.1, without Python, with GnuTLS
2.12.18, with Gcrypt 1.4.6, without Kerberos, with GeoIP, with PortAudio
V19-devel (built Oct  2 2012), with AirPcap.</code></pre><p>Note the "without Kerberos" - the 64-bit Windows version of Wireshark 1.8.3 doesn't include a Kerberos library, so there's no support for reading keytab files.</p><p>The 32-bit version says:</p><pre><code>Compiled (32-bit) with GTK+ 2.24.10, with Cairo 1.10.2, with Pango 1.30.0, with
GLib 2.32.2, with WinPcap (4_1_2), with libz 1.2.5, without POSIX capabilities,
with SMI 0.4.8, with c-ares 1.7.1, with Lua 5.1, without Python, with GnuTLS
2.12.18, with Gcrypt 1.4.6, with MIT Kerberos, with GeoIP, with PortAudio
V19-devel (built Oct  2 2012), with AirPcap.</code></pre><p>It <em>is</em> built with Kerberos, so it will support reading keytab files. If you switch to a 32-bit version, you will be able to read a keytab file.</p><p>(The problem is probably that we don't have a 64-bit version of the Kerberos library with which to link Wireshark.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '12, 12:45</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-15835" class="comments-container"><span id="15850"></span><div id="comment-15850" class="comment"><div id="post-15850-score" class="comment-score"></div><div class="comment-text"><p>Hi All,</p><p>Thank you for your help.</p><p>Rgds</p><p>Vincent.</p></div><div id="comment-15850-info" class="comment-info"><span class="comment-age">(13 Nov '12, 00:29)</span> vincenth</div></div></div><div id="comment-tools-15835" class="comment-tools"></div><div class="clear"></div><div id="comment-15835-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15834"></span>

<div id="answer-container-15834" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15834-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe <a href="http://ask.wireshark.org/questions/7408/keytab-kerberos">this</a> similar question helps?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '12, 12:34</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-15834" class="comments-container"></div><div id="comment-tools-15834" class="comment-tools"></div><div class="clear"></div><div id="comment-15834-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

