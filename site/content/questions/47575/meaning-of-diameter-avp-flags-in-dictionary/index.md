+++
type = "question"
title = "Meaning of Diameter AVP flags in dictionary"
description = '''Hi, I know what the M, V and P stand for and how they work. What I don&#x27;t quite understand is meaning of &quot;MUST&quot;, &quot;MUST NOT&quot;, &quot;SHOULD&quot;... There are only 2 possible values for each bit (0 and 1) but more then one value of MUST, MUST NOT... I&#x27;ve been googling quite a lot (unsuccessfully) to find the sol...'''
date = "2015-11-13T06:27:00Z"
lastmod = "2015-11-13T07:19:00Z"
weight = 47575
keywords = [ "dissection", "dictionary" ]
aliases = [ "/questions/47575" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Meaning of Diameter AVP flags in dictionary](/questions/47575/meaning-of-diameter-avp-flags-in-dictionary)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47575-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I know what the M, V and P stand for and how they work. What I don't quite understand is meaning of "MUST", "MUST NOT", "SHOULD"... There are only 2 possible values for each bit (0 and 1) but more then one value of MUST, MUST NOT... I've been googling quite a lot (unsuccessfully) to find the solution for setting these in the vendor specific dictionary I'm working on. In 3GPP specs, there's always a neat table with bits and their values. However, the spec for the VSA I'm working on, has only these values provided: <img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-6.png" alt="alt text" /></p><p>So, the question is, how should I set mandatory, vendot-bit, protected and encryption values in the dictionary? How does wireshark use these values when dissecting the packet?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">dissection dictionary</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Nov '15, 06:27</strong></p><img src="https://secure.gravatar.com/avatar/a03fa5b340afab78d2e44b63e8dcf3d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aliniel&#39;s gravatar image" /><p>Aliniel<br />
<span class="score" title="30 reputation points">30</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aliniel has 2 accepted answers">100%</span></p></img></div></div><div id="comments-container-47575" class="comments-container"></div><div id="comment-tools-47575" class="comment-tools"></div><div class="clear"></div><div id="comment-47575-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47576"></span>

<div id="answer-container-47576" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47576-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The MUST, MUST NOT, and SHOULD are telling you whether the bit should be set or not. The meanings of those key words come from <a href="https://www.ietf.org/rfc/rfc2119.txt">RFC 2119</a>. Basically: if some bit MUST be set then you really, really better set it to 1. If it SHOULD be set then you probably should set it to 1 but you don't have to (you won't risk interoperability by leaving it 0).</p><p>It appears that VzW doesn't use those terms but simply tells you what you MUST set the values to (M=0, V=1, P=0 in your example).</p><p>Wireshark doesn't currently do anything with the bit fields (e.g., <code>may-encrypt="no"</code>). I suppose it might in the future so it's probably Better to fill them in correctly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Nov '15, 07:19</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-47576" class="comments-container"><span id="47610"></span><div id="comment-47610" class="comment"><div id="post-47610-score" class="comment-score"></div><div class="comment-text"><p>Or, you SHOULD fill them in. :)</p></div><div id="comment-47610-info" class="comment-info"><span class="comment-age">(14 Nov '15, 14:34)</span> Quadratic</div></div></div><div id="comment-tools-47576" class="comment-tools"></div><div class="clear"></div><div id="comment-47576-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

