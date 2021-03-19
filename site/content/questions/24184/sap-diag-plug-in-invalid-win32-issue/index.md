+++
type = "question"
title = "SAP diag Plug-in invalid Win32 issue"
description = '''Hi guys, got invalid Win32 application&#x27;s issue running SAP Diag Plug-in from http://blog.ptsecurity.com/2011/10/sap-diag-decompress-plugin-for.html on Win7. Any Idea, how to capture SAP diag with latest Wireshark on Win7? Thx Reza666'''
date = "2013-08-30T01:46:00Z"
lastmod = "2014-03-12T16:04:00Z"
weight = 24184
keywords = [ "sap" ]
aliases = [ "/questions/24184" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [SAP diag Plug-in invalid Win32 issue](/questions/24184/sap-diag-plug-in-invalid-win32-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24184-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys, got invalid Win32 application's issue running SAP Diag Plug-in from <a href="http://blog.ptsecurity.com/2011/10/sap-diag-decompress-plugin-for.html">http://blog.ptsecurity.com/2011/10/sap-diag-decompress-plugin-for.html</a> on Win7.</p><p>Any Idea, how to capture SAP diag with latest Wireshark on Win7?</p><p>Thx Reza666</p></div><div id="question-tags" class="tags-container tags">sap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Aug '13, 01:46</strong></p><img src="https://secure.gravatar.com/avatar/3057867f6aaee6adcac69f83d02c42d0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="reza666&#39;s gravatar image" /><p>reza666<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="reza666 has no accepted answers">0%</span></p></div></div><div id="comments-container-24184" class="comments-container"></div><div id="comment-tools-24184" class="comment-tools"></div><div class="clear"></div><div id="comment-24184-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="24187"></span>

<div id="answer-container-24187" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24187-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That plugin is produced by a third party so you'll have to ask them for support. Furthermore they are distributing it without access to the source which not only makes fixing whatever issues it has impossible for anyone other than the originators, it's probably in violation of the GPL that Wireshark is released under.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '13, 02:11</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-24187" class="comments-container"><span id="24188"></span><div id="comment-24188" class="comment"><div id="post-24188-score" class="comment-score"></div><div class="comment-text"><blockquote><p>it's probably in <strong>violation of the GPL</strong> that Wireshark is released under.</p></blockquote><p>good point!</p><blockquote><p><a href="http://www.gnu.org/licenses/gpl-faq.html#GPLPluginsInNF">http://www.gnu.org/licenses/gpl-faq.html#GPLPluginsInNF</a></p></blockquote></div><div id="comment-24188-info" class="comment-info"><span class="comment-age">(30 Aug '13, 02:13)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-24187" class="comment-tools"></div><div class="clear"></div><div id="comment-24187-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24186"></span>

<div id="answer-container-24186" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24186-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The link contains only a binary version of the plugin and that is only compatible with certain Wireshark versions, the plugin was developed/compiled for.</p><p>If you want to use the plugin with a current Wireshark version, you need to ask the author of that plugin to provide either the source code (there is a hint about the code on the page) or a new binary release of the plugin.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '13, 02:10</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Aug '13, 02:12</p></div></div><div id="comments-container-24186" class="comments-container"></div><div id="comment-tools-24186" class="comment-tools"></div><div class="clear"></div><div id="comment-24186-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30745"></span>

<div id="answer-container-30745" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30745-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi ! Probable out of date, but checking in just to mention that there's another plugin for dissecting SAP protocols traffic from Core Security you can try.</p><p>Check it out at: <a href="http://corelabs.coresecurity.com/index.php?action=view&amp;module=Wiki&amp;name=SAP_Dissection_plu-gin_for_Wireshark&amp;type=tool">http://corelabs.coresecurity.com/index.php?action=view&amp;module=Wiki&amp;name=SAP_Dissection_plu-gin_for_Wireshark&amp;type=tool</a></p><p>Also there's a good review of different sniffing tools at <a href="http://www.daniel-berlin.de/security/sap-sec/sniffing-sap-gui-passwords/">http://www.daniel-berlin.de/security/sap-sec/sniffing-sap-gui-passwords/</a> and <a href="http://www.daniel-berlin.de/security/sap-sec/sniffing-sap-gui-passwords-part-2/">http://www.daniel-berlin.de/security/sap-sec/sniffing-sap-gui-passwords-part-2/</a></p><p>Cheers.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '14, 16:04</strong></p><img src="https://secure.gravatar.com/avatar/3db2b8a556c32a6fbc6e288df6d21815?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mgallo&#39;s gravatar image" /><p>mgallo<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mgallo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Mar '14, 18:10</p></div></div><div id="comments-container-30745" class="comments-container"><span id="30747"></span><div id="comment-30747" class="comment"><div id="post-30747-score" class="comment-score"></div><div class="comment-text"><p>It's:</p><p><a href="http://corelabs.coresecurity.com/index.php?action=view&amp;module=Wiki&amp;name=SAP_Dissection_plu-gin_for_Wireshark&amp;type=tool">http://corelabs.coresecurity.com/index.php?action=view&amp;module=Wiki&amp;name=SAP_Dissection_plu-gin_for_Wireshark&amp;type=tool</a></p><p>No period at the end (the HMTL link in your comment has the period in the URL).</p></div><div id="comment-30747-info" class="comment-info"><span class="comment-age">(12 Mar '14, 17:51)</span> Hadriel</div></div><span id="30748"></span><div id="comment-30748" class="comment"><div id="post-30748-score" class="comment-score"></div><div class="comment-text"><p>Thanks, fixed !</p></div><div id="comment-30748-info" class="comment-info"><span class="comment-age">(12 Mar '14, 18:10)</span> mgallo</div></div></div><div id="comment-tools-30745" class="comment-tools"></div><div class="clear"></div><div id="comment-30745-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

