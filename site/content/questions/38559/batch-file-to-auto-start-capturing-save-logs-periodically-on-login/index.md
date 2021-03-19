+++
type = "question"
title = "Batch file to auto-start capturing &amp; save logs periodically on login"
description = '''I’m hoping for assistance in configuring Wireshark (portable) to automatically open and start capturing when a user logs in, and to save the logs files at 30 minute intervals. We are trying to run Wireshark on 20 different PC’s to track the source of random network drops. But trying to start it dail...'''
date = "2014-12-14T10:25:00Z"
lastmod = "2014-12-14T14:06:00Z"
weight = 38559
keywords = [ "batch", "automate" ]
aliases = [ "/questions/38559" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Batch file to auto-start capturing & save logs periodically on login](/questions/38559/batch-file-to-auto-start-capturing-save-logs-periodically-on-login)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38559-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I’m hoping for assistance in configuring Wireshark (portable) to automatically open and start capturing when a user logs in, and to save the logs files at 30 minute intervals. We are trying to run Wireshark on 20 different PC’s to track the source of random network drops. But trying to start it daily and having the user not reboot before we save the captured files is cumbersome. I have found a few articles that discuss batch files, but never on how to create one for my exact needs.</p><p>Again, my goal is to:</p><ul><li>Start Wireshark when a user logins into a Windows 7 PC</li><li>Have the capture process start automatically</li><li>Have the log files saved to a specific directory at 30 minute intervals</li></ul><p>Our PC’s are running Windows 7 &amp; using Wireshark v1.12.1 (v1.12.1-0-g01b65bf from master-1.12)</p><p>Any help (examples) would be greatly appreciated.</p><p>Thank you….</p></div><div id="question-tags" class="tags-container tags">batch automate</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Dec '14, 10:25</strong></p><img src="https://secure.gravatar.com/avatar/8837001ae7e0f70e943fb9f6f913d70a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BobSwanson&#39;s gravatar image" /><p>BobSwanson<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BobSwanson has no accepted answers">0%</span></p></div></div><div id="comments-container-38559" class="comments-container"></div><div id="comment-tools-38559" class="comment-tools"></div><div class="clear"></div><div id="comment-38559-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38561"></span>

<div id="answer-container-38561" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38561-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><ol><li>Use dumpcap to make the captures, not Wireshark as that will run out of memory. See the <a href="https://www.wireshark.org/docs/man-pages/dumpcap.html">dumpcap</a> man page for the options. dumpcap is installed in the same directory as Wireshark.</li><li>To find out the interface number to use with the <code>-i</code> parameter use <code>dumpcap -D</code> to list the interfaces. Hopefully the interface number is the same on all machines.</li><li>dumpcap takes a number of options to create multiple capture files, for 30 minute files use the parameter <code>-b duration:1800</code>.</li><li>Use the <code>-w path\to directory\basefile.pcapng</code> parameter to specify the base filename, new files will be generated as <code>basename_nnnnn_date_and_time.pcapng</code>, where <code>nnnnn</code> is an incrementing number starting from 00001, and <code>date_and_time</code> is the dtate and time the file was created in YYYYMMDDHHMMSS format.</li><li>Create a batch file (i.e. makecap.bat) that contains the dumpcap command line, e.g. <code>path\to\dumpcap -i 1 -w path\to\basefile.pcapng -b duration:1800</code> and place it in the startup directory for each user, e.g. <code>%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup</code>.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '14, 14:06</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-38561" class="comments-container"><span id="38569"></span><div id="comment-38569" class="comment"><div id="post-38569-score" class="comment-score"></div><div class="comment-text"><p>grahamb - Thank you for this detailed example! We will work on this over the course of the next week or so and update this thread as to how it worked.</p></div><div id="comment-38569-info" class="comment-info"><span class="comment-age">(15 Dec '14, 06:31)</span> BobSwanson</div></div></div><div id="comment-tools-38561" class="comment-tools"></div><div class="clear"></div><div id="comment-38561-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

