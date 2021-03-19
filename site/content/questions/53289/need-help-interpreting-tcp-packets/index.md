+++
type = "question"
title = "Need help interpreting TCP packets"
description = '''I need help analyzing the logs that are presented by Wireshark. I need someone that knows how to interpret the packet traces involving some handheld scanners in a warehouse. Something has happened to the network traffic in the last 2 weeks making the scanner connections unstable. Before that the net...'''
date = "2016-06-07T12:00:00Z"
lastmod = "2016-06-07T12:00:00Z"
weight = 53289
keywords = [ "packets" ]
aliases = [ "/questions/53289" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Need help interpreting TCP packets](/questions/53289/need-help-interpreting-tcp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53289-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need help analyzing the logs that are presented by Wireshark. I need someone that knows how to interpret the packet traces involving some handheld scanners in a warehouse. Something has happened to the network traffic in the last 2 weeks making the scanner connections unstable. Before that the network was performing well. We ran a trace using Wireshark but need an expert to help us in interpretation and diagnosis. We see a lot of retransmitted TCP packets (both normal and “spurious”) and a lot of reset packets in the log. Now every 15 minutes or so we get a lost connection error on the wireless devices which forces the user to reconnect. Is there a way to isolate the problem to a specific device or network node?</p></div><div id="question-tags" class="tags-container tags">packets</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jun '16, 12:00</strong></p><img src="https://secure.gravatar.com/avatar/0a99c27fa61c49299a67e3ad7d176f5d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jdm77&#39;s gravatar image" /><p>jdm77<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jdm77 has no accepted answers">0%</span></p></div></div><div id="comments-container-53289" class="comments-container"><span id="53300"></span><div id="comment-53300" class="comment"><div id="post-53300-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Is there a way to isolate the problem to a specific device or network node?</p></blockquote><p>Yes, there is, but you gave no details about your network topology, and a single Wireshark trace (taken at a single capturing point) is not enough.</p><p>In wired networks, you have to take two captures simultaneously, one at the server end and another one on the scanner end, and see the difference - packets sent at one side but never reaching the other one. After doing that, you would move the capturing point one network segment closer to the source of packets which get lost and do the two captures again. After several such steps, you should be able to identify a network element which causes the loss. But it may well be a passive one (a broken cable or connector).</p><p>In wireless networks, the process may be much more complex, as the packet loss may be caused by radio interference from other wireless networks or even completely other equipment. But unless you have a single AP to which all scanners and also the server are connected wirelessly, there should still be plenty of space for isolating the issue to a limited set of network elements.</p><p>A sketch of the network topology should be your starting point, so that you would be able to identify the part of the path between the scanners and the server which is common for all scanners which exhibit the issue.</p><p>Publishing the sketch would raise your chances for getting a more targeted advice here.</p></div><div id="comment-53300-info" class="comment-info"><span class="comment-age">(07 Jun '16, 22:11)</span> sindy</div></div></div><div id="comment-tools-53289" class="comment-tools"></div><div class="clear"></div><div id="comment-53289-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

