+++
type = "question"
title = "Exporting Decrypted 802.11 WPA/PSK Packets in PCAP Format"
description = '''Hello Experts,  I am looking for a way to export single packets that have been decrypted with a wpa-pwd.  When I export the packets, the generation of a new PCAP file works without a problem, but the packets are no longer in their decrypted state. The 802.11 radiotap header details are visible, but ...'''
date = "2015-11-30T07:02:00Z"
lastmod = "2015-11-30T17:30:00Z"
weight = 48086
keywords = [ "wpa-psk", "export", "pcap", "wifi", "802.11" ]
aliases = [ "/questions/48086" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Exporting Decrypted 802.11 WPA/PSK Packets in PCAP Format](/questions/48086/exporting-decrypted-80211-wpapsk-packets-in-pcap-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48086-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Experts,</p><p>I am looking for a way to export single packets that have been decrypted with a wpa-pwd.</p><p>When I export the packets, the generation of a new PCAP file works without a problem, but the packets are no longer in their decrypted state. The 802.11 radiotap header details are visible, but the data is no longer showing up.</p><p>I know that I can do a text based export, which keeps the full state of the packet, but I was hoping to get it exportable in a PCAP format.</p><p>Can anybody suggest a way of doing this (I am running version 1.12.2 )?</p><p>Kind Regards,</p><p>Josh</p></div><div id="question-tags" class="tags-container tags">wpa-psk export pcap wifi 802.11</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Nov '15, 07:02</strong></p><img src="https://secure.gravatar.com/avatar/fc13abd7c82055bfbec02496e094d39a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krypton&#39;s gravatar image" /><p>krypton<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krypton has no accepted answers">0%</span></p></div></div><div id="comments-container-48086" class="comments-container"></div><div id="comment-tools-48086" class="comment-tools"></div><div class="clear"></div><div id="comment-48086-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="48113"></span>

<div id="answer-container-48113" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48113-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I am looking for a way to export single packets that have been decrypted with a wpa-pwd.</p></blockquote><p>There is currently no such function in Wireshark for wifi decrypted frames. There is <code>File -&gt; Export PDUs</code>, but that does not work for decrypted wifi frames.</p><p><strong>What you can do:</strong></p><ul><li><code>File --&gt; Export Packet Dissection --&gt; as "C Arrays"</code></li><li>run a script (sample below) to convert that output to a format that <strong><a href="https://www.wireshark.org/docs/man-pages/text2pcap.html">text2pcap</a></strong> understands</li></ul><p><strong>Sample file:</strong></p><blockquote><p><a href="https://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=wpa-Induction.pcap">https://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=wpa-Induction.pcap</a></p></blockquote><p><strong>Example output of Export:</strong><br />
</p><pre><code>/ Decrypted CCMP data (631 bytes) /
static const unsigned char pkt439_1[631] = {
0xaa, 0xaa, 0x03, 0x00, 0x00, 0x00, 0x08, 0x00, / ........ /
0x45, 0x00, 0x02, 0x6f, 0x23, 0x5d, 0x40, 0x00, / E..o#]@. /
0x40, 0x06, 0x49, 0x07, 0xc0, 0xa8, 0x00, 0x32, / @.I....2 /
0x42, 0xe6, 0xc8, 0x64, 0xc9, 0xe9, 0x00, 0x50, / B..d...P /
0x71, 0x43, 0xd3, 0x97, 0x94, 0xfd, 0xd3, 0xe3, / qC...... /
0x80, 0x18, 0xff, 0xff, 0x45, 0xdc, 0x00, 0x00, / ....E... /
0x01, 0x01, 0x08, 0x0a, 0x03, 0x3a, 0x9f, 0x62, / .....:.b /
0x0d, 0x26, 0x71, 0x08, 0x47, 0x45, 0x54, 0x20, / .&amp;q.GET  /
0x2f, 0x77, 0x69, 0x6b, 0x69, 0x2f, 0x4c, 0x61, / /wiki/La /
0x6e, 0x64, 0x73, 0x68, 0x61, 0x72, 0x6b, 0x20, / ndshark  /
0x48, 0x54, 0x54, 0x50, 0x2f, 0x31, 0x2e, 0x31, / HTTP/1.1 /
0x0d, 0x0a, 0x48, 0x6f, 0x73, 0x74, 0x3a, 0x20, / ..Host:  /
0x65, 0x6e, 0x2e, 0x77, 0x69, 0x6b, 0x69, 0x70, / en.wikip /</code></pre><p><strong>Perl Script</strong> to convert that into text2pcap format:</p><pre><code>my $n = 0;

while (&lt;STDIN&gt;) {

    chomp;
    next if (not /Decrypted CCMP data/);
    while (&lt;STDIN&gt;) {
        next if (/static const unsigned/);
        last if (/^\}\;/);

        s/\/\*.*$//;
        s/\s+//g;
        s/0x//g;

        push(@hexdata,split(&#39;,&#39;));
    }

    # remove leading 8 bytes LLC
    foreach (1..8) {shift(@hexdata)};

    # print hex data in text2pcap format
    while (@hexdata) {
        printf &quot;%06x &quot;, $n;
        foreach (1..16) { print shift(@hexdata) . &#39; &#39;};

        $n += 16;
        print &quot;\n&quot;;
    }

    $n = 0;
    print &quot;\n&quot;;
}</code></pre><p><strong>Run the perl script</strong> like this:</p><blockquote><p>cat exported.c | perl convert.pl &gt; exported.txt<br />
text2pcap -e 0x800 exported.txt exported.pcap<br />
</p></blockquote><p><strong>Sample output of perl script:</strong> (text2pcap format)</p><pre><code>000000 45 00 02 6f 23 5d 40 00 40 06 49 07 c0 a8 00 32 
000010 42 e6 c8 64 c9 e9 00 50 71 43 d3 97 94 fd d3 e3 
000020 80 18 ff ff 45 dc 00 00 01 01 08 0a 03 3a 9f 62 
000030 0d 26 71 08 47 45 54 20 2f 77 69 6b 69 2f 4c 61 
000040 6e 64 73 68 61 72 6b 20 48 54 54 50 2f 31 2e 31 
000050 0d 0a 48 6f 73 74 3a 20 65 6e 2e 77 69 6b 69 70 
000060 65 64 69 61 2e 6f 72 67 0d 0a 55 73 65 72 2d 41 
000070 67 65 6e 74 3a 20 4d 6f 7a 69 6c 6c 61 2f 35 2e 
000080 30 20 28 4d 61 63 69 6e 74 6f 73 68 3b 20 55 3b 
000090 20 50 50 43 20 4d 61 63 20 4f 53 20 58 20 4d 61 
0000a0 63 68 2d 4f 3b 20 65 6e 2d 55 53 3b 20 72 76 3a 
0000b0 31 2e 38 2e 30 2e 39 29 20 47 65 63 6b 6f 2f 32 
0000c0 30 30 36 31 32 30 36 20 46 69 72 65 66 6f 78 2f 
0000d0 31 2e 35 2e 30 2e 39 0d 0a 41 63 63 65 70 74 3a 
0000e0 20 74 65 78 74 2f 78 6d 6c 2c 61 70 70 6c 69 63 
0000f0 61 74 69 6f 6e 2f 78 6d 6c 2c 61 70 70 6c 69 63 </code></pre><p><strong>Resulting pcap file</strong></p><p>only screenshot as cloudshark.org has closed the free public file upload.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/48086_screenshot.png" alt="alt text" /></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Nov '15, 17:30</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 01 Dec '15, 00:00</p></div></div><div id="comments-container-48113" class="comments-container"><span id="48118"></span><div id="comment-48118" class="comment"><div id="post-48118-score" class="comment-score"></div><div class="comment-text"><p>voted for this answer because</p><ul><li><p>as compared to the other one, it does not require to hand over the wpa "password" along with the capture, as I assume that avoidance of this need was the very goal of the exercise (leaving aside that I strongly suspect that if the wpa session has already been rekeyed since the EAPOL exchange took place, it would not work anyway)</p></li><li><p>it highlights things that are not obvious (i.e. that it depends on the output format choice whether deciphered packet contents can be exported or not)</p></li><li><p>I'm a perl fan myself ;-)</p></li></ul></div><div id="comment-48118-info" class="comment-info"><span class="comment-age">(01 Dec '15, 00:46)</span> sindy</div></div></div><div id="comment-tools-48113" class="comment-tools"></div><div class="clear"></div><div id="comment-48113-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="48105"></span>

<div id="answer-container-48105" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48105-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could copy the EAPOL exchange and the desired packet. Then the desired packet will be decrypted when you open the PCAP file. But please note that the EAPOL exchange must contain all 4 frames.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Nov '15, 12:01</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span> </br></br></p></div></div><div id="comments-container-48105" class="comments-container"></div><div id="comment-tools-48105" class="comment-tools"></div><div class="clear"></div><div id="comment-48105-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

