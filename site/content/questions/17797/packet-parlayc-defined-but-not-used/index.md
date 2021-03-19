+++
type = "question"
title = "packet-parlay.c ... defined but not used"
description = '''Hello, I&#x27;m [trying to] install wireshark-1.8.4 on CentOS 6.3. Version details: [root@daedalus wireshark-1.8.4]# uname -r 2.6.32-279.19.1.el6.x86_64 I have uncompressed the bz2 and run ./configure (all passed OK after yum-ming a couple of packages). When I run &#x27;make&#x27; the output stops at: packet-parla...'''
date = "2013-01-20T15:36:00Z"
lastmod = "2013-01-21T08:41:00Z"
weight = 17797
keywords = [ "6.3", "centos", "wireshark" ]
aliases = [ "/questions/17797" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [packet-parlay.c ... defined but not used](/questions/17797/packet-parlayc-defined-but-not-used)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17797-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm [trying to] install wireshark-1.8.4 on CentOS 6.3. Version details:</p><p>[[email protected] wireshark-1.8.4]# uname -r 2.6.32-279.19.1.el6.x86_64</p><p>I have uncompressed the bz2 and run ./configure (all passed OK after yum-ming a couple of packages). When I run 'make' the output stops at:</p><p>packet-parlay.c:82294: warning: 'decode_org_csapi_fw_TpLoadPolicy_st' defined but not used packet-parlay.c:82360: warning: 'decode_org_csapi_fw_TpLoadInitVal_st' defined but not used packet-parlay.c:83511: warning: 'decode_org_csapi_ui_TpUIEventInfo_st' defined but not used</p><p>I have saved the full history if you'd like to see it.</p><p>Any pointers? I'm fairly new to Linux/CentOS so please excuse any ignorance on my part!</p><p>Cheers,</p><p>Ben</p></div><div id="question-tags" class="tags-container tags">6.3 centos wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jan '13, 15:36</strong></p><img src="https://secure.gravatar.com/avatar/3ff7bf66c7eb4ca1f4f949e83e23e5d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Norbert_von_Batfink&#39;s gravatar image" /><p>Norbert_von_...<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Norbert_von_Batfink has no accepted answers">0%</span></p></div></div><div id="comments-container-17797" class="comments-container"><span id="17799"></span><div id="comment-17799" class="comment"><div id="post-17799-score" class="comment-score"></div><div class="comment-text"><p>That dissector is auto-generated; the auto-generator produces a lot of routines that aren't used.</p><p>There are some other generated .c files that produce warnings.</p><p>We're aware of them, but squelching the warnings is not as high a priority as fixing warnings in human-written code; they're just warnings, and compilers that support -Werror (to turn warnings into errors) aren't passed that flag when compiling those generated .c files.</p><p>Was there an actual <em>error</em> that stopped the compilation? Or did -Werror happen to get passed to the compiler when compiling packet-parlay.c?</p></div><div id="comment-17799-info" class="comment-info"><span class="comment-age">(20 Jan '13, 16:29)</span> Guy Harris ♦♦</div></div><span id="17800"></span><div id="comment-17800" class="comment"><div id="post-17800-score" class="comment-score"></div><div class="comment-text"><p>There wasn't an error as such reported in the output, it just appeared to stop and hang at that point.</p><p>When I ctrl+C'd, there were interrupts by the [make] tasks with an error reported, but not sure if that's down to me killing the task. Can provide the output when next at my machine if you'd like to see it.</p><p>Does the compiler take a long time at that point, or should I do something with -Werror?</p></div><div id="comment-17800-info" class="comment-info"><span class="comment-age">(20 Jan '13, 17:50)</span> Norbert_von_...</div></div><span id="17801"></span><div id="comment-17801" class="comment"><div id="post-17801-score" class="comment-score"></div><div class="comment-text"><p>The compiler takes a long time at that point. It's a big file. If your machine doesn't have enough main memory, it could not only take a lot of CPU time, but also cause thrashing.</p></div><div id="comment-17801-info" class="comment-info"><span class="comment-age">(20 Jan '13, 19:35)</span> Guy Harris ♦♦</div></div><span id="17807"></span><div id="comment-17807" class="comment"><div id="post-17807-score" class="comment-score"></div><div class="comment-text"><p>I must apologise - all I needed was to learn a bit of patience. Remarkable, really, seeing as I come from a Windows background (patience of a saint, comes to mind) and also drink Guinness. Anyways, have gotten so used to everything Linux-related happening at the speed of light I was taken aback at the prospect of having to wait for something, so had just assumed it was broken!</p><p>Thanks for your replies though - greatly appreciated. Now off to discover the deep, dark depths of packet socket...</p></div><div id="comment-17807-info" class="comment-info"><span class="comment-age">(21 Jan '13, 07:29)</span> Norbert_von_...</div></div></div><div id="comment-tools-17797" class="comment-tools"></div><div class="clear"></div><div id="comment-17797-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17812"></span>

<div id="answer-container-17812" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17812-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As Guy said (maybe I should just convert his Comment to an Answer, hmmm), packet-parlay.c can take a LONG time to compile. The time taken to compile varies not only with hardware but also compiler versions. Some improvements have been made in trunk (Wireshark 1.9); in the 1.8.x versions you just need to wait a while (we've seen reports as high as 10 <em>minutes</em> to compile that one file).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '13, 08:41</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-17812" class="comments-container"><span id="17815"></span><div id="comment-17815" class="comment"><div id="post-17815-score" class="comment-score"></div><div class="comment-text"><p>...And if you don't want to wait that long you can always kick it out of epan/dissectors/Makefile.common.</p></div><div id="comment-17815-info" class="comment-info"><span class="comment-age">(21 Jan '13, 09:04)</span> Jaap ♦</div></div></div><div id="comment-tools-17812" class="comment-tools"></div><div class="clear"></div><div id="comment-17812-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

