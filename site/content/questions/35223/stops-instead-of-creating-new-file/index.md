+++
type = "question"
title = "stops instead of creating new file"
description = '''Hi, I have a script I made that is run on 4 pcs every day for 8 hours and saved to a mapped shared drive (edited only for the folder location on the share to differentiate them).  2 PCS this thing runs fine on, the other 2 pcs T shark stops at 200MB and doesn&#x27;t create a new file. At the end of the d...'''
date = "2014-08-05T08:39:00Z"
lastmod = "2014-08-05T08:45:00Z"
weight = 35223
keywords = [ "new", "create", "doesnt", "tshark", "script" ]
aliases = [ "/questions/35223" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [stops instead of creating new file](/questions/35223/stops-instead-of-creating-new-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35223-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a script I made that is run on 4 pcs every day for 8 hours and saved to a mapped shared drive (edited only for the folder location on the share to differentiate them).</p><p>2 PCS this thing runs fine on, the other 2 pcs T shark stops at 200MB and doesn't create a new file. At the end of the day two PCS have generated 5GB worth of 200MB files which is what I want, while the other 2... 200MB. This is the script. "C:\Program Files\Wireshark\tshark.exe" -i 1 -a duration:28800 -a filesize:20480 -a files:512 -w "M:\Departments\tcs\Issue Log-Proclarity\Desktop\test\%dt%.pcap"</p></div><div id="question-tags" class="tags-container tags">new create doesnt tshark script</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '14, 08:39</strong></p><img src="https://secure.gravatar.com/avatar/d3a12bd72c531357ff1d67facef58c77?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="weeksa&#39;s gravatar image" /><p>weeksa<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="weeksa has no accepted answers">0%</span></p></div></div><div id="comments-container-35223" class="comments-container"></div><div id="comment-tools-35223" class="comment-tools"></div><div class="clear"></div><div id="comment-35223-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35224"></span>

<div id="answer-container-35224" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35224-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Don't use tshark, use dumpcap. tshark (and wireshark) store state for reassembly and at some point WILL run out of memory regardless of how many capture files you create, and are not designed for long-term capture.</p><p>Also saving to a shared drive probably isn't the greatest idea, as a) it is much slower than a local drive (which might not be an issue if your traffic being captured is minimal) and b) might fail if the network connection to the mapped drive is lost.</p><p>If you explained what you are trying to achieve then we might be able to offer a better solution.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '14, 08:45</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-35224" class="comments-container"><span id="35226"></span><div id="comment-35226" class="comment"><div id="post-35226-score" class="comment-score"></div><div class="comment-text"><p>What's dumpcap?</p><p>Sorry, I'm new to this and just learnt the script. I was thrown into a project where they want to monitor the network on these 4 pcs and then check logs to see differences and spot an apparent slowness issue with one application we use. Because of that, that shared drive was setup.</p><p>So what I did was learn how to create a batch file (the one above - "C:\Program Files\Wireshark\tshark.exe" -i 1 -a duration:28800 -a filesize:20480 -a files:512 -w "M:\Departments\tcs\Issue Log-Proclarity\Desktop\test\%dt%.pcap"</p><p>and from there made a vbscript to make that run in the background (so the users won't accidentally close it) - Set WshShell = CreateObject("WScript.Shell") WshShell.Run chr(34) &amp; "C:\script\wshark.bat" &amp; Chr(34), 0 Set WshShell = Nothing</p><p>and from there created a Monday-Friday windows task to launch the script at 9am. It works flawlessly on two pcs. The other two I set the filesize higher since it won't re-generate the new file. So every 2GB I go to those PCs and manually run the script.</p></div><div id="comment-35226-info" class="comment-info"><span class="comment-age">(05 Aug '14, 09:05)</span> weeksa</div></div><span id="35227"></span><div id="comment-35227" class="comment"><div id="post-35227-score" class="comment-score"></div><div class="comment-text"><p>dumpcap is a component of the wireshark suite that actually handles the capturing tasks. tshark and Wireshark run dumpcap to capture traffic. See the dumpcap man page <a href="http://www.wireshark.org/docs/man-pages/dumpcap.html">here</a>.</p><p>Is it possible there are quota limits for the users on the machines that don't work?</p></div><div id="comment-35227-info" class="comment-info"><span class="comment-age">(05 Aug '14, 09:18)</span> grahamb ♦</div></div><span id="35229"></span><div id="comment-35229" class="comment"><div id="post-35229-score" class="comment-score"></div><div class="comment-text"><p>How would I find out if there is a quota limit? to the best of my knowledge there is nothing stopping this, especially because increasing the filesize from 200MB to 4GB yields one giant 2GB file... They never go past 2GB</p></div><div id="comment-35229-info" class="comment-info"><span class="comment-age">(05 Aug '14, 10:16)</span> weeksa</div></div></div><div id="comment-tools-35224" class="comment-tools"></div><div class="clear"></div><div id="comment-35224-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

