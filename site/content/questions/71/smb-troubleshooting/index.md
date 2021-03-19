+++
type = "question"
title = "SMB troubleshooting"
description = '''Can someone help me with troubleshooting SMB/CIFS traffic. I have a user that experiences &quot;lost connections&quot; opening MS Access databases and slowness/errors opening MS Excel documents, both from a remote file share on a NetApp storage appliance. From a network perspective, the traces look good but w...'''
date = "2010-09-14T13:17:00Z"
lastmod = "2010-09-21T06:18:00Z"
weight = 71
keywords = [ "wireshark", "smb", "trace", "cifs" ]
aliases = [ "/questions/71" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [SMB troubleshooting](/questions/71/smb-troubleshooting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-71-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can someone help me with troubleshooting SMB/CIFS traffic. I have a user that experiences "lost connections" opening MS Access databases and slowness/errors opening MS Excel documents, both from a remote file share on a NetApp storage appliance. From a network perspective, the traces look good but we are seeing a number of messages in WireShark like the one below.<br />
</p><table style="width:100%;"><colgroup><col style="width: 16%" /><col style="width: 16%" /><col style="width: 16%" /><col style="width: 16%" /><col style="width: 16%" /><col style="width: 16%" /></colgroup><tbody><tr class="odd"><td><h4 id="no.">No.</h4></td><td><h4 id="time">Time</h4></td><td><h4 id="source">Source</h4></td><td><h4 id="destination">Destination</h4></td><td><h4 id="protocol">Protocol</h4></td><td><h4 id="info">Info</h4></td></tr><tr class="even"><td>73672</td><td>2010-09-10 06:28:57.228319947</td><td>10.225.10.148</td><td>10.170.100.60</td><td>SMB</td><td>NT Create AndX Response, FID: 0x0000, Error: STATUS_ACCESS_DENIED</td></tr></tbody></table><br />
<p>It has been a long time since I have been in the server world so, I am not sure where to start looking. As I said, there do not appear to be any latency or other issues with the network and based on research, it appears that there are some issues with SMB signing in the MicroSoft world. I am just trying to find a place to really start troubleshooting. If more information is needed let me know. Any help would be appreciated.</p><p>Brad Walker</p></div><div id="question-tags" class="tags-container tags">wireshark smb trace cifs</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '10, 13:17</strong></p><img src="https://secure.gravatar.com/avatar/dfa864459179bdadc35de414b97cb75d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mbwalker&#39;s gravatar image" /><p>mbwalker<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mbwalker has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-71" class="comments-container"><span id="130"></span><div id="comment-130" class="comment"><div id="post-130-score" class="comment-score">1</div><div class="comment-text"><p>STATUS_ACCESS_DENIED sounds as if a program on the client tried to open or create a file to which the account being used for the SMB connection did not have access - i.e., it's not a networking problem or an SMB packet-signing problem, it's a file permissions problem.</p><p>Whether that's the cause of the lost connections or slowness is another matter; it might not be trying to open an Access database or an Excel document. What was the matching NTCreateAndX request? That should indicate what it was trying to open/create.</p></div><div id="comment-130-info" class="comment-info"><span class="comment-age">(15 Sep '10, 17:15)</span> Guy Harris ♦♦</div></div><span id="186"></span><div id="comment-186" class="comment"><div id="post-186-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Guy! That is what my thoughts were but I was just looking for ways to prove it. I will scan the trace again and see what I can find out.</p></div><div id="comment-186-info" class="comment-info"><span class="comment-age">(17 Sep '10, 09:25)</span> mbwalker</div></div></div><div id="comment-tools-71" class="comment-tools"></div><div class="clear"></div><div id="comment-71-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="148"></span>

<div id="answer-container-148" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-148-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hello Brad,</p><p>I have the same problem working with an MS Access file on a Netapp filer.... if I put the same file on a Windows fileserver all works fine! the nas is joined to the domain and the resource isn't poor (cpu etc. etc.) Do you have resolved the problem? Bye</p><p>Federico</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '10, 06:51</strong></p><img src="https://secure.gravatar.com/avatar/30ab5c83d377d733296c9652686e8e62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Federico&#39;s gravatar image" /><p>Federico<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Federico has no accepted answers">0%</span></p></div></div><div id="comments-container-148" class="comments-container"><span id="191"></span><div id="comment-191" class="comment"><div id="post-191-score" class="comment-score"></div><div class="comment-text"><p>This is a Q&amp;A site, which operates a little differently from traditional web forums. If you're not answering @mbwalker's question can you click on the "add new comment" button?</p></div><div id="comment-191-info" class="comment-info"><span class="comment-age">(17 Sep '10, 11:04)</span> Gerald Combs ♦♦</div></div></div><div id="comment-tools-148" class="comment-tools"></div><div class="clear"></div><div id="comment-148-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="243"></span>

<div id="answer-container-243" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-243-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This message is likely buried in the middle of lots of SMB layer messages, right? Is the user going through Windows Explorer to find the file on the server? If you look at the full decode you should see what they're being denied access to. This is common, especially when the user is browsing the server through WE to find the file - there may be lots of directories/files the user doesn't have access to. AND WE likes to load pretty little icons for the files, which usually requires atleast read access. This/These errors may or may not have anything to do with the disconnections. If the user pings the server what is the response time? Does the connection break during the middle of the transfer? Is he working via VPN? There are lots of factors that can break SMB connections - good luck!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Sep '10, 06:18</strong></p><img src="https://secure.gravatar.com/avatar/9e493496d59bb4ce33c37cd6e7a26a4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeonJay&#39;s gravatar image" /><p>GeonJay<br />
<span class="score" title="470 reputation points">470</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeonJay has 2 accepted answers">5%</span></p></div></div><div id="comments-container-243" class="comments-container"></div><div id="comment-tools-243" class="comment-tools"></div><div class="clear"></div><div id="comment-243-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

