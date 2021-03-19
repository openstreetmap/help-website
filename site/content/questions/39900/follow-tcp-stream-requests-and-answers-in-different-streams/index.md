+++
type = "question"
title = "Follow TCP stream, requests and answers in different streams"
description = '''Hello. I&#x27;m trying to analyze some HTTP trafic, in the older version of wireshark, requests and responses were displayed in the same window, but after an update I can only see requests or only responses, they are in different streams for some reason.'''
date = "2015-02-16T21:58:00Z"
lastmod = "2015-02-17T14:50:00Z"
weight = 39900
keywords = [ "follow.tcp.stream" ]
aliases = [ "/questions/39900" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Follow TCP stream, requests and answers in different streams](/questions/39900/follow-tcp-stream-requests-and-answers-in-different-streams)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39900-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39900-score" class="post-score" title="current number of votes">0</div><span id="post-39900-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello. I'm trying to analyze some HTTP trafic, in the older version of wireshark, requests and responses were displayed in the same window, but after an update I can only see requests or only responses, they are in different streams for some reason.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-follow.tcp.stream" rel="tag" title="see questions tagged &#39;follow.tcp.stream&#39;">follow.tcp.stream</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '15, 21:58</strong></p><img src="https://secure.gravatar.com/avatar/b38f9c32ab6aecea6d748c4b2070331a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="blaine&#39;s gravatar image" /><p><span>blaine</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="blaine has no accepted answers">0%</span></p></div></div><div id="comments-container-39900" class="comments-container"><span id="39904"></span><div id="comment-39904" class="comment"><div id="post-39904-score" class="comment-score"></div><div class="comment-text"><p>Which version of wireshark were you using when it still worked and which version are you using now?</p><p>If you can supply the capture file (on <a href="https://appliance.cloudshark.org/upload/">Cloudshark</a> for instance), that would be great. You can anonimize the file with <a href="https://www.tracewrangler.com/">TraceWrangler</a> if you need to remove the ip addresses and/or the TCP payload of the packets.</p></div><div id="comment-39904-info" class="comment-info"><span class="comment-age">(17 Feb '15, 00:31)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="39915"></span><div id="comment-39915" class="comment"><div id="post-39915-score" class="comment-score"></div><div class="comment-text"><p>here it is: <a href="https://www.cloudshark.org/captures/28457348b590">https://www.cloudshark.org/captures/28457348b590</a></p><p>I don't remember what version it was exactly, but it was few months ago. I needed to see why something isn't working so I launched wireshark, and it requested an update, I updated and...</p></div><div id="comment-39915-info" class="comment-info"><span class="comment-age">(17 Feb '15, 08:08)</span> <span class="comment-user userinfo">blaine</span></div></div></div><div id="comment-tools-39900" class="comment-tools"></div><div class="clear"></div><div id="comment-39900-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39918"></span>

<div id="answer-container-39918" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39918-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39918-score" class="post-score" title="current number of votes">1</div><span id="post-39918-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>but after an update I can only see requests or only responses, they are in different streams for some reason.</p></blockquote><p>this is (most certainly) not a Wireshark issue, but an issue with the capture file. Take a look at frame #1 and frame #2 and you'll realize that the capture file (most certainly) has been modified with some tools and something went wrong.</p><p>Reasons:</p><p>Frame #1: SEQ = 4259920039<br />
Frame #2: ACK = 4259920040</p><p>So, frame #2 is (most certainly) the SYN-ACK for the SYN in frame #1, however with <strong>different source ports</strong>.</p><p>Furthermore, the src-mac and dst-mac in frame #2 is IDENTICAL !?! Same for other frames...</p><p>My conclusion: This capture file has been run through an pcap anonymization tool and something went wrong.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '15, 14:50</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Feb '15, 14:53</strong> </span></p></div></div><div id="comments-container-39918" class="comments-container"></div><div id="comment-tools-39918" class="comment-tools"></div><div class="clear"></div><div id="comment-39918-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

