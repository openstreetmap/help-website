+++
type = "question"
title = "Wireshark to capture 6lowpan packages"
description = '''Hi there, I run ns3 6lowpan example and it created some pcap files. Then I open that file with wireshark but it seems something is wrong. It didn&#x27;t dissect the message. I downloaded sample 6lowpan capture and it seemed well. What am i doing wrong? Thank you for your help. My pcap file : https://www....'''
date = "2016-04-16T04:55:00Z"
lastmod = "2016-07-20T08:58:00Z"
weight = 51716
keywords = [ "6lowpan" ]
aliases = [ "/questions/51716" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark to capture 6lowpan packages](/questions/51716/wireshark-to-capture-6lowpan-packages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51716-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51716-score" class="post-score" title="current number of votes">0</div><span id="post-51716-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>I run ns3 6lowpan example and it created some pcap files. Then I open that file with wireshark but it seems something is wrong. It didn't dissect the message. I downloaded sample 6lowpan capture and it seemed well. What am i doing wrong? Thank you for your help.</p><p>My pcap file : <a href="https://www.cloudshark.org/captures/d0ee8d4cef2e">https://www.cloudshark.org/captures/d0ee8d4cef2e</a></p><p>Sample pcap file: <a href="https://www.cloudshark.org/captures/bf3241f1a282">https://www.cloudshark.org/captures/bf3241f1a282</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-6lowpan" rel="tag" title="see questions tagged &#39;6lowpan&#39;">6lowpan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '16, 04:55</strong></p><img src="https://secure.gravatar.com/avatar/14b50c1494afdd9ee534ceeb46db575b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tarikkarsi&#39;s gravatar image" /><p><span>tarikkarsi</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tarikkarsi has no accepted answers">0%</span></p></div></div><div id="comments-container-51716" class="comments-container"><span id="54191"></span><div id="comment-54191" class="comment"><div id="post-54191-score" class="comment-score"></div><div class="comment-text"><p>Your pcap file with Ethernet encapsulation has an unknown Ethertype of 0xffff. I don't know enough about ns3 to be able to suggest how to correct that though.</p></div><div id="comment-54191-info" class="comment-info"><span class="comment-age">(20 Jul '16, 08:58)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-51716" class="comment-tools"></div><div class="clear"></div><div id="comment-51716-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

