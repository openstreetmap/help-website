+++
type = "question"
title = "Unable to set Promiscuous Mode"
description = '''Hello all: I&#x27;m unable to get Wireshark to view &quot;promiscuously&quot; on my home LAN. Home LAN consists of: MINT 13 Mate machine one Ubuntu machine (11 something I think) one mac os X laptop and two windows xp boxes I&#x27;m working from the MINT machine (13) and have successfully configured wireshark ( I think...'''
date = "2012-12-12T08:36:00Z"
lastmod = "2012-12-12T10:02:00Z"
weight = 16813
keywords = [ "promiscuous" ]
aliases = [ "/questions/16813" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Unable to set Promiscuous Mode](/questions/16813/unable-to-set-promiscuous-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16813-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16813-score" class="post-score" title="current number of votes">0</div><span id="post-16813-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all:</p><p>I'm unable to get Wireshark to view "promiscuously" on my home LAN. Home LAN consists of:</p><p>MINT 13 Mate machine one Ubuntu machine (11 something I think) one mac os X laptop and two windows xp boxes</p><p>I'm working from the MINT machine (13) and have successfully configured wireshark ( I think ) such that I should be able to successfully capture all the traffic on my network. Checkbox for promiscous mode is checked. ip link show eth0 shows PROMISC.</p><p>But traffic captured does not include packets between windows boxes for example. Only traffic to and from the MINT 13 machine ( and broadcasts etc )</p><p>Should work but it dosen't.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-promiscuous" rel="tag" title="see questions tagged &#39;promiscuous&#39;">promiscuous</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Dec '12, 08:36</strong></p><img src="https://secure.gravatar.com/avatar/6d2dc8f290f91128080170611c777b47?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jda8818&#39;s gravatar image" /><p><span>jda8818</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jda8818 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Dec '12, 09:12</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-16813" class="comments-container"></div><div id="comment-tools-16813" class="comment-tools"></div><div class="clear"></div><div id="comment-16813-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16814"></span>

<div id="answer-container-16814" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16814-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16814-score" class="post-score" title="current number of votes">2</div><span id="post-16814-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jda8818 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This doesn't have much to do with promiscuous mode, which will only allow your capturing NIC to accept frames that it normally would not. But in your case the capture setup is problematic since in a switched environment you'll only receive frames for your MAC address (plus broadcasts/multicasts).</p><p>Take a look at the Wiki page here: <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '12, 08:42</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Dec '12, 08:44</strong> </span></p></div></div><div id="comments-container-16814" class="comments-container"><span id="16818"></span><div id="comment-16818" class="comment"><div id="post-16818-score" class="comment-score"></div><div class="comment-text"><p>Thank you Jasper ...</p><p>Home network is not swithched however. Consists of a Netgear 114P Firewall/print server (4 port) connected to an 8 port hub (Netgear FE108). I should see everything, no?</p><p>Thanks again Jasper,</p><p>J</p><p>PS: in this case I'm interested in the traffic from one specific machine, so I guess I could make sure that this particular machine is attached directly to the firewall ... I'll try that now</p></div><div id="comment-16818-info" class="comment-info"><span class="comment-age">(12 Dec '12, 08:50)</span> <span class="comment-user userinfo">jda8818</span></div></div><span id="16821"></span><div id="comment-16821" class="comment"><div id="post-16821-score" class="comment-score"></div><div class="comment-text"><p>Hint: I converted your answer to a comment to keep things tidy.</p><p>If your hub is really a hub (and not a "switching" hub, which often happens to be the case - things that work as a switch but being called a hub) you should see everything that any port on that hub sends and receives. As far as I read the PDF manual of the device it really seems to be a hub. You should communicate in half duplex mode if it really is.</p><p>If any of the other boxes is directly attached to the Firewall you might not see it, because I guess that the Firewall doesn't work in hub mode but is in fact switching packets.</p></div><div id="comment-16821-info" class="comment-info"><span class="comment-age">(12 Dec '12, 08:59)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="16822"></span><div id="comment-16822" class="comment"><div id="post-16822-score" class="comment-score"></div><div class="comment-text"><p>Well Jasper, I'm making some progress. I moved the MINT machine (with Wireshark) from the Firewall to the hub, and I can now see ping traffic between (for instance) the two XP boxes, which are also no the hub.</p><p>Thank You for your knowledge and attention!</p></div><div id="comment-16822-info" class="comment-info"><span class="comment-age">(12 Dec '12, 09:10)</span> <span class="comment-user userinfo">jda8818</span></div></div><span id="16824"></span><div id="comment-16824" class="comment"><div id="post-16824-score" class="comment-score"></div><div class="comment-text"><p>You're welcome :-) If you think your question was solved you might want to accept the answer with the checkmark icon on the left. That way others can see that it helped.</p></div><div id="comment-16824-info" class="comment-info"><span class="comment-age">(12 Dec '12, 10:02)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-16814" class="comment-tools"></div><div class="clear"></div><div id="comment-16814-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

