+++
type = "question"
title = "Header checksum Error even when Disabling checksum validation in Wireshark"
description = '''Hi all , i need your help please , i sniffed my packets and saw many error evrey seconds , i read about it and saw it excaly match the problem with checksum validation in Wireshark. i turn it off and still it doesn&#x27;t go away , i still see all Red packets in my network. any Suggestions?'''
date = "2013-03-03T22:46:00Z"
lastmod = "2013-03-04T05:56:00Z"
weight = 19116
keywords = [ "checksum", "validation", "error" ]
aliases = [ "/questions/19116" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Header checksum Error even when Disabling checksum validation in Wireshark](/questions/19116/header-checksum-error-even-when-disabling-checksum-validation-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19116-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19116-score" class="post-score" title="current number of votes">0</div><span id="post-19116-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all ,</p><p>i need your help please , i sniffed my packets and saw many error evrey seconds , i read about it and saw it excaly match the problem with checksum validation in Wireshark. i turn it off and still it doesn't go away , i still see all Red packets in my network. any Suggestions?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-checksum" rel="tag" title="see questions tagged &#39;checksum&#39;">checksum</span> <span class="post-tag tag-link-validation" rel="tag" title="see questions tagged &#39;validation&#39;">validation</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Mar '13, 22:46</strong></p><img src="https://secure.gravatar.com/avatar/7546a5dc6967574e6c3c9923ace6240e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alon%20Fox&#39;s gravatar image" /><p><span>Alon Fox</span><br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alon Fox has no accepted answers">0%</span></p></div></div><div id="comments-container-19116" class="comments-container"></div><div id="comment-tools-19116" class="comment-tools"></div><div class="clear"></div><div id="comment-19116-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19117"></span>

<div id="answer-container-19117" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19117-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19117-score" class="post-score" title="current number of votes">1</div><span id="post-19117-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Red packets matched a specific coloring rule and so were colored that way. To find out which coloring rule a particular packet matched, you can expand the Frame in the packet details and look for the name and rule string. For example:</p><pre><code>[-] Frame 6: 60 bytes on wire (480 bits), 60 bytes captured (480 bits)
      Encapsulation type: Ethernet (1)
      ...
      [Protocols in frame: eth:ip:tcp]
      [Coloring Rule Name: Bad TCP]
      [Coloring Rule String: tcp.analysis.flags]</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Mar '13, 23:16</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-19117" class="comments-container"><span id="19118"></span><div id="comment-19118" class="comment"><div id="post-19118-score" class="comment-score"></div><div class="comment-text"><p>HI , I have diffrent types of error when i sniffed .the most common is the third ,and the checksum error come from my nic ,but the checksum validation in Wireshark is not enabled .</p><p>First:</p><pre><code>[Protocols in frame: eth:ip:tcp]
      [Coloring Rule Name: Bad TCP]
      [Coloring Rule String: tcp.analysis.flags]</code></pre><p>Second:</p><pre><code>[Protocols in frame: eth:ip:tcp:http:data]
      [Coloring Rule Name: Bad TCP]
      [Coloring Rule String: tcp.analysis.flags]</code></pre><p>third:</p><pre><code>[Protocols in frame: eth:ip:tcp]
[Coloring Rule Name: checksum Errors]
Coloring Rule String: cdp.checksum_bad==1 || edp.checksum_bad==1 || ip.checksum_bad==1 || tcp.checksum_bad==1 || udp.checksum_bad==1 || mstp.checksum_bad==1</code></pre></div><div id="comment-19118-info" class="comment-info"><span class="comment-age">(03 Mar '13, 23:59)</span> <span class="comment-user userinfo">Alon Fox</span></div></div><span id="19121"></span><div id="comment-19121" class="comment"><div id="post-19121-score" class="comment-score"></div><div class="comment-text"><p>As you can see, the same coloring rule is applied for multiple cases of checksum errors. Since the packet contains both IP and TCP data, it's likely that you only disabled IP checksum validation or TCP checksum validation, but not both.</p></div><div id="comment-19121-info" class="comment-info"><span class="comment-age">(04 Mar '13, 05:56)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-19117" class="comment-tools"></div><div class="clear"></div><div id="comment-19117-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

