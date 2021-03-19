+++
type = "question"
title = "How do I read an *.xml file in wireshark?"
description = '''I&#x27;m trying to dissect FP over UDP, but this process needs some extra information. So, I added an *.xml to save the information, but I don&#x27;t know how to read an *.xml file in Wireshark. How can I accomplish this?'''
date = "2012-07-04T23:40:00Z"
lastmod = "2012-07-07T07:28:00Z"
weight = 12451
keywords = [ "xml" ]
aliases = [ "/questions/12451" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I read an \*.xml file in wireshark?](/questions/12451/how-do-i-read-an-xml-file-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12451-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to dissect FP over UDP, but this process needs some extra information. So, I added an *.xml to save the information, but I don't know how to read an *.xml file in Wireshark. How can I accomplish this?</p></div><div id="question-tags" class="tags-container tags">xml</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jul '12, 23:40</strong></p><img src="https://secure.gravatar.com/avatar/f6eeed42d5aadabfed2ca2cb1faabff1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smilezuzu&#39;s gravatar image" /><p>smilezuzu<br />
<span class="score" title="20 reputation points">20</span><span title="32 badges"><span class="badge1">●</span><span class="badgecount">32</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smilezuzu has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Jul '12, 22:29</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-12451" class="comments-container"></div><div id="comment-tools-12451" class="comment-tools"></div><div class="clear"></div><div id="comment-12451-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12498"></span>

<div id="answer-container-12498" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12498-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Look at packet-diameter.c and the related files in /epan. You should probably look at using preferences instead, possibly with an UAT table. Look for other source files using UAT:s (grep). Another posibillity is to create a heuristic FP dissector using the header CRC then create GUI code to fill in the missing information via some sort of "decode as" functionality.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jul '12, 07:28</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-12498" class="comments-container"></div><div id="comment-tools-12498" class="comment-tools"></div><div class="clear"></div><div id="comment-12498-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

