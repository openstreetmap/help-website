+++
type = "question"
title = "No new log file is created after restart PC"
description = '''When I use the link below to automatically start wireshark when starting the PC, wireshark will not create a new log file each time the computer is restarted: &quot;C:&#92;Program Files (x86)&#92;Wireshark&#92;wireshark.exe&quot; -i &quot;&#92;Device&#92;NPF_{59A6CEB4-F94B-47ED-A6FF-7F61ED6EED06}&quot; -k -w &quot;C:&#92;Users&#92;receptie1&#92;Desktop&#92;SH...'''
date = "2013-01-13T21:12:00Z"
lastmod = "2013-01-14T15:08:00Z"
weight = 17655
keywords = [ "new", "logfile", "reboot", "after" ]
aliases = [ "/questions/17655" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [No new log file is created after restart PC](/questions/17655/no-new-log-file-is-created-after-restart-pc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17655-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I use the link below to automatically start wireshark when starting the PC, wireshark will not create a new log file each time the computer is restarted:</p><p>"C:\Program Files (x86)\Wireshark\wireshark.exe" -i "\Device\NPF_{59A6CEB4-F94B-47ED-A6FF-7F61ED6EED06}" -k -w "C:\Users\receptie1\Desktop\SHARE\capture.pcap" -B10 -b:5000</p><p>Please provide me a solution. Thank you.</p></div><div id="question-tags" class="tags-container tags">new logfile reboot after</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '13, 21:12</strong></p><img src="https://secure.gravatar.com/avatar/dddcd0fc568165e669b68896ac9aa881?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ruben&#39;s gravatar image" /><p>Ruben<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ruben has no accepted answers">0%</span></p></div></div><div id="comments-container-17655" class="comments-container"></div><div id="comment-tools-17655" class="comment-tools"></div><div class="clear"></div><div id="comment-17655-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17656"></span>

<div id="answer-container-17656" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17656-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use the following command in your batch script, to add the current date/time to the file name:</p><blockquote><p><code>set filename=C:\Users\receptie1\Desktop\SHARE\capture-%date%-%time:~0,2%-%time:~3,2%-%time:~6,2%.pcap</code></p></blockquote><p>Then use the variable filename with the option <strong><code>-w</code></strong></p><blockquote><p><code>wireshark -w %filename%</code><br />
</p></blockquote><p>Sample:</p><p><code> C:&gt;set filename=C:\Users\receptie1\Desktop\SHARE\capture-%date%-%time:~0,2%-%time:~3,2%-%time:~6,2%.pcap</code></p><code></code><p><code>C:&gt;echo %filename% C:\Users\receptie1\Desktop\SHARE\capture-14.01.2013-10-19-01.pcap</code></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '13, 01:21</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Jan '13, 02:01</p></div></div><div id="comments-container-17656" class="comments-container"></div><div id="comment-tools-17656" class="comment-tools"></div><div class="clear"></div><div id="comment-17656-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17678"></span>

<div id="answer-container-17678" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17678-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is a syntax error in your command, which prevents the command from being run:</p><pre><code>&quot;C:\Program Files (x86)\Wireshark\wireshark.exe&quot; -i &quot;\Device\NPF_{59A6CEB4-F94B-47ED-A6FF-7F61ED6EED06}&quot; -k 
    -w &quot;C:\Users\receptie1\Desktop\SHARE\capture.pcap&quot; -B10 -b:5000</code></pre><p>The "-b" option expects some more info (see "wireshark -h" output):</p><pre><code>  -b &lt;ringbuffer opt.&gt; ... duration:NUM - switch to next file after NUM secs
                           filesize:NUM - switch to next file after NUM KB
                           files:NUM - ringbuffer: replace after NUM files</code></pre><p>So you could use the following command:</p><pre><code>&quot;C:\Program Files (x86)\Wireshark\wireshark.exe&quot; -i &quot;\Device\NPF_{59A6CEB4-F94B-47ED-A6FF-7F61ED6EED06}&quot; -k 
    -w &quot;C:\Users\receptie1\Desktop\SHARE\capture.pcap&quot; -B10 -b filesize:5000 -b files:100</code></pre><p>To create a ringbuffer of 100 files of 5000KB each (500 MB in total). When wireshark needs to create the 101st file, it will delete the oldest file first. Please be aware that old files are not removed after each restart, so each restart will add another 100 files of 5000KB. You need to remove the files yourself after a reboot.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '13, 15:08</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-17678" class="comments-container"></div><div id="comment-tools-17678" class="comment-tools"></div><div class="clear"></div><div id="comment-17678-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

