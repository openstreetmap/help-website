+++
type = "question"
title = "Error LNK2019"
description = '''Hi, I&#x27;m trying to create a new dissector based on the tftp disector. For that I copy/cut packet-tftp.c from epan/dissector/ to a new folder /dissector/myProject. I replaced &quot;tftp&quot; by &quot;myDissector&quot; in this file. During the compilation, I get an error like this: packet-myDissector.obj : error LNK2019:...'''
date = "2011-01-11T04:38:00Z"
lastmod = "2011-03-26T05:17:00Z"
weight = 1700
keywords = [ "dissector" ]
aliases = [ "/questions/1700" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Error LNK2019](/questions/1700/error-lnk2019)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1700-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm trying to create a new dissector based on the tftp disector. For that I copy/cut packet-tftp.c from epan/dissector/ to a new folder /dissector/myProject. I replaced "tftp" by "myDissector" in this file. During the compilation, I get an error like this:</p><p>packet-myDissector.obj : error LNK2019: symbole externe non résolu tvb_get_seasonal_string référencé dans la fonction dissect_myDissector_message myDissector.dll : fatal error LNK1120: 1 external non résolus.</p><p>The tvb_get_seasonal_string is in the tvbuff.c file, but tftp use other fonction from this file and it does'nt crash. I don't understand why 'im getting this error, can someone explain to me how to fix this error plz.</p><p>Thx Alrik</p></div><div id="question-tags" class="tags-container tags">dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jan '11, 04:38</strong></p><img src="https://secure.gravatar.com/avatar/878c62d2f87284c01ed450e8df7883a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alrik&#39;s gravatar image" /><p>Alrik<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alrik has no accepted answers">0%</span></p></div></div><div id="comments-container-1700" class="comments-container"></div><div id="comment-tools-1700" class="comment-tools"></div><div class="clear"></div><div id="comment-1700-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3140"></span>

<div id="answer-container-3140" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3140-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The libwireshark.dll exports only functions that are defined in the <code>libwireshark.def</code> file. The entries in the .DEF file are usually added on request. That means that the export list of the current Wireshark distribution is always somewhat behind the requirements.</p><p>You can modify the .def file, and verify that it will fullfill your requirements. Than you can send the change request to the core development team and you might get a compatible Libwireshark.dll in the next version. But you need to tell you dissector users to update to this 'next version'.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '11, 05:17</strong></p><img src="https://secure.gravatar.com/avatar/585595b6a24df9b742ebc186788e9a8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="harper&#39;s gravatar image" /><p>harper<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="harper has no accepted answers">0%</span></p></div></div><div id="comments-container-3140" class="comments-container"></div><div id="comment-tools-3140" class="comment-tools"></div><div class="clear"></div><div id="comment-3140-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1702"></span>

<div id="answer-container-1702" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1702-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not sure where you placed your file, it should go into /epan/dissectors/ and should be added to Makefile.common</p><p>See <a href="http://anonsvn.wireshark.org/wireshark/trunk/doc/README.developer">/doc/README.developer</a> section 1.2 and 1.9</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jan '11, 06:32</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-1702" class="comments-container"><span id="1703"></span><div id="comment-1703" class="comment"><div id="post-1703-score" class="comment-score"></div><div class="comment-text"><p>The other plugins I wrote are in the /plugins/ folder, and worked succesfully. I read that it can be caused by the missing declaration of tvb_get_seasonal_string in libwireshark.def file, when I add it, it seems to work. But, is there any other solution, because I don't want to modify the libwireshark.def file?</p></div><div id="comment-1703-info" class="comment-info"><span class="comment-age">(11 Jan '11, 06:41)</span> Alrik</div></div></div><div id="comment-tools-1702" class="comment-tools"></div><div class="clear"></div><div id="comment-1702-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

