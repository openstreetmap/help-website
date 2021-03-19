+++
type = "question"
title = "How to unpack a sniff file"
description = '''Hello, I have catched 2 files with wireshark but I have no idea, how to unpack, or filter the sniff, to get the files. http://forum.ican3800.zajsoft.net/download/ADB3800TW-Italy/capture1_win.pcap http://forum.ican3800.zajsoft.net/download/ADB3800TW-Italy/capture1.pcap Can somebody help me please?'''
date = "2013-12-15T04:26:00Z"
lastmod = "2013-12-18T02:14:00Z"
weight = 28116
keywords = [ "firmware", "unpack", "sniff" ]
aliases = [ "/questions/28116" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to unpack a sniff file](/questions/28116/how-to-unpack-a-sniff-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28116-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28116-score" class="post-score" title="current number of votes">0</div><span id="post-28116-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have catched 2 files with wireshark but I have no idea, how to unpack, or filter the sniff, to get the files.</p><p><a href="http://forum.ican3800.zajsoft.net/download/ADB3800TW-Italy/capture1_win.pcap">http://forum.ican3800.zajsoft.net/download/ADB3800TW-Italy/capture1_win.pcap</a></p><p><a href="http://forum.ican3800.zajsoft.net/download/ADB3800TW-Italy/capture1.pcap">http://forum.ican3800.zajsoft.net/download/ADB3800TW-Italy/capture1.pcap</a></p><p>Can somebody help me please?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-firmware" rel="tag" title="see questions tagged &#39;firmware&#39;">firmware</span> <span class="post-tag tag-link-unpack" rel="tag" title="see questions tagged &#39;unpack&#39;">unpack</span> <span class="post-tag tag-link-sniff" rel="tag" title="see questions tagged &#39;sniff&#39;">sniff</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '13, 04:26</strong></p><img src="https://secure.gravatar.com/avatar/9c333de3633e59d97be8bff879aa5653?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joseff&#39;s gravatar image" /><p><span>joseff</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joseff has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Dec '13, 04:28</strong> </span></p></div></div><div id="comments-container-28116" class="comments-container"><span id="28120"></span><div id="comment-28120" class="comment"><div id="post-28120-score" class="comment-score"></div><div class="comment-text"><p>What kind of files?</p></div><div id="comment-28120-info" class="comment-info"><span class="comment-age">(15 Dec '13, 06:48)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="28121"></span><div id="comment-28121" class="comment"><div id="post-28121-score" class="comment-score"></div><div class="comment-text"><p>It is a Firmware update by using a TFTP transfer. The firs file shall prepare the unpacking for the second file posted above.</p></div><div id="comment-28121-info" class="comment-info"><span class="comment-age">(15 Dec '13, 09:26)</span> <span class="comment-user userinfo">joseff</span></div></div><span id="28123"></span><div id="comment-28123" class="comment"><div id="post-28123-score" class="comment-score"></div><div class="comment-text"><p>do you mind to tell us the IP addresses of the involved systems?</p></div><div id="comment-28123-info" class="comment-info"><span class="comment-age">(15 Dec '13, 10:36)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="28127"></span><div id="comment-28127" class="comment"><div id="post-28127-score" class="comment-score"></div><div class="comment-text"><p>Well, there is no problem to tell the IP (I am authorized), but I don't have them. The box is using DHCP, but only one IP is fixed. It is the multicast address 239.113.254.2:22222</p><p>That IP is important to receive the access key (BootCast), or the Firmware in the box.</p><p>There are 2 sniff files instead of 1 because the sniff was done with a configuration "network tap" with 2 PC's simultaneously. One PC was recording the exchange with the VS and the other PC was recording the exchange with the server. The sniff on the 2 PS was started almost simultaneously but obviously it is not exactly the same time.</p></div><div id="comment-28127-info" class="comment-info"><span class="comment-age">(15 Dec '13, 12:03)</span> <span class="comment-user userinfo">joseff</span></div></div></div><div id="comment-tools-28116" class="comment-tools"></div><div class="clear"></div><div id="comment-28116-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="28119"></span>

<div id="answer-container-28119" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28119-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28119-score" class="post-score" title="current number of votes">0</div><span id="post-28119-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Presuming you mean you transferred two files using a protocol such as HTTP and captured the traffic during the transfer, open the files with Wireshark, then from the File menu select "Export Objects" and then the transport protocol used, e.g. "HTTP". From the resulting dialog, select the object of choice and then click the "Save As" button and save the object to your filesystem.</p><p>I didn't look too hard at your files, but the first one didn't seem to have any http objects (there are only requests, no server responses) and the second contains a video stream over udp (using ISO 13818-1) and a a jpg over http (Captain America DVD cover?). The image can be saved using the above description, but I don't know how to save the stream. Try searching on the rest of this site.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '13, 06:46</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-28119" class="comments-container"><span id="28169"></span><div id="comment-28169" class="comment"><div id="post-28169-score" class="comment-score"></div><div class="comment-text"><p>Thanks for this informations, I am a Wireshark newbie and all helps. Really, Captain America, now I see it too, that is funny.</p><p>I have no idea, how is shall work. The problem is, that the box don't work without this information.</p><p>Before the box start, it must be connected to IPTV. On the boot procedure is it downloading something and than it works. But the provider has end his service, so the box is by all users a goot paperweighter. The only possibility, how to rescue it is to do some access, but we need the Firmware to remove the password by root.</p><p>So we have hoped, that in this old sniff files is the Firmware. That files are related to the data exchange during the VS boot at the time it was connected to the iptv server. Those recordings were for the complete process. At the end of the files the VS was operating correctly.</p><p>So, maybe is it only some unlock key and not Firmware.</p><p>The transfer was TFTP. Is it somehow possible to reverse this sniff and send it to the box? Because we have some files, that we can send to the box, but at the end of the process we are stop with the TCP at the port 19076 and the box is still not working.</p></div><div id="comment-28169-info" class="comment-info"><span class="comment-age">(16 Dec '13, 10:30)</span> <span class="comment-user userinfo">joseff</span></div></div><span id="28205"></span><div id="comment-28205" class="comment"><div id="post-28205-score" class="comment-score"></div><div class="comment-text"><p>I dismissed the DHCP traffic (i.e. the tftp) as noise and went for the usual suspects, http and video\audio.</p></div><div id="comment-28205-info" class="comment-info"><span class="comment-age">(17 Dec '13, 02:38)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="28242"></span><div id="comment-28242" class="comment"><div id="post-28242-score" class="comment-score"></div><div class="comment-text"><p>I have asked the Italian and he told me:</p><p>The bigger .pcap file is large because the sniff acquisition was much longer than the boot of the VS. In that sniff there should be also the streaming from the server (http) and that is the reason of the jpg over http (Captain America DVD cover: at that moment they were promote Captain America)</p></div><div id="comment-28242-info" class="comment-info"><span class="comment-age">(18 Dec '13, 02:14)</span> <span class="comment-user userinfo">joseff</span></div></div></div><div id="comment-tools-28119" class="comment-tools"></div><div class="clear"></div><div id="comment-28119-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28174"></span>

<div id="answer-container-28174" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28174-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28174-score" class="post-score" title="current number of votes">0</div><span id="post-28174-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>The only possibility, how to rescue it is to do some access, but we need the Firmware to remove the password by root.</p></blockquote><p>I don't think the firmware you are looking for is in the capture file. And if it is (there are some larger UDP downloads), it is most certainly encrypted/scrambled (with a key stored on the box).</p><p>Solution to your problem: Instead of trying to extract the firmware from the capture file, google for: <strong><a href="https://www.google.com/?q=adb-3800-tw%20alternative%20firmware">adb-3800-tw alternative firmware</a></strong> and you'll find some information about the boot process and some ideas how to load a different firmware to the box :-)</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Dec '13, 11:40</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-28174" class="comments-container"><span id="28188"></span><div id="comment-28188" class="comment"><div id="post-28188-score" class="comment-score"></div><div class="comment-text"><p>:-D Well, the most found sites are from me, or from some one else of the team. :-)</p><p>We play with this box 4 years and the modified Firmware is working in CZ and ES.</p><p>But this is "the same" box, but from Italy and there was used another Firmware and another data transfer to the box.</p><p>JTAG is possible to use with the CZ and ES box, but by the German Alice HSN-3800TW is some JTAG protection and I get the <strong>Sentinel not found ERROR</strong>. So I can not help the people in Germany with the acces into their box.</p><pre><code>(gdb) sh4tp STMCLT1000A:mb411:st40
The target is assumed to be little endian
The target architecture is assumed to be sh4
mb411_stx7100_cut31 (mb411) connect start - parameters {}
Initialization TCK frequency set to 3000000 Hz
Device id  0x2d424041
tapmux connect(): boot mode single core setup
tapmux setup to bypass to core st40, channel 1
SDI [ERROR] :: [SERVER] serviceASEMode: Sentinel not found (0xffffffff != 0xbeefface)
SDI [ERROR] :: [SERVER] sdi_Attach: Unable to service target after attaching
SDI [ERROR] :: [SERVER] processSDICommand: sdi_Attach failed
SDI [ERROR] :: Command SDI_ATTACH failed (0)
mb411 initialization start with SoC stx7100_cut31 ...
stx7100_cut31: booted audio companion
stx7100_cut31: booted video companion
TCK frequency set to 10000000 Hz
tapmux complete_connect(): single core setup
mb411 initialization complete
SDI [ERROR] :: [SERVER] serviceASEMode: Sentinel not found (0xffffffff != 0xbeefface)
SDI [ERROR] :: [SERVER] sdi_Attach: Unable to service target after attaching
SDI [ERROR] :: [SERVER] processSDICommand: sdi_Attach failed
SDI [ERROR] :: Command SDI_ATTACH failed (0)
Unable to attach to remote target STMCLT1000A:mb411:st40
(gdb)</code></pre><p>The same protection is in the Italian box.</p><p>The last different working IPTV provider, that I know is in Austria: A1 - TLA-3801W - Österreich</p><p>But I had no success to contact someone with this box. I hear, that maybe too in Hungary, Ukraine and USA is someone using this box, but nothing found.</p><p>Our last chance is to unpack this files:</p><p><a href="http://forum.ican3800.zajsoft.net/download/ADB3800TW-Italy/239113254011.ldr">239113254011.ldr</a></p><p><a href="http://forum.ican3800.zajsoft.net/download/ADB3800TW-Italy/239113254012.krn">239113254012.krn</a></p><p>This is the Firmware, but we have trouble to unpack it. The small file prep something for the other file in the box.</p><p>Regards<br />
Joseff</p></div><div id="comment-28188-info" class="comment-info"><span class="comment-age">(16 Dec '13, 14:23)</span> <span class="comment-user userinfo">joseff</span></div></div><span id="28209"></span><div id="comment-28209" class="comment"><div id="post-28209-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Our last chance is to <strong>unpack this files</strong>:</p></blockquote><p>well, I don't think this site is the right place for your problem. We are talking mainly about Wireshark and sometimes about network troubleshooting in general. You should try it in a reversing forum.</p></div><div id="comment-28209-info" class="comment-info"><span class="comment-age">(17 Dec '13, 02:59)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-28174" class="comment-tools"></div><div class="clear"></div><div id="comment-28174-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

