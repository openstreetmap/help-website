+++
type = "question"
title = "i got following error during compiling my dissector for windows [fatal error U1073: don&#x27;t know how to make &#x27;packet-tlv.obj&#x27;]"
description = '''Hi,  I had written a dissector to identify my protocol. when compiling it for windows i got following error.please help me to resolve this one. fatal error U1073: don&#x27;t know how to make &#x27;packet-tlv.obj&#x27;  Output:  C: /wireshark /plugins /tlv&amp;gt;nmake -f Makefile.nmake distclean Microsoft (R) Program ...'''
date = "2011-11-17T18:18:00Z"
lastmod = "2011-11-18T06:02:00Z"
weight = 7497
keywords = [ "dissector", "plugin" ]
aliases = [ "/questions/7497" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [i got following error during compiling my dissector for windows \[fatal error U1073: don't know how to make 'packet-tlv.obj'\]](/questions/7497/i-got-following-error-during-compiling-my-dissector-for-windows-fatal-error-u1073-dont-know-how-to-make-packet-tlvobj)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7497-score" class="post-score" title="current number of votes">0</div><span id="post-7497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I had written a dissector to identify my protocol. when compiling it for windows i got following error.please help me to resolve this one.</p><p><strong>fatal error U1073: don't know how to make 'packet-tlv.obj'</strong></p><hr /><p>Output:</p><hr /><p>C: /wireshark /plugins /tlv&gt;nmake -f Makefile.nmake distclean</p><p>Microsoft (R) Program Maintenance Utility Version 9.00.30729.01 Copyright (C) Microsoft Corporation. All rights reserved.</p><pre><code>    rm -f packet-tlv.obj  plugin.obj tlv.res plugin.c *.pdb  tlv.dll tlv.dll</code></pre><p>.manifest tlv.lib tlv.exp tlv.rc</p><p>C: /wireshark /plugins /tlv&gt;nmake -f Makefile.nmake all</p><p>Microsoft (R) Program Maintenance Utility Version 9.00.30729.01 Copyright (C) Microsoft Corporation. All rights reserved.</p><p>NMAKE : fatal error U1073: don't know how to make 'packet-tlv.obj' Stop.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '11, 18:18</strong></p><img src="https://secure.gravatar.com/avatar/01febacc45af8ecf743c4f575d428326?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JK7&#39;s gravatar image" /><p><span>JK7</span><br />
<span class="score" title="31 reputation points">31</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JK7 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Nov '11, 18:23</strong> </span></p></div></div><div id="comments-container-7497" class="comments-container"></div><div id="comment-tools-7497" class="comment-tools"></div><div class="clear"></div><div id="comment-7497-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7502"></span>

<div id="answer-container-7502" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7502-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7502-score" class="post-score" title="current number of votes">0</div><span id="post-7502-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Most likely you have an error in your Makefile.nmake file. Try verifying it against another plugin's Makefile.nmake file, such as gryphon. If it's OK, then try rereading <a href="http://anonsvn.wireshark.org/viewvc/trunk/doc/README.plugins?revision=34921&amp;view=markup">README.plugins</a> and then verify all of your other files as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Nov '11, 06:02</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-7502" class="comments-container"></div><div id="comment-tools-7502" class="comment-tools"></div><div class="clear"></div><div id="comment-7502-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

