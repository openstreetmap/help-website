+++
type = "question"
title = "SMB_FS_INFO_0x"
description = '''I would like to read about SMB_FS_INFO_0x requests. I&#x27;ve tried poking through: [MS-SMB2], [MS-FSCC], and [MS-FSMOD] -- no dice. Suggestions? In particular, I&#x27;m seeing hard-to-believe &#x27;Date Created&#x27; timestamps associated with a file in the traces I&#x27;m examining. Specifically, I want to know how the &#x27;C...'''
date = "2014-08-22T08:07:00Z"
lastmod = "2014-08-22T08:07:00Z"
weight = 35676
keywords = [ "documentation", "smb_fs_info_0x" ]
aliases = [ "/questions/35676" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SMB\_FS\_INFO\_0x](/questions/35676/smb_fs_info_0x)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35676-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to read about SMB_FS_INFO_0x requests.</p><p>I've tried poking through: [MS-SMB2], [MS-FSCC], and [MS-FSMOD] -- no dice.</p><p>Suggestions?</p><p>In particular, I'm seeing hard-to-believe 'Date Created' timestamps associated with a file in the traces I'm examining. Specifically, I want to know how the 'Created' time stamp is encoded in an SMB_FS_INFO_01 Response. I have two frames of interest: in one, the time stamp is encoded as '1' ... which suggests either a bug or perhaps that '1' connotes some special value, like 'unknown'. [Wireshark says "Time can't be converted".]</p><p>And in the other, Wireshark displays the timestamp as Wireshark displays this date as Aug 26, 25218 01:56:06.230304100 Hard to believe.</p><p>The hex for the timestamp is 4163717572696e67 ... probably not Unix epoch seconds (Oct 29, 2130) ... probably not in Unix epoch nanoseconds (Mar 17 1983) ...</p><p>Anyway, I want to read what Microsoft says this field should contain.</p><p>?</p><p>--sk</p></div><div id="question-tags" class="tags-container tags">documentation smb_fs_info_0x</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Aug '14, 08:07</strong></p><img src="https://secure.gravatar.com/avatar/18ae5b8bfddad49931ec557b9342075a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skendric&#39;s gravatar image" /><p>skendric<br />
<span class="score" title="11 reputation points">11</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skendric has no accepted answers">0%</span></p></div></div><div id="comments-container-35676" class="comments-container"><span id="35679"></span><div id="comment-35679" class="comment"><div id="post-35679-score" class="comment-score"></div><div class="comment-text"><p>OK, I figured this out. MS-SMB2 calls this 'SMB2 Query Info', whereas Wireshark calls it 'SMB_FS_INFO' ... I'm happily reading the relevant protocol spec now ... :)</p><p>--sk</p></div><div id="comment-35679-info" class="comment-info"><span class="comment-age">(22 Aug '14, 11:07)</span> skendric</div></div></div><div id="comment-tools-35676" class="comment-tools"></div><div class="clear"></div><div id="comment-35676-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

