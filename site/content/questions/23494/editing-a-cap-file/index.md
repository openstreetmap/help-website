+++
type = "question"
title = "Editing a .cap-file"
description = '''Hello! I have captured the PPPoE/PPP-Session Packets at my DSL-Router and want to use the .cap file for Trainings. Naturally I want to remove my PAP-ID and Password for Security reasons. How can I edit a .cap-File? I tried the Windows Editor, but it alters something in the file so that Wireshark ref...'''
date = "2013-08-01T02:08:00Z"
lastmod = "2013-08-05T01:49:00Z"
weight = 23494
keywords = [ ".cap", "editing", "file" ]
aliases = [ "/questions/23494" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Editing a .cap-file](/questions/23494/editing-a-cap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23494-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello! I have captured the PPPoE/PPP-Session Packets at my DSL-Router and want to use the .cap file for Trainings. Naturally I want to remove my PAP-ID and Password for Security reasons. How can I edit a .cap-File? I tried the Windows Editor, but it alters something in the file so that Wireshark refuses to open it.</p><p>Any suggestions?</p></div><div id="question-tags" class="tags-container tags">.cap editing file</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Aug '13, 02:08</strong></p><img src="https://secure.gravatar.com/avatar/e876c59741ed9f39704354f1f509f375?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="udo229&#39;s gravatar image" /><p>udo229<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="udo229 has no accepted answers">0%</span></p></div></div><div id="comments-container-23494" class="comments-container"></div><div id="comment-tools-23494" class="comment-tools"></div><div class="clear"></div><div id="comment-23494-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="23497"></span>

<div id="answer-container-23497" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23497-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>PCAP files are binary files so you can't edit them with most text editors. Some UNIX/Linux editors like <code>vile</code> (Vi Like Emacs) advertise themselves as being 8-bit clean (so you can edit binary files without destroying them) but still aren't ideal for editing binary files.</p><p>A much better solution in the UNIX/Linux (and also Cygwin) worlds is <code>bvi</code>. It is a true hex editor. I've edited PCAP files with it before (with Wireshark running on the side) and it has worked well enough for small changes.</p><p>There may be native Windows binary editors but I'm not aware of them.</p><p>Wireshark does have some basic/experimental packet editing features but they are not compiled in by default; to get them you would need to compile your own version of Wireshark with the feature enabled.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '13, 06:16</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-23497" class="comments-container"><span id="23499"></span><div id="comment-23499" class="comment"><div id="post-23499-score" class="comment-score"></div><div class="comment-text"><p>Perfect! I found a binary Editor for Windows (FrHed) and it worked out perfect!</p><p>Thank You very much!</p></div><div id="comment-23499-info" class="comment-info"><span class="comment-age">(01 Aug '13, 06:41)</span> udo229</div></div></div><div id="comment-tools-23497" class="comment-tools"></div><div class="clear"></div><div id="comment-23497-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23542"></span>

<div id="answer-container-23542" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23542-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use <a href="http://mh-nexus.de/en/hxd/">HxD</a>, a freeware hex editor, to edit capture files. It works fine on Windows.<br />
You can download HxD <a href="http://mh-nexus.de/en/downloads.php?product=HxD">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Aug '13, 22:45</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></p></div></div><div id="comments-container-23542" class="comments-container"></div><div id="comment-tools-23542" class="comment-tools"></div><div class="clear"></div><div id="comment-23542-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23548"></span>

<div id="answer-container-23548" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23548-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is also <a href="http://www.tracewrangler.com/">TraceWrangler</a>, a capture sanitisation tool for pcapng files made by @Jasper. I don't know if it deals with PPP Id's and passwords though.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '13, 01:49</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-23548" class="comments-container"><span id="23549"></span><div id="comment-23549" class="comment"><div id="post-23549-score" class="comment-score"></div><div class="comment-text"><p>no, it does not handle ppp headers yet, but I admit that this question made me look at a trace to see how much work it is :-)</p></div><div id="comment-23549-info" class="comment-info"><span class="comment-age">(05 Aug '13, 02:57)</span> Jasper ♦♦</div></div></div><div id="comment-tools-23548" class="comment-tools"></div><div class="clear"></div><div id="comment-23548-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

