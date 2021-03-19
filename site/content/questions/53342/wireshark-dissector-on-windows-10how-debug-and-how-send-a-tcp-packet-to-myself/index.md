+++
type = "question"
title = "wireshark dissector on windows 10:how debug and how send a tcp packet to myself"
description = '''Hi, After building my solution with Visual Studio 2013 I have 3 questions:  I&#x27;d like to know how to debug my code: I&#x27;m not able via Visual Studio. How can I send to myself a TCP packet (with a specific port) in order to activate and debug my own dissector? I&#x27;m working on Windows. I don&#x27;t want to sel...'''
date = "2016-06-09T13:53:00Z"
lastmod = "2016-06-10T02:26:00Z"
weight = 53342
keywords = [ "debug", "dissector", "postdissector" ]
aliases = [ "/questions/53342" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark dissector on windows 10:how debug and how send a tcp packet to myself](/questions/53342/wireshark-dissector-on-windows-10how-debug-and-how-send-a-tcp-packet-to-myself)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53342-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, After building my solution with Visual Studio 2013 I have 3 questions:</p><ol><li>I'd like to know how to debug my code: I'm not able via Visual Studio.</li><li>How can I send to myself a TCP packet (with a specific port) in order to activate and debug my own dissector? I'm working on Windows.</li><li>I don't want to select a specific port on my dissector, I'd like to call my dissector for every port.</li></ol></div><div id="question-tags" class="tags-container tags">debug dissector postdissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '16, 13:53</strong></p><img src="https://secure.gravatar.com/avatar/39c90bff22b6fa58db657d5af50c7899?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kenhero&#39;s gravatar image" /><p>kenhero<br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kenhero has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jun '16, 14:50</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-53342" class="comments-container"></div><div id="comment-tools-53342" class="comment-tools"></div><div class="clear"></div><div id="comment-53342-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53343"></span>

<div id="answer-container-53343" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53343-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hopefully you're using a CMake build which generates a Visual Studio solution (Wireshark.sln) that you can open in VS. If you're still using nmake, stop now and change to CMake. Have you looked at the (sparse) <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChToolsMSChain.html#ChToolsDebugger">debugging section</a> in the developer's guide? Basically, it's standard Visual Studio debugging, nothing special for Wireshark.</p><p>For item 2, use any programming or scripting language or tool you have handy to open a tcp connection and send your required packet. For example, <a href="http://www.leeholmes.com/blog/2009/10/28/scripting-network-tcp-connections-in-powershell/">here's</a> a recipe using PowerShell. Google is your friend here.</p><p>For item 3, this requires a heuristic dissector, see doc\README.heuristic in the sources for more info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jun '16, 02:26</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-53343" class="comments-container"><span id="53345"></span><div id="comment-53345" class="comment"><div id="post-53345-score" class="comment-score"></div><div class="comment-text"><p>Hi Grahamb,</p><p>on MSVS 2013 if i start with Debug-&gt;start debugging this window appears</p><p><img src="https://osqa-ask.wireshark.org/upfiles/debugissue.png" alt="alt text" /></p><p>After clicking on "yes" the second window appears and blocked me.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/debugissue2.png" alt="alt text" /></p><p>Could you explain me briefly what it means and how to solve it? Btw i used : 1) cmake -DENABLE_CHM_GUIDES=on -G "Visual Studio 12 Win64" ..\wireshark</p><p>2)msbuild /m /p:Configuration=Debug Wireshark.sln</p></div><div id="comment-53345-info" class="comment-info"><span class="comment-age">(10 Jun '16, 02:58)</span> kenhero</div></div><span id="53347"></span><div id="comment-53347" class="comment"><div id="post-53347-score" class="comment-score"></div><div class="comment-text"><p>For point 2), you may prefer to draw your packet (or several packets) in hexadecimal, using a text editor, and use Wireshark's <code>File -&gt; Import from Hex Dump</code> capability. This way you can create any packet contents you like (including some malformed ones to check your dissector's handling of non-standard packets) and you don't need any additional software. You may use existing packets as a base, using <code>Copy -&gt; ... as Hex Dump</code> from the context menu (right click) on the Frame line in packet dissection pane first, pasting the result into the text editor, and editing the part of the packets which represents your protocol to be dissected.</p></div><div id="comment-53347-info" class="comment-info"><span class="comment-age">(10 Jun '16, 03:36)</span> sindy</div></div><span id="53348"></span><div id="comment-53348" class="comment"><div id="post-53348-score" class="comment-score"></div><div class="comment-text"><p>The out of date issue is due to some (unknown to me) discrepancy between an msbuild and a VS build, possibly due to timestamps. You can either ignore the error or rebuild the solution in Visual Studio.</p><p>The unable to start program issue is because you haven't set Wireshark to be the "start-up project to run when debugging. Right-click the "Wireshark" node in the project tree and click "Set as StartUp Project".</p></div><div id="comment-53348-info" class="comment-info"><span class="comment-age">(10 Jun '16, 03:42)</span> grahamb ♦</div></div></div><div id="comment-tools-53343" class="comment-tools"></div><div class="clear"></div><div id="comment-53343-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

