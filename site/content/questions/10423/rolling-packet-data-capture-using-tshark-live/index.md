+++
type = "question"
title = "Rolling packet data capture using tshark live."
description = '''Lets say if i want to capture the wireshark capture GUI column data live to a windows txt file using tshark. The tshark command will be like this : tshark -i your_interface -n &amp;gt; your _path _to _text _file I would like to ROLL the windows txt file that conatins the wireshark capture GUI column dat...'''
date = "2012-04-24T18:38:00Z"
lastmod = "2012-04-30T09:18:00Z"
weight = 10423
keywords = [ "capture", "live", "tshark" ]
aliases = [ "/questions/10423" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Rolling packet data capture using tshark live.](/questions/10423/rolling-packet-data-capture-using-tshark-live)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10423-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Lets say if i want to capture the wireshark capture GUI column data live to a windows txt file using tshark. The tshark command will be like this : <code>tshark -i your_interface -n &gt; your _path _to _text _file</code> I would like to ROLL the windows txt file that conatins the wireshark capture GUI column data that is captured live. The windows batch file will then run the java files that process the txt file data that has just rolled (The packet data info had stopped appending to the same file) while more the packet data is captured to another txt file live. The whole process will repeat. My goal is to automate this whole process by writing a windows 7 batch file and run it on boot.(Placing the written batch file on the STARTUP folder so the batch file will execute). i tried this command on windows 7 CLI: <code>tshark -i 3 -b filesize:1024 -b files:5 -n&gt; "C:\\Users\\L33604\\Desktop\\Folder\\Capture.txt"</code> The error message was thrown tshark : maximum capture file size specified, but capture isn't saved to a file. I know that this command would never run the java file that processes the txt file that has been just rolled. How would the above tshark command change and how would the batch file be written to execute the whole process i described?? Or any better recommendation? The main idea is</p><ol><li>rolling captured packet data live using tshark command.</li><li>running java files that process the single txt file just rolled while live capturing is still going on to another txt file in a multitasking manner.</li><li>Once after the java file has finished executing its codes, wait for more packet data to be captured to the other txt file to its limit then run the same java files again.</li></ol></div><div id="question-tags" class="tags-container tags">capture live tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Apr '12, 18:38</strong></p><img src="https://secure.gravatar.com/avatar/94990dfa38fcf1b33157bef842da0291?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="misteryuku&#39;s gravatar image" /><p>misteryuku<br />
<span class="score" title="20 reputation points">20</span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="misteryuku has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Apr '12, 07:10</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-10423" class="comments-container"><span id="10518"></span><div id="comment-10518" class="comment"><div id="post-10518-score" class="comment-score"></div><div class="comment-text"><p>Modifying your question so heavily that the previous answers barely make sense isn't the correct way to use this site. Minor edits to clarify things are acceptable.</p><p>You ask a question, others answer it, you then accept all answers that solve your issue so that others who have a similar question can see the answers given that helped you and help themselves.</p><p>If you have another question, then please create a new one, so that the the correct answers will appear after it.</p><p>I have reverted your question to its original state.</p></div><div id="comment-10518-info" class="comment-info"><span class="comment-age">(30 Apr '12, 07:05)</span> grahamb ♦</div></div></div><div id="comment-tools-10423" class="comment-tools"></div><div class="clear"></div><div id="comment-10423-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10445"></span>

<div id="answer-container-10445" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10445-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You're assuming that the <code>-b</code> options apply when writing out dissected packet information in text form rather than when writing out raw binary packet data in pcap or pcap-ng form; they do not.</p><p>Dissected packet information is written to the standard output, which is not necessarily being written to a file; even if it happens to be written to a file, TShark has no control over the file - it just gets its standard output redirected to a file by the program that runs it - probably <code>cmd.exe</code> in your case.</p><p>You would have to pipe the output of TShark to <em>another</em> program; <em>that</em> program could, for example, be given an argument specifying the path to the directory into which to write the files and part of the name to be given to the files, and could read its standard input and write it to a file and, when that file reaches its maximum size, close that file, open a new file, and continue writing its standard input to the new file. I don't know whether any such programs already exist, either for UN*X or Windows; if not, you might have to write it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '12, 12:16</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-10445" class="comments-container"><span id="10454"></span><div id="comment-10454" class="comment"><div id="post-10454-score" class="comment-score"></div><div class="comment-text"><p>I wanted the output as the wireshark GUI column data when i call this tshark command tshark -i your_interface -n &gt; your _path _to _text _file. So if that kind of text output were to be generated form tshark, then can i also pipe the text output from the tshark command tshark -i your_interface -n &gt; your _path _to _text _file to another program instead of piping the standard output??</p></div><div id="comment-10454-info" class="comment-info"><span class="comment-age">(25 Apr '12, 20:07)</span> misteryuku</div></div><span id="10464"></span><div id="comment-10464" class="comment"><div id="post-10464-score" class="comment-score"></div><div class="comment-text"><p>If you're piping the output from tshark, there's <em>no</em> <code>&gt;</code> in the tshark command; the command would be something such as</p><pre><code>tshark -i your_interface -n | your_program</code></pre><p>That will write the column data (as you haven't used the <code>-V</code> flag) to a pipe and the pipe will be the standard input of "your_program".</p></div><div id="comment-10464-info" class="comment-info"><span class="comment-age">(26 Apr '12, 09:36)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-10445" class="comment-tools"></div><div class="clear"></div><div id="comment-10445-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10525"></span>

<div id="answer-container-10525" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10525-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>to hand over the capture files you will have to implement a "directory watcher" in java, that fires every time a new file is created in your working directory. tshark itself will not tell your external java programm when it creates a new "rolling" capture file. You can find some information about a "directory watcher" in java here:</p><p><a href="http://docs.oracle.com/javase/tutorial/essential/io/notification.html">http://docs.oracle.com/javase/tutorial/essential/io/notification.html</a><br />
<a href="http://java.dzone.com/news/how-watch-file-system-changes">http://java.dzone.com/news/how-watch-file-system-changes</a><br />
<a href="http://www.venishjoe.net/2009/10/monitor-directory-for-changes-using.html">http://www.venishjoe.net/2009/10/monitor-directory-for-changes-using.html</a><br />
</p><p>I think you will get further information in a java programmer forum.</p><p>BTW: Why not using a libpcap wrapper in java altogether, instead of tshark?</p><p>jNetPcap<br />
<a href="http://jnetpcap.com/">http://jnetpcap.com/</a></p><p>Jpcap<br />
<a href="http://netresearch.ics.uci.edu/kfujii/Jpcap/doc/">http://netresearch.ics.uci.edu/kfujii/Jpcap/doc/</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '12, 09:18</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-10525" class="comments-container"></div><div id="comment-tools-10525" class="comment-tools"></div><div class="clear"></div><div id="comment-10525-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

