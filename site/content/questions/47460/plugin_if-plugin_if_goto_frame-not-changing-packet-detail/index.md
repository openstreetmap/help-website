+++
type = "question"
title = "plugin_if: plugin_if_goto_frame not changing packet detail"
description = '''Hi, I&#x27;ve written a small TCP service that runs on a thread inside Wireshark. I use Putty to send a frame number to the service which then uses plugin_if_goto_frame to command Wireshark to jump to the frame number sent. It works fine except for one problem. Although the correct frame is highlighted i...'''
date = "2015-11-10T00:46:00Z"
lastmod = "2015-11-10T01:37:00Z"
weight = 47460
keywords = [ "plugin_if" ]
aliases = [ "/questions/47460" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [plugin\_if: plugin\_if\_goto\_frame not changing packet detail](/questions/47460/plugin_if-plugin_if_goto_frame-not-changing-packet-detail)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47460-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I've written a small TCP service that runs on a thread inside Wireshark. I use Putty to send a frame number to the service which then uses <code>plugin_if_goto_frame</code> to command Wireshark to jump to the frame number sent. It works fine except for one problem.</p><p>Although the correct frame is highlighted in the Packet List, the Packet Detail and Packet Bytes don't change to match the new frame number. I've recorded a short video of this which you can see at <a href="https://youtu.be/jUHuC_2rTcM">https://youtu.be/jUHuC_2rTcM</a></p><p>What do I need to do to get Wireshark to update the Packet Detail and Packet Bytes?</p><p>Thanks and regards...Paul</p></div><div id="question-tags" class="tags-container tags">plugin_if</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Nov '15, 00:46</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-47460" class="comments-container"></div><div id="comment-tools-47460" class="comment-tools"></div><div class="clear"></div><div id="comment-47460-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47461"></span>

<div id="answer-container-47461" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47461-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not sure. It triggers a 'find frame' kind of action, but doesn't seem to select it, which should trigger detailed dissection. Maybe better to go over to the <a href="https://wireshark.org/mailman/listinfo/wireshark-dev">wireshark developers mailinglist</a> with these type of questions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '15, 01:37</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-47461" class="comments-container"><span id="47462"></span><div id="comment-47462" class="comment"><div id="post-47462-score" class="comment-score"></div><div class="comment-text"><p>Will do. Thanks.</p></div><div id="comment-47462-info" class="comment-info"><span class="comment-age">(10 Nov '15, 01:43)</span> PaulOfford</div></div></div><div id="comment-tools-47461" class="comment-tools"></div><div class="clear"></div><div id="comment-47461-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

