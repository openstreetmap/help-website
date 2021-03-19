+++
type = "question"
title = "Why am I getting DUP ACK from the HOST and retransmissions from the SERVER?"
description = '''When I see the trace in wireshark, what I see is the client sending DUP ACK to the server and the server keeps on Retransmitting the data? What does this situation signify? How to correct this?'''
date = "2013-09-25T06:36:00Z"
lastmod = "2013-09-25T10:18:00Z"
weight = 25211
keywords = [ "dupack", "retransmissions" ]
aliases = [ "/questions/25211" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why am I getting DUP ACK from the HOST and retransmissions from the SERVER?](/questions/25211/why-am-i-getting-dup-ack-from-the-host-and-retransmissions-from-the-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25211-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25211-score" class="post-score" title="current number of votes">0</div><span id="post-25211-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I see the trace in wireshark, what I see is the client sending DUP ACK to the server and the server keeps on Retransmitting the data? What does this situation signify? How to correct this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dupack" rel="tag" title="see questions tagged &#39;dupack&#39;">dupack</span> <span class="post-tag tag-link-retransmissions" rel="tag" title="see questions tagged &#39;retransmissions&#39;">retransmissions</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '13, 06:36</strong></p><img src="https://secure.gravatar.com/avatar/35b2a87d9cc60520bbf423e4ba8370d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vaibhav%20Khare&#39;s gravatar image" /><p><span>Vaibhav Khare</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vaibhav Khare has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Sep '13, 11:21</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-25211" class="comments-container"><span id="25228"></span><div id="comment-25228" class="comment"><div id="post-25228-score" class="comment-score"></div><div class="comment-text"><p>Your situation is not clear. Do you have a trace that you can upload to <a href="http://www.cloudshark.org">http://www.cloudshark.org</a>? If not: how many DUP ACKs do you see? are they all for the same packet, or are there many DUP ACKs for different packets? Are the retransmissions for the same packet, or for different packets? How did you capture? On a SPAN port? Multiple source ports/VLANs, or just one port?</p></div><div id="comment-25228-info" class="comment-info"><span class="comment-age">(25 Sep '13, 10:18)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-25211" class="comment-tools"></div><div class="clear"></div><div id="comment-25211-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

