+++
type = "question"
title = "Outbound traffic to China"
description = '''Brand new Checkpoint firewall. Super powered for the size of my organization. Quite an education. A few days ago I started seeing outbound traffic to a few IP&#x27;s in China being Blocked by my egress rules (good times)The traffic is reverse lookup DNS queries (UDP 53) They happen about 15 times an hour...'''
date = "2011-09-02T04:35:00Z"
lastmod = "2011-09-05T01:29:00Z"
weight = 6060
keywords = [ "malware", "dns" ]
aliases = [ "/questions/6060" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Outbound traffic to China](/questions/6060/outbound-traffic-to-china)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6060-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6060-score" class="post-score" title="current number of votes">0</div><span id="post-6060-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Brand new Checkpoint firewall. Super powered for the size of my organization. Quite an education. A few days ago I started seeing outbound traffic to a few IP's in China being Blocked by my egress rules (good times)The traffic is reverse lookup DNS queries (UDP 53) They happen about 15 times an hour or more. I'm having a very tough time tracking where it's coming from. When I capture DNS,the queries come from mostly the inside interface of the firewall itself. Not always, but mostly. there is no other suspicious traffic. My egress rules are pretty tight and nothing else is trying to get to China. IP spoof? I've fully scanned for malware throughout my office. Solid antivirus/malware is resident on every internal machine.</p><p>Thoughts?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-malware" rel="tag" title="see questions tagged &#39;malware&#39;">malware</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Sep '11, 04:35</strong></p><img src="https://secure.gravatar.com/avatar/527570a0e746a4066d14f0cd8f97545b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cholmes&#39;s gravatar image" /><p><span>cholmes</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cholmes has no accepted answers">0%</span></p></div></div><div id="comments-container-6060" class="comments-container"><span id="6089"></span><div id="comment-6089" class="comment"><div id="post-6089-score" class="comment-score"></div><div class="comment-text"><p>I've seen similar behaviour on other vendor's appliances. It should help to consider the following things and test (if you can manage to do so for productive reasons):</p><ul><li>Isolate the fw and see if it's still sending s.th. out to foreign IPs</li><li>if not possible to isolate sniff traffic on both inside and outside interfaces and really compare icmp, dns and related packets to find the trigger</li><li>IP Spoof with inside (RFC 1918?) address would not be useful for WAN connections, double check that</li></ul><p>if detailed questions or comments arise please provide an email address</p><p>good luck</p></div><div id="comment-6089-info" class="comment-info"><span class="comment-age">(05 Sep '11, 01:29)</span> <span class="comment-user userinfo">Landi</span></div></div></div><div id="comment-tools-6060" class="comment-tools"></div><div class="clear"></div><div id="comment-6060-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

