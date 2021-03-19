+++
type = "question"
title = "Help decoding ZKsoftware Stand-alone fingerprint reader protocol"
description = '''Hi! I just purchased a Stand-alone, linux-based fingerprint reader for T&amp;amp;A purposes from dealextreme. http://www.dealextreme.com/p/x628-staff-time-attendance-system-1500-user-standalone-linux-network-fingerprint-4966 The hardware seems good enough, but the naive guy I am, I thought that with thi...'''
date = "2011-05-18T00:25:00Z"
lastmod = "2011-05-18T17:56:00Z"
weight = 4113
keywords = [ "zksoftware", "protocol" ]
aliases = [ "/questions/4113" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Help decoding ZKsoftware Stand-alone fingerprint reader protocol](/questions/4113/help-decoding-zksoftware-stand-alone-fingerprint-reader-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4113-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi!</p><p>I just purchased a Stand-alone, linux-based fingerprint reader for T&amp;A purposes from dealextreme. <a href="http://www.dealextreme.com/p/x628-staff-time-attendance-system-1500-user-standalone-linux-network-fingerprint-4966">http://www.dealextreme.com/p/x628-staff-time-attendance-system-1500-user-standalone-linux-network-fingerprint-4966</a></p><p>The hardware seems good enough, but the naive guy I am, I thought that with this thing being Linux-based, it would have some kind of open API to download the data stored on the device. But the rather nasty software that comes with the product (even made Avast shout out that something is wrong) is Windows-only, and not at all what I need in order to integrate this puppy into my other programs.</p><p>I contacted zksoftware.com, but haven't received a reply yet, and am a bit pessimistic about their collaboration, judging by their website, and the fact that I couldn't find their Linux source code anywhere (GPL violation?)</p><p>So I did the next logical thing and simply used the included software to download the "punches" that were stored on the machine, and recorded the transaction with Wireshark - but I am a bit at a loss about what to do now. There are some promising ASCII characters in the dump, but I still can't make heads or tails out of this and would appreciate any help anyone could give me with this.</p><p>My plan is to write a (perl) module that would provide some kind of basic API, so that I, and anyone else, can "talk" to these devices. I would of course share my scripts online, for free.</p><p>I uploaded the conversation to: <a href="http://gometa.org/fingerprint.pcap">http://gometa.org/fingerprint.pcap</a></p><ul><li>The first approx. 5 seconds of traffic resulted from me clicking "connect".</li><li>The following data (20.44+ secs) seem to be related to the downloading of 32 records, each of which should include a timestamp, and a userid (000001 to 000006).</li></ul><p>thanks for any help!</p><p>M.</p></div><div id="question-tags" class="tags-container tags">zksoftware protocol</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 May '11, 00:25</strong></p><img src="https://secure.gravatar.com/avatar/5d93b56d083dd77eacd5bef79ef2b938?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="schweini&#39;s gravatar image" /><p>schweini<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="schweini has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 May '11, 18:32</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-4113" class="comments-container"></div><div id="comment-tools-4113" class="comment-tools"></div><div class="clear"></div><div id="comment-4113-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4124"></span>

<div id="answer-container-4124" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4124-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe the following helps? <a href="http://www.scribd.com/doc/54798939/Communication-Protocol-Manual-CMD">http://www.scribd.com/doc/54798939/Communication-Protocol-Manual-CMD</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 May '11, 17:56</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-4124" class="comments-container"><span id="4127"></span><div id="comment-4127" class="comment"><div id="post-4127-score" class="comment-score"></div><div class="comment-text"><p>Thanks that API description is a bot longer than another one I found, but they do share the problem of being in a language utterly, but not quite, completly unlike english! :)</p><p>Especially the checksum, which I would figure would be one the first things to get running, eludes me:</p><p>--SNIP--</p><p>Verification and (CheckSum) algorithm: According to unsign short integer accumulate the entire packet, till over 2147483648 (long 4 bytes), gains the low 2 byte values continue to add together again, depending on the position that the value is obtained to get ones complement, and transform it into the short integer (unsigned short 2 bytes), namely obtains the verification sum.</p><p>--SNAP--</p><p>Do you or anyone else know whether this might be some "standard" checksumming protocol? Or someone with more checksumming experience than me might be able to translate this into a more understandable way?</p><p>Cheers,</p><p>M.</p></div><div id="comment-4127-info" class="comment-info"><span class="comment-age">(18 May '11, 19:39)</span> schweini</div></div><span id="4128"></span><div id="comment-4128" class="comment"><div id="post-4128-score" class="comment-score">1</div><div class="comment-text"><p>It sounds to me like a description of the standard Internet checksum algorithm; to quote the description of that algorithm in RFC 793:</p><p>Checksum: 16 bits</p><pre><code>The checksum field is the 16 bit one&#39;s complement of the one&#39;s
complement sum of all 16 bit words in the header and text.  If a
segment contains an odd number of header and text octets to be
checksummed, the last octet is padded on the right with zeros to
form a 16 bit word for checksum purposes.  The pad is not
transmitted as part of the segment.</code></pre><p>See epan/in_cksum.c in the Wireshark source for a C implementation.</p></div><div id="comment-4128-info" class="comment-info"><span class="comment-age">(18 May '11, 19:59)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-4124" class="comment-tools"></div><div class="clear"></div><div id="comment-4124-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

