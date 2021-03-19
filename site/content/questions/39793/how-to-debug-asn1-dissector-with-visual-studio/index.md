+++
type = "question"
title = "How to debug ASN.1 dissector with Visual Studio?"
description = '''I have a problem with decoding RRC TargetRNC-toSourceRNC-Container with an error exception showing up. I tried to debug but debugger randomly pops through packet-rrc-template.c and not the actual packet-rrc.c.  I removed /O2 from config.nmake and added /DEBUG to LOCAL_LDFLAGS but with no luck. I als...'''
date = "2015-02-11T05:14:00Z"
lastmod = "2015-02-11T06:17:00Z"
weight = 39793
keywords = [ "debug", "rrc" ]
aliases = [ "/questions/39793" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to debug ASN.1 dissector with Visual Studio?](/questions/39793/how-to-debug-asn1-dissector-with-visual-studio)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39793-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a problem with decoding RRC TargetRNC-toSourceRNC-Container with an error exception showing up. I tried to debug but debugger randomly pops through packet-rrc-template.c and not the actual packet-rrc.c.</p><p>I removed /O2 from config.nmake and added /DEBUG to LOCAL_LDFLAGS but with no luck. I also tried latest released both official and development, the problem presents there too. Is there any way to debug it after all?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/rrc.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">debug rrc</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '15, 05:14</strong></p><img src="https://secure.gravatar.com/avatar/4320b9b92552cf7634852b54c07462c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jsnk&#39;s gravatar image" /><p>jsnk<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jsnk has no accepted answers">0%</span></p></img></div></div><div id="comments-container-39793" class="comments-container"></div><div id="comment-tools-39793" class="comment-tools"></div><div class="clear"></div><div id="comment-39793-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39796"></span>

<div id="answer-container-39796" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39796-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sure, see the Developers Guide <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChToolsMSChain.html#ChToolsDebugger">Debugging Tools</a> section 4.6.8. What was the problem with using the debugger and which version of VS are you using?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '15, 06:17</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-39796" class="comments-container"><span id="39797"></span><div id="comment-39797" class="comment"><div id="post-39797-score" class="comment-score"></div><div class="comment-text"><p>RRC TargetRNC-toSourceRNC-Container is sometims filled with junk if you are using a traffic generator. I beleve there there is a preference to turn the dissection off.</p><p>Debuging asn2wrs generated files with the debugger can be a pain as the line numbers don't match you may have to set the breakpoints in the .cnf file or rerun asn2wrs with the -L option see <a href="http://wiki.wireshark.org/Asn2wrs">http://wiki.wireshark.org/Asn2wrs</a> or put debug statements in the code. or set breakpoints in packet-per.c possibly.</p></div><div id="comment-39797-info" class="comment-info"><span class="comment-age">(11 Feb '15, 07:06)</span> Anders ♦</div></div><span id="39799"></span><div id="comment-39799" class="comment"><div id="post-39799-score" class="comment-score"></div><div class="comment-text"><p>ISTR using the -L flag with asn2wrs (or removing the #line directives from the generated .c file using an editor) worked for me ...</p></div><div id="comment-39799-info" class="comment-info"><span class="comment-age">(11 Feb '15, 08:15)</span> Bill Meier ♦♦</div></div></div><div id="comment-tools-39796" class="comment-tools"></div><div class="clear"></div><div id="comment-39796-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

