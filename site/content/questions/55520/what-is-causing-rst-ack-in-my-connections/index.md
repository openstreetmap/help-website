+++
type = "question"
title = "What is causing RST ACK in my connections?"
description = '''75% of calls to a 3rd party API are getting dropped.  Here is a wireshark capture of RST ACK happening with 2 calls: Failing Capture. Here is a wireshark capture of a successful connection for comparison: Success Capture. I cant figure out what is causing the RST ACK flag. Couple things I&#x27;ve noticed...'''
date = "2016-09-13T06:47:00Z"
lastmod = "2016-09-13T06:47:00Z"
weight = 55520
keywords = [ "rst+ack" ]
aliases = [ "/questions/55520" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What is causing RST ACK in my connections?](/questions/55520/what-is-causing-rst-ack-in-my-connections)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55520-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>75% of calls to a 3rd party API are getting dropped.</p><p>Here is a wireshark capture of RST ACK happening with 2 calls: <a href="https://www.cloudshark.org/captures/a05d6b08cfe4">Failing Capture</a>.</p><p>Here is a wireshark capture of a successful connection for comparison: <a href="https://www.cloudshark.org/captures/93f0d40fe878">Success Capture</a>.</p><p>I cant figure out what is causing the RST ACK flag. Couple things I've noticed. TCP DUP ACK is common between both success and failure. It seems to recover from it sometimes. The Server doesn't seem to support SACK_PERM=1. Not sure if that is relevant or not.</p><p>Any ideas on why a TCP RST ACK is happening?</p></div><div id="question-tags" class="tags-container tags">rst+ack</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '16, 06:47</strong></p><img src="https://secure.gravatar.com/avatar/645c2a3b9c2bb50630256d96426873de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cripsola&#39;s gravatar image" /><p>cripsola<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cripsola has no accepted answers">0%</span></p></div></div><div id="comments-container-55520" class="comments-container"></div><div id="comment-tools-55520" class="comment-tools"></div><div class="clear"></div><div id="comment-55520-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

