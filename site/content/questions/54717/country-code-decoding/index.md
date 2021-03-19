+++
type = "question"
title = "Country Code decoding"
description = '''Hi, when i view any trace via wire-shark, how wire shark identifying the country code from the calling or called party number ? Some of the country codes are two digits and some are three digits what is the logic to identify the country code out of the number ? Best Regards Anand.R'''
date = "2016-08-10T04:22:00Z"
lastmod = "2016-08-10T05:02:00Z"
weight = 54717
keywords = [ "countrycode" ]
aliases = [ "/questions/54717" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Country Code decoding](/questions/54717/country-code-decoding)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54717-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>when i view any trace via wire-shark, how wire shark identifying the country code from the calling or called party number ?</p><p>Some of the country codes are two digits and some are three digits what is the logic to identify the country code out of the number ?</p><p>Best Regards Anand.R</p></div><div id="question-tags" class="tags-container tags">countrycode</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Aug '16, 04:22</strong></p><img src="https://secure.gravatar.com/avatar/d78228e147cd39c8fd894a44aa8277bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AnandRoni&#39;s gravatar image" /><p>AnandRoni<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AnandRoni has no accepted answers">0%</span></p></div></div><div id="comments-container-54717" class="comments-container"></div><div id="comment-tools-54717" class="comment-tools"></div><div class="clear"></div><div id="comment-54717-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54718"></span>

<div id="answer-container-54718" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54718-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at dissect_e164_cc() in packet-e164.c <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-e164.c;h=00638ab5c72f3dd76971cb9f3fc8e865119e5554;hb=HEAD">https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-e164.c;h=00638ab5c72f3dd76971cb9f3fc8e865119e5554;hb=HEAD</a></p><p>But basically looking at the digits one by one. eg First digit == 1 CC Length =1.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '16, 05:02</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-54718" class="comments-container"></div><div id="comment-tools-54718" class="comment-tools"></div><div class="clear"></div><div id="comment-54718-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

