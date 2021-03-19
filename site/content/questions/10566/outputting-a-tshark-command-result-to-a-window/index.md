+++
type = "question"
title = "Outputting a tshark command result to a window"
description = '''Let&#x27;s say the tshark command for converting a pcap file to a Windows .txt file is: tshark -n -r &quot;C:&#92;Users&#92;L33604&#92;Desktop&#92;SplunkWireshark&#92;WiresharkPacketLogMonitor&#92;SynFlood Sample.pcap&quot; &amp;gt; &quot;C:&#92;Users&#92;L33604&#92;Desktop&#92;SplunkWireshark&#92;WiresharkPacketLogMonitor&#92;capfile.txt&quot;  The output is shown in the .t...'''
date = "2012-05-01T22:49:00Z"
lastmod = "2012-05-02T00:21:00Z"
weight = 10566
keywords = [ "tshark" ]
aliases = [ "/questions/10566" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Outputting a tshark command result to a window](/questions/10566/outputting-a-tshark-command-result-to-a-window)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10566-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Let's say the tshark command for converting a pcap file to a Windows .txt file is:</p><pre><code>tshark -n -r &quot;C:\Users\L33604\Desktop\SplunkWireshark\WiresharkPacketLogMonitor\SynFlood Sample.pcap&quot; &gt; &quot;C:\Users\L33604\Desktop\SplunkWireshark\WiresharkPacketLogMonitor\capfile.txt&quot;</code></pre><p>The output is shown in the .txt file but not on the Windows <code>cmd</code> console.</p><p>How do I change the above tshark command such that it shows the same output from the .txt file on the console?</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 May '12, 22:49</strong></p><img src="https://secure.gravatar.com/avatar/94990dfa38fcf1b33157bef842da0291?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="misteryuku&#39;s gravatar image" /><p>misteryuku<br />
<span class="score" title="20 reputation points">20</span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="misteryuku has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 May '12, 00:23</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-10566" class="comments-container"></div><div id="comment-tools-10566" class="comment-tools"></div><div class="clear"></div><div id="comment-10566-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="10567"></span>

<div id="answer-container-10567" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10567-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>type <a href="http://capfile.txt">capfile.txt</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 May '12, 22:54</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span></p></div></div><div id="comments-container-10567" class="comments-container"></div><div id="comment-tools-10567" class="comment-tools"></div><div class="clear"></div><div id="comment-10567-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10570"></span>

<div id="answer-container-10570" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10570-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Do you mean that you want to see the output in the command console and at the same time written to a file?</p><p>If so, with PowerShell (available by default in Win 7), you can use the Tee-Object cmdlet to do that:</p><p><code>tshark "your tshark parameters" | Tee-Object "your text file"</code></p><p>Note that the text file will be in Unicode format but your Java programs should be able to handle that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 May '12, 23:56</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-10570" class="comments-container"><span id="10571"></span><div id="comment-10571" class="comment"><div id="post-10571-score" class="comment-score"></div><div class="comment-text"><p>No the cmd console only.. I forgot to show my expected output. I would like to see the output below on the cmd console using tshark when converting .pcap file</p><p>1 0.000000 164.124.33.78 -&gt; 192.168.0.1 TCP 54 35165 &gt; 80 [SYN] Seq=0 Win=16384 Len=0</p><p>2 0.000001 38.198.26.9 -&gt; 192.168.0.1 TCP 54 14378 &gt; 80 [SYN] Seq=0 Win=16384 Len=0</p><p>3 0.000003 132.212.36.201 -&gt; 192.168.0.1 TCP 54 31944 &gt; 80 [SYN] Seq=0 Win=16384 Len=0</p><p>4 0.000005 76.196.6.157 -&gt; 192.168.0.1 TCP 54 10404 &gt; 80 [RST] Seq=1 Win=0 Len=0</p><p>....................................................</p></div><div id="comment-10571-info" class="comment-info"><span class="comment-age">(02 May '12, 00:02)</span> misteryuku</div></div></div><div id="comment-tools-10570" class="comment-tools"></div><div class="clear"></div><div id="comment-10570-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10572"></span>

<div id="answer-container-10572" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10572-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your command is redirecting the <code>tshark</code> stdout to <code>capfile.txt</code>. If you removed the redirection, the output would print only to the console (as you require). That is, enter this:</p><pre><code>tshark -n -r &quot;C:\Users\L33604\Desktop\SplunkWireshark\WiresharkPacketLogMonitor\SynFlood Sample.pcap&quot;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '12, 00:21</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-10572" class="comments-container"></div><div id="comment-tools-10572" class="comment-tools"></div><div class="clear"></div><div id="comment-10572-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

