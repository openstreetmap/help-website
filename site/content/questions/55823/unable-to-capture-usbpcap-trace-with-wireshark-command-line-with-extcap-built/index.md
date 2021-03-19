+++
type = "question"
title = "Unable to capture USBPCAP trace with Wireshark Command Line with extcap built."
description = '''.&#92;Wireshark.exe -i 3 -k -w a.pcap Using this command on Wireshark to capture USB traffic - .&#92;Wireshark.exe -i 8 -k -w a.pcap - throws an Error &quot;ERROR READING FROM PIPE:THIS OPERATION RETURNED BECAUSE THE TIMEOUT PERIOD EXPIRED (error 1460)&quot; Using Wireshark GUI - When double clicked on the Interface ...'''
date = "2016-09-26T04:13:00Z"
lastmod = "2016-09-27T13:57:00Z"
weight = 55823
keywords = [ "wireshark", "extcap", "usbpcap" ]
aliases = [ "/questions/55823" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to capture USBPCAP trace with Wireshark Command Line with extcap built.](/questions/55823/unable-to-capture-usbpcap-trace-with-wireshark-command-line-with-extcap-built)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55823-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55823-score" class="post-score" title="current number of votes">0</div><span id="post-55823-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><code>.\Wireshark.exe -i 3 -k -w a.pcap</code> Using this command on Wireshark to capture USB traffic - <code>.\Wireshark.exe -i 8 -k -w a.pcap</code> - throws an Error "ERROR READING FROM PIPE:THIS OPERATION RETURNED BECAUSE THE TIMEOUT PERIOD EXPIRED (error 1460)"</p><p>Using Wireshark GUI - When double clicked on the Interface name (USBPCAP3) the same error is observed using Wireshark GUI.</p><p>Only when i click on the extCap capture options i.e the round circular black button next to the interface, it asks to start the trace and on clicking start it works and captures the packets.</p><p>Please let me know as to how do i capture packets from USB using Wireshark Command Line.</p><p>Thanks Abhinand</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-extcap" rel="tag" title="see questions tagged &#39;extcap&#39;">extcap</span> <span class="post-tag tag-link-usbpcap" rel="tag" title="see questions tagged &#39;usbpcap&#39;">usbpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '16, 04:13</strong></p><img src="https://secure.gravatar.com/avatar/32e1bf16adec54806ef4591a2d304596?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="abhierao&#39;s gravatar image" /><p><span>abhierao</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="abhierao has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Sep '16, 05:05</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-55823" class="comments-container"></div><div id="comment-tools-55823" class="comment-tools"></div><div class="clear"></div><div id="comment-55823-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="55844"></span>

<div id="answer-container-55844" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55844-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55844-score" class="post-score" title="current number of votes">1</div><span id="post-55844-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12846">bug 12846</a> which has been marked as resolved and fixed today, so we can expect the fix to become part of the next stable release.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '16, 08:03</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-55844" class="comments-container"><span id="55888"></span><div id="comment-55888" class="comment"><div id="post-55888-score" class="comment-score"></div><div class="comment-text"><p>I did raise a Bug also they did mark it as a duplicate of 12846 and provided me with a new exe, its working fine with the new version, thanks.</p><p>When used Tshark.exe -i 8 -w a.pcap - The same error returns this is probably a Bug which needs FIX.</p></div><div id="comment-55888-info" class="comment-info"><span class="comment-age">(26 Sep '16, 23:04)</span> <span class="comment-user userinfo">abhierao</span></div></div><span id="55889"></span><div id="comment-55889" class="comment"><div id="post-55889-score" class="comment-score"></div><div class="comment-text"><p>Download the new version from here to fix the above problem - <a href="https://www.wireshark.org/download/automated/win64/Wireshark-win64-2.3.0-850-g73a0ee0.exe">https://www.wireshark.org/download/automated/win64/Wireshark-win64-2.3.0-850-g73a0ee0.exe</a></p><p>NOTE : Tshark.exe -i 8 -w a.pcap - doesn't work with this build. Wireshark.exe command line works well. - Wireshark.exe -i 8 -k -w a.pcap</p><p>Thanks Abhinand</p></div><div id="comment-55889-info" class="comment-info"><span class="comment-age">(26 Sep '16, 23:08)</span> <span class="comment-user userinfo">abhierao</span></div></div><span id="55890"></span><div id="comment-55890" class="comment"><div id="post-55890-score" class="comment-score"></div><div class="comment-text"><p><span>@abhierao</span>, please provide the output of <code>tshark.exe -D</code>, because from just <code>-i 3</code> and <code>-i 8</code> it is not clear what interface types the 3 and 8 represent, so it is hard to say whether it is the same issue or a different one.</p></div><div id="comment-55890-info" class="comment-info"><span class="comment-age">(26 Sep '16, 23:12)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="55891"></span><div id="comment-55891" class="comment"><div id="post-55891-score" class="comment-score"></div><div class="comment-text"><p>Requested output:<br />
</p><pre><code>C:\Program Files\Wireshark&gt;tshark.exe -D

** (tshark.exe:3908): WARNING **: No such preference &quot;extcap.____usbpcap3.devices&quot; at line 367 of
C:\Users\sandisk\AppData\Roaming\Wireshark\preferences (save preferences to remove this warning)

** (tshark.exe:3908): WARNING **: No such preference &quot;extcap.____usbpcap1.devices&quot; at line 407 of
C:\Users\sandisk\AppData\Roaming\Wireshark\preferences (save preferences to remove this warning)
1. \Device\NPF_{9B098323-011F-469A-B256-FA2AA31034ED} (Bluetooth Network Connection)
2. \Device\NPF_{337CAB15-451E-434E-94D4-D691228A096C} (Wireless Network Connection 2)
3. \Device\NPF_{F647C413-A878-43BF-AF0F-BC848D6A1359} (Wireless Network Connection)
4. \Device\NPF_{CB16933C-1DCA-461B-A5B5-334D69669EAD} (Wireless Network Connection 3)
5. \Device\NPF_{B508384C-DAFC-4C50-B0A4-3C5C8C062864} (Local Area Connection)
6. \\.\USBPcap1 (USBPcap1)
7. \\.\USBPcap2 (USBPcap2)
8. \\.\USBPcap3 (USBPcap3)
9. cisco (Cisco remote capture)
10. randpkt (Random packet generator)
11. ssh (SSH remote capture)
12. udpdump (UDP Listener remote capture)

C:\Program Files\Wireshark&gt;tshark.exe -i 8 -w cmd.pcap

** (tshark.exe:1248): WARNING **: No such preference &quot;extcap.____usbpcap3.devices&quot; at line 367 of
C:\Users\sandisk\AppData\Roaming\Wireshark\preferences (save preferences to remove this warning)

** (tshark.exe:1248): WARNING **: No such preference &quot;extcap.____usbpcap1.devices&quot; at line 407 of
C:\Users\sandisk\AppData\Roaming\Wireshark\preferences (save preferences to remove this warning)
Capturing on &#39;USBPcap3&#39;
tshark: Error reading from pipe: This operation returned because the timeout period expired.
 (error 1460)

tshark: Error by extcap pipe: C:\Program Files\Wireshark\extcap\USBPcapCMD.exe: --devices: option requires an option argument

C:\Program Files\Wireshark&gt;</code></pre></div><div id="comment-55891-info" class="comment-info"><span class="comment-age">(26 Sep '16, 23:47)</span> <span class="comment-user userinfo">abhierao</span></div></div><span id="55892"></span><div id="comment-55892" class="comment"><div id="post-55892-score" class="comment-score"></div><div class="comment-text"><ol><li>.\USBPcap3 (USBPcap3) - USB Drive is interface number 8 ; when given i = 3 i.e Wireless network it works without any problem</li></ol></div><div id="comment-55892-info" class="comment-info"><span class="comment-age">(26 Sep '16, 23:48)</span> <span class="comment-user userinfo">abhierao</span></div></div><span id="55893"></span><div id="comment-55893" class="comment not_top_scorer"><div id="post-55893-score" class="comment-score"></div><div class="comment-text"><p>OK, now it makes more sense to me. Assuming you observe this behaviour while using the snapshot version, please provide your output of <code>tshark.exe -i 8 -w cmd.pcap</code> as above as a comment to <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12846">bug 12846</a>, stating that it is obtained using the snapshot version (Wireshark-win64-2.3.0-850-g73a0ee0.exe) and that in that version the issue survives in tshark.</p><p>I'm afraid that when testing, Pascal may have saved the preferences while in Wireshark, effectively hiding the issue of tshark as both use the same preferences file.</p></div><div id="comment-55893-info" class="comment-info"><span class="comment-age">(27 Sep '16, 00:29)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-55844" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-55844-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="55934"></span>

<div id="answer-container-55934" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55934-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55934-score" class="post-score" title="current number of votes">1</div><span id="post-55934-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For reference, the issue with Wireshark GUI was tracked by <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12846">bug 12846</a> that was fixed on the 18th of September.</p><p>The issue with tshark was tracked by <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12949">bug 12949</a> and was fixed today.</p><p>Both will be part of Wireshark 2.2.1 once it is released.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Sep '16, 13:57</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span> </br></p></div></div><div id="comments-container-55934" class="comments-container"></div><div id="comment-tools-55934" class="comment-tools"></div><div class="clear"></div><div id="comment-55934-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

