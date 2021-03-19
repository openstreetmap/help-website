+++
type = "question"
title = "Gateway Settings"
description = '''Hello!  If a network has newly reconfigured routers, how can you use Wireshark to check if the default gateway settings for the hosts are correct? Thanks!'''
date = "2012-03-25T10:22:00Z"
lastmod = "2012-03-26T11:24:00Z"
weight = 9747
keywords = [ "correct", "hosts", "gateway", "settings" ]
aliases = [ "/questions/9747" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Gateway Settings](/questions/9747/gateway-settings)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9747-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello! If a network has newly reconfigured routers, how can you use Wireshark to check if the default gateway settings for the hosts are correct? Thanks!</p></div><div id="question-tags" class="tags-container tags">correct hosts gateway settings</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Mar '12, 10:22</strong></p><img src="https://secure.gravatar.com/avatar/76a2cf301464c2ff14df94fd8042e00f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cveti&#39;s gravatar image" /><p>Cveti<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cveti has no accepted answers">0%</span></p></div></div><div id="comments-container-9747" class="comments-container"></div><div id="comment-tools-9747" class="comment-tools"></div><div class="clear"></div><div id="comment-9747-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9760"></span>

<div id="answer-container-9760" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9760-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could hook up Wireshark at the mirror port and look for ARP requests for the old routers.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '12, 03:53</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-9760" class="comments-container"></div><div id="comment-tools-9760" class="comment-tools"></div><div class="clear"></div><div id="comment-9760-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9770"></span>

<div id="answer-container-9770" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9770-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wirehark may not be the best tool for this. Perhaps you should just be going to the hosts and checking the settings directly, for example, with <em>ipconfig</em> on Windows hosts.</p><p>If your hosts are getting their configuration from DHCP, you can check the configuration that the DHCP server is handing out.</p><p>Is there a communications problem that leads you to believe the default gateway may not be correct?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '12, 11:24</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-9770" class="comments-container"><span id="9773"></span><div id="comment-9773" class="comment"><div id="post-9773-score" class="comment-score"></div><div class="comment-text"><p>Yes, there were some problems. I was just wondering if there is a faster way to check the settings (by using a network analyzer) than doing ipconfig from each workstation. Thanks for the answers!</p></div><div id="comment-9773-info" class="comment-info"><span class="comment-age">(26 Mar '12, 14:55)</span> Cveti</div></div><span id="9782"></span><div id="comment-9782" class="comment"><div id="post-9782-score" class="comment-score"></div><div class="comment-text"><p>@Cveti: If you like an answer it's customary to click the check, to mark it as the accepted answer.</p></div><div id="comment-9782-info" class="comment-info"><span class="comment-age">(27 Mar '12, 00:29)</span> Jaap ♦</div></div></div><div id="comment-tools-9770" class="comment-tools"></div><div class="clear"></div><div id="comment-9770-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

