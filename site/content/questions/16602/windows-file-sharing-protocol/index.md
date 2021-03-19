+++
type = "question"
title = "Windows file sharing protocol"
description = '''I understand the capture of a ftp as it uses tcp handshake to setup the communication. But for Windows file sharing, like copy a file from the server to the PC via the WAN. I am not sure what is a normal traffic pattern for Windows copy.   Is there a Wireshark trace file of a normal behavior of a Wi...'''
date = "2012-12-05T10:36:00Z"
lastmod = "2012-12-05T15:04:00Z"
weight = 16602
keywords = [ "windows", "sharing", "protocol", "file" ]
aliases = [ "/questions/16602" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Windows file sharing protocol](/questions/16602/windows-file-sharing-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16602-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I understand the capture of a ftp as it uses tcp handshake to setup the communication. But for Windows file sharing, like copy a file from the server to the PC via the WAN. I am not sure what is a normal traffic pattern for Windows copy.</p><ul><li>Is there a Wireshark trace file of a normal behavior of a Windows copy file?</li><li>What protocol does Windows copy uses? What CIFS, SMB, and NBSS?</li></ul><p>Thanks</p></div><div id="question-tags" class="tags-container tags">windows sharing protocol file</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '12, 10:36</strong></p><img src="https://secure.gravatar.com/avatar/4bf9a4681570406f873b404a912f2a7b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="character9&#39;s gravatar image" /><p>character9<br />
<span class="score" title="16 reputation points">16</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="character9 has no accepted answers">0%</span></p></div></div><div id="comments-container-16602" class="comments-container"></div><div id="comment-tools-16602" class="comment-tools"></div><div class="clear"></div><div id="comment-16602-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="16608"></span>

<div id="answer-container-16608" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16608-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>What protocol does Windows copy uses? What CIFS, SMB, and NBSS?</p></blockquote><p>Could be CIFS/SMB, NFS (if configured) or even WebDAV (if configured). It all depends on the configuration of the systems and how you access the remote file system.</p><p>Please read the following to understand how CIFS is related to SMB (and vice versa).</p><blockquote><p><code>http://msdn.microsoft.com/en-us/library/cc246232%28v=prot.20%29.aspx</code><br />
<code>http://msdn.microsoft.com/en-us/library/ee441901%28v=prot.20%29.aspx</code><br />
</p></blockquote><p>A bit technical, but ... ;-)</p><blockquote><p>Is there a Wireshark trace file of a normal behavior of a Windows copy file?</p></blockquote><p>Please check out the Wireshark Sample captures. Search for SMB or CIFS.</p><blockquote><p><code>http://wiki.wireshark.org/SampleCaptures</code><br />
</p></blockquote><p>Maybe you'll find something here:</p><blockquote><p><code>https://www.openpacket.org/capture/by_tag?tag=smb</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '12, 11:45</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-16608" class="comments-container"><span id="16655"></span><div id="comment-16655" class="comment"><div id="post-16655-score" class="comment-score"></div><div class="comment-text"><p>I will take a look at that in more details. But I am having a very slow response while copying files from the server to the PC over the MPLS Wan. It is taking 2 days for a 300mb file to copy from the server to the PC. I looked at the captured files and it using SMB. But from what I noticed, I have many duplicate ACK and a lot of NBSS before the actual transfer of the file. Any help will be appreciated. Thx</p></div><div id="comment-16655-info" class="comment-info"><span class="comment-age">(06 Dec '12, 12:31)</span> character9</div></div><span id="16656"></span><div id="comment-16656" class="comment"><div id="post-16656-score" class="comment-score"></div><div class="comment-text"><p>If "a lot of NBSS" means "a lot of frames marked as NBSS rather than as SMB", those are probably either retransmissions or the result of frames either being lost or not getting captured - the latter would just be a problem with the machine running the capture program not handling incoming packets well enough, but the former could be the result of a networking issue.</p></div><div id="comment-16656-info" class="comment-info"><span class="comment-age">(06 Dec '12, 12:37)</span> Guy Harris ♦♦</div></div><span id="16662"></span><div id="comment-16662" class="comment"><div id="post-16662-score" class="comment-score"></div><div class="comment-text"><p>O.K. if it's SMB, please run the Response time stats and post the screenshot here.</p><blockquote><p><code>Statistics -&gt; Service Response Time -&gt; SMB</code><br />
</p></blockquote><p>regarding the slow response time. Can you please give some more details.</p><ul><li>do you have the same problem with other protocols (HTTP, FTP download)</li><li>is there a VPN involved (IPSEC)?</li><li>is there any QoS or WAN accelerator device involved?</li><li>what is the RTT over the MPLS (ping)?</li></ul></div><div id="comment-16662-info" class="comment-info"><span class="comment-age">(06 Dec '12, 14:44)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-16608" class="comment-tools"></div><div class="clear"></div><div id="comment-16608-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16614"></span>

<div id="answer-container-16614" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16614-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>What protocol does Windows copy uses? What CIFS, SMB, and NBSS?</p></blockquote><p>For "Windows file sharing", it's probably CIFS/SMB; they're really the same thing, just different names. It was originally called SMB (Server Message Block); there was an attempt to standardize it as the Common Internet File System, as a file system for use over the Internet (at about the same time that Sun was promoting WebNFS as "NFS for the Internet"), but it's really all the same thing.</p><p>NBSS is the NetBIOS Session Service, as defined in <a href="http://tools.ietf.org/html/rfc1001">RFC 1001</a> and <a href="http://tools.ietf.org/html/rfc1002">RFC 1002</a>. SMB ran atop the NetBIOS services and thus atop the protocols that provide them, including but not limited to the NetBIOS-over-TCP NBSS protocol. Later, the encapsulation of SMB packets over a TCP stream used by NBSS was simplified (by removing all the connection-setup mechanism) and used for a direct encapsulation of SMB over TCP; NBSS ran over TCP port 139, and SMB-over-TCP ran over TCP port 445.</p><p>So you're probably either seeing SMB/CIFS-over-NBSS (and thus over TCP) or SMB/CIFS-over-TCP - in current versions of Windows, it's probably SMB/CIFS-over-TCP.</p><p>There's a newer "SMB2" protocol, which I think first appeared in Windows Vista and the server equivalent, which would be used between clients and servers that both support SMB2. Wireshark dissects both SMB and SMB2, and both SMB/CIFS-over-TCP and SMB/CIFS-over-NBSS.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '12, 15:04</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></br></p></div></div><div id="comments-container-16614" class="comments-container"></div><div id="comment-tools-16614" class="comment-tools"></div><div class="clear"></div><div id="comment-16614-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

