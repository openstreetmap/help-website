+++
type = "question"
title = "Perl Net::Pcap Can not parse wireshark saved pcap file"
description = '''hello, I am writing a perl script to parse pcap file from wireshark with Net::Pcap module, here are the simple code:  use strict; use warnings; use utf8; use NetPacket::Ethernet qw(:types); use NetPacket::IP qw(:protos); use NetPacket::TCP; use Net::Pcap qw(:functions); my $pcap_file = &quot;test.cap&quot;; m...'''
date = "2012-07-22T02:17:00Z"
lastmod = "2012-07-22T14:04:00Z"
weight = 12896
keywords = [ "wireshark", "pcap", "tshark", "perl" ]
aliases = [ "/questions/12896" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Perl Net::Pcap Can not parse wireshark saved pcap file](/questions/12896/perl-netpcap-can-not-parse-wireshark-saved-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12896-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello,<br />
I am writing a perl script to parse pcap file from wireshark with Net::Pcap module, here are the simple code:<br />
</p><pre><code>use strict;
use warnings;
use utf8;
use NetPacket::Ethernet qw(:types);
use NetPacket::IP qw(:protos);
use NetPacket::TCP;
use Net::Pcap qw(:functions);
my $pcap_file = &quot;test.cap&quot;;
my $err = undef;
# read data from pcap file.
my $pcap = pcap_open_offline($pcap_file, \$err)
    or die &quot;Can&#39;t read $pcap_file : $err\n&quot;;
 #  loop over next 10 packets
pcap_loop($pcap, -1, \&amp;process_packet, &quot;just for the demo&quot;);
# close the device
pcap_close($pcap);
sub process_packet {
    my ($user_data, $header, $packet) = @_;
    my $ether_data = NetPacket::Ethernet-&gt;decode($packet);
    # Decode contents of TCP/IP packet contained within 
    # captured ethernet packet
    # Print all out where its coming from and where its 
    # going to!
    my $eth_type = $ether_data-&gt;{&#39;type&#39;};
    print &quot;prototype is $eth_type\n&quot;;
    if ($eth_type != NetPacket::Ethernet::ETH_TYPE_IP) {
        print &quot;non-ip protocol\n&quot;;
        exit;
    }
}</code></pre><p>I want to get the ethernet type from the pcap file from wireshark, but I just can get 0 any way, so I compare to tcpdump, tshark saved pcap file, it works well, so guess may wireshark save the pcap file in a slight different format, right?<br />
So, do I have to use tshark -w instead wireshark to capture the packets? Any tips?<br />
regards<br />
</p></div><div id="question-tags" class="tags-container tags">wireshark pcap tshark perl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jul '12, 02:17</strong></p><img src="https://secure.gravatar.com/avatar/d7511cd99041bcb5eda1ff4b6792b8c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="liunx&#39;s gravatar image" /><p>liunx<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="liunx has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jul '12, 08:00</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></br></p></div></div><div id="comments-container-12896" class="comments-container"><span id="12903"></span><div id="comment-12903" class="comment"><div id="post-12903-score" class="comment-score"></div><div class="comment-text"><p>I also used ubuntu12.04LST x86_64, I got libpcap, libnet-pcap-perl from apt,should I compile them from source?</p></div><div id="comment-12903-info" class="comment-info"><span class="comment-age">(22 Jul '12, 18:33)</span> liunx</div></div></div><div id="comment-tools-12896" class="comment-tools"></div><div class="clear"></div><div id="comment-12896-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="12897"></span>

<div id="answer-container-12897" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12897-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Current Wireshark/tshark versions use the pcapng format for the capture file. Net::Pcap can only read libpcap compatible files.</p><p>If that's the problem, please use Wireshark/tshark option -F to write pcap format.</p><blockquote><p><code>tshark -i eth0 -F libpcap -w /var/tmp/output.cap</code></p></blockquote><p><strong>UPDATE</strong>: It seems that Net::Pcap <strong>CAN read pcapng files</strong>, if libpcap can read that format (depends on the release of libpcap). I ran your script against the same file. Once in libpcap format and once in pcapng format. The script returned the same output (after I removed the exit statement). The output looks reasonable (correct ether_type).</p><p>So it's either a problem with your OS (libpcap version) or the input file (corrupt data).</p><p>My test OS: Ubuntu 12.04, latest patches.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '12, 03:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jul '12, 08:28</p></div></div><div id="comments-container-12897" class="comments-container"><span id="12904"></span><div id="comment-12904" class="comment"><div id="post-12904-score" class="comment-score"></div><div class="comment-text"><p>Thanks very much for your tips, when I saved as Wireshark - pcapng file, it works well, thanks again!</p></div><div id="comment-12904-info" class="comment-info"><span class="comment-age">(22 Jul '12, 19:18)</span> liunx</div></div><span id="12905"></span><div id="comment-12905" class="comment"><div id="post-12905-score" class="comment-score"></div><div class="comment-text"><p>So what format had you saved it in before? libpcap only handles pcap and pcap-ng format; it doesn't, for example, handle Network Monitor format, at least not currently.</p></div><div id="comment-12905-info" class="comment-info"><span class="comment-age">(22 Jul '12, 23:31)</span> Guy Harris ♦♦</div></div><span id="12906"></span><div id="comment-12906" class="comment"><div id="post-12906-score" class="comment-score"></div><div class="comment-text"><p>you are welcome. good luck with your further scripting efforts...</p></div><div id="comment-12906-info" class="comment-info"><span class="comment-age">(23 Jul '12, 00:50)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-12897" class="comment-tools"></div><div class="clear"></div><div id="comment-12897-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12902"></span>

<div id="answer-container-12902" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12902-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If your system has libpcap 1.1.0 or later, code using libpcap will be able to read pcap-ng files (as long as all network interfaces have the same link-layer header type; the current libpcap API doesn't support multiple link-layer header types in one file). If your Perl program was failing in</p><pre><code>my $pcap = pcap_open_offline($pcap_file, \$err)
    or die &quot;Can&#39;t read $pcap_file : $err\n&quot;;</code></pre><p>when you handed it a pcap-ng file, then that's probably the problem you had.</p><p>If the open <em>succeeded</em>, then either the file is a pcap file or you have libpcap 1.1.0 or later. If you're getting 0 for the Ethernet type, then either the file is <em>not</em> an Ethernet capture, in which case the 12th and 13th bytes of the packet are <em>not</em> an Ethernet type, or the packet is somehow corrupted.</p><p>A program that calls <code>pcap_open_live()</code>, <code>pcap_open_offline()</code>, or <code>pcap_create()</code> and <code>pcap_activate()</code>, and does not ever call <code>pcap_datalink()</code>, is almost certainly buggy; only if it does not look <em>at all</em> at the packet data or is a quick hack that opens a wired-in device name for capture is it not buggy.</p><p>You should, if <code>pcap_open_offline()</code> succeeds, call <code>pcap_datalink($pcap)</code> and check whether its return value is <code>DLT_EN10MB</code> (as defined by Net::Pcap; I don't know if it's just <code>DLT_EN10MB</code> or <code>Net::Pcap::DLT_EN10MB</code> or something such as that). If it is not <code>DLT_EN10MB</code>, your program should fail with a "this is not an Ethernet capture" error (unless you want to enhance it to handle other link-layer types).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '12, 14:04</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jul '12, 14:05</p></div></div><div id="comments-container-12902" class="comments-container"></div><div id="comment-tools-12902" class="comment-tools"></div><div class="clear"></div><div id="comment-12902-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

