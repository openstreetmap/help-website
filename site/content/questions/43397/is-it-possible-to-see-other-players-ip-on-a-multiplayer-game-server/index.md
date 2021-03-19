+++
type = "question"
title = "Is it possible to see other players IP on a multiplayer game server?"
description = '''Hey everyone, I would like to know if its possible to see the IP&#x27;s of other players on a multiplayer server. If i use ip.addr == (IP Server) in the filter then the only ip addresses it gives me are mine and the servers. Does the server keeps the IP&#x27;s of its players and never send it to others? Sorry...'''
date = "2015-06-20T05:23:00Z"
lastmod = "2015-06-21T07:49:00Z"
weight = 43397
keywords = [ "finding", "ip" ]
aliases = [ "/questions/43397" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to see other players IP on a multiplayer game server?](/questions/43397/is-it-possible-to-see-other-players-ip-on-a-multiplayer-game-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43397-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey everyone,</p><p>I would like to know if its possible to see the IP's of other players on a multiplayer server. If i use ip.addr == (IP Server) in the filter then the only ip addresses it gives me are mine and the servers. Does the server keeps the IP's of its players and never send it to others?</p><p>Sorry for my bad english.</p><p>Greetings</p></div><div id="question-tags" class="tags-container tags">finding ip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jun '15, 05:23</strong></p><img src="https://secure.gravatar.com/avatar/b27506631fad2d90185abf01fc10eed2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SuperVanquisher&#39;s gravatar image" /><p>SuperVanquisher<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SuperVanquisher has no accepted answers">0%</span></p></div></div><div id="comments-container-43397" class="comments-container"><span id="43400"></span><div id="comment-43400" class="comment"><div id="post-43400-score" class="comment-score">1</div><div class="comment-text"><pre><code>Does the server keeps the IP&#39;s of its players and never send it to others?</code></pre><p>Easily said: Yes that is what a server does. A server does not share all his connected client with these clients. Think about a webserver.</p><p>If the server should send the connected IPs around then it has to be done by the application and not by the network layer.</p></div><div id="comment-43400-info" class="comment-info"><span class="comment-age">(20 Jun '15, 16:39)</span> Christian_R</div></div></div><div id="comment-tools-43397" class="comment-tools"></div><div class="clear"></div><div id="comment-43397-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43401"></span>

<div id="answer-container-43401" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43401-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It depends on the protocol they are using for the game traffic. There are (at least) two methods:</p><ol><li>relay the whole game traffic over central servers</li><li>use some form of P2P protocol to let clients talk to each other directly</li></ol><p>In case 1. you won't see the IP address of other players, as your game client will only communicate with the game server(s).</p><p>In case 2. you might see the IP address of other players. It depends on the nature of the P2P protocol.</p><p>See a similar discussion:</p><blockquote><p><a href="https://ask.wireshark.org/questions/40225/unable-to-capture-remote-ip-on-omegle-please-help">https://ask.wireshark.org/questions/40225/unable-to-capture-remote-ip-on-omegle-please-help</a></p></blockquote><p>I suggest to ask the same question in a forum for the game you are interested in. I guess other users of that game should know if it's possible or not.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '15, 07:49</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-43401" class="comments-container"><span id="43403"></span><div id="comment-43403" class="comment"><div id="post-43403-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answers! This is good to know. So i guess the only way to get to people's IP through a Relay server is by actually breaking in the server?</p><p>Anyway thatnks allot for clearing this up for me!</p><p>Greetings</p></div><div id="comment-43403-info" class="comment-info"><span class="comment-age">(21 Jun '15, 09:22)</span> SuperVanquisher</div></div><span id="43404"></span><div id="comment-43404" class="comment"><div id="post-43404-score" class="comment-score"></div><div class="comment-text"><blockquote><p>So i guess the only way to get to people's IP through a Relay server is by actually breaking in the server?</p></blockquote><p>Well yes, if you look at it that way ;-)</p></div><div id="comment-43404-info" class="comment-info"><span class="comment-age">(21 Jun '15, 09:37)</span> Kurt Knochner ♦</div></div><span id="43405"></span><div id="comment-43405" class="comment"><div id="post-43405-score" class="comment-score"></div><div class="comment-text"><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-43405-info" class="comment-info"><span class="comment-age">(21 Jun '15, 09:37)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-43401" class="comment-tools"></div><div class="clear"></div><div id="comment-43401-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

