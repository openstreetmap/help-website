+++
type = "question"
title = "Display filters for AC parameters for different QOS access categories are missing in Wireshark 1.67 version"
description = '''Hello, In wireshark 1.2 version, we had display filters such as  wlan_mgt.wme.be.ac_param.ecwmin==7 or wlan_mgt.wme.bg.ac_param.txop_limit==$value where it will filter out packets with ecwmin=7 in specific access category like BE/Voice/BG/Video.  In wireshark 1.67 or higher, this display filter for ...'''
date = "2013-09-26T05:17:00Z"
lastmod = "2013-09-26T06:35:00Z"
weight = 25273
keywords = [ "display-filter" ]
aliases = [ "/questions/25273" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Display filters for AC parameters for different QOS access categories are missing in Wireshark 1.67 version](/questions/25273/display-filters-for-ac-parameters-for-different-qos-access-categories-are-missing-in-wireshark-167-version)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25273-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>In wireshark 1.2 version, we had display filters such as</p><p>wlan_mgt.wme.be.ac_param.ecwmin==7 or wlan_mgt.wme.bg.ac_param.txop_limit==$value</p><p>where it will filter out packets with ecwmin=7 in specific access category like BE/Voice/BG/Video.</p><p>In wireshark 1.67 or higher, this display filter for each Access category is not provided.</p><p>Instead they have just given a filter for each AC parameters common for all QOS access categories like below</p><p>wlan_mgt.wfa.ie.wme.acp.aci wlan_mgt.wfa.ie.wme.acp.aifsn wlan_mgt.wfa.ie.wme.acp.ecw.min wlan_mgt.wfa.ie.wme.acp.ecw.min</p><p>So we will not be able to filter the packets based on the each access category's AC parameters ?</p><p>Does anyone has a workaround or a solution for this issue ? Please suggest.</p></div><div id="question-tags" class="tags-container tags">display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '13, 05:17</strong></p><img src="https://secure.gravatar.com/avatar/b4114b9082a0f82fda642868a1d28ed3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Keerthi&#39;s gravatar image" /><p>Keerthi<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Keerthi has no accepted answers">0%</span></p></div></div><div id="comments-container-25273" class="comments-container"></div><div id="comment-tools-25273" class="comment-tools"></div><div class="clear"></div><div id="comment-25273-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25279"></span>

<div id="answer-container-25279" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25279-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>see my answer in your other question.</p><blockquote><p><a href="http://ask.wireshark.org/questions/25271/display-filter-help">http://ask.wireshark.org/questions/25271/display-filter-help</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '13, 06:35</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-25279" class="comments-container"></div><div id="comment-tools-25279" class="comment-tools"></div><div class="clear"></div><div id="comment-25279-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

