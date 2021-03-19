+++
type = "question"
title = "error  while dissecting mac-lte packets"
description = '''Hi, i am using Wireshark Version 1.4.3. I have downloaded mac_lte_logger.c. For its compilation I used packet-mac-lte.h which is present under /usr/local/src/wireshark-1.4.3/epan/dissectors/ But during compilation I got the error: packet-mac-lte.h:148: error: expected ‘)’ before ‘*’ token Since it w...'''
date = "2012-11-07T02:20:00Z"
lastmod = "2012-11-07T02:20:00Z"
weight = 15616
keywords = [ "mac-lte" ]
aliases = [ "/questions/15616" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [error while dissecting mac-lte packets](/questions/15616/error-while-dissecting-mac-lte-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15616-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15616-score" class="post-score" title="current number of votes">0</div><span id="post-15616-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, i am using Wireshark Version 1.4.3. I have downloaded mac_lte_logger.c. For its compilation I used packet-mac-lte.h which is present under /usr/local/src/wireshark-1.4.3/epan/dissectors/ But during compilation I got the error:</p><p>packet-mac-lte.h:148: error: expected ‘)’ before ‘*’ token</p><p>Since it was not able to find the definition of "packet_info" in following lines:</p><p>/ <em>Accessor function to check if a frame was considered to be ReTx</em> / int is_mac_lte_frame_retx(packet_info *pinfo, guint8 direction);</p><p>Then I commented these line and compiled the mac_lte_logger.c</p><p>cc -o diss mac_lte_logger.c</p><p>After running "diss" executable I am not able to see the dissected packet in wireshark. the same packet is visible under filter "udp.port==xxxx" but not filter "mac-lte"</p><p>Please help.<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mac-lte" rel="tag" title="see questions tagged &#39;mac-lte&#39;">mac-lte</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '12, 02:20</strong></p><img src="https://secure.gravatar.com/avatar/c234383a5e571778032d0fc85af5c327?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pravineteng&#39;s gravatar image" /><p><span>pravineteng</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pravineteng has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-15616" class="comments-container"></div><div id="comment-tools-15616" class="comment-tools"></div><div class="clear"></div><div id="comment-15616-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

