+++
type = "question"
title = "PCAPNG support for storing information for decoding SSL/TLS"
description = '''I am the developer of a device which now maintains a queue of packet traffic from which you can generate a PCAPNG file on command. The resulting file can be easily downloaded and wonderfully opened by Wireshark. Thank you all for that.  I&#x27;ve also developed all of the crypto for that device (as we do...'''
date = "2016-10-14T07:27:00Z"
lastmod = "2016-10-14T07:37:00Z"
weight = 56368
keywords = [ "tls", "ssl", "pcapng", "dissector", "decryption" ]
aliases = [ "/questions/56368" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [PCAPNG support for storing information for decoding SSL/TLS](/questions/56368/pcapng-support-for-storing-information-for-decoding-ssltls)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56368-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am the developer of a device which now maintains a queue of packet traffic from which you can generate a PCAPNG file on command. The resulting file can be easily downloaded and wonderfully opened by Wireshark. Thank you all for that.</p><p>I've also developed all of the crypto for that device (as we don't use 3rd party software so as to be assured of being able to debug, not have to work-around, and respond quickly).</p><p>Regarding SSL decoding, I have access to the all of the key material for a connection, has Wireshark grown to support the master secret (whatever is needed) from the capture file?</p><p>I can decode when I have the private key. This is generally only with incoming TLS connections. Outgoing traffic (recently SMTP using STARTTLS) ends up encoded with the remote server's key. It would be so nice to include the key material in the capture file. I'd have to figure out how to log it in the queue but that's the fun stuff to do.</p></div><div id="question-tags" class="tags-container tags">tls ssl pcapng dissector decryption</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Oct '16, 07:27</strong></p><img src="https://secure.gravatar.com/avatar/7203c573a775bc6198814d357531940d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bscloutier&#39;s gravatar image" /><p>bscloutier<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bscloutier has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Oct '16, 13:28</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-56368" class="comments-container"></div><div id="comment-tools-56368" class="comment-tools"></div><div class="clear"></div><div id="comment-56368-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56369"></span>

<div id="answer-container-56369" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56369-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark has support for decryption using an RSA key file (when RSA key exchanges are in use) or the (pre-)master secrets. See <a href="http://security.stackexchange.com/a/42350/2630">this list</a> for all supported formats.</p><p>The pcapng format does not have support for including key material. There was a suggestion in the past, but nothing has really materialized: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9616">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9616</a></p><p>The current best practice is to create a second file that contains the key material (also known as "(pre-)master secrets key log file"). This file can then be <a href="https://wiki.wireshark.org/SSL#Using_the_.28Pre.29-Master-Secret">configured</a> in the SSL/TLS dissector. A common convention given a pcap "foo.pcapng" is to name the keylog file "foo.keys", but you use any name you like (I often use "premaster.txt").</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Oct '16, 07:37</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-56369" class="comments-container"><span id="56371"></span><div id="comment-56371" class="comment"><div id="post-56371-score" class="comment-score"></div><div class="comment-text"><p>Okay, Understood. As the capture file would contain many separate sessions each with its own key material I wonder how to handle that. Having the pre-master secret material available for each would be preferable to handling RSA private keys without password protection. I also do not have the private key for some sessions involving the device (certificate optional sometimes).</p><p>Please consider this my vote for an EPB option to carry pre-master secret key material if available. I would be happy to prototype this and help test/debug if anyone is interested in the Wireshark upgrade. - Thanks.</p></div><div id="comment-56371-info" class="comment-info"><span class="comment-age">(14 Oct '16, 08:11)</span> bscloutier</div></div><span id="56372"></span><div id="comment-56372" class="comment"><div id="post-56372-score" class="comment-score"></div><div class="comment-text"><p>Each session is identified by a unique Client Random value and can be mapped to a (pre-)master secret. So you would list it one by one, see for example the captures + keylog files at the <a href="https://wiki.wireshark.org/SampleCaptures#SSL_with_decryption_keys">SampleCaptures wiki</a>. This method is preferred over RSA key files since it always works. RSA keyfiles are limited to RSA key exchanges (which is removed in TLS 1.3).</p><p>If you would like to enable support for secrets in the pcapng format, you would first have to make it into the specification, see <a href="https://github.com/pcapng/pcapng">https://github.com/pcapng/pcapng</a> (otherwise the code will not be accepted in Wireshark as that would harm interop).</p></div><div id="comment-56372-info" class="comment-info"><span class="comment-age">(14 Oct '16, 08:24)</span> Lekensteyn</div></div><span id="56381"></span><div id="comment-56381" class="comment"><div id="post-56381-score" class="comment-score"></div><div class="comment-text"><p>In particular, note the "Join the <a href="https://www.winpcap.org/mailman/listinfo/pcap-ng-format">pcapng mailing list</a> to discuss" on the pcapng page to which Peter pointed you; that's the place to discuss additions to pcapng.</p></div><div id="comment-56381-info" class="comment-info"><span class="comment-age">(14 Oct '16, 13:31)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-56369" class="comment-tools"></div><div class="clear"></div><div id="comment-56369-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

