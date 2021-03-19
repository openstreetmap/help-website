+++
type = "question"
title = "Is ExecDos.dll a valid part of your install ?"
description = '''I downloaded and attempted to install WireShart / WinpCap. I am using Malwarebytes and it picks up one of your install files as being Malware - ExecDos.dll, Hmmm - Is this program part of your normal install (and it is safe to install) or did some malware get into your build /install ??'''
date = "2010-09-29T12:28:00Z"
lastmod = "2010-09-29T13:32:00Z"
weight = 356
keywords = [ "malware", "execdos.dll" ]
aliases = [ "/questions/356" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is ExecDos.dll a valid part of your install ?](/questions/356/is-execdosdll-a-valid-part-of-your-install)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-356-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I downloaded and attempted to install WireShart / WinpCap.</p><p>I am using Malwarebytes and it picks up one of your install files as being Malware - ExecDos.dll,</p><p>Hmmm - Is this program part of your normal install (and it is safe to install) or did some malware get into your build /install ??</p></div><div id="question-tags" class="tags-container tags">malware execdos.dll</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Sep '10, 12:28</strong></p><img src="https://secure.gravatar.com/avatar/4b425ee0c06bf0978a91b38fd390d9c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gordzilla&#39;s gravatar image" /><p>Gordzilla<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gordzilla has no accepted answers">0%</span></p></div></div><div id="comments-container-356" class="comments-container"></div><div id="comment-tools-356" class="comment-tools"></div><div class="clear"></div><div id="comment-356-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="363"></span>

<div id="answer-container-363" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-363-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Did MalwareBytes identify ExecDos.dll in Wireshark (note the spelling and capitalization) or WinPcap? NSIS, the installer system used by both WinPcap and Wireshark has a <a href="http://nsis.sourceforge.net/ExecDos_plug-in">plugin named ExecDos</a>. The Wireshark installer doesn't use it, but the WinPcap installer does.</p><p>What version of Wireshark and WinPcap are you trying to install? <a href="http://www.virustotal.com/url-scan/report.html?id=5aa428187db497f57d89653ae2d026e6-1285455607">Wireshark 1.4.0 for Win32</a>, <a href="http://www.virustotal.com/url-scan/report.html?id=b8c2825796a57339ac418bc55826fcfb-1284446308">Wireshark 1.4.0 for Win64</a>, and <a href="http://www.virustotal.com/file-scan/report.html?id=6dd1fd832de94c4b374b25f44f6bf8fb0af034fe6768bd58d79b439b55d09993-1285689800">WinPcap 4.1.2</a> are all clean according to VirusTotal.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '10, 13:32</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-363" class="comments-container"><span id="364"></span><div id="comment-364" class="comment"><div id="post-364-score" class="comment-score"></div><div class="comment-text"><p>I was using the wireshark-win32-1.4.0 install and it was during the WinPcap install. Basically malwarebytes picks it up as a piece of potential Spyware with the Prompt "Malwarebytes' Anti-Malware has detected a malicious process attempting to start and has blocked the execution attempt. Please select an option below." The options are Disable Protection, Ignore, Quarintine. The file ExecDos.dll is labeled by them as a Trojan.</p><p>What do you think ? It this file supposed to be in the install and is it Trojan???</p></div><div id="comment-364-info" class="comment-info"><span class="comment-age">(29 Sep '10, 14:00)</span> Gordzilla</div></div><span id="365"></span><div id="comment-365" class="comment"><div id="post-365-score" class="comment-score"></div><div class="comment-text"><p>It's likely a false positive. NSIS has certainly had its fair share: http://nsis.sourceforge.net/NSIS_False_Positives</p><p>Would it be possible to submit Wireshark and/or WinPcap to Malwarebytes to be analyzed again?</p></div><div id="comment-365-info" class="comment-info"><span class="comment-age">(29 Sep '10, 14:03)</span> Gerald Combs ♦♦</div></div><span id="366"></span><div id="comment-366" class="comment"><div id="post-366-score" class="comment-score"></div><div class="comment-text"><p>I would imagine so. They have an email address on their "Support Page". Thanks and I am going to assume that it is OK.</p></div><div id="comment-366-info" class="comment-info"><span class="comment-age">(29 Sep '10, 14:22)</span> Gordzilla</div></div></div><div id="comment-tools-363" class="comment-tools"></div><div class="clear"></div><div id="comment-363-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

