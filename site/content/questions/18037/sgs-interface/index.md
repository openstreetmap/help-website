+++
type = "question"
title = "SGS interface"
description = '''Hello, I&#x27;m trying to decode SG interface, but i can&#x27;t, I see that there is a correction to can do it, but i don&#x27;t know how can load. Please could you send me info? how can I load this correction or how can I decode SG interface? SG interface (MSS&amp;lt;---&amp;gt;MME) BR, Raúl'''
date = "2013-01-29T06:42:00Z"
lastmod = "2013-01-29T16:22:00Z"
weight = 18037
keywords = [ "sg_protocol" ]
aliases = [ "/questions/18037" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [SGS interface](/questions/18037/sgs-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18037-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm trying to decode SG interface, but i can't, I see that there is a correction to can do it, but i don't know how can load.</p><p>Please could you send me info? how can I load this correction or how can I decode SG interface?</p><p>SG interface (MSS&lt;---&gt;MME)</p><p>BR, Raúl</p></div><div id="question-tags" class="tags-container tags">sg_protocol</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '13, 06:42</strong></p><img src="https://secure.gravatar.com/avatar/dcab6aedd9e37a3ca8391eca8cc6856f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ratienz&#39;s gravatar image" /><p>ratienz<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ratienz has no accepted answers">0%</span></p></div></div><div id="comments-container-18037" class="comments-container"><span id="18038"></span><div id="comment-18038" class="comment"><div id="post-18038-score" class="comment-score"></div><div class="comment-text"><p>Which protocols(s) are used on that interface? what version of Wireshark do you have?</p></div><div id="comment-18038-info" class="comment-info"><span class="comment-age">(29 Jan '13, 06:56)</span> Anders ♦</div></div></div><div id="comment-tools-18037" class="comment-tools"></div><div class="clear"></div><div id="comment-18037-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18062"></span>

<div id="answer-container-18062" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18062-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The SGsAP dissector has the SCTP port hardwired to 29118; as it has no preferences, you can't change that.</p><p>However, if you have SGsAP traffic using a different SCTP port, you can select one of the packets that should be dissected as SGsAP, select Analyze -&gt; Decode As..., select "Transport" if it's not already selected in the dialog box that pops up, choose "Port", choose the proper port from the "option menu" item between "SCTP" and "as", and then choose SGSAP (yes, that's how it's capitalized in that list) from the list to the right of "as", and then click "OK".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '13, 16:22</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-18062" class="comments-container"><span id="18088"></span><div id="comment-18088" class="comment"><div id="post-18088-score" class="comment-score"></div><div class="comment-text"><p>Ok, very grateful. Thanks.</p></div><div id="comment-18088-info" class="comment-info"><span class="comment-age">(30 Jan '13, 03:19)</span> ratienz</div></div><span id="18116"></span><div id="comment-18116" class="comment"><div id="post-18116-score" class="comment-score"></div><div class="comment-text"><p>So are you using a specific SCTP port other then 29118? If so, perhaps there <em>should</em> be a port preference for the SGsAP dissector.</p></div><div id="comment-18116-info" class="comment-info"><span class="comment-age">(30 Jan '13, 10:58)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-18062" class="comment-tools"></div><div class="clear"></div><div id="comment-18062-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18039"></span>

<div id="answer-container-18039" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18039-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>An SGsAP dissector is available in Wireshark 1.8, if that's the protocol you are refering to.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '13, 07:00</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-18039" class="comments-container"><span id="18059"></span><div id="comment-18059" class="comment"><div id="post-18059-score" class="comment-score"></div><div class="comment-text"><p>Yes, correct, is the SGsAP protocol, but I've installed 1.8.5 and 1.8.0 and the protocol SGsAP doesn't apper in the protocols list inside the edit-&gt;Preferents.</p><p>am I searching in the correct menu?</p><p>Please, how can I see? where?</p></div><div id="comment-18059-info" class="comment-info"><span class="comment-age">(29 Jan '13, 16:07)</span> ratienz</div></div><span id="18060"></span><div id="comment-18060" class="comment"><div id="post-18060-score" class="comment-score"></div><div class="comment-text"><p>Not all protocols have preferences, so the protocols list in Edit -&gt; Preferences is <em>definitely</em> the wrong place to look to see what protocols are supported; there are a <em>LOT</em> of protocols that aren't in that list. SGsAP has no preferences, so it's one of the protocols not in the list.</p></div><div id="comment-18060-info" class="comment-info"><span class="comment-age">(29 Jan '13, 16:18)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-18039" class="comment-tools"></div><div class="clear"></div><div id="comment-18039-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

