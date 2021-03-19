+++
type = "question"
title = "Trace blocked DNS requests?"
description = '''We are a group of volunteers for a non profit WISP in the Yorkshire Dales. We have intermittently but serious spasms of various clients&#x27; DNS requests blocked. Note we have only one Internet IP, the 50+ clients are all on fixed IPs served by various APs. To effect a cure, usually only temporarily, we...'''
date = "2016-08-01T07:16:00Z"
lastmod = "2016-08-04T02:39:00Z"
weight = 54480
keywords = [ "ubiquti", "draytek" ]
aliases = [ "/questions/54480" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Trace blocked DNS requests?](/questions/54480/trace-blocked-dns-requests)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54480-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are a group of volunteers for a non profit WISP in the Yorkshire Dales. We have intermittently but serious spasms of various clients' DNS requests blocked. Note we have only one Internet IP, the 50+ clients are all on fixed IPs served by various APs. To effect a cure, usually only temporarily, we allocate the offending device with a different IP address. This may work for two hours or two months before the problem reappears. What I/we need to do is track down where the DNS request is being blocked. Using Tracert with Wireshark doesn't seem to work, i.e. the request path doesn't appear.</p><p>Can you help?</p></div><div id="question-tags" class="tags-container tags">ubiquti draytek</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Aug '16, 07:16</strong></p><img src="https://secure.gravatar.com/avatar/255b87a38b36888b508f767b4269dbd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fopetesl&#39;s gravatar image" /><p>fopetesl<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fopetesl has no accepted answers">0%</span></p></div></div><div id="comments-container-54480" class="comments-container"></div><div id="comment-tools-54480" class="comment-tools"></div><div class="clear"></div><div id="comment-54480-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54569"></span>

<div id="answer-container-54569" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54569-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Where is the DNS server located that the clients send their requests to? Is it an internal server, or an external one?</p><p>You should try to capture the packets at the server (if internal) or on the ISP uplink (if external) to check request/reply functionality. The idea is to find out what happens if the requests are not answered anymore. Also, check if there's a firewall that has a rate limit for connections - those settings are often too strict and start blocking too soon.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Aug '16, 02:39</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-54569" class="comments-container"><span id="54572"></span><div id="comment-54572" class="comment"><div id="post-54572-score" class="comment-score"></div><div class="comment-text"><p>We've tried different DNS (external) servers, Google, ISP and couple of other public servers. I like the idea of capturing packets at the VDSL modem if that's what you are suggesting. No idea how I might do that though. The Draytek modem doesn't seem to have that facility built in unfortunately. Note though, that in April 15 client's were affected but 35 clients weren't. All the clients have internal 192.168.32.xxx addresses which feed though one public Internet IP address. No incidents occurred until last weekend when eight of the original clients with DNS failures were re-affected plus three new ones. One of these new ones is a domestic router on fixed address because of a bridge route, so the problem is not down to the Ubiquti 5GHz links. There is a rate limit but not for connections I could find. The rate limit caps link speed if number of connections/sessions exceeds a preset number.</p></div><div id="comment-54572-info" class="comment-info"><span class="comment-age">(04 Aug '16, 03:12)</span> fopetesl</div></div><span id="54573"></span><div id="comment-54573" class="comment"><div id="post-54573-score" class="comment-score"></div><div class="comment-text"><p>There is a moment which makes me cautious: you wrote you could not see the icmp requests sent by <code>traceroute</code> which implies that the responses do come and that you can capture them. So I wonder what is your capture setup.</p><p>Also, when you say that all your clients live in the same private subnet and you "have just one Internet IP", I deduce that there is a device which performs NAT. So from the internet facing interface of this device, there is no difference between the IP and UDP portions of the requests originally sent by different clients. Is your single public IP address assigned to the VDSL modem or the modem is a bridge and some routing (and NATing) device is located between the clients and the modem? A sketch of the complete network topology added to the original Question (<strong>not</strong> to any Comment) would be helpful.</p></div><div id="comment-54573-info" class="comment-info"><span class="comment-age">(04 Aug '16, 03:37)</span> sindy</div></div></div><div id="comment-tools-54569" class="comment-tools"></div><div class="clear"></div><div id="comment-54569-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

