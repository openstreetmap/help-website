+++
type = "question"
title = "creating pcap with multiple packets"
description = '''I have a binary file that I want to convert to a pcap file. I did a hexdump and then converted to a pcap using text2pcap. But there are multiple packets(custom protocol, custom dissector) in that binary file. How do I use hexdump to delineate different packets so that my pcap file has multiple packe...'''
date = "2011-06-13T12:37:00Z"
lastmod = "2011-06-13T14:14:00Z"
weight = 4543
keywords = [ "hexdump", "pcap" ]
aliases = [ "/questions/4543" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [creating pcap with multiple packets](/questions/4543/creating-pcap-with-multiple-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4543-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4543-score" class="post-score" title="current number of votes">0</div><span id="post-4543-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a binary file that I want to convert to a pcap file. I did a hexdump and then converted to a pcap using text2pcap. But there are multiple packets(custom protocol, custom dissector) in that binary file. How do I use hexdump to delineate different packets so that my pcap file has multiple packets??</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-hexdump" rel="tag" title="see questions tagged &#39;hexdump&#39;">hexdump</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jun '11, 12:37</strong></p><img src="https://secure.gravatar.com/avatar/25b19db92f6c5c1102813db491e41432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tut087&#39;s gravatar image" /><p><span>tut087</span><br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tut087 has no accepted answers">0%</span></p></div></div><div id="comments-container-4543" class="comments-container"></div><div id="comment-tools-4543" class="comment-tools"></div><div class="clear"></div><div id="comment-4543-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4545"></span>

<div id="answer-container-4545" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4545-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4545-score" class="post-score" title="current number of votes">1</div><span id="post-4545-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The different packets are tracked through their offset:</p><blockquote><p>An offset of zero is indicative of starting a new packet, so a single text file with a series of hexdumps can be converted into a packet capture with multiple packets.</p></blockquote><p>See the section in the <a href="http://www.wireshark.org/docs/wsug_html_chunked/AppToolstext2pcap.html">User's Guide</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '11, 13:50</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-4545" class="comments-container"><span id="4548"></span><div id="comment-4548" class="comment"><div id="post-4548-score" class="comment-score"></div><div class="comment-text"><p>Thanks. When I create ahexdump. offset of zero comes in the beginning only. So do I have to manually change it? Or is there a method to produce a zero offset after regular byte interval?</p></div><div id="comment-4548-info" class="comment-info"><span class="comment-age">(13 Jun '11, 14:14)</span> <span class="comment-user userinfo">tut087</span></div></div></div><div id="comment-tools-4545" class="comment-tools"></div><div class="clear"></div><div id="comment-4545-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

