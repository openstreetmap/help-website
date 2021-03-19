+++
type = "question"
title = "Error C2065: &#x27;off64_t&#x27; during the CMake build"
description = '''Hello everyone, I would like to build my own Wireshark from the source code 2.0.4 and I have followed all the step of the developer guide but unfortunately I have some errors during the compilation. I admit that I haven&#x27;t followed the steps with Git because my company use TortoiseSVN. Thank you in a...'''
date = "2016-06-14T01:21:00Z"
lastmod = "2016-06-14T10:47:00Z"
weight = 53429
keywords = [ "compile" ]
aliases = [ "/questions/53429" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Error C2065: 'off64\_t' during the CMake build](/questions/53429/error-c2065-off64_t-during-the-cmake-build)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53429-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone,</p><p>I would like to build my own Wireshark from the source code 2.0.4 and I have followed all the step of the developer guide but unfortunately I have some errors during the compilation.</p><p>I admit that I haven't followed the steps with Git because my company use TortoiseSVN. Thank you in advance for your answers</p><p>Here you can find my output from the command prompt:</p><p><a href="http://pastebin.com/ZmE1CMMh">http://pastebin.com/ZmE1CMMh</a></p></div><div id="question-tags" class="tags-container tags">compile</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jun '16, 01:21</strong></p><img src="https://secure.gravatar.com/avatar/1e089af1440cad240cf3e9651ec1b2fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stezerow&#39;s gravatar image" /><p>stezerow<br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stezerow has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Jun '16, 03:57</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-53429" class="comments-container"></div><div id="comment-tools-53429" class="comment-tools"></div><div class="clear"></div><div id="comment-53429-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53441"></span>

<div id="answer-container-53441" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53441-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I cannot see any error compilation in your pasted log: it simply shows that the cmake projects were successfully generated (MSVC does not support off64_t so the test program fails, which is OK).</p><p>What happens when you execute 'msbuild /m /p:Configuration=RelWithDebInfo Wireshark.sln'?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '16, 10:47</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-53441" class="comments-container"><span id="53452"></span><div id="comment-53452" class="comment"><div id="post-53452-score" class="comment-score"></div><div class="comment-text"><p>When I build Wireshark with the command msbuild "/m /p:Configuration=RelWithDebInfo Wireshark.sln" I have got 6 compilation errors:</p><p><a href="http://pastebin.com/7PN5q8wX">http://pastebin.com/7PN5q8wX</a></p></div><div id="comment-53452-info" class="comment-info"><span class="comment-age">(14 Jun '16, 23:34)</span> stezerow</div></div><span id="53453"></span><div id="comment-53453" class="comment"><div id="post-53453-score" class="comment-score">2</div><div class="comment-text"><blockquote><p>"PERL_EXECUTABLE-NOTFOUND" no se reconoce como un comando interno o externo, programa o archivo por lotes ejecutable.</p></blockquote><p>Step 2.2.5 "Install Cygwin" in <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html">section 2.2 "Win32/64: Step-by-Step Guide"</a> of the Wireshark Developer's Guide lists "Interpreters/perl" as one of the components of Cygwin that you must install. Did you install it?</p></div><div id="comment-53453-info" class="comment-info"><span class="comment-age">(15 Jun '16, 00:35)</span> Guy Harris ♦♦</div></div><span id="53457"></span><div id="comment-53457" class="comment"><div id="post-53457-score" class="comment-score"></div><div class="comment-text"><p>I have reinstalled Cygwin and all its components and it works! Thank you for your help</p><p>They said on the Cygwin website that antivirus can stop the installation procedure and I suppose that mine (OfficeScan which wasn't on their list) was the source of my trouble</p></div><div id="comment-53457-info" class="comment-info"><span class="comment-age">(15 Jun '16, 01:15)</span> stezerow</div></div></div><div id="comment-tools-53441" class="comment-tools"></div><div class="clear"></div><div id="comment-53441-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

