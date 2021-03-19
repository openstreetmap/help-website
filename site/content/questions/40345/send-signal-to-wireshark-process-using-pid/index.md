+++
type = "question"
title = "Send signal to wireshark process using pid"
description = '''Hi all, I am developing one utility in windows. I can successfully start Wireshark GUI using CreateProcess function.  Now I want to stop the capture only(not to close that Wireshark window) of that particular created Wireshark process. If I kill dumpcap process by same CreateProcess function, it is ...'''
date = "2015-03-07T01:26:00Z"
lastmod = "2015-03-09T09:23:00Z"
weight = 40345
keywords = [ "stop-capture", "dumpcap" ]
aliases = [ "/questions/40345" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Send signal to wireshark process using pid](/questions/40345/send-signal-to-wireshark-process-using-pid)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40345-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I am developing one utility in windows. I can successfully start Wireshark GUI using CreateProcess function. Now I want to stop the capture only(not to close that Wireshark window) of that particular created Wireshark process. If I kill dumpcap process by same CreateProcess function, it is stopping all the other Wireshark instances.</p><p>Is there any way to stop dumpcap of my own created Wireshark process while other Wireshark window will still be active and capture as before. Can I send any signal by using the PID of my created Wireshark process to do that?</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">stop-capture dumpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Mar '15, 01:26</strong></p><img src="https://secure.gravatar.com/avatar/e82780891a1e938f0bf3a529adc858a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baila&#39;s gravatar image" /><p>baila<br />
<span class="score" title="21 reputation points">21</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baila has no accepted answers">0%</span></p></div></div><div id="comments-container-40345" class="comments-container"></div><div id="comment-tools-40345" class="comment-tools"></div><div class="clear"></div><div id="comment-40345-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="40388"></span>

<div id="answer-container-40388" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40388-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>From the command line, you can do something like:</p><pre><code>C:\&gt;wmic process where (ParentProcessId=XXXX) get Caption,ProcessId
Caption      ProcessId
dumpcap.exe  YYYY</code></pre><p>... where <code>XXXX</code> is the process ID of Wireshark and <code>YYYY</code> is the process ID of Wireshark's dumpcap instance. Once you have dumpcap's process ID, it should be easy to terminate only that instance. One such way:</p><pre><code>C:\&gt;taskkill /f /pid YYYY
SUCCESS: The process with PID YYYY has been terminated.</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Mar '15, 09:23</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-40388" class="comments-container"><span id="40391"></span><div id="comment-40391" class="comment"><div id="post-40391-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot cmaynard. I'll definitely try that and let you know!</p></div><div id="comment-40391-info" class="comment-info"><span class="comment-age">(09 Mar '15, 10:03)</span> baila</div></div><span id="40394"></span><div id="comment-40394" class="comment"><div id="post-40394-score" class="comment-score"></div><div class="comment-text"><p>Another possible option, if you want to do it entirely in code instead of using the command-line, might be to borrow <a href="http://stackoverflow.com/questions/20874381/get-a-process-id-in-c-by-name">this</a> idea.</p><p>Basically, take a snapshot of all running processes, then iterate through them all. For each one named, "dumpcap.exe", see if its parent process ID matches the process ID of your Wireshark instance of interest. If it does, you have found the child process ID and can then kill it, presumably by first calling <code>OpenProcess()</code> to get the handle, and then calling <code>TerminateProcess()</code>.</p><p>I don't know, there might be an easier way ...</p></div><div id="comment-40394-info" class="comment-info"><span class="comment-age">(09 Mar '15, 10:33)</span> cmaynard ♦♦</div></div><span id="40468"></span><div id="comment-40468" class="comment"><div id="post-40468-score" class="comment-score"></div><div class="comment-text"><p>@cmaynard - your first solution works great. Thanks for your great solution.</p></div><div id="comment-40468-info" class="comment-info"><span class="comment-age">(11 Mar '15, 03:56)</span> baila</div></div></div><div id="comment-tools-40388" class="comment-tools"></div><div class="clear"></div><div id="comment-40388-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40352"></span>

<div id="answer-container-40352" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40352-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is no way to do this with the current Wireshark version, as that functionality is not implemented.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Mar '15, 13:22</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-40352" class="comments-container"><span id="40360"></span><div id="comment-40360" class="comment"><div id="post-40360-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt. Is there any way to get the pid of the dumpcap of my own created instance, so that i can kill that particular dumpcap instance?</p><p>Thanks.</p></div><div id="comment-40360-info" class="comment-info"><span class="comment-age">(07 Mar '15, 20:17)</span> baila</div></div><span id="40368"></span><div id="comment-40368" class="comment"><div id="post-40368-score" class="comment-score"></div><div class="comment-text"><p>Is there any work around??</p></div><div id="comment-40368-info" class="comment-info"><span class="comment-age">(08 Mar '15, 10:51)</span> baila</div></div><span id="40402"></span><div id="comment-40402" class="comment"><div id="post-40402-score" class="comment-score"></div><div class="comment-text"><p>You can do what @cmaynard wrote.</p><p>As an alternative, you could describe what you are trying to do with your windows tool. Maybe there is a totally different approach to solve that without starting a GUI version of Wireshark ;-)</p></div><div id="comment-40402-info" class="comment-info"><span class="comment-age">(09 Mar '15, 13:42)</span> Kurt Knochner ♦</div></div><span id="40415"></span><div id="comment-40415" class="comment"><div id="post-40415-score" class="comment-score"></div><div class="comment-text"><p>@Kurt I am writing one application, which will open the Wireshark GUI, captures packets and stop capturing if signaled from my application. It will just stop the capture, not close the Wireshark GUI. Users may have multiple Wireshark instances running on their system, so I don't want to disturb those instances.</p></div><div id="comment-40415-info" class="comment-info"><span class="comment-age">(09 Mar '15, 22:26)</span> baila</div></div><span id="40418"></span><div id="comment-40418" class="comment"><div id="post-40418-score" class="comment-score"></div><div class="comment-text"><p>I see the following alternatives:</p><p>1.) Don't capture with the GUI Wireshark. Use dumpcap directly (start / stop it as you need it) and then start Wireshark to load the capture file (-nr)</p><p>2.) Start your own dumpcap and Wireshark instances in the following way.</p><ul><li>Create a named pipe (see MSDN how to do that, or search ask.wireshark.org)</li><li>Let Wireshark read from the named pipe (Wireshark -ni \.\pipe\whatever -k)</li><li>start dumpcap and let it write to the named pipe.</li></ul><p>With option 2. you know the PIDs of both tools and you can kill either of them as you need it.</p><p>You can search this Q&amp;A site for named pipes and also read my answer to the following question:</p><blockquote><p><a href="https://ask.wireshark.org/questions/13059/capturing-from-multiple-pipes">https://ask.wireshark.org/questions/13059/capturing-from-multiple-pipes</a></p></blockquote><p>The wiki has some information as well:</p><blockquote><p><a href="http://wiki.wireshark.org/CaptureSetup/Pipes">http://wiki.wireshark.org/CaptureSetup/Pipes</a></p></blockquote></div><div id="comment-40418-info" class="comment-info"><span class="comment-age">(10 Mar '15, 04:00)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-40352" class="comment-tools"></div><div class="clear"></div><div id="comment-40352-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

