+++
type = "question"
title = "How to run Wireshark on Linux to capture Web Service traffic?"
description = '''I have WebSphere installed on a server which is hosting a web service. We have to capture the packets of request and response of this web service.  So I am assuming if I install Wireshark on the server it will be able to capture incoming traffic and outgoing HTTP traffic of that web service.  I aske...'''
date = "2016-06-08T05:31:00Z"
lastmod = "2016-06-08T06:51:00Z"
weight = 53314
keywords = [ "rhel6" ]
aliases = [ "/questions/53314" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to run Wireshark on Linux to capture Web Service traffic?](/questions/53314/how-to-run-wireshark-on-linux-to-capture-web-service-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53314-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have WebSphere installed on a server which is hosting a web service. We have to capture the packets of request and response of this web service.</p><p>So I am assuming if I install Wireshark on the server it will be able to capture incoming traffic and outgoing HTTP traffic of that web service.</p><p>I asked Unix team to install Wireshark and here I can see the directories. But I don't know how to run it or which binary I need to execute.</p><p>I can see two directories created after its installation. <a href="http://i.stack.imgur.com/MEInB.png"><img src="http://i.stack.imgur.com/MEInB.png" alt="enter image description here" /></a></p><p><strong>How to run it?</strong></p></div><div id="question-tags" class="tags-container tags">rhel6</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '16, 05:31</strong></p><img src="https://secure.gravatar.com/avatar/7b747d2764678accdcb62440d708df0b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tahirakram&#39;s gravatar image" /><p>tahirakram<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tahirakram has no accepted answers">0%</span></p></img></div></div><div id="comments-container-53314" class="comments-container"></div><div id="comment-tools-53314" class="comment-tools"></div><div class="clear"></div><div id="comment-53314-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53317"></span>

<div id="answer-container-53317" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53317-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Normally the name of the binary file is called wireshark</p><p>When your system is missing X11 you can use the program tshark (CLI version of Wireshark). To start it simple use '$/path/to/bin/tshark -i interfacename'.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jun '16, 06:51</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p>Uli<br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-53317" class="comments-container"></div><div id="comment-tools-53317" class="comment-tools"></div><div class="clear"></div><div id="comment-53317-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

