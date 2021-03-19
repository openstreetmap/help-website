+++
type = "question"
title = "bulk extraction of UDP payload data"
description = '''Hi All, In brief, what I have:  50GB (100 x 512MB) pcap files captured with dumpcap containing multicast UDP data (mixed target ports). Matlab scripts dealing with the raw binary payload data for a selection of ports.  What I want to do:  For each of the 100 pcap files, extract raw UDP binary PAYLOA...'''
date = "2015-11-03T05:49:00Z"
lastmod = "2015-11-03T07:13:00Z"
weight = 47183
keywords = [ "binary", "udp", "payload" ]
aliases = [ "/questions/47183" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [bulk extraction of UDP payload data](/questions/47183/bulk-extraction-of-udp-payload-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47183-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>In brief, what I have:</p><ul><li>50GB (100 x 512MB) pcap files captured with dumpcap containing multicast UDP data (mixed target ports).</li><li>Matlab scripts dealing with the raw binary payload data for a selection of ports.</li></ul><p>What I want to do:</p><ul><li>For each of the 100 pcap files, extract raw UDP binary PAYLOAD-ONLY data sent to a specific port X.</li><li>Repeat process for each port of interest (eg if I had 7 ports of interest, I'd end up with 700 files containing payload data)</li></ul><p>Essentially it is the same conversion performed by Wiresharks "Follow UDP Stream", but the data volume is too high to use that feature.</p><p>I noticed a couple of other threads dealing with this or similar issues:</p><p><a href="https://ask.wireshark.org/questions/38998/automating-extraction-of-udp-payload-from-pcap-file/">https://ask.wireshark.org/questions/38998/automating-extraction-of-udp-payload-from-pcap-file/</a></p><p><a href="https://ask.wireshark.org/questions/15374/dump-raw-packet-data-field-only/">https://ask.wireshark.org/questions/15374/dump-raw-packet-data-field-only/</a></p><p>but I feel I am missing something, it seems the data has to go to ASCII first? Rather than straight to binary. With such large volumes of data, I was hoping there might be a perl or python trick out there to help batch this job. I'm not that familiar with PERL, but I have started looking into the Net::Pcap libraries.</p><p>I have no use for the additional packet info/stats collected by dumpcap, so in hindsight I probably would have been better off coding up a simple bit of software to receive and record the UDP data of interest directly, but it's a bit late for that now.</p><p>Any further tips greatly appreciated.</p></div><div id="question-tags" class="tags-container tags">binary udp payload</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Nov '15, 05:49</strong></p><img src="https://secure.gravatar.com/avatar/cf186b966d6d2b4af4810006086e557a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kevenofnine&#39;s gravatar image" /><p>kevenofnine<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kevenofnine has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Nov '15, 06:15</p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-47183" class="comments-container"></div><div id="comment-tools-47183" class="comment-tools"></div><div class="clear"></div><div id="comment-47183-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47185"></span>

<div id="answer-container-47185" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47185-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please take a look at my perl code in a similar question. Maybe you can use it as a starting point.</p><blockquote><p><a href="https://ask.wireshark.org/questions/15928/how-to-export-hex-and-timestamp">https://ask.wireshark.org/questions/15928/how-to-export-hex-and-timestamp</a><br />
</p></blockquote><p>Instead of printing the hex representation of the UDP payload, you could write it to a binary file.</p><p><strong>++UPDATE++</strong></p><p>So, the code could look like this (works on my systems).</p><p>BTW: Net::Pcap will be able to read the pcap format by default. It will be able to alo read pcap-ng, if the version of libpacap on your system does support it, otherwise you will get an error message ("FATAL: cannot open 47183.pcapng -&gt; ERROR: bad dump file format")</p><pre><code>#!/usr/bin/perl

use warnings;
use strict;
use Net::Pcap;
use NetPacket::Ethernet qw(eth_strip);
use NetPacket::IP qw(:ALL);
use NetPacket::UDP;
use POSIX qw(strftime);

my $pcap_file = $ARGV[0];

my $port_list = {
    53 =&gt; 1,
    5353 =&gt; 1,
    1900 =&gt; 1
};

my $filehandles;

my $error;

my $pcap = Net::Pcap::open_offline($pcap_file, \$error) or die(&quot;FATAL: cannot open $pcap_file -&gt; ERROR: $error\n&quot;);

Net::Pcap::loop($pcap, -1, \&amp;process_packet, &#39;&#39;);
Net::Pcap::close($pcap);

sub process_packet {   
    my ($user_data,$header, $packet) = @_;

    my $ip = NetPacket::IP-&gt;decode(eth_strip($packet));
    my $src = $ip-&gt;{src_ip};
    my $dst = $ip-&gt;{dest_ip};

    if ($ip-&gt;{proto} == IP_PROTO_UDP) {

        my $udp = NetPacket::UDP-&gt;decode($ip-&gt;{data});
        my $udp_sport = $udp-&gt;{src_port};
        my $udp_dport = $udp-&gt;{dest_port};

        if (not exists $port_list-&gt;{$udp_dport}) {
            return;
        }

        my $session = &quot;${src}_${udp_sport}__${dst}_${udp_dport}&quot;;

        write_payload($session, $udp-&gt;{data});
    }

}

sub write_payload {

    my $session = shift;
    my $data = shift;
    my $fh;

    if (exists $filehandles-&gt;{$session}) {
        $fh = $filehandles-&gt;{$session};
    } else { 
        my $filename = $pcap_file . &quot;__&quot; . $session . &quot;.payload&quot;;
        open($fh, &quot;&gt;&gt;:raw&quot;, $filename) || die(&quot;FATAL: cannot write to file $filename\n&quot;);
        $filehandles-&gt;{$session} = $fh;
    }

    print $fh $data;
}</code></pre><p>My script writes only the payload of one direction to the file (it looks for destination port), as it won't make much sense to mix data of both directions, packet by packet, into the binary output file. If you need something different, please adjust the script to your needs.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Nov '15, 07:13</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Nov '15, 12:03</p></div></div><div id="comments-container-47185" class="comments-container"></div><div id="comment-tools-47185" class="comment-tools"></div><div class="clear"></div><div id="comment-47185-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

