+++
type = "question"
title = "bogus ipv4 with ver 2.0.1"
description = '''I just downloaded version 2.0.1. I have a pcap that works in Wireshark version 1.12.9 but gives me bogus IPv4 in version 2.0.1. I can read other pcaps in 2.0.1 which have both ipv4 and 6, but this one is giving me trouble. I have attached a couple of screenshots. Not sure if the screenshots will wor...'''
date = "2016-02-04T08:26:00Z"
lastmod = "2016-02-04T11:32:00Z"
weight = 49829
keywords = [ "version", "bogus", "2.0.1", "ipv4" ]
aliases = [ "/questions/49829" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [bogus ipv4 with ver 2.0.1](/questions/49829/bogus-ipv4-with-ver-201)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49829-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49829-score" class="post-score" title="current number of votes">0</div><span id="post-49829-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just downloaded version 2.0.1. I have a pcap that works in Wireshark version 1.12.9 but gives me bogus IPv4 in version 2.0.1. I can read other pcaps in 2.0.1 which have both ipv4 and 6, but this one is giving me trouble. I have attached a couple of screenshots. Not sure if the screenshots will work or not since this is the first question I have ever asked. Appreciate any assistance.</p><p>Here is a link to a single packet pcap <a href="https://drive.google.com/open?id=0B6xDWNlkBv4CTEo3RzdKS2hiYW8.">https://drive.google.com/open?id=0B6xDWNlkBv4CTEo3RzdKS2hiYW8.</a></p><p><img src="https://osqa-ask.wireshark.org/upfiles/imsi_311480060671752_160122_0943.jpg" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/imsi_311480060671752_160122_0943.pcap_%5BWireshark_1.12.9_(v1.12.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-version" rel="tag" title="see questions tagged &#39;version&#39;">version</span> <span class="post-tag tag-link-bogus" rel="tag" title="see questions tagged &#39;bogus&#39;">bogus</span> <span class="post-tag tag-link-2.0.1" rel="tag" title="see questions tagged &#39;2.0.1&#39;">2.0.1</span> <span class="post-tag tag-link-ipv4" rel="tag" title="see questions tagged &#39;ipv4&#39;">ipv4</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '16, 08:26</strong></p><img src="https://secure.gravatar.com/avatar/8ec5421aba59ad66d9e7c135a3b31c31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bmwdad&#39;s gravatar image" /><p><span>bmwdad</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bmwdad has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Feb '16, 10:48</strong> </span></p></div></div><div id="comments-container-49829" class="comments-container"><span id="49832"></span><div id="comment-49832" class="comment"><div id="post-49832-score" class="comment-score"></div><div class="comment-text"><p>Could you share a pcap file? A single packet should be sufficient.</p><p>This code part was reworked between Wireshark 1.12.9 and 2.0.1, but the decoding should still be the same. If you provide a sample capture quickly I should be able to look at it and eventually fix the bug before Wireshark 2.0.2 is released.</p></div><div id="comment-49832-info" class="comment-info"><span class="comment-age">(04 Feb '16, 08:46)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="49833"></span><div id="comment-49833" class="comment"><div id="post-49833-score" class="comment-score"></div><div class="comment-text"><p>The usual issue with trying to debug screenshots, the bit we'd like to see isn't displayed. The contents of the Null/Loopback part of the tree are interesting as that's where the subsequent protocol is determined.</p><p>A capture file would allow direct examination, could you supply one? You can slice the capture file after the IP header if privacy is an issue.</p></div><div id="comment-49833-info" class="comment-info"><span class="comment-age">(04 Feb '16, 09:07)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="49835"></span><div id="comment-49835" class="comment"><div id="post-49835-score" class="comment-score"></div><div class="comment-text"><p>I do not see a method to attach a pcap to the question. I have responded in email to Pascal with a pcap.</p></div><div id="comment-49835-info" class="comment-info"><span class="comment-age">(04 Feb '16, 09:51)</span> <span class="comment-user userinfo">bmwdad</span></div></div><span id="49836"></span><div id="comment-49836" class="comment"><div id="post-49836-score" class="comment-score"></div><div class="comment-text"><p>To share a pcap, put in in a publicly shared place, e.g. Google Drive, Dropbox etc. and edit the original question with a link to the file.</p></div><div id="comment-49836-info" class="comment-info"><span class="comment-age">(04 Feb '16, 09:57)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="49838"></span><div id="comment-49838" class="comment"><div id="post-49838-score" class="comment-score"></div><div class="comment-text"><p>I did not receive an email. Please consider uploading the file on one of the site suggested by Graham. Thanks.</p></div><div id="comment-49838-info" class="comment-info"><span class="comment-age">(04 Feb '16, 10:14)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="49848"></span><div id="comment-49848" class="comment not_top_scorer"><div id="post-49848-score" class="comment-score"></div><div class="comment-text"><p>I have updated the original question with a link to a pcap</p></div><div id="comment-49848-info" class="comment-info"><span class="comment-age">(04 Feb '16, 11:05)</span> <span class="comment-user userinfo">bmwdad</span></div></div></div><div id="comment-tools-49829" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-49829-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49851"></span>

<div id="answer-container-49851" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49851-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49851-score" class="post-score" title="current number of votes">0</div><span id="post-49851-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your capture is using an Ethertype IPv4 (0x0800) while encapsulating an IPv6 packet.</p><p>Wireshark versions up to 1.12.X allowed this but Wireshark 2.0.X strengthens the checks and consider this as an error. Your application doing the capture should use an ethertype IPv6 (0x86DD) instead.</p><p>In the meantime, you can force the dissection as IPv6 by using 'Decode As' functionality and force dissection of Ethertype 0x0800 as IPv6. But this will break dissection of standard Ethernet packets for example, so use this with caution.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '16, 11:32</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Feb '16, 11:32</strong> </span></p></div></div><div id="comments-container-49851" class="comments-container"></div><div id="comment-tools-49851" class="comment-tools"></div><div class="clear"></div><div id="comment-49851-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

