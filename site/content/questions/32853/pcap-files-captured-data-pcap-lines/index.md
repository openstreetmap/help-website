+++
type = "question"
title = "Pcap files : Captured Data + pcap lines"
description = '''Hi there, I&#x27;m just wondering how much size of .pcap file is the data captured by the application form the interface, and how much of it is for the pcap format itself. Could someone help me, please? Thanks'''
date = "2014-05-17T00:53:00Z"
lastmod = "2014-05-17T22:43:00Z"
weight = 32853
keywords = [ "pcap" ]
aliases = [ "/questions/32853" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Pcap files : Captured Data + pcap lines](/questions/32853/pcap-files-captured-data-pcap-lines)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32853-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32853-score" class="post-score" title="current number of votes">0</div><span id="post-32853-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there, I'm just wondering how much size of .pcap file is the data captured by the application form the interface, and how much of it is for the pcap format itself. Could someone help me, please?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '14, 00:53</strong></p><img src="https://secure.gravatar.com/avatar/07da332d5eb4e9d3e3c205c281a4d003?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="abd&#39;s gravatar image" /><p><span>abd</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="abd has no accepted answers">0%</span></p></div></div><div id="comments-container-32853" class="comments-container"><span id="32861"></span><div id="comment-32861" class="comment"><div id="post-32861-score" class="comment-score">1</div><div class="comment-text"><p>You're referring to pcap files, not pcap-ng files, right? The general convention is that pcap-ng files should have the file suffix .pcapng, but nothing <em>requires</em> that they do.</p><p>Wireshark, by default, writes pcap-ng files.</p></div><div id="comment-32861-info" class="comment-info"><span class="comment-age">(17 May '14, 13:35)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-32853" class="comment-tools"></div><div class="clear"></div><div id="comment-32853-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32856"></span>

<div id="answer-container-32856" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32856-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32856-score" class="post-score" title="current number of votes">2</div><span id="post-32856-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="abd has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>you can find a description of the pcap format <a href="http://wiki.wireshark.org/Development/LibpcapFileFormat">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '14, 07:05</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-32856" class="comments-container"><span id="32859"></span><div id="comment-32859" class="comment"><div id="post-32859-score" class="comment-score"></div><div class="comment-text"><p>Thank you Pascal Quantin. But I'm a bit confused here. You mean I should read the number of packets wiresharke has captured and then x with the size of headers(in Byte)? What's the size of each header?</p></div><div id="comment-32859-info" class="comment-info"><span class="comment-age">(17 May '14, 12:55)</span> <span class="comment-user userinfo">abd</span></div></div><span id="32860"></span><div id="comment-32860" class="comment"><div id="post-32860-score" class="comment-score"></div><div class="comment-text"><p>No. Read the number of frames in the capture, substract that number x size of PCAP frame headers in bytes, and substract pcap file header once.</p></div><div id="comment-32860-info" class="comment-info"><span class="comment-age">(17 May '14, 13:19)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="32866"></span><div id="comment-32866" class="comment"><div id="post-32866-score" class="comment-score"></div><div class="comment-text"><p>Gotcha. You mean 5 guint32 + 2 guint16 = 24Byte for Global header, and 4 guint32 = 16Byte for each packet.</p><p>Thanks</p></div><div id="comment-32866-info" class="comment-info"><span class="comment-age">(17 May '14, 22:43)</span> <span class="comment-user userinfo">abd</span></div></div></div><div id="comment-tools-32856" class="comment-tools"></div><div class="clear"></div><div id="comment-32856-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

