+++
type = "question"
title = "wireshark not able to launch - stuck at &quot;finding local interfaces&quot;"
description = '''Hello Forum, I have recently been provided with windows 10 laptop, however, I am facing issue with running wireshark, and openning pcap files. When I launch wireshark, it gets stuck with &quot;Finding Local Interfaces&quot;. I am a bit surprised from google results as it looks like no one is facing this issue...'''
date = "2016-11-28T23:53:00Z"
lastmod = "2018-02-02T02:43:00Z"
weight = 57688
keywords = [ "interface", "finding", "local", "windows10", "stuck" ]
aliases = [ "/questions/57688" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark not able to launch - stuck at "finding local interfaces"](/questions/57688/wireshark-not-able-to-launch-stuck-at-finding-local-interfaces)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57688-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Forum,</p><p>I have recently been provided with windows 10 laptop, however, I am facing issue with running wireshark, and openning pcap files. When I launch wireshark, it gets stuck with "Finding Local Interfaces".</p><p>I am a bit surprised from google results as it looks like no one is facing this issue ..</p><p>Please advise, as I am stuck with windows 10, and I use wireshark quite often ..</p><p>Waiting for your responses :)</p><p>Best Regards, Ala</p></div><div id="question-tags" class="tags-container tags">interface finding local windows10 stuck</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Nov '16, 23:53</strong></p><img src="https://secure.gravatar.com/avatar/6a909b7d4780a3f7cfe51206b58d0569?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ala-Shehadeh&#39;s gravatar image" /><p>Ala-Shehadeh<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ala-Shehadeh has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Nov '16, 19:18</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-57688" class="comments-container"><span id="57689"></span><div id="comment-57689" class="comment"><div id="post-57689-score" class="comment-score"></div><div class="comment-text"><p>Hi Ala, I experienced the very same issue after opening trace files from Steelcentral Packet Analyzer (right click a file and choose "open in Wireshark"). Don't know if the problem was related to the files being opened from Packet Analyzer, but a restart fixed the issue for me.</p><p>I also believe I experienced the same when a network interface card was added or removed while Wireshark was running on my computer.</p></div><div id="comment-57689-info" class="comment-info"><span class="comment-age">(29 Nov '16, 00:43)</span> www_wireshar...</div></div><span id="57752"></span><div id="comment-57752" class="comment"><div id="post-57752-score" class="comment-score"></div><div class="comment-text"><p>I too see this problem. I already restarted several times, I uninstalled Wireshark and reinstalled the latest version to no effect. Wireshark shows the load screen untill "Finding local interfaces" and is just stuck there unresponding. The legacy version shows the same effect.<br />
I work with windows 10 64-bit.</p></div><div id="comment-57752-info" class="comment-info"><span class="comment-age">(01 Dec '16, 05:51)</span> cloidnerux</div></div><span id="57755"></span><div id="comment-57755" class="comment"><div id="post-57755-score" class="comment-score"></div><div class="comment-text"><p>Please post the contents of the Wireshark -&gt; Help -&gt; About Wireshark dialog, in particular the Wireshark and Plugins tabs.</p></div><div id="comment-57755-info" class="comment-info"><span class="comment-age">(01 Dec '16, 07:04)</span> grahamb ♦</div></div><span id="57756"></span><div id="comment-57756" class="comment"><div id="post-57756-score" class="comment-score"></div><div class="comment-text"><p>I am unable to access this information, as wireshark is stuck on startup. But this is a fresh standard installation of the latest wireshark 64-bit version.<br />
Here is a screenshot: <a href="http://i.imgur.com/RDbSBrl.png">http://i.imgur.com/RDbSBrl.png</a></p></div><div id="comment-57756-info" class="comment-info"><span class="comment-age">(01 Dec '16, 07:09)</span> cloidnerux</div></div><span id="57757"></span><div id="comment-57757" class="comment"><div id="post-57757-score" class="comment-score"></div><div class="comment-text"><p>Ah, I didn't think that through.</p></div><div id="comment-57757-info" class="comment-info"><span class="comment-age">(01 Dec '16, 07:16)</span> grahamb ♦</div></div><span id="57758"></span><div id="comment-57758" class="comment not_top_scorer"><div id="post-57758-score" class="comment-score"></div><div class="comment-text"><p>In the install did you enable any of the "dump" tools in the "Tools section, e.g. Androiddump, SSHdump, UDPdump, Randpktdump, or install USBPcap?</p><p>You can re-run the install to check.</p></div><div id="comment-57758-info" class="comment-info"><span class="comment-age">(01 Dec '16, 07:39)</span> grahamb ♦</div></div><span id="60235"></span><div id="comment-60235" class="comment not_top_scorer"><div id="post-60235-score" class="comment-score"></div><div class="comment-text"><p>This isn't an answer, but another report of the same behavior. Fresh installation of wireshark &amp; all related libraries (libpcap and the USB one) on windows10 -- Locks up on "finding local interfaces" exactly as in the screenshot by cloidnerux [except english language version].</p><p>Thanks!</p></div><div id="comment-60235-info" class="comment-info"><span class="comment-age">(21 Mar '17, 12:58)</span> mattaltieri</div></div><span id="60254"></span><div id="comment-60254" class="comment not_top_scorer"><div id="post-60254-score" class="comment-score"></div><div class="comment-text"><p>Can you try uninstalling USBCap?</p></div><div id="comment-60254-info" class="comment-info"><span class="comment-age">(22 Mar '17, 03:27)</span> grahamb ♦</div></div></div><div id="comment-tools-57688" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-57688-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="58220"></span>

<div id="answer-container-58220" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58220-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I had the same issue and for me worked a downgrade to version 2.0.3</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Dec '16, 01:15</strong></p><img src="https://secure.gravatar.com/avatar/92f0e934c5b2012a775665074d7a32e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pati1990&#39;s gravatar image" /><p>pati1990<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pati1990 has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-58220" class="comments-container"></div><div id="comment-tools-58220" class="comment-tools"></div><div class="clear"></div><div id="comment-58220-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="64337"></span>

<div id="answer-container-64337" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64337-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks for the answer 2.0.3 works fine for me, I had the same issue with 2.4.4 and 2.2.12 but 2.0.3 is working fine.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Feb '18, 02:43</strong></p><img src="https://secure.gravatar.com/avatar/baceef154bcf13cabe1498ac7598b962?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="worto03&#39;s gravatar image" /><p>worto03<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="worto03 has no accepted answers">0%</span></p></div></div><div id="comments-container-64337" class="comments-container"></div><div id="comment-tools-64337" class="comment-tools"></div><div class="clear"></div><div id="comment-64337-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

