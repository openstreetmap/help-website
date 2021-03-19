+++
type = "question"
title = "Server 2003 file listing problem Part 2"
description = '''Hi, I have the following wireshark log and was hoping for some assistance figuring out what is happening: 44120 2013-02-21 10:27:34.667718000 408.146329000 53.248.98.60 53.248.98.58 SMB 326 Trans2 Response, FIND_FIRST2, Files: . .. 44125 2013-02-21 10:27:34.776725000 408.255336000 53.248.98.58 53.24...'''
date = "2013-02-22T15:09:00Z"
lastmod = "2013-02-22T15:09:00Z"
weight = 18825
keywords = [ "2003", "smb", "server" ]
aliases = [ "/questions/18825" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Server 2003 file listing problem Part 2](/questions/18825/server-2003-file-listing-problem-part-2)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18825-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have the following wireshark log and was hoping for some assistance figuring out what is happening:</p><p>44120 2013-02-21 10:27:34.667718000 408.146329000 53.248.98.60 53.248.98.58 SMB 326 Trans2 Response, FIND_FIRST2, Files: . ..</p><p>44125 2013-02-21 10:27:34.776725000 408.255336000 53.248.98.58 53.248.98.60 SMB 97 Logoff AndX Request</p><p>44126 2013-02-21 10:27:34.776874000 408.255485000 53.248.98.60 53.248.98.58 SMB 97 Logoff AndX Response</p><p>44127 2013-02-21 10:27:34.776896000 408.255507000 53.248.98.58 53.248.98.60 SMB 93 Tree Disconnect Request</p><p>44128 2013-02-21 10:27:34.776976000 408.255587000 53.248.98.60 53.248.98.58 SMB 93 Tree Disconnect Response</p><p>44133 2013-02-21 10:27:34.948610000 408.427221000 53.248.98.58 53.248.98.60 TCP 54 appworxsrv &gt; microsoft-ds [ACK] Seq=18552 Ack=39734 Win=65077 Len=0</p><p>44693 2013-02-21 10:28:08.416593000 441.895204000 53.248.98.58 53.248.98.60 TCP 54 appworxsrv &gt; microsoft-ds [FIN, ACK] Seq=18552 Ack=39734 Win=65077 Len=0</p><p>44694 2013-02-21 10:28:08.416658000 441.895269000 53.248.98.60 53.248.98.58 TCP 60 microsoft-ds &gt; appworxsrv [FIN, ACK] Seq=39734 Ack=18553 Win=65283 Len=0</p><p>44695 2013-02-21 10:28:08.416670000 441.895281000 53.248.98.58 53.248.98.60 TCP 54 appworxsrv &gt; microsoft-ds [ACK] Seq=18553 Ack=39735 Win=65077 Len=0</p><p>Our server is going through an intermittent 30 second delay that is characterized between lines 44133 and 44693 and I've included some SMB traffic in hopes that someone can tell me what is happening on our server.</p><p>This is impacting our Production server and causing us lots of headache.</p><p>Any ideas?</p><p>Kevin</p></div><div id="question-tags" class="tags-container tags">2003 smb server</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Feb '13, 15:09</strong></p><img src="https://secure.gravatar.com/avatar/0e65e537256654384be2035887749f42?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KPMoore&#39;s gravatar image" /><p>KPMoore<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KPMoore has no accepted answers">0%</span></p></div></div><div id="comments-container-18825" class="comments-container"></div><div id="comment-tools-18825" class="comment-tools"></div><div class="clear"></div><div id="comment-18825-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

