+++
type = "question"
title = "Wireshark versions after 1.4.11 crash when running on Windows 7 32 bit"
description = '''I run Wireshark 1.4.11 on Windows 7 32 bit OS and works OK. I install any later version of Wireshark and installs OK and starts OK but after 5 or minutes it crashes and wants to close indicating Visual C++ error. I revert back to Wireshark 1.4.11 and it works reliably and stays open for ages without...'''
date = "2013-06-27T19:29:00Z"
lastmod = "2013-06-27T23:27:00Z"
weight = 22432
keywords = [ "visual", "crash", "c++" ]
aliases = [ "/questions/22432" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark versions after 1.4.11 crash when running on Windows 7 32 bit](/questions/22432/wireshark-versions-after-1411-crash-when-running-on-windows-7-32-bit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22432-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I run Wireshark 1.4.11 on Windows 7 32 bit OS and works OK.</p><p>I install any later version of Wireshark and installs OK and starts OK but after 5 or minutes it crashes and wants to close indicating Visual C++ error.</p><p>I revert back to Wireshark 1.4.11 and it works reliably and stays open for ages without any problems.</p><p>Today I tried Wireshark 1.10.o and also update WinPcap to 4.1.3. Again it all installs OK and Wireshark starts OK but after 5 or 10 minutes it crashes. I reverted back to Wireshark 1.4.11 and keeping WinPcap 4.1.3 and all works OK.</p><p>I have tried Wireshark versions win32-1.6.14, win32-1.8.4, win32-1.8.6, win32-1.9.2 and win32-1.10.0 and all install OK and crash after 5 or 10 minutes.</p></div><div id="question-tags" class="tags-container tags">visual crash c++</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jun '13, 19:29</strong></p><img src="https://secure.gravatar.com/avatar/c3d527531f237a48df662abeff58b2eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kleinschmidtmj&#39;s gravatar image" /><p>kleinschmidtmj<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kleinschmidtmj has no accepted answers">0%</span></p></div></div><div id="comments-container-22432" class="comments-container"></div><div id="comment-tools-22432" class="comment-tools"></div><div class="clear"></div><div id="comment-22432-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22433"></span>

<div id="answer-container-22433" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22433-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>A possible preference problem? When you upgraded, did you try to uninstall <em>everything</em>, including all user preferences too? You can save your preferences elsewhere first if you wish in order to narrow down which file/preference might be the cause.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '13, 19:56</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-22433" class="comments-container"><span id="22436"></span><div id="comment-22436" class="comment"><div id="post-22436-score" class="comment-score"></div><div class="comment-text"><p>I have unistalled Wireshark 1.4.11 and reinstalled Wireshark 1.10.0 and as suggested uninstalled the user preferences as well.</p><p>I should add that previously I was starting Wireshark and then running packet capture using default buffer settings and letting it run in the background. This was the same for all versions I indicated. I will re-test and post the results.</p></div><div id="comment-22436-info" class="comment-info"><span class="comment-age">(27 Jun '13, 22:30)</span> kleinschmidtmj</div></div><span id="22437"></span><div id="comment-22437" class="comment"><div id="post-22437-score" class="comment-score"></div><div class="comment-text"><p>Wireshark 1.10.0 still crashes once packet capture is started after 5 or 10 mins and this was after uninstalling everything.</p><p>I have reinstalled ver 1.4.11 and will re-test</p></div><div id="comment-22437-info" class="comment-info"><span class="comment-age">(27 Jun '13, 22:32)</span> kleinschmidtmj</div></div><span id="22438"></span><div id="comment-22438" class="comment"><div id="post-22438-score" class="comment-score"></div><div class="comment-text"><p>Wireshark version 1.4.11 is stable - sits there running packet capture for last 45 minutes without a crash</p></div><div id="comment-22438-info" class="comment-info"><span class="comment-age">(27 Jun '13, 22:50)</span> kleinschmidtmj</div></div></div><div id="comment-tools-22433" class="comment-tools"></div><div class="clear"></div><div id="comment-22433-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22439"></span>

<div id="answer-container-22439" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22439-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'd like to test whether it is a particular packet seen on your network that make newer versions crash. Could you run 1.4.11 for about 15 minutes (at least the time in which other versions would crash) and then save all the packets in a file. Then please install Wireshark 1.10 and load the file. Does it crash? If it does, are you able to share the file?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '13, 23:27</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-22439" class="comments-container"><span id="22626"></span><div id="comment-22626" class="comment"><div id="post-22626-score" class="comment-score"></div><div class="comment-text"><p>I have resolved my issue with Windows 8 (64bit)and Wireshark 1.10.0 running OK the last 30 minutes.</p><p>I am sorry I was not able to do the packet capture with vers 1.4.11 and then load in ver 1.10.0.</p></div><div id="comment-22626-info" class="comment-info"><span class="comment-age">(03 Jul '13, 17:34)</span> kleinschmidtmj</div></div><span id="22627"></span><div id="comment-22627" class="comment"><div id="post-22627-score" class="comment-score"></div><div class="comment-text"><p>I resolved my issue when I installed Windows 8 (64 bit). Wireshark 1.10.0 ben running perfectly.</p><p>Sorry but I was unable to run the packet capture using ver 1.4.11 and then load into ver 1.10.0 before I installed Windows 8.</p></div><div id="comment-22627-info" class="comment-info"><span class="comment-age">(03 Jul '13, 17:36)</span> kleinschmidtmj</div></div></div><div id="comment-tools-22439" class="comment-tools"></div><div class="clear"></div><div id="comment-22439-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

