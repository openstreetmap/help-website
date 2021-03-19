+++
type = "question"
title = "calculating ping time for a game"
description = '''hi, i need to graph the packet delay for a game called league of legends, the game uses udp and a port range between 5000-5500. im pretty sure that the delay time is calculated from the udp stream, see explanation in the link at the end. inside the game you can see what they call ping time in ms, bu...'''
date = "2013-10-16T15:43:00Z"
lastmod = "2013-11-26T05:07:00Z"
weight = 26090
keywords = [ "python", "league", "legends", "of" ]
aliases = [ "/questions/26090" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [calculating ping time for a game](/questions/26090/calculating-ping-time-for-a-game)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26090-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi,</p><p>i need to graph the packet delay for a game called league of legends, the game uses udp and a port range between 5000-5500. im pretty sure that the delay time is calculated from the udp stream, see explanation in the link at the end. inside the game you can see what they call ping time in ms, but how they measure that im not sure.</p><p>from a 2000packets capture midgame ive already calculated the following times(script at the end):</p><pre><code>between first and next client packet
between first and next server packet
between client packet and next server packet</code></pre><p>but all these come up with less then 10ms, normal ping time for the game is 20ms. do you think they calculate ping time on the server side and send the ping data back with the game data?</p><p>this is why i belive that ping time is calculcated from the UDP packets: i used the HSFC traffic shaper class to make sure ping is calculated from the UDP packets the game uses for data traffic. other ports/protocols are used as well. for that i created two classes: 1:20 and 1:30, 1:20 holds the lol packets and a scp stream if started. 1:30 is the catch all for the rest.</p><p>if scp isnt running league of legends (lol) ping is fine, if http(1:30) is downloading in parrallel with ~200kb/s as expected lol ping is fine - now if there were some other data connection that does not fall beween in the games udp port range ping would spike because of the http download. now with a running scp download ping goes up to at least 100ms, normally its 20ms.</p><p>traffic shaper / python code to calculate packet times: <a href="http://pastebin.ca/2467393">http://pastebin.ca/2467393</a></p><p>tcpdump file: <a href="http://www.file-upload.net/download-8186822/lol.pcap.html">http://www.file-upload.net/download-8186822/lol.pcap.html</a></p></div><div id="question-tags" class="tags-container tags">python league legends of</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '13, 15:43</strong></p><img src="https://secure.gravatar.com/avatar/9adcd1030ec748b5598d4de0a374f305?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="newusergreek&#39;s gravatar image" /><p>newusergreek<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="newusergreek has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Oct '13, 00:39</p></div></div><div id="comments-container-26090" class="comments-container"></div><div id="comment-tools-26090" class="comment-tools"></div><div class="clear"></div><div id="comment-26090-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="26093"></span>

<div id="answer-container-26093" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26093-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>do you think they calculate ping time on the server side and send the ping data back with the game data?</p></blockquote><p>Leage of Legends seems to use an 'in protocol' ping command (and protocol). So you need to understand the protocol to be able to calculate the same 'ping time' that the game client shows. This includes:</p><ul><li>identifying the ping request command in the protocol</li><li>identifying the ping response command in the protocol</li><li>calculating the delta time with or without time stamps in the protocol (if available)</li></ul><p>Fortunately there is a dissector for the Leage of Legends protocol.</p><blockquote><p><a href="http://code.google.com/p/packet-lol/">http://code.google.com/p/packet-lol/</a></p></blockquote><p><strong>Unfortunately</strong>, that dissector is <strong>not</strong> part of the official Wireshark code base. So, if you want to dissect the protocol, you need to add that code to the Wireshark code and compile your own version.</p><p>Please <strong>contact the original author</strong> of that dissector (see link above) for any further information how to build it, how to use it and what version of Wireshark it is compatible with. Maybe they can also provide a binary version of Wireshark that includes the dissector.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '13, 16:35</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Oct '13, 17:10</p></div></div><div id="comments-container-26093" class="comments-container"><span id="26104"></span><div id="comment-26104" class="comment"><div id="post-26104-score" class="comment-score"></div><div class="comment-text"><blockquote><p>this is why i belive that ping time is calculcated from the UDP packets:</p></blockquote><p>yes it is, with the internal ping command/protocol (see my answer). Your way to calculate the response time will create wrong results, because:</p><p>See the following command/response sequence of the Leage of Legends protocol (UDP frames in and out).</p><pre><code>cmd1,cmd2,resp1,cmd3,cmd4,resp2</code></pre><p>cmdx is: client -&gt; game server UDP outgoing respx is: game server -&gt; client UDP incoming</p><p>What you calculate is: <strong>delta(cmd2,resp1)</strong> and <strong>delta(cmd4,resp2)</strong></p><p>However, resp1 is totally unrelated to cmd1 and resp2 is unrelated to cmd4.</p><p>You cannot use just the UDP packets for the calculation, as Leage of Legends has its own protocol on top of UDP with commands, responses and internal time stamps.</p><p>So, as I said in my answer you need to understand the Leage of Legends protocol to be able to calculate the correct 'delta'.</p></div><div id="comment-26104-info" class="comment-info"><span class="comment-age">(17 Oct '13, 01:38)</span> Kurt Knochner ♦</div></div><span id="26199"></span><div id="comment-26199" class="comment"><div id="post-26199-score" class="comment-score"></div><div class="comment-text"><p>yes, i knew that i didnt knew which response came in to what packet. i just guessed.</p></div><div id="comment-26199-info" class="comment-info"><span class="comment-age">(18 Oct '13, 11:41)</span> newusergreek</div></div></div><div id="comment-tools-26093" class="comment-tools"></div><div class="clear"></div><div id="comment-26093-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26097"></span>

<div id="answer-container-26097" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26097-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I would guess you're measuring round-trip times, and the in-game UDP measurements are one-way measurements. Typically, this is how financial market data latencies are measured (using one way) since UDP is unidirectional.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '13, 19:25</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p>hansangb<br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span></p></div></div><div id="comments-container-26097" class="comments-container"></div><div id="comment-tools-26097" class="comment-tools"></div><div class="clear"></div><div id="comment-26097-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27419"></span>

<div id="answer-container-27419" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27419-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, I don't know what you need this for or what your intentions are, but there is a very simple way to do this using a program called Bot of Legends.</p><p>This program injects itself into League of Legends so it is able to grab things like ping fairly easily (among other things you're probably not interested in). As an example here is a script for avg ping (it's in lua): <a href="https://privatepaste.com/e75dfe18a3">https://privatepaste.com/e75dfe18a3</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '13, 05:07</strong></p><img src="https://secure.gravatar.com/avatar/587f34343fe9a3863cb233170692b5c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NewGuy&#39;s gravatar image" /><p>NewGuy<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NewGuy has no accepted answers">0%</span></p></div></div><div id="comments-container-27419" class="comments-container"></div><div id="comment-tools-27419" class="comment-tools"></div><div class="clear"></div><div id="comment-27419-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

