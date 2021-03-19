+++
type = "question"
title = "XML capture view translations on the &amp; ampersand"
description = '''Trying to capture an XML response sent to a customer that contains the ampersand. Customer is saying they are only getting the &amp;amp; and not the proper &amp;amp; xml required value. Need to prove was are sending the proper XML format for &amp;amp;.   Does Wireshark use XML to display the HTTP/XML data there...'''
date = "2015-05-29T12:35:00Z"
lastmod = "2015-05-29T15:49:00Z"
weight = 42751
keywords = [ "ampersand", "view" ]
aliases = [ "/questions/42751" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [XML capture view translations on the & ampersand](/questions/42751/xml-capture-view-translations-on-the-ampersand)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42751-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Trying to capture an XML response sent to a customer that contains the ampersand. Customer is saying they are only getting the &amp; and not the proper &amp; xml required value. Need to prove was are sending the proper XML format for &amp;.<br />
</p><p>Does Wireshark use XML to display the HTTP/XML data thereby changing a single &amp; ampersand to the &amp; format, or does the output provided by Wireshark reflect the true output packet?</p></div><div id="question-tags" class="tags-container tags">ampersand view</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 May '15, 12:35</strong></p><img src="https://secure.gravatar.com/avatar/bf51add4d7467d0d47898758baef36af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TALall&#39;s gravatar image" /><p>TALall<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TALall has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-42751" class="comments-container"></div><div id="comment-tools-42751" class="comment-tools"></div><div class="clear"></div><div id="comment-42751-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42753"></span>

<div id="answer-container-42753" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42753-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark shows the true output packet, it does not decode/visualize HTML/XML. Or, in other words, Wireshark will show you "&amp;" if there's just an ampersand. If there's "&amp;amp" it will show exactly "&amp;amp", and <strong>not</strong> the decoded "&amp;".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 May '15, 15:49</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-42753" class="comments-container"></div><div id="comment-tools-42753" class="comment-tools"></div><div class="clear"></div><div id="comment-42753-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

