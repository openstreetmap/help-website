+++
type = "question"
title = "Where has makefile.nmake gone?"
description = '''Hi, With the current version 2.2.5, I do not see makefile.nmake. Older versions still has makefile.nmake.  I&#x27;m adding something similar to: randpkt.exe : $(randpkt_OBJECTS)  @echo Linking $@  $(LINK) @&amp;lt;&amp;lt;  /OUT:randpkt.exe $(conflags) $(conlibsdll) $(LDFLAGS) /SUBSYSTEM:console $(randpkt_LIBS) ...'''
date = "2017-04-04T20:35:00Z"
lastmod = "2017-04-04T23:39:00Z"
weight = 60574
keywords = [ "makefile.nmake" ]
aliases = [ "/questions/60574" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Where has makefile.nmake gone?](/questions/60574/where-has-makefilenmake-gone)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60574-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>With the current version 2.2.5, I do not see makefile.nmake. Older versions still has makefile.nmake.</p><p>I'm adding something similar to:</p><p>randpkt.exe : $(randpkt_OBJECTS) @echo Linking [email protected] $(LINK) @&lt;&lt; /OUT:randpkt.exe $(conflags) $(conlibsdll) $(LDFLAGS) /SUBSYSTEM:console $(randpkt_LIBS) $(randpkt_OBJECTS) &lt;&lt; !IFDEF MANIFEST_INFO_REQUIRED mt.exe -nologo -manifest "randpkt.exe.manifest" -outputresource:randpkt.exe;1 !ENDIF</p></div><div id="question-tags" class="tags-container tags">makefile.nmake</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Apr '17, 20:35</strong></p><img src="https://secure.gravatar.com/avatar/823bb3318e8675ca95342455cc07146e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="James%20Adriano&#39;s gravatar image" /><p>James Adriano<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="James Adriano has no accepted answers">0%</span></p></div></div><div id="comments-container-60574" class="comments-container"></div><div id="comment-tools-60574" class="comment-tools"></div><div class="clear"></div><div id="comment-60574-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60577"></span>

<div id="answer-container-60577" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60577-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Windows builds have moved to CMake and nmake isn't supported. Please read and follow the Developers Guide instructions as shown <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html">here</a>.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '17, 23:39</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></p></div></div><div id="comments-container-60577" class="comments-container"><span id="60581"></span><div id="comment-60581" class="comment"><div id="post-60581-score" class="comment-score"></div><div class="comment-text"><p>Ok, thanks for the information!</p></div><div id="comment-60581-info" class="comment-info"><span class="comment-age">(05 Apr '17, 00:43)</span> James Adriano</div></div></div><div id="comment-tools-60577" class="comment-tools"></div><div class="clear"></div><div id="comment-60577-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

