+++
type = "question"
title = "How to recover the analyzing process after crashing"
description = '''I modified a tshark version to filter the packets that I concerned, and record them in files. When tshark crashes or has no response, I want to recover the analyzing process at next tshark start up. How to record and recover the index info in minimum modifies? Any ideas?'''
date = "2014-02-16T23:39:00Z"
lastmod = "2014-02-18T00:05:00Z"
weight = 29923
keywords = [ "recover", "crash" ]
aliases = [ "/questions/29923" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to recover the analyzing process after crashing](/questions/29923/how-to-recover-the-analyzing-process-after-crashing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29923-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I modified a tshark version to filter the packets that I concerned, and record them in files. When tshark crashes or has no response, I want to recover the analyzing process at next tshark start up. How to record and recover the index info in minimum modifies? Any ideas?</p></div><div id="question-tags" class="tags-container tags">recover crash</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '14, 23:39</strong></p><img src="https://secure.gravatar.com/avatar/13679628c84abac93be65773340d2589?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="metamatrix&#39;s gravatar image" /><p>metamatrix<br />
<span class="score" title="56 reputation points">56</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="metamatrix has one accepted answer">100%</span></p></div></div><div id="comments-container-29923" class="comments-container"><span id="29955"></span><div id="comment-29955" class="comment"><div id="post-29955-score" class="comment-score"></div><div class="comment-text"><p>Anyone give me some advice? Appreciated.</p></div><div id="comment-29955-info" class="comment-info"><span class="comment-age">(17 Feb '14, 23:37)</span> metamatrix</div></div></div><div id="comment-tools-29923" class="comment-tools"></div><div class="clear"></div><div id="comment-29923-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29957"></span>

<div id="answer-container-29957" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29957-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could record the frame number (frame.number) of the processed packets to a file. When you restart tshark (with a wrapper script) you could determine the last processed frame number from that file and start tshark with the following option.</p><blockquote><p>tshark -nr input.pcap -Y "frame.number &gt; 1234"</p></blockquote><p>If your version of tshark does not know -Y, please use -R instead.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Feb '14, 00:05</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-29957" class="comments-container"><span id="29959"></span><div id="comment-29959" class="comment"><div id="post-29959-score" class="comment-score"></div><div class="comment-text"><p>Thank you，Kurt. I'll have a try.</p></div><div id="comment-29959-info" class="comment-info"><span class="comment-age">(18 Feb '14, 01:12)</span> metamatrix</div></div><span id="29960"></span><div id="comment-29960" class="comment"><div id="post-29960-score" class="comment-score"></div><div class="comment-text"><p>I'm not really sure if tshark would <strong>not</strong> crash if you use that method. I guess it depends on the reason for the crash.</p><p>If it still crashes at the same frame, you can try to modify the capture file (probably with <a href="http://www.wireshark.org/docs/man-pages/editcap.html">editcap</a>) and remove the frame(s) that led to the crash. There is no guarantee that this works, but at least it's a simple solution to implement with scripting.</p><p>Everything else would require larger changes to tshark and the whole wireshark dissection engine to catch and process exceptions.</p></div><div id="comment-29960-info" class="comment-info"><span class="comment-age">(18 Feb '14, 01:32)</span> Kurt Knochner ♦</div></div><span id="30036"></span><div id="comment-30036" class="comment"><div id="post-30036-score" class="comment-score"></div><div class="comment-text"><p>Kurt，when tshark crashes or has no response, is there one ".pcapng" file or more files not analyzed in the temp directory? In other words, after tshark crashing or having no response, can dumpcap produce new ".pcapng" files?</p></div><div id="comment-30036-info" class="comment-info"><span class="comment-age">(19 Feb '14, 17:05)</span> metamatrix</div></div></div><div id="comment-tools-29957" class="comment-tools"></div><div class="clear"></div><div id="comment-29957-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

