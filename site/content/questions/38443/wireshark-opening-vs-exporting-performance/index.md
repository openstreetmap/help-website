+++
type = "question"
title = "Wireshark opening vs exporting performance"
description = '''Hi, In wireshark opening a pcap and displaying some IE is much faster than exporting the very same info.  What is the difference? Tshark export is also slow. Thanks PeterK'''
date = "2014-12-08T08:26:00Z"
lastmod = "2014-12-09T07:12:00Z"
weight = 38443
keywords = [ "performance", "export", "wireshark" ]
aliases = [ "/questions/38443" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark opening vs exporting performance](/questions/38443/wireshark-opening-vs-exporting-performance)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38443-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>In wireshark opening a pcap and displaying some IE is much faster than exporting the very same info. What is the difference? Tshark export is also slow.</p><p>Thanks PeterK</p></div><div id="question-tags" class="tags-container tags">performance export wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Dec '14, 08:26</strong></p><img src="https://secure.gravatar.com/avatar/d7a0b0243086b78ddd5ff6626e729976?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PeterK&#39;s gravatar image" /><p>PeterK<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PeterK has no accepted answers">0%</span></p></div></div><div id="comments-container-38443" class="comments-container"><span id="38448"></span><div id="comment-38448" class="comment"><div id="post-38448-score" class="comment-score"></div><div class="comment-text"><p>some questions:</p><ul><li>what is your OS and OS version</li><li>what is you Wireshark version</li><li>do you read/write from/to a local file system or a network share</li><li>how do you define "much faster"?</li><li>can you provice a sample capture file that shows that effect</li></ul></div><div id="comment-38448-info" class="comment-info"><span class="comment-age">(08 Dec '14, 11:20)</span> Kurt Knochner ♦</div></div><span id="38462"></span><div id="comment-38462" class="comment"><div id="post-38462-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>The following config is used: -Windows Server 2003 R2 Enterprise x64 SP2 -WS 1.12.0 (v1.12.0-0-g4fab41a from master-1.12) -Everything is processed locally -Opening in Wireshark takes 10 sec, exporting/tshark takes 60 sec -It is LTE S1 capture and unfortunatelly not authorised to share it publicly</p><p>I think the 1:6 speed difference is interesting. What I noticed that exporting/Tshark does not care how many IE gets exported, 1 or 100 it is the same speed. The Tshark command line is like this:</p><p>tshark.exe -n -r "s1_pcap" -2 -d sctp.ppi==18,s1ap -R "s1ap" -e frame.time_epoch -e ip.src -e ip.dst -e s1ap.procedureCode -e s1ap.tAC -e s1ap.cell_ID ...<br />
-T fields -E separator=/t -E quote=n -E header=y -E occurrence=a &gt;"s1_csv"</p><p>Thank you, Peter</p></div><div id="comment-38462-info" class="comment-info"><span class="comment-age">(09 Dec '14, 00:18)</span> PeterK</div></div><span id="38464"></span><div id="comment-38464" class="comment"><div id="post-38464-score" class="comment-score"></div><div class="comment-text"><p>If Wireshark is all ready started all the initialasions are allready done. Tshark has to do that before starting to read the file. How long does it take Wireshark to load the file if you start it from the command line? wireshark.exe "s1_pcap" or wireshark.exe -R "s1ap"</p></div><div id="comment-38464-info" class="comment-info"><span class="comment-age">(09 Dec '14, 00:41)</span> Anders ♦</div></div><span id="38487"></span><div id="comment-38487" class="comment"><div id="post-38487-score" class="comment-score"></div><div class="comment-text"><p>Hi Anders,</p><p>In fact it is the same time, becuase I am opening the capture via extension assocation, so Wireshark starts from scratch. Just realised that talking about pcapng not pcap if that makes any difference...</p><p>Best regards, Peter</p></div><div id="comment-38487-info" class="comment-info"><span class="comment-age">(09 Dec '14, 06:41)</span> PeterK</div></div><span id="38492"></span><div id="comment-38492" class="comment"><div id="post-38492-score" class="comment-score"></div><div class="comment-text"><p>Then it might be the filtering, try starting WS from the command line with the filter...</p></div><div id="comment-38492-info" class="comment-info"><span class="comment-age">(09 Dec '14, 07:19)</span> Anders ♦</div></div></div><div id="comment-tools-38443" class="comment-tools"></div><div class="clear"></div><div id="comment-38443-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38490"></span>

<div id="answer-container-38490" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38490-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>realised that talking about pcapng not pcap if that makes any difference.</p></blockquote><p>It probably makes a difference. pcapng files are compressed while pcap is not.</p><p>My experience is, that reading a compressed file (not necessarily pcapng) is usually way faster than writing/creating a compressed file, especially if the files are large enough the experience any delay.</p><p>I'm not sure if that's the same for all compression algortihms, but it's certainly true for some of them.</p><p>My test with 7-Zip shows a factor of ~3 between compression (13 seconds) and decompression (4 seconds) of the same file. The test was repeated several times to eliminate file system caching.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Dec '14, 07:12</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Dec '14, 07:14</p></div></div><div id="comments-container-38490" class="comments-container"><span id="38491"></span><div id="comment-38491" class="comment"><div id="post-38491-score" class="comment-score"></div><div class="comment-text"><p>Pcap-ng files are not compressed by default.</p></div><div id="comment-38491-info" class="comment-info"><span class="comment-age">(09 Dec '14, 07:17)</span> Anders ♦</div></div><span id="38493"></span><div id="comment-38493" class="comment"><div id="post-38493-score" class="comment-score"></div><div class="comment-text"><p>I thought they were, but you are right, they are not.</p><p>Strange, who/what planted that idea into my mind?</p></div><div id="comment-38493-info" class="comment-info"><span class="comment-age">(09 Dec '14, 07:38)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-38490" class="comment-tools"></div><div class="clear"></div><div id="comment-38490-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

