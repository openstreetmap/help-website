+++
type = "question"
title = "winpcap Lua disector"
description = '''Hi, I&#x27;m working with an Inner protocol (made up in the company I&#x27;m working), using the winpcap driver. Can I write a Lua disector to a winpcap protocol? If so I&#x27;m not sure how, since I don&#x27;t have a specific port/ address I can set the dissector to work on. Can you please advice if posible and how? T...'''
date = "2016-07-21T04:38:00Z"
lastmod = "2016-07-21T04:38:00Z"
weight = 54216
keywords = [ "winpcap", "dissector", "lua" ]
aliases = [ "/questions/54216" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [winpcap Lua disector](/questions/54216/winpcap-lua-disector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54216-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm working with an Inner protocol (made up in the company I'm working), using the winpcap driver. Can I write a Lua disector to a winpcap protocol?<br />
If so I'm not sure how, since I don't have a specific port/ address I can set the dissector to work on. Can you please advice if posible and how?</p><p>Thanks, Dana.</p></div><div id="question-tags" class="tags-container tags">winpcap dissector lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jul '16, 04:38</strong></p><img src="https://secure.gravatar.com/avatar/875df97aef066b94b202e3bf76a771c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DanaR&#39;s gravatar image" /><p>DanaR<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DanaR has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-54216" class="comments-container"><span id="54217"></span><div id="comment-54217" class="comment"><div id="post-54217-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure where the winpcap driver fits in here, that's for capturing traffic for all protocols, not dissecting them.</p><p>What protocol carries your protocol, i.e. does it run over tcp or udp or something else?</p></div><div id="comment-54217-info" class="comment-info"><span class="comment-age">(21 Jul '16, 05:26)</span> grahamb ♦</div></div><span id="54218"></span><div id="comment-54218" class="comment"><div id="post-54218-score" class="comment-score"></div><div class="comment-text"><p>No. My protocol is not udp or TCP, it is an "made up" protocol using "wpcap.dll" . (not a very standart use of winpcap, but this is the case in here )</p></div><div id="comment-54218-info" class="comment-info"><span class="comment-age">(21 Jul '16, 05:37)</span> DanaR</div></div><span id="54219"></span><div id="comment-54219" class="comment"><div id="post-54219-score" class="comment-score"></div><div class="comment-text"><p>I'll try to be more clear: In the company I'm working in a new protocol was writen from scratch, including the low level network layer . No address is actuly needed since two computers are talking using a direct cable. In order to send and recive packets we are using "wpcap.dll", pcap_open/ pcap_sendqueue_transmit and other interface options. I'm trying to undersant if I can create a LUA to such a protocol ? (Thanks :)</p></div><div id="comment-54219-info" class="comment-info"><span class="comment-age">(21 Jul '16, 05:49)</span> DanaR</div></div><span id="54220"></span><div id="comment-54220" class="comment"><div id="post-54220-score" class="comment-score"></div><div class="comment-text"><p>Presumably you are using Ethernet though? What do you see when you capture this traffic?</p></div><div id="comment-54220-info" class="comment-info"><span class="comment-age">(21 Jul '16, 06:38)</span> grahamb ♦</div></div><span id="54221"></span><div id="comment-54221" class="comment"><div id="post-54221-score" class="comment-score"></div><div class="comment-text"><p>What you're trying to say is that you are developing a raw Ethernet protocol, and use winpcap to get it on the wire. In that case it's not called a winpcap protocol but an Ethernet protocol. There are several: IPv4 may be the best known, but there are <a href="https://www.iana.org/assignments/ieee-802-numbers/ieee-802-numbers.xhtml#ieee-802-numbers-1">many more</a>.</p></div><div id="comment-54221-info" class="comment-info"><span class="comment-age">(21 Jul '16, 06:49)</span> Jaap ♦</div></div></div><div id="comment-tools-54216" class="comment-tools"></div><div class="clear"></div><div id="comment-54216-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

