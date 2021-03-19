+++
type = "question"
title = "Is it possible to capture TCPDUMP logging and import into Wireshark?"
description = '''Hello, Is it possible to capture tcpdump data from the screen (not a file) and then import into Wireshark? For example, I want to run the following tcpdump command: ./tcpdump -vvvvv -i eth0 Then I want to be able to import this into Wireshark (Window GuI version) for analysis. Thanks in advance '''
date = "2012-08-13T13:51:00Z"
lastmod = "2012-08-15T02:23:00Z"
weight = 13593
keywords = [ "tcpdump" ]
aliases = [ "/questions/13593" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to capture TCPDUMP logging and import into Wireshark?](/questions/13593/is-it-possible-to-capture-tcpdump-logging-and-import-into-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13593-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Is it possible to capture tcpdump data from the screen (not a file) and then import into Wireshark? For example, I want to run the following tcpdump command:</p><p>./tcpdump -vvvvv -i eth0</p><p>Then I want to be able to import this into Wireshark (Window GuI version) for analysis.</p><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags">tcpdump</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Aug '12, 13:51</strong></p><img src="https://secure.gravatar.com/avatar/8f8e1f010f6bdba9ac95ff48b525b89b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gil_happy&#39;s gravatar image" /><p>gil_happy<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gil_happy has no accepted answers">0%</span></p></div></div><div id="comments-container-13593" class="comments-container"></div><div id="comment-tools-13593" class="comment-tools"></div><div class="clear"></div><div id="comment-13593-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="13636"></span>

<div id="answer-container-13636" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13636-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>OK, I did some testing, you can use the following also. Dump the packet data with '-xx' (double x to get the link layer data too) like this:</p><pre><code>$ tcpdump -nli en1 -xx -s0 -c 3 icmp
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on en1, link-type EN10MB (Ethernet), capture size 65535 bytes
23:06:22.515580 IP 192.168.1.22 &gt; 8.8.8.8: ICMP echo request, id 44623, seq 0, length 64
    0x0000:  0012 1ebb d132 f81e dfd8 8748 0800 4500
    0x0010:  0054 153e 0000 4001 939d c0a8 0116 0808
    0x0020:  0808 0800 72d6 ae4f 0000 502a bdce 0007
    0x0030:  ddd6 0809 0a0b 0c0d 0e0f 1011 1213 1415
    0x0040:  1617 1819 1a1b 1c1d 1e1f 2021 2223 2425
    0x0050:  2627 2829 2a2b 2c2d 2e2f 3031 3233 3435
    0x0060:  3637
23:06:22.538398 IP 8.8.8.8 &gt; 192.168.1.22: ICMP echo reply, id 44623, seq 0, length 64
    0x0000:  f81e dfd8 8748 0012 1ebb d132 0800 4500
    0x0010:  0054 5a72 0000 3701 5769 0808 0808 c0a8
    0x0020:  0116 0000 7ad6 ae4f 0000 502a bdce 0007
    0x0030:  ddd6 0809 0a0b 0c0d 0e0f 1011 1213 1415
    0x0040:  1617 1819 1a1b 1c1d 1e1f 2021 2223 2425
    0x0050:  2627 2829 2a2b 2c2d 2e2f 3031 3233 3435
    0x0060:  3637
23:06:23.515979 IP 192.168.1.22 &gt; 8.8.8.8: ICMP echo request, id 44623, seq 1, length 64
    0x0000:  0012 1ebb d132 f81e dfd8 8748 0800 4500
    0x0010:  0054 4543 0000 4001 6398 c0a8 0116 0808
    0x0020:  0808 0800 714b ae4f 0001 502a bdcf 0007
    0x0030:  df5f 0809 0a0b 0c0d 0e0f 1011 1213 1415
    0x0040:  1617 1819 1a1b 1c1d 1e1f 2021 2223 2425
    0x0050:  2627 2829 2a2b 2c2d 2e2f 3031 3233 3435
    0x0060:  3637
3 packets captured
62 packets received by filter
0 packets dropped by kernel
$</code></pre><p>Then copy the output and process it with sed like this:</p><pre><code>$ cat screendump.txt | sed -e &#39;s/ \([^ ][^ ]\)\([^ ][^ ]\)/ \1 \2/g&#39; -e &#39;s/^\(..:..:..\).*$/\1/&#39; -e &#39;s/^.*0x\(....\): /\1/&#39; 
23:06:22
0000 00 12 1e bb d1 32 f8 1e df d8 87 48 08 00 45 00
0010 00 54 15 3e 00 00 40 01 93 9d c0 a8 01 16 08 08
0020 08 08 08 00 72 d6 ae 4f 00 00 50 2a bd ce 00 07
0030 dd d6 08 09 0a 0b 0c 0d 0e 0f 10 11 12 13 14 15
0040 16 17 18 19 1a 1b 1c 1d 1e 1f 20 21 22 23 24 25
0050 26 27 28 29 2a 2b 2c 2d 2e 2f 30 31 32 33 34 35
0060 36 37
23:06:22
0000 f8 1e df d8 87 48 00 12 1e bb d1 32 08 00 45 00
0010 00 54 5a 72 00 00 37 01 57 69 08 08 08 08 c0 a8
0020 01 16 00 00 7a d6 ae 4f 00 00 50 2a bd ce 00 07
0030 dd d6 08 09 0a 0b 0c 0d 0e 0f 10 11 12 13 14 15
0040 16 17 18 19 1a 1b 1c 1d 1e 1f 20 21 22 23 24 25
0050 26 27 28 29 2a 2b 2c 2d 2e 2f 30 31 32 33 34 35
0060 36 37
23:06:23
0000 00 12 1e bb d1 32 f8 1e df d8 87 48 08 00 45 00
0010 00 54 45 43 00 00 40 01 63 98 c0 a8 01 16 08 08
0020 08 08 08 00 71 4b ae 4f 00 01 50 2a bd cf 00 07
0030 df 5f 08 09 0a 0b 0c 0d 0e 0f 10 11 12 13 14 15
0040 16 17 18 19 1a 1b 1c 1d 1e 1f 20 21 22 23 24 25
0050 26 27 28 29 2a 2b 2c 2d 2e 2f 30 31 32 33 34 35
0060 36 37
$</code></pre><p>If you redirect that output to a file, it can be imported in Wireshark with "File -&gt; Import...", just make sure you enable timestamps and give "%T" as time format.</p><p>(if you're on Windows, you might want to consider installing a sed program or <a href="http://www.cygwin.com/">cygwin</a>)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '12, 14:12</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-13636" class="comments-container"><span id="13640"></span><div id="comment-13640" class="comment"><div id="post-13640-score" class="comment-score"></div><div class="comment-text"><p>Fabulous... I will give this a go tomorrow.</p><p>However, if I just want to sniff everything on a particular interface, e.g. eth0, what would the syntax be? Note, there is not a lot of traffic on this interface.</p><p>Thanks</p></div><div id="comment-13640-info" class="comment-info"><span class="comment-age">(14 Aug '12, 16:21)</span> gil_happy</div></div><span id="13657"></span><div id="comment-13657" class="comment"><div id="post-13657-score" class="comment-score"></div><div class="comment-text"><p>Then the syntax would be:</p><pre><code>tcpdump -s0 -nn -l -xx -i eth0</code></pre></div><div id="comment-13657-info" class="comment-info"><span class="comment-age">(15 Aug '12, 07:46)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-13636" class="comment-tools"></div><div class="clear"></div><div id="comment-13636-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13598"></span>

<div id="answer-container-13598" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13598-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately that is not possible, as the packet bytes get lost. You might be able to use some scripting to be able to import "tcpdump -s0 -x -i eth0" output.</p><p>If the problem is that you can only copy screen output, you might want to save the trace locally with "tcpdump -s0 -w tmp.cap" and then use uuencode to create ascii text on the screen which you can copy &amp; paste and uudecode.</p><p>Or do it in one go: "tcpdump -s0 -i en1 -w - -c 10 2&gt;/dev/null | uuencode tmp.cap"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '12, 15:14</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-13598" class="comments-container"><span id="13631"></span><div id="comment-13631" class="comment"><div id="post-13631-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the info... Unfortunately the problem is that if I save it to a file (which is a remote device), I have no way to pull the pcap file off the unit. That is why I was wondering if there was a way to dump the screen output into Wireshark.</p><p>Thanks for the help.</p></div><div id="comment-13631-info" class="comment-info"><span class="comment-age">(14 Aug '12, 12:43)</span> gil_happy</div></div><span id="13633"></span><div id="comment-13633" class="comment"><div id="post-13633-score" class="comment-score"></div><div class="comment-text"><p>That's why I suggested to uuencode the binary file, you can copy the output from the console/terminal/screen and paste it into a file on your own system to uudecode it back to a binary file.</p><p>I have used this when I only had a 9600 bps serial console available, it takes time, but at least you get all the data :-)</p><p>(if the box does not have uuencode but does have perl, you can paste <a href="http://userpages.monmouth.com/~colonel/unixware/uuencode.pl">this code</a> to it to do the encoding :-)</p></div><div id="comment-13633-info" class="comment-info"><span class="comment-age">(14 Aug '12, 13:34)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-13598" class="comment-tools"></div><div class="clear"></div><div id="comment-13598-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13641"></span>

<div id="answer-container-13641" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13641-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are some other options as well.</p><p><strong>xxd</strong><br />
xxd is available (per default) on many Linux distributions and there is also a windows version (e.g. as part of vim - <a href="http://www.vim.org">http://www.vim.org</a>)</p><blockquote><p><code>tcpdump -ni eth0 -s0 -w /var/tmp/dump.pcap</code><br />
<code>xxd /var/tmp/dump.pcap /var/tmp/dump.hex</code><br />
<code>cat /var/tmp/dump.hex</code><br />
</p></blockquote><p>Copy the output and save it as dump.hex on another system. Then use <strong>xxd</strong> on that system to <strong>revert</strong> the hex dump back to a binary.</p><blockquote><p><code>xxd -r dump.hex dump.pcap</code><br />
</p></blockquote><p>You can now open dump.pcap in Wireshark.</p><p><strong>remote capture with ssh</strong><br />
I assume, you are able to connect to the system with ssh to run the tcpdump command. However, if that is possible, you could also just copy the binary data with <strong>scp</strong> through that channel, and the whole HEX -&gt; binary conversion would not be necessary !??!</p><blockquote><p><code>ssh -l root 192.168.0.1 "tcpdump -ni eth0 -s0 -w -" &gt; dump.pcap</code></p></blockquote><p>Then open dump.pcap in Wireshark.</p><p><strong>UPDATE:</strong><br />
If you don't have xxd on your system, you can also use hexdump and then convert the output to something xxd understands.</p><p>HOWTO:</p><ul><li><p>run this command</p><blockquote><p><code>hexdump -C input.cap | awk '{$1 = substr($1,2) ":"; gsub(/\|/," "); gsub(/[0-9a-f]+:$/,""); print}' &gt; capture.hex</code><br />
</p></blockquote></li><li>copy/paste the output of capture.hex to your windows system</li><li>install vim from <a href="http://www.vim.org">http://www.vim.org</a></li><li><p>run the following commands<br />
</p><blockquote><p><code>cd %PROGRAMFILES%\vim\vim73</code><br />
<code>xxd -r c:\temp\capture.hex c:\temp\capture.pcap</code><br />
</p></blockquote></li><li>open c:\temp\capture.pcap in Wireshark</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '12, 17:47</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Aug '12, 02:44</p></div></div><div id="comments-container-13641" class="comments-container"><span id="13643"></span><div id="comment-13643" class="comment"><div id="post-13643-score" class="comment-score"></div><div class="comment-text"><p>I did not know about xxd, we learn everyday :-)</p><p>However, for this purpose, I think uuencode is a lot more efficient:</p><pre><code>$ wc bug4716.cap 
  12      19     498 bug4716.cap
$ uuencode bug4716.cap bug4716.cap | wc
  15      17     716
$ xxd bug4716.cap | wc
  32     313    2130
$</code></pre><p>But if xxd is available and uuencode is not... :-)</p><p>UPDATE: OK, when using xxd, you might want to use -p to reduce the size:</p><pre><code>$ xxd -p bug4716.cap | wc
  17      17    1013
$</code></pre></div><div id="comment-13643-info" class="comment-info"><span class="comment-age">(15 Aug '12, 00:10)</span> SYN-bit ♦♦</div></div><span id="13646"></span><div id="comment-13646" class="comment"><div id="post-13646-score" class="comment-score"></div><div class="comment-text"><blockquote><p>But if xxd is available and uuencode is not... :-)</p></blockquote><p>That's the only good reason to use xxd, as uuencode tends to be missing on some linux systems ;-)</p></div><div id="comment-13646-info" class="comment-info"><span class="comment-age">(15 Aug '12, 01:17)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-13641" class="comment-tools"></div><div class="clear"></div><div id="comment-13641-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13648"></span>

<div id="answer-container-13648" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13648-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I recently used a remote command over ssh to pipe back into a local copy of tshark which then wrote into local files.</p><pre><code>ssh [email protected] &quot;tcpdump -i eth0 -w -&quot; | tshark -i - -b filesize:50000 -w dump.pcap</code></pre><p>Note that I had installed a public key for the user on the remote system so no user input was required on the ssh connection.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Aug '12, 02:23</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></br></p></div></div><div id="comments-container-13648" class="comments-container"><span id="13655"></span><div id="comment-13655" class="comment"><div id="post-13655-score" class="comment-score"></div><div class="comment-text"><p>Thanks for all suggestions to date.. unfortunately the SSH suggestion is not an option.</p><p>Here is what I have done so far.</p><ul><li>I captured DHCP logs on the remote device using the following: ./tcpdump -v -i br0 -s 65535 -w dhcp.pcap</li><li>Then I did, ‘hexdump -C dhcp.pcap’</li></ul><p>I then copied and pasted the output on my screen and saved it to Notepad. Now I'm trying to figure out how to Import back to Wireshark or even 'Packet Dump Decode'. I don't know if I'm doing something incorrectly, or if I need to make minor edit to the pasted output?</p></div><div id="comment-13655-info" class="comment-info"><span class="comment-age">(15 Aug '12, 07:32)</span> gil_happy</div></div><span id="13656"></span><div id="comment-13656" class="comment"><div id="post-13656-score" class="comment-score"></div><div class="comment-text"><p>hexdump does not seem to have a 'reverse' option. Do you have uuencode or xdd on the box?</p></div><div id="comment-13656-info" class="comment-info"><span class="comment-age">(15 Aug '12, 07:46)</span> SYN-bit ♦♦</div></div><span id="13677"></span><div id="comment-13677" class="comment"><div id="post-13677-score" class="comment-score"></div><div class="comment-text"><p>if you don't have uuencode (preferred) or xxd, did you try the option posted by SYN-bit (tcpdump -xxx ...)? That will work.</p><p>Another option would be to convert the output of hexdump to a format that xxd (windows version) accepts. See the UPDATE in my answer above.</p></div><div id="comment-13677-info" class="comment-info"><span class="comment-age">(16 Aug '12, 02:33)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-13648" class="comment-tools"></div><div class="clear"></div><div id="comment-13648-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

