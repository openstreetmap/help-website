+++
type = "question"
title = "Extract files from pcap file programatically"
description = '''I want to extract the files such as pdfs, images, javascripts etc. from the pcap file captured using wireshark. I want the protocols such as http, ftp, smtp, pop supported. Please let me know how can i extract the files using code preferably c programming to do the same.'''
date = "2015-06-16T17:11:00Z"
lastmod = "2015-06-17T08:38:00Z"
weight = 43223
keywords = [ "files", "extract", "code", "pcap" ]
aliases = [ "/questions/43223" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Extract files from pcap file programatically](/questions/43223/extract-files-from-pcap-file-programatically)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43223-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to extract the files such as pdfs, images, javascripts etc. from the pcap file captured using wireshark. I want the protocols such as http, ftp, smtp, pop supported. Please let me know how can i extract the files using code preferably c programming to do the same.</p></div><div id="question-tags" class="tags-container tags">files extract code pcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jun '15, 17:11</strong></p><img src="https://secure.gravatar.com/avatar/01dc4abf2dc404ecc82284d9a3879637?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kruthi&#39;s gravatar image" /><p>kruthi<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kruthi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Jun '15, 08:38</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-43223" class="comments-container"></div><div id="comment-tools-43223" class="comment-tools"></div><div class="clear"></div><div id="comment-43223-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43266"></span>

<div id="answer-container-43266" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43266-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is able to export objects from a pcap file, but only for HTTP, DICOM and SMB. If you want to know how that works, take a look at the Wireshark source code (Files: export_object*.c).</p><p>An alternative are the following tools:</p><blockquote><p><a href="http://www.xplico.org">http://www.xplico.org</a><br />
<a href="http://sourceforge.net/projects/networkminer/">http://sourceforge.net/projects/networkminer/</a><br />
<a href="https://github.com/caesar0301/awesome-pcaptools#fileextraction">https://github.com/caesar0301/awesome-pcaptools#fileextraction</a><br />
<a href="http://isc.sans.edu/diary/Tools+for+extracting+files+from+pcaps/6961">http://isc.sans.edu/diary/Tools+for+extracting+files+from+pcaps/6961</a><br />
<a href="https://code.google.com/p/nfex/">https://code.google.com/p/nfex/</a></p></blockquote><p>Either use them directly, or take a look at the code to learn from it.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '15, 08:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Jun '15, 08:38</p></div></div><div id="comments-container-43266" class="comments-container"></div><div id="comment-tools-43266" class="comment-tools"></div><div class="clear"></div><div id="comment-43266-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

