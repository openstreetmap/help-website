+++
type = "question"
title = "The temporary file to which the capture would be saved (&quot;&quot;) could not be opened: Invalid argument."
description = '''Hi I have Windows Seven Home Prenium, fresh installed. When I choose a interface and start a capture, I have this error : The temporary file to which the capture would be saved (&quot;&quot;) could not be opened: Permission denied. What I tried : 1) I checked the global variables TMP and TEMP. It&#x27;s okay (%USE...'''
date = "2015-02-14T17:40:00Z"
lastmod = "2017-01-04T06:07:00Z"
weight = 39864
keywords = [ "temporary", "file", "permission" ]
aliases = [ "/questions/39864" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [The temporary file to which the capture would be saved ("") could not be opened: Invalid argument.](/questions/39864/the-temporary-file-to-which-the-capture-would-be-saved-could-not-be-opened-invalid-argument)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39864-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I have Windows Seven Home Prenium, fresh installed. When I choose a interface and start a capture, I have this error : <strong>The temporary file to which the capture would be saved ("") could not be opened: Permission denied.</strong></p><p>What I tried : 1) I checked the global variables TMP and TEMP. It's okay (%USERPROFILE%\AppData\Local\Temp;) I wireshark, About, Folder tab, there is the \Local\Temp folder. 2) I gave all the rights on the Local/Temp for the Guest user, all user etc. 3) My Windows account has the administrator rights 4) I ran the executable as administrator (click right etc.) 5) I installed wireshark (x86 or x64) as administrator, same problem... 6) I tried to install wireshark 1.99...same problem</p><p>How can I solve my problem ?</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags">temporary file permission</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Feb '15, 17:40</strong></p><img src="https://secure.gravatar.com/avatar/bb815b46a2b20bbb4a8bea157207b394?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nico128&#39;s gravatar image" /><p>Nico128<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nico128 has no accepted answers">0%</span></p></div></div><div id="comments-container-39864" class="comments-container"></div><div id="comment-tools-39864" class="comment-tools"></div><div class="clear"></div><div id="comment-39864-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="39867"></span>

<div id="answer-container-39867" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39867-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In the Help -&gt; About Wireshark -&gt; Folders dialog, the Temp folder should be an absolute path, i.e. I have <code>C:\Users\grahamb\AppData\Local\Temp</code> and the Wireshark Temp folder tracks the environment variable "TEMP".</p><p>Try opening a command prompt, check the value of the environment var TEMP (<code>echo %TEMP%</code>) adjust if necessary to be an absolute path and then run Wireshark from that command prompt.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '15, 01:56</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-39867" class="comments-container"><span id="39870"></span><div id="comment-39870" class="comment"><div id="post-39870-score" class="comment-score"></div><div class="comment-text"><p>Hi</p><p>I rebooted my computer and now it's work. there is now a new folder named "Temp;" with the char ";". =&gt; "AppData\Local\Temp;"</p><p>Problem fixed Thank you</p></div><div id="comment-39870-info" class="comment-info"><span class="comment-age">(15 Feb '15, 11:15)</span> Nico128</div></div></div><div id="comment-tools-39867" class="comment-tools"></div><div class="clear"></div><div id="comment-39867-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="58497"></span>

<div id="answer-container-58497" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58497-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Sirs,</p><p>I got the same problem today with the error message.</p><p>Even though I use "echo %TEMP%" and it shows the same path as I see in the help dialog, there's still the same error message. Then I tried this:</p><ol><li>Go to edit the path of environment variable "TEMP", make it to be "%USERPROFILE%\Local Settings\Temp<strong>1</strong>". Then the error disappears when I run Wireshark.</li><li>Reboot (I'm not sure if need to do this)</li><li>Make the "TEMP" path back to "%USERPROFILE%\Local Settings\Temp" and open the porgram. The wireshark works now as normal.</li></ol><p>BTW, I got this problem because I used ramdisk and move my "TEMP" to it. When I removed the ramdisk and recoverd the path of "TEMP", it occurs.</p><p>Hope this post can save people who have the same problem with me.</p><p>BRs,</p><p>Mark</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '17, 06:07</strong></p><img src="https://secure.gravatar.com/avatar/1a7c48bb55fc3a0373b42b03398c748e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hcbamboo&#39;s gravatar image" /><p>hcbamboo<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hcbamboo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Jan '17, 06:13</p></div></div><div id="comments-container-58497" class="comments-container"></div><div id="comment-tools-58497" class="comment-tools"></div><div class="clear"></div><div id="comment-58497-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

