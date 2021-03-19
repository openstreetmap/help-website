+++
type = "question"
title = "Convert .pcap using dumpcap"
description = '''Hi, I&#x27;m Automatically capturing logs in .pcap format using below command dumpcap.exe -i 4 -a files:3 -a filesize:5 -w test.pcap how can convert this files to .txt format automatically using dumpcap command.... '''
date = "2013-03-02T20:55:00Z"
lastmod = "2013-03-03T17:23:00Z"
weight = 19099
keywords = [ "convert", "dumpcap", ".pcap" ]
aliases = [ "/questions/19099" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Convert .pcap using dumpcap](/questions/19099/convert-pcap-using-dumpcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19099-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19099-score" class="post-score" title="current number of votes">0</div><span id="post-19099-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm Automatically capturing logs in .pcap format using below command <strong>dumpcap.exe -i 4 -a files:3 -a filesize:5 -w test.pcap</strong></p><p>how can convert this files to .txt format automatically using dumpcap command....</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-convert" rel="tag" title="see questions tagged &#39;convert&#39;">convert</span> <span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span> <span class="post-tag tag-link-.pcap" rel="tag" title="see questions tagged &#39;.pcap&#39;">.pcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Mar '13, 20:55</strong></p><img src="https://secure.gravatar.com/avatar/47050f603ff32c64a34a83fe723500b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Irsh&#39;s gravatar image" /><p><span>Irsh</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Irsh has no accepted answers">0%</span></p></div></div><div id="comments-container-19099" class="comments-container"></div><div id="comment-tools-19099" class="comment-tools"></div><div class="clear"></div><div id="comment-19099-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19101"></span>

<div id="answer-container-19101" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19101-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19101-score" class="post-score" title="current number of votes">0</div><span id="post-19101-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>dumpcap always writes pcapng or pcap files by default, depending on the version of the executable, so the "logs" are always in a binary format. No way around that. If you need text files you can try to use tshark to display decoded data after it has been written to disk, or you could use Wireshark to export the packets to decoded .txt format manually.</p><p>Why do you need .txt format anyway? Usually it is more useful to have the binary format since it can be worked with much easier.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Mar '13, 05:02</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Mar '13, 05:03</strong> </span></p></div></div><div id="comments-container-19101" class="comments-container"><span id="19102"></span><div id="comment-19102" class="comment"><div id="post-19102-score" class="comment-score"></div><div class="comment-text"><p>Hi, I'm Running a program where certain data comes in hidden format where wireshark Picks. What I want is to get that data to another Program .... can I use tshark to achieve this ? If so... what is the command please. Thanks</p></div><div id="comment-19102-info" class="comment-info"><span class="comment-age">(03 Mar '13, 08:17)</span> <span class="comment-user userinfo">Irsh</span></div></div><span id="19110"></span><div id="comment-19110" class="comment"><div id="post-19110-score" class="comment-score"></div><div class="comment-text"><p>what do you mean by "hidden format"? Sounds like Wireshark/Tshark just do not have dissectors for it - if so, you'll be stuck with undecoded bytes either way.</p><p>So do I get this correctly - you want to extract payload bytes that Wireshark/TShark does not decode?</p></div><div id="comment-19110-info" class="comment-info"><span class="comment-age">(03 Mar '13, 17:23)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-19101" class="comment-tools"></div><div class="clear"></div><div id="comment-19101-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

