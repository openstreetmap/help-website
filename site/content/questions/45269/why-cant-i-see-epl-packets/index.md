+++
type = "question"
title = "Why can&#x27;t I see EPL packets?"
description = '''I&#x27;m directly wired to an ethernet network of 3 hubs, one master and two slaves which communicate (and I&#x27;m sure they&#x27;re sending the correct thing). Network card is in promiscuous mode and I can see a ping from another computer connected on that network, to one of the hubs. So it&#x27;s working as expected...'''
date = "2015-08-20T07:49:00Z"
lastmod = "2015-08-20T07:49:00Z"
weight = 45269
keywords = [ "powerlinkv2", "eplv2", "epl", "powerlink" ]
aliases = [ "/questions/45269" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why can't I see EPL packets?](/questions/45269/why-cant-i-see-epl-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45269-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45269-score" class="post-score" title="current number of votes">0</div><span id="post-45269-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm directly wired to an ethernet network of 3 hubs, one master and two slaves which communicate (and I'm sure they're sending the correct thing). Network card is in promiscuous mode and I can see a ping from another computer connected on that network, to one of the hubs. So it's working as expected.</p><p>But in wireshark I can't see a single EPL packet but I know they should be there. This morning I was fiddling around and managed to see them once, everything was perfectly working but I'm not sure what I changed and I never saw them again.</p><p>It may be useful to note that in the past I've had no problem doing the exact same process to sniff those packets, but today on windows7, a new computer and an updated wireshark I can't.</p><p>Everything is checked, EPL etc.. I only see the ARP packets each hub send etc. For my network card I took 192.168.100.241 with a 255.255.255.0 network mask. The master is at 192.168.100.240 and slaves at 100.1 and 100.2. So promiscuous mode is working, windows network status shows a lot of octets recevied but wireshark isn't showing a lot.. Any idea to solve this problem?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-powerlinkv2" rel="tag" title="see questions tagged &#39;powerlinkv2&#39;">powerlinkv2</span> <span class="post-tag tag-link-eplv2" rel="tag" title="see questions tagged &#39;eplv2&#39;">eplv2</span> <span class="post-tag tag-link-epl" rel="tag" title="see questions tagged &#39;epl&#39;">epl</span> <span class="post-tag tag-link-powerlink" rel="tag" title="see questions tagged &#39;powerlink&#39;">powerlink</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Aug '15, 07:49</strong></p><img src="https://secure.gravatar.com/avatar/68547127888eb12def6c2884b9da1c61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kolofar&#39;s gravatar image" /><p><span>Kolofar</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kolofar has no accepted answers">0%</span></p></div></div><div id="comments-container-45269" class="comments-container"></div><div id="comment-tools-45269" class="comment-tools"></div><div class="clear"></div><div id="comment-45269-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

