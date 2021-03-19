+++
type = "question"
title = "File too big?"
description = '''Dear Wireshark-community, I have captured a file from my Fritzbox (fritzbox-vcc0.eth with a size of 1.3 GB). When I try to open the file Wireshark (version 1.12.7) gives following error-note: The capture file appears to be damaged or corrupt. (pcap: File has 875560560-byte packet, bigger than maximu...'''
date = "2015-08-18T16:30:00Z"
lastmod = "2015-08-18T23:52:00Z"
weight = 45221
keywords = [ "bigger_than_maximum" ]
aliases = [ "/questions/45221" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [File too big?](/questions/45221/file-too-big)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45221-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45221-score" class="post-score" title="current number of votes">0</div><span id="post-45221-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear Wireshark-community, I have captured a file from my Fritzbox (fritzbox-vcc0.eth with a size of 1.3 GB). When I try to open the file Wireshark (version 1.12.7) gives following error-note:</p><p>The capture file appears to be damaged or corrupt. (pcap: File has 875560560-byte packet, bigger than maximum of 262144)</p><p>When I try to analyze the phone-calls (Telephony - RTP - Show all streams) the programm does not find any stream though I made some phone-calls myself.</p><p>According to the error-note I assume that the file is too big. Is there a way to split the file into smaller ones which can be read by Wireshark? Or is there another way to solve the problem?</p><p>Thank you in advance T</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bigger_than_maximum" rel="tag" title="see questions tagged &#39;bigger_than_maximum&#39;">bigger_than_maximum</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '15, 16:30</strong></p><img src="https://secure.gravatar.com/avatar/b649fde160aa85b05c98141ac2f95563?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Martin_Brody&#39;s gravatar image" /><p><span>Martin_Brody</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Martin_Brody has no accepted answers">0%</span></p></div></div><div id="comments-container-45221" class="comments-container"><span id="45229"></span><div id="comment-45229" class="comment"><div id="post-45229-score" class="comment-score"></div><div class="comment-text"><p>So how did you transfer the capture the file from the FRITZ!Box to your machine? And what operating system is your machine running? The most likely reasons for this are either that the FRITZ!Box wrote out a damaged capture file or that it got damaged in the process of transferring it to your machine.</p></div><div id="comment-45229-info" class="comment-info"><span class="comment-age">(18 Aug '15, 23:52)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-45221" class="comment-tools"></div><div class="clear"></div><div id="comment-45221-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45222"></span>

<div id="answer-container-45222" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45222-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45222-score" class="post-score" title="current number of votes">0</div><span id="post-45222-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds more like there is at least one packet in the file that has a broken/damaged frame size value in the frame header meta data. You might want to try to fix the problem using <a href="https://f00l.de/pcapfix/">pcapfix</a>.</p><p>If you want to split capture files into smaller files, use editcap (command line tool, installed together with Wireshark), e.g.</p><p><code>editcap -c 100000 in.pcap out.pcap</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Aug '15, 16:35</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-45222" class="comments-container"></div><div id="comment-tools-45222" class="comment-tools"></div><div class="clear"></div><div id="comment-45222-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

