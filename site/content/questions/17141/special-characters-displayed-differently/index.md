+++
type = "question"
title = "Special characters displayed differently"
description = '''I am using Wireshark to capture traffic from an application we are testing. Currently the UN/PWD&#x27;s are transmitted via http. I can capture the username just fine. However, the the password contains the # which wireshark either omits to display or shows the % in place of the #.  The # is valid as the...'''
date = "2012-12-21T11:37:00Z"
lastmod = "2012-12-21T11:59:00Z"
weight = 17141
keywords = [ "password" ]
aliases = [ "/questions/17141" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Special characters displayed differently](/questions/17141/special-characters-displayed-differently)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17141-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using Wireshark to capture traffic from an application we are testing. Currently the UN/PWD's are transmitted via http. I can capture the username just fine. However, the the password contains the # which wireshark either omits to display or shows the % in place of the #.</p><p>The # is valid as the UN/PWD combination works.</p></div><div id="question-tags" class="tags-container tags">password</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Dec '12, 11:37</strong></p><img src="https://secure.gravatar.com/avatar/87c5b3c659418c48b1d30a0d37a1d032?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rojasj&#39;s gravatar image" /><p>rojasj<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rojasj has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Dec '12, 03:53</p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-17141" class="comments-container"></div><div id="comment-tools-17141" class="comment-tools"></div><div class="clear"></div><div id="comment-17141-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17142"></span>

<div id="answer-container-17142" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17142-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I bet the "%" sign is followed by 23, together that makes %23, which is the HTTP <a href="http://www.blooberry.com/indexdot/html/topics/urlencoding.htm">url encoding</a> string for the character "#".</p><p>In short, your browser translates "#" to "%23" to prevent interpretation problems between the client and the server. The server translates the "%23" back to "#". Wireshark just shows you the raw data as it is sent over the network.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Dec '12, 11:59</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-17142" class="comments-container"></div><div id="comment-tools-17142" class="comment-tools"></div><div class="clear"></div><div id="comment-17142-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

