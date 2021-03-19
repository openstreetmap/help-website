+++
type = "question"
title = "How can I find the inbound and outbound traffic from a captured file"
description = '''I have the wind 7 PC with Wireshark installed. I captured the traffic from my network card interface. How can I tell it is the inbound or outbound traffic from the captured file? Thank you'''
date = "2014-04-30T15:31:00Z"
lastmod = "2014-04-30T19:55:00Z"
weight = 32326
keywords = [ "wireshark" ]
aliases = [ "/questions/32326" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I find the inbound and outbound traffic from a captured file](/questions/32326/how-can-i-find-the-inbound-and-outbound-traffic-from-a-captured-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32326-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have the wind 7 PC with Wireshark installed. I captured the traffic from my network card interface. How can I tell it is the inbound or outbound traffic from the captured file? Thank you</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Apr '14, 15:31</strong></p><img src="https://secure.gravatar.com/avatar/d9695580361f0a23df499811e535b694?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="log&#39;s gravatar image" /><p>log<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="log has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 May '14, 01:55</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-32326" class="comments-container"></div><div id="comment-tools-32326" class="comment-tools"></div><div class="clear"></div><div id="comment-32326-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="32330"></span>

<div id="answer-container-32330" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32330-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If the packets are coming from the IP your Windows 7 PC had during capture they are outgoing. If they're sent to the IP of the PC they're incoming. You can also do this based on the Ethernet MAC address of the PC's network card (which you can find out by entering "ipconfig /all" on a command prompt).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '14, 16:56</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-32330" class="comments-container"></div><div id="comment-tools-32330" class="comment-tools"></div><div class="clear"></div><div id="comment-32330-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="32334"></span>

<div id="answer-container-32334" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32334-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hopefully since your here you know your IP and MAC Address, but if not use cmd prompt with command Ipconfig /all or viewing Control Panel&gt; Network and Internet&gt;Networking Sharing Center&gt;View Network Status and Tasks. Then under active networks click the connections link and select details.</p><p>Your capture shows source and destination column containing addresses. If your IP is in the source column, the traffic is outgoing, if your IP is in the destination column then the traffic is incoming. If the traffic shows 255.255.255.255 in the destination it is broadcast traffic on your subnet and can be incoming if the source is from another IP address. There are also multicast addresses that start with 224.x.x.x that can also be incoming if from another IP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '14, 19:55</strong></p><img src="https://secure.gravatar.com/avatar/3179a2e857857fc32eb5d30f074546b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cptamericajd&#39;s gravatar image" /><p>cptamericajd<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cptamericajd has no accepted answers">0%</span></p></div></div><div id="comments-container-32334" class="comments-container"><span id="32355"></span><div id="comment-32355" class="comment"><div id="post-32355-score" class="comment-score"></div><div class="comment-text"><p>Thank you Jasper and Cptamericajd. You answer is very helpful. I am clear now. Thank you again.</p></div><div id="comment-32355-info" class="comment-info"><span class="comment-age">(01 May '14, 09:53)</span> log</div></div></div><div id="comment-tools-32334" class="comment-tools"></div><div class="clear"></div><div id="comment-32334-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

