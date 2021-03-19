+++
type = "question"
title = "Unable to receive the specific packet data from the network"
description = '''Hello Folks,  I&#x27;m new to this forum and an avid user of Wireshark Packet Analyzer. The problem that I&#x27;m facing is a very generic yet it would be of immense help if somebody who has a knowledge on this can answer. I&#x27;m able to see the UDP protocol connection established between the Source and Destinat...'''
date = "2017-02-01T05:18:00Z"
lastmod = "2017-02-01T05:47:00Z"
weight = 59215
keywords = [ "udp", "dissector" ]
aliases = [ "/questions/59215" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to receive the specific packet data from the network](/questions/59215/unable-to-receive-the-specific-packet-data-from-the-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59215-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59215-score" class="post-score" title="current number of votes">0</div><span id="post-59215-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Folks, I'm new to this forum and an avid user of Wireshark Packet Analyzer. The problem that I'm facing is a very generic yet it would be of immense help if somebody who has a knowledge on this can answer. I'm able to see the UDP protocol connection established between the Source and Destination but when i try to send the intended packets in the buffer location in the code, I'm unable to get the specific bytes. I can research a lot on the internet about solutions but those would be very broad to start with until somebody with an experience in answering what could be the probable reasons that my packets in the network are getting lost. I get data from all over the network. I get zeroes in the buffer section of packet location. Please guide.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Feb '17, 05:18</strong></p><img src="https://secure.gravatar.com/avatar/556b3b8aaf533233da1b82f1b90f6684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ZeeshanHashmi&#39;s gravatar image" /><p><span>ZeeshanHashmi</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ZeeshanHashmi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Feb '17, 05:44</strong> </span></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-59215" class="comments-container"><span id="59218"></span><div id="comment-59218" class="comment"><div id="post-59218-score" class="comment-score"></div><div class="comment-text"><p>UDP does not have a connection establishment, it's connectionless. So what do you see on the network, between Source and Destination related to this?</p><p>What do you mean 'I'm unable to get the specific bytes'? You don't see them in Wireshark, or not on the Destination node? Are they even transmitted from the Source?</p></div><div id="comment-59218-info" class="comment-info"><span class="comment-age">(01 Feb '17, 05:47)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-59215" class="comment-tools"></div><div class="clear"></div><div id="comment-59215-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

