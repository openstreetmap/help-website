+++
type = "question"
title = "network type 12 unknown or unsupported"
description = '''The file &quot;test.cap&quot; is a capture for a network type that Wire shark doesn&#x27;t support. (snoop: network type 12 unknown or unsupported) I tried to read test.cap file but i am not able to read it. could anyone help me on this?'''
date = "2013-11-18T03:54:00Z"
lastmod = "2013-11-18T10:17:00Z"
weight = 27066
keywords = [ "capture-file" ]
aliases = [ "/questions/27066" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [network type 12 unknown or unsupported](/questions/27066/network-type-12-unknown-or-unsupported)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27066-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The file "test.cap" is a capture for a network type that Wire shark doesn't support. (snoop: network type 12 unknown or unsupported) I tried to read test.cap file but i am not able to read it. could anyone help me on this?</p></div><div id="question-tags" class="tags-container tags">capture-file</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '13, 03:54</strong></p><img src="https://secure.gravatar.com/avatar/d1445373e43dc1a4c5a4545279a3aebd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Muthu%20Kumar&#39;s gravatar image" /><p>Muthu Kumar<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Muthu Kumar has no accepted answers">0%</span></p></div></div><div id="comments-container-27066" class="comments-container"></div><div id="comment-tools-27066" class="comment-tools"></div><div class="clear"></div><div id="comment-27066-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27071"></span>

<div id="answer-container-27071" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27071-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Apparently you have a snoop-like capture file with a format that is not (yet) supported by Wireshark. Please file a bug report at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> and add as much information as possible</p><ul><li>Tool name and version</li><li>Wireshark version</li><li>OS and version you tested with</li><li>IMPORTANT: a small sample capture file</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Nov '13, 10:17</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-27071" class="comments-container"><span id="27075"></span><div id="comment-27075" class="comment"><div id="post-27075-score" class="comment-score"></div><div class="comment-text"><p>Yes, type 12 is listed on <a href="http://www.iana.org/assignments/snoop-datalink-types/snoop-datalink-types.xhtml">the IANA page for snoop network types</a> as being reserved. <a href="http://pubs.opengroup.org/onlinepubs/009638599/apdxf.htm">The DLPI specification's dlpi.h</a> lists it as <code>DL_ASYNC</code>, for "Character Asynchronous Protocol", with no indication of what that means.</p><p>So please do as Kurt suggests; otherwise, we won't be able to figure out what that network type means.</p></div><div id="comment-27075-info" class="comment-info"><span class="comment-age">(18 Nov '13, 11:45)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-27071" class="comment-tools"></div><div class="clear"></div><div id="comment-27071-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

