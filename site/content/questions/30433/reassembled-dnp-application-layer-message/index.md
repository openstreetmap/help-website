+++
type = "question"
title = "Reassembled DNP  Application Layer Message"
description = '''Hi ,  when i&#x27;m examining DNP 3 packets i noticed that you parsed some packets that in the bytes pane windows there was &quot;Reassamble DNP AL Message&quot;. how can i know how to parse it? (did you only use the specification?) thanks , '''
date = "2014-03-05T00:24:00Z"
lastmod = "2014-03-05T03:22:00Z"
weight = 30433
keywords = [ "dnp" ]
aliases = [ "/questions/30433" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Reassembled DNP Application Layer Message](/questions/30433/reassembled-dnp-application-layer-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30433-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30433-score" class="post-score" title="current number of votes">0</div><span id="post-30433-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi ,</p><p>when i'm examining DNP 3 packets i noticed that you parsed some packets that in the bytes pane windows there was "Reassamble DNP AL Message".</p><p>how can i know how to parse it? (did you only use the specification?)</p><p>thanks ,<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dnp" rel="tag" title="see questions tagged &#39;dnp&#39;">dnp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Mar '14, 00:24</strong></p><img src="https://secure.gravatar.com/avatar/8e63c6464bed174c7c39c659f39e5392?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eligator28&#39;s gravatar image" /><p><span>eligator28</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eligator28 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-30433" class="comments-container"></div><div id="comment-tools-30433" class="comment-tools"></div><div class="clear"></div><div id="comment-30433-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30439"></span>

<div id="answer-container-30439" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30439-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30439-score" class="post-score" title="current number of votes">1</div><span id="post-30439-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As a DNP3 datalink layer message body can only be 250 octets long, and as that body only carries 222 octets of payload (2 octet CRC for every 16 octets of data), and as the Transport layer header consumes 1 octet in every data link layer, and as an Application Layer message may be fragmented into multiple parts to ease memory requirements, the dissector extracts all the relevant portions of data from multiple data link messages and reassembles them into the complete application layer message.</p><p>The dissector was written with access to the protocol specification and has been tested with numerous actual master and slave devices. You can browse the source code of the dissector <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-dnp.c;hb=HEAD">here</a>, but note that it uses the Wireshark packet reassembly routines to do the bulk of the work.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '14, 03:22</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-30439" class="comments-container"></div><div id="comment-tools-30439" class="comment-tools"></div><div class="clear"></div><div id="comment-30439-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

