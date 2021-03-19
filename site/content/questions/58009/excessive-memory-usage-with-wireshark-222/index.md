+++
type = "question"
title = "Excessive memory usage with Wireshark 2.2.2"
description = '''Hi, I recently upgraded my Wireshark from 1.x to 2.2.2 and noticed that the memory usage on Wireshark is excessively high. For example, I have a 2MB capture file and when I opened it in 2.2.2, it used almost 500MB of RAM. If I open the same file on 1.x, the memory was about 128MB. Has anybody seen s...'''
date = "2016-12-11T19:36:00Z"
lastmod = "2017-06-15T12:10:00Z"
weight = 58009
keywords = [ "excessive", "memory" ]
aliases = [ "/questions/58009" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Excessive memory usage with Wireshark 2.2.2](/questions/58009/excessive-memory-usage-with-wireshark-222)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58009-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I recently upgraded my Wireshark from 1.x to 2.2.2 and noticed that the memory usage on Wireshark is excessively high. For example, I have a 2MB capture file and when I opened it in 2.2.2, it used almost 500MB of RAM. If I open the same file on 1.x, the memory was about 128MB.</p><p>Has anybody seen something like this before?</p><p>Thanks,</p><p>Blanco</p></div><div id="question-tags" class="tags-container tags">excessive memory</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Dec '16, 19:36</strong></p><img src="https://secure.gravatar.com/avatar/d89b3d51dbe502fa1b291c0bcd6a805c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="blam008&#39;s gravatar image" /><p>blam008<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="blam008 has no accepted answers">0%</span></p></div></div><div id="comments-container-58009" class="comments-container"><span id="58012"></span><div id="comment-58012" class="comment"><div id="post-58012-score" class="comment-score"></div><div class="comment-text"><p>On what OS are you running Wireshark?</p><p>Can you try this with the "legacy" version of 2.2.2? That might determine whether it's an issue with the 2.2.2 dissector core or with the Qt user interface (the "legacy" version uses the GTK+ UI but uses the exact same dissector core as the Qt version).</p></div><div id="comment-58012-info" class="comment-info"><span class="comment-age">(12 Dec '16, 01:41)</span> Guy Harris ♦♦</div></div><span id="58014"></span><div id="comment-58014" class="comment"><div id="post-58014-score" class="comment-score"></div><div class="comment-text"><p>Can you share the capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive, DropBox etc.?</p></div><div id="comment-58014-info" class="comment-info"><span class="comment-age">(12 Dec '16, 02:25)</span> grahamb ♦</div></div><span id="58015"></span><div id="comment-58015" class="comment"><div id="post-58015-score" class="comment-score"></div><div class="comment-text"><p>@Guy - I'm using this Win7 SP1 and I also tried the legacy version of 2.2.2 with the same result.</p><p>@grahamb - here's the link to the packet capture</p><p><a href="https://www.dropbox.com/s/3z7wariqjl7bf52/CFE_lan0_0_2016-12-11-23-33-36.cap0?dl=0">https://www.dropbox.com/s/3z7wariqjl7bf52/CFE_lan0_0_2016-12-11-23-33-36.cap0?dl=0</a></p><p>Thanks!</p></div><div id="comment-58015-info" class="comment-info"><span class="comment-age">(12 Dec '16, 03:42)</span> blam008</div></div></div><div id="comment-tools-58009" class="comment-tools"></div><div class="clear"></div><div id="comment-58009-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="58040"></span>

<div id="answer-container-58040" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58040-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Or it could be related to a preference setting. To confirm this, you could make a backup of your personal configuration folder (location found in Help -&gt; About Wireshark -&gt; Folders), empty it and restart Wireshark (it will take the default settings).</p><p>If it changes the behavior, then we could investigate which setting is impacting, and whether it is expected or not. For example, are you doing some TLS decryption? If yes, what's the memory usage if you remove the keys?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Dec '16, 05:11</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-58040" class="comments-container"><span id="58046"></span><div id="comment-58046" class="comment"><div id="post-58046-score" class="comment-score"></div><div class="comment-text"><p>Bingo! Perfect Pascal, it was indeed the pre-master log file for SSL that was causing the issue. The log file I had was 24MB and that triggered this problem. Once I remove that, memory usage went back to normal.<br />
</p><p>Thank you all for your help!</p><p>Blanco</p></div><div id="comment-58046-info" class="comment-info"><span class="comment-age">(13 Dec '16, 06:34)</span> blam008</div></div></div><div id="comment-tools-58040" class="comment-tools"></div><div class="clear"></div><div id="comment-58040-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="58019"></span>

<div id="answer-container-58019" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58019-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Using your capture file and Wireshark portable <a href="https://1.eu.dl.wireshark.org/win32/all-versions/WiresharkPortable-1.12.13.paf.exe">1.12.13</a> and <a href="https://1.eu.dl.wireshark.org/win32/all-versions/WiresharkPortable_2.2.2.paf.exe">2.2.2</a>, and checking the working set using Process Explorer I see a very small difference in the size before and after loading the capture:</p><ul><li>1.12.13, before 84 MB, after 88 MB</li><li>2.2.2, before 86 MB, after 92 MB</li></ul><p>How did you determine the memory usage has increased? Did you compare before and after loading the file, and did you do anything else while the capture was loaded?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '16, 06:42</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Dec '16, 05:05</p></div></div><div id="comments-container-58019" class="comments-container"><span id="58038"></span><div id="comment-58038" class="comment"><div id="post-58038-score" class="comment-score"></div><div class="comment-text"><p>I tried the portable version as well for 2.2.2 and sure enough, the problem doesn't exist. Now I'm wondering whether the issue has to do with 64bit version vs the 32bit version. The installed version that I'm having trouble with is 64bit.</p><p>As for determining memory usage, I used Windows Task Manager | Processes. When I loaded 64bit Wireshark, it started off at about 58MB. When I opened the capture file, it jumped to around 500MB.</p></div><div id="comment-58038-info" class="comment-info"><span class="comment-age">(13 Dec '16, 04:25)</span> blam008</div></div><span id="58039"></span><div id="comment-58039" class="comment"><div id="post-58039-score" class="comment-score"></div><div class="comment-text"><p>Using a 64 bit build from master (2.3.0-rc) I see an increase (using Task Manager) from 65 MB to 71 MB when the file is opened.</p><p>Can you replicate the issue?</p></div><div id="comment-58039-info" class="comment-info"><span class="comment-age">(13 Dec '16, 05:09)</span> grahamb ♦</div></div></div><div id="comment-tools-58019" class="comment-tools"></div><div class="clear"></div><div id="comment-58019-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="62049"></span>

<div id="answer-container-62049" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62049-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I was having extreme memory consumption issues, and Wireshark was going into a "not responding" state regularly. As a test I started task manager (to watch memory usage) then started a wireshark capture on my laptop wired connection with nothing much going on.<br />
The capture lasted four minutes. During that time, only 6,000 packets were captured.<br />
But there were three occasions when Wireshark went "Not responding" during that time, and while "not responding" I could see the consumed memory ramping up rapidly.<br />
With the hints from blam008 and Pascal, I looked at Edit&gt;Prefernces&gt;Protocols&gt;SSL&gt;(pre)-master-secrets log file and found it pointed to d:\temp\sslkeylog.log.<br />
I found this file was large (122Mb) and locked by Chrome for significant periods of time. Thunderbird also uses it.<br />
I closed all applications which seemed to be using it, and renamed the file (hey - it is in \temp\ - what could possibly go wrong?)<br />
Now, I am able to leave Wireshark running for significant periods without it hanging and gobbling up memory. As far as I can see, nothing ever "trims" this log, so on a busy PC (and mine is) it is going to just keep growing, and it would appear that Wireshark does not like dealing with this, especially when other applications "hog" it for significant periods of time.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '17, 12:10</strong></p><img src="https://secure.gravatar.com/avatar/d9fa65a5118d05f8c5e773cfe7609ff9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="boatbodger&#39;s gravatar image" /><p>boatbodger<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="boatbodger has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Jun '17, 12:51</p></div></div><div id="comments-container-62049" class="comments-container"></div><div id="comment-tools-62049" class="comment-tools"></div><div class="clear"></div><div id="comment-62049-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

