+++
type = "question"
title = "Debugging Wireshark dissector in Visual Studio 2013"
description = '''According to the Howto here I can just open the Wireshark.exe and debug it in VisualStudio, but the debugging option is greyed out. Can anyone help me?'''
date = "2014-10-15T07:38:00Z"
lastmod = "2014-10-16T04:38:00Z"
weight = 37065
keywords = [ "debugging", "visual-studio" ]
aliases = [ "/questions/37065" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Debugging Wireshark dissector in Visual Studio 2013](/questions/37065/debugging-wireshark-dissector-in-visual-studio-2013)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37065-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37065-score" class="post-score" title="current number of votes">0</div><span id="post-37065-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>According to the Howto <a href="https://ask.wireshark.org/questions/8660/wireshark-building-and-debugging-on-visual-c-or-visual-studio">here</a> I can just open the Wireshark.exe and debug it in VisualStudio,<br />
but the debugging option is greyed out.<br />
Can anyone help me?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-debugging" rel="tag" title="see questions tagged &#39;debugging&#39;">debugging</span> <span class="post-tag tag-link-visual-studio" rel="tag" title="see questions tagged &#39;visual-studio&#39;">visual-studio</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Oct '14, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/cc56ba9bd225bd68cea09a404ecc0b6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lal12&#39;s gravatar image" /><p><span>lal12</span><br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lal12 has 2 accepted answers">33%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Oct '14, 08:54</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-37065" class="comments-container"><span id="37094"></span><div id="comment-37094" class="comment"><div id="post-37094-score" class="comment-score"></div><div class="comment-text"><p>Now I found a way:</p><ul><li>Compiled wireshark on the usual way.</li><li>Started the "wireshark-gtk2\Wireshark.exe".</li><li>Opened the source file I wanted to debug.</li><li>Now I clicked on the "Anhängen" option (in english maybe someting like ~"Append to process").</li><li>Then I choose the wireshark.exe from the process list and confirmed.</li><li>Now it was possible to debug mostly as I was already used it from Visual Studio.</li></ul><p><strong>But some bugs seems to occure:</strong><br />
- If you set an breakpoint to an "if" or "switch" you cannot see the value of compared variables, also this is not possible in the if/switch block itself. But it works if you set the breakpoint at least one step before the if or switch command.<br />
- I am note sure, but I think sometimes the "Einzelschritt" (~"go one step") does not work, it seems that it jumps several steps.</p></div><div id="comment-37094-info" class="comment-info"><span class="comment-age">(16 Oct '14, 01:01)</span> <span class="comment-user userinfo">lal12</span></div></div><span id="37096"></span><div id="comment-37096" class="comment"><div id="post-37096-score" class="comment-score">1</div><div class="comment-text"><p>Ensure to compile Wireshark without optimization. Edit config.nmake and remove the /O2 flag from LOCAL_CFLAGS. Then clean the objects and recompile.</p></div><div id="comment-37096-info" class="comment-info"><span class="comment-age">(16 Oct '14, 02:50)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-37065" class="comment-tools"></div><div class="clear"></div><div id="comment-37065-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37074"></span>

<div id="answer-container-37074" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37074-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37074-score" class="post-score" title="current number of votes">0</div><span id="post-37074-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="lal12 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Works for me with VS 2013 Pro</p><ul><li>Start Visual Studio.</li><li>From the File | Open | Project/Solution ... menu, open the wireshark executable in <code>yourbuilddir\wireshark-gtk\Wireshark-gtk.exe</code> or <code>yourbuilddir\wireshark-qt-release\Wireshark.exe</code></li><li>F5 or Debug | Start Debugging</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Oct '14, 09:00</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></br></p></div></div><div id="comments-container-37074" class="comments-container"><span id="37093"></span><div id="comment-37093" class="comment"><div id="post-37093-score" class="comment-score"></div><div class="comment-text"><p>Well, it does not work for me. I also have VS 2013 Pro installed, but when I open the file the only available option in the debug menu is "An den Prozess anhängen" (~"concat on the process", probably wrong translated).<br />
It is a german installation, so I do not know how it is called in english, but maybe you see what I mean in the picture below.<br />
I tried all combinations of calling the "SetEnv.cmd" (Debug x86, Debug x64, Release x86, Release x64),<br />
but it is the same every case.<br />
</p><p><img src="https://osqa-ask.wireshark.org/upfiles/vs13pro_wireshark-debug.PNG" alt="alt text" /></p></div><div id="comment-37093-info" class="comment-info"><span class="comment-age">(16 Oct '14, 00:05)</span> <span class="comment-user userinfo">lal12</span></div></div><span id="37098"></span><div id="comment-37098" class="comment"><div id="post-37098-score" class="comment-score"></div><div class="comment-text"><p>You haven't followed the instructions properly, you have opened Wireshark.exe as a "File", e.g. the following menu op; File | Open | File, or "Ctrl + O", probably not helped by my instructions being in English and your VS running in German.</p><p>Reread the instructions above or use the "Ctrl + Shift + O" shortcut.</p></div><div id="comment-37098-info" class="comment-info"><span class="comment-age">(16 Oct '14, 03:55)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="37099"></span><div id="comment-37099" class="comment"><div id="post-37099-score" class="comment-score">1</div><div class="comment-text"><p>An image of the required operation:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wireshark-debug.png" alt="alt text" /></p></div><div id="comment-37099-info" class="comment-info"><span class="comment-age">(16 Oct '14, 03:57)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="37101"></span><div id="comment-37101" class="comment"><div id="post-37101-score" class="comment-score"></div><div class="comment-text"><p>Ok thx, I found that by myself after a while. But removing the O2 flag helped.</p></div><div id="comment-37101-info" class="comment-info"><span class="comment-age">(16 Oct '14, 04:31)</span> <span class="comment-user userinfo">lal12</span></div></div><span id="37102"></span><div id="comment-37102" class="comment"><div id="post-37102-score" class="comment-score"></div><div class="comment-text"><p>Actually debugging optimised code is a separate question I think.</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-37102-info" class="comment-info"><span class="comment-age">(16 Oct '14, 04:38)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-37074" class="comment-tools"></div><div class="clear"></div><div id="comment-37074-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

