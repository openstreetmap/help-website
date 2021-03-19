+++
type = "question"
title = "KNXnet/IP plugin error"
description = '''Hi, I&#x27;m using Wireshark on a Win 8 OS to check the datagrams of a KNX software, and also using a .dll plugin already developed and distributed by http://knxnetipdissect.sourceforge.net/ But I haven&#x27;t get it to work fine. I&#x27;ve installed 64 and 32 bit version, and applying the compatibility to Win 7 a...'''
date = "2013-03-13T10:04:00Z"
lastmod = "2013-03-13T10:32:00Z"
weight = 19459
keywords = [ "knxnetip" ]
aliases = [ "/questions/19459" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [KNXnet/IP plugin error](/questions/19459/knxnetip-plugin-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19459-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm using Wireshark on a Win 8 OS to check the datagrams of a KNX software, and also using a .dll plugin already developed and distributed by <a href="http://knxnetipdissect.sourceforge.net/">http://knxnetipdissect.sourceforge.net/</a></p><p>But I haven't get it to work fine. I've installed 64 and 32 bit version, and applying the compatibility to Win 7 and it's still not working.</p><p>The site says that I should copy the plugin to the Plugin folder inside the Wireshark folder from windows.</p><p>The error that shows using 64bit version is:</p><p>"Couldn't load module C:\Program Files\Wireshark\plugins\1.8.4\knxnetip.dll: `C:\Program Files\Wireshark\plugins\1.8.4\knxnetip.dll': %1 is not a valid Win32 application."</p><p>And the 32bit version is:</p><p>"The program can't start because MSVCR71.dll is missing from your computer. Try reinstalling the program to fix this problem."</p><p>and also:</p><p>Couldn't load module C:\Program Files (x86)\Wireshark\plugins\1.8.4\knxnetip.dll: `C:\Program Files (x86)\Wireshark\plugins\1.8.4\knxnetip.dll': The specified module could not be found.</p><p>Can anyone explain me a solution?!</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">knxnetip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '13, 10:04</strong></p><img src="https://secure.gravatar.com/avatar/645e840409f2adae1d1fa3838be40518?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Canha&#39;s gravatar image" /><p>Canha<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Canha has no accepted answers">0%</span></p></div></div><div id="comments-container-19459" class="comments-container"></div><div id="comment-tools-19459" class="comment-tools"></div><div class="clear"></div><div id="comment-19459-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19460"></span>

<div id="answer-container-19460" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19460-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like the plugin dll is a 32 bit version, so you will have to use a 32 bit version of Wireshark. This explains the "not a valid Win32 application" error when you try to run it with 64 bit Wireshark.</p><p>Next, the dll appears to have been built using VS 2003 for Wireshark 1.0.6 and requires the VC 7.1 runtime DLL. Unfortunately I don't think this is available for download now. In addition, as Wireshark 1.8.x is compiled with a much newer version of VC that uses a newer version of the VC runtime DLL, bad things might happen even if you can find a MSVCR71.dll.</p><p>To get this running, your best bet will be to setup a Wireshark build environment, create a build of wireshark to ensure you can build it, then add the source of the plugin, fix up whatever has changed between Wireshark 1.0.6 and the current 1.8.x to enable the plugin to be built and then you'll be good to go.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '13, 10:32</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-19460" class="comments-container"><span id="19465"></span><div id="comment-19465" class="comment"><div id="post-19465-score" class="comment-score"></div><div class="comment-text"><p>Also note: <a href="http://www.codeproject.com/KB/IP/custom_dissector.aspx">http://www.codeproject.com/KB/IP/custom_dissector.aspx</a> (as mentioned in the README.windows) is somewhat out of date as to setting up a Wireshark development environment.</p><p>The <a href="https://www.wireshark.org/docs/wsdg_html_chunked/">Wireshark Development Guide</a> has up-to-date information.</p></div><div id="comment-19465-info" class="comment-info"><span class="comment-age">(13 Mar '13, 11:16)</span> Bill Meier ♦♦</div></div><span id="19468"></span><div id="comment-19468" class="comment"><div id="post-19468-score" class="comment-score">2</div><div class="comment-text"><p>Just for the heck of it, I tried building the knxnetip plugin with Wireshark 1.8.</p><p>The plugin, as is, built w/o error.</p><p>(Note: This is <em>not</em> true for the current dev Wireshark (1.9). There have been some changes in the Wireshark API and in the plugin Windows makefiles in 1.9).</p><p>(If you choose to create the plugin for 1.8) basically:</p><ol><li><p>Setup and test by doing a build the Wireshark build environment (as Graham indicated).</p></li><li><p>Create a dir ...\plugins\knxnetip Put the plugin sources in that dir.</p></li><li><p>add knxnetip to the appropriate line in plugins\Makefile.nmake</p></li><li><p>Do a make again ....</p></li></ol></div><div id="comment-19468-info" class="comment-info"><span class="comment-age">(13 Mar '13, 12:02)</span> Bill Meier ♦♦</div></div><span id="19493"></span><div id="comment-19493" class="comment"><div id="post-19493-score" class="comment-score"></div><div class="comment-text"><p>Thanks Bill Meier and grahamb...I'll try it in the next couple of days..</p></div><div id="comment-19493-info" class="comment-info"><span class="comment-age">(14 Mar '13, 03:18)</span> Canha</div></div></div><div id="comment-tools-19460" class="comment-tools"></div><div class="clear"></div><div id="comment-19460-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

