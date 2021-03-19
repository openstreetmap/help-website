+++
type = "question"
title = "How should I register a subtree type when I can&#x27;t predetermine the number of types of subtree?"
description = '''Hi, folks, sorry for the probably confusing title. I&#x27;m dissecting a packet that consists of TLV(type, length, value) units. each TLV unit is composed of three parts, a type field, length field, and a value field of variable length as specified in length field. The value field may contain primitive d...'''
date = "2017-07-25T22:44:00Z"
lastmod = "2017-07-26T06:58:00Z"
weight = 63108
keywords = [ "register", "subdissector", "subtree" ]
aliases = [ "/questions/63108" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How should I register a subtree type when I can't predetermine the number of types of subtree?](/questions/63108/how-should-i-register-a-subtree-type-when-i-cant-predetermine-the-number-of-types-of-subtree)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63108-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, folks, sorry for the probably confusing title.</p><p>I'm dissecting a packet that consists of TLV(type, length, value) units. each TLV unit is composed of three parts, a type field, length field, and a value field of variable length as specified in length field. The value field may contain primitive data or another TLV unit, and so on so forth.</p><p>As I understand, I need to maintain one distinct integer to register for every type of subtree that I have(which I later pass to proto_item_add_subtree()).And since these types need to be registered in register_dissector(), I have to predetermine the number of subtree types that I would need. Different subtrees can share same type, and they would be expanded/folded simultaneously. For my purpose, I think I need more than one type because I don't want users to expand a huge tree everytime they try to view one TLV unit. I would need one type, at least for every level subtree in the hierarchy. Since I can't predetermined the how deep the hierarchy would be, I'm stuck. Of course I could make an array that's supposedly large enough (say 16), but that doesn't seem to be a proper and efficient way.</p><p>Maybe I have some misunderstanding, what is the proper way to handle this?</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags">register subdissector subtree</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jul '17, 22:44</strong></p><img src="https://secure.gravatar.com/avatar/4222adcf6d70b2c359746d893f30c045?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nickzhang&#39;s gravatar image" /><p>nickzhang<br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nickzhang has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Jul '17, 22:58</p></div></div><div id="comments-container-63108" class="comments-container"></div><div id="comment-tools-63108" class="comment-tools"></div><div class="clear"></div><div id="comment-63108-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="63109"></span>

<div id="answer-container-63109" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63109-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There's a slight misunderstanding I guess. Subtrees come of tree items, where tree items are the node you create while parsing your packet. proto_tree_add_item() returns such a tree item. Have a look at other dissectors that use these calls. Oh, and you can use a subtree registration multiple times.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jul '17, 22:59</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-63109" class="comments-container"></div><div id="comment-tools-63109" class="comment-tools"></div><div class="clear"></div><div id="comment-63109-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="63133"></span>

<div id="answer-container-63133" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63133-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are a number of TLV-based protocol dissectors out there, you might want to take a look at how some of them do it.</p><p>One example that comes to mind is the Diameter dissector. It reads the possible tags from XML files and generates an ett_ value for every grouped AVP (an TLV whose value is one or more TLVs). That way if the user expands, say, the subtree that contains AVP (TLV) X then all instances of X will be expanded but instances of all other AVPs (TLVs) would not.</p><p>Presuming that you know which TLVs can contain other TLVs that's probably a reasonable way to go.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '17, 06:58</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-63133" class="comments-container"></div><div id="comment-tools-63133" class="comment-tools"></div><div class="clear"></div><div id="comment-63133-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

