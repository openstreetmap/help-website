+++
type = "question"
title = "Disable check for updates and downloads for wireshark 1.11.3"
description = '''Hi,How to disable the check for updates and downloads after installation.Is there any Registry to suppress for this.Please provide the solution for this ASAP as it is urgent requirement'''
date = "2014-02-09T23:58:00Z"
lastmod = "2014-02-10T03:08:00Z"
weight = 29595
keywords = [ "updates" ]
aliases = [ "/questions/29595" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Disable check for updates and downloads for wireshark 1.11.3](/questions/29595/disable-check-for-updates-and-downloads-for-wireshark-1113)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29595-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,How to disable the check for updates and downloads after installation.Is there any Registry to suppress for this.Please provide the solution for this ASAP as it is urgent requirement</p></div><div id="question-tags" class="tags-container tags">updates</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '14, 23:58</strong></p><img src="https://secure.gravatar.com/avatar/9e1a4cf24ba4c99becad013f05cfa946?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pkumar&#39;s gravatar image" /><p>pkumar<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pkumar has no accepted answers">0%</span></p></div></div><div id="comments-container-29595" class="comments-container"></div><div id="comment-tools-29595" class="comment-tools"></div><div class="clear"></div><div id="comment-29595-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="29609"></span>

<div id="answer-container-29609" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29609-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>To disable the Check for Update after installation use either:</p><ul><li>The GUI (GTK version); Edit | Preferences... | User Interface | Check for updates</li><li>Use a text editor to modify the config files, use Help | About | Folders to determine the location of the files, and in those locations edit the "preferences" file to add the setting <code>gui_update_enabled: FALSE</code>.</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '14, 03:08</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-29609" class="comments-container"><span id="29632"></span><div id="comment-29632" class="comment"><div id="post-29632-score" class="comment-score"></div><div class="comment-text"><p>I can see that updates are suppressed in the edit/Preferences by following the above steps. I need to supress the check for updates and downloads in Help menu. Please let me know Thanks in advance</p></div><div id="comment-29632-info" class="comment-info"><span class="comment-age">(10 Feb '14, 06:56)</span> pkumar</div></div><span id="29638"></span><div id="comment-29638" class="comment"><div id="post-29638-score" class="comment-score"></div><div class="comment-text"><p>I think you would need to compile your own version to do that and remove the menu entry.</p></div><div id="comment-29638-info" class="comment-info"><span class="comment-age">(10 Feb '14, 08:21)</span> grahamb ♦</div></div></div><div id="comment-tools-29609" class="comment-tools"></div><div class="clear"></div><div id="comment-29609-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="29596"></span>

<div id="answer-container-29596" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29596-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>See the answer to a similar question</p><blockquote><p><a href="http://ask.wireshark.org/questions/24780/remove-update-feature">http://ask.wireshark.org/questions/24780/remove-update-feature</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '14, 00:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-29596" class="comments-container"><span id="29599"></span><div id="comment-29599" class="comment"><div id="post-29599-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Thanks for your reply. After installation i dont see the file name "config.nmake" is present in the INSTALLDIR.Please let me know where this file is located.</p><p>Thanks PKumar</p></div><div id="comment-29599-info" class="comment-info"><span class="comment-age">(10 Feb '14, 01:12)</span> pkumar</div></div><span id="29608"></span><div id="comment-29608" class="comment"><div id="post-29608-score" class="comment-score"></div><div class="comment-text"><p>The answer Kurt refers to discusses disabling the update check when developing and compiling, not after installation, thus config.nmake is a file used during development and it won't be in your INSTALDIR.</p></div><div id="comment-29608-info" class="comment-info"><span class="comment-age">(10 Feb '14, 03:02)</span> grahamb ♦</div></div></div><div id="comment-tools-29596" class="comment-tools"></div><div class="clear"></div><div id="comment-29596-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

