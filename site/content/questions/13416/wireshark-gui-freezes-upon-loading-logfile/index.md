+++
type = "question"
title = "wireshark gui freezes upon loading logfile"
description = '''I am having difficulty opening a series of files created by tshark.exe. It is rather large, but I have opened large files before without a problem. The loading is even done in a separate thread so I can see the progress of it in the GUI. This is the info from capsinfos.exe about the file in question...'''
date = "2012-08-06T23:33:00Z"
lastmod = "2012-08-07T04:20:00Z"
weight = 13416
keywords = [ "gui", "logfile", "freeze" ]
aliases = [ "/questions/13416" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark gui freezes upon loading logfile](/questions/13416/wireshark-gui-freezes-upon-loading-logfile)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13416-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am having difficulty opening a series of files created by tshark.exe. It is rather large, but I have opened large files before without a problem. The loading is even done in a separate thread so I can see the progress of it in the GUI.</p><p>This is the info from capsinfos.exe about the file in question:</p><pre><code>File type:           Wireshark - pcapng
File encapsulation:  Ethernet
Packet size limit:   file hdr: (not set)
Number of packets:   907544
File size:           146040212 bytes
Data size:           115427911 bytes
Capture duration:    86397 seconds
Start time:          Sat Aug 04 22:07:38 2012
End time:            Sun Aug 05 22:07:35 2012
Data byte rate:      1336.02 bytes/sec
Data bit rate:       10688.14 bits/sec
Average packet size: 127.19 bytes
Average packet rate: 10.50 packets/sec
SHA1:                074c2dbbfa65835f8cb6deb595ee6face9159ed9
RIPEMD160:           d7f963a411ae8d37c83b07fe660a11163a11bc57
MD5:                 612aac26fa3c140bd182ad44ae8836bd
Strict time order:   False</code></pre>This is one example in a series of files I am generating on a 24 hour rotation. Any suggestions how I might get these files opened?</div><div id="question-tags" class="tags-container tags">gui logfile freeze</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Aug '12, 23:33</strong></p><img src="https://secure.gravatar.com/avatar/822c402217458d571a8cb1ed4dfad78e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="namreeb&#39;s gravatar image" /><p>namreeb<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="namreeb has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Aug '12, 02:26</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-13416" class="comments-container"></div><div id="comment-tools-13416" class="comment-tools"></div><div class="clear"></div><div id="comment-13416-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="13418"></span>

<div id="answer-container-13418" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13418-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark collects (possibly an awful) lot of state while loading a capture. It's impossible to tell how much beforehand. That could lead to problems. Another option is that you've hit upon a dissection bug.</p><p>Anyway, to work around these use editcap to slice your capture in two and try to load each separately. This may show which part contains the cause. Maybe repeat the slicing even further. You can also load a file set if you need packets from multiple slices. Experiment a bit and see what it tells you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Aug '12, 02:31</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-13418" class="comments-container"></div><div id="comment-tools-13418" class="comment-tools"></div><div class="clear"></div><div id="comment-13418-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13421"></span>

<div id="answer-container-13421" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13421-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>File size: 146040212 bytes</p></blockquote><p>146 MByte is not really a large capture file for a "decent" system. If your system has &gt;= 2 GByte RAM, you "should" be able to open that file, expect you are running into a bug.</p><p>Somme suggestions:</p><ol><li>Please try to open the file with different versions of Wireshark (1.6, 1.8).</li><li>Please check if there are some time consuming options enabled (like "Name Resoultion"). <code>Edit -&gt; Preferences -&gt; Name Resolution</code>. Disable all "name resolution" options, then try again to open the file.</li><li>Try to open the file with tshark. Does it freeze?</li></ol><p>Regards Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Aug '12, 04:20</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Aug '12, 05:14</p></div></div><div id="comments-container-13421" class="comments-container"><span id="13422"></span><div id="comment-13422" class="comment"><div id="post-13422-score" class="comment-score"></div><div class="comment-text"><p>I have 16Gb of RAM on both systems that I used to try opening the file. I have opened other, larger files without any problems. I did use editcap.exe to split the file into 100,000 packet files which makes them 13-15Mb and had the exact same problem. If I try and open a log file from a previous week, which was generated on the same system with (I think) the exact same tshark.exe syntax, it works fine!</p></div><div id="comment-13422-info" class="comment-info"><span class="comment-age">(07 Aug '12, 05:52)</span> namreeb</div></div><span id="13423"></span><div id="comment-13423" class="comment"><div id="post-13423-score" class="comment-score"></div><div class="comment-text"><p>Some more questions:</p><ol><li>did you check the "Name Resolution" options?</li><li>does Wireshark freeze "instantly" at a certain point (e.g. after loading 10% of the file), or will it gradually slow down during the load process until it freezes?</li><li>did you install anything on your system lately (please double check!)</li><li>what is your wireshark version (wireshark -v)?</li><li>what is your OS (and version) of the system running Wireshark?</li></ol></div><div id="comment-13423-info" class="comment-info"><span class="comment-age">(07 Aug '12, 06:21)</span> Kurt Knochner ♦</div></div><span id="13440"></span><div id="comment-13440" class="comment"><div id="post-13440-score" class="comment-score"></div><div class="comment-text"><ol><li>Yes, I tried the Name Resolution suggestion with no effect.</li><li>Yes, Wireshark freezes instantly. The "Open File" dialog does not even go away.</li><li>Well again this is happening on both systems I tried it on, so I don't think it is an issue with my system, but on one of them I did recently install .NET Reflector.</li><li>My Wireshark version is 1.8.1 rev 43946. My local computer here which is not the system these logs were recorded on, but is the one I have been spending the most time to try and open them, is Windows 7 Ultimate x64 with all Windows Updates installed.</li></ol></div><div id="comment-13440-info" class="comment-info"><span class="comment-age">(07 Aug '12, 12:52)</span> namreeb</div></div><span id="13444"></span><div id="comment-13444" class="comment"><div id="post-13444-score" class="comment-score"></div><div class="comment-text"><blockquote><p>2.Yes, Wireshark freezes instantly. The "Open File" dialog does not even go away.</p></blockquote><p>sounds like a bug. By any chance: Is there HSRP traffic in the capture file (<a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7581">Bug 7581</a>)?</p><p>Some more questions:</p><ul><li>Did you try other Wireshark versions (1.6.9)?</li><li>Do you load the files from a share? If so, please try from a local path.</li></ul></div><div id="comment-13444-info" class="comment-info"><span class="comment-age">(07 Aug '12, 17:18)</span> Kurt Knochner ♦</div></div><span id="13448"></span><div id="comment-13448" class="comment"><div id="post-13448-score" class="comment-score"></div><div class="comment-text"><p>No, it should be strictly MySQL traffic in the capture. But it is on port 3307 rather than 3306 and at the time of loading I have not yet told it to analyze the traffic as MySQL.</p><p>No, the files are not being loaded from a share.</p><p>I downloaded Wireshark 1.6.9 and was unable to load it due to a missing "libxml2-2.dll". I downloaded 1.4.14 (rev 43964) and it loads! Should I report this on the bug tracker? I can provide my traffic dump if it will be limited to the developer(s).</p></div><div id="comment-13448-info" class="comment-info"><span class="comment-age">(07 Aug '12, 19:40)</span> namreeb</div></div><span id="13452"></span><div id="comment-13452" class="comment not_top_scorer"><div id="post-13452-score" class="comment-score"></div><div class="comment-text"><p>O.K. this sounds like a bug.</p><blockquote><p>Should I report this on the bug tracker?</p></blockquote><p>yes please.</p><blockquote><p>I can provide my traffic dump if it will be limited to the developer(s).</p></blockquote><p>You can mark the file as private during upload.</p><blockquote><p>But it is on port 3307 rather than 3306</p></blockquote><p>Does it fail to load any (mysql) capture file, or just your mysqsl traffic on port 3307?</p><p>Can you please try this short mysql sample?</p><blockquote><p><code>http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=view&amp;target=mysql_complete.pcap</code></p></blockquote></div><div id="comment-13452-info" class="comment-info"><span class="comment-age">(08 Aug '12, 01:28)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-13421" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-13421-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

