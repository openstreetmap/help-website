+++
type = "question"
title = "Connection to license server [RST]"
description = ''' Thanks for getting to me...unfortunately I can&#x27;t upload the whole pcap. I have attached the trace in chronological order for your viewing. Let me know if this helps. The pc checks into the license server on port 1025 every 10 mins. So far we only have had this happen at 3 locations(we have 25 locat...'''
date = "2017-04-12T14:38:00Z"
lastmod = "2017-04-12T14:38:00Z"
weight = 60788
keywords = [ "rst" ]
aliases = [ "/questions/60788" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Connection to license server \[RST\]](/questions/60788/connection-to-license-server-rst)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60788-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture2_1K5suva.PNG" alt="alt text" /> <strong>Thanks for getting to me...unfortunately I can't upload the whole pcap. I have attached the trace in chronological order for your viewing. Let me know if this helps. The pc checks into the license server on port 1025 every 10 mins. So far we only have had this happen at 3 locations(we have 25 locations,MPLS).Yes there is NAT being performed but this only started to happen recently to users</strong></p><p>Client PC connects to a license server and checks in every 10 mins.</p><p>Randomly the connection is "reset" where the user has to re-launch application again. Wireshark pcap show the connection using port 992 for SSL and port 1025 to check into license server. The last entry on the pcap show a [RST] just as connection to server is lost.</p><p>Attached is pic of pcap if anybody has any ideas....thanks in advance.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture1_RDp0R87.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">rst</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Apr '17, 14:38</strong></p><img src="https://secure.gravatar.com/avatar/0323ddb09c8612d629adba6fa14b4d13?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jrafter&#39;s gravatar image" /><p>jrafter<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jrafter has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 13 Apr '17, 12:45</p></div></div><div id="comments-container-60788" class="comments-container"><span id="60802"></span><div id="comment-60802" class="comment"><div id="post-60802-score" class="comment-score">1</div><div class="comment-text"><p>Somehow your picture does not fit to your problem description. The server port in the screen shot is 49411 not 992 ! Also you only show uni-directional traffic and the packets listed are not in chronological order - making it even more difficult to understand what is going on. . It'll be hard to give you any advice based on the information you provide. Can you share the original pcap file filtered on the session ?</p><p>regards Matthias</p></div><div id="comment-60802-info" class="comment-info"><span class="comment-age">(13 Apr '17, 05:32)</span> mrEEde</div></div><span id="60814"></span><div id="comment-60814" class="comment"><div id="post-60814-score" class="comment-score">1</div><div class="comment-text"><p>Are the license connections mostly idle? If so, are there any middleboxes (NAT, proxy, etc) between the client and the license server that would reject a timed-out session?</p></div><div id="comment-60814-info" class="comment-info"><span class="comment-age">(13 Apr '17, 12:23)</span> Gerald Combs ♦♦</div></div></div><div id="comment-tools-60788" class="comment-tools"></div><div class="clear"></div><div id="comment-60788-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

