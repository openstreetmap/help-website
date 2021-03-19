+++
type = "question"
title = "how to load 3rd party module into my lua script"
description = '''Hello, I am beginning Lua scripting in general and for Wireshark dissectors in specific. I am trying to write a basic script that reads an xml file that contains some values of fields in my packets. For this I require two modules(LuaXml and Bit), Bit is for some binary operations. I would like to kn...'''
date = "2015-04-09T02:20:00Z"
lastmod = "2015-04-09T04:28:00Z"
weight = 41314
keywords = [ "lua", "modules", "3rd", "party" ]
aliases = [ "/questions/41314" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to load 3rd party module into my lua script](/questions/41314/how-to-load-3rd-party-module-into-my-lua-script)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41314-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am beginning Lua scripting in general and for Wireshark dissectors in specific. I am trying to write a basic script that reads an xml file that contains some values of fields in my packets. For this I require two modules(LuaXml and Bit), Bit is for some binary operations. I would like to know how to use these modules with Wireshark? I tried to use the LuaForWindows tool but it supports Lua 5.1 and my Wireshark version comes with Lua5.2 I tried to copy the dll file for LuaXml(downloaded directly from their website) to my Wireshark directory and it seems to work fine. But for the Bit module, I had to build the dll file myself using MSVC10 but then Wireshark crashes without any error(the typical Windows crash). I would like to know the proper way of integrating 3rd party modules into my Wireshark script.</p><p>Thanks a lot in advance</p></div><div id="question-tags" class="tags-container tags">lua modules 3rd party</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Apr '15, 02:20</strong></p><img src="https://secure.gravatar.com/avatar/6a8427ead4bf3634030701b9ba9940af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amine%20Ahd&#39;s gravatar image" /><p>Amine Ahd<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amine Ahd has one accepted answer">33%</span></p></div></div><div id="comments-container-41314" class="comments-container"></div><div id="comment-tools-41314" class="comment-tools"></div><div class="clear"></div><div id="comment-41314-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41318"></span>

<div id="answer-container-41318" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41318-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I found another alternative that might help anyone in the future. instead of using a C library, I have found <a href="http://www.dialectronics.com/Lua/">a pure Lua</a> library that solved my problem. I had just to copy the .lua files inside the lua/ directory in Wireshark and require the library in my script.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Apr '15, 04:28</strong></p><img src="https://secure.gravatar.com/avatar/6a8427ead4bf3634030701b9ba9940af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amine%20Ahd&#39;s gravatar image" /><p>Amine Ahd<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amine Ahd has one accepted answer">33%</span></p></div></div><div id="comments-container-41318" class="comments-container"><span id="41372"></span><div id="comment-41372" class="comment"><div id="post-41372-score" class="comment-score"></div><div class="comment-text"><p>If suppose the information in xml file i want to validate using xsd schema then is there any possibility in lua to validate xml file or xsd schema. means Is lua provies any kind of API which validate xsd scema???</p></div><div id="comment-41372-info" class="comment-info"><span class="comment-age">(10 Apr '15, 22:59)</span> ankit</div></div></div><div id="comment-tools-41318" class="comment-tools"></div><div class="clear"></div><div id="comment-41318-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

