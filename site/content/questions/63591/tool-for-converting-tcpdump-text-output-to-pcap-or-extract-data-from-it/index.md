+++
type = "question"
title = "Tool for converting TcpDump text output to pcap or extract data from it."
description = '''I would like to analyse network traffic of a system, which I don&#x27;t have write access on it, so I couldn&#x27;t save the tcpdump as pcap file using -w options. So, I came up with saving the command line result in text file by following command: tcpdump -nnvvvSettXXU -s 0 -i eth1 &amp;gt; traffic.txt  How can ...'''
date = "2017-09-12T14:07:00Z"
lastmod = "2017-09-14T12:47:00Z"
weight = 63591
keywords = [ "text2pcap", "howtoanalyzetcpdump", "tcpdump" ]
aliases = [ "/questions/63591" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Tool for converting TcpDump text output to pcap or extract data from it.](/questions/63591/tool-for-converting-tcpdump-text-output-to-pcap-or-extract-data-from-it)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63591-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to analyse network traffic of a system, which I don't have write access on it, so I couldn't save the tcpdump as pcap file using <code>-w</code> options. So, I came up with saving the command line result in text file by following command:</p><pre><code>tcpdump -nnvvvSettXXU -s 0 -i eth1 &gt; traffic.txt</code></pre><p>How can I analyses the output.</p><p>Following is the sample of output:</p><pre><code>1505232640.039941 MAC &gt; MAC, ethertype ARP (0x0806), length 42: Ethernet (len 6), IPv4 (len 4), Request who-has 10.0.3.2 tell 10.0.3.15, length 28
    0x0000:  5254 0012 3502 0800 2767 89f1 0806 0001  RT..5...&#39;g......
    0x0010:  0800 0604 0001 0800 2767 89f1 0a00 030f  ........&#39;g......
    0x0020:  0000 0000 0000 0a00 0302                 ..........
1505232640.040137 MAC &gt; MAC, ethertype ARP (0x0806), length 42: Ethernet (len 6), IPv4 (len 4), Reply 10.0.3.2 is-at 52:54:00:12:35:02, length 28
    0x0000:  0800 2767 89f1 5254 0012 3502 0806 0001  ..&#39;g..RT..5.....
    0x0010:  0800 0604 0002 5254 0012 3502 0a00 0302  ......RT..5.....
    0x0020:  0800 2767 89f1 0a00 030f                 ..&#39;g......
1505232650.113663 MAC &gt; MAC, ethertype IPv4 (0x0800), length 155: (tos 0x0, ttl 64, id 2428, offset 0, flags [none], proto TCP (6), length 141)
    37.48.64.202.7095 &gt; 10.0.3.15.37022: Flags [P.], cksum 0x09ee (correct), seq 2844491:2844592, ack 905630997, win 65535, length 101
    0x0000:  0800 2767 89f1 5254 0012 3502 0800 4500  ..&#39;g..RT..5...E.
    0x0010:  008d 097c 0000 4006 fde6 2530 40ca 0a00  ...|[email protected]%[email protected]
    0x0020:  030f 1bb7 909e 002b 674b 35fa d515 5018  .......+gK5...P.
    0x0030:  ffff 09ee 0000 1703 0300 6098 68bf 586b  ..........`.h.Xk
    0x0040:  09e6 6472 fc92 b4c0 4d4e a3d4 4c4c f8df  ..dr....MN..LL..
    0x0050:  4760 64d0 fd12 ec6c 058e 8f7f ecf4 e5e0  G`d....l........
    0x0060:  1e3a 32c4 1b33 459d a3e8 b5d0 3481 7901  .:2..3E.....4.y.
    0x0070:  36f6 712a f14f 5bc5 076c 941d 8a24 a541  6.q*.O[..l...$.A
    0x0080:  7d88 5a6b 5dff 19c5 80db 4f8c d7a4 b490  }.Zk].....O.....
    0x0090:  6869 b1b1 c344 5894 d2c4 56              hi...DX...V</code></pre><p><strong>Edit</strong>:</p><p>I find text2pacp but my text file format isn't acceptable by it. So I write the following python script to convert the format to suitable form:</p><pre><code>import re
regexp_time =re.compile(&quot;\d\d\d\d\d\d\d\d\d\d.\d\d\d\d\d\d+&quot;)
regexp_hex = re.compile(&quot;(\t0x\d+:\s+)([0-9a-f ]+)+  &quot;)

with open (&#39;../Traffic/traffic1.txt&#39;) as input,open (&#39;../Traffic/txt2.txt&#39;,&#39;w&#39;) as output:
    for line in input:
        if regexp_time.match(line):
            output.write (&quot;%s\n&quot; % (line.split()[0]))
        elif regexp_hex.match(line):
            words = line.split(&quot;  &quot;)
            bytes=&quot;&quot;
            for byte in words[1].split():
                if len(byte) == 4:
                    bytes += &quot;%s%s %s%s &quot;%(byte[0],byte[1],byte[2],byte[3])
                elif len(byte) == 2:
                    bytes += &quot;%s%s &quot;%(byte[0],byte[1])
            output.write (&quot;%s  %s %s \n&quot; % (words[0].replace(&quot;0x&quot;,&quot;00&quot;),&quot;{:&lt;47}&quot;.format (bytes),words[2].replace(&quot;\n&quot;,&quot;&quot;)))

input.close()
output.close()</code></pre><p>As I'm new to python could someone help me to speed up the code?! You can find more efficient code <a href="https://stackoverflow.com/questions/46216925/speed-up-python-code">here</a>:</p><p><strong>Edit</strong>:</p><p>Here is the story why I should capture in this way.</p><p>I have multiple Genymotion devices on host, which is assigned static IP, So I couldn't set network mode of the devices to bridge. Therefor all of them set to NAT mode and then get same IP but different MAC addresses. So I came up with capturing each devices traffic by running <code>tcpdump</code> on each devices. but As I have other running processes in each device and also limited space on each of them and also no write permission. I couldn't use <code>-w</code> which lead to save file on emulators. But when I use <code>&gt;</code> it will write on host machine which I don't have any limitation.</p><p>PS: Genymotion run on top of Virtualbox.</p></div><div id="question-tags" class="tags-container tags">text2pcap howtoanalyzetcpdump tcpdump</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '17, 14:07</strong></p><img src="https://secure.gravatar.com/avatar/1595a24111dff7d0376d456e91895399?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zahra&#39;s gravatar image" /><p>Zahra<br />
<span class="score" title="31 reputation points">31</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zahra has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Sep '17, 14:34</p></div></div><div id="comments-container-63591" class="comments-container"><span id="63592"></span><div id="comment-63592" class="comment"><div id="post-63592-score" class="comment-score"></div><div class="comment-text"><p>I don't understand. If you're able to create the <code>traffic.txt</code> file, you must have write access so therefore you ought to be able to create a .pcap file using the -w option. Perhaps there's more to the story?</p></div><div id="comment-63592-info" class="comment-info"><span class="comment-age">(12 Sep '17, 14:11)</span> cmaynard ♦♦</div></div><span id="63594"></span><div id="comment-63594" class="comment"><div id="post-63594-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/402/cmaynard">@cmaynard</a> I add the story behind it, do have any Idea? or other way of capturing traffic?</p></div><div id="comment-63594-info" class="comment-info"><span class="comment-age">(13 Sep '17, 11:08)</span> Zahra</div></div></div><div id="comment-tools-63591" class="comment-tools"></div><div class="clear"></div><div id="comment-63591-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63598"></span>

<div id="answer-container-63598" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63598-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I guess I still don't quite understand, but it seems that writing to <code>stdout</code> writes to your host and not to the emulator, so maybe you could just have <a href="http://www.tcpdump.org/tcpdump_man.html"><code>tcpdump</code></a> write to <code>stdout</code> and then redirect the output to a file? For example:</p><pre><code>tcpdump -nnvvvSettXXU -s 0 -i eth1 -w - &gt; traffic.pcap</code></pre><p>Or maybe you could use <a href="https://www.wireshark.org/docs/man-pages/sshdump.html"><code>sshdump</code></a>?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '17, 12:47</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-63598" class="comments-container"><span id="63599"></span><div id="comment-63599" class="comment"><div id="post-63599-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I will try it out. Unfortunately, because of some network issue my connection to host is lost.</p></div><div id="comment-63599-info" class="comment-info"><span class="comment-age">(14 Sep '17, 14:26)</span> Zahra</div></div><span id="63600"></span><div id="comment-63600" class="comment"><div id="post-63600-score" class="comment-score"></div><div class="comment-text"><p>I get following error when I capture using the command you suggest. <code>The capture file appears to be damaged or corrupt. (pcap: File has 1936288800-byte packet, bigger than maximum of 262144)</code></p></div><div id="comment-63600-info" class="comment-info"><span class="comment-age">(16 Sep '17, 00:09)</span> Zahra</div></div><span id="63605"></span><div id="comment-63605" class="comment"><div id="post-63605-score" class="comment-score"></div><div class="comment-text"><p>Did you capture any packets though? Did you try to open the resulting capture file? It might just be the last packet that is affected, and so it probably doesn't matter.</p></div><div id="comment-63605-info" class="comment-info"><span class="comment-age">(19 Sep '17, 07:08)</span> cmaynard ♦♦</div></div><span id="63607"></span><div id="comment-63607" class="comment"><div id="post-63607-score" class="comment-score"></div><div class="comment-text"><p>I capture packet, but when I try to open the file I get that error. How can I solve it?</p></div><div id="comment-63607-info" class="comment-info"><span class="comment-age">(19 Sep '17, 08:56)</span> Zahra</div></div><span id="63608"></span><div id="comment-63608" class="comment"><div id="post-63608-score" class="comment-score"></div><div class="comment-text"><p>If it bothers you, you can probably just use <a href="https://www.wireshark.org/docs/man-pages/editcap.html"><code>editcap</code></a> to remove the last packet from the capture file. Or you can use Wireshark itself: <em>File -&gt; Export Specified Packets... -&gt; Range: 1-N</em> ... where <em>N</em> is 1 less than the number of packets you captured. This assumes the last packet is the mal-formed one.</p></div><div id="comment-63608-info" class="comment-info"><span class="comment-age">(19 Sep '17, 09:12)</span> cmaynard ♦♦</div></div><span id="63609"></span><div id="comment-63609" class="comment not_top_scorer"><div id="post-63609-score" class="comment-score"></div><div class="comment-text"><p>Why It happens? How can I Prevent it?</p></div><div id="comment-63609-info" class="comment-info"><span class="comment-age">(19 Sep '17, 09:48)</span> Zahra</div></div><span id="63610"></span><div id="comment-63610" class="comment not_top_scorer"><div id="post-63610-score" class="comment-score"></div><div class="comment-text"><p>Maybe try experimenting with <a href="https://linux.die.net/man/1/stdbuf"><code>stdbuf</code></a>? For example:</p><pre><code>stdbuf -o 0 tcpdump -nnvvvSettXXU -s 0 -i eth1 -w - &gt; traffic.pcap</code></pre><p>(I see now that you were already using -U, so obviously that wasn't helping.)</p></div><div id="comment-63610-info" class="comment-info"><span class="comment-age">(19 Sep '17, 09:57)</span> cmaynard ♦♦</div></div><span id="63611"></span><div id="comment-63611" class="comment not_top_scorer"><div id="post-63611-score" class="comment-score"></div><div class="comment-text"><p>I didn't get what you mean by "that wasn't helping".</p></div><div id="comment-63611-info" class="comment-info"><span class="comment-age">(19 Sep '17, 10:24)</span> Zahra</div></div><span id="63612"></span><div id="comment-63612" class="comment not_top_scorer"><div id="post-63612-score" class="comment-score"></div><div class="comment-text"><p>I meant that the <code>-U</code> option wasn't helping to prevent the corrupted packet from being written to the pcap file. I was going to suggest using it, but then I noticed that you already were.</p></div><div id="comment-63612-info" class="comment-info"><span class="comment-age">(19 Sep '17, 10:30)</span> cmaynard ♦♦</div></div><span id="64335"></span><div id="comment-64335" class="comment not_top_scorer"><div id="post-64335-score" class="comment-score"></div><div class="comment-text"><p>Is it possible that capturing traffic this way result in missing packets?</p></div><div id="comment-64335-info" class="comment-info"><span class="comment-age">(08 Dec '17, 22:02)</span> Zahra</div></div></div><div id="comment-tools-63598" class="comment-tools"><span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a></div><div class="clear"></div><div id="comment-63598-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

