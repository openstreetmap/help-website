+++
type = "question"
title = "Unable to Decode DAP(X.519 Directory Access Protocol) messages using wireshark"
description = '''Hi, I have captured the DAP protocol messages in a file Dumpfile.pcap. I opened the file with Wireshark &amp;amp; used the following filter to filter DAP protocol messages: tcp.srcport == 16602 || tcp.srcport == 16614 || tcp.dstport == 16602 || tcp.dstport == 16614 Where 16602 &amp;amp; 16614 are the TCP po...'''
date = "2012-05-02T03:19:00Z"
lastmod = "2012-05-02T05:49:00Z"
weight = 10579
keywords = [ "x.519", "dap", "tcp" ]
aliases = [ "/questions/10579" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to Decode DAP(X.519 Directory Access Protocol) messages using wireshark](/questions/10579/unable-to-decode-dapx519-directory-access-protocol-messages-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10579-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have captured the DAP protocol messages in a file Dumpfile.pcap. I opened the file with Wireshark &amp; used the following filter to filter DAP protocol messages:</p><p>tcp.srcport == 16602 || tcp.srcport == 16614 || tcp.dstport == 16602 || tcp.dstport == 16614</p><p>Where 16602 &amp; 16614 are the TCP ports used for DAP protocol.</p><p>Then I went to wiresharks "Analyze" menu &amp; selected the Option "Decode As". In this "Transport" TAB I have choosen TCP "both" ports &amp; tried to select the "DAP" protocol. But there is no DAP protocol available. only LDAP was available.</p><p>Please suggest how can I decode DAP protocol messages using wireshark?</p><p>Additional Info: When I select the "Follow TCP stream" option in Analyze menu I was able to see contents of DAP query. But it is not clear.</p></div><div id="question-tags" class="tags-container tags">x.519 dap tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '12, 03:19</strong></p><img src="https://secure.gravatar.com/avatar/6d3141b7be0500208a8e696a149b519a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ramakrishna&#39;s gravatar image" /><p>Ramakrishna<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ramakrishna has no accepted answers">0%</span></p></div></div><div id="comments-container-10579" class="comments-container"></div><div id="comment-tools-10579" class="comment-tools"></div><div class="clear"></div><div id="comment-10579-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10593"></span>

<div id="answer-container-10593" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10593-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The DAP dissector has a preference (Edit-&gt;Preferences-&gt;Protocols-&gt;OSI-&gt;X.500-&gt;DAP, yikes that was hard to find!) where you can set the TCP port used for this protocol. Setting that also has the advantage that the setting is persistent.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '12, 05:49</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-10593" class="comments-container"></div><div id="comment-tools-10593" class="comment-tools"></div><div class="clear"></div><div id="comment-10593-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

