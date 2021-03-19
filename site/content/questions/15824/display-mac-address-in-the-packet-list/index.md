+++
type = "question"
title = "Display MAC address in the packet list"
description = '''I am using the filter &quot;bootp.option.type==1 and bootp.option.value==01&quot; to find the DHCP Discovers. When I export the results to a csv file, I get IP addresses all-zeros (No IP yet) and all-ones (broadcast) To know what station is doing this, I need the MAC address of the sender. How can I define th...'''
date = "2012-11-12T07:25:00Z"
lastmod = "2012-11-12T11:38:00Z"
weight = 15824
keywords = [ "dhcp", "packetlist", "mac-address" ]
aliases = [ "/questions/15824" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Display MAC address in the packet list](/questions/15824/display-mac-address-in-the-packet-list)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15824-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using the filter "bootp.option.type==1 and bootp.option.value==01" to find the DHCP Discovers. When I export the results to a csv file, I get IP addresses all-zeros (No IP yet) and all-ones (broadcast) To know what station is doing this, I need the MAC address of the sender. How can I define the fields that are displayed in the packet list view to include MAC addresses?</p></div><div id="question-tags" class="tags-container tags">dhcp packetlist mac-address</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Nov '12, 07:25</strong></p><img src="https://secure.gravatar.com/avatar/2f4fff4550777f303d310bc5503493cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Han%20Koster&#39;s gravatar image" /><p>Han Koster<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Han Koster has no accepted answers">0%</span></p></div></div><div id="comments-container-15824" class="comments-container"></div><div id="comment-tools-15824" class="comment-tools"></div><div class="clear"></div><div id="comment-15824-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="15825"></span>

<div id="answer-container-15825" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15825-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can add a column containing the MAC address you want by selecting it in the decode pane and using the popup menu to "Apply as Column". That way you'll get a new column containing the MAC address, which will be exported in the .csv as well.</p><p>Alternatively you can use the Preferences dialog to configure your columns, but it is usually faster to do it from the decode.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '12, 07:31</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-15825" class="comments-container"><span id="15826"></span><div id="comment-15826" class="comment"><div id="post-15826-score" class="comment-score"></div><div class="comment-text"><p>Thanks, The option "Apply as Column" is not available on my Kubuntu version of Wireshark 1.2.7 But via the Preferences dialog I could do it.</p></div><div id="comment-15826-info" class="comment-info"><span class="comment-age">(12 Nov '12, 07:49)</span> Han Koster</div></div><span id="15827"></span><div id="comment-15827" class="comment"><div id="post-15827-score" class="comment-score"></div><div class="comment-text"><p>Correct, the "Apply as Column" option is a feature of v1.6.x IIRC..</p></div><div id="comment-15827-info" class="comment-info"><span class="comment-age">(12 Nov '12, 07:52)</span> Jasper ♦♦</div></div></div><div id="comment-tools-15825" class="comment-tools"></div><div class="clear"></div><div id="comment-15825-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15832"></span>

<div id="answer-container-15832" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15832-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Add a column of type "Hardware src addr" to get the source MAC address.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '12, 11:38</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-15832" class="comments-container"></div><div id="comment-tools-15832" class="comment-tools"></div><div class="clear"></div><div id="comment-15832-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

