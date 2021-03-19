+++
type = "question"
title = "Is it possible to add Wireshark to the Windows path during installation?"
description = '''I&#x27;d like to use Wireshark command line tools, such as tshark on Windows. In the command prompt, tshark can be only invoked if the Wireshark install directory is known or if it is added to the Windows path variables. Is there a way that when Wireshark is installed with the standard Windows installer,...'''
date = "2011-12-22T17:14:00Z"
lastmod = "2011-12-22T17:48:00Z"
weight = 8092
keywords = [ "windows", "installer", "command-line", "path" ]
aliases = [ "/questions/8092" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to add Wireshark to the Windows path during installation?](/questions/8092/is-it-possible-to-add-wireshark-to-the-windows-path-during-installation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8092-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'd like to use Wireshark command line tools, such as tshark on Windows. In the command prompt, tshark can be only invoked if the Wireshark install directory is known or if it is added to the Windows path variables.</p><p>Is there a way that when Wireshark is installed with the standard Windows installer, the install directory is automatically added to the Path variable, so that the command line tools can be used from the command prompt? i.e <strong>not manually added by the user, but automatically by the installer</strong></p></div><div id="question-tags" class="tags-container tags">windows installer command-line path</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '11, 17:14</strong></p><img src="https://secure.gravatar.com/avatar/d7c782bb984b130f22efa1bd122633da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tonio09&#39;s gravatar image" /><p>tonio09<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tonio09 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Dec '11, 17:49</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-8092" class="comments-container"></div><div id="comment-tools-8092" class="comment-tools"></div><div class="clear"></div><div id="comment-8092-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8094"></span>

<div id="answer-container-8094" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8094-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could do this yourself by modifying <code>packaging/nsis/wireshark.nsi</code> to include sections similar to those found on the <a href="http://nsis.sourceforge.net/Path_Manipulation" title="Path Manipulation">NSIS Wiki article on Path Manipulation</a>. However, you should keep in mind the <a href="http://nsis.sourceforge.net/Path_Manipulation#Warning" title="String Length Warning">warning</a> mentioned on the same page. You could probably get around this using the <a href="http://nsis.sourceforge.net/Special_Builds#Large_strings" title="Large Strings Build">Large Strings build</a>, but even this could fail for exceptionally long <code>PATH</code>s.</p><p>Ultimately, I don't think Wireshark will include this feature out of the box until and if the string length limitation of NSIS is fixed (and then someone has to update the installer script). By far, the easiest way to do this for now will be to do so manually after installation. If you do end up making such modifications to Wireshark, and they work with the regular version of NSIS without messing up the <code>PATH</code>, I would highly recommend <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSrcContribute.html" title="3.9. Contribute your changes">submitting</a> a patch to be included in Wireshark itself.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '11, 17:48</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-8094" class="comments-container"></div><div id="comment-tools-8094" class="comment-tools"></div><div class="clear"></div><div id="comment-8094-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

