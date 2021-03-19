+++
type = "question"
title = "Strip off GTP Headers"
description = '''Hello, I&#x27;m trying to strip off the GTP headers of a Gn trace and be left with the TCP/IP stream, which I can then feed into tcptrace for analysis. Any idea how this can be done? What layer 2 protocol is then used for the IP packets, which won&#x27;t have the GTP headers anymore? Thanks, Dan'''
date = "2012-02-23T00:44:00Z"
lastmod = "2013-09-27T06:22:00Z"
weight = 9180
keywords = [ "gtp", "header", "tcptrace", "strip" ]
aliases = [ "/questions/9180" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Strip off GTP Headers](/questions/9180/strip-off-gtp-headers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9180-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I'm trying to strip off the GTP headers of a Gn trace and be left with the TCP/IP stream, which I can then feed into tcptrace for analysis. Any idea how this can be done? What layer 2 protocol is then used for the IP packets, which won't have the GTP headers anymore? Thanks, Dan</p></div><div id="question-tags" class="tags-container tags">gtp header tcptrace strip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Feb '12, 00:44</strong></p><img src="https://secure.gravatar.com/avatar/ab01eaa7365fcdfd5e28b002d284f1b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dan%20Eman&#39;s gravatar image" /><p>Dan Eman<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dan Eman has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jul '12, 23:36</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-9180" class="comments-container"></div><div id="comment-tools-9180" class="comment-tools"></div><div class="clear"></div><div id="comment-9180-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="13029"></span>

<div id="answer-container-13029" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13029-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use <a href="http://bittwist.sourceforge.net/index.html">bittwiste</a> (Linux and Windows version available).</p><blockquote><p><code>bittwiste -I gtp-u.pcap -O gtp-stripped.pcap -D 15-54</code></p></blockquote><p>This removes (-D) the frame IP-, UDP- and GTP-Header. Result: The encapsulated IP header will be the new frame IP header ;-) Maybe you'll have to adjust the number of stripped bytes for your environment (IP Options).</p><p>It's easier to look at the sample data:</p><blockquote><p><code>GTP: http://cloudshark.org/captures/374cf36574b6</code><br />
<code>GTP Stripped: http://cloudshark.org/captures/69de59cb48d6</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '12, 09:35</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jul '12, 09:36</p></div></div><div id="comments-container-13029" class="comments-container"><span id="13044"></span><div id="comment-13044" class="comment"><div id="post-13044-score" class="comment-score"></div><div class="comment-text"><p>@Kurt, I guess the range depends on the version of GTP? I looked at another capture file from the Wireshark menagerie (<code>3503-rdp_2_packets.trc</code>) where the version was indicated as <em>"GTP release 97/98"</em> and the GTP header was 20 bytes. It looks like your capture file has <em>"GTP release 99"</em>, which apparently only has a 12 byte GTP header, thus I assume the range for a 97/98 version would be <code>-D 15-62</code>.</p></div><div id="comment-13044-info" class="comment-info"><span class="comment-age">(26 Jul '12, 18:29)</span> cmaynard ♦♦</div></div><span id="13050"></span><div id="comment-13050" class="comment"><div id="post-13050-score" class="comment-score"></div><div class="comment-text"><p>good hint. Thanks!</p><p>Yes, the byte range may vary, depending on IP Options and apparently also GTP version. But it's easy to find the byte range in Wireshark by looking at the packet bytes pane. BTW: Is that trace file from your personal archive or somewhere on the internet?</p></div><div id="comment-13050-info" class="comment-info"><span class="comment-age">(26 Jul '12, 22:50)</span> Kurt Knochner ♦</div></div><span id="13074"></span><div id="comment-13074" class="comment"><div id="post-13074-score" class="comment-score"></div><div class="comment-text"><p>The capture file is from Wireshark's own collection of capture files that are submitted in bug reports, on the <a href="http://wiki.wireshark.org/SampleCaptures">wiki</a>, through the mailing lists, etc. It's a really useful collection, but unfortunately, I don't know a way for everyone to access them - well, those not marked as "private" that is. If there's another developer who knows how to do it, please post the solution. If there is no way currently, maybe someone (Gerald?) could make it possible for the non-private capture files to be made available for download by the general public?</p></div><div id="comment-13074-info" class="comment-info"><span class="comment-age">(27 Jul '12, 05:53)</span> cmaynard ♦♦</div></div><span id="13077"></span><div id="comment-13077" class="comment"><div id="post-13077-score" class="comment-score"></div><div class="comment-text"><blockquote><p>If there is no way currently, maybe someone (Gerald?) could make it possible for the non-private capture files to be made available for download by the general public?</p></blockquote><p>That would really help! Sometimes it's easier to understand a problem with a capture file and the Wireshark Sample Captures (wiki) are kind of limited to the well known protocols (more or less).</p></div><div id="comment-13077-info" class="comment-info"><span class="comment-age">(27 Jul '12, 05:59)</span> Kurt Knochner ♦</div></div><span id="13081"></span><div id="comment-13081" class="comment"><div id="post-13081-score" class="comment-score"></div><div class="comment-text"><p>And I think what would make it really nice would be not only having the ability to download the capture files, but if there was a way to search for capture files containing specific protocols (or possibly other search criteria?), and have only those capture files of interest displayed ... basically similar to <a href="http://pcapr.net"></a><a href="http://pcapr.net">pcapr.net</a>.</p><p>Well, since this isn't a discussion forum, maybe we should move this to wireshark-dev?</p></div><div id="comment-13081-info" class="comment-info"><span class="comment-age">(27 Jul '12, 07:01)</span> cmaynard ♦♦</div></div><span id="13082"></span><div id="comment-13082" class="comment not_top_scorer"><div id="post-13082-score" class="comment-score"></div><div class="comment-text"><blockquote><p>maybe we should move this to wireshark-dev</p></blockquote><p>good idea.</p></div><div id="comment-13082-info" class="comment-info"><span class="comment-age">(27 Jul '12, 09:01)</span> Kurt Knochner ♦</div></div><span id="13099"></span><div id="comment-13099" class="comment not_top_scorer"><div id="post-13099-score" class="comment-score"></div><div class="comment-text"><p>Well, I tried using gmane to post to wireshark-dev, but for some reason, the post never showed up. This is an annoying thing w/gmane that seems to happen quite a lot, but I still prefer to use gmane instead of my company e-mail, since my company always sticks their annoying confidentiality disclaimer at the end of my e-mail, which I (and many others) despise. Anyway, feel free to try posting something if you want to see if Wireshark capture files can be made available for download ... and be protocol-searchable as well.</p></div><div id="comment-13099-info" class="comment-info"><span class="comment-age">(29 Jul '12, 07:33)</span> cmaynard ♦♦</div></div><span id="13147"></span><div id="comment-13147" class="comment not_top_scorer"><div id="post-13147-score" class="comment-score"></div><div class="comment-text"><p>We'd be interested in providing a CloudShark system to the Wireshark dev team. This would give you lots of control over your capture files and allow a capture to be public or require authentication. There are several models that could be deployed. Captures can be organized and searched using the tagging system. If anyone wants to take the lead on this, I'd be happy to talk with you and explore this possibility. You can contact us at <a href="http://appliance.cloudshark.org/contact.html">http://appliance.cloudshark.org/contact.html</a></p></div><div id="comment-13147-info" class="comment-info"><span class="comment-age">(30 Jul '12, 17:52)</span> joemc</div></div><span id="13168"></span><div id="comment-13168" class="comment not_top_scorer"><div id="post-13168-score" class="comment-score"></div><div class="comment-text"><p>Thank you for this offer! Can you please post it on the <a href="http://www.wireshark.org/lists/">wireshark-dev list</a>?</p></div><div id="comment-13168-info" class="comment-info"><span class="comment-age">(31 Jul '12, 00:29)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-13029" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-13029-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25314"></span>

<div id="answer-container-25314" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25314-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The problem with the above methods is that it blindly strips a number of bytes off the packet while the pcap file may also contain other content than GTP-User.</p><p>I use the following python script (which is not perfect as I'm in no way a developer). It does the job fairly quickly even on large files and has proven to be a great tool.</p><pre><code>#!/usr/bin/env python
&#39;&#39;&#39;Remove GTP layer from PCAP file&#39;&#39;&#39;
import dpkt, struct, time, re, socket
import platform
import sys

# Check for arguments
if len(sys.argv) &lt; 3 or len(sys.argv) &gt; 3:
    print &quot;Usage:\n&quot;, sys.argv[0], &quot;input.pcap&quot;, &quot;output.pcap&quot;
    sys.exit()

# Open files for input and output
try:
    fi = open(sys.argv[1],&#39;r&#39;)
    fo = open(sys.argv[2],&#39;w&#39;)

    # Prepare PCAP reader and writter
    pcapin = dpkt.pcap.Reader(fi)
    pcapout = dpkt.pcap.Writer(fo)

    for ts, buf in pcapin:
        # make sure we are dealing with IP traffic
        # ref: http://www.iana.org/assignments/ethernet-numbers
        try: eth = dpkt.ethernet.Ethernet(buf)
        except: continue
        if eth.type != 2048: continue

        # make sure we are dealing with UDP
        # ref: http://www.iana.org/assignments/protocol-numbers/
        try: ip = eth.data
        except: continue
        if ip.p != 17: continue

        # filter on UDP assigned ports for GTP User
        # ref: http://www.iana.org/assignments/port-numbers
        try: udp = ip.data
        except: continue
        try:
            if udp.dport != 2152: continue
        except: continue

        # extract GTP flags to detect header length
        gtpflags = udp.data[:1]
        try:
            if gtpflags == &#39;\x30&#39;: payload = udp.data[8:]
            elif gtpflags == &#39;\x32&#39;: payload = udp.data[12:]
            else: continue
        except: continue

        # at this point we have a confirmed ETH/IP/UDP/GTP packet structure
        # UDP payload is GTP header + real user payload
        try:
            # append real user payload to ethernet layer and writeout
            eth.data = payload
            pcapout.writepkt(eth, ts)
        except: continue

    fi.close()
    fo.close()

except IOError as (errno, strerror):
    print &quot;I/O error({0}): {1}&quot;.format(errno, strerror)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Sep '13, 06:22</strong></p><img src="https://secure.gravatar.com/avatar/266ce8d554380aab282c11e3cb821a28?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kiloohm&#39;s gravatar image" /><p>Kiloohm<br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kiloohm has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-25314" class="comments-container"><span id="25319"></span><div id="comment-25319" class="comment"><div id="post-25319-score" class="comment-score"></div><div class="comment-text"><p>Thanks for providing another option. I think <a href="http://www.tracewrangler.com/">tracewrangler</a> might be the best overall solution though.</p></div><div id="comment-25319-info" class="comment-info"><span class="comment-age">(27 Sep '13, 08:42)</span> cmaynard ♦♦</div></div><span id="25320"></span><div id="comment-25320" class="comment"><div id="post-25320-score" class="comment-score"></div><div class="comment-text"><p>If this is desired functionality open a bug requesting the feature, it should be easy to implement as part of "Export PDUs". Preferably also attach a sample file to test with.</p></div><div id="comment-25320-info" class="comment-info"><span class="comment-age">(27 Sep '13, 09:02)</span> Anders ♦</div></div><span id="25321"></span><div id="comment-25321" class="comment"><div id="post-25321-score" class="comment-score"></div><div class="comment-text"><p>I just tried tracewrangler on one of my files and it resulted in an access violation error. Perhaps the file is too large (750 Mbytes).</p><p>As for adding it as a feature in Wireshark, it could be great but it would likely be needed as well through command line to be able to parse large files.</p></div><div id="comment-25321-info" class="comment-info"><span class="comment-age">(27 Sep '13, 09:09)</span> Kiloohm</div></div><span id="25324"></span><div id="comment-25324" class="comment"><div id="post-25324-score" class="comment-score"></div><div class="comment-text"><p>The file size limit for TraceWrangler is 2GB at the moment, so 750MBytes should not be a problem. I don't have any files that size with GTP headers, so I can't really reproduce the issue, but I'll see what I can do.</p></div><div id="comment-25324-info" class="comment-info"><span class="comment-age">(27 Sep '13, 12:09)</span> Jasper ♦♦</div></div><span id="25671"></span><div id="comment-25671" class="comment"><div id="post-25671-score" class="comment-score"></div><div class="comment-text"><p>I just uploaded a new TraceWrangler build that has a couple of fixes regardings memory leaks, some especially for Edit tasks. I tried with a 900 MB file and it worked fine (while it crashed before due to mem problems), but since I don't know what frames you had in your file it might still run into trouble.</p></div><div id="comment-25671-info" class="comment-info"><span class="comment-age">(05 Oct '13, 16:53)</span> Jasper ♦♦</div></div><span id="30043"></span><div id="comment-30043" class="comment not_top_scorer"><div id="post-30043-score" class="comment-score"></div><div class="comment-text"><p>Hi Kiloohm,</p><p>I've used your script successfully but it also removes the dot1.q vlan tag ... can you help ? tks</p><p>P</p></div><div id="comment-30043-info" class="comment-info"><span class="comment-age">(20 Feb '14, 06:14)</span> Trigas</div></div></div><div id="comment-tools-25314" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-25314-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13017"></span>

<div id="answer-container-13017" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13017-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hey!!</p><p>This can be done using perl. Let me know if you still required this. I may have some scripts to achieve the same.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '12, 05:34</strong></p><img src="https://secure.gravatar.com/avatar/6b9ae8a749ec26d7d2cbb3507068861f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vineeth&#39;s gravatar image" /><p>Vineeth<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vineeth has no accepted answers">0%</span></p></div></div><div id="comments-container-13017" class="comments-container"></div><div id="comment-tools-13017" class="comment-tools"></div><div class="clear"></div><div id="comment-13017-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22698"></span>

<div id="answer-container-22698" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22698-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Not to resurrect a dead thread, but I noticed this one in a search and I think I have a better answer than the bittwiste example, since it keeps the top IP header when the desire is to create a raw IP capture starting with the inside IP header.</p><p>To do that, export the trace into a hex dump form (via Wireshark or Tshark), and execute this. This script assumes no IP options fields are present in the top IP header (would be a very unusual case), and it expects the input file in the same directory called hex_input as it's written there. It also is assuming that you've got an Ethernet header to start with, and GTPv1, but the number of bytes to subtract is controlled by the one line 'substr($packet,0,84)= "" ' so it's easily modified to do what you want. I quickly made it a bit generic but in my normal version of this I have it set to use perl's system commands, first to have tshark read the GTP-encapsulated capture file to get the hex printout, then at the end here I call text2pcap to rewrite the new capture file. Since the script starts by building a packet array out of text and follows by rebuilding it, it's actually a very useful script to tinker with, to quickly modify a few packet bits while they're nicely stored in an array.</p><p>Simply put, this script will take a hex dump file, puts it into an array, cut X number bytes, and rebuild a new hex dump file. It's written below to pull the internal IP packets out of GTP-U, and from there you can easily call the text2pcap utility to build it into a .pcap file as the script's output conforms to the expected text2pcap input format.</p><pre><code>#!/usr/bin/perl

# Used to build an array of packets out of a hex dump and reassemble
# them into a new hex dump. Allows for easy manipulation of packets
# in hex while cleanly stored into an array prior to reconstruction.
# In this case, we&#39;re stripping 42 bytes to account for Ethernet, IP and GTP headers.
# Written by Russell DeLong ([email protected]).

use strict;

# Declarations
my $input_file = &quot;hex_input&quot;;
my $n;
my @line;
my $line_count;
my @packets;
my $packet;
my $packet_length;
my $offset;
my $lead_zeros;
my $bytes;

# Take capture file input.
open (INPUT, $input_file) or die &quot;couldn&#39;t open $input_file\n&quot;;

# Build a packet array.
while (&lt;INPUT&gt;){
        @line = split(&#39;  &#39;, $_);
        if (@line[0] =~ m/0000/) {
            $n = $n + 1;
        }
        @packets[$n] = @packets[$n] . @line[1];
        @packets[$n] =~ s/ //g;
}

# Rebuild the text file from @packets array.
foreach (@packets) {
        $packet = $_;
        substr($packet,0,84)= &quot;&quot;; # Strip&#39;s 42 bytes from the top of the packet.
        $packet_length = $_ =~ tr/[0-9a-zA-Z]//;
        # The +0.999... is a cheap way to round up for the last line.
        $line_count = int(($packet_length/32) + 0.9999999999);
        for ($n=0; $n &lt; $line_count; $n++){
            $offset = sprintf(&quot;%x&quot;,($n*16));
            # Assumes no offset greater than 4 hex characters.
            $lead_zeros = 4 - ($offset =~ tr/[0-9a-zA-Z]//);
            $lead_zeros = &#39;0&#39; x $lead_zeros;
            $bytes = substr($packet,$n*32,32);
            # Adds a space character after every byte.
            $bytes =~ s/([0-9a-zA-Z]{2})/$1 /g;
            print &quot;$lead_zeros$offset  $bytes\n&quot;;
        }
}</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '13, 15:29</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Jul '13, 16:27</p></div></div><div id="comments-container-22698" class="comments-container"><span id="22700"></span><div id="comment-22700" class="comment"><div id="post-22700-score" class="comment-score"></div><div class="comment-text"><p>The new export PDU functionality in trunk could be expanded to export the GTP payload.</p></div><div id="comment-22700-info" class="comment-info"><span class="comment-age">(07 Jul '13, 04:29)</span> Anders ♦</div></div></div><div id="comment-tools-22698" class="comment-tools"></div><div class="clear"></div><div id="comment-22698-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

