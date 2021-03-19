+++
type = "question"
title = "Winpcap Will Not Install"
description = '''I downloaded Wireshark and am having trouble getting Winpcap to install with it. The Wireshark installer does not detect any version of Winpcap on my system and I cannot find it in my system, but every time I run the Winpcap installer I get a message that it detects another version of Winpcap an app...'''
date = "2012-02-26T20:56:00Z"
lastmod = "2014-10-28T09:09:00Z"
weight = 9229
keywords = [ "winpcap", "install" ]
aliases = [ "/questions/9229" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Winpcap Will Not Install](/questions/9229/winpcap-will-not-install)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9229-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I downloaded Wireshark and am having trouble getting Winpcap to install with it. The Wireshark installer does not detect any version of Winpcap on my system and I cannot find it in my system, but every time I run the Winpcap installer I get a message that it detects another version of Winpcap an application is running. No applications besides the installer are running. I am using Windows 7. What is the problem? What should I do?</p></div><div id="question-tags" class="tags-container tags">winpcap install</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Feb '12, 20:56</strong></p><img src="https://secure.gravatar.com/avatar/fb6f317d40585b45ff6ffc00bd2140ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ant_phil&#39;s gravatar image" /><p>ant_phil<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ant_phil has no accepted answers">0%</span></p></div></div><div id="comments-container-9229" class="comments-container"></div><div id="comment-tools-9229" class="comment-tools"></div><div class="clear"></div><div id="comment-9229-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="37398"></span>

<div id="answer-container-37398" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37398-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I just had this problem trying to install 1.12.1-0-g01b65bf from master-1.12 64-bit on Windows 7 Enterprise. When I look in Programs and Features control panel, WinPcap is not listed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '14, 08:08</strong></p><img src="https://secure.gravatar.com/avatar/1c1187fdc03bc230366111c30314e0a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="J4E&#39;s gravatar image" /><p>J4E<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="J4E has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Oct '14, 09:31</p></div></div><div id="comments-container-37398" class="comments-container"><span id="37402"></span><div id="comment-37402" class="comment"><div id="post-37402-score" class="comment-score"></div><div class="comment-text"><p>I downloaded Listdlls.exe from <a href="http://technet.microsoft.com/en-us/sysinternals/bb896656.aspx">http://technet.microsoft.com/en-us/sysinternals/bb896656.aspx</a> and it does not show winpcap.dll</p></div><div id="comment-37402-info" class="comment-info"><span class="comment-age">(28 Oct '14, 08:33)</span> J4E</div></div></div><div id="comment-tools-37398" class="comment-tools"></div><div class="clear"></div><div id="comment-37398-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="37410"></span>

<div id="answer-container-37410" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37410-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is a blog post at <a href="http://nicolask.wordpress.com/2012/09/23/solved-winpcap-4-12-install-error/">http://nicolask.wordpress.com/2012/09/23/solved-winpcap-4-12-install-error/</a> that lists a couple of other names that winpcap.dll might appear under, such as wpcap.dll and packet.dll</p><p>In my case, searching for packet.dll in the listdlls.exe output revealed that a program called WifiSvc.exe was using it (shown in Task Manager "Show Processes of all users" as WifiSvc.exe*32). Trying to End Process on it results in it being automagically re-launched. This program comes with Netgear wireless dongles and apparently thinks it has to run even when the dongle is not plugged in. So my solution was to go to Programs and Features and uninstall the Netgear software. Now WinPcap installs just fine.</p><p>Needless to say, Netgear might not be the only culprit out there, and there might even be other dll's that WinPcap thinks it needs to replace, so if you find something else, please add a reply to this thread so that others can benefit from your research.</p><p>Best of luck!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '14, 09:09</strong></p><img src="https://secure.gravatar.com/avatar/1c1187fdc03bc230366111c30314e0a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="J4E&#39;s gravatar image" /><p>J4E<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="J4E has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Oct '14, 05:56</p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-37410" class="comments-container"></div><div id="comment-tools-37410" class="comment-tools"></div><div class="clear"></div><div id="comment-37410-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

