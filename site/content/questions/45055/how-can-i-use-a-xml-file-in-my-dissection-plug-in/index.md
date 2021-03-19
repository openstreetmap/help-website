+++
type = "question"
title = "How can I use a XML file in my dissection plug-in?"
description = '''Hi, I&#x27;m developing a plug-in for Wireshark and I have dissected headers and trailers that belongs to my protocol. Now I want to dissect the data part of the packages. For this part I have a XML file that represent a description of it. It will tell where in the data part I can find different variable...'''
date = "2015-08-13T05:50:00Z"
lastmod = "2015-08-13T07:40:00Z"
weight = 45055
keywords = [ "xml", "dissection", "plugin" ]
aliases = [ "/questions/45055" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How can I use a XML file in my dissection plug-in?](/questions/45055/how-can-i-use-a-xml-file-in-my-dissection-plug-in)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45055-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm developing a plug-in for Wireshark and I have dissected headers and trailers that belongs to my protocol. Now I want to dissect the data part of the packages. For this part I have a XML file that represent a description of it. It will tell where in the data part I can find different variables, their size in bits, their unit etc. So, I have some parts of the protocol that will never change (headers and trailers) and one part that might change (the data part described by the XML file). How can I be able to access the information in the XML file in my plug-in and use it for dissection of the data part?<br />
</p></div><div id="question-tags" class="tags-container tags">xml dissection plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Aug '15, 05:50</strong></p><img src="https://secure.gravatar.com/avatar/700fdbce0e12ea13d88d310e180269d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sof&#39;s gravatar image" /><p>Sof<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sof has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-45055" class="comments-container"></div><div id="comment-tools-45055" class="comment-tools"></div><div class="clear"></div><div id="comment-45055-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45061"></span>

<div id="answer-container-45061" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45061-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is currently no way to have dynamic dissection from any sort of configuration file, the colsest is asn2ws which can create C code from an ASN1 description with the aid of templates and configuration files. So you would have to write code from scratch to do that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '15, 07:40</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Aug '15, 07:40</p></div></div><div id="comments-container-45061" class="comments-container"><span id="45068"></span><div id="comment-45068" class="comment"><div id="post-45068-score" class="comment-score"></div><div class="comment-text"><p>Thanks for answering so quickly!</p></div><div id="comment-45068-info" class="comment-info"><span class="comment-age">(13 Aug '15, 11:57)</span> Sof</div></div></div><div id="comment-tools-45061" class="comment-tools"></div><div class="clear"></div><div id="comment-45061-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

