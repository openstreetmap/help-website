+++
type = "question"
title = "how to get decoded data of jn5148 using eclipse"
description = '''I am a newbie . we are using NXP &#x27;s jn518 ek 010 and I am using jennet stack . we are using win 7 and for application development we are using eclipse . our project task is to get the temperature , humidity and luminosity sensors value on PC , from which decision making will be proceeded. can any on...'''
date = "2013-06-07T06:23:00Z"
lastmod = "2013-06-07T07:24:00Z"
weight = 21815
keywords = [ "wireshark" ]
aliases = [ "/questions/21815" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to get decoded data of jn5148 using eclipse](/questions/21815/how-to-get-decoded-data-of-jn5148-using-eclipse)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21815-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am a newbie . we are using NXP 's jn518 ek 010 and I am using jennet stack . we are using win 7 and for application development we are using eclipse . our project task is to get the temperature , humidity and luminosity sensors value on PC , from which decision making will be proceeded. can any one guide me how to get these values in human readable format? I have read about the custom flash programmer which provide these functionality but they were limited to jn5139. 2 )Is it can be done by the help of wireshark? I am using wireshark provided by NXP ,and have capture some packets... but i don't know to decode the capture payload. 3 ) can I get values with the help of hyper terminal?</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jun '13, 06:23</strong></p><img src="https://secure.gravatar.com/avatar/7187af967a307b3dc7014deae47637b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gopalani&#39;s gravatar image" /><p>gopalani<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gopalani has no accepted answers">0%</span></p></div></div><div id="comments-container-21815" class="comments-container"></div><div id="comment-tools-21815" class="comment-tools"></div><div class="clear"></div><div id="comment-21815-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21819"></span>

<div id="answer-container-21819" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21819-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Using the plugin from Jennic and the matching version of Wireshark (very old), captures can be made of the Jennic traffic.</p><p>Whether this will help you in your project is another matter. The EK010 sensor demo users a controller board with an LCD screen to display the sensor data from the wireless remotes. To display the same data on a PC, you will need an appropriate application on the PC that communicates with the controller board over a suitable interface (serial?). You will need an app on the PC and an app on the controller to handle the communication. Wireshark is unlikely to be of much help in doing this, you'll probably get better support on the NXP forums.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jun '13, 07:24</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-21819" class="comments-container"></div><div id="comment-tools-21819" class="comment-tools"></div><div class="clear"></div><div id="comment-21819-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

