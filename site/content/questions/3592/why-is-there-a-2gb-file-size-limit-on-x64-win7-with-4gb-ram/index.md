+++
type = "question"
title = "Why is there a 2GB file size limit on x64 Win7 with 4GB RAM"
description = '''I have the 64 bit version of Wireshark installed Version 1.4.5 (SVN Rev 36650 from /trunk-1.4) on Win7 Ultimate with 4GB of RAM. I am trying to load a 1.3GB PCAP file. When Wireshark gets to 2GB of memory allocated even though there is 1GB free it crashes. I was under the impression that the x64 ver...'''
date = "2011-04-18T18:32:00Z"
lastmod = "2011-04-18T18:37:00Z"
weight = 3592
keywords = [ "memory" ]
aliases = [ "/questions/3592" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why is there a 2GB file size limit on x64 Win7 with 4GB RAM](/questions/3592/why-is-there-a-2gb-file-size-limit-on-x64-win7-with-4gb-ram)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3592-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have the 64 bit version of Wireshark installed Version 1.4.5 (SVN Rev 36650 from /trunk-1.4) on Win7 Ultimate with 4GB of RAM. I am trying to load a 1.3GB PCAP file. When Wireshark gets to 2GB of memory allocated even though there is 1GB free it crashes.</p><p>I was under the impression that the x64 version of Wireshark did not have any limitations on memory. Any ideas?</p></div><div id="question-tags" class="tags-container tags">memory</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '11, 18:32</strong></p><img src="https://secure.gravatar.com/avatar/3412e30a2549d7bba26454ed07541eca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gff1stof3&#39;s gravatar image" /><p>gff1stof3<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gff1stof3 has no accepted answers">0%</span></p></div></div><div id="comments-container-3592" class="comments-container"></div><div id="comment-tools-3592" class="comment-tools"></div><div class="clear"></div><div id="comment-3592-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3594"></span>

<div id="answer-container-3594" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3594-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Given that the file is only 1.3GB, presumably you mean "2GB address space size limit" rather than "2GB file size limit". (There's a 2GB file size limit in 1.4.5 because, in all Ethereal/Wireshark releases prior to 1.5, and in the 1.5 (trunk) until recently, the calls used to seek into the capture file used a 32-bit file offset, even on most 64-bit platforms, including Windows.)</p><p>I'd report that as a bug at <a href="http://bugs.wireshark.org">the Wireshark Bugzilla</a>. Please give as much information as you can, including any error information from Windows.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '11, 18:37</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-3594" class="comments-container"><span id="4316"></span><div id="comment-4316" class="comment"><div id="post-4316-score" class="comment-score"></div><div class="comment-text"><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5979">Bug 5979</a> is now tracking this issue.</p></div><div id="comment-4316-info" class="comment-info"><span class="comment-age">(01 Jun '11, 06:45)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-3594" class="comment-tools"></div><div class="clear"></div><div id="comment-3594-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

