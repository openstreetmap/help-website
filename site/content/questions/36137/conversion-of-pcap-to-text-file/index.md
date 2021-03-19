+++
type = "question"
title = "conversion of pcap to text file"
description = '''Hi  I am using wireshark version 1.0.2 in unix.I Want to convert pcap to text file using command  &quot;tshark -r filename.pcap -O tcp -x &amp;gt; filename.txt&quot;,but the command is not working for me. Could you please tell me what command I should give to make it work in wireshark 1.0.2 version. Thanks Ram'''
date = "2014-09-09T22:59:00Z"
lastmod = "2014-09-10T07:47:00Z"
weight = 36137
keywords = [ "command-line" ]
aliases = [ "/questions/36137" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [conversion of pcap to text file](/questions/36137/conversion-of-pcap-to-text-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36137-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I am using wireshark version 1.0.2 in unix.I Want to convert pcap to text file using command "tshark -r filename.pcap -O tcp -x &gt; filename.txt",but the command is not working for me.</p><p>Could you please tell me what command I should give to make it work in wireshark 1.0.2 version.</p><p>Thanks Ram</p></div><div id="question-tags" class="tags-container tags">command-line</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Sep '14, 22:59</strong></p><img src="https://secure.gravatar.com/avatar/7343ee112ff5ce3e89c692e5b9acdf93?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ramkumarbarai&#39;s gravatar image" /><p>ramkumarbarai<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ramkumarbarai has no accepted answers">0%</span></p></div></div><div id="comments-container-36137" class="comments-container"></div><div id="comment-tools-36137" class="comment-tools"></div><div class="clear"></div><div id="comment-36137-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36172"></span>

<div id="answer-container-36172" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36172-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The <code>-O</code> option was only introduced in Wireshark 1.6.0 so you can't use that in version 1.0.2 (assuming that wasn't a typo).</p><p>In 1.0.2 you'll have to do something like <code>tshark -r filename.pcap -V -x &gt; filename.txt</code>. "-V" will decode/expand all the protocol layers, though. If you want just TCP to be expanded you'll need to upgrade.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '14, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-36172" class="comments-container"></div><div id="comment-tools-36172" class="comment-tools"></div><div class="clear"></div><div id="comment-36172-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

