+++
type = "question"
title = "How can I play back captured data"
description = '''I&#x27;ve captured packets going to a WAN router. I want to play them back at ideally a user specifed rate to a new router model so I an monitor the router&#x27;s performance using our data in our configuration.  I realize I&#x27;ll have to configure the MAC address of the new router&#x27;s interface to match the MAC i...'''
date = "2011-05-13T12:50:00Z"
lastmod = "2014-06-16T05:51:00Z"
weight = 4072
keywords = [ "playback", "data", "captured" ]
aliases = [ "/questions/4072" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [How can I play back captured data](/questions/4072/how-can-i-play-back-captured-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4072-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've captured packets going to a WAN router. I want to play them back at ideally a user specifed rate to a new router model so I an monitor the router's performance using our data in our configuration.<br />
</p><p>I realize I'll have to configure the MAC address of the new router's interface to match the MAC in the captured packets.</p></div><div id="question-tags" class="tags-container tags">playback data captured</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 May '11, 12:50</strong></p><img src="https://secure.gravatar.com/avatar/06ee8b72a5034e6c5bd688cd0a684ecf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DonDCajun&#39;s gravatar image" /><p>DonDCajun<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DonDCajun has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-4072" class="comments-container"></div><div id="comment-tools-4072" class="comment-tools"></div><div class="clear"></div><div id="comment-4072-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="4076"></span>

<div id="answer-container-4076" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4076-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, you indeed need to change the mac-address of the traffic. You would also need to split the traffic into incoming and outgoing traffic, as you would want both to be injected to a different interface (internal and external interface). The the router must not do anything else than routing. Even NAT will break this kind of reproduction...</p><p>A tool that you can use to replace the mac-addresses is <a href="http://bittwist.sourceforge.net/">bittwist</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '11, 13:51</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4076" class="comments-container"><span id="4077"></span><div id="comment-4077" class="comment"><div id="post-4077-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the comment. Several of my captures are one way only so no need to separate.</p><p>BUT how do I play back the traffic?????</p></div><div id="comment-4077-info" class="comment-info"><span class="comment-age">(13 May '11, 14:04)</span> DonDCajun</div></div><span id="4078"></span><div id="comment-4078" class="comment"><div id="post-4078-score" class="comment-score"></div><div class="comment-text"><p>You can also do that with bittwist (actually, bittwist will replay the traffic after you first changed the mac-addresses with bittwiste which is also in the suite).</p></div><div id="comment-4078-info" class="comment-info"><span class="comment-age">(13 May '11, 14:06)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-4076" class="comment-tools"></div><div class="clear"></div><div id="comment-4076-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14365"></span>

<div id="answer-container-14365" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14365-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you only want to replay one TCP/UDP stream, you can use <a href="http://netexpect.org/wiki/NetworkExpect">NetworkExpect</a> with your <a href="http://netexpect.org/wiki/PacketHexDump">captured data</a>. See also <a href="http://netexpect.org/wiki/RewriteAndReplay">Rewrite And Replay</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Sep '12, 13:59</strong></p><img src="https://secure.gravatar.com/avatar/d797538504a367f277d19bd8369e9a19?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Janus%20Troelsen&#39;s gravatar image" /><p>Janus Troelsen<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Janus Troelsen has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Sep '12, 14:07</p></div></div><div id="comments-container-14365" class="comments-container"></div><div id="comment-tools-14365" class="comment-tools"></div><div class="clear"></div><div id="comment-14365-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16687"></span>

<div id="answer-container-16687" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16687-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can play back using <a href="http://sourceforge.net/projects/tcpreplay/">TCP Replay</a>. This application exactly replay the captured traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '12, 08:03</strong></p><img src="https://secure.gravatar.com/avatar/2c33bce451fd8dc3844b351b798cbee1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fates&#39;s gravatar image" /><p>fates<br />
<span class="score" title="35 reputation points">35</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fates has no accepted answers">0%</span></p></div></div><div id="comments-container-16687" class="comments-container"></div><div id="comment-tools-16687" class="comment-tools"></div><div class="clear"></div><div id="comment-16687-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33860"></span>

<div id="answer-container-33860" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33860-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I use <a href="http://www.colasoft.com/download/products/download_packet_player.php">Colasoft Packet Player</a>. I have also used a commandline utility named Preplay (PacketSendingUtility.exe) from <a href="http://www.secgeeks.com">Secgeeks</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jun '14, 05:51</strong></p><img src="https://secure.gravatar.com/avatar/c92e01769c957228c35d0ef9c1b61b8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alfa&#39;s gravatar image" /><p>alfa<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alfa has no accepted answers">0%</span></p></div></div><div id="comments-container-33860" class="comments-container"></div><div id="comment-tools-33860" class="comment-tools"></div><div class="clear"></div><div id="comment-33860-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

