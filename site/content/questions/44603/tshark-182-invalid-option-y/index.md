+++
type = "question"
title = "tshark 1.8.2: invalid option -- &#x27;Y&#x27;"
description = '''Hi,  I am running following command with tshark 1.8.2  tshark -nr 2calls.pcap -Y &quot;ip.src eq 207.239.33.54 || ip.dst eq 207.239.33.54 &quot; -w final.cap But always encounter this type of error. tshark: invalid option -- &#x27;Y&#x27; Running tshark -h does not show display filter option.  I tried installing tshark...'''
date = "2015-07-29T12:57:00Z"
lastmod = "2015-07-29T13:12:00Z"
weight = 44603
keywords = [ "display-filter", "tshark", "wireshark" ]
aliases = [ "/questions/44603" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark 1.8.2: invalid option -- 'Y'](/questions/44603/tshark-182-invalid-option-y)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44603-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am running following command with tshark 1.8.2<br />
</p><p><strong>tshark -nr 2calls.pcap -Y "ip.src eq 207.239.33.54 || ip.dst eq 207.239.33.54 " -w final.cap</strong></p><p>But always encounter this type of error.<br />
<strong>tshark: invalid option -- 'Y'</strong></p><p>Running <strong>tshark -h</strong> does not show display filter option. I tried installing tshark 1.12 on my debian (Linux debian 3.2.0-4-amd64 #1 SMP Debian 3.2.68-1+deb7u1 x86_64 GNU/Linux) but no luck, a lot of dependencies are involved there.</p><p>How can i run the above command or install tshark 1.12 on my debian server?</p><p>Any help would be much appreciated. Thanks</p></div><div id="question-tags" class="tags-container tags">display-filter tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jul '15, 12:57</strong></p><img src="https://secure.gravatar.com/avatar/0fd6a9123c5686dec9ced8b314643a2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aqsyounas&#39;s gravatar image" /><p>aqsyounas<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aqsyounas has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-44603" class="comments-container"></div><div id="comment-tools-44603" class="comment-tools"></div><div class="clear"></div><div id="comment-44603-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44604"></span>

<div id="answer-container-44604" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44604-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The command you provided works on TShark 1.12.5</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jul '15, 13:12</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-44604" class="comments-container"><span id="44606"></span><div id="comment-44606" class="comment"><div id="post-44606-score" class="comment-score"></div><div class="comment-text"><p>Thanks for reply. So, any alternative command working in 1.8.2 giving above results?</p></div><div id="comment-44606-info" class="comment-info"><span class="comment-age">(29 Jul '15, 13:36)</span> aqsyounas</div></div><span id="44608"></span><div id="comment-44608" class="comment"><div id="post-44608-score" class="comment-score"></div><div class="comment-text"><p>Try to -R option = that is a capital R</p></div><div id="comment-44608-info" class="comment-info"><span class="comment-age">(29 Jul '15, 13:44)</span> Amato_C</div></div></div><div id="comment-tools-44604" class="comment-tools"></div><div class="clear"></div><div id="comment-44604-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

