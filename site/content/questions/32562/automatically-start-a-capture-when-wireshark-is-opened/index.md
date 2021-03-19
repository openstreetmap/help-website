+++
type = "question"
title = "Automatically Start a Capture When Wireshark is Opened"
description = '''TLDR; Is there a way to start a capture automatically upon opening Wireshark? I work with multiple windows 7 pcs where the people using them are constantly switching in and out. It is our protocol to have a user restart the machine when they begin their session. I&#x27;ve hosted a wireshark shortcut in t...'''
date = "2014-05-06T13:30:00Z"
lastmod = "2014-06-25T12:01:00Z"
weight = 32562
keywords = [ "start", "automatically", "capture" ]
aliases = [ "/questions/32562" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Automatically Start a Capture When Wireshark is Opened](/questions/32562/automatically-start-a-capture-when-wireshark-is-opened)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32562-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><strong>TLDR</strong>; Is there a way to start a capture automatically upon opening Wireshark?</p><p>I work with multiple windows 7 pcs where the people using them are constantly switching in and out. It is our protocol to have a user restart the machine when they begin their session.</p><p>I've hosted a wireshark shortcut in the startup folder so wireshark opens when the computer is booted on but it still requires the user to manually start the capture. Most of our users know to do this by habit but I'd like to remove this step by <strong>automatically starting a capture when Wireshark opens</strong>.</p><p>Is there some way to do this? Our pcs only have one interface option so there is not the concern they would capture the wrong interface.</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">start automatically capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 May '14, 13:30</strong></p><img src="https://secure.gravatar.com/avatar/7f1b38719761be6e0b29139a55683a8f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dude213&#39;s gravatar image" /><p>dude213<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dude213 has no accepted answers">0%</span></p></div></div><div id="comments-container-32562" class="comments-container"></div><div id="comment-tools-32562" class="comment-tools"></div><div class="clear"></div><div id="comment-32562-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="32563"></span>

<div id="answer-container-32563" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32563-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sure, just run Wireshark from a command prompt like this:</p><pre><code>wireshark -i interfaceid -k</code></pre><p>You can determine the interface ID by running "Wireshark -D" first.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 May '14, 13:44</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-32563" class="comments-container"><span id="34135"></span><div id="comment-34135" class="comment"><div id="post-34135-score" class="comment-score"></div><div class="comment-text"><p>How do you turn off the Display Options from the command line? I'm not using -S or -l and live capture/scrolling is displayed in WS.</p><p>I want to turn off the Display Options because it tends to utilize more PC resources and in some cases, WS will crash when running for a few days. Turning off the live display resolves the issue.</p><p>Also, is there a command line argument to minimize WS when you start it from the command line.</p></div><div id="comment-34135-info" class="comment-info"><span class="comment-age">(24 Jun '14, 11:38)</span> ZETRON-CF</div></div><span id="34136"></span><div id="comment-34136" class="comment"><div id="post-34136-score" class="comment-score"></div><div class="comment-text"><p>If you turn off the live display, does that prevent Wireshark from crashing at all, or does it just mean that it crashes when you stop the capture and Wireshark tries to read the several days worth of traffic that it's been capturing?</p></div><div id="comment-34136-info" class="comment-info"><span class="comment-age">(24 Jun '14, 13:40)</span> Guy Harris ♦♦</div></div><span id="34138"></span><div id="comment-34138" class="comment"><div id="post-34138-score" class="comment-score"></div><div class="comment-text"><p>When I have all 3 Display Options unchecked, I can run Wireshark for weeks/months without it crashing. When I stop WS, it stops normally. With Display Options enabled, I'm lucky to get a few days out of WS before it crashes. <em>We cycled through a 10mb pcap file about every minute. So we run a ring buffer of 10mb files at 200 files.</em> Lots of hard drive space.</p><p>As I researched how to turn off the Display Options, I found that dumpcap may be the solution I'm looking for. Dumpcap runs in the DOS/command window and you can add commands in a batch file to run minimized so the user never sees it on the screen.</p><p>**Both wireshark and dumpcap have command line arguments for setting up a ring buffer/files.</p></div><div id="comment-34138-info" class="comment-info"><span class="comment-age">(24 Jun '14, 14:00)</span> ZETRON-CF</div></div><span id="34139"></span><div id="comment-34139" class="comment"><div id="post-34139-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I can run Wireshark for weeks/months without it crashing</p></blockquote><p>With a ring buffer, or capturing to a single file? If it's capturing to a single file, you'll probably crash with an out-of-memory indication if you stop the capture and Wireshark then tries to read in a capture file with weeks or months of traffic.</p><blockquote><p>Dumpcap runs in the DOS/command window and you can add commands in a batch file to run minimized so the user never sees it on the screen.</p></blockquote><p>Yes, Wireshark, the program, is all about the GUI, so, if you just want something that captures traffic in the background and doesn't show anything to the user, it's the wrong choice; dumpcap is a more appropriate choice there.</p></div><div id="comment-34139-info" class="comment-info"><span class="comment-age">(24 Jun '14, 14:33)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-32563" class="comment-tools"></div><div class="clear"></div><div id="comment-32563-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="34185"></span>

<div id="answer-container-34185" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34185-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>We always use the ring buffer because we need to capture specific time durations of traffic and need the ability to go back in history to review traffic when an issue is reported.</p><p>The dumpcap worked very well for our requirement. For reference, here's the dumpcap commandline I used in a batch file. 200 10MB files. About 2GB of HD space. The script before the dumpcap will minimize the DOS/cmd window at start up. *I had to run wireshark -D first to get the NIC ID for the -i argument.</p><pre><code>REM Start batch file with cmd window minimized
REM
if not &quot;%minimized%&quot;==&quot;&quot; goto :minimized
set minimized=true
start /min cmd /C &quot;%~dpnx0&quot;
goto :EOF
:minimized
REM Anything after here will run in a minimized window
dumpcap -i 1 -w c:\temp\WS_capture.pcap -b filesize:10000 -b files:200</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jun '14, 12:01</strong></p><img src="https://secure.gravatar.com/avatar/670bd7efb04e4c74e0ad38bcb0f53f41?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ZETRON-CF&#39;s gravatar image" /><p>ZETRON-CF<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ZETRON-CF has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Jun '14, 14:04</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-34185" class="comments-container"></div><div id="comment-tools-34185" class="comment-tools"></div><div class="clear"></div><div id="comment-34185-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

