+++
type = "question"
title = "UDP packets not received my application but received in WS"
description = '''Dear All, I am facing a problem in transferring data UDP data to a python application. I have an embedded system transmitting UDP packets to the PC. I can clearly recognize the packets with WS but my application cannot receive them. In WS I can check the headers and they are correct in each field. T...'''
date = "2016-06-09T06:12:00Z"
lastmod = "2016-06-09T06:12:00Z"
weight = 53331
keywords = [ "udp" ]
aliases = [ "/questions/53331" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [UDP packets not received my application but received in WS](/questions/53331/udp-packets-not-received-my-application-but-received-in-ws)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53331-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear All, I am facing a problem in transferring data UDP data to a python application. I have an embedded system transmitting UDP packets to the PC. I can clearly recognize the packets with WS but my application cannot receive them. In WS I can check the headers and they are correct in each field. There is only one point that puzzles me. It seems that on the wire there are always 4 bytes more than the expected. Anyway WS doesn't complain about that. Does anyone have some opinions to share on this? Thanks a lot in Advance. MMM<br />
</p></div><div id="question-tags" class="tags-container tags">udp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '16, 06:12</strong></p><img src="https://secure.gravatar.com/avatar/3e3017ce150afcd8a315c019d3d3d1f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MMM&#39;s gravatar image" /><p>MMM<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MMM has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-53331" class="comments-container"><span id="53332"></span><div id="comment-53332" class="comment"><div id="post-53332-score" class="comment-score"></div><div class="comment-text"><p>You'll have to publish the capture on Cloudshark or some file sharing service (Dropbox, Google Drive), login-free, and edit your question with a link to it if you want some advice, and explain whether the extra 4 bytes are in the end of the packet or somewhere else.</p><p>And if the receiving application has an issue, a capture won't disclose that. In case of UDP with proprietary payload, you can use Wireshark only to analyse the contents of the packets.</p></div><div id="comment-53332-info" class="comment-info"><span class="comment-age">(09 Jun '16, 06:17)</span> sindy</div></div></div><div id="comment-tools-53331" class="comment-tools"></div><div class="clear"></div><div id="comment-53331-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

