+++
type = "question"
title = "File transfer between Windows Machines"
description = '''Hi All, I&#x27;m looking into issues with transferring files across a WAN (VPN) and see some strange packets in the pcap.  Server - 10.49.3.61 Client - 172.25.225.10 Copying files from the server to the client just via windows copy/unc. I ran the capture on a transparent ASA at the Server end which is in...'''
date = "2015-11-27T05:07:00Z"
lastmod = "2015-11-29T09:08:00Z"
weight = 48021
keywords = [ "wireshark", "pcap", "file", "slowness", "copying" ]
aliases = [ "/questions/48021" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [File transfer between Windows Machines](/questions/48021/file-transfer-between-windows-machines)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48021-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48021-score" class="post-score" title="current number of votes">0</div><span id="post-48021-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I'm looking into issues with transferring files across a WAN (VPN) and see some strange packets in the pcap.</p><p>Server - 10.49.3.61 Client - 172.25.225.10</p><p>Copying files from the server to the client just via windows copy/unc. I ran the capture on a transparent ASA at the Server end which is inline to the traffic flow. Issues I have are that the transfer just stalls, seems to try again and the eventually just stops with a general windows error, cannot copy blah blah. It seems to occur if I copy anything more than a few 100MB. I see references to mturoute and iperf in my captures which I have no idea where they are coming from. Neither are running on the server / client. Is there any indication as to why the capture is failing and also to why mturoute and iperf are showing within the SMB messages? The buffer on the ASA wasn't big enough so had to run circular buffer and managed to capture the moment the copy failed. This is across a DMVPN also. Capture attached <a href="https://www.dropbox.com/s/papy5awytjxfu9l/transfer.pcap?dl=0">https://www.dropbox.com/s/papy5awytjxfu9l/transfer.pcap?dl=0</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-file" rel="tag" title="see questions tagged &#39;file&#39;">file</span> <span class="post-tag tag-link-slowness" rel="tag" title="see questions tagged &#39;slowness&#39;">slowness</span> <span class="post-tag tag-link-copying" rel="tag" title="see questions tagged &#39;copying&#39;">copying</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Nov '15, 05:07</strong></p><img src="https://secure.gravatar.com/avatar/a28bceae0effe0ec1130bab7cb87a4e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="exit12&#39;s gravatar image" /><p><span>exit12</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="exit12 has no accepted answers">0%</span></p></div></div><div id="comments-container-48021" class="comments-container"></div><div id="comment-tools-48021" class="comment-tools"></div><div class="clear"></div><div id="comment-48021-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48058"></span>

<div id="answer-container-48058" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48058-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48058-score" class="post-score" title="current number of votes">0</div><span id="post-48058-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looking at the trace I'd say your description of the environment is incorrect. The windows client is at 10.49.3.61 and the trace was taken close(r) to the client. The server is at 172.25.225.10 and behind a WAN VPN connection through a riverbed. The initial RTT towards the server is 166 ms The direction of the traffic is from client to server -&gt; 445 The riverbed is offering a window_scale factor of 4 The stalled session is due to a zero window offering of the riverbed device, obviously it is not getting the data forwarded fast enough over the WAN (maybe packet loss?)</p><p>The occurances of "mturoute" and "iperf" are simply filen-ames in the directory of the of the server.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Selection_194.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Nov '15, 09:08</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div></div><div id="comments-container-48058" class="comments-container"></div><div id="comment-tools-48058" class="comment-tools"></div><div class="clear"></div><div id="comment-48058-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

