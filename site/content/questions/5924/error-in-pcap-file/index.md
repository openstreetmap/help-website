+++
type = "question"
title = "Error in Pcap file"
description = '''Hello;  I have used wireshark to capture a full days worth of data; however, when I try to open the file, I receive the following error. The capture file appears to be damaged or corrupt. (pcap: File has 1313056966-byte packet, bigger than maximum of 65535), Is there a work around so I can view the ...'''
date = "2011-08-29T11:41:00Z"
lastmod = "2013-05-17T00:17:00Z"
weight = 5924
keywords = [ "corrupt", "damaged", "pcap", "error" ]
aliases = [ "/questions/5924" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Error in Pcap file](/questions/5924/error-in-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5924-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5924-score" class="post-score" title="current number of votes">1</div><span id="post-5924-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello; I have used wireshark to capture a full days worth of data; however, when I try to open the file, I receive the following error.</p><p>The capture file appears to be damaged or corrupt. (pcap: File has 1313056966-byte packet, bigger than maximum of 65535), Is there a work around so I can view the entire file ?</p><p>Thanks Ian</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-corrupt" rel="tag" title="see questions tagged &#39;corrupt&#39;">corrupt</span> <span class="post-tag tag-link-damaged" rel="tag" title="see questions tagged &#39;damaged&#39;">damaged</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Aug '11, 11:41</strong></p><img src="https://secure.gravatar.com/avatar/8a07219d38d20f5fce43ba56ec8823f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sehguh&#39;s gravatar image" /><p><span>sehguh</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sehguh has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Feb '12, 19:10</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-5924" class="comments-container"><span id="10414"></span><div id="comment-10414" class="comment"><div id="post-10414-score" class="comment-score"></div><div class="comment-text"><p>I too is facing this problem.</p><p>Running Wireshark 1.6.7, WinPcap 4.1.2 on Windows 7 x64 intel PRO/1000 PM nic. I capture using tshark with this string: "C:\Program Files\Wireshark\tshark" -a duration:60 -B 2 -i 1 -n -q -w D:\wireshark\ny_c\udfald\capture.pcap</p><p>When opening the capture.pcap file (on the same machine, no ftp transfers!) I get the following error: The capture file appears to be damaged or corrupt. (pcap: File has 39931111361-byte packet, bigger than maximum of 65535)</p><p>I click "OK" and the file opens just fine. I filter the file using "frame.len &gt; 1514" and there is nothing?! Should I expect to see the 39931111361-byte packet, or not?</p><p>Regards Anders</p></div><div id="comment-10414-info" class="comment-info"><span class="comment-age">(24 Apr '12, 02:23)</span> <span class="comment-user userinfo">Smakodak</span></div></div><span id="10429"></span><div id="comment-10429" class="comment"><div id="post-10429-score" class="comment-score"></div><div class="comment-text"><p>Uploaded the file to <a href="http://f00l.de/pcapfix/.">http://f00l.de/pcapfix/.</a> Below is the last lines of the pcapfix report.</p><hr /><p>[+] Packet #19422 at position 9571953 (1335214033 | 262752 | 1514 | 1514). [-] Corrupted packet #19423 at position 9573483 (2985547892 | 1583189366 | 4270389735 | 4251964125). [*] Recovering... [-] FAILED! Unable to recover pcap file.</p><hr /><p>To be continuded...</p></div><div id="comment-10429-info" class="comment-info"><span class="comment-age">(25 Apr '12, 01:43)</span> <span class="comment-user userinfo">Smakodak</span></div></div><span id="10430"></span><div id="comment-10430" class="comment"><div id="post-10430-score" class="comment-score"></div><div class="comment-text"><p>In wireshark the last packet I can view, is #19422.</p><p>So the answer to my question is - No, I shouldn't expect to see the 39931111361-byte packet!</p><p>Been trying to use editcap, but had no luck. I tried to delete packet #19423, and to capture packet #1-19422. In both cases, I get this error message: : File contains a record that's not valid. (pcap: File has 4270389735-byte packet, bigger than maximum of 65535)</p></div><div id="comment-10430-info" class="comment-info"><span class="comment-age">(25 Apr '12, 01:43)</span> <span class="comment-user userinfo">Smakodak</span></div></div><span id="10436"></span><div id="comment-10436" class="comment"><div id="post-10436-score" class="comment-score"></div><div class="comment-text"><p>your pcapfix-output was very helpful for me... i improved the detection algorithm the tool is using... please try this version to repair your file... i hope it works this time...</p><p>ONLINE: <a href="http://f00l.de/hacking/pcapfix-0.4rc3.php">http://f00l.de/hacking/pcapfix-0.4rc3.php</a> OFFLINE: <a href="http://f00l.de/pcapfix/pcapfix-0.4rc3.tar.gz">http://f00l.de/pcapfix/pcapfix-0.4rc3.tar.gz</a></p></div><div id="comment-10436-info" class="comment-info"><span class="comment-age">(25 Apr '12, 07:09)</span> <span class="comment-user userinfo">creeq</span></div></div><span id="10456"></span><div id="comment-10456" class="comment"><div id="post-10456-score" class="comment-score"></div><div class="comment-text"><p>Thanks! That did it. These are the last lines of my repaired file:</p><p>""[+] POSSIBLE Packet #93952 at position 65590147 (1335214073 | 81395 | 66 | 66). [+] SUCCESS.</p><p>Your pcap file has been successfully repaired (49 corrupted packet(s)). Wrote 93952 packets to file fixed_phpUe2tRN.""</p><p>And it has helped me reveal my problem - Spanning-tree!</p><p>Thanks again:)</p></div><div id="comment-10456-info" class="comment-info"><span class="comment-age">(26 Apr '12, 01:20)</span> <span class="comment-user userinfo">Smakodak</span></div></div></div><div id="comment-tools-5924" class="comment-tools"></div><div class="clear"></div><div id="comment-5924-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="5932"></span>

<div id="answer-container-5932" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5932-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5932-score" class="post-score" title="current number of votes">2</div><span id="post-5932-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The usual cause of this error is the file being mangled by transferring it over FTP in ASCII mode instead of BINARY mode. If you did transfer the file by FTP, please transfer the file again, now using BINARY mode.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Aug '11, 16:08</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5932" class="comments-container"><span id="21203"></span><div id="comment-21203" class="comment"><div id="post-21203-score" class="comment-score"></div><div class="comment-text"><p>my file was names .txt and file size got changed during transfer. Renamed it to pcap and wollla :)</p></div><div id="comment-21203-info" class="comment-info"><span class="comment-age">(16 May '13, 23:38)</span> <span class="comment-user userinfo">imdeepakg</span></div></div><span id="21206"></span><div id="comment-21206" class="comment"><div id="post-21206-score" class="comment-score"></div><div class="comment-text"><p>Whatever program you used to transfer the file may have assumed that, because the file's name ended in <code>.txt</code>, it was a text file, and transferred in it a mode that didn't preserve its contents (instead perhaps converting LF to CR-LF or vice versa, if it was copying between Windows and UN*X).</p><p>Changing the name and copying it again may have caused the program to transfer it byte-by-byte rather than trying to convert between Windows and UN*X text file format.</p></div><div id="comment-21206-info" class="comment-info"><span class="comment-age">(17 May '13, 00:17)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-5932" class="comment-tools"></div><div class="clear"></div><div id="comment-5932-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10351"></span>

<div id="answer-container-10351" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10351-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10351-score" class="post-score" title="current number of votes">1</div><span id="post-10351-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>maybe you could use "pcapfix" ... it tries to repair broken / corrupted pcap files...</p><p><a href="http://f00l.de/pcapfix">http://f00l.de/pcapfix/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '12, 07:58</strong></p><img src="https://secure.gravatar.com/avatar/3bd81edc96c5877d644377567c344e6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="creeq&#39;s gravatar image" /><p><span>creeq</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="creeq has no accepted answers">0%</span></p></div></div><div id="comments-container-10351" class="comments-container"></div><div id="comment-tools-10351" class="comment-tools"></div><div class="clear"></div><div id="comment-10351-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5927"></span>

<div id="answer-container-5927" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5927-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5927-score" class="post-score" title="current number of votes">0</div><span id="post-5927-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately, no - if the file is corrupt, perhaps due to a Wireshark bug, there's no way to read past the bad packet. There <em>might</em> be a Wireshark bug when reading the packet; if you're not using the latest version of Wireshark (1.6.1, currently), try installing that and see whether it can read it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Aug '11, 13:55</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-5927" class="comments-container"></div><div id="comment-tools-5927" class="comment-tools"></div><div class="clear"></div><div id="comment-5927-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5931"></span>

<div id="answer-container-5931" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5931-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5931-score" class="post-score" title="current number of votes">0</div><span id="post-5931-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>... or you can use editcap to cut the capture into parts, which then can, or cannot be read.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Aug '11, 14:36</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-5931" class="comments-container"></div><div id="comment-tools-5931" class="comment-tools"></div><div class="clear"></div><div id="comment-5931-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

