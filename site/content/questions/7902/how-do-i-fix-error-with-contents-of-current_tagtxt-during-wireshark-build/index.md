+++
type = "question"
title = "How do I fix error with contents of current_tag.txt during Wireshark build"
description = '''I&#x27;ve run nmake -f Makefile.nmake setup with out any errors. When I run nmake -f Makefile.nmake check_libs I get: ERROR: The contents of C:&#92;wireshark-win32-libs&#92;current_tag.txt is (unknown). It should be 2011-06-27. Wireshark is ready to build. Then when I run nmake -f Makefile.nmake all I get this e...'''
date = "2011-12-11T17:54:00Z"
lastmod = "2011-12-12T18:32:00Z"
weight = 7902
keywords = [ "win32", "errors", "build", "nmake" ]
aliases = [ "/questions/7902" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I fix error with contents of current\_tag.txt during Wireshark build](/questions/7902/how-do-i-fix-error-with-contents-of-current_tagtxt-during-wireshark-build)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7902-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've run nmake -f Makefile.nmake setup with out any errors. When I run nmake -f Makefile.nmake check_libs I get:</p><p>ERROR: The contents of C:\wireshark-win32-libs\current_tag.txt is (unknown). It should be 2011-06-27.</p><p>Wireshark is ready to build.</p><p>Then when I run nmake -f Makefile.nmake all I get this error:<br />
</p><p>ERROR: The contents of C:\wireshark-win32-libs\current_tag.txt is (unknown). It should be 2011-06-27.</p><p>? Wireshark Libraries not up-to-date ? ? Do you need to run nmake -f Makefile.nmake setup ?</p><p>NMAKE : fatal error U1077: 'exit' : return code '0x1' Stop.</p><p>I have configured the Config.nmake for my compiler and have followed all the directions. Im trying to build this on windows using visual studio express 2008.</p></div><div id="question-tags" class="tags-container tags">win32 errors build nmake</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Dec '11, 17:54</strong></p><img src="https://secure.gravatar.com/avatar/dd5e2e3639af31f77026c2808f357671?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smithc&#39;s gravatar image" /><p>smithc<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smithc has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Dec '11, 02:44</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-7902" class="comments-container"><span id="7910"></span><div id="comment-7910" class="comment"><div id="post-7910-score" class="comment-score"></div><div class="comment-text"><p>Where are your libraries stored? Is it C:\wireshark-win32-libs-1.6 or somewhere else?</p></div><div id="comment-7910-info" class="comment-info"><span class="comment-age">(12 Dec '11, 04:25)</span> Jaap ♦</div></div><span id="7934"></span><div id="comment-7934" class="comment"><div id="post-7934-score" class="comment-score"></div><div class="comment-text"><p>yeah, it's in C:\wireshark-win32-libs-1.6. I got Wireshark to compile in WinXP, but I still can't get it to compile in Win7.</p></div><div id="comment-7934-info" class="comment-info"><span class="comment-age">(12 Dec '11, 23:19)</span> smithc</div></div><span id="7936"></span><div id="comment-7936" class="comment"><div id="post-7936-score" class="comment-score"></div><div class="comment-text"><p>There should be a file called current_tag.txt in there. What is its contents?</p></div><div id="comment-7936-info" class="comment-info"><span class="comment-age">(13 Dec '11, 01:58)</span> Jaap ♦</div></div><span id="7938"></span><div id="comment-7938" class="comment"><div id="post-7938-score" class="comment-score"></div><div class="comment-text"><p>The contents are 2011-06-27. Thats whats confusing. Maybe its looking somewhere else for current_tag.txt?</p></div><div id="comment-7938-info" class="comment-info"><span class="comment-age">(13 Dec '11, 02:57)</span> smithc</div></div><span id="7941"></span><div id="comment-7941" class="comment"><div id="post-7941-score" class="comment-score"></div><div class="comment-text"><p>You state that your libraries are in "C:\wireshark-win32-libs-1.6" but the error message says the setting for libraries is "C:\wireshark-win32-libs". Which is correct?</p></div><div id="comment-7941-info" class="comment-info"><span class="comment-age">(13 Dec '11, 03:30)</span> grahamb ♦</div></div><span id="7942"></span><div id="comment-7942" class="comment not_top_scorer"><div id="post-7942-score" class="comment-score"></div><div class="comment-text"><p>@graham: Whoo, why did you have to spill the beans ;)</p><p>@smithc: Graham may be onto something here. Are your path settings in config.nmake in order? Or, did you define WIRESHARK_LIB_DIR yourself?</p></div><div id="comment-7942-info" class="comment-info"><span class="comment-age">(13 Dec '11, 03:56)</span> Jaap ♦</div></div></div><div id="comment-tools-7902" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-7902-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7933"></span>

<div id="answer-container-7933" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7933-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Like the output indicates, you need to run <code>nmake -f Makefile.nmake setup</code> before running <code>nmake -f Makefile.nmake all</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '11, 18:32</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-7933" class="comments-container"><span id="8242"></span><div id="comment-8242" class="comment"><div id="post-8242-score" class="comment-score"></div><div class="comment-text"><p>I have the same problem</p><p>Tried using the "setup" but I get the same output</p><p>How can I solve this?</p><p>Thanks,</p><p>Armando</p></div><div id="comment-8242-info" class="comment-info"><span class="comment-age">(05 Jan '12, 14:02)</span> avr989</div></div><span id="8244"></span><div id="comment-8244" class="comment"><div id="post-8244-score" class="comment-score"></div><div class="comment-text"><p>thanks, I just ignored the error and run the setup, then I closed the cmd and opened it again. Then I followed again steps 2.2.6 thru 2.2.8 and everything went just fine.</p></div><div id="comment-8244-info" class="comment-info"><span class="comment-age">(05 Jan '12, 16:53)</span> avr989</div></div></div><div id="comment-tools-7933" class="comment-tools"></div><div class="clear"></div><div id="comment-7933-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

