+++
type = "question"
title = "how to decode a CITRIX capture"
description = '''I have a pcap of a citrix capture within a citrix network. I am trying to replay this in a not citrix environment to simulate the traffic for test purposes. When i look at the pcap, &quot;citrix&quot; or ICA is not seen in the decode. When I try to decode as, Citrix and ICA are not seen. What am i missing? Or...'''
date = "2012-08-30T09:29:00Z"
lastmod = "2012-09-04T01:46:00Z"
weight = 13965
keywords = [ "decode", "as", "citrix" ]
aliases = [ "/questions/13965" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to decode a CITRIX capture](/questions/13965/how-to-decode-a-citrix-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13965-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a pcap of a citrix capture within a citrix network. I am trying to replay this in a not citrix environment to simulate the traffic for test purposes. When i look at the pcap, "citrix" or ICA is not seen in the decode. When I try to decode as, Citrix and ICA are not seen.</p><p>What am i missing? Or is a Citrix capture decode not supported?</p></div><div id="question-tags" class="tags-container tags">decode as citrix</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Aug '12, 09:29</strong></p><img src="https://secure.gravatar.com/avatar/04259ce7fce28ac9b7d7ba5f54596140?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lenalbanese&#39;s gravatar image" /><p>lenalbanese<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lenalbanese has no accepted answers">0%</span></p></div></div><div id="comments-container-13965" class="comments-container"></div><div id="comment-tools-13965" class="comment-tools"></div><div class="clear"></div><div id="comment-13965-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="13967"></span>

<div id="answer-container-13967" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13967-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark cannot decode the Citrix ICA protocol since it is a proprietary protocol. Only a few commercial analyzers like Sniffer Pro or Clearsight can "decode" it after having signed an NDA (as far as I know), but last time I checked their decodes were far from perfect and do not help much anyway.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '12, 15:32</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-13967" class="comments-container"></div><div id="comment-tools-13967" class="comment-tools"></div><div class="clear"></div><div id="comment-13967-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14015"></span>

<div id="answer-container-14015" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14015-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark cannot.</p><p>Sniffer Global / A3(A-CUBE) /Netscout Probe /PM from Netscout Systems will decode it <a href="http://www.netscout.com"></a><a href="http://www.sniffer.com">www.sniffer.com</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Sep '12, 01:46</strong></p><img src="https://secure.gravatar.com/avatar/0cf7e05b14ad6662ecde4c327bb2c39f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harsha&#39;s gravatar image" /><p>Harsha<br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harsha has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Sep '12, 01:47</p></div></div><div id="comments-container-14015" class="comments-container"></div><div id="comment-tools-14015" class="comment-tools"></div><div class="clear"></div><div id="comment-14015-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

