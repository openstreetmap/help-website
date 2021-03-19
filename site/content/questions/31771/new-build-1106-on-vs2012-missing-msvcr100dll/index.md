+++
type = "question"
title = "New build 1.10.6 on VS2012 - missing msvcr100.dll"
description = '''Hi guys I&#x27;ve been building Wireshark on VS2012 for a while now, but my most recent builds report MSVCR100.dll missing (even though the redist successfully installs - and it includes MSVCR110.dll) Not sure why it&#x27;s looking for the older version, do you think it might be WinPCap requiring this DLL, in...'''
date = "2014-04-13T17:00:00Z"
lastmod = "2015-01-21T22:01:00Z"
weight = 31771
keywords = [ "development", "64-bit" ]
aliases = [ "/questions/31771" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [New build 1.10.6 on VS2012 - missing msvcr100.dll](/questions/31771/new-build-1106-on-vs2012-missing-msvcr100dll)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31771-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys I've been building Wireshark on VS2012 for a while now, but my most recent builds report MSVCR100.dll missing (even though the redist successfully installs - and it includes MSVCR110.dll) Not sure why it's looking for the older version, do you think it might be WinPCap requiring this DLL, in which case what's the solution?</p><p>The 32-bit version installs and runs without any issue - this fault only appears to affect the 64-bit build</p><p>Will attach a screenshot shortly</p><p>Cheers</p></div><div id="question-tags" class="tags-container tags">development 64-bit</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Apr '14, 17:00</strong></p><img src="https://secure.gravatar.com/avatar/c4a59238ef906285e110fa429a9a94b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Scott%20Harman&#39;s gravatar image" /><p>Scott Harman<br />
<span class="score" title="46 reputation points">46</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Scott Harman has one accepted answer">50%</span></p></div></div><div id="comments-container-31771" class="comments-container"></div><div id="comment-tools-31771" class="comment-tools"></div><div class="clear"></div><div id="comment-31771-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="31807"></span>

<div id="answer-container-31807" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31807-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Simply install the <a href="http://www.microsoft.com/en-us/download/details.aspx?id=13523">MSVC2010 redistributable for x64</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Apr '14, 14:49</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-31807" class="comments-container"><span id="31808"></span><div id="comment-31808" class="comment"><div id="post-31808-score" class="comment-score"></div><div class="comment-text"><p>Why doesn't the 32-bit build require it then. It should require MSVC2012, not 2010 - we want to have a one-shot install on any of our 2008 or Win7 64-bit systems</p></div><div id="comment-31808-info" class="comment-info"><span class="comment-age">(14 Apr '14, 14:53)</span> Scott Harman</div></div><span id="31849"></span><div id="comment-31849" class="comment"><div id="post-31849-score" class="comment-score"></div><div class="comment-text"><p>Because your 32-bit system already has the x86 MSVC 2010 redistributable installed? Wireshark relies on third party libraries (the ones that get downloaded in wireshark-win64-libs folder) and at least one of them must be built with MSVC2010. If you really want a one-shot install, you should build Wireshark with MSVC2010 instead of MSVC2012 (like the official release). This way the MSVC2010 redistributable will be installed during the installation process.</p></div><div id="comment-31849-info" class="comment-info"><span class="comment-age">(15 Apr '14, 13:54)</span> Pascal Quantin</div></div><span id="31852"></span><div id="comment-31852" class="comment"><div id="post-31852-score" class="comment-score"></div><div class="comment-text"><p>Hi Pascal - I've checked, and it doesn't - the 32-bit installer installs the 32-bit version of msvc2012</p></div><div id="comment-31852-info" class="comment-info"><span class="comment-age">(15 Apr '14, 14:17)</span> Scott Harman</div></div><span id="31854"></span><div id="comment-31854" class="comment"><div id="post-31854-score" class="comment-score"></div><div class="comment-text"><p>Yes each installer installs the MSVC redistributable used to compile Wireshark, but you still have dependencies for the pre built 3rd party libraries as I explained earlier. If you open Wireshark with Dependency Walker, you will see which DLL depends on MSC2010. For example with my 1.11.3 build, it is required for lua52.dll. The easiest way to solve your problem, is either to manually recompile the DLL having this dependency, or simply build Wireshark with MSVC2010 instead of MSVC2012.</p></div><div id="comment-31854-info" class="comment-info"><span class="comment-age">(15 Apr '14, 15:09)</span> Pascal Quantin</div></div><span id="31857"></span><div id="comment-31857" class="comment"><div id="post-31857-score" class="comment-score"></div><div class="comment-text"><p>Hi Pascal - you're exactly right The 32bit package of Wireshark has lua5.1.dll which depends on msvcrt.dll, where the 64-bit wireshark package has lua5.1.dll which depends on msvcr100.dll I will try to build a new version</p></div><div id="comment-31857-info" class="comment-info"><span class="comment-age">(15 Apr '14, 16:48)</span> Scott Harman</div></div><span id="31870"></span><div id="comment-31870" class="comment not_top_scorer"><div id="post-31870-score" class="comment-score"></div><div class="comment-text"><p>Be aware that the current development release is moving to a new version of Lua, albeit still built with MSVC2010, see <a href="http://www.wireshark.org/lists/wireshark-dev/201404/msg00016.html">this</a> thread from the dev mail list and <a href="https://code.wireshark.org/review/#/c/991/">this</a> change from Gerrit.</p></div><div id="comment-31870-info" class="comment-info"><span class="comment-age">(16 Apr '14, 02:29)</span> grahamb ♦</div></div><span id="31873"></span><div id="comment-31873" class="comment not_top_scorer"><div id="post-31873-score" class="comment-score"></div><div class="comment-text"><p>We should probably include lua-5.2.3_Win32_dll11_lib.zip in our packages and use that one if building with MSVC2012 and corresponding for Win64 parhaps even add the packages for VC12. <a href="http://sourceforge.net/projects/luabinaries/files/5.2.3/Windows%20Libraries/Dynamic/">http://sourceforge.net/projects/luabinaries/files/5.2.3/Windows%20Libraries/Dynamic/</a></p></div><div id="comment-31873-info" class="comment-info"><span class="comment-age">(16 Apr '14, 04:31)</span> Anders ♦</div></div><span id="31885"></span><div id="comment-31885" class="comment not_top_scorer"><div id="post-31885-score" class="comment-score"></div><div class="comment-text"><p>This is something that could be done, yes. But how many MSVC version should we "support" in parallel? I tried to avoid using a Lua version linked to a specific MSVC version but the one compiled with mingw introduced bug 9957</p></div><div id="comment-31885-info" class="comment-info"><span class="comment-age">(16 Apr '14, 07:27)</span> Pascal Quantin</div></div><span id="31886"></span><div id="comment-31886" class="comment not_top_scorer"><div id="post-31886-score" class="comment-score"></div><div class="comment-text"><p>I'm building with MSVC2012 and would like that supported :-) Perhaps we should move to use that one officially?</p></div><div id="comment-31886-info" class="comment-info"><span class="comment-age">(16 Apr '14, 07:35)</span> Anders ♦</div></div><span id="31889"></span><div id="comment-31889" class="comment not_top_scorer"><div id="post-31889-score" class="comment-score"></div><div class="comment-text"><p>I've taken this up with a thread on the dev list.</p></div><div id="comment-31889-info" class="comment-info"><span class="comment-age">(16 Apr '14, 07:47)</span> grahamb ♦</div></div><span id="31912"></span><div id="comment-31912" class="comment not_top_scorer"><div id="post-31912-score" class="comment-score"></div><div class="comment-text"><p>A commit has been done in the development tree (not 1.10 branch) so as to rely only on MSVCR110.dll when building the GTK based Wireshark with MSVC2012: <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commit;h=791dd4e1285e10ab875ef741ec16fdbd406cf034">https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commit;h=791dd4e1285e10ab875ef741ec16fdbd406cf034</a></p><p>Qt based Wireshark still has the dependency on MSVCR100.dll, as discussed on the dev mailing list.</p></div><div id="comment-31912-info" class="comment-info"><span class="comment-age">(17 Apr '14, 01:06)</span> Pascal Quantin</div></div></div><div id="comment-tools-31807" class="comment-tools"><span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a></div><div class="clear"></div><div id="comment-31807-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39348"></span>

<div id="answer-container-39348" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39348-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I have 64 windows machine and were trying to install customized 32bit wireshark. The problem fixed after installing 32bit MSVC distribution. Krishankant Jingar</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '15, 22:01</strong></p><img src="https://secure.gravatar.com/avatar/42c26082f626d3d20bfc1aab76b096ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Krish&#39;s gravatar image" /><p>Krish<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Krish has no accepted answers">0%</span></p></div></div><div id="comments-container-39348" class="comments-container"></div><div id="comment-tools-39348" class="comment-tools"></div><div class="clear"></div><div id="comment-39348-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

