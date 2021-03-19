+++
type = "question"
title = "How to export hex and timestamp"
description = '''Hi all, I want to export raw hexadecimal values and timestamp of all my selected packets. Unfortunately exporting as &quot;C arrays&quot; does not shows the timestamp and also includes quite annoying ASCII representation. Moreover the exported file is not in a format like &quot;one packet per line&quot;. All this makes...'''
date = "2012-11-15T06:42:00Z"
lastmod = "2012-11-15T12:56:00Z"
weight = 15928
keywords = [ "excel", "dissector", "export", "timestamp", "hex" ]
aliases = [ "/questions/15928" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How to export hex and timestamp](/questions/15928/how-to-export-hex-and-timestamp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15928-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I want to export raw hexadecimal values and timestamp of all my selected packets.</p><p>Unfortunately exporting as "C arrays" does not shows the timestamp and also includes quite annoying ASCII representation.</p><p>Moreover the exported file is not in a format like "one packet per line". All this makes my life quite difficult trying to tokenize strings with sed and tr...</p><p>Is there any other option?</p><p>In the UDP payload of my packets are contained fields of a simple protocol that I defined for research proposes and I need to analyze those fields together with the time stamp.</p><p>I was considering to create a dissector but, since my lack of experience, it turns to be quite complicated and time consuming for my purpose.</p><p>To give an example of the output that I'd like to get:</p><p>This is what I'd like to have:</p><pre><code>2012-11-15,  12:53:32.1432, 0x60, 0x00, 0x00, 0x00, 0x00, 0x2b, 0x11, 0x41, 0x20, 0x01, 0x07, 0x70, 0x01, 0x9e, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0b, 0x41, 0x20, 0x01, 0x07, 0x70, 0x01, 0x9e, 0x00, 0x03</code></pre><p>This is what I currently get exporting in "C Arrays"</p><pre><code>/* Frame (83 bytes) */
static const unsigned char pkt63[83] = {
0x60, 0x00, 0x00, 0x00, 0x00, 0x2b, 0x11, 0x41, /* `....+.A */
0x20, 0x01, 0x07, 0x70, 0x01, 0x9e, 0x00, 0x03, /*  ..p.... */
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0b, 0x41, /* .......A */
0x20, 0x01, 0x07, 0x70, 0x01, 0x9e, 0x00, 0x03, /*  ..p.... */
};</code></pre><p>Btw, the previous Wireshark version (1.6.11) has a slightly better "C Array" output because it does not show the ASCII part...</p><p>Is "hexdump" used there?</p><p>Thanks a million</p><p>Davide</p><p>Any help/comment is much appreciated</p><p>Thanks and regards</p><p>Davide</p></div><div id="question-tags" class="tags-container tags">excel dissector export timestamp hex</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Nov '12, 06:42</strong></p><img src="https://secure.gravatar.com/avatar/6ceca94eb48b5579c804334452d699aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Davide&#39;s gravatar image" /><p>Davide<br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Davide has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Nov '12, 07:13</p></div></div><div id="comments-container-15928" class="comments-container"></div><div id="comment-tools-15928" class="comment-tools"></div><div class="clear"></div><div id="comment-15928-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="15932"></span>

<div id="answer-container-15932" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15932-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><em>Is there any other option?</em></p><p>This is the closest thing I know that exists today that might help you:</p><pre><code>tshark -r somefile.pcap -T fields -e frame.time -e data</code></pre><p>Using your example, the output will be something like follows:</p><pre><code>Nov 15, 2012 12:53:32.1432 60000000002b114120010770019e00030000000000000b4120010770019e0003</code></pre><p>Note: You probably want to qualify the output by specifying a read filter to only match those packets containing your particular protocol, e.g., <code>-R "udp.port eq &lt;your port&gt;"</code> or similar.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Nov '12, 11:07</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Nov '12, 11:12</p></div></div><div id="comments-container-15932" class="comments-container"><span id="15934"></span><div id="comment-15934" class="comment"><div id="post-15934-score" class="comment-score"></div><div class="comment-text"><p>Many thanks, your suggestion is very close to the solution. Unfortunately, wireshark interprets most of my packets as RX protocol (bad luck) and the output -e data is empty.</p><p>Only few of them are interpreted as raw UDP Is there a way to tell tshark to interpret every packet as raw UDP?</p><p>One more thing: I would prefere to extract the whole raw packet and not just the UDP payload (-e data) otherwise I have to include many other fields as IPv6.src dst port ...</p><p>Just a raw hex packet with time stamp would be perfec!</p><p>Thanks a million</p></div><div id="comment-15934-info" class="comment-info"><span class="comment-age">(15 Nov '12, 12:12)</span> Davide</div></div><span id="15936"></span><div id="comment-15936" class="comment"><div id="post-15936-score" class="comment-score"></div><div class="comment-text"><p>You could try disabling the IPv[4|6] dissectors in Wireshark first, and then run the <code>tshark</code> command. Since those protocols will be disabled, the data <em>"dissector"</em> will include those bytes as part of the output as well. (Wireshark: Analyze -&gt; Enabled Protocols -&gt; deselect the protocols of interest.)</p><p>Note that the <code>-R "udp.port eq &lt;your port&gt;"</code> read filter won't work anymore because the UDP dissector will no longer be called, so you may want to pre-filter the capture file, saving only your packets to a separate capture file and then work with that file.</p></div><div id="comment-15936-info" class="comment-info"><span class="comment-age">(15 Nov '12, 12:28)</span> cmaynard ♦♦</div></div><span id="15967"></span><div id="comment-15967" class="comment"><div id="post-15967-score" class="comment-score"></div><div class="comment-text"><p>This works like a charm. I disabled all protocol dissectors and used tshark to print timestamp and raw data as you suggested.</p><p>Thanks a million!</p></div><div id="comment-15967-info" class="comment-info"><span class="comment-age">(16 Nov '12, 07:53)</span> Davide</div></div></div><div id="comment-tools-15932" class="comment-tools"></div><div class="clear"></div><div id="comment-15932-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15931"></span>

<div id="answer-container-15931" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15931-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Not a direct answer but there are several options for creating a dissector, some are easier (but possibly less flexible) than others:</p><ul><li>A C based dissector - full access to all functionality, although the API is huge and can be overwhelming at first</li><li>A Lua based dissector - access to all the functionality offered though the Lua API</li><li>A Python based dissector - access to all the functionality offered though the Python API (not used much AFAIK)</li><li><a href="http://wsgd.free.fr/">WSGD</a> - A plugin that allows you to define dissection based on text files</li></ul><p>Personally I've only done 'C' dissectors so I have no idea if the other options are "easier" in some undefinable way.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Nov '12, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-15931" class="comments-container"><span id="15935"></span><div id="comment-15935" class="comment"><div id="post-15935-score" class="comment-score"></div><div class="comment-text"><p>thank you very much. I'll try WSGD</p></div><div id="comment-15935-info" class="comment-info"><span class="comment-age">(15 Nov '12, 12:12)</span> Davide</div></div></div><div id="comment-tools-15931" class="comment-tools"></div><div class="clear"></div><div id="comment-15931-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15939"></span>

<div id="answer-container-15939" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15939-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you just want the HEX dump of the whole packet (or parts of it), tshark/wireshark is probably not the right tool for you, as you don't need any of its packet dissecting capabilities.</p><p>Please try my perl script instead. Save it as <code>dump-packet.pl</code> and then call it like this:</p><blockquote><p><code>perl dump-packet.pl input.cap</code></p></blockquote><p>You can choose to print the whole packet, the IP part or just the UDP payload, by setting the variables <strong>print_packet</strong> or <strong>print_ip</strong> or <strong>print_udp</strong>.</p><p>The script may not be perfect, but I'm sure you can modify it to your needs ;-)</p><pre><code>#!/usr/bin/perl

use warnings;
use strict;
use Net::Pcap;
use NetPacket::Ethernet qw(eth_strip);
use NetPacket::IP qw(:ALL);
use NetPacket::UDP;
use POSIX qw(strftime);

my $pcap_file = $ARGV[0];

my $print_packet = 1;
my $print_ip = 0;
my $print_udp = 0;

my $error;

my $pcap = Net::Pcap::open_offline($pcap_file, \$error) or die(&quot;FATAL: cannot open $pcap_file -&gt; ERROR: $error\n&quot;);

Net::Pcap::loop($pcap, -1, \&amp;process_packet, &#39;&#39;);
Net::Pcap::close($pcap);

sub process_packet {   
    my ($user_data,$header, $packet) = @_;

    #--- get timestamp from packet header
    my $time_stamp =  strftime(&quot;%Y-%m-%d, %H:%M:%S&quot;,localtime($header-&gt;{tv_sec})); 
    $time_stamp .= &quot;.&quot; . $header-&gt;{tv_usec}; 

    my $hex_string = &#39;&#39;;

    if ($print_packet) {
       $hex_string = print_hex($packet);
    }

    my $ip = NetPacket::IP-&gt;decode(eth_strip($packet));
    my $src = $ip-&gt;{src_ip};
    my $dst = $ip-&gt;{dest_ip};

    if ($print_ip) {
       $hex_string = print_hex($ip);
    }

    if ($ip-&gt;{proto} == IP_PROTO_UDP) {
        my $udp = NetPacket::UDP-&gt;decode($ip-&gt;{data});
        my $udp_payload = $udp-&gt;{data};

        if ($print_udp) {
           $hex_string = print_hex($udp_payload);
        }
    }

   print &quot;$time_stamp, $hex_string\n&quot;;
}

sub print_hex {
   my $data = shift;

   return &#39;0x&#39; . join(&#39;, 0x&#39;,unpack(&quot;H2&quot; x length($data),$data));
}</code></pre><p><strong>Sample output:</strong></p><p><code> 2012-09-10, 13:06:21.726884, 0x00, 0x09, 0x0f, 0x09, 0x0f, 0x05, 0x00, 0x21, 0x6a, 0x46, 0x46, 0x38, 0x08, 0x00, 0x45, 0x00,</code></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Nov '12, 12:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Nov '12, 13:00</p></div></div><div id="comments-container-15939" class="comments-container"><span id="15968"></span><div id="comment-15968" class="comment"><div id="post-15968-score" class="comment-score"></div><div class="comment-text"><p>Many thanks for your script. Unfortunately I couldn't make it working on my Mac (so far many libs are missing)... I'll keep it in my todolist anyway. Thanks again</p></div><div id="comment-15968-info" class="comment-info"><span class="comment-age">(16 Nov '12, 07:57)</span> Davide</div></div><span id="15970"></span><div id="comment-15970" class="comment"><div id="post-15970-score" class="comment-score"></div><div class="comment-text"><p>Installing the libs is pretty simple. Run these commands:</p><blockquote><p><code>perl -MCPAN -e shell</code><br />
</p></blockquote><p>After the shell started, type:</p><blockquote><p><code>install Net::Pcap</code><br />
<code>install NetPacket::EthernetNet</code><br />
<code>install NetPacket::IP</code><br />
<code>install NetPacket::UDP</code><br />
</p></blockquote><p>Watch for any errors during the installation of the Perl modules.</p><p>Good luck.</p></div><div id="comment-15970-info" class="comment-info"><span class="comment-age">(16 Nov '12, 08:19)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-15939" class="comment-tools"></div><div class="clear"></div><div id="comment-15939-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

