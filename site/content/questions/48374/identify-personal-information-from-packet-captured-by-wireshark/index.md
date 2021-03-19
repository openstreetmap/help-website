+++
type = "question"
title = "Identify Personal information from packet captured by Wireshark"
description = '''Hi Sorry for my poor english. I am using wireshark as a tool to investigate network problems. Is it possible that the packet captured by Wireshark may contain Personal information? If the packet contain Personal information,are they encrypted? Is these a possibility that these information got identi...'''
date = "2015-12-09T01:38:00Z"
lastmod = "2015-12-09T03:09:00Z"
weight = 48374
keywords = [ "wireshark" ]
aliases = [ "/questions/48374" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Identify Personal information from packet captured by Wireshark](/questions/48374/identify-personal-information-from-packet-captured-by-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48374-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>Sorry for my poor english.</p><p>I am using wireshark as a tool to investigate network problems. Is it possible that the packet captured by Wireshark may contain Personal information? If the packet contain Personal information,are they encrypted? Is these a possibility that these information got identified?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Dec '15, 01:38</strong></p><img src="https://secure.gravatar.com/avatar/3ce66a3b341a2e2a9307962052af4a67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="udtren&#39;s gravatar image" /><p>udtren<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="udtren has no accepted answers">0%</span></p></div></div><div id="comments-container-48374" class="comments-container"></div><div id="comment-tools-48374" class="comment-tools"></div><div class="clear"></div><div id="comment-48374-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48375"></span>

<div id="answer-container-48375" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48375-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is a tool for analysing network traffic and identifying eventual problems. Its intention and purpose is to display anything what happens on the network as anything may be important for the analysis and solution.</p><p>So yes, if the personal (or in other way sensitive) information is transported over the network without encryption, Wireshark will display it, just like any other tool you would use to sniff network traffic, so declaring Wireshark illegal would not help you protect that information from unauthorized access.</p><p>Even if the information is encrypted and the analyst receives the necessary keys from the person who has access to these keys, in many cases Wireshark is able to decrypt that information into its original form. In other cases, the encryption method is not publicly known so Wireshark is unable to decrypt such communication even if the keys or passwords are available.</p><p>Whether a given packet is encrypted or not does not depend on Wireshark but on the application which has sent the packet.</p><p>If you are asking because you have a Wireshark capture file which you would like to share with someone to help you analyse it and understand what happens there, there are tools allowing you to strip the informational contents beyond the protocol headers (so the analysis of protocol issues is still possible but the application information transported by that protocols is removed from the capture). It is also possible to replace each individual address in the capture by another one, making equipment identification impossible. Search the internet for the TraceWrangler tool, which can do far more than that but capture anonymization is one of its popular features.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Dec '15, 03:09</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Dec '15, 03:21</p></div></div><div id="comments-container-48375" class="comments-container"><span id="48377"></span><div id="comment-48377" class="comment"><div id="post-48377-score" class="comment-score"></div><div class="comment-text"><p>I think i got it. Thank you for answering.</p></div><div id="comment-48377-info" class="comment-info"><span class="comment-age">(09 Dec '15, 04:46)</span> udtren</div></div></div><div id="comment-tools-48375" class="comment-tools"></div><div class="clear"></div><div id="comment-48375-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

