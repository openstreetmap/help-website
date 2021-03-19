+++
type = "question"
title = "how to decode mef8 88d8 protocol"
description = '''Hi I will appreciate help . I am using Version 1.8.1 (SVN Rev 43946 from /trunk-1.8). My packet stack is eth 88a8 8100 88d8. The application recognizes 88d8 as MEF 8 but the protocol is not decoded. I tried in several protocols enable: 1. All  2. Ethernet , Vlan, IEEE8021.D with several combination ...'''
date = "2012-08-13T05:18:00Z"
lastmod = "2012-08-15T04:02:00Z"
weight = 13583
keywords = [ "decode", "mef8", "pw" ]
aliases = [ "/questions/13583" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to decode mef8 88d8 protocol](/questions/13583/how-to-decode-mef8-88d8-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13583-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="http://" alt="alt text" />Hi I will appreciate help . I am using Version 1.8.1 (SVN Rev 43946 from /trunk-1.8). My packet stack is eth 88a8 8100 88d8. The application recognizes 88d8 as MEF 8 but the protocol is not decoded. I tried in several protocols enable: 1. All 2. Ethernet , Vlan, IEEE8021.D with several combination of the following a. Ethernet PW (CW heuristic) b. Ethernet PW (no CW) c. Ethernet PW (with CW) d. SATop ( no RTP) e. CESoPSN basic (no RTP) More than that when I try to use the decode option only the mandatory 3 are avialble. TX Bentzi</p><p><img src="http://" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">decode mef8 pw</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Aug '12, 05:18</strong></p><img src="https://secure.gravatar.com/avatar/ec602eeb5c9bd0be3c1ade340de7fb2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bentzii&#39;s gravatar image" /><p>bentzii<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bentzii has no accepted answers">0%</span></p></img></div></div><div id="comments-container-13583" class="comments-container"></div><div id="comment-tools-13583" class="comment-tools"></div><div class="clear"></div><div id="comment-13583-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13652"></span>

<div id="answer-container-13652" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13652-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The MEF-8 dissector isn't available (yet). What you see ("MEF 8") is the interpretation by the Ethertype dissector for the value in the Ethernet header, but that is as far as it goes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Aug '12, 04:02</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></img></div></div><div id="comments-container-13652" class="comments-container"></div><div id="comment-tools-13652" class="comment-tools"></div><div class="clear"></div><div id="comment-13652-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

