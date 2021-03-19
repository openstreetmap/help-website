+++
type = "question"
title = "How to add extra file to Wireshark folder for plugin"
description = '''I have a plugin for Wireshark that works when copying my files to  C:&#92;Program Files&#92;Wireshark&#92;plugins&#92;MyPlugin&#92;myplugin.dll C:&#92;Program Files&#92;Wireshark&#92;myplug.dll (required for myplugin.dll to actually work - by design)  Now I want to build my plugin as part of Wireshark. The myplug.obj, myplug.lib (...'''
date = "2010-11-05T13:11:00Z"
lastmod = "2010-11-05T14:25:00Z"
weight = 828
keywords = [ "development", "file", "plugins" ]
aliases = [ "/questions/828" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to add extra file to Wireshark folder for plugin](/questions/828/how-to-add-extra-file-to-wireshark-folder-for-plugin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-828-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a plugin for Wireshark that works when copying my files to</p><blockquote><p>C:\Program Files\Wireshark\plugins\MyPlugin\myplugin.dll</p><p>C:\Program Files\Wireshark\myplug.dll (required for myplugin.dll to actually work - by design)</p></blockquote><p>Now I want to build my plugin as part of Wireshark. The myplug.obj, myplug.lib (needed by myplugin.dll to built), and myplug.dll are located outside of the C:\wireshark-trunk and everything is built correctly but I cannot get myplug.dll copied into the wireshark folder during initial build.</p><p>What file(s) do I need to look at to include myplug.dll for packaging?</p><p>Thanks, Michael</p></div><div id="question-tags" class="tags-container tags">development file plugins</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Nov '10, 13:11</strong></p><img src="https://secure.gravatar.com/avatar/5159f162cc2dd7daa781617151ce2efc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michael%20Wells&#39;s gravatar image" /><p>Michael Wells<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michael Wells has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Nov '10, 06:03</p></div></div><div id="comments-container-828" class="comments-container"></div><div id="comment-tools-828" class="comment-tools"></div><div class="clear"></div><div id="comment-828-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="829"></span>

<div id="answer-container-829" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-829-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><ol><li>to get them copied during the build, adapt plugins/Makefile.nmake, the code for target install-plugins</li><li>to get them packaged adapt packaging/nsis/wireshark.nsi section SecPlugins</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Nov '10, 14:25</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-829" class="comments-container"><span id="852"></span><div id="comment-852" class="comment"><div id="post-852-score" class="comment-score"></div><div class="comment-text"><p>Thank you, I have already modified all the files including the two you mentioned.<br />
The build and installer correctly get myplugin.dll but I have not found a way to get myplug.dll (notice the difference in name) copied into the install dir of Wireshark during build.install time. I still need to copy that one manually.</p></div><div id="comment-852-info" class="comment-info"><span class="comment-age">(08 Nov '10, 06:18)</span> Michael Wells</div></div></div><div id="comment-tools-829" class="comment-tools"></div><div class="clear"></div><div id="comment-829-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

