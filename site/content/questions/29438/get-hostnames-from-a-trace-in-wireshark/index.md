+++
type = "question"
title = "Get hostnames from a trace in wireshark"
description = '''Hi, I need to get all the hostnames from a trace that i opened using wireshark that it already have alot of data.Is there any filter that i can use in wireshark?  Otherwiese what should i do to get the hostnames ? Any help will be appreciated.'''
date = "2014-02-04T13:51:00Z"
lastmod = "2014-02-04T22:00:00Z"
weight = 29438
keywords = [ "filter", "hostname", "wireshark" ]
aliases = [ "/questions/29438" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Get hostnames from a trace in wireshark](/questions/29438/get-hostnames-from-a-trace-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29438-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I need to get all the hostnames from a trace that i opened using wireshark that it already have alot of data.Is there any filter that i can use in wireshark? Otherwiese what should i do to get the hostnames ? Any help will be appreciated.</p></div><div id="question-tags" class="tags-container tags">filter hostname wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '14, 13:51</strong></p><img src="https://secure.gravatar.com/avatar/d937f97d4465a534a269a0a3cbafae1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FalaG&#39;s gravatar image" /><p>FalaG<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FalaG has no accepted answers">0%</span></p></div></div><div id="comments-container-29438" class="comments-container"></div><div id="comment-tools-29438" class="comment-tools"></div><div class="clear"></div><div id="comment-29438-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29440"></span>

<div id="answer-container-29440" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29440-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are 'hostnames' in the capture file, like in the HTTP Host: header or in service banners, and there are ip addresses in the capture file (src/dst address) which you or Wireshark can resolve to names via DNS (works only if there is a DNS entry - PTR record - for the address). So, what exactly are you looking for?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '14, 22:00</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Feb '14, 22:11</p></div></div><div id="comments-container-29440" class="comments-container"></div><div id="comment-tools-29440" class="comment-tools"></div><div class="clear"></div><div id="comment-29440-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

