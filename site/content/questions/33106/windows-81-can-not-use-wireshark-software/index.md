+++
type = "question"
title = "windows 8.1 Can not use Wireshark software"
description = '''My windows get upgrade form Windows 8 To windows 8.1，The software Wireshark Can not use 。 When I start Wireshark，the software stop at “network protocol analyzer ，loading configuration files”'''
date = "2014-05-27T07:34:00Z"
lastmod = "2014-05-27T07:38:00Z"
weight = 33106
keywords = [ "windows", "8.1", "use", "not", "can" ]
aliases = [ "/questions/33106" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [windows 8.1 Can not use Wireshark software](/questions/33106/windows-81-can-not-use-wireshark-software)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33106-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My windows get upgrade form Windows 8 To windows 8.1，The software Wireshark Can not use 。</p><p>When I start Wireshark，the software stop at “network protocol analyzer ，loading configuration files”</p></div><div id="question-tags" class="tags-container tags">windows 8.1 use not can</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 May '14, 07:34</strong></p><img src="https://secure.gravatar.com/avatar/530c9c1b84f744c704ae34af2fc4953e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="taodegui&#39;s gravatar image" /><p>taodegui<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="taodegui has no accepted answers">0%</span></p></div></div><div id="comments-container-33106" class="comments-container"><span id="33122"></span><div id="comment-33122" class="comment"><div id="post-33122-score" class="comment-score"></div><div class="comment-text"><p>It might also be noted that need reinstalling Winpcap， After that it's OK.</p></div><div id="comment-33122-info" class="comment-info"><span class="comment-age">(27 May '14, 19:25)</span> taodegui</div></div></div><div id="comment-tools-33106" class="comment-tools"></div><div class="clear"></div><div id="comment-33106-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33107"></span>

<div id="answer-container-33107" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33107-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try uninstalling and reinstalling again. Wireshark runs fine on Win 8.1 for me.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 May '14, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-33107" class="comments-container"><span id="34163"></span><div id="comment-34163" class="comment"><div id="post-34163-score" class="comment-score"></div><div class="comment-text"><p>After resimstalling again same problem accour. I cant found the solution. Maybe I turn back to Win7</p><p>Emre.</p></div><div id="comment-34163-info" class="comment-info"><span class="comment-age">(25 Jun '14, 05:22)</span> emre</div></div><span id="34164"></span><div id="comment-34164" class="comment"><div id="post-34164-score" class="comment-score"></div><div class="comment-text"><p>I use Wireshark on Win 8.1 on two different machines multiple times per day without any issues. Both machines were installed as 8.1, not upgraded.</p><p>Can you stop any running wireshark instances and check for a running instance of dumpcap.exe? If you find one, kill it and try starting Wireshark again.</p></div><div id="comment-34164-info" class="comment-info"><span class="comment-age">(25 Jun '14, 05:35)</span> grahamb ♦</div></div><span id="34171"></span><div id="comment-34171" class="comment"><div id="post-34171-score" class="comment-score"></div><div class="comment-text"><p>Ensure to reinstall WinPCAP with administrative rights, this is the usual culprit for issues with Windows 8.1.</p></div><div id="comment-34171-info" class="comment-info"><span class="comment-age">(25 Jun '14, 08:59)</span> Pascal Quantin</div></div><span id="34173"></span><div id="comment-34173" class="comment"><div id="post-34173-score" class="comment-score"></div><div class="comment-text"><p>@Pascal Quantin</p><p>What do you mean by "Install with Admin Rights", right click and select "Run As Administrator"? The installer (IMHO) always asks for elevation, so what does "Run As Administrator" bring to the party.</p><p>FWIW, I've never had to do that on any install, just say yes to the UAC elevation prompt.</p></div><div id="comment-34173-info" class="comment-info"><span class="comment-age">(25 Jun '14, 09:22)</span> grahamb ♦</div></div><span id="34179"></span><div id="comment-34179" class="comment"><div id="post-34179-score" class="comment-score"></div><div class="comment-text"><p>Yes that's what I meant, sorry for the confusion. I do not have UAC activated on my PC so I was not sure whether the installer was prompting the user or not.</p></div><div id="comment-34179-info" class="comment-info"><span class="comment-age">(25 Jun '14, 10:01)</span> Pascal Quantin</div></div></div><div id="comment-tools-33107" class="comment-tools"></div><div class="clear"></div><div id="comment-33107-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

