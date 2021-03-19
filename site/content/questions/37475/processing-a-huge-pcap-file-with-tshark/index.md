+++
type = "question"
title = "Processing a huge .pcap file with tshark"
description = '''I am trying to process a huge .pcap file. I&#x27;m talking about a more than 50GB file. I also have a separated file with the following flow&#x27;s parameter for each flow: the start time (epoch time), end time (epoch time), and socket information (IP source, IP destination, port source, port destination and ...'''
date = "2014-10-30T14:32:00Z"
lastmod = "2014-11-02T08:57:00Z"
weight = 37475
keywords = [ "tshark", "scripting" ]
aliases = [ "/questions/37475" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Processing a huge .pcap file with tshark](/questions/37475/processing-a-huge-pcap-file-with-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37475-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37475-score" class="post-score" title="current number of votes">0</div><span id="post-37475-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to process a huge .pcap file. I'm talking about a more than 50GB file. I also have a separated file with the following flow's parameter for each flow: the start time (epoch time), end time (epoch time), and socket information (IP source, IP destination, port source, port destination and transport protocol. I want to extract each packet of each flow and write a .csv file different for each flow with the information of every packet of that flow. The flows in the file are either TCP or UDP.</p><p>I've written a bash script that starts by splitting the file in a 100MB files in order to be able to process it. Then I read the first packet epoch time and the last packet epoch time of each 100Mb file and I write them down to a file. After that, I read start reading each line of the separated file and compare the start times and end times of each flow with the first packet time and last packet time of each 100Mb file. Doing so I know which files I have to process to gather all the packets of a flow. After that I apply a filter with tshark and save the parameters I need on a separated file. As I said, I create a different file for each flow</p><p>This process take a lot of time. How can I speed up this process? I've been thinking about the following possibilities:</p><p>1) Use 10Mb files instead of 100Mb files. Could that improve the speed? Is there and known size that yields good performance when processing a huge file?</p><p>2) Once I've read with tshark a flow is it possible to delete that flow from the pcap file? Is it possible to generate a separated .pcap file with only that flow and delete it from the original file? Doing that I will only read a flow once. Looks like that tshark filters the packets comparing the desired information with all the packets in the .pcap file and that slows down the performance a lot</p><p>Thanks</p><p>Edit:</p><p>I read the start time (epoch), end time (epoch) IP source, IP destination Port source Port destination and Transport protocol form my separate file. The using the time information I check which .pcap 100Mb I should use for this flow. (If you split a large file some flows may start in one file and end in another one). Then I run the following lines with tshark.</p><p>For TCP</p><pre><code>tshark -r pkt.pcap$i -n -Y &quot;frame.time_epoch &gt;= $start_time &amp;&amp; frame.time_epoch &lt;= $end_time &amp;&amp; ip.src==$local_ip &amp;&amp; ip.dst==$remote_ip &amp;&amp; tcp.srcport == $local_port &amp;&amp; tcp.dstport ==$remote_port&quot; -T fields -E separator=, -e frame.time_epoch -e frame.cap_len -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport &gt;&gt; temp1.csv

tshark -r pkt.pcap$i -n -Y &quot;frame.time_epoch &gt;= $start_time &amp;&amp; frame.time_epoch &lt;= $end_time &amp;&amp; ip.dst==$local_ip &amp;&amp; ip.src==$remote_ip &amp;&amp; tcp.dstport == $local_port &amp;&amp; tcp.srcport ==$remote_port&quot; -T fields -E separator=, -e frame.time_epoch -e frame.cap_len -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport &gt;&gt; temp1.csv</code></pre><p>For udp is the same changing tcp.srcport and so on for udp.src and so on</p><p>Then I add the transport protocol to the csv file</p><pre><code>add=&quot;$transport_protocol&quot;
awk -v d=&quot;$add&quot; -F&quot;,&quot; &#39;BEGIN { OFS = &quot;,&quot; } {$7=d; print}&#39; temp1.csv &gt; flow$flow.csv</code></pre><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-scripting" rel="tag" title="see questions tagged &#39;scripting&#39;">scripting</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Oct '14, 14:32</strong></p><img src="https://secure.gravatar.com/avatar/aa83aec4e912a89f254d24456c7d5b11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Xavi1618&#39;s gravatar image" /><p><span>Xavi1618</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Xavi1618 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Oct '14, 15:01</strong> </span></p></div></div><div id="comments-container-37475" class="comments-container"></div><div id="comment-tools-37475" class="comment-tools"></div><div class="clear"></div><div id="comment-37475-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="37477"></span>

<div id="answer-container-37477" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37477-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37477-score" class="post-score" title="current number of votes">1</div><span id="post-37477-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Whats included in "the information of every packet of that flow" ?</p><p>Does it involve and dissection of the TCP/UDP payloads ? Is this a one-time project or something which is to be used repeatedly ?</p><p>In any case, a couple of thoughts:</p><ol><li>Disable all protocols except ethernet/ip/tcp/udp/etc. That might speed up tshark processing significantly. There's a tremendous amount of work being done by tshark to dissect all the layers of each frame.</li><li>Or: maybe write what I expect might not be too large a program to read the pcap file directly and do minimal dissection to get the info you need. It's been quite a while since I've done this sort of thing, but I expect there are libraries to read pcap files &amp; etc.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Oct '14, 14:53</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-37477" class="comments-container"><span id="37479"></span><div id="comment-37479" class="comment"><div id="post-37479-score" class="comment-score"></div><div class="comment-text"><p>How can I disable the other protocols?</p></div><div id="comment-37479-info" class="comment-info"><span class="comment-age">(30 Oct '14, 15:00)</span> <span class="comment-user userinfo">Xavi1618</span></div></div><span id="37481"></span><div id="comment-37481" class="comment"><div id="post-37481-score" class="comment-score"></div><div class="comment-text"><p>See:</p><p><a href="https://ask.wireshark.org/questions/9544/how-to-disable-dissectors-in-tshark">https://ask.wireshark.org/questions/9544/how-to-disable-dissectors-in-tshark</a></p><p>Essentially:</p><p>Using wireshark:</p><ul><li>Create a new profile in Wireshark;</li><li>Disable all protocols and then re-enable as desired.</li><li>(Open a capture file &amp; verify that protocokls needed are enabled).</li></ul><p>Then: specify profile created above to tshark using -C option.</p></div><div id="comment-37481-info" class="comment-info"><span class="comment-age">(30 Oct '14, 16:00)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="37512"></span><div id="comment-37512" class="comment"><div id="post-37512-score" class="comment-score"></div><div class="comment-text"><p>Thanks, It helps but not that much. It improves the processing time, but no significantly. 5-10% improvement</p></div><div id="comment-37512-info" class="comment-info"><span class="comment-age">(31 Oct '14, 14:02)</span> <span class="comment-user userinfo">Xavi1618</span></div></div></div><div id="comment-tools-37477" class="comment-tools"></div><div class="clear"></div><div id="comment-37477-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="37476"></span>

<div id="answer-container-37476" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37476-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37476-score" class="post-score" title="current number of votes">0</div><span id="post-37476-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>1) the file size will not improve speeds as it is your processing that is the problem, not the file size</p><p>2) you can't remove flows from pcap files, except if you parse it again and leave out all packets matching a certain filter - but that's going to make things slower, not faster.</p><p>By the way, what exactly are you trying to get as a result? CSV, yes, but how many files and what should they contain? Maybe there is an easier way to achieve what you need, e.g. by using tools like <a href="http://www.icir.org/mallman/software/tcpsplit/">tcpsplit</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Oct '14, 14:49</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-37476" class="comments-container"><span id="37478"></span><div id="comment-37478" class="comment"><div id="post-37478-score" class="comment-score"></div><div class="comment-text"><p>edited, helps?</p></div><div id="comment-37478-info" class="comment-info"><span class="comment-age">(30 Oct '14, 15:00)</span> <span class="comment-user userinfo">Xavi1618</span></div></div><span id="37513"></span><div id="comment-37513" class="comment"><div id="post-37513-score" class="comment-score"></div><div class="comment-text"><p>Helps a lot processing smaller files. With 1Mb-5Mb the improvement is considerably. Just tried out. However the time it takes tcpdump command to split the archive is considerable</p></div><div id="comment-37513-info" class="comment-info"><span class="comment-age">(31 Oct '14, 14:04)</span> <span class="comment-user userinfo">Xavi1618</span></div></div></div><div id="comment-tools-37476" class="comment-tools"></div><div class="clear"></div><div id="comment-37476-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="37494"></span>

<div id="answer-container-37494" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37494-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37494-score" class="post-score" title="current number of votes">0</div><span id="post-37494-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>tshark -r pkt.pcap$i -n -Y "frame.time_epoch &gt;= $start_time &amp;&amp; frame.time_epoch &lt;= $end_time &amp;&amp; ip.src==$local_ip &amp;&amp; ip.dst==$remote_ip &amp;&amp; tcp.srcport == <strong>$local_port</strong> &amp;&amp; tcp.dstport == <strong>$remote_port</strong>" -T fields -E separator=, -e frame.time_epoch -e frame.cap_len -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport &gt;&gt; temp1.csv</p></blockquote><p>Hm... why are you using tshark at all? All you do is to write the IP addresses, the ports and the time stamps into a capture file, but you already <strong>know the IP addresses and the ports</strong> as you have them in variables ($local_port, $remote_port, etc.). All you actually <strong>extract</strong> from the capture file are the time stamps and the frame len.</p><p>Maybe I'm missing something, but your whole process to extract data seems to have another "loop" somewhere to get the IP addresses and ports and maybe that additional step creates the extra processing time. Can you please describe in more details what you are doing right now and what you want to achieve?</p><p><strong>++ UPDATE ++</strong></p><p>O.K. in your case you won't need the whole <strong>dissection capabilities</strong> of wireshark/tshark. A simple perl script, that reads the pcap file and extracts the same information would be way faster.</p><p>Sample script:</p><pre><code>use strict;
use warnings;

use Net::Pcap;
use NetPacket::Ethernet qw(:types);
use NetPacket::IP qw(:protos);
use NetPacket::TCP;
use NetPacket::UDP;

my $pcap_file = $ARGV[0];

if (not $pcap_file) { 
    die(&quot;ERROR: please give pcap file name on the cli\n&quot;)
};

my $err = undef;

# read data from pcap file.
my $pcap = pcap_open_offline($pcap_file, \$err) or die &quot;Can&#39;t read $pcap_file : $err\n&quot;;
pcap_loop($pcap, -1, \&amp;process_packet, &quot;just for the demo&quot;);

# close the device
pcap_close($pcap);

my $ethernet;
my $ip;
my $payload;

sub process_packet {
    my ($user_data, $header, $packet) = @_;

    my $cap_len = $header-&gt;{caplen};
    my $frame_len = $header-&gt;{len};
    my $time_epoch = $header-&gt;{tv_sec} . &quot;.&quot; . $header-&gt;{tv_usec};

    $ethernet = NetPacket::Ethernet-&gt;decode($packet);

    if ($ethernet-&gt;{type} != ETH_TYPE_IP) {
        return;
    }

    $ip = NetPacket::IP -&gt; decode($ethernet-&gt;{data});

    my $src_ip = $ip-&gt;{src_ip};
    my $dst_ip = $ip-&gt;{dest_ip};

    if ($ip-&gt;{proto} == IP_PROTO_TCP) {
        $payload = NetPacket::TCP-&gt;decode($ip-&gt;{data});
    } elsif ($ip-&gt;{proto} == IP_PROTO_UDP) {
        $payload = NetPacket::UDP-&gt;decode($ip-&gt;{data});
    } else {
        return;
    }

    my $src_port = $payload-&gt;{src_port};
    my $dst_port = $payload-&gt;{dest_port};

    #print &quot;$time_epoch;$cap_len;$frame_len;$src_ip;$dst_ip;$src_port;$dst_port\n&quot;;#
    print &quot;$time_epoch,$cap_len,$src_ip,$dst_ip,$src_port,$dst_port\n&quot;;
}</code></pre><p><strong>Test</strong></p><p>I tested the script and tshark against the same file (90 MByte, several http/https downloads):</p><p>tshark: ~20 seconds<br />
script: ~4 seconds</p><p>BTW: If you need the output only for one direction (as implied by your tshark filter), you can either post process the output file or change the perl script to use filters.</p><blockquote><p><a href="http://search.cpan.org/dist/Net-Pcap/Pcap.pm">http://search.cpan.org/dist/Net-Pcap/Pcap.pm</a></p></blockquote><p>BTW: Net::Pcap only supports libpcap files. So, if your capture file is pcap-ng, you'll have to convert if first with editcap, which takes only a few seconds on a fast system.</p><blockquote><p>editcap -F pcap input.pcapng output.pcap</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Oct '14, 01:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Nov '14, 10:14</strong> </span></p></div></div><div id="comments-container-37494" class="comments-container"><span id="37514"></span><div id="comment-37514" class="comment"><div id="post-37514-score" class="comment-score"></div><div class="comment-text"><p>I have the information of the flow in a separated file. I want to know what the parameters about every packet of a flow as its direction, bytes and frame time</p></div><div id="comment-37514-info" class="comment-info"><span class="comment-age">(31 Oct '14, 14:05)</span> <span class="comment-user userinfo">Xavi1618</span></div></div><span id="37542"></span><div id="comment-37542" class="comment"><div id="post-37542-score" class="comment-score"></div><div class="comment-text"><p>see the <strong>UPDATE</strong> in my answer.</p></div><div id="comment-37542-info" class="comment-info"><span class="comment-age">(02 Nov '14, 08:57)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-37494" class="comment-tools"></div><div class="clear"></div><div id="comment-37494-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

