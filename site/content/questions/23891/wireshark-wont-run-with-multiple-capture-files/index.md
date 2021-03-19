+++
type = "question"
title = "Wireshark won&#x27;t run with multiple capture files"
description = '''I would like to run wireshark with multiple files of 2 GB each, with max. 50 files. When i start wireshark, the windows flashes and with every flash a file is created, up to 50 files. Then wireshark stops. This happens in the 64 bit and 32 bit version. I&#x27;m running windows 7 Pro '''
date = "2013-08-21T00:58:00Z"
lastmod = "2013-08-26T06:20:00Z"
weight = 23891
keywords = [ "multiple-files" ]
aliases = [ "/questions/23891" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark won't run with multiple capture files](/questions/23891/wireshark-wont-run-with-multiple-capture-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23891-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to run wireshark with multiple files of 2 GB each, with max. 50 files. When i start wireshark, the windows flashes and with every flash a file is created, up to 50 files. Then wireshark stops. This happens in the 64 bit and 32 bit version. I'm running windows 7 Pro</p></div><div id="question-tags" class="tags-container tags">multiple-files</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Aug '13, 00:58</strong></p><img src="https://secure.gravatar.com/avatar/0f01187582313ec338c90164fe3433be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FMvdBergh&#39;s gravatar image" /><p>FMvdBergh<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FMvdBergh has no accepted answers">0%</span></p></div></div><div id="comments-container-23891" class="comments-container"><span id="23899"></span><div id="comment-23899" class="comment"><div id="post-23899-score" class="comment-score"></div><div class="comment-text"><blockquote><p>a file is created, up to 50 files. Then wireshark stops.</p></blockquote><p>Isn't that what you want?</p></div><div id="comment-23899-info" class="comment-info"><span class="comment-age">(21 Aug '13, 03:20)</span> Kurt Knochner ♦</div></div><span id="23975"></span><div id="comment-23975" class="comment"><div id="post-23975-score" class="comment-score"></div><div class="comment-text"><p>What do you call files ?</p></div><div id="comment-23975-info" class="comment-info"><span class="comment-age">(23 Aug '13, 05:07)</span> Afrim</div></div><span id="24053"></span><div id="comment-24053" class="comment"><div id="post-24053-score" class="comment-score"></div><div class="comment-text"><p>For Kurt,</p><p>yes, that is what i want, but i want them also to be filled with data.</p><p>For Afrim,</p><p>Names like DVL, or DVL-1, or DVL_captures_data, names like that. Nothing complecited. I've tried them all.</p></div><div id="comment-24053-info" class="comment-info"><span class="comment-age">(26 Aug '13, 02:59)</span> FMvdBergh</div></div></div><div id="comment-tools-23891" class="comment-tools"></div><div class="clear"></div><div id="comment-23891-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="24059"></span>

<div id="answer-container-24059" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24059-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>. I see that I left out the fact that the files were all fifty filled with only a few bytes. If they were filled to the max with captured data then would not have a problem. The settings were 2 GB per file and to stop after 50 files, no ringbuffer.</p></blockquote><p>I can confirm thar behavior for 10.0.x on Windows XP SP3. It only happens if you select a file size of &gt;= 2 Gigabyte. In that case the file switch takes place after a single frame, thus the "flashing" of the window. This looks like a yet undiscovered bug as it is the same for 1.8.x and 1.9.x.</p><p>Instruction to reproduce it.</p><blockquote><p>Capture -&gt; Options</p></blockquote><p>Select: Use multiple files Select: Next file every 2 Gigabyte Select: Stop capture a xx files</p><p>Please file a bug report at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> with a link to this question.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '13, 06:20</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-24059" class="comments-container"><span id="24063"></span><div id="comment-24063" class="comment"><div id="post-24063-score" class="comment-score"></div><div class="comment-text"><p>Does this hold true for a 64 bit version of Wireshark?</p></div><div id="comment-24063-info" class="comment-info"><span class="comment-age">(26 Aug '13, 07:28)</span> grahamb ♦</div></div><span id="24067"></span><div id="comment-24067" class="comment"><div id="post-24067-score" class="comment-score"></div><div class="comment-text"><p>Grahamb,</p><p>that holds for the 64 bit version. I observed this behavior also in the linux version.</p></div><div id="comment-24067-info" class="comment-info"><span class="comment-age">(26 Aug '13, 08:57)</span> FMvdBergh</div></div><span id="24174"></span><div id="comment-24174" class="comment"><div id="post-24174-score" class="comment-score"></div><div class="comment-text"><p>No need for a bug report; I committed a fix in <a href="http://anonsvn.wireshark.org/viewvc?revision=51576&amp;view=revision">r51576</a> and <a href="http://wiki.wireshark.org/Development/Roadmap">scheduled it for 1.10.2</a>. In the meantime, you can either download a <a href="http://www.wireshark.org/download/automated/win32/">win32</a> (or <a href="http://www.wireshark.org/download/automated/win64/">win64</a>) automated release or use the following work-around: Instead of specifying 2 gigabyte(s) for the "Next file every" setting, specify 2000 megabyte(s).</p></div><div id="comment-24174-info" class="comment-info"><span class="comment-age">(29 Aug '13, 12:23)</span> cmaynard ♦♦</div></div><span id="24266"></span><div id="comment-24266" class="comment"><div id="post-24266-score" class="comment-score"></div><div class="comment-text"><p>This means that this question can be closed. I'm not sure how to do that.</p></div><div id="comment-24266-info" class="comment-info"><span class="comment-age">(01 Sep '13, 05:35)</span> FMvdBergh</div></div><span id="24267"></span><div id="comment-24267" class="comment"><div id="post-24267-score" class="comment-score"></div><div class="comment-text"><p>I marked Kurt's answer as the accepted one. This is done by clicking on the check mark next to the answer per the <a href="http://ask.wireshark.org/faq/">faq</a>.</p></div><div id="comment-24267-info" class="comment-info"><span class="comment-age">(01 Sep '13, 05:43)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-24059" class="comment-tools"></div><div class="clear"></div><div id="comment-24059-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23982"></span>

<div id="answer-container-23982" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23982-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, I'm assuming that when you configured your ring buffer for a maximum of 50 files that you didn't also set the "<em>Stop capture after 50 files</em>" too?</p><p>Those are pretty big files, and I wouldn't be the least bit surprised if you encountered an <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">Out of Memory</a> condition, which may or may not be the cause of the problem here. In any case, I highly recommend using <a href="http://www.wireshark.org/docs/man-pages/dumpcap.html">dumpcap</a> instead, which can provide the same ring buffering options as Wireshark provides, but which will obviate the risk of running out of memory.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Aug '13, 07:35</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-23982" class="comments-container"><span id="24052"></span><div id="comment-24052" class="comment"><div id="post-24052-score" class="comment-score"></div><div class="comment-text"><p>Hi, thanks for the answer. I see that I left out the fact that the files were all fifty filled with only a few bytes. If they were filled to the max with captured data then would not have a problem. The settings were 2 GB per file and to stop after 50 files, no ringbuffer. So, i don't think is a Out of memory problem since there is no data. For now i'm using the next settings and that seems to work: Every 30 minutes a file with 4 ringbuffers.</p></div><div id="comment-24052-info" class="comment-info"><span class="comment-age">(26 Aug '13, 02:53)</span> FMvdBergh</div></div><span id="24596"></span><div id="comment-24596" class="comment"><div id="post-24596-score" class="comment-score"></div><div class="comment-text"><p>OK I'm jumping in here because I've run into this issue more than once. I set it up to capture 5-20M files and use a ring buffer of say 200 files. It will capture 5-20 files and then crash. It appears to be that the smaller I set up the file sizes the larger number of files it creates before crashing. So now I see this dumpcap and think ok this sounds like the direction I need to go. So now I'm off to research this. This appears to be tshark which I've never run....</p></div><div id="comment-24596-info" class="comment-info"><span class="comment-age">(11 Sep '13, 18:25)</span> ChiefWFB</div></div></div><div id="comment-tools-23982" class="comment-tools"></div><div class="clear"></div><div id="comment-23982-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

