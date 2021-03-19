+++
type = "question"
title = "How to display strings instead of values for custom columns defined"
description = '''Hi, I have defined some custom columns through prefs.c. The columns which I have defined take values from fields registered through my custom dissector. But the problem is that in packet details the value of these fields are displayed as strings(As I have used vals() function in dissector code) but ...'''
date = "2012-03-01T20:37:00Z"
lastmod = "2012-03-03T08:33:00Z"
weight = 9301
keywords = [ "development", "columns" ]
aliases = [ "/questions/9301" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to display strings instead of values for custom columns defined](/questions/9301/how-to-display-strings-instead-of-values-for-custom-columns-defined)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9301-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have defined some custom columns through prefs.c. The columns which I have defined take values from fields registered through my custom dissector. But the problem is that in packet details the value of these fields are displayed as strings(As I have used vals() function in dissector code) but while the same field is used in column the raw value is displayed.</p></div><div id="question-tags" class="tags-container tags">development columns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Mar '12, 20:37</strong></p><img src="https://secure.gravatar.com/avatar/d221d26845724614e25ab8e51887c4bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ashish_goel&#39;s gravatar image" /><p>ashish_goel<br />
<span class="score" title="15 reputation points">15</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ashish_goel has no accepted answers">0%</span></p></div></div><div id="comments-container-9301" class="comments-container"><span id="9324"></span><div id="comment-9324" class="comment"><div id="post-9324-score" class="comment-score"></div><div class="comment-text"><p>any suggestions?? I have searched through readme.developer many times but found nothing related to this :(</p></div><div id="comment-9324-info" class="comment-info"><span class="comment-age">(03 Mar '12, 06:27)</span> ashish_goel</div></div></div><div id="comment-tools-9301" class="comment-tools"></div><div class="clear"></div><div id="comment-9301-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9328"></span>

<div id="answer-container-9328" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9328-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Which version are you using? In recent versions you can rightclick on the column title and check "Show Resolved". I'm not sure if that was already added in 1.6.x or that you need to install 1.7.x.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Mar '12, 08:33</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-9328" class="comments-container"><span id="9329"></span><div id="comment-9329" class="comment"><div id="post-9329-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>I am using version 1.7.1. There is an option of "Show Resolved" and it is already checked. Unchecking it converts the value into hexadecimal.</p></div><div id="comment-9329-info" class="comment-info"><span class="comment-age">(03 Mar '12, 08:52)</span> ashish_goel</div></div><span id="9343"></span><div id="comment-9343" class="comment"><div id="post-9343-score" class="comment-score"></div><div class="comment-text"><p>suggestions plz ??</p></div><div id="comment-9343-info" class="comment-info"><span class="comment-age">(04 Mar '12, 06:02)</span> ashish_goel</div></div></div><div id="comment-tools-9328" class="comment-tools"></div><div class="clear"></div><div id="comment-9328-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

