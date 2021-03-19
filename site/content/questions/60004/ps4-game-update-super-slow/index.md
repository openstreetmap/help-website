+++
type = "question"
title = "ps4 game update super slow"
description = '''Hello other sharks ! Recently I bought a new ps4 pro , the most game update taking very long and than they break completly and the download starts again.  Not every Update is slow sometimes a update runs well the next one is slow again.  I did a trace from a broken one and know need help from the co...'''
date = "2017-03-11T06:39:00Z"
lastmod = "2017-03-18T05:15:00Z"
weight = 60004
keywords = [ "gaming", "capture" ]
aliases = [ "/questions/60004" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ps4 game update super slow](/questions/60004/ps4-game-update-super-slow)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60004-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60004-score" class="post-score" title="current number of votes">0</div><span id="post-60004-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello other sharks !</p><p>Recently I bought a new ps4 pro , the most game update taking very long and than they break completly and the download starts again.</p><p>Not every Update is slow sometimes a update runs well the next one is slow again.</p><p>I did a trace from a broken one and know need help from the community.</p><p><a href="https://www.cloudshark.org/captures/0eaa7754549e">https://www.cloudshark.org/captures/0eaa7754549e</a></p><p>Packet 15 PS &amp; 17 (sony server )shows an encrypted alert 21 in ssl . Followed by a reset by the ps4 itself.</p><p>Is there anything I can do ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gaming" rel="tag" title="see questions tagged &#39;gaming&#39;">gaming</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Mar '17, 06:39</strong></p><img src="https://secure.gravatar.com/avatar/6bb7322c1d4291e1019cfc6c2c4bc110?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sharky1337&#39;s gravatar image" /><p><span>sharky1337</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sharky1337 has no accepted answers">0%</span></p></div></div><div id="comments-container-60004" class="comments-container"></div><div id="comment-tools-60004" class="comment-tools"></div><div class="clear"></div><div id="comment-60004-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60025"></span>

<div id="answer-container-60025" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60025-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60025-score" class="post-score" title="current number of votes">1</div><span id="post-60025-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As there has been data exchanged between the client and the server, the "Encrypted Alert" is most likely just a normal "Close Notify", which is the proper way to close the connection at the SSL layer (like the FIN does for the TCP layer). The TCP/RST packets are probably sent by the PS4 as it already has closed the TCP session before it receievd back the "Encrypted Alert" and the TCP/FIN after ~185ms.</p><p>The question is why is there a round trip time of ~185ms throughout the tracefile? This is quite a long RTT. Combined with some packet loss, this can cause slow download speeds. Is the PS4 connected through WiFi or wired?</p><p>Could you provide a capture of the actual download of a game update that takes a long time?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '17, 02:57</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-60025" class="comments-container"><span id="60163"></span><div id="comment-60163" class="comment"><div id="post-60163-score" class="comment-score"></div><div class="comment-text"><p>I tried a connection via wifi &amp; wired and both are slow.</p><p>Year but it is pretty big.</p><p><a href="https://www.dropbox.com/s/nuk98t03cxrjehz/ps4-via-eth-game-update-slow.pcap?dl=0">https://www.dropbox.com/s/nuk98t03cxrjehz/ps4-via-eth-game-update-slow.pcap?dl=0</a></p></div><div id="comment-60163-info" class="comment-info"><span class="comment-age">(18 Mar '17, 05:15)</span> <span class="comment-user userinfo">sharky1337</span></div></div></div><div id="comment-tools-60025" class="comment-tools"></div><div class="clear"></div><div id="comment-60025-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

