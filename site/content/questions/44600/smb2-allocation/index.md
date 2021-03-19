+++
type = "question"
title = "SMB2 Allocation"
description = '''Hello, I&#x27;m curious how to use the Allocation Size of the field SMB2_FS_INFO_07. I have a Windows client connecting to a file system on a NAS device. Allocation Size 655360 Caller Free Units 645372 Actual Free Units 645372 Sectors/Unit 64 Bytes per Sector 512 So what am I looking at here, the word &#x27;F...'''
date = "2015-07-29T11:17:00Z"
lastmod = "2015-07-29T11:17:00Z"
weight = 44600
keywords = [ "smb2" ]
aliases = [ "/questions/44600" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SMB2 Allocation](/questions/44600/smb2-allocation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44600-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm curious how to use the Allocation Size of the field SMB2_FS_INFO_07. I have a Windows client connecting to a file system on a NAS device.</p><p>Allocation Size 655360 Caller Free Units 645372 Actual Free Units 645372 Sectors/Unit 64 Bytes per Sector 512</p><p>So what am I looking at here, the word 'FS' would make me think the Allocation Size is the total size of the file system itself, would that be correct?</p><p>If not the total size of the file system, would it maybe be the reporting if data within the CIFS share as reported by Windows?</p><p>The measurement is in bytes?</p><p>I will add this to make it clear as well.</p><p>How can I determine using SBM2 protocol the size on disk a file is using or reporting in Wireshark?</p></div><div id="question-tags" class="tags-container tags">smb2</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jul '15, 11:17</strong></p><img src="https://secure.gravatar.com/avatar/4136f47fd762c7ca82d7455c7d5b6ee6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ew0506&#39;s gravatar image" /><p>ew0506<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ew0506 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Jul '15, 11:56</p></div></div><div id="comments-container-44600" class="comments-container"><span id="44841"></span><div id="comment-44841" class="comment"><div id="post-44841-score" class="comment-score"></div><div class="comment-text"><p>Does this help? <a href="https://msdn.microsoft.com/en-us/library/cc232088.aspx">https://msdn.microsoft.com/en-us/library/cc232088.aspx</a></p></div><div id="comment-44841-info" class="comment-info"><span class="comment-age">(04 Aug '15, 15:37)</span> PaulOfford</div></div></div><div id="comment-tools-44600" class="comment-tools"></div><div class="clear"></div><div id="comment-44600-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

