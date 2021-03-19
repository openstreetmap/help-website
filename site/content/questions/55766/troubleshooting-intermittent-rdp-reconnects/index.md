+++
type = "question"
title = "Troubleshooting intermittent RDP reconnects"
description = '''Hi, I`m trying to find out what is causing intermittent RDP reconnects on our network. We connect via a RDP gateway proxy (which runs over HTTS / port 443). We reach the server via internet. It is not hosted in our LAN. I notice some &#x27;TCP Previous segment not captured&#x27; followed by TCK ACKed unsem se...'''
date = "2016-09-22T15:28:00Z"
lastmod = "2016-09-25T05:45:00Z"
weight = 55766
keywords = [ "rdp" ]
aliases = [ "/questions/55766" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Troubleshooting intermittent RDP reconnects](/questions/55766/troubleshooting-intermittent-rdp-reconnects)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55766-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55766-score" class="post-score" title="current number of votes">0</div><span id="post-55766-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I`m trying to find out what is causing intermittent RDP reconnects on our network. We connect via a RDP gateway proxy (which runs over HTTS / port 443). We reach the server via internet. It is not hosted in our LAN.</p><p>I notice some 'TCP Previous segment not captured' followed by TCK ACKed unsem segment. I captured all traffic going to the RDP gateway using our PFsense router. From what I read, these notices are nothing to worry about.</p><p>I`m a bit stuck, because I cant find any other hints in the packet capture. Therefore I uploaded a snippet of my packetcapture. Can you guys make anything out of this? All 'black entries' display the same notifications. There are no different ones, like retransmissions, etc.</p><p><a href="https://www.cloudshark.org/captures/c15924c217ae">https://www.cloudshark.org/captures/c15924c217ae</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rdp" rel="tag" title="see questions tagged &#39;rdp&#39;">rdp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '16, 15:28</strong></p><img src="https://secure.gravatar.com/avatar/aa37f4a1ef5ed10e622d24d203ab1338?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jortie2&#39;s gravatar image" /><p><span>jortie2</span><br />
<span class="score" title="10 reputation points">10</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jortie2 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Sep '16, 15:32</strong> </span></p></div></div><div id="comments-container-55766" class="comments-container"></div><div id="comment-tools-55766" class="comment-tools"></div><div class="clear"></div><div id="comment-55766-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55809"></span>

<div id="answer-container-55809" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55809-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55809-score" class="post-score" title="current number of votes">0</div><span id="post-55809-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jortie2 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your capture doesn't show anything special - the two symptoms "segment not captured" and "ACKed unseen segment" are clear signs of insufficient capture performance, meaning that packets weren't captured because the device doing the capture was too slow to grab them all.</p><p>There is also no session start or end in the capture. What you need to check is the end of the connection - you should see a FIN/ACK - FIN/ACK sequence, or a RST (reset) packet. The one sending the first FIN or RST is the one tearing down the connection. If you can, post a better capture with the teardown packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '16, 05:45</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-55809" class="comments-container"></div><div id="comment-tools-55809" class="comment-tools"></div><div class="clear"></div><div id="comment-55809-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

