+++
type = "question"
title = "show ICMP RTTs"
description = '''I have a packet trace consisting solely of ICMP echo requests (probes) with a low ttl and corresponding ICMP time-exceeded messages (replies).  Is there a way for Wireshark to show the round-trip time (RTT) for each probe packet that I sent?'''
date = "2013-12-11T09:08:00Z"
lastmod = "2013-12-11T13:00:00Z"
weight = 28007
keywords = [ "rtt", "icmp" ]
aliases = [ "/questions/28007" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [show ICMP RTTs](/questions/28007/show-icmp-rtts)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28007-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a packet trace consisting solely of ICMP echo requests (probes) with a low ttl and corresponding ICMP time-exceeded messages (replies).</p><p>Is there a way for Wireshark to show the round-trip time (RTT) for each probe packet that I sent?</p></div><div id="question-tags" class="tags-container tags">rtt icmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Dec '13, 09:08</strong></p><img src="https://secure.gravatar.com/avatar/37d5ac39226e28baf623ed0794a82daf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rick_r&#39;s gravatar image" /><p>rick_r<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rick_r has no accepted answers">0%</span></p></div></div><div id="comments-container-28007" class="comments-container"></div><div id="comment-tools-28007" class="comment-tools"></div><div class="clear"></div><div id="comment-28007-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="28020"></span>

<div id="answer-container-28020" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28020-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p><strong>Option #1:</strong></p><p>Take a look at the following output of tshark</p><blockquote><p>[email protected]:/tmp$ tshark -nr icmp.pcap -T fields -e frame.number -e frame.time_relative -e ip.src -e ip.dst -e icmp.type -e icmp.code -e icmp.ident -e icmp.seq -E separator=\; -E header=y</p></blockquote><p>Output (copy to editor to remove possible wrap-around):</p><pre><code>frame.number;frame.time_relative;ip.src;ip.dst;icmp.type;icmp.code;icmp.ident;icmp.seq
10;8.271326000;192.168.158.186;80.190.158.9;8;0;25976,30821;1
11;8.271483000;192.168.158.2,192.168.158.186;192.168.158.186,80.190.158.9;11,8;0,0;25976,30821;1
35;13.305895000;192.168.158.186;80.190.158.9;8;0;25976,30821;2
36;13.306017000;192.168.158.2,192.168.158.186;192.168.158.186,80.190.158.9;11,8;0,0;25976,30821;2
45;18.338883000;192.168.158.186;80.190.158.9;8;0;25976,30821;3
46;18.339073000;192.168.158.2,192.168.158.186;192.168.158.186,80.190.158.9;11,8;0,0;25976,30821;3
52;19.553171000;192.168.158.186;80.190.158.9;8;0;25977,31077;1
53;19.553253000;192.168.158.2,192.168.158.186;192.168.158.186,80.190.158.9;11,8;0,0;25977,31077;1
66;24.581539000;192.168.158.186;80.190.158.9;8;0;25977,31077;2
67;24.581686000;192.168.158.2,192.168.158.186;192.168.158.186,80.190.158.9;11,8;0,0;25977,31077;2
72;27.909485000;192.168.158.186;80.190.158.9;8;0;25978,31333;1
73;27.909622000;192.168.158.2,192.168.158.186;192.168.158.186,80.190.158.9;11,8;0,0;25978,31333;1
81;32.932901000;192.168.158.186;80.190.158.9;8;0;25978,31333;2
82;32.933046000;192.168.158.2,192.168.158.186;192.168.158.186,80.190.158.9;11,8;0,0;25978,31333;2
101;37.959543000;192.168.158.186;80.190.158.9;8;0;25978,31333;3
102;37.959667000;192.168.158.2,192.168.158.186;192.168.158.186,80.190.158.9;11,8;0,0;25978,31333;3</code></pre><p>Wireshark (tshark) will also dissect the ICMP ECHO Request header within ICMP Time Exceeded. Frame #10 is the ECHO Request. Frame #11 is the TIME Exeeded for that ECHO Request. As you can see, you will find the necessary information in the output (IP Adresses, ICMP Identifier and Sequence number) to match those two frames. Then take the time stamp of both (here frame.time_relative) to calculate the RTT. Of course you will need some script (Perl, Python or whatever you speak fluently) to extract and calculate that. However, there is no way to do the same in Wireshark (without programming, e.g. a Lua Listener), especially if you have bursts of requests and replies.</p><p><strong>Option #2:</strong></p><p>Another option would be to use the field <strong><a href="http://www.wireshark.org/docs/dfref/i/icmp.html">icmp.data_time</a></strong> of the ICMP Time Exceeded frames in conjunction with the time stamp of the Time Exceed frame itself. The delta should be equal to the RTT. However, on my test system that did not work, as I had a strange offset, which might be caused by VMware. However, you can still try it in your environment and see what happens.</p><blockquote><p>[email protected]:/tmp$ tshark -nr icmp.pcap -Y 'icmp.type eq 11 and icmp.code eq 0' -T fields -e frame.number -e frame.time -e ip.src -e ip.dst -e icmp.data_time -E separator=\; -E header=y</p></blockquote><p>Output (copy to editor to remove possible wrap-around):</p><pre><code>frame.number;frame.time;ip.src;ip.dst;icmp.data_time
11;Dec 11, 2013 21:28:00.039026000;192.168.158.2,192.168.158.186;192.168.158.186,80.190.158.9;Dec 11, 2013 21:28:00.000000000
36;Dec 11, 2013 21:28:05.073560000;192.168.158.2,192.168.158.186;192.168.158.186,80.190.158.9;Dec 11, 2013 21:28:05.000000000
46;Dec 11, 2013 21:28:10.106616000;192.168.158.2,192.168.158.186;192.168.158.186,80.190.158.9;Dec 11, 2013 21:28:10.000000000
53;Dec 11, 2013 21:28:11.320796000;192.168.158.2,192.168.158.186;192.168.158.186,80.190.158.9;Dec 11, 2013 21:28:11.000000000
67;Dec 11, 2013 21:28:16.349229000;192.168.158.2,192.168.158.186;192.168.158.186,80.190.158.9;Dec 11, 2013 21:28:16.000000000
73;Dec 11, 2013 21:28:19.677165000;192.168.158.2,192.168.158.186;192.168.158.186,80.190.158.9;Dec 11, 2013 21:28:19.000000000
82;Dec 11, 2013 21:28:24.700589000;192.168.158.2,192.168.158.186;192.168.158.186,80.190.158.9;Dec 11, 2013 21:28:24.000000000
102;Dec 11, 2013 21:28:29.727210000;192.168.158.2,192.168.158.186;192.168.158.186,80.190.158.9;Dec 11, 2013 21:28:29.000000000</code></pre><p>Then take the two time stamps to calculate the difference, which is again the RTT. <strong>HOWEVER</strong>: As you can see the data time stamp is allway xx:xx:xx.<strong>0000000</strong>, which is simply wrong. I'm not yet sure if that's a Wireshark bug or a problem with VMware and time stamping the frames. If you see the same problem on your system, please use method #1.</p><p><strong>Option #3:</strong></p><p>Finally, there is <strong><a href="http://www.wireshark.org/docs/dfref/i/icmp.html">icmp.data_time_relative</a></strong>, which is, according to the definition of that field: <code>The timestamp of the packet, relative to the timestamp in the first 8 bytes of the icmp data</code>. So, that's actually the RTT of the ECHO request (data part of time exceeded) and the ICMP time exceeded frame. <strong>However</strong>: That did also not work on my system. Same problem as mentioned above. Anyway, you can try this as well. Maybe it works in your environment. You can even apply that field as a column in Wireshark. Find the field in the ICMP time exceeded frame, then right click it and choose "Apply as column".</p><p><strong>-- UPDATE --</strong></p><p>I think I need to be more specific on Option #2 and #3, as that's only going to work if you use ping (ECHO request) on a Linux system.</p><p><a href="http://manpages.ubuntu.com/manpages/hardy/man8/ping.8.html">man page of ping</a>:</p><pre><code>ICMP PACKET DETAILS

     .....

     If the data space is at least eight bytes large, ping uses the first
     eight bytes of this space to include a timestamp which it uses in the
     computation of round trip times. If less than eight bytes of pad are
     specified, no round trip times are given.
</code></pre><p>As you can see, the Linux ping command (at least on Ubuntu) will add a timestamp to the ICMP ECHO request, if there is 'enough space'. That timestamp will be 'detected' by Wireshark (dissected as fields <code>icmp.data_time</code> and <code>icmp.data_time_relative</code>). So, you can use those fields to 'calcuate' the RTT.</p><p>You say: <code>There is no timestamp inside an ICMP time-exceeded packet.</code><br />
</p><p>You are right. But, <strong>there is</strong> a timestamp in the ECHO request, <strong>if you are using ping on Linux</strong> (as I did). As every ICMP 'error frame' (I don't know a better name for that), includes the first few bytes of the packet that caused the ICMP 'error frame' (mainly the IP + TCP/UDP header), the ICMP time exceeded contains the header of the ICMP ECHO request, including the timestamp in it. See the following capture file:</p><p>ICMP on Linux:</p><blockquote><p><a href="http://cloudshark.org/captures/8676c0c2afad">http://cloudshark.org/captures/8676c0c2afad</a></p></blockquote><p>See frame #1 (ECHO request): Open 'Internet Control Message Protocol' and you'll see the timestamp.</p><p>See frame #2 (TIME exceeded): Open 'Internet Control Message Protocol' and then 'Internet Control Message Protocol' again and you'll see the <strong>timestamp</strong> of the <strong>ECHO request</strong> (original packet that caused the time exceeded).</p><p><strong>However</strong> that method (Options #2 and #3) has two problems:</p><ul><li>the timestamp on Linux seems to be slightly false. There is an offset between the timestamp in the ICMP ECHO data payload and the timestamp of the ECHO frame itself. That could be due to VMware or a general problem with the ping command on Linux/Ubuntu. I have no interest to analyze that ;-)</li><li>If you are using <strong>Windows</strong> to send ECHO requests, the method <strong>does not work at all</strong>, as the Windows ping command does not add a timestamp to the ECHO request.</li></ul><p>ICMP on Windows:</p><blockquote><p><a href="http://cloudshark.org/captures/e5a55c87d6fd">http://cloudshark.org/captures/e5a55c87d6fd</a></p></blockquote><p>So, if you are using <strong>Linux</strong> to send the ICMP ECHO requests, <strong>you can use Option #2 and #3</strong> to calculate the RTT, which is simply this:</p><ul><li>timestamp of ICMP time exceeded - timestamp of ECHO request <strong>within</strong> the same frame</li></ul><p>If you are using <strong>Windows</strong> there is no timestamp within the ECHO request, so you can only use <strong>method #1</strong>. That's gonna work in both cases.</p><p><strong>-- UPDATE 2 --</strong></p><p>The following (simple) Perl script will calculate the RTT, according to the method described in Option #1.</p><p><strong>CLI:</strong></p><blockquote><p>tshark -nr icmp.pcap -Y icmp -T fields -e frame.number -e frame.time_relative -e ip.src -e ip.dst -e icmp.type -e icmp.code -e icmp.ident -e icmp.seq -E separator=';' | perl calculate_rtt.pl</p></blockquote><p><strong>Output:</strong></p><pre><code>RTT:8.1e-05:192.168.158.186:80.190.158.9:2:0.000081000:26494,32359:1
RTT:0.000121000000000038:192.168.158.186:80.190.158.9:4:5.011520000:26494,32359:2
RTT:0.000293999999998462:192.168.158.186:80.190.158.9:6:8.353810000:26497,33127:1
RTT:0.000146000000000868:192.168.158.186:80.190.158.9:8:13.397372000:26497,33127:2
RTT:6.70000000013715e-05:192.168.158.186:80.190.158.9:10:14.153415000:26501,34151:1
RTT:6.40000000018404e-05:192.168.158.186:80.190.158.9:12:16.978635000:26502,34407:1</code></pre><p>The format of the output is:</p><blockquote><p>RTT:{RTT time}:{src}:{dst}:{frame number}:{timestamp of time exceeded}:{ICMP Ident}:{ICMP Sequence}</p></blockquote><p><strong>Hint</strong>: The RTT values are pretty small in my example, as I used a TTL of 1 for the ECHO request and the first router on my network responded with a TIME EXCEEDED, which was within a few microseconds on a Gigabit network!</p><p><strong>Code:</strong></p><pre><code>#!/usr/bin/perl

use strict;
use warnings;

my %icmp_data;

while (&lt;STDIN&gt;) {

    my $line = $_;
    chomp($line);

    # ECHO request 
    if ($line =~ /;8;0/) {
        my ($frame_num, $time, $src, $dst, undef, undef, $ident, $seq) = (split(&#39;;&#39;, $line));

        my $key = &quot;$src + $dst + $ident + $seq&quot;;

    # If the same ECHO request is found, print a WARNING
        if (exists $icmp_data{$key}-&gt;{echo_request}) {
           print &quot;WARNING: Duplicate ICMP ECHO REQUEST found\n&quot;;
           print &quot;Old Entry: \n&quot;; 
           print &quot;    Frame: &quot; + $icmp_data{$key}-&gt;{echo_request}-&gt;{frame_num} + &quot;\n&quot;;
           print &quot;    Time : &quot; + $icmp_data{$key}-&gt;{echo_request}-&gt;{time} + &quot;\n&quot;;
           print &quot;    Src  : &quot; + $icmp_data{$key}-&gt;{echo_request}-&gt;{src} + &quot;\n&quot;;
           print &quot;    Dst  : &quot; + $icmp_data{$key}-&gt;{echo_request}-&gt;{dst} + &quot;\n&quot;;
           print &quot;    Ident: &quot; + $icmp_data{$key}-&gt;{echo_request}-&gt;{ident} + &quot;\n&quot;;
           print &quot;    Seq  : &quot; + $icmp_data{$key}-&gt;{echo_request}-&gt;{seq} + &quot;\n&quot;;

           print &quot;New Entry: \n&quot;; 
           print &quot;    Frame: &quot; + $frame_num + &quot;\n&quot;;
           print &quot;    Time : &quot; + $time + &quot;\n&quot;;
           print &quot;    Src  : &quot; + $src + &quot;\n&quot;;
           print &quot;    Dst  : &quot; + $dst + &quot;\n&quot;;
           print &quot;    Ident: &quot; + $ident + &quot;\n&quot;;
           print &quot;    Seq  : &quot; + $seq + &quot;\n&quot;;
       print &quot;\n&quot;;

        } else {

           $icmp_data{$key}-&gt;{echo_request}-&gt;{frame_num} = $frame_num;
           $icmp_data{$key}-&gt;{echo_request}-&gt;{time} = $time;
           $icmp_data{$key}-&gt;{echo_request}-&gt;{src} = $src;
           $icmp_data{$key}-&gt;{echo_request}-&gt;{dst} = $dst;
           $icmp_data{$key}-&gt;{echo_request}-&gt;{ident} = $ident;
           $icmp_data{$key}-&gt;{echo_request}-&gt;{seq} = $seq;
    }
    }

    # TIME EXCEEDED 
    if ($line =~ /;11,8;0,0/) {
        my ($frame_num, $time, undef, $src_dst, undef, undef, $ident, $seq) = (split(&#39;;&#39;, $line));
        my ($src, $dst) = (split(&#39;,&#39;, $src_dst));

        my $key = &quot;$src + $dst + $ident + $seq&quot;;

        $icmp_data{$key}-&gt;{time_exceeded}-&gt;{frame_num} = $frame_num;
        $icmp_data{$key}-&gt;{time_exceeded}-&gt;{time} = $time;
        $icmp_data{$key}-&gt;{time_exceeded}-&gt;{src} = $src;
        $icmp_data{$key}-&gt;{time_exceeded}-&gt;{dst} = $dst;
        $icmp_data{$key}-&gt;{time_exceeded}-&gt;{ident} = $ident;
        $icmp_data{$key}-&gt;{time_exceeded}-&gt;{seq} = $seq;

        if (exists $icmp_data{$key}-&gt;{echo_request}) {
            my $rtt = $icmp_data{$key}-&gt;{time_exceeded}-&gt;{time} - $icmp_data{$key}-&gt;{echo_request}-&gt;{time};

        print &quot;RTT:$rtt:$src:$dst:$frame_num:$time:$ident:$seq\n&quot;;
        }
    }
}

__END__

Sample Data, generated by:

tshark -nr icmp.pcap -Y icmp -T fields -e frame.number -e frame.time_relative -e ip.src -e ip.dst -e icmp.type -e icmp.code -e icmp.ident -e icmp.seq -E separator=&#39;;&#39;

10;8.271326000;192.168.158.186;80.190.158.9;8;0;25976,30821;1
11;8.271483000;192.168.158.2,192.168.158.186;192.168.158.186,80.190.158.9;11,8;0,0;25976,30821;1
35;13.305895000;192.168.158.186;80.190.158.9;8;0;25976,30821;2
36;13.306017000;192.168.158.2,192.168.158.186;192.168.158.186,80.190.158.9;11,8;0,0;25976,30821;2

Sample Output:

RTT:{RTT time}:{src}:{dst}:{frame number}:{timestamp of time exceeded}:{ICMP Ident}:{ICMP Sequence}

RTT:8.1e-05:192.168.158.186:80.190.158.9:2:0.000081000:26494,32359:1
RTT:0.000121000000000038:192.168.158.186:80.190.158.9:4:5.011520000:26494,32359:2
RTT:0.000293999999998462:192.168.158.186:80.190.158.9:6:8.353810000:26497,33127:1
RTT:0.000146000000000868:192.168.158.186:80.190.158.9:8:13.397372000:26497,33127:2
RTT:6.70000000013715e-05:192.168.158.186:80.190.158.9:10:14.153415000:26501,34151:1
RTT:6.40000000018404e-05:192.168.158.186:80.190.158.9:12:16.978635000:26502,34407:1</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Dec '13, 13:00</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Dec '13, 01:42</p></div></div><div id="comments-container-28020" class="comments-container"><span id="28022"></span><div id="comment-28022" class="comment"><div id="post-28022-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the detailed answer. I already have my own Python script that computes such RTTs, I just needed to doublecheck with wireshark some weird patterns that I observed. Since I am sending trains of probes, my packet trace doesn't look like: [probe_1, reply_1, ..., probe_n, reply_n], but more like: [probe_1, probe_2, ..., probe_k, reply_1, reply_2,... reply_k, probe_k+1, ..., reply_k+1,...]. Will this still work on wireshark? I don't understand what <code>icmp.data_time</code> means. There is no timestamp inside an ICMP time-exceeded packet. It is just the pcap timestamp, so wireshark should have to match a reply with a probe and only then compute the RTT. Is it capable of doing it? Or does it just compute the difference of timestamps between two consecutive packets in the trace?</p></div><div id="comment-28022-info" class="comment-info"><span class="comment-age">(11 Dec '13, 14:37)</span> rick_r</div></div><span id="28023"></span><div id="comment-28023" class="comment"><div id="post-28023-score" class="comment-score"></div><div class="comment-text"><p>If you are trying to measure the RTT between ICMP echo request and ICMP echo reply packets, then you could use <code>icmp.resptime</code>. That field won't be present in "Time to live exceeded" packets though.</p></div><div id="comment-28023-info" class="comment-info"><span class="comment-age">(11 Dec '13, 14:44)</span> cmaynard ♦♦</div></div><span id="28035"></span><div id="comment-28035" class="comment"><div id="post-28035-score" class="comment-score"></div><div class="comment-text"><p>see the <strong>UPDATE</strong> in my answer.</p></div><div id="comment-28035-info" class="comment-info"><span class="comment-age">(11 Dec '13, 23:43)</span> Kurt Knochner ♦</div></div><span id="28037"></span><div id="comment-28037" class="comment"><div id="post-28037-score" class="comment-score"></div><div class="comment-text"><p>Thank you again, Kurt. In my trace I didn't use ping. I sent my own ICMP echo request packets from a Linux box. Is there anything I can do for this trace of mine?</p></div><div id="comment-28037-info" class="comment-info"><span class="comment-age">(12 Dec '13, 01:05)</span> rick_r</div></div><span id="28039"></span><div id="comment-28039" class="comment not_top_scorer"><div id="post-28039-score" class="comment-score"></div><div class="comment-text"><p>see <strong>UPDATE 2</strong> in my answer</p></div><div id="comment-28039-info" class="comment-info"><span class="comment-age">(12 Dec '13, 01:17)</span> Kurt Knochner ♦</div></div><span id="28040"></span><div id="comment-28040" class="comment not_top_scorer"><div id="post-28040-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I sent my own ICMP echo request packets from a Linux box.</p></blockquote><p>can you post a small capture file somewhere (google drive, dropbox, cloudshark.org or mega.co.nz)?</p></div><div id="comment-28040-info" class="comment-info"><span class="comment-age">(12 Dec '13, 01:43)</span> Kurt Knochner ♦</div></div><span id="28041"></span><div id="comment-28041" class="comment not_top_scorer"><div id="post-28041-score" class="comment-score"></div><div class="comment-text"><p>You did a lot more than I could ever expect! I tried to run your script, but tshark says there is not such option as <code>-Y icmp</code>. There is <code>-y</code>, but it is <code>[ -y &lt;capture link type&gt; ]</code>. Which parameter did you think of here?</p></div><div id="comment-28041-info" class="comment-info"><span class="comment-age">(12 Dec '13, 01:53)</span> rick_r</div></div><span id="28042"></span><div id="comment-28042" class="comment not_top_scorer"><div id="post-28042-score" class="comment-score"></div><div class="comment-text"><p>There you go: <a href="http://cloudshark.org/captures/3f4157b48a06">http://cloudshark.org/captures/3f4157b48a06</a></p></div><div id="comment-28042-info" class="comment-info"><span class="comment-age">(12 Dec '13, 01:57)</span> rick_r</div></div><span id="28043"></span><div id="comment-28043" class="comment"><div id="post-28043-score" class="comment-score">1</div><div class="comment-text"><p>O.K. here is the sample output for your capture file. The RTT values seem to be correct (approved by manual comparison).</p><p>RTT:0.009429:193.1.13.12:138.96.116.134:12:0.009429000:0,0:0 RTT:0.008586:193.1.13.12:138.96.116.134:13:0.009479000:0,0:1 RTT:0.007735:193.1.13.12:138.96.116.134:14:0.009517000:0,0:2 RTT:0.006914:193.1.13.12:138.96.116.134:15:0.009559000:0,0:3 RTT:0.006067:193.1.13.12:138.96.116.134:16:0.009603000:0,0:4</p><blockquote><p>not such option as -Y icmp.</p></blockquote><p>Your tshark version is older than mine (1.10.2). You can try to use -R instead of -Y</p></div><div id="comment-28043-info" class="comment-info"><span class="comment-age">(12 Dec '13, 02:10)</span> Kurt Knochner ♦</div></div><span id="28054"></span><div id="comment-28054" class="comment not_top_scorer"><div id="post-28054-score" class="comment-score"></div><div class="comment-text"><p>I'm not really sure what you're trying to accomplish. If you want to know the RTT between 193.1.13.12 and the host replying with the TTL exceeded packet, why not just send an ICMP echo request packet from 193.1.13.12 to 193.1.244.121 and then use the <code>icmp.resptime</code> field?</p></div><div id="comment-28054-info" class="comment-info"><span class="comment-age">(12 Dec '13, 07:58)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-28020" class="comment-tools"><span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a></div><div class="clear"></div><div id="comment-28020-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28009"></span>

<div id="answer-container-28009" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28009-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you see time_exceeded messages then you did not reach your target. Or are you tracing traceroute traffic?<br />
If you want to see the RTT to each router sending the ICMP TTL exceeded simply look at the delta time of each inbound packet from the previous outbound packet.</p><p>Just did this and here is my results with filtering on inbound ICMP packets for a given ip_address and icmp.ident: <code>ip.dst == 173.194.34.69 and icmp.ident == 1 and ip.ttl gt 30</code> The frame.time__delta added as a column shows the RTT of each router on the path. <img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-tracert.ttl3-5.pcapng_1.png" alt="alt text" /></p><p>The Satistics - FlowGraph on a filtered trace should also help to see the 'RTT's of each hop' <img src="https://osqa-ask.wireshark.org/upfiles/ttl3-5.pcapng.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Dec '13, 09:43</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 11 Dec '13, 11:30</p></div></div><div id="comments-container-28009" class="comments-container"><span id="28010"></span><div id="comment-28010" class="comment"><div id="post-28010-score" class="comment-score"></div><div class="comment-text"><p>I want to see the RTT between my host and the targeted router. As far as I could tell, delta time is the time between two consecutive packets in the packet trace, right? If so, it's of no interest to me, as I have bursts of probes and bursts of replies.</p></div><div id="comment-28010-info" class="comment-info"><span class="comment-age">(11 Dec '13, 09:46)</span> rick_r</div></div></div><div id="comment-tools-28009" class="comment-tools"></div><div class="clear"></div><div id="comment-28009-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

