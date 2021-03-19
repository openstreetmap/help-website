+++
type = "question"
title = "How is the &quot;guid handle file&quot; set in SMB2 dissector with multiple netbios parts?"
description = '''Hello, I stumbled upon a strange packet in a SMB2 conversion. The packets contains 3 Netbios parts, each containing 1 SMB2 part. Looks to me like something Rolf Leutert described in the SMB troubleshooting session at the Sharkfest 2013. The packet is a response to 3 separate commands. When looking a...'''
date = "2014-01-05T08:05:00Z"
lastmod = "2014-01-05T08:05:00Z"
weight = 28586
keywords = [ "guid", "smb2", "file" ]
aliases = [ "/questions/28586" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How is the "guid handle file" set in SMB2 dissector with multiple netbios parts?](/questions/28586/how-is-the-guid-handle-file-set-in-smb2-dissector-with-multiple-netbios-parts)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28586-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I stumbled upon a strange packet in a SMB2 conversion. The packets contains 3 Netbios parts, each containing 1 SMB2 part. Looks to me like something Rolf Leutert described in the SMB troubleshooting session at the Sharkfest 2013. The packet is a response to 3 separate commands. When looking at "smb2.seq_num", "smb2.cmd" and "smb2.nt_status" it looks good, Wireshark shows a comma separated list of values: "smb2.seq_num" = "81048,810,49,81050" "smb2.cmd" = "Close,Create,GetInfo" "smb2.nt_status" = "Status_Success,Status_Success,Status_Success"</p><p>However, looking at "smb2.fid" there is only 1 value, "smb2.fid" = "218dbaea-0000-0000-744b-000000000000" This refers to the second SMB2 part, response to the Create Request. Although this is technically correct I wonder if something like "smb2.fid" = ",218dbaea-0000-0000-744b-000000000000," would make it easier to see to which command sequence number the File ID belongs. Or am I missing something?</p></div><div id="question-tags" class="tags-container tags">guid smb2 file</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jan '14, 08:05</strong></p><img src="https://secure.gravatar.com/avatar/8745a7230463c8273ffe2d4ebb47fa72?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dife2013&#39;s gravatar image" /><p>dife2013<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dife2013 has no accepted answers">0%</span></p></div></div><div id="comments-container-28586" class="comments-container"></div><div id="comment-tools-28586" class="comment-tools"></div><div class="clear"></div><div id="comment-28586-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

