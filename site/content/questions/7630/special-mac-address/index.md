+++
type = "question"
title = "Special MAC address"
description = '''Hey there, i came across an interesting MAC address related to a troubleshooting issue. There was a device using MAC address 19:02:16:08:vw:xy and i wonder where this address comes from. OUI has no info about 19:02:16 - so i googled for the string and found several forums etc. where people asked que...'''
date = "2011-11-25T05:09:00Z"
lastmod = "2011-11-25T18:10:00Z"
weight = 7630
keywords = [ "mac", "oui", "address" ]
aliases = [ "/questions/7630" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Special MAC address](/questions/7630/special-mac-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7630-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey there,</p><p>i came across an interesting MAC address related to a troubleshooting issue.</p><p>There was a device using MAC address 19:02:16:08:vw:xy and i wonder where this address comes from. OUI has no info about 19:02:16 - so i googled for the string and found several forums etc. where people asked questions about systems having those MAC addresses. The vendors are widely spread like linksys, dlink, siemens and so on, but all those had this special MAC plus (!) the next byte in all cases was "08"</p><p>So has anyone an idea, what those 19:02:16:08:xx:xx addresses could be?</p></div><div id="question-tags" class="tags-container tags">mac oui address</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '11, 05:09</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-7630" class="comments-container"></div><div id="comment-tools-7630" class="comment-tools"></div><div class="clear"></div><div id="comment-7630-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7637"></span>

<div id="answer-container-7637" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7637-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like a local IP address is being encoded in a locally assigned mac-address. This might be on purpose or it might be some malware that does this. If you say multiple devices do this... hmmm...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '11, 14:33</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-7637" class="comments-container"><span id="7646"></span><div id="comment-7646" class="comment"><div id="post-7646-score" class="comment-score"></div><div class="comment-text"><p>Great Idea - that could fit the scheme! Malware was also one of my thoughts, gotta go after that one</p></div><div id="comment-7646-info" class="comment-info"><span class="comment-age">(26 Nov '11, 05:01)</span> Landi</div></div></div><div id="comment-tools-7637" class="comment-tools"></div><div class="clear"></div><div id="comment-7637-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7642"></span>

<div id="answer-container-7642" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7642-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Reinstall your NIC driver - make sure you have the latest version.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '11, 18:10</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p>wesmorgan1<br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-7642" class="comments-container"></div><div id="comment-tools-7642" class="comment-tools"></div><div class="clear"></div><div id="comment-7642-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

