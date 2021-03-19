+++
type = "question"
title = "How to: buffering recent packets only?"
description = '''I want to debug:  WireShark should run continuously, since I don&#x27;t know when the bug shows up.  I don&#x27;t want/need to save all packets, as WireShark will crash.  When the bug shows up, I will stop the WireShark.  When it stop, I hope I can see/save the last few packets (for example 1000 packets)  (so...'''
date = "2015-11-19T08:21:00Z"
lastmod = "2015-11-19T11:00:00Z"
weight = 47752
keywords = [ "buffering", "recent" ]
aliases = [ "/questions/47752" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How to: buffering recent packets only?](/questions/47752/how-to-buffering-recent-packets-only)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47752-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to debug:</p><ul><li>WireShark should run continuously, since I don't know when the bug shows up.<br />
</li><li>I don't want/need to save all packets, as WireShark will crash.<br />
</li><li>When the bug shows up, I will stop the WireShark.<br />
</li><li>When it stop, I hope I can see/save the last few packets (for example 1000 packets)<br />
</li><li>(so it should get rid of all previous packets to avoid low memory)</li></ul><p>So is it possible to do this way? How?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">buffering recent</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '15, 08:21</strong></p><img src="https://secure.gravatar.com/avatar/ee39f3f30d7889c05533e4b17771956e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jerryws&#39;s gravatar image" /><p>jerryws<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jerryws has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Nov '15, 08:27</p></div></div><div id="comments-container-47752" class="comments-container"><span id="47771"></span><div id="comment-47771" class="comment"><div id="post-47771-score" class="comment-score"></div><div class="comment-text"><p>Thanks all you guys!</p><p>I tried the solution from Kurt, and it works well: much better than my expectation!</p></div><div id="comment-47771-info" class="comment-info"><span class="comment-age">(19 Nov '15, 11:24)</span> jerryws</div></div><span id="47776"></span><div id="comment-47776" class="comment"><div id="post-47776-score" class="comment-score">1</div><div class="comment-text"><p>So, have fun with it!</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-47776-info" class="comment-info"><span class="comment-age">(19 Nov '15, 11:57)</span> Kurt Knochner ♦</div></div><span id="47777"></span><div id="comment-47777" class="comment"><div id="post-47777-score" class="comment-score"></div><div class="comment-text"><p>Yes, I checked and thumbed up!</p><p>Haha, first time to know and use these fun tools.</p></div><div id="comment-47777-info" class="comment-info"><span class="comment-age">(19 Nov '15, 12:22)</span> jerryws</div></div></div><div id="comment-tools-47752" class="comment-tools"></div><div class="clear"></div><div id="comment-47752-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="47757"></span>

<div id="answer-container-47757" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47757-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can't do that with Wireshark, as it will run out of memory. Please use dumpcap instead with a file ring buffer.</p><blockquote><p>dumpcap -ni &lt;interface&gt; -w output.pcap -b filesize:100000 -b files:50</p></blockquote><p>This will generate 50 files, each 100 Mbytes large. The 51st file will overwrite the 1st. You can leave this running until the problem shows up. Then stop dumpcap and open the last few files (maybe just the last one).</p><p>Please see the dumpcap man page for more options.</p><blockquote><p><a href="https://www.wireshark.org/docs/man-pages/dumpcap.html">https://www.wireshark.org/docs/man-pages/dumpcap.html</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '15, 09:13</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-47757" class="comments-container"></div><div id="comment-tools-47757" class="comment-tools"></div><div class="clear"></div><div id="comment-47757-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47756"></span>

<div id="answer-container-47756" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47756-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use dumpcap, not Wireshark for continuous captures.</p><p>How long are you going to sit staring at it waiting for the issue to happen?</p><p>If you use the -b options you can have multiple files of a set size or duration so you can maintain lots of history in smaller file chunks that you can then grab the file of interest.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '15, 09:12</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></p></div></div><div id="comments-container-47756" class="comments-container"></div><div id="comment-tools-47756" class="comment-tools"></div><div class="clear"></div><div id="comment-47756-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47770"></span>

<div id="answer-container-47770" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47770-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hmm, actually you can do this kind of thing with Wireshark too. In the Capture Options dialog select "Use multiple files" mode (Gtk+ GUI; the Qt/2.0 GUI's interface is somewhat different) and select how often you want a new file. From the sounds of it you also want to select ring buffer mode (and specify how many files you want in the buffer).</p><p>Doing this in Wireshark can be helpful if you want to see the packets while you're waiting for the failure, for example if you need to see the packets to know if you've hit the bug.</p><p><em>Theoretically</em> Wireshark should free most (if not all) of its memory each time it closes the but I'm pretty sure memory usage will still grow a bit while doing this. So if you plan to run for a very long time Kurt or Graham's suggestion to use dumpcap is certainly better.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '15, 11:00</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-47770" class="comments-container"></div><div id="comment-tools-47770" class="comment-tools"></div><div class="clear"></div><div id="comment-47770-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

