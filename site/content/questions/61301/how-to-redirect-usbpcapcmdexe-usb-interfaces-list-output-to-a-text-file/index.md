+++
type = "question"
title = "How to Redirect USBPcapCmd.exe &quot;USB interfaces list&quot; output to a text file."
description = '''Hi i need to redirect interface list from USBPcapcmd.exe to an text file for getting USB HUB number in command line. please help me how to achieve this, is there any way, i can get &quot;USB interface list&quot; to a text file. Thanks, Pramod'''
date = "2017-05-09T03:24:00Z"
lastmod = "2017-05-31T10:53:00Z"
weight = 61301
keywords = [ "usbpcapcmd" ]
aliases = [ "/questions/61301" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to Redirect USBPcapCmd.exe "USB interfaces list" output to a text file.](/questions/61301/how-to-redirect-usbpcapcmdexe-usb-interfaces-list-output-to-a-text-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61301-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi i need to redirect interface list from USBPcapcmd.exe to an text file for getting USB HUB number in command line. please help me how to achieve this, is there any way, i can get <strong>"USB interface list"</strong> to a text file.</p><p>Thanks, Pramod</p></div><div id="question-tags" class="tags-container tags">usbpcapcmd</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '17, 03:24</strong></p><img src="https://secure.gravatar.com/avatar/d2c9789a43b411fb047ce641badacaf5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pramod&#39;s gravatar image" /><p>Pramod<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pramod has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 May '17, 22:03</p></div></div><div id="comments-container-61301" class="comments-container"></div><div id="comment-tools-61301" class="comment-tools"></div><div class="clear"></div><div id="comment-61301-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="61719"></span>

<div id="answer-container-61719" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61719-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use the following command:</p><pre><code>USBPcapCMD.exe --extcap-interfaces &gt; interfaces.txt</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '17, 10:53</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-61719" class="comments-container"><span id="61726"></span><div id="comment-61726" class="comment"><div id="post-61726-score" class="comment-score"></div><div class="comment-text"><p>Thanks for ur reply. Is there any way we can redirect all output to a text file. I need to redirect all interface details which is in below image.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Usbpcap_interface.PNG" alt="alt text" /></p></div><div id="comment-61726-info" class="comment-info"><span class="comment-age">(31 May '17, 22:54)</span> Pramod</div></div></div><div id="comment-tools-61719" class="comment-tools"></div><div class="clear"></div><div id="comment-61719-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="61707"></span>

<div id="answer-container-61707" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61707-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think you can, the program doesn't have an option to list the interfaces and if you don't provide any options it assumes interactive mode in a new console window.</p><p>As it's not part of the Wireshark project you'll either need to modify the code yourself, or file an issue over at the <a href="https://github.com/desowin/usbpcap/issues">USBPcap site</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '17, 03:25</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></img></div></div><div id="comments-container-61707" class="comments-container"><span id="61710"></span><div id="comment-61710" class="comment"><div id="post-61710-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/1225/grahamb">@grahamb</a>, thanks for ur replay. I will report the issue in USBPcap site.</p></div><div id="comment-61710-info" class="comment-info"><span class="comment-age">(31 May '17, 07:24)</span> Pramod</div></div></div><div id="comment-tools-61707" class="comment-tools"></div><div class="clear"></div><div id="comment-61707-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

