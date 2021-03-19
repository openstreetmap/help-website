+++
type = "question"
title = "How to use wireshark on pc to find out if network traffic is being sniffed?"
description = '''Hi, Been searching the web but with not much luck in finding any good info. So wanted to post my question here. How do I set up wireshark to find out if someone is sniffing traffic on my network? And what would I be looking for in the capture to indicate that sniffing is really happening? thank you ...'''
date = "2017-06-18T12:54:00Z"
lastmod = "2017-06-19T13:18:00Z"
weight = 62109
keywords = [ "sniffed", "sniff", "snoop", "snooped" ]
aliases = [ "/questions/62109" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to use wireshark on pc to find out if network traffic is being sniffed?](/questions/62109/how-to-use-wireshark-on-pc-to-find-out-if-network-traffic-is-being-sniffed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62109-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62109-score" class="post-score" title="current number of votes">0</div><span id="post-62109-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Been searching the web but with not much luck in finding any good info. So wanted to post my question here. How do I set up wireshark to find out if someone is sniffing traffic on my network? And what would I be looking for in the capture to indicate that sniffing is really happening?</p><p>thank you for any info you can provide</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sniffed" rel="tag" title="see questions tagged &#39;sniffed&#39;">sniffed</span> <span class="post-tag tag-link-sniff" rel="tag" title="see questions tagged &#39;sniff&#39;">sniff</span> <span class="post-tag tag-link-snoop" rel="tag" title="see questions tagged &#39;snoop&#39;">snoop</span> <span class="post-tag tag-link-snooped" rel="tag" title="see questions tagged &#39;snooped&#39;">snooped</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jun '17, 12:54</strong></p><img src="https://secure.gravatar.com/avatar/8dee94c293100aa35c2dfca05fa51b50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shad&#39;s gravatar image" /><p><span>Shad</span><br />
<span class="score" title="3 reputation points">3</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shad has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Jun '17, 12:55</strong> </span></p></div></div><div id="comments-container-62109" class="comments-container"></div><div id="comment-tools-62109" class="comment-tools"></div><div class="clear"></div><div id="comment-62109-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62110"></span>

<div id="answer-container-62110" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62110-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62110-score" class="post-score" title="current number of votes">1</div><span id="post-62110-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That depends a lot on your how much control you have over the network.</p><p>There are two aspects:</p><ul><li>the sniffing itself</li><li>the delivery of the sniffing results.</li></ul><p>You can only notice <strong>the sniffing itself</strong> using Wireshark if the person uses some techniques which actively modifies the network traffic, like arp spoofing or arp flooding, or downloading files from shared folders, all that done on your own compromised machine connected to the network or some machine connected secretly. If they run a passive monitoring tool (wireshark or tcpdump or alike) on one of your machines, or aren't sniffing raw network traffic but some files on the machines instead, you won't see anything using your own passive monitor - Wireshark.</p><p>Symptoms:</p><ul><li>arp spoofing would mean that you'd see wrong associations between destination IP addresses and destination MAC addresses on your LAN (you must know the real MAC addresses of your end devices and gateway elements and search for packets where the IP addresses of these devices are combined with other devices' MAC addresses)</li><li>mac flooding would mean that you would see packets intended for other machines arriving to your own machine, and likely also a decrease in network throughput (supposing that you use switches rater than real hubs on which this was a normal behaviour)</li><li>downloading files from shared folders would be seen as file transfers between machines which are not expected to exchange files with each other, but you'd have to arrange mirroring of individual machines' traffic to your Wireshark machine one by one, as it is close to impossible to capture the traffic of the whole network.</li></ul><p>You can notice <strong>the delivery of sniffing results</strong> if there are sessions to unknown destinations getting open by some of your machines, but this may not be a continuous activity so you'd basically have to capture all your traffic over the internet uplink for days to have a chance to spot that, and you'd have to know how your "legal" traffic looks like. And if someone comes to collect the sniffed data with a flashdisk now and then, Wireshark is also not the tool you need.</p><p>Oh, and all this is only valid if we talk about wired networks or file transfers; if someone is sniffing your wireless network, it is simply impossible to detect as that can be done fully passively if your wireless passwords have leaked or you use a weak encryption.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jun '17, 13:23</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Jun '17, 13:25</strong> </span></p></div></div><div id="comments-container-62110" class="comments-container"><span id="62114"></span><div id="comment-62114" class="comment"><div id="post-62114-score" class="comment-score"></div><div class="comment-text"><p>Hi Sindy,</p><p>Thanks for your reply and for the info. Yes, sounds difficult. I've checked my arp table and looks ok. I'm not as concerned about my internal network getting sniffed, but more from the external. In other words, am more concerned about my traffic being sniffed from anywhere outside my premises, perhaps even from the ISP. I have read here and there that wireshark may be able to detect if any sniffing is indeed happening. But it sounds like I would have to check every IP address that is captured and see where it is connecting to, and that for sure isn't easy to check and is very tedious. Was hoping there was a tell-tale way to check. Any suggestions would be really appreciated. thanks in advance to anyone that may have a way to check.</p></div><div id="comment-62114-info" class="comment-info"><span class="comment-age">(18 Jun '17, 23:32)</span> <span class="comment-user userinfo">Shad</span></div></div><span id="62137"></span><div id="comment-62137" class="comment"><div id="post-62137-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I am more concerned about my traffic being sniffed from anywhere outside my premises, perhaps even from the ISP</p></blockquote><p>Well, if your ISP is sniffing your traffic which passes through their network, there is no (0) way for you to notice that. On the other hand, if you (and your users) use secure protocols and do not ignore safety warnings about non-matching certificates, this way the ISP can learn little more than just the list of sites you visit and the amount of traffic which you exchange with them.</p><p>Unless you are the U.S. embassy in Russia or vice versa, the ISPs usually have enough more important things to do than spy on their clients. And it is one of the least efficient methods for the a.m. reason. Reportedly (I'm not directly involved in network security) and sadly, non-loyal insiders are the most eficient one.</p></div><div id="comment-62137-info" class="comment-info"><span class="comment-age">(19 Jun '17, 13:18)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-62110" class="comment-tools"></div><div class="clear"></div><div id="comment-62110-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

