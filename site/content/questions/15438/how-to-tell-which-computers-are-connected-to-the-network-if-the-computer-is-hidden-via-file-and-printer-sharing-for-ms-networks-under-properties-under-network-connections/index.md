+++
type = "question"
title = "how to tell which computers are connected to the network if the computer is hidden via &quot;file and printer sharing for ms networks&quot; under properties under network connections"
description = '''how to tell which computers are connected to the network if the computer is hidden via &quot;file and printer sharing for ms networks&quot; under properties under network connections '''
date = "2012-10-31T18:14:00Z"
lastmod = "2012-11-01T02:27:00Z"
weight = 15438
keywords = [ "network" ]
aliases = [ "/questions/15438" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to tell which computers are connected to the network if the computer is hidden via "file and printer sharing for ms networks" under properties under network connections](/questions/15438/how-to-tell-which-computers-are-connected-to-the-network-if-the-computer-is-hidden-via-file-and-printer-sharing-for-ms-networks-under-properties-under-network-connections)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15438-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15438-score" class="post-score" title="current number of votes">0</div><span id="post-15438-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how to tell which computers are connected to the network if the computer is hidden via "file and printer sharing for ms networks" under properties under network connections</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Oct '12, 18:14</strong></p><img src="https://secure.gravatar.com/avatar/b2a4006b4a0252f8be292c57acde97ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wiresharkhelpers&#39;s gravatar image" /><p><span>wiresharkhel...</span><br />
<span class="score" title="30 reputation points">30</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wiresharkhelpers has no accepted answers">0%</span></p></div></div><div id="comments-container-15438" class="comments-container"></div><div id="comment-tools-15438" class="comment-tools"></div><div class="clear"></div><div id="comment-15438-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="15446"></span>

<div id="answer-container-15446" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15446-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15446-score" class="post-score" title="current number of votes">1</div><span id="post-15446-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your question addresses two topics "Which computers" and "file and printer sharing".</p><p>From the network perspective you are probably more looking at hosts. A host can be anything, like a printer, a telephone, a computer or several other things.</p><p>Identifying the computers (i. e. hosts) is easy: Statistics -&gt; Endpoints gets you a list of MAC addresses. Each of address sending data (don't count Broadcast for the moment) translates to one host (or computer, if you don't have network printers, telephones etc).</p><p>Usually you are more interested in the IP addresses used by these computers. The IP addresses are listed in the <strong>IPv4 tab</strong>, you should be able to tell your local addresses from the remote addresses contacted your systems.</p><p>The "file and printer sharing" part probably means, that you want to identify computers running Microsoft Windows, or more generally speaking, computers running the NetBIOS/SMB/CIFS protocol family.</p><p>This protocol family uses the following ports:</p><ul><li>UDP port 137 for NetBIOS name services</li><li>UDP port 138 for NetBIOS datagrams</li><li>TCP port 139 and TCP port 445 for file sharing (NetBIOS sessions)</li></ul><p>Depending on the systems configuration the workstation will announce their presence periodically through one or more protocols, even if they are hidden from your Windows Explorer.</p><p>Just capture traffic for some time and apply the filter <strong>udp.port == 137 or udp.port == 138 or tcp.port == 139 or tcp.port == 445</strong></p><p>Again, use Statistics -&gt; Endpoints -&gt; IPv4 and set a check mark "Limit to display filter". Voila.</p><p>Good hunting!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '12, 01:39</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-15446" class="comments-container"></div><div id="comment-tools-15446" class="comment-tools"></div><div class="clear"></div><div id="comment-15446-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15448"></span>

<div id="answer-container-15448" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15448-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15448-score" class="post-score" title="current number of votes">0</div><span id="post-15448-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>if the computer is hidden via "file and printer sharing for ms networks"</p></blockquote><p>'file and printer sharing' does <strong>not</strong> hide any computer on the network it just makes printers and file shares <strong>available</strong> for others on the network. So, what are you actually looking for?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '12, 02:27</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-15448" class="comments-container"></div><div id="comment-tools-15448" class="comment-tools"></div><div class="clear"></div><div id="comment-15448-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

