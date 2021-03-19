+++
type = "question"
title = "SMB protocol parsing BUG found"
description = '''Hi, when you parsing SMB protocol requests you parse SMB_COM_TRANSACTION2 (0x32) command and SMB_COM_TRANSACTION2_SECONDARY (0x33) command as commands that have the equal request parameters structure. But this is mistake. SMB_COM_TRANSACTION2_SECONDARY command have it&#x27;s own parameters structure: SMB...'''
date = "2017-05-06T04:19:00Z"
lastmod = "2017-05-06T04:22:00Z"
weight = 61266
keywords = [ "smb", "structure" ]
aliases = [ "/questions/61266" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SMB protocol parsing BUG found](/questions/61266/smb-protocol-parsing-bug-found)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61266-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, when you parsing SMB protocol requests you parse SMB_COM_TRANSACTION2 (0x32) command and SMB_COM_TRANSACTION2_SECONDARY (0x33) command as commands that have the equal request parameters structure. But this is mistake.</p><p>SMB_COM_TRANSACTION2_SECONDARY command have it's own parameters structure:</p><p>SMB_Parameters { UCHAR WordCount; Words { USHORT TotalParameterCount; USHORT TotalDataCount; USHORT ParameterCount; USHORT ParameterOffset; USHORT ParameterDisplacement; USHORT DataCount; USHORT DataOffset; USHORT DataDisplacement; USHORT FID; } }</p><p>SMB_Data { USHORT ByteCount; Bytes { UCHAR Pad1[]; UCHAR Trans2_Parameters[ParameterCount]; UCHAR Pad2[]; UCHAR Trans2_Data[DataCount]; } }</p><p>Detailed here: <a href="https://msdn.microsoft.com/en-us/library/ee442192.aspx">https://msdn.microsoft.com/en-us/library/ee442192.aspx</a> <a href="https://msdn.microsoft.com/en-us/library/ee442105.aspx">https://msdn.microsoft.com/en-us/library/ee442105.aspx</a></p></div><div id="question-tags" class="tags-container tags">smb structure</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 May '17, 04:19</strong></p><img src="https://secure.gravatar.com/avatar/a2de17bf1c9b167a13bd9070edbded3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexweb&#39;s gravatar image" /><p>alexweb<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexweb has no accepted answers">0%</span></p></div></div><div id="comments-container-61266" class="comments-container"></div><div id="comment-tools-61266" class="comment-tools"></div><div class="clear"></div><div id="comment-61266-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61267"></span>

<div id="answer-container-61267" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61267-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wrong place to report this; please open a bug report at</p><p><a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> and attach a PCAP file if you can.</p><p>Thanks!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 May '17, 04:22</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-61267" class="comments-container"></div><div id="comment-tools-61267" class="comment-tools"></div><div class="clear"></div><div id="comment-61267-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

