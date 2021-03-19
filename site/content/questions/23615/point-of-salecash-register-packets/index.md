+++
type = "question"
title = "Point of sale/cash register packets"
description = '''Buddy of mine owns a small comic book shop, and he text me and said his register has been declining credit cards. He asked me if I can come over to see what I could do, I restarted his router and modem, but cards kept getting declined (tested it with my credit card) and I connected to his router wit...'''
date = "2013-08-07T09:51:00Z"
lastmod = "2013-08-07T09:58:00Z"
weight = 23615
keywords = [ "dhcp", "of", "point", "sale", "wireshark" ]
aliases = [ "/questions/23615" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Point of sale/cash register packets](/questions/23615/point-of-salecash-register-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23615-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Buddy of mine owns a small comic book shop, and he text me and said his register has been declining credit cards. He asked me if I can come over to see what I could do, I restarted his router and modem, but cards kept getting declined (tested it with my credit card) and I connected to his router with my laptop, and decided to see if I can use wireshark and see what the packets are doing (I'm no way a expert with wireshark) and to be honest so much stuff showed up (could be because his computer is on the network too, but I am not sure) how would I filter out just for the cash register? I am sure it uses a request/ack. I did come across a dhcp protocol with transaction ID 0x0384 (thats just random but it looked like hexadecimal) is that what I am looking for?</p></div><div id="question-tags" class="tags-container tags">dhcp of point sale wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Aug '13, 09:51</strong></p><img src="https://secure.gravatar.com/avatar/083d275a2426f33251378ebf7d09dba2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lolslim&#39;s gravatar image" /><p>lolslim<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lolslim has no accepted answers">0%</span></p></div></div><div id="comments-container-23615" class="comments-container"></div><div id="comment-tools-23615" class="comment-tools"></div><div class="clear"></div><div id="comment-23615-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23616"></span>

<div id="answer-container-23616" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23616-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Seriously, your buddy should contact the credit card company/the technical support that he should have for the PoS installation. The reason is quite simple: even if you manage to sort out the packets for the cash register it will most certainly only contain heavily encrypted stuff, so you can't see anything anyway. Also, the credit card companies are usually very interested to have the payment process working, so they'll help much faster than anything else, and they can determine the cause of the problem a lot easier.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Aug '13, 09:58</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-23616" class="comments-container"><span id="23617"></span><div id="comment-23617" class="comment"><div id="post-23617-score" class="comment-score"></div><div class="comment-text"><p>Thank you, I will have him contact whoever he needs to contact. (I am sure he will know who to contact)</p></div><div id="comment-23617-info" class="comment-info"><span class="comment-age">(07 Aug '13, 10:01)</span> lolslim</div></div></div><div id="comment-tools-23616" class="comment-tools"></div><div class="clear"></div><div id="comment-23616-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

