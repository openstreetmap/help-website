+++
type = "question"
title = "Wireshark does not capture network data on Windows 7 and Windows 2008"
description = '''I am using the stable build - Wireshark 1.6.2 on Windows 7 32 Bit and Windows 2008 32 Bit Operating Systems. To analyse the captured network data and the service elements I am using Merge DPM. Network data is captured on Windows 7 (i.e. Wireshark running on Windows 7)and saved in .cap format NA Snif...'''
date = "2012-12-09T20:01:00Z"
lastmod = "2012-12-09T20:01:00Z"
weight = 16739
keywords = [ "windows", "1.6.2", "7", "wireshark" ]
aliases = [ "/questions/16739" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark does not capture network data on Windows 7 and Windows 2008](/questions/16739/wireshark-does-not-capture-network-data-on-windows-7-and-windows-2008)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16739-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using the stable build - Wireshark 1.6.2 on Windows 7 32 Bit and Windows 2008 32 Bit Operating Systems. To analyse the captured network data and the service elements I am using Merge DPM. Network data is captured on Windows 7 (i.e. Wireshark running on Windows 7)and saved in .cap format NA Sniffer 2.00x so that Merge DPM can read the file. But when the file captured on Windows 7 is opened in MergeDPM it does not show any service elements.</p><p>Where as for captures taken on other OS like Windows Vista 32/64, Windows 2003 Server 32/64 etc... do show the service elements in MergeDPM.</p><p>What is the possible problem? Any suggestions?</p><p>Can anybody help giving the answer as soon as possible?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">windows 1.6.2 7 wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Dec '12, 20:01</strong></p><img src="https://secure.gravatar.com/avatar/c7e7df90e3cf2ce7787ea705ebbf12e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yogini&#39;s gravatar image" /><p>yogini<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yogini has no accepted answers">0%</span></p></div></div><div id="comments-container-16739" class="comments-container"><span id="16921"></span><div id="comment-16921" class="comment"><div id="post-16921-score" class="comment-score"></div><div class="comment-text"><blockquote><p>But when the file captured on Windows 7 is opened in MergeDPM it does not show any service elements.</p></blockquote><p>did you limit the capture size?</p></div><div id="comment-16921-info" class="comment-info"><span class="comment-age">(14 Dec '12, 13:58)</span> Kurt Knochner ♦</div></div><span id="16922"></span><div id="comment-16922" class="comment"><div id="post-16922-score" class="comment-score"></div><div class="comment-text"><p>What happens if you use <a href="http://www.microsoft.com/en-us/download/details.aspx?id=4865">Microsoft Network Monitor</a> to capture the traffic on the Windows 7/Windows Server 2008 machines, open it in Wireshark, try to save it in Sniffer format, and, if that succeeds, read it in MergeDPM?</p><p>Is Wireshark capturing <em>other</em> packets on those machines, or is it not capturing <em>any</em> packets?</p></div><div id="comment-16922-info" class="comment-info"><span class="comment-age">(14 Dec '12, 20:24)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-16739" class="comment-tools"></div><div class="clear"></div><div id="comment-16739-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

