+++
type = "question"
title = "tshark shows unknown mactype 2147483653"
description = '''Dear support, we have installed wireshark successfully as a package from sunfreeware. Now we want to start tshark and we get the following message: Capturing on lo0 tshark: Can&#x27;t install filter (unknown mactype 2147483653). Please report this to the Wireshark developers. (This is not a crash; please...'''
date = "2013-07-29T00:04:00Z"
lastmod = "2013-07-29T01:14:00Z"
weight = 23418
keywords = [ "tshark" ]
aliases = [ "/questions/23418" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark shows unknown mactype 2147483653](/questions/23418/tshark-shows-unknown-mactype-2147483653)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23418-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear support,</p><p>we have installed wireshark successfully as a package from sunfreeware.</p><p>Now we want to start tshark and we get the following message:</p><p>Capturing on lo0 tshark: Can't install filter (unknown mactype 2147483653). Please report this to the Wireshark developers. (This is not a crash; please do not report it as such.) 0 packets captured</p><p>Out platform is sun4v ( T4-1 ).</p><p>Thanks in advance.</p><p>Kind Regards</p><p>Ronald</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jul '13, 00:04</strong></p><img src="https://secure.gravatar.com/avatar/d5e88276361775e47a480b40143aef07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rwijna&#39;s gravatar image" /><p>rwijna<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rwijna has no accepted answers">0%</span></p></div></div><div id="comments-container-23418" class="comments-container"><span id="23419"></span><div id="comment-23419" class="comment"><div id="post-23419-score" class="comment-score"></div><div class="comment-text"><p>Solaris 10, Solaris 11, or an earlier version?</p></div><div id="comment-23419-info" class="comment-info"><span class="comment-age">(29 Jul '13, 00:43)</span> Guy Harris ♦♦</div></div><span id="23420"></span><div id="comment-23420" class="comment"><div id="post-23420-score" class="comment-score"></div><div class="comment-text"><p>Solaris 10</p></div><div id="comment-23420-info" class="comment-info"><span class="comment-age">(29 Jul '13, 00:48)</span> rwijna</div></div></div><div id="comment-tools-23418" class="comment-tools"></div><div class="clear"></div><div id="comment-23418-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23421"></span>

<div id="answer-container-23421" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23421-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's <code>DL_IPNET</code>, which isn't supported by libpcap. You'd need to either 1) upgrade to Solaris 11 or 2) get DL_IPNET support added to the DLPI code in libpcap in order to capture on a loopback interface on Solaris.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jul '13, 01:14</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-23421" class="comments-container"></div><div id="comment-tools-23421" class="comment-tools"></div><div class="clear"></div><div id="comment-23421-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

