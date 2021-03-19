+++
type = "question"
title = "Wireshark shows error message box while debugging in VS 2008"
description = '''I just downloaded the source zip of Wireshark 1.4.6, built it on Windows XP SP3, and tried starting it from the Visual Studio 2008 debugger. When Wireshark starts, I get this error message box: Child dumpcap process died: Exception 0xc0000135 This message box also appears when I try to open the &quot;Cap...'''
date = "2011-04-27T15:03:00Z"
lastmod = "2011-04-28T09:14:00Z"
weight = 3764
keywords = [ "windows", "debug", "exception", "dumpcap", "visual-studio" ]
aliases = [ "/questions/3764" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark shows error message box while debugging in VS 2008](/questions/3764/wireshark-shows-error-message-box-while-debugging-in-vs-2008)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3764-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3764-score" class="post-score" title="current number of votes">1</div><span id="post-3764-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just downloaded the source zip of Wireshark 1.4.6, built it on Windows XP SP3, and tried starting it from the Visual Studio 2008 debugger. When Wireshark starts, I get this error message box:</p><p><font><strong>Child dumpcap process died: Exception 0xc0000135</strong></font></p><p>This message box also appears when I try to open the "Capture Options" or "Interface List" dialog. From "Capture Options", the interface list only shows one entry: <code>\Device\NPF_{D0C748F9-7B75-453D-A585-0813AE3B8A13}</code></p><p>This problem does not occur if I start the executable itself (not via the VS debugger). It seems like some VS setting is not correct.</p><p><strong>How can I resolve this problem?</strong> Thanks.</p><p><font> P.S. I see that there have been similar problems without a [known] solution:</font></p><font> </font><ul><li>http://ask.wireshark.org/questions/2626/child-dumpcap-process-died-exception</li><li><font>http://ask.wireshark.org/questions/3443/child-capture-process-exited-exited-status-127 </font></li></ul></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-debug" rel="tag" title="see questions tagged &#39;debug&#39;">debug</span> <span class="post-tag tag-link-exception" rel="tag" title="see questions tagged &#39;exception&#39;">exception</span> <span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span> <span class="post-tag tag-link-visual-studio" rel="tag" title="see questions tagged &#39;visual-studio&#39;">visual-studio</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Apr '11, 15:03</strong></p><img src="https://secure.gravatar.com/avatar/aa651167cb1d51fa9dca1212f1123bfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bstn&#39;s gravatar image" /><p><span>bstn</span><br />
<span class="score" title="375 reputation points">375</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bstn has 4 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Apr '11, 17:50</strong> </span></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span></p></div></div><div id="comments-container-3764" class="comments-container"></div><div id="comment-tools-3764" class="comment-tools"></div><div class="clear"></div><div id="comment-3764-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3767"></span>

<div id="answer-container-3767" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3767-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3767-score" class="post-score" title="current number of votes">2</div><span id="post-3767-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bstn has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><strong>Found the problem:</strong> Exception 0xc0000135 is the Windows error code for "DLL not found".</p><p><strong>Solution:</strong> Edit project properties to add a reference path to the project's output directory (where the necessary DLLs are found)...</p><p>From Visual Studio 2008:</p><ol><li>Open menu <strong>Project &gt; Properties</strong></li><li>Expand tree node <strong>Common Properties &gt; Framework and References</strong></li><li>From <strong>Additional reference search paths</strong>, click the <strong>Add Path...</strong> button</li><li>Browse to project's output directory (e.g., <code>c:\sandbox\wireshark-1.4.6\wireshark-gtk2</code>)</li><li>Click <strong>OK</strong></li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '11, 15:59</strong></p><img src="https://secure.gravatar.com/avatar/aa651167cb1d51fa9dca1212f1123bfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bstn&#39;s gravatar image" /><p><span>bstn</span><br />
<span class="score" title="375 reputation points">375</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bstn has 4 accepted answers">14%</span></p></div></div><div id="comments-container-3767" class="comments-container"><span id="3769"></span><div id="comment-3769" class="comment"><div id="post-3769-score" class="comment-score">2</div><div class="comment-text"><p>An alternative:</p><p>To create the project/Solution. in VS, do File ! Open ! Project/Solution of the executable in the wireshark-gtk2 directory (rather than using the executable in the top-level directory).</p><p>That is:</p><p>....\wireshark-gtk2\wireshark.exe (or tshark.exe or ...)</p><p>if this is done, then there will be no need to set additional search paths.</p></div><div id="comment-3769-info" class="comment-info"><span class="comment-age">(27 Apr '11, 17:35)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="3789"></span><div id="comment-3789" class="comment"><div id="post-3789-score" class="comment-score"></div><div class="comment-text"><p>Ah, very cool. I had created a <em>Project From Existing Source</em> (before I had the binary) and used VS instead of the command line to build the binary. My method is somewhat painful because VS runs make before every debugging session. Doing it your way is much faster: exclusively use the command line to build and VS to debug. It would be great if someone updated the <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#id519914">Developer's Guide</a> to indicate these simple steps (there's currently a TODO comment for <strong>Debug Environment Setup</strong>).</p></div><div id="comment-3789-info" class="comment-info"><span class="comment-age">(28 Apr '11, 09:14)</span> <span class="comment-user userinfo">bstn</span></div></div></div><div id="comment-tools-3767" class="comment-tools"></div><div class="clear"></div><div id="comment-3767-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

