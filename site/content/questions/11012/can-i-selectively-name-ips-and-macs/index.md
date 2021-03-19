+++
type = "question"
title = "Can I selectively name IPs and MACs?"
description = '''For troubleshooting on a regular basis I would LOVE to right-click on a src or dst addr in EITHER the packet list or packet details pane and name the item and ONLY the item (like an alias). AFAIK this is only currently (1.6.7) available if I edit the hosts file. I do not want to resolve every IP and...'''
date = "2012-05-15T18:44:00Z"
lastmod = "2012-05-16T01:06:00Z"
weight = 11012
keywords = [ "alias", "naming" ]
aliases = [ "/questions/11012" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can I selectively name IPs and MACs?](/questions/11012/can-i-selectively-name-ips-and-macs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11012-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>For troubleshooting on a regular basis I would LOVE to right-click on a src or dst addr in EITHER the packet list or packet details pane and name the item and ONLY the item (like an alias). AFAIK this is only currently (1.6.7) available if I edit the hosts file. I do not want to resolve every IP and I don't want to match MACs to IPs. Please someone tell me I've missed something and there's a button for that. Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">alias naming</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 May '12, 18:44</strong></p><img src="https://secure.gravatar.com/avatar/636ee3cf7f6c87abe47bda876e443c99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bupkes&#39;s gravatar image" /><p>bupkes<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bupkes has no accepted answers">0%</span></p></div></div><div id="comments-container-11012" class="comments-container"></div><div id="comment-tools-11012" class="comment-tools"></div><div class="clear"></div><div id="comment-11012-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11024"></span>

<div id="answer-container-11024" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11024-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can resolve an IP address manually.</p><p>right-click the src or dst IP in the packet list and select "Manullay Resolve Address". That should be available since Wireshark 1.4.</p><blockquote><p><code>I do not want to resolve every IP</code></p></blockquote><p>Unfortunately, you need to enable "Network Address Resolution", for this feature (manual resolve) to work. There is a checkbox for that as well when right-clicking the src/dst.</p><p>Unfortunately, this does not work with MAC addresses, even if you add a src/dst mac column in the packet list. For mac addresses you can use the ethers file:</p><p><strong>Windows:</strong><br />
%APPDATA%\wireshark\ethers</p><p><strong>Unix:</strong><br />
/etc/ethers</p><p><strong>File Format:</strong><br />
mac-address string (name or ip)</p><p><strong>Sample:</strong><br />
00:23:ae:01:02:03 client_mac</p><p><strong>CAUTION:</strong> Windows editors tend to attach .txt to the filename. However the file name must be ethers and <strong>not <a href="http://ethers.txt">ethers.txt</a></strong>.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '12, 01:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 May '12, 01:49</p></div></div><div id="comments-container-11024" class="comments-container"><span id="11137"></span><div id="comment-11137" class="comment"><div id="post-11137-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the answer but I specifically do NOT want to enable automatic resolution.<br />
For anyone trying to track down a problem using Wireshark it seems like this would be high on the list of needs. Renaming IPs and MACs of identified nodes without confusing the issue with enabling any kind of automatic resolution.</p></div><div id="comment-11137-info" class="comment-info"><span class="comment-age">(18 May '12, 10:09)</span> bupkes</div></div><span id="11140"></span><div id="comment-11140" class="comment"><div id="post-11140-score" class="comment-score"></div><div class="comment-text"><p>You might want to file an enhancement request on the Wireshark Bugzilla (<a href="https://bugs.wireshark.org/bugzilla/)">https://bugs.wireshark.org/bugzilla/)</a></p></div><div id="comment-11140-info" class="comment-info"><span class="comment-age">(18 May '12, 15:08)</span> Jim Aragon</div></div></div><div id="comment-tools-11024" class="comment-tools"></div><div class="clear"></div><div id="comment-11024-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

