+++
type = "question"
title = "Wireshark build on Visual studio 2010"
description = '''I am getting compile time error when I am trying to compile the Windows source build in the Visual studio 2010. Error 1 error U1065: invalid option &#x27;-&#x27; C:&#92;Wireshark&#92;NMAKE wireshark Error 2 error MSB3073: The command &quot;nmake -f Makefile.nmake distclean&quot; exited with code 2. C:&#92;Program Files&#92;MSBuild&#92;Mic...'''
date = "2012-03-12T10:01:00Z"
lastmod = "2012-03-12T17:44:00Z"
weight = 9493
keywords = [ "2010", "visual-studio" ]
aliases = [ "/questions/9493" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark build on Visual studio 2010](/questions/9493/wireshark-build-on-visual-studio-2010)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9493-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am getting compile time error when I am trying to compile the Windows source build in the Visual studio 2010.</p><p>Error 1 error U1065: invalid option '-' C:\Wireshark\NMAKE wireshark Error 2 error MSB3073: The command "nmake -f Makefile.nmake distclean" exited with code 2. C:\Program Files\MSBuild\Microsoft.Cpp\v4.0\Microsoft.MakeFile.Targets 33 6 wireshark</p></div><div id="question-tags" class="tags-container tags">2010 visual-studio</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Mar '12, 10:01</strong></p><img src="https://secure.gravatar.com/avatar/bab04ba0cbde9ec0f486a7866e9d3932?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Krishna&#39;s gravatar image" /><p>Krishna<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Krishna has no accepted answers">0%</span></p></div></div><div id="comments-container-9493" class="comments-container"><span id="9494"></span><div id="comment-9494" class="comment"><div id="post-9494-score" class="comment-score"></div><div class="comment-text"><p>This type of question is better asked on the [email protected]<a href="http://wireshark.org">wireshark.org</a> mailing list.</p><p>Did you follow exactly the instructions in the <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html">Wireshark Developer's Guide</a> ?</p><p>In any case, to maybe get an idea of what's happening, we'll need to start with a file showing the complete output from</p><pre><code>nmake -f Makefile.nmake verify_tools
nmake -f Makefile.nmake distclean</code></pre></div><div id="comment-9494-info" class="comment-info"><span class="comment-age">(12 Mar '12, 10:24)</span> Bill Meier ♦♦</div></div></div><div id="comment-tools-9493" class="comment-tools"></div><div class="clear"></div><div id="comment-9493-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9502"></span>

<div id="answer-container-9502" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9502-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Do you have <code>MAKEFLAGS</code> set in your environment?</p><p>A couple of references to others who had this same problem, albeit not specifically with Wireshark:</p><ul><li><a href="http://stackoverflow.com/questions/1975240/nmake-exe-keeps-complaining-about-flags-im-not-giving-it-u1065">http://stackoverflow.com/questions/1975240/nmake-exe-keeps-complaining-about-flags-im-not-giving-it-u1065</a></li><li><a href="http://www-01.ibm.com/support/docview.wss?uid=swg21323645">http://www-01.ibm.com/support/docview.wss?uid=swg21323645</a></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '12, 17:44</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-9502" class="comments-container"></div><div id="comment-tools-9502" class="comment-tools"></div><div class="clear"></div><div id="comment-9502-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

