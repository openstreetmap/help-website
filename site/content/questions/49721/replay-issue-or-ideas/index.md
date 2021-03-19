+++
type = "question"
title = "Replay Issue or ideas?"
description = '''I&#x27;m having an issue with replaying Wireshark packets. I&#x27;ve captured data being received on a remote network on a port - say port 12345. I&#x27;m trying to change the destination IP in the capture (Idid so using bittwist) but when I replay the packets, the machine I&#x27;m trying to send the packets to on my l...'''
date = "2016-02-02T06:50:00Z"
lastmod = "2016-02-02T06:50:00Z"
weight = 49721
keywords = [ "replay" ]
aliases = [ "/questions/49721" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Replay Issue or ideas?](/questions/49721/replay-issue-or-ideas)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49721-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm having an issue with replaying Wireshark packets. I've captured data being received on a remote network on a port - say port 12345. I'm trying to change the destination IP in the capture (Idid so using bittwist) but when I replay the packets, the machine I'm trying to send the packets to on my local network is not receiving them, and it's listening on the same port (12345). When I run a capture on third machine on my network (not sending or receiving) I do see the packets being broadcast. Does anyone have any ideas?</p></div><div id="question-tags" class="tags-container tags">replay</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Feb '16, 06:50</strong></p><img src="https://secure.gravatar.com/avatar/2c9c9b037158907063e4e3decb635492?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ultron&#39;s gravatar image" /><p>Ultron<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ultron has no accepted answers">0%</span></p></div></div><div id="comments-container-49721" class="comments-container"><span id="49738"></span><div id="comment-49738" class="comment"><div id="post-49738-score" class="comment-score"></div><div class="comment-text"><p>Have you changed the mac address, too?</p></div><div id="comment-49738-info" class="comment-info"><span class="comment-age">(02 Feb '16, 12:19)</span> Christian_R</div></div><span id="49748"></span><div id="comment-49748" class="comment"><div id="post-49748-score" class="comment-score"></div><div class="comment-text"><p>Yes - source and destination MAC addresses have been changed. I also tried to modify the data to remove the replies from the host so I would only send the packets to the server that should be receiving/processing the data (with none of the original replies). The listener I have running never receives the replayed data.</p></div><div id="comment-49748-info" class="comment-info"><span class="comment-age">(02 Feb '16, 15:21)</span> Ultron</div></div><span id="49757"></span><div id="comment-49757" class="comment"><div id="post-49757-score" class="comment-score"></div><div class="comment-text"><p>How do you know your receiving station is properly setup? Have you tested that, with netcap for instance? What type of traffic is this anyway? UDP/IP?</p></div><div id="comment-49757-info" class="comment-info"><span class="comment-age">(02 Feb '16, 22:47)</span> Jaap ♦</div></div></div><div id="comment-tools-49721" class="comment-tools"></div><div class="clear"></div><div id="comment-49721-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

