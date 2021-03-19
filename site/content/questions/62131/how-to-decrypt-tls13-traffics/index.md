+++
type = "question"
title = "How to decrypt TLS1.3 traffics?"
description = '''Hi I am using the daily build of Wireshark for monitoring some TLS1.3 traffics. I am wondering if there is any way I can decrypt the traffic?  Specifically, I can successfully decrypt TLS1.2 traffics by exporting the SSLKEYLOGFILE for Firefox to save its session keys and set this path in my SSL pref...'''
date = "2017-06-19T11:39:00Z"
lastmod = "2017-06-19T11:46:00Z"
weight = 62131
keywords = [ "decode", "tls", "tls.1.3", "ssl_decrypt" ]
aliases = [ "/questions/62131" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to decrypt TLS1.3 traffics?](/questions/62131/how-to-decrypt-tls13-traffics)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62131-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I am using the daily build of Wireshark for monitoring some TLS1.3 traffics. I am wondering if there is any way I can decrypt the traffic?</p><p>Specifically, I can successfully decrypt TLS1.2 traffics by exporting the SSLKEYLOGFILE for Firefox to save its session keys and set this path in my SSL preference in Wireshark. However, it doesn't work in TLS1.3.</p><p>Is it normal (not supported for TLS1.3)? or just a bug?</p></div><div id="question-tags" class="tags-container tags">decode tls tls.1.3 ssl_decrypt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jun '17, 11:39</strong></p><img src="https://secure.gravatar.com/avatar/c3d1b49b2211ff683647dc2a4c47eb41?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yctung&#39;s gravatar image" /><p>yctung<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yctung has no accepted answers">0%</span></p></div></div><div id="comments-container-62131" class="comments-container"></div><div id="comment-tools-62131" class="comment-tools"></div><div class="clear"></div><div id="comment-62131-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62132"></span>

<div id="answer-container-62132" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62132-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>TLS 1.3 is supported in Wireshark upcoming 2.4 (and by extension, the latest development version). Since most messages are encrypted however you need session secrets for decryption.</p><p>Unfortunately, NSS (the cryptographic library used by Firefox) has not been updated yet to dump these secrets (its most recent version is 3.31 as of this writing). You can track the latest status of this in <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=1287711">https://bugzilla.mozilla.org/show_bug.cgi?id=1287711</a></p><p>BoringSSL (as used by Google Chrome/Chromium) does however support this newer format, so you could give that a try. It is supported by <em>some</em> version (do not know exactly which).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '17, 11:46</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-62132" class="comments-container"><span id="62133"></span><div id="comment-62133" class="comment"><div id="post-62133-score" class="comment-score"></div><div class="comment-text"><p>Wow. That is a helpful answer, saving me lots of time digging into it. Thanks!</p></div><div id="comment-62133-info" class="comment-info"><span class="comment-age">(19 Jun '17, 11:52)</span> yctung</div></div><span id="62134"></span><div id="comment-62134" class="comment"><div id="post-62134-score" class="comment-score"></div><div class="comment-text"><p>More information about the status of TLS 1.3 can be found in: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12779">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12779</a> <a href="https://github.com/tlswg/tls13-spec/wiki/Implementations">https://github.com/tlswg/tls13-spec/wiki/Implementations</a> (Everything is basically done except for TLS 1.3 0RTT trial decryption, i.e. packets with 0RTT data for which you do not have the keys.)</p></div><div id="comment-62134-info" class="comment-info"><span class="comment-age">(19 Jun '17, 11:55)</span> Lekensteyn</div></div><span id="62486"></span><div id="comment-62486" class="comment"><div id="post-62486-score" class="comment-score"></div><div class="comment-text"><p>Hi. Just a follow up of this problem.</p><p>I try the NSS dump function in OpenSSL and also the Chrome (Canary). I can see sslkeylog.log is dumped correctly, but wireshark (nightly build) still can't understand TLS1.3 traffic. Attached an example of TLS1.3 in wireshark: <a href="http://imgur.com/a/odAwH">http://imgur.com/a/odAwH</a></p><p>Yu-Chih</p></div><div id="comment-62486-info" class="comment-info"><span class="comment-age">(03 Jul '17, 16:02)</span> yctung</div></div><span id="63639"></span><div id="comment-63639" class="comment"><div id="post-63639-score" class="comment-score"></div><div class="comment-text"><p>Hi <a href="https://ask.wireshark.org/users/35700/yctung">@yctung</a>, do you still have problems with the current version of Wireshark? If so, please open a bugreport and attach a pcap+keylog file.</p></div><div id="comment-63639-info" class="comment-info"><span class="comment-age">(24 Sep '17, 11:49)</span> Lekensteyn</div></div></div><div id="comment-tools-62132" class="comment-tools"></div><div class="clear"></div><div id="comment-62132-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

