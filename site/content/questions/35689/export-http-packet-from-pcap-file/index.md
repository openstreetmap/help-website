+++
type = "question"
title = "export http packet from pcap file"
description = '''hello everybody, I have pcap file that need separate http packets to another pcap file I can do this by GUI, but How can I do that in commandline ? I use gnu/linux distro. Thank you all'''
date = "2014-08-24T04:27:00Z"
lastmod = "2014-08-27T05:20:00Z"
weight = 35689
keywords = [ "export-http" ]
aliases = [ "/questions/35689" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [export http packet from pcap file](/questions/35689/export-http-packet-from-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35689-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35689-score" class="post-score" title="current number of votes">0</div><span id="post-35689-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello everybody, I have pcap file that need separate http packets to another pcap file I can do this by GUI, but How can I do that in commandline ? I use gnu/linux distro. Thank you all</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-export-http" rel="tag" title="see questions tagged &#39;export-http&#39;">export-http</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Aug '14, 04:27</strong></p><img src="https://secure.gravatar.com/avatar/cf7f33aed85508132958f44c08251306?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="linuxuser&#39;s gravatar image" /><p><span>linuxuser</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="linuxuser has no accepted answers">0%</span></p></div></div><div id="comments-container-35689" class="comments-container"></div><div id="comment-tools-35689" class="comment-tools"></div><div class="clear"></div><div id="comment-35689-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35693"></span>

<div id="answer-container-35693" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35693-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35693-score" class="post-score" title="current number of votes">2</div><span id="post-35693-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="linuxuser has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could use tshark to read the file with the "-r" parameter, filter for what you need by using "-R" and writing the results to a new file with "-w", e.g.</p><p>tshark -r original.pcap -R "http" -w httponly.pcap</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '14, 09:43</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-35693" class="comments-container"><span id="35801"></span><div id="comment-35801" class="comment"><div id="post-35801-score" class="comment-score">1</div><div class="comment-text"><p>I found this filter : tshark -R 'tcp.port == 80' -r mypcap.pcap -w all80porttraffic.pcap</p></div><div id="comment-35801-info" class="comment-info"><span class="comment-age">(27 Aug '14, 05:20)</span> <span class="comment-user userinfo">linuxuser</span></div></div></div><div id="comment-tools-35693" class="comment-tools"></div><div class="clear"></div><div id="comment-35693-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

