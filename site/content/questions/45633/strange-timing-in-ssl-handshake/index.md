+++
type = "question"
title = "Strange timing in SSL handshake"
description = '''Saw this pcap about a SSL handshake. The timing seems a little strange: The time between TCP SYN and SYNACK is 91ms. But the time between CLIENT_HELLO and SERVER_HELLO is only 9ms.  Wonder what&#x27;s the reason for that. '''
date = "2015-09-04T08:03:00Z"
lastmod = "2015-09-04T18:53:00Z"
weight = 45633
keywords = [ "wireshark" ]
aliases = [ "/questions/45633" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Strange timing in SSL handshake](/questions/45633/strange-timing-in-ssl-handshake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45633-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45633-score" class="post-score" title="current number of votes">0</div><span id="post-45633-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Saw this <a href="https://www.cloudshark.org/captures/33757ff5e07d">pcap</a> about a SSL handshake. The timing seems a little strange:</p><p>The time between TCP SYN and SYNACK is 91ms. But the time between CLIENT_HELLO and SERVER_HELLO is only 9ms.<br />
</p><p>Wonder what's the reason for that.<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Sep '15, 08:03</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p><span>pktUser1001</span><br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span> </br></br></p></div></div><div id="comments-container-45633" class="comments-container"></div><div id="comment-tools-45633" class="comment-tools"></div><div class="clear"></div><div id="comment-45633-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45637"></span>

<div id="answer-container-45637" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45637-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45637-score" class="post-score" title="current number of votes">0</div><span id="post-45637-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pktUser1001 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The path is probably going through a firewall infrastructure.<br />
When A SYN packet hits the firewall, it will cause a lookup in the filter rules database, create a connection entry in its stateful connection table etc.<br />
All this processing might be duplicated at the edges of the public network, so it is not surprising that the SYN packets are delayed as they are being inspected for security reasons.<br />
Once the connection is setup, the packets just pass through an 'existing' connection and are simply routed which certainly is faster...<br />
Just a thought that might or might not be the what is happening here ...</p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Sep '15, 15:50</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-45637" class="comments-container"><span id="45638"></span><div id="comment-45638" class="comment"><div id="post-45638-score" class="comment-score"></div><div class="comment-text"><p>It makes sense. Wonder what's the best way to measure round-trip time from a pcap.</p></div><div id="comment-45638-info" class="comment-info"><span class="comment-age">(04 Sep '15, 18:53)</span> <span class="comment-user userinfo">pktUser1001</span></div></div></div><div id="comment-tools-45637" class="comment-tools"></div><div class="clear"></div><div id="comment-45637-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

