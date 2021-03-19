+++
type = "question"
title = "Diameter IPAddress type convert"
description = '''Hello, I&#x27;m interrested by Diameter Protocol, specially by the way AVP of type IPAddress are encoded: Example: 10.50.54.38 will be (hex) 0a 32 36 26 and octetstring representation will be .26&amp;amp; I would like to know to to convert from xxxx.xxxx.xxxx.xxxx to the octetstring. (I know that the represe...'''
date = "2014-02-25T07:18:00Z"
lastmod = "2014-02-25T09:33:00Z"
weight = 30178
keywords = [ "diameter", "conversion", "ipaddress" ]
aliases = [ "/questions/30178" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Diameter IPAddress type convert](/questions/30178/diameter-ipaddress-type-convert)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30178-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm interrested by Diameter Protocol, specially by the way AVP of type IPAddress are encoded: Example: 10.50.54.38 will be (hex) 0a 32 36 26 and octetstring representation will be .26&amp; I would like to know to to convert from xxxx.xxxx.xxxx.xxxx to the octetstring. (I know that the representation must have 12 or 24 long length).</p><p>Thank for your share.</p></div><div id="question-tags" class="tags-container tags">diameter conversion ipaddress</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Feb '14, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/776accde8c4d99555d3c9ebd9e031007?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arkham&#39;s gravatar image" /><p>Arkham<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arkham has no accepted answers">0%</span></p></div></div><div id="comments-container-30178" class="comments-container"></div><div id="comment-tools-30178" class="comment-tools"></div><div class="clear"></div><div id="comment-30178-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30184"></span>

<div id="answer-container-30184" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30184-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The "octetstring" is just the binary values as displayed in ASCII, with a '.' period used when it's not a printable ASCII character. So the number 10 in the IP address is the hex byte 0x0a on the wire, and that's not a display-able ASCII character so it shows a period; whereas the number 50 is hex 0x32, which happens to be the ASCII character "2", 0x36 is "6", and 0x26 is "&amp;". But basically those octetstring displays are meaningless for binary data such as an IP Address.</p><p>I don't know what you mean by "12 or 24 length" - an IPv4 address is 4 octets big, which is 8 hex characters, or 4 "octetstring" characters; IPv6 is 16 octets, 32 hex chars, and 16 octetstring chars.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '14, 09:33</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-30184" class="comments-container"></div><div id="comment-tools-30184" class="comment-tools"></div><div class="clear"></div><div id="comment-30184-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

