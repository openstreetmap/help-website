+++
type = "question"
title = "Failed uninstall"
description = '''I am trying to remove Wireshark from my computer, but upon uninstalling, I immediately receive an error message &quot;rawshark.exe could not be removed. Is it in use?&quot; I am having difficulty finding a way to end the rawshark.exe process - no rawshark.exe process shown in task manager. I am running Window...'''
date = "2013-11-20T06:41:00Z"
lastmod = "2015-01-20T12:21:00Z"
weight = 27158
keywords = [ "rawshark", "rawshark.exe", "uninstall" ]
aliases = [ "/questions/27158" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Failed uninstall](/questions/27158/failed-uninstall)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27158-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to remove Wireshark from my computer, but upon uninstalling, I immediately receive an error message "rawshark.exe could not be removed. Is it in use?" I am having difficulty finding a way to end the rawshark.exe process - no rawshark.exe process shown in task manager.</p><p>I am running Windows 7. Thanks in advance.</p><p>Tom</p></div><div id="question-tags" class="tags-container tags">rawshark rawshark.exe uninstall</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Nov '13, 06:41</strong></p><img src="https://secure.gravatar.com/avatar/e26914f4ca59b10878c0ba104bd9561d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tjenks2&#39;s gravatar image" /><p>tjenks2<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tjenks2 has no accepted answers">0%</span></p></div></div><div id="comments-container-27158" class="comments-container"></div><div id="comment-tools-27158" class="comment-tools"></div><div class="clear"></div><div id="comment-27158-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="27162"></span>

<div id="answer-container-27162" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27162-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://www.wireshark.org/docs/man-pages/rawshark.html">rawshark.exe</a> is part of the Wireshark install, but isn't normally started unless requested by the user. As it's a command line utility double clicking it from explorer or running it from the command line with parameters just causes an error response and the program exits.</p><p>Have you clicked the Task Manager button "Show processes from all users"? Have you tried rebooting and running the uninstall again? I suppose it's possible that some other process is starting rawshark, but it should still show up in Task Mgr if so.</p><p>It's possible that rawshark isn't running but some other app has a "lock" on the file, possibly a virus scanner.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '13, 07:00</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-27162" class="comments-container"><span id="27171"></span><div id="comment-27171" class="comment"><div id="post-27171-score" class="comment-score"></div><div class="comment-text"><p>I tried the task manager and reboot already, and now looked in the "Show processes from all users", but still no luck. If there were a lock on the file, which is possible (I'm running Norton360), do you have ideas as to how to get it unlocked?</p></div><div id="comment-27171-info" class="comment-info"><span class="comment-age">(20 Nov '13, 09:04)</span> tjenks2</div></div><span id="27173"></span><div id="comment-27173" class="comment"><div id="post-27173-score" class="comment-score"></div><div class="comment-text"><p>did you try to delete rawshark.exe manually?</p></div><div id="comment-27173-info" class="comment-info"><span class="comment-age">(20 Nov '13, 09:31)</span> Kurt Knochner ♦</div></div><span id="27174"></span><div id="comment-27174" class="comment"><div id="post-27174-score" class="comment-score"></div><div class="comment-text"><p>If the file is "locked" then you probably won't be able to delete it. I use a utility <a href="http://www.emptyloop.com/unlocker/">Unlocker</a> for occasions such as this.</p></div><div id="comment-27174-info" class="comment-info"><span class="comment-age">(20 Nov '13, 09:38)</span> grahamb ♦</div></div><span id="27240"></span><div id="comment-27240" class="comment"><div id="post-27240-score" class="comment-score"></div><div class="comment-text"><p>I was able to delete rawshark manually, though received the same error message for another associated .exe file. After deleting all the .exe files in the Wireshark directory, I was able to fully uninstall. Thanks for the help, a bit of a workaround, but the end goal was reached.</p></div><div id="comment-27240-info" class="comment-info"><span class="comment-age">(21 Nov '13, 13:12)</span> tjenks2</div></div></div><div id="comment-tools-27162" class="comment-tools"></div><div class="clear"></div><div id="comment-27162-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30932"></span>

<div id="answer-container-30932" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30932-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Ran into the same problem when trying to install a Wireshark update on Win7.</p><p>But manually downloading the update and then running the Wireshark installer using the "Run as administrator" option worked without the need for any other workarounds.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Mar '14, 09:20</strong></p><img src="https://secure.gravatar.com/avatar/c60a5a5619fcae230257214ec8c12ce6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PolarBear&#39;s gravatar image" /><p>PolarBear<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PolarBear has no accepted answers">0%</span></p></div></div><div id="comments-container-30932" class="comments-container"><span id="35858"></span><div id="comment-35858" class="comment"><div id="post-35858-score" class="comment-score"></div><div class="comment-text"><p>I faced with the same problem. Everything that was needed is to run uninstaller with Admin permissions.</p></div><div id="comment-35858-info" class="comment-info"><span class="comment-age">(28 Aug '14, 23:30)</span> Pilgrim</div></div><span id="41426"></span><div id="comment-41426" class="comment"><div id="post-41426-score" class="comment-score"></div><div class="comment-text"><p>Run the Uninstaller at Admininstrater... it will remove everything</p></div><div id="comment-41426-info" class="comment-info"><span class="comment-age">(14 Apr '15, 05:25)</span> Rajan Dave</div></div></div><div id="comment-tools-30932" class="comment-tools"></div><div class="clear"></div><div id="comment-30932-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39322"></span>

<div id="answer-container-39322" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39322-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Go to your Startup menu</p><p>type in wireshark</p><p>click see more results link</p><p>Find the downloaded wireshark folder. It will contain an uninstall folder.</p><p>Double click this folder and the windows operating system will get you through the rest.</p><p>Go throuh these steps from the start and you will be able to delete all folders and captures pertaining to wireshark.</p><p>Done Deal</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '15, 12:21</strong></p><img src="https://secure.gravatar.com/avatar/cf37b82c74c5b187f0323c0ea0c6995e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="1424dmitch&#39;s gravatar image" /><p>1424dmitch<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="1424dmitch has no accepted answers">0%</span></p></div></div><div id="comments-container-39322" class="comments-container"><span id="48220"></span><div id="comment-48220" class="comment"><div id="post-48220-score" class="comment-score"></div><div class="comment-text"><p>Right click uninstall.exe and select "run as Administrator"</p></div><div id="comment-48220-info" class="comment-info"><span class="comment-age">(03 Dec '15, 03:58)</span> Vash</div></div></div><div id="comment-tools-39322" class="comment-tools"></div><div class="clear"></div><div id="comment-39322-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

