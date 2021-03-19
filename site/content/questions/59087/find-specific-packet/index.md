+++
type = "question"
title = "Find Specific Packet"
description = '''I&#x27;m creating a module for Wireshark and have the first parts of the module all setup where my module looks at the current ongoing TCP connections. The next part of the module will allow the user to analyse an individual connection, for example, see all packets which are part of that connection.  I w...'''
date = "2017-01-26T13:00:00Z"
lastmod = "2017-01-26T13:00:00Z"
weight = 59087
keywords = [ "development", "code", "guide", "tcp" ]
aliases = [ "/questions/59087" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Find Specific Packet](/questions/59087/find-specific-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59087-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm creating a module for Wireshark and have the first parts of the module all setup where my module looks at the current ongoing TCP connections. The next part of the module will allow the user to analyse an individual connection, for example, see all packets which are part of that connection.</p><p>I was wondering if there were any functions/classes which are available to me which could be called to help with this. To be more specific if I had a source IP address and destination IP address is there any way in which to get data on all the packets in that conversation and allow me to print them to a dialog box?</p><p>Please let me know if I have not made things entirely clear.</p><p>Any help would be much appreciated!</p></div><div id="question-tags" class="tags-container tags">development code guide tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jan '17, 13:00</strong></p><img src="https://secure.gravatar.com/avatar/3b7eb282c454b776eac0e960a3798043?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ModuleMan&#39;s gravatar image" /><p>ModuleMan<br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ModuleMan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jan '17, 13:19</p></div></div><div id="comments-container-59087" class="comments-container"><span id="59193"></span><div id="comment-59193" class="comment"><div id="post-59193-score" class="comment-score">1</div><div class="comment-text"><p>Hi, Could you tell us more about how you are writing this module? Is it a C plugin or a LUA plugin?</p><p>Best regards...Paul</p></div><div id="comment-59193-info" class="comment-info"><span class="comment-age">(31 Jan '17, 14:25)</span> PaulOfford</div></div><span id="59194"></span><div id="comment-59194" class="comment"><div id="post-59194-score" class="comment-score"></div><div class="comment-text"><p>Hi Paul,</p><p>I am using C++ for the GUI and I have been implementing the existing GUI methods available to me so far to get a conversation item which the user selects (conv_item_t - similar to the way conversation_dialog.cpp allows filters to be selected).</p><p>Kind regards, ModuleMan</p></div><div id="comment-59194-info" class="comment-info"><span class="comment-age">(31 Jan '17, 14:42)</span> ModuleMan</div></div></div><div id="comment-tools-59087" class="comment-tools"></div><div class="clear"></div><div id="comment-59087-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

