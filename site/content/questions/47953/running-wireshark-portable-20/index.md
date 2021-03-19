+++
type = "question"
title = "running wireshark portable 2.0"
description = '''Hello,  I installed WiresharkPortable_2.0.0.paf.exe in my system and I can&#x27;t get it to work properly. The installation was done inside a Portable apps directory, that is created on its own partition.  Versions 1.x had no problem running here. I use windows7. First it asked for msvcr120 dll when tryi...'''
date = "2015-11-25T01:46:00Z"
lastmod = "2015-11-25T02:44:00Z"
weight = 47953
keywords = [ "gtk", "qt", "wireshark" ]
aliases = [ "/questions/47953" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [running wireshark portable 2.0](/questions/47953/running-wireshark-portable-20)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47953-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I installed WiresharkPortable_2.0.0.paf.exe in my system and I can't get it to work properly. The installation was done inside a Portable apps directory, that is created on its own partition. Versions 1.x had no problem running here. I use windows7.</p><p>First it asked for msvcr120 dll when trying to start all the exe files. After downloading and copying it (32 bit) to the wireshark directory, all the utilities (capinfos, mergecap, tshark) are working, and so is wireshark-gtk. But Wireshark.exe is still not running (unable to start correctly 0xc00007b). Is it something that I need to do to have it running in a portable way?</p></div><div id="question-tags" class="tags-container tags">gtk qt wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '15, 01:46</strong></p><img src="https://secure.gravatar.com/avatar/8979d3708607d42c61c44da210514487?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rovv&#39;s gravatar image" /><p>rovv<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rovv has no accepted answers">0%</span></p></div></div><div id="comments-container-47953" class="comments-container"></div><div id="comment-tools-47953" class="comment-tools"></div><div class="clear"></div><div id="comment-47953-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47956"></span>

<div id="answer-container-47956" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47956-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like a bug, possibly with the Qt DLLs used by 2.0 in the portable packaging. Please check for an existing entry first, and if not found raise a bug on the Wireshark <a href="https://bugs.wireshark.org">Bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '15, 02:44</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-47956" class="comments-container"><span id="47959"></span><div id="comment-47959" class="comment"><div id="post-47959-score" class="comment-score"></div><div class="comment-text"><p>That error is STATUS_INVALID_IMAGE_FORMAT, the description for which on <a href="https://msdn.microsoft.com/en-us/library/cc704588.aspx">Microsoft's list of NT status values</a> is</p><blockquote><p>{Bad Image} %hs is either not designed to run on Windows or it contains an error. Try installing the program again using the original installation media or contact your system administrator or the software vendor for support.</p></blockquote></div><div id="comment-47959-info" class="comment-info"><span class="comment-age">(25 Nov '15, 03:39)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-47956" class="comment-tools"></div><div class="clear"></div><div id="comment-47956-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

