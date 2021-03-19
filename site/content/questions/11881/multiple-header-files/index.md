+++
type = "question"
title = "Multiple Header Files"
description = '''I am working on a network-layer dissector for a prototypical protocol (that&#x27;s a mouthful) that is an alternative to IP; an eXpressive Internet Architecture. The addressing scheme for this protocol includes the use of DAGs, which require a few header files and a .c source file that defines various fu...'''
date = "2012-06-13T18:04:00Z"
lastmod = "2012-06-13T21:28:00Z"
weight = 11881
keywords = [ "header", "patch" ]
aliases = [ "/questions/11881" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Multiple Header Files](/questions/11881/multiple-header-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11881-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am working on a network-layer dissector for a prototypical protocol (that's a mouthful) that is an alternative to IP; an <a href="http://www.cs.cmu.edu/~xia/">eXpressive Internet Architecture</a>. The addressing scheme for this protocol includes the use of DAGs, which require a few header files and a .c source file that defines various functions for operating on the DAGs.</p><p>I would like to keep the header files intact and separate, rather than incorporating them all into packet-xip.c and packet-xip.h. This would make the dissector file cleaner and the headers easy to update as our research continues. Is there a preferred mechanism for including multiple header/source files? For example, a new directory in the epan directory seems like it would be a nice fit, but I am unsure if this would preclude the possibility of having a patch with our protocols approved in the future.</p><p>Thank you for any advice.</p></div><div id="question-tags" class="tags-container tags">header patch</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jun '12, 18:04</strong></p><img src="https://secure.gravatar.com/avatar/e247e0fb9b9f23b4f23793ef6811d476?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cody&#39;s gravatar image" /><p>Cody<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cody has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Jun '12, 18:05</p></div></div><div id="comments-container-11881" class="comments-container"></div><div id="comment-tools-11881" class="comment-tools"></div><div class="clear"></div><div id="comment-11881-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11885"></span>

<div id="answer-container-11885" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11885-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>See, for example, the dissector for the Zigbee protocol; there are several packet-zbee-XXX.[ch] files, or look at the XMPP dissector, which has a bunch of packet-xmpp-XXX.[ch] files. The best thing to do would be to have packet-xip.c and various packet-xip-*.c files, plus accompanying header files.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '12, 21:28</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Jun '12, 21:29</p></div></div><div id="comments-container-11885" class="comments-container"></div><div id="comment-tools-11885" class="comment-tools"></div><div class="clear"></div><div id="comment-11885-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

