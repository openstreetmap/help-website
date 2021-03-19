+++
type = "question"
title = "Profinet dissector&#x27;s GSDML parser doesn&#x27;t seem to be ignoring HTML comments"
description = '''I am developing a Profinet IO device. Using Wireshark Version 2.2.2, which allows registering a folder or directory for GSDML files. I have noticed an interesting issue when using a preliminary GSDML for which I commented out some identification information of the devices IO modules, and then added ...'''
date = "2016-12-21T22:14:00Z"
lastmod = "2016-12-22T01:05:00Z"
weight = 58285
keywords = [ "parser", "gsdml", "profinet" ]
aliases = [ "/questions/58285" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Profinet dissector's GSDML parser doesn't seem to be ignoring HTML comments](/questions/58285/profinet-dissectors-gsdml-parser-doesnt-seem-to-be-ignoring-html-comments)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58285-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am developing a Profinet IO device. Using Wireshark Version 2.2.2, which allows registering a folder or directory for GSDML files. I have noticed an interesting issue when using a preliminary GSDML for which I commented out some identification information of the devices IO modules, and then added the specific information for the device under development. This GSDML file passes the syntax check from the Profibus International GSD Checker, as well as the syntax check of various PLC engineering tools, hence I have a reasonable degree of confidence on the GSDML file itself.</p><p>The interesting thing is that the captured Wireshark trace identifies the IO modules with the information which is supposed to be commented out in the HTML code, as opposed to the information on the valid GSDML code.</p><p>So my question is, may I be doing something wrong or is there a possibility that the GSDML parser in the Wireshark Profinet add-in is not handling the comments properly? I think it is well beyond my capability to develop a fix if the parser has a problem, so if I am right and somebody with higher skills would fix this issue, I would be extremely grateful.</p></div><div id="question-tags" class="tags-container tags">parser gsdml profinet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Dec '16, 22:14</strong></p><img src="https://secure.gravatar.com/avatar/0c254e108dbc164209ac04c8d9e51b96?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alfredo_Quintero&#39;s gravatar image" /><p>Alfredo_Quin...<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alfredo_Quintero has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jan '17, 03:39</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-58285" class="comments-container"><span id="58295"></span><div id="comment-58295" class="comment"><div id="post-58295-score" class="comment-score"></div><div class="comment-text"><p>Could you share us a trace at a public accessible place?</p></div><div id="comment-58295-info" class="comment-info"><span class="comment-age">(22 Dec '16, 01:14)</span> Christian_R</div></div></div><div id="comment-tools-58285" class="comment-tools"></div><div class="clear"></div><div id="comment-58285-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58291"></span>

<div id="answer-container-58291" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58291-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds like a bug, so please raise an entry on the Wireshark <a href="https://bugs.wireshark.org">bugzilla</a>, attaching a capture and GSDML file that exhibits the issue.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '16, 01:05</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-58291" class="comments-container"><span id="58572"></span><div id="comment-58572" class="comment"><div id="post-58572-score" class="comment-score"></div><div class="comment-text"><p>Hello. I have prepared the capture, the GSDML file and a screenshot with comments, which will make it a bit easier. Sorry it took a bit due to get it. Thanks for the follow-up.</p></div><div id="comment-58572-info" class="comment-info"><span class="comment-age">(06 Jan '17, 20:11)</span> Alfredo_Quin...</div></div><span id="58573"></span><div id="comment-58573" class="comment"><div id="post-58573-score" class="comment-score"></div><div class="comment-text"><p>Hello. I have posted my report. This is the first time I have done this so I hope I did it correctly and that this can be helpful. <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13303">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13303</a></p></div><div id="comment-58573-info" class="comment-info"><span class="comment-age">(06 Jan '17, 20:24)</span> Alfredo_Quin...</div></div><span id="58609"></span><div id="comment-58609" class="comment"><div id="post-58609-score" class="comment-score"></div><div class="comment-text"><p>A fix (that works at least for the files you provided) was committed by change <a href="https://code.wireshark.org/review/19593">19593</a>.</p><p>You should be able to pick up an automated build from <a href="https://www.wireshark.org/download/automated/">here</a> if you're running on one of the supported OS's, else you'll have to build it yourself from git.</p></div><div id="comment-58609-info" class="comment-info"><span class="comment-age">(09 Jan '17, 03:23)</span> grahamb ♦</div></div></div><div id="comment-tools-58291" class="comment-tools"></div><div class="clear"></div><div id="comment-58291-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

