+++
type = "question"
title = "Trying to analyse high network utilization"
description = '''I´m trying to locate an issue with a certain application exe file my company uses. When this exe file is on a network share, every time a user views it, right click &amp;amp; properties, network utilization spikes (60-80%)for 5-20 seconds, depending on the link between client and file server. The exe fi...'''
date = "2016-12-15T15:23:00Z"
lastmod = "2016-12-18T11:10:00Z"
weight = 58150
keywords = [ "exe", "smb", "file", "in" ]
aliases = [ "/questions/58150" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Trying to analyse high network utilization](/questions/58150/trying-to-analyse-high-network-utilization)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58150-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I´m trying to locate an issue with a certain application exe file my company uses. When this exe file is on a network share, every time a user views it, right click &amp; properties, network utilization spikes (60-80%)for 5-20 seconds, depending on the link between client and file server. The exe file is about 118MB, signed with SHA256 digital signature.</p><p>Only thing I see in Process Explorer is that system process (pid 4) is responsible but why?</p><p>Looking at the wireshark capture is filled with "TCP segment of a reassembled PDU" and "TCP Dup ACP..."</p><p>I´m novice to wireshark but fast learner so any help you give me is greatly appreciated.</p></div><div id="question-tags" class="tags-container tags">exe smb file in</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '16, 15:23</strong></p><img src="https://secure.gravatar.com/avatar/7ba425f47a8d321ba7104b45b2f1041e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kristjang&#39;s gravatar image" /><p>kristjang<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kristjang has no accepted answers">0%</span></p></div></div><div id="comments-container-58150" class="comments-container"><span id="58180"></span><div id="comment-58180" class="comment"><div id="post-58180-score" class="comment-score"></div><div class="comment-text"><blockquote><blockquote><p>Looking at the wireshark capture</p></blockquote></blockquote><p>Maybe if we looked at them too we might notice something....</p><p>Can you share a capture in a publicly accessible spot, e.g. CloudShark, Google Drive, DropBox etc.?</p></div><div id="comment-58180-info" class="comment-info"><span class="comment-age">(17 Dec '16, 05:47)</span> Bob Jones</div></div></div><div id="comment-tools-58150" class="comment-tools"></div><div class="clear"></div><div id="comment-58150-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58216"></span>

<div id="answer-container-58216" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58216-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>A number of things happen in the background, when you point the Windows file explorer to a directory that is located on the network share. Here are a few of the activities, that happen in the background:</p><ul><li>The explorer will collect a list of all files in the directory and it's attributes like time stamps.</li><li>Your computer collects or updates icons for all files in the folder.</li><li>Hopefully at least one virus scanner will check the file (or at least all executable files in that directory).</li><li>The search indexer might start browsing files to prepare for later search operations.</li></ul><p>The virus scanner's behavior depends on your specific configuration. I have seen a number of variations. Some of them are:</p><ul><li>The client scanns the remote file (ok, but with performance impact)</li><li>The server delays access for the client until it has finished it's scan (better, since the server can cache the verdict until a pattern update is available or the file has been changed)</li><li>Both systems scan the file simultaneously (not good, as this can lead to a lot of lock management)</li></ul><p><strong><em>Note A:</em></strong> The client's virus scanner should not cache it's verdict on files stored on the server as the file might be changed (infected) by another client.</p><p><strong><em>Note B:</em></strong> Starting applications from a network drive is always a bad idea: Windows treats executables as small paging file. Sections from the program can be read multiple times, if the Windows kernel needs more space for other applications.</p><p><strong><em>Note C:</em></strong> Programs can be compiled to be kept in memory, once they are loaded. The behavior is specified by a special bit in the EXE-files PE header.</p><p>The network load increases if the client uses the program frequently: Windows has a mechanism called the prefetcher or superfetch. The prefetcher will identify the most popular programs and load these into memory, even if the user did not click them (yet). If necessary all required DLLs will be loaded as well. This further increases the network load, as your virus scanner(s) hopefully scans all DLLs.</p><p>Many other things can happen in the background: If the 118 MB executable is a self extracting archive or an installer, all the files contained in this container will (hopefully) be scanned by your virus scanner.</p><p>As Bob Jones mentioned, a Wireshark trace file will reveal the nature of the traffic.</p><p>The fact that the system process (pid 4) is responsible for the I/O is quite comforting: Access to network shares is facilitated by a driver (either SMB.SYS or SMB2.SYS). Drivers are considered part of or an extension to the Windows kernel, hence their activity is charged to the system process.</p><p>Good hunting</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Dec '16, 11:10</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-58216" class="comments-container"></div><div id="comment-tools-58216" class="comment-tools"></div><div class="clear"></div><div id="comment-58216-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

