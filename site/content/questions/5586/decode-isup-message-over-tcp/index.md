+++
type = "question"
title = "Decode ISUP Message Over TCP"
description = '''I want to know how i can decode ISUP China messages that were in the data field of TCP packets. for example decode the REL message that was in the data field of TCP.'''
date = "2011-08-09T08:56:00Z"
lastmod = "2011-08-09T08:56:00Z"
weight = 5586
keywords = [ "over", "isup", "tcp" ]
aliases = [ "/questions/5586" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decode ISUP Message Over TCP](/questions/5586/decode-isup-message-over-tcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5586-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to know how i can decode ISUP China messages that were in the data field of TCP packets. for example decode the REL message that was in the data field of TCP.</p></div><div id="question-tags" class="tags-container tags">over isup tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Aug '11, 08:56</strong></p><img src="https://secure.gravatar.com/avatar/8055ad8f128ba36bb317aaf6ea84055a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aMot&#39;s gravatar image" /><p>aMot<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aMot has no accepted answers">0%</span></p></div></div><div id="comments-container-5586" class="comments-container"><span id="5591"></span><div id="comment-5591" class="comment"><div id="post-5591-score" class="comment-score"></div><div class="comment-text"><p>How is the ISUP transported over TCP? Is it, for example, using <a href="http://tools.ietf.org/html/rfc3094">TALI</a>?</p></div><div id="comment-5591-info" class="comment-info"><span class="comment-age">(09 Aug '11, 11:12)</span> Guy Harris ♦♦</div></div><span id="5593"></span><div id="comment-5593" class="comment"><div id="post-5593-score" class="comment-score"></div><div class="comment-text"><p>i prepare the SS7 signaling monitor hardware to monitor SS7 link then i send the SS7 Messages to another computer via TCP protocol. finally i want to decode the recived SS7 messages with Wireshark.</p></div><div id="comment-5593-info" class="comment-info"><span class="comment-age">(09 Aug '11, 11:26)</span> aMot</div></div><span id="5594"></span><div id="comment-5594" class="comment"><div id="post-5594-score" class="comment-score"></div><div class="comment-text"><p>So what's the protocol stack in the TCP stream you're sending? You say "SS7 link"; is that all the way down to MTP2, or is it just ISUP-over-TCP, or...?</p></div><div id="comment-5594-info" class="comment-info"><span class="comment-age">(09 Aug '11, 11:45)</span> Guy Harris ♦♦</div></div><span id="5621"></span><div id="comment-5621" class="comment"><div id="post-5621-score" class="comment-score"></div><div class="comment-text"><p>it is just ISUP (China) over TCP.</p></div><div id="comment-5621-info" class="comment-info"><span class="comment-age">(10 Aug '11, 06:51)</span> aMot</div></div></div><div id="comment-tools-5586" class="comment-tools"></div><div class="clear"></div><div id="comment-5586-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

