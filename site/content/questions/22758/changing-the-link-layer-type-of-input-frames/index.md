+++
type = "question"
title = "Changing the link-layer type of input frames"
description = '''Hi, I am writing a dissector plugin for Wireshark, which decapsulates an Ethernet frame with an additional tag between src address and type/length field (like 802.1q). I understood about the wtap_encap dissector table. By default (as far as I know) Wireshark reads the link-layer type from the interf...'''
date = "2013-07-09T06:50:00Z"
lastmod = "2013-07-18T12:23:00Z"
weight = 22758
keywords = [ "text2pcap", "dlt_user" ]
aliases = [ "/questions/22758" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Changing the link-layer type of input frames](/questions/22758/changing-the-link-layer-type-of-input-frames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22758-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am writing a dissector plugin for Wireshark, which decapsulates an Ethernet frame with an additional tag between src address and type/length field (like 802.1q). I understood about the wtap_encap dissector table. By default (as far as I know) Wireshark reads the link-layer type from the interface (which is usually 1 =&gt; Ethernet) and that's the first dissector that it uses. My target is to change the link-layer input type of wireshark to 147 (DLT_USER0) so that my dissector can be the entry point of the process of decapsulation. How can I do that ? I tried to make a crazy pipe<br />
</p><p><em>tcpdump -l -nvvvXXes0 | od -Ax -tx1 -v - | text2pcap -l 147 - - | wireshark -k -i -</em></p><p>The goal of the upper command is to capture (live) packets with tcpdump then use od to hexdump them in the appropriate format for text2pcap which then changes the link-layer type to 147 and pipes that to wireshark. The problem is that text2pcap, for some reason, merges the packets and outputs them to wireshark as 64000 byte packets.</p><p>Is there any other way of making a live wireshark capture while changing the link-layer type to 147 ?<br />
And what's the problem of text2pcap ? Maybe I'm not using the appropriate options to tcpdump and it doesn't like the input format ...</p></div><div id="question-tags" class="tags-container tags">text2pcap dlt_user</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '13, 06:50</strong></p><img src="https://secure.gravatar.com/avatar/af14bf0d1eefdb1659cb46b96be7f639?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dvlahovski&#39;s gravatar image" /><p>dvlahovski<br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dvlahovski has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-22758" class="comments-container"></div><div id="comment-tools-22758" class="comment-tools"></div><div class="clear"></div><div id="comment-22758-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="22794"></span>

<div id="answer-container-22794" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22794-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are several problems with your command chain.</p><p>1.) tcpdump output to od</p><p>This is what tcpdump writes on my system, if I run it with your parameters (tcpdump -l -nvvvXXes0).</p><pre><code>01:14:07.649043 00:0c:29:f6:9e:14 &gt; 00:50:56:e0:14:49, ethertype IPv4 (0x0800), length 95: (tos 0x0, ttl 64, id 9872, offset 0, flags [DF], proto TCP (6), length 81)
    192.168.158.128.50199 &gt; 1.2.3.4.443: Flags [P.], cksum 0x6667 (correct), seq 1547098647:1547098688, ack 492193187, win 64197, length 41
    0x0000:  0050 56e0 1449 000c 29f6 9e14 0800 4500  .PV..I..).....E.
    0x0010:  0051 2690 4000 4006 53e8 c0a8 9e80 5043  .Q&amp;[email protected]@.S.....PC
    0x0020:  10c3 c417 01bb 5c36 da17 1d56 45a3 5018  ......\6...VE.P.
    0x0030:  fac5 6667 0000 1703 0100 24a0 d25c bdcb  ..fg......$..\..
    0x0040:  9f8e 7ffd 2892 68a8 9fee d381 8d85 ee0e  ....(.h.........
    0x0050:  2f42 8e1a 4942 d8c7 e65b 07f0 0be2 e9    /B..IB...[.....</code></pre><p>Converting that output with od to hex and then piping it to text2pcap does not work, as you will pipe the hex representation of the ASCII output of tcpdump to text2pcap. This will give totally random results.</p><p>2.) Output of tcpdump</p><p>The output of tcpdump is (unfortunately) <strong>not</strong> in a format that text2pcap understands (see man page of text2pcap)</p><pre><code>Text2pcap understands a hexdump of the form generated by od -Ax -tx1 -v. In other words, each byte is individually displayed and surrounded with a space. Each line begins with an offset describing the position in the file. The offset is a hex number (can also be octal or decimal - see -o), of more than two hex digits. Here is a sample dump that text2pcap can recognize:</code></pre><p>Output of tcpdump:</p><pre><code>01:14:07.649043 00:0c:29:f6:9e:14 &gt; 00:50:56:e0:14:49, ethertype IPv4 (0x0800), length 95: (tos 0x0, ttl 64, id 9872, offset 0, flags [DF], proto TCP (6), length 81)
    192.168.158.128.50199 &gt; 1.2.3.4.443: Flags [P.], cksum 0x6667 (correct), seq 1547098647:1547098688, ack 492193187, win 64197, length 41
    0x0000:  0050 56e0 1449 000c 29f6 9e14 0800 4500  .PV..I..).....E.
    0x0010:  0051 2690 4000 4006 53e8 c0a8 9e80 5043  .Q&amp;[email protected]@.S.....PC</code></pre><p>This is what text2pcap needs:</p><pre><code>01:14:07.649043
0000  00 50 56 e0 14 49 00 0c 29 f6 9e 14 08 00 45 00
0010  00 51 26 90 40 00 40 06 53 e8 c0 a8 9e 80 50 43</code></pre><p>So, you need to reformat the tcpdump output. Here is a small perl script that will reformat the text.</p><pre><code>#!/usr/bin/perl

$| = 1;

my $regexp_time = &#39;(\d\d:\d\d:\d\d\.\d+ )&#39;;
my $regexp_hex = &#39;(0x\d+:\s+)([0-9a-f ]+)+  &#39;;

while (&lt;STDIN&gt;) {

   my $input = $_;

   if ($input =~ /^$regexp_time/) {
      print &quot;$1\n&quot;;
   }

   if ($input =~ /$regexp_hex/) {
      my $counter = $1;
      my $line = $2;

      $line =~ s/ //g;
      $counter =~ s/(0x|:)//g;

      print $counter . join(&#39; &#39;, ( $line =~ m/../g )) . &quot;\n&quot;;
   }
}</code></pre><p>Then run your command like this:</p><blockquote><p>tcpdump -l -nvvvXXes0 | perl convert.pl | text2pcap -l 147 - - | wireshark -k -i -</p></blockquote><p>Please report back, if it works. I was not able to test it yet.</p><p><strong>UPDATE</strong>:</p><p>Basically it (the script) works, but without a dissector for the link-layer type 147, the data makes no sense to wireshark.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '13, 03:13</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Jul '13, 01:02</p></div></div><div id="comments-container-22794" class="comments-container"><span id="23106"></span><div id="comment-23106" class="comment"><div id="post-23106-score" class="comment-score"></div><div class="comment-text"><p>Hi,<br />
Thank you very much for the help !<br />
The script really perfectly does the job. But for the first N packets. I mean that, when I run the command chain, the first time, I got 17 proper packets (with total length of ~2100 bytes) and then it started to print only 16 byte packets. After that, I ran it a second time and then got 64 proper packets (with total size of ~4400 bytes) and then started to output only 16 byte packets again. And it happens every time - from a given point on(undefined, I think, because the byte offset after it happens is different every time) it prints only 16 byte packets. When I changed the link-layer type to 1, to see what's happening, I saw that it was dissecting the proper packets without a problem. The 16 byte packets ethertype was recognized, but they were (obviously) stated as malformed. Do you have any idea why does this problem occur ?</p><p>Best regards and many thanks,<br />
D. Vlahovski</p></div><div id="comment-23106-info" class="comment-info"><span class="comment-age">(18 Jul '13, 06:54)</span> dvlahovski</div></div><span id="23140"></span><div id="comment-23140" class="comment"><div id="post-23140-score" class="comment-score">1</div><div class="comment-text"><p>I had the same issue with text2pcap 1.6.9 (Ubuntu). After I upgraded to 1.10.0 the problem was gone.</p></div><div id="comment-23140-info" class="comment-info"><span class="comment-age">(19 Jul '13, 01:47)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-22794" class="comment-tools"></div><div class="clear"></div><div id="comment-22794-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22791"></span>

<div id="answer-container-22791" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22791-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think the problem is that your hex stream after the od command is just one continuous block of hex data, so text2pcap probably cuts it into the larges slices it can. Have you tried the -m parameter of text2pcak that limits the maximum packet size? I haven't tested if it help, but you might want to check it out. Unfortunately that will probably result in packets of the same size, and not what they originally where, so I guess it will not help that much either.</p><p>You could also try to get better results by capturing with dumpcap or tshark to get the frame delimiter right, but once again I haven't tried that myself. All in all you're trying some sort of Frankenstein capture maneuver and I'm not sure if it can work at all :-)</p><p>Maybe changing the link-layer type in the file after capture is complete may be an option?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '13, 02:05</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span> </br></br></p></div></div><div id="comments-container-22791" class="comments-container"></div><div id="comment-tools-22791" class="comment-tools"></div><div class="clear"></div><div id="comment-22791-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23108"></span>

<div id="answer-container-23108" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23108-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>My target is to change the link-layer input type of wireshark to 147 (DLT_USER0) so that my dissector can be the entry point of the process of decapsulation. How can I do that ?</p></blockquote><p>Try</p><pre><code>editcap -T user0 -F libpcap {input file} {output file}</code></pre><p>to read a pcap file {input file} and write out the exact same packet data to a pcap file {output file}, but with a different link-layer header type in the file header.</p><p>That <em>might</em> also work for pcap-ng files (if you're reading a pcap-ng file, you can leave out the <code>-F libpcap</code>).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jul '13, 12:23</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></p></div></div><div id="comments-container-23108" class="comments-container"></div><div id="comment-tools-23108" class="comment-tools"></div><div class="clear"></div><div id="comment-23108-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

