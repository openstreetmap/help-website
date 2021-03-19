+++
type = "question"
title = "ldap simple bind"
description = '''When I look at an LDAP v3 bind request in the packet details pane under authentication: simple (0), I see simple: followed by a 20 digit number. What does this represent? Thanks'''
date = "2013-06-10T14:23:00Z"
lastmod = "2013-06-11T03:05:00Z"
weight = 21902
keywords = [ "malhenry", "ldap" ]
aliases = [ "/questions/21902" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [ldap simple bind](/questions/21902/ldap-simple-bind)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21902-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I look at an LDAP v3 bind request in the packet details pane under authentication: simple (0), I see simple: followed by a 20 digit number. What does this represent?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">malhenry ldap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jun '13, 14:23</strong></p><img src="https://secure.gravatar.com/avatar/ed4374aa147ed1279961c32dccfe9e85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="malhenry&#39;s gravatar image" /><p>malhenry<br />
<span class="score" title="21 reputation points">21</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="malhenry has no accepted answers">0%</span></p></div></div><div id="comments-container-21902" class="comments-container"><span id="21903"></span><div id="comment-21903" class="comment"><div id="post-21903-score" class="comment-score"></div><div class="comment-text"><p>I am referring to the 20 digit number.</p></div><div id="comment-21903-info" class="comment-info"><span class="comment-age">(10 Jun '13, 14:24)</span> malhenry</div></div></div><div id="comment-tools-21902" class="comment-tools"></div><div class="clear"></div><div id="comment-21902-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21909"></span>

<div id="answer-container-21909" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21909-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I see simple: followed by a 20 digit number.</p></blockquote><p>It's the password, ASCII encoded. You can see the 'decoded' password in the HEX view of the packet bytes.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '13, 03:05</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Jun '13, 03:06</p></div></div><div id="comments-container-21909" class="comments-container"><span id="21961"></span><div id="comment-21961" class="comment"><div id="post-21961-score" class="comment-score"></div><div class="comment-text"><p>Correct....good stuff. thanks.</p></div><div id="comment-21961-info" class="comment-info"><span class="comment-age">(12 Jun '13, 07:03)</span> malhenry</div></div></div><div id="comment-tools-21909" class="comment-tools"></div><div class="clear"></div><div id="comment-21909-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21904"></span>

<div id="answer-container-21904" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21904-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can probably find out from RFC 2251. In ASN1 it's defined as Simple ::= OCTET STRING and is probably an Authentication token.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jun '13, 21:08</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-21904" class="comments-container"><span id="21908"></span><div id="comment-21908" class="comment"><div id="post-21908-score" class="comment-score"></div><div class="comment-text"><p>Link to <a href="http://www.ietf.org/rfc/rfc2251.txt">RFC 2251 - Lightweight Directory Access Protocol (v3)</a></p></div><div id="comment-21908-info" class="comment-info"><span class="comment-age">(11 Jun '13, 02:01)</span> grahamb ♦</div></div></div><div id="comment-tools-21904" class="comment-tools"></div><div class="clear"></div><div id="comment-21904-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

