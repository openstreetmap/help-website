+++
type = "question"
title = "Capturing packets to a file using Wireshark&#x27;s Capture options."
description = '''I went to the Wireshark&#x27;s caputure options and created file name, check use multiple files, determine the rotation of files, check ring buffer with x files, how many files to create...? The files are generated and when i opened up the files, i saw many unreadable characters on the windows 7 notepad ...'''
date = "2012-04-13T00:56:00Z"
lastmod = "2012-04-13T01:16:00Z"
weight = 10105
keywords = [ "capture", "log", "file" ]
aliases = [ "/questions/10105" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing packets to a file using Wireshark's Capture options.](/questions/10105/capturing-packets-to-a-file-using-wiresharks-capture-options)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10105-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I went to the Wireshark's caputure options and created file name, check use multiple files, determine the rotation of files, check ring buffer with x files, how many files to create...? The files are generated and when i opened up the files, i saw many unreadable characters on the windows 7 notepad file. Why is this so? I want to get the events in the windows 7 notepad file as readable logs.</p></div><div id="question-tags" class="tags-container tags">capture log file</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Apr '12, 00:56</strong></p><img src="https://secure.gravatar.com/avatar/94990dfa38fcf1b33157bef842da0291?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="misteryuku&#39;s gravatar image" /><p>misteryuku<br />
<span class="score" title="20 reputation points">20</span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="misteryuku has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Apr '12, 01:14</p></div></div><div id="comments-container-10105" class="comments-container"></div><div id="comment-tools-10105" class="comment-tools"></div><div class="clear"></div><div id="comment-10105-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10106"></span>

<div id="answer-container-10106" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10106-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark writes network packets into binary trace files, and not as human readable events - so if you're expecting to see some sort of ASCII dump you are mistaken about how Wireshark works.</p><p>You'll need to open the files in Wireshark, or display them using tshark. Notepad won't help unless you open the files in Wireshark first and then use the export option to write the decoded packet contents to a text file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Apr '12, 01:16</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-10106" class="comments-container"><span id="10108"></span><div id="comment-10108" class="comment"><div id="post-10108-score" class="comment-score"></div><div class="comment-text"><p>What you mean is that while Wireshark is caputuring packets, export the decoded packet contents to a file is it?</p></div><div id="comment-10108-info" class="comment-info"><span class="comment-age">(13 Apr '12, 01:21)</span> misteryuku</div></div><span id="10110"></span><div id="comment-10110" class="comment"><div id="post-10110-score" class="comment-score"></div><div class="comment-text"><p>If you want to see packets decoded in a ASCII format, yes, you can do that. Open the trace file in Wireshark (which will allow you to look at packets, too), and then use the "File" - "Export" - "File" and select "Plain Text".</p><p>I would recommend using Wireshark to examine the packets though - it's much more powerful to filter and search packets there compared to using a text editor.</p></div><div id="comment-10110-info" class="comment-info"><span class="comment-age">(13 Apr '12, 01:27)</span> Jasper ♦♦</div></div><span id="10111"></span><div id="comment-10111" class="comment"><div id="post-10111-score" class="comment-score"></div><div class="comment-text"><p>My intention for capturing packets to a file is to capture DoS attack events as log events. And i will use this information to be put inside Splunk.</p></div><div id="comment-10111-info" class="comment-info"><span class="comment-age">(13 Apr '12, 01:33)</span> misteryuku</div></div><span id="10112"></span><div id="comment-10112" class="comment"><div id="post-10112-score" class="comment-score"></div><div class="comment-text"><p>In that case you could write a batch file that uses tshark.exe to read the binary files you have captured and put its output to a text file. That way you can automate your process.</p><p>For example:</p><p><strong>tshark -r "tracefile01" &gt; <a href="http://tracefile01.txt">tracefile01.txt</a></strong></p><p>Maybe you can even use tshark on its own to generate the ascii files right away, but I haven't tested that yet.</p></div><div id="comment-10112-info" class="comment-info"><span class="comment-age">(13 Apr '12, 01:42)</span> Jasper ♦♦</div></div><span id="10116"></span><div id="comment-10116" class="comment"><div id="post-10116-score" class="comment-score"></div><div class="comment-text"><p>I'm new to writing batch files so the writing of batch files is on the notepad is it?</p></div><div id="comment-10116-info" class="comment-info"><span class="comment-age">(13 Apr '12, 02:20)</span> misteryuku</div></div><span id="10119"></span><div id="comment-10119" class="comment not_top_scorer"><div id="post-10119-score" class="comment-score"></div><div class="comment-text"><p>Yes, it is. Batch files are scripts that you write in any text editor you like, for example notepad (though that is considered doing it the hard way, there are way better editors out there, for example Notepad++ etc)</p></div><div id="comment-10119-info" class="comment-info"><span class="comment-age">(13 Apr '12, 02:28)</span> Jasper ♦♦</div></div><span id="10121"></span><div id="comment-10121" class="comment not_top_scorer"><div id="post-10121-score" class="comment-score"></div><div class="comment-text"><p>You'll find that standard DOS (Windows) batch files are very limited when you want to filter and process text. Generally you'll need to go for something better such as Cygwin (U*ix emulation, separate download and install, can be confusing for newbies) or my recommendation, PowerShell which comes with Win 7.</p></div><div id="comment-10121-info" class="comment-info"><span class="comment-age">(13 Apr '12, 02:35)</span> grahamb ♦</div></div><span id="10123"></span><div id="comment-10123" class="comment not_top_scorer"><div id="post-10123-score" class="comment-score"></div><div class="comment-text"><p>I'm really a newbie, what is the reason that i need to filter and process text? i don't really understand? My intention for capturing packets to a file is to capture DoS attack events as log events. And i will use this information to be put inside Splunk.</p></div><div id="comment-10123-info" class="comment-info"><span class="comment-age">(13 Apr '12, 05:45)</span> misteryuku</div></div><span id="10127"></span><div id="comment-10127" class="comment not_top_scorer"><div id="post-10127-score" class="comment-score"></div><div class="comment-text"><p>I'm guessing that the output format of tshark and the input format of Splunk may be different. If that's the case, you'll need some form of script to convert between the two formats.</p></div><div id="comment-10127-info" class="comment-info"><span class="comment-age">(13 Apr '12, 06:22)</span> grahamb ♦</div></div><span id="10144"></span><div id="comment-10144" class="comment not_top_scorer"><div id="post-10144-score" class="comment-score"></div><div class="comment-text"><p>okay. i see.</p></div><div id="comment-10144-info" class="comment-info"><span class="comment-age">(13 Apr '12, 19:53)</span> misteryuku</div></div></div><div id="comment-tools-10106" class="comment-tools"><span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a></div><div class="clear"></div><div id="comment-10106-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

