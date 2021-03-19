+++
type = "question"
title = "Data Structure of address defined in address.h"
description = '''Hello! I want to put the protocol information which is dissected by Wireshark into SQL Server. Now I am planning to add codes in the function of add_packet_to_packet_list in file.c. And the place to insert new codes is somewhere after the line of  row = packet_list_append(cinfo, fdata, &amp;amp;edt.pi);...'''
date = "2013-07-05T00:36:00Z"
lastmod = "2013-07-07T10:58:00Z"
weight = 22683
keywords = [ "src", "ip.src" ]
aliases = [ "/questions/22683" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Data Structure of address defined in address.h](/questions/22683/data-structure-of-address-defined-in-addressh)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22683-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello! I want to put the protocol information which is dissected by Wireshark into SQL Server. Now I am planning to add codes in the function of <code>add_packet_to_packet_list</code> in <code>file.c</code>. And the place to insert new codes is somewhere after the line of</p><pre><code>    row = packet_list_append(cinfo, fdata, &amp;edt.pi);</code></pre><p>I have figured out that the row equals to the column number minus one. However, I could not print out the source address and destination address. The parameter <code>&amp;edt.pi</code> is used to save the protocol tree information including the src address and dst address. And I have noticed that for the parameter <code>edt.pi.dl_src.data</code>, its type is <code>const void *</code>. How could I get the string type of source address from this parameter? I am very confused. So Would you like to help me make it out? Thank you very much!</p></div><div id="question-tags" class="tags-container tags">src ip.src</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jul '13, 00:36</strong></p><img src="https://secure.gravatar.com/avatar/df5946b250ac0802ce044aef61aa1402?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="constance&#39;s gravatar image" /><p>constance<br />
<span class="score" title="10 reputation points">10</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="constance has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Jul '13, 11:00</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-22683" class="comments-container"></div><div id="comment-tools-22683" class="comment-tools"></div><div class="clear"></div><div id="comment-22683-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22703"></span>

<div id="answer-container-22703" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22703-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Its type is <code>const void *</code> because it points to a blob of address-type-dependent binary data.</p><p>If you want a human-readable text form for the address, you would have to use one of the <code>address_to_str</code> functions declared in <code>epan/to_str.h</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jul '13, 10:58</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-22703" class="comments-container"><span id="22780"></span><div id="comment-22780" class="comment"><div id="post-22780-score" class="comment-score"></div><div class="comment-text"><p>Thank you! I have solved this problem by printing out ip_to_str( (const guint8 *)edt.pi.net_src.data) if it's an IPV4 address.</p></div><div id="comment-22780-info" class="comment-info"><span class="comment-age">(09 Jul '13, 21:19)</span> constance</div></div></div><div id="comment-tools-22703" class="comment-tools"></div><div class="clear"></div><div id="comment-22703-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

