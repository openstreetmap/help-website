+++
type = "question"
title = "Generating own expected output form live pcap capture live to a windows txt file"
description = '''This is a tshark command to output packet capture live to a windows txt file. tshark -i your_interface -V &amp;gt; your _path _to _text _file This is a tshark command to output the wireshark GUI column data of the pcap to the txt file tshark -n -r path _ of _ pcap_file &amp;gt; path _ of _ txt _ file My exp...'''
date = "2012-04-23T00:30:00Z"
lastmod = "2012-04-23T01:03:00Z"
weight = 10389
keywords = [ "live", "txt", "tshark" ]
aliases = [ "/questions/10389" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Generating own expected output form live pcap capture live to a windows txt file](/questions/10389/generating-own-expected-output-form-live-pcap-capture-live-to-a-windows-txt-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10389-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This is a tshark command to output packet capture live to a windows txt file.</p><p>tshark -i your_interface -V &gt; your _path _to _text _file</p><p>This is a tshark command to output the wireshark GUI column data of the pcap to the txt file</p><p>tshark -n -r path _ of _ pcap_file &gt; path _ of _ txt _ file</p><p>My expected windows txt output :</p><p>1 0.000000 164.124.33.78 -&gt; 192.168.0.1 TCP 54 35165 &gt; 80 [SYN] Seq=0 Win=16384 Len=0</p><p>2 0.000001 38.198.26.9 -&gt; 192.168.0.1 TCP 54 14378 &gt; 80 [SYN] Seq=0 Win=16384 Len=0</p><p>3 0.000003 132.212.36.201 -&gt; 192.168.0.1 TCP 54 31944 &gt; 80 [SYN] Seq=0 Win=16384 Len=0</p><p>First Question : How do i know what is the interface to capture the packets live and how to address that in a tshark command as its IP address or its name?</p><p>Second Question : I would like to capture the packet data live, generate the above txt output that i expect to a txt file as in "combining the two tshark commands" stated above??</p></div><div id="question-tags" class="tags-container tags">live txt tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '12, 00:30</strong></p><img src="https://secure.gravatar.com/avatar/94990dfa38fcf1b33157bef842da0291?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="misteryuku&#39;s gravatar image" /><p>misteryuku<br />
<span class="score" title="20 reputation points">20</span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="misteryuku has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Apr '12, 00:35</p></div></div><div id="comments-container-10389" class="comments-container"></div><div id="comment-tools-10389" class="comment-tools"></div><div class="clear"></div><div id="comment-10389-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10391"></span>

<div id="answer-container-10391" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10391-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How do i know what is the interface to capture the packets live and how to address that in a tshark command as its IP address or its name?</p></blockquote><p>You can't specify an interface by IP address. If you run <code>tshark -D</code>, it will print the interfaces available; if this is on Windows, the names will not be particularly simple, but there should also be a description given, as well as a number, and you can (whether on Windows or not) use the number as an argument to <code>-i</code>. <code>ipconfig/all</code> on Windows, and <code>ifconfig -a</code> on most UN*Xes, should list the IP addresses assigned to various interfaces, which should let you figure out which interface to use.</p><blockquote><p>I would like to capture the packet data live, generate the above txt output that i expect to a txt file as in "combining the two tshark commands" stated above??</p></blockquote><p>You combine the two commands by taking the first command, removing <code>-V</code>, and adding <code>-n</code>, so that it prints column data rather than a full dissection of the packets, and doesn't try to translate IP addresses to host names:</p><pre><code>tshark -i your_interface -n &gt; your _path _to _text _file</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '12, 01:03</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-10391" class="comments-container"><span id="10393"></span><div id="comment-10393" class="comment"><div id="post-10393-score" class="comment-score"></div><div class="comment-text"><p>The description capture interface that i use to capture live packets on Windows is Intel(R)Gigabit network connection when i ran tshark -D</p><p>is something like this:</p><p>DeviceNPF_{97DEDE1D-222F-4F9B-8A5C-C4BFF6C3904C} (Intel(R)Gigabit network connection)</p><p>I ran the command like this : tshark -i DeviceNPF_{97DEDE1D-222F-4F9B-8A5C-C4BFF6C3904C} (Intel(R)Gigabit network connection) -n &gt; "C:\Users\L33604\Desktop\<a href="http://capture.txt">capture.txt</a>"</p><p>then windows cmd CLI threw the error message :</p><p>Please check that DeviceNPF_{97DEDE1D-222F-4F9B-8A5C-C4BFF6C3904C} is the correct interface. What is wrong here??</p></div><div id="comment-10393-info" class="comment-info"><span class="comment-age">(23 Apr '12, 01:37)</span> misteryuku</div></div><span id="10398"></span><div id="comment-10398" class="comment"><div id="post-10398-score" class="comment-score"></div><div class="comment-text"><p>You need to use the number associated with each interface, e.g. if tshark -D gives you this:</p><p><code> 1. DeviceNPF_{AA1F8321-8EB5-4B77-A0E9-D4B359711C2B} (Microsoft) 2. DeviceNPF_{C2E403B5-FAD0-479C-96FD-0E44EB22CD74} (Intel(R) 82579LM Gigabit Network Connection) 3. DeviceNPF_{6EB43EB8-D680-4363-B6BA-E3373CC7ACF7} (Microsoft)</code></p><p>then use <code>-i 2</code> to select the Gigabit connection.</p></div><div id="comment-10398-info" class="comment-info"><span class="comment-age">(23 Apr '12, 04:39)</span> grahamb ♦</div></div></div><div id="comment-tools-10391" class="comment-tools"></div><div class="clear"></div><div id="comment-10391-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

