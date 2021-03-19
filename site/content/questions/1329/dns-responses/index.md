+++
type = "question"
title = "DNS responses"
description = '''Ok, a simple question here. I&#x27;m trying to trace DNS traffic. I&#x27;ve enable port spanning to watch traffic. I use DNS as the filter. I see all the DNS queries going to my DNS but I see no responses, and I know it gets a response because it resolves. Am I missing a setting somewhere? Some more info. I a...'''
date = "2010-12-13T13:10:00Z"
lastmod = "2010-12-17T09:10:00Z"
weight = 1329
keywords = [ "response", "dns" ]
aliases = [ "/questions/1329" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [DNS responses](/questions/1329/dns-responses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1329-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Ok, a simple question here. I'm trying to trace DNS traffic. I've enable port spanning to watch traffic. I use DNS as the filter. I see all the DNS queries going to my DNS but I see no responses, and I know it gets a response because it resolves. Am I missing a setting somewhere?</p><p>Some more info.</p><p>I am Spaning from port 15 cisco 4948( where the server is connected to the switch) to port 13 ( where my laptop with wireshark is connected) The server only has one NIC. I can see traffic of diffrent types leaving and entering the server.</p><p>in regards to span</p><p>Encapsulation : Native Ingress : Disabled Learning : Disabled Filter Pkt Type : RX Only : Good</p><p>I did try it on a diffrent switch with no show filter type so I assume it is set to both.</p><p>I tried the requested (vlan and dns) filter with no change</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">response dns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Dec '10, 13:10</strong></p><img src="https://secure.gravatar.com/avatar/44a4c1dac6233a4b873d23629b876d1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tubamaphoner&#39;s gravatar image" /><p>tubamaphoner<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tubamaphoner has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Dec '10, 08:58</p></div></div><div id="comments-container-1329" class="comments-container"><span id="1331"></span><div id="comment-1331" class="comment"><div id="post-1331-score" class="comment-score"></div><div class="comment-text"><p>Where are you spanning? Although the default for cisco switches is to span TX/RX, it's possible that someone set it up to be RX only.</p><p>Or it's possible that your server is using a teaming adapter (Etherchannel or LACP bundles) and you are watching only one adapter.<br />
</p><p>Finally, it's possible that your server has two NICs and the return traffic is coming in via the other NIC.</p></div><div id="comment-1331-info" class="comment-info"><span class="comment-age">(13 Dec '10, 14:14)</span> hansangb</div></div><span id="1339"></span><div id="comment-1339" class="comment"><div id="post-1339-score" class="comment-score"></div><div class="comment-text"><p>... or could it be that the request is not vlan tagged and the response is vlan tagged? Could you try the filter "dns or (vlan and dns)"?</p></div><div id="comment-1339-info" class="comment-info"><span class="comment-age">(14 Dec '10, 01:27)</span> SYN-bit ♦♦</div></div><span id="1345"></span><div id="comment-1345" class="comment"><div id="post-1345-score" class="comment-score"></div><div class="comment-text"><p>@SYNbit: I don't have a trace to check this, but I wonder if you would really need to add "vlan and dns" if you're already filtering on dns. As far as my experience goes Wireshark tries to find matches (I would call it greedy), so an additional VLAN tag would not exclude a DNS packet IMHO because it is still a DNS packet. Or am I mistaken?</p></div><div id="comment-1345-info" class="comment-info"><span class="comment-age">(14 Dec '10, 09:26)</span> Jasper ♦♦</div></div><span id="1395"></span><div id="comment-1395" class="comment"><div id="post-1395-score" class="comment-score"></div><div class="comment-text"><p>"but I wonder if you would really need to add "vlan and dns" if you're already filtering on dns"</p><p>In a capture filter, yes, you do. That's libpcap/WinPcap, not Wireshark, doing the filtering, and it requires the "vlan and" to find VLAN-encapsulated DNS packets.</p><p>In a display filter, no, you don't.</p></div><div id="comment-1395-info" class="comment-info"><span class="comment-age">(18 Dec '10, 18:35)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-1329" class="comment-tools"></div><div class="clear"></div><div id="comment-1329-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1383"></span>

<div id="answer-container-1383" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1383-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>"I can see traffic of different types leaving and entering the server." Then the span and the capture is correctly set up.</p><p>You say "it resolves" : then another machine (or local file) did it. Try to figure out the source of it</p><p>on a windows client : nslookup (ENTER and check the default server)</p><p>on a linux client : dig (ENTER and check for the line begining with ";; SERVER:")</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '10, 09:10</strong></p><img src="https://secure.gravatar.com/avatar/510925bc19c48cf1ccdb6c2b93f119ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frame&#39;s gravatar image" /><p>frame<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frame has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Dec '10, 09:16</p></div></div><div id="comments-container-1383" class="comments-container"><span id="1419"></span><div id="comment-1419" class="comment"><div id="post-1419-score" class="comment-score"></div><div class="comment-text"><p>Wait...can you type "show span" or "show monitor" and post the output?</p></div><div id="comment-1419-info" class="comment-info"><span class="comment-age">(20 Dec '10, 19:04)</span> hansangb</div></div></div><div id="comment-tools-1383" class="comment-tools"></div><div class="clear"></div><div id="comment-1383-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

