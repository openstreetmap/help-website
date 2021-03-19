+++
type = "question"
title = "nmake errors"
description = '''hi,i am new to wireshark trying to build a disssector.i&#x27;ve downloaded all the required tools-vs2010ee,pyton,cygwin,svntortoise.i am not able to download from trunk through svn in my company,though it worked in my home.so i just copy pastedinto c:&#92;wireshark.i am not able to verify the tools or instal...'''
date = "2013-03-12T02:53:00Z"
lastmod = "2013-03-12T04:54:00Z"
weight = 19378
keywords = [ "verify", "installation", "nmake", "tools", "build" ]
aliases = [ "/questions/19378" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [nmake errors](/questions/19378/nmake-errors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19378-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi,i am new to wireshark trying to build a disssector.i've downloaded all the required tools-vs2010ee,pyton,cygwin,svntortoise.i am not able to download from trunk through svn in my company,though it worked in my home.so i just copy pastedinto c:\wireshark.i am not able to verify the tools or install libraries using nmake. i am getting different errors at differnt times. 1)nmake not recognized as an internal or external command 2)nmake cannot make '-f' stop(checked with minus/hyphen solution,but in vain) 3)your moon-man"win32"architecture confuse us. 3)file'win32.mak'not found(on installing libraries). plz help asap..really urgent..thanks</p></div><div id="question-tags" class="tags-container tags">verify installation nmake tools build</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Mar '13, 02:53</strong></p><img src="https://secure.gravatar.com/avatar/afa04deca78e2ac8df31ecc4deea5bde?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ajain&#39;s gravatar image" /><p>ajain<br />
<span class="score" title="14 reputation points">14</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ajain has no accepted answers">0%</span></p></div></div><div id="comments-container-19378" class="comments-container"></div><div id="comment-tools-19378" class="comment-tools"></div><div class="clear"></div><div id="comment-19378-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19385"></span>

<div id="answer-container-19385" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19385-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It sounds as though your build environment isn't correct, you must follow the <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html">developers guide</a> to the letter, any skipping of steps is likely to cause failure.</p><p>Taking your reported issues in turn:</p><ol><li>nmake not recognised - You haven't prepared your command prompt to use the Visual Studio executables, see <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#ChSetupPrepareCommandCom">this</a> step.</li><li>nmake cannot make '-f' - The command you should use is <code>nmake -f Makefile.nmake</code> from the top level directory of the Wireshark source tree. You should verify your setup with <code>nmake -f Makefile.nmake verify_tools</code> as per <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html#ChToolsWin32Verify">this</a> step.</li><li>Very odd. The reported error is if the make variable <code>WIRESHARK_TARGET_PLATFORM</code> is not set to <code>win32</code> or <code>win64</code>.</li></ol><p>Just a thought, you are running from a cmd.exe prompt and not a cygwin one?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '13, 04:54</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-19385" class="comments-container"><span id="19426"></span><div id="comment-19426" class="comment"><div id="post-19426-score" class="comment-score"></div><div class="comment-text"><p>thanx..i had skipped windows sdk .but,i got another error which i asked as another question.</p></div><div id="comment-19426-info" class="comment-info"><span class="comment-age">(13 Mar '13, 01:16)</span> ajain</div></div></div><div id="comment-tools-19385" class="comment-tools"></div><div class="clear"></div><div id="comment-19385-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

