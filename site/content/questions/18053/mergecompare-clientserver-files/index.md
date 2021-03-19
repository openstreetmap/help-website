+++
type = "question"
title = "Merge/Compare -- client/server files"
description = '''Hi, I have two capture files, client facing and server facing. There is a device in the middle that is dropping packets and I have identified the device, however, I require a little more evidence. I would like to know if there is a way to merge these two files together and &quot;see&quot; with a graph or othe...'''
date = "2013-01-29T12:12:00Z"
lastmod = "2013-02-06T04:47:00Z"
weight = 18053
keywords = [ "merge" ]
aliases = [ "/questions/18053" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Merge/Compare -- client/server files](/questions/18053/mergecompare-clientserver-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18053-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18053-score" class="post-score" title="current number of votes">0</div><span id="post-18053-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have two capture files, client facing and server facing. There is a device in the middle that is dropping packets and I have identified the device, however, I require a little more evidence. I would like to know if there is a way to merge these two files together and "see" with a graph or other method, that lines up the missing packets.</p><p>Ex: Packet 201 (authent packet) is sent from the client, but never "seen" on the Server side.</p><p>Packet 200 -- sent from client / Packet 200 seen on Server side</p><p>Packet 201 -- sent from client / ...not seen on Server side</p><p>Packet 202 -- sent from client / Packet 202 seen on Server side</p><p>Packet 203 -- sent from client / Packet 203 seen on Server side</p><p>Packet 204 -- sent from client / ...not seen on Server side</p><p>My captures occur on each side of the device. I have a suspicion that there are <em>multiple</em> instances of this behavior but I feel that I'm not using the best discovery method to determine which ones, how often, and how many packets are getting dropped.</p><p>I'm currently working with WS - 1.8.4,</p><p>thanks,</p><p>JTech</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '13, 12:12</strong></p><img src="https://secure.gravatar.com/avatar/791c3a844bb1629d3a685adab364e2d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JTech_17&#39;s gravatar image" /><p><span>JTech_17</span><br />
<span class="score" title="41 reputation points">41</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JTech_17 has no accepted answers">0%</span></p></div></div><div id="comments-container-18053" class="comments-container"><span id="18096"></span><div id="comment-18096" class="comment"><div id="post-18096-score" class="comment-score"></div><div class="comment-text"><p>Thank you all for the answers. I will try each one and provide feedback.</p><p>JTech</p></div><div id="comment-18096-info" class="comment-info"><span class="comment-age">(30 Jan '13, 05:48)</span> <span class="comment-user userinfo">JTech_17</span></div></div><span id="18099"></span><div id="comment-18099" class="comment"><div id="post-18099-score" class="comment-score"></div><div class="comment-text"><p><span>@JTech_17</span></p><p>I've converted your "answer" to a comment as that's how this site works, please see the FAQ for more info.</p><p>If any of the answers do solve your issue, for the benefit of other users, please accept the answer by clicking the checkmark icon next to it.</p></div><div id="comment-18099-info" class="comment-info"><span class="comment-age">(30 Jan '13, 05:58)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-18053" class="comment-tools"></div><div class="clear"></div><div id="comment-18053-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="18069"></span>

<div id="answer-container-18069" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18069-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18069-score" class="post-score" title="current number of votes">1</div><span id="post-18069-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JTech_17 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>JTech, go to Riverbed.com and somewhere there, you should be able to download an eval version of Pilot program (Yes, I do work for Riverbed now, but I'm not trying to sell you anything)</p><p>In Pilot, there is a Multi Segment Analysis that does what you're looking for. It will take two (or more) trace files and will give you a report on packet drops etc. So if you're looking for a one time thing, download the eval, use it, and uninstall it when the timebomb goes off. No harm, no foul.<br />
</p><p>Or as Jasper mentioned, export TCP Sequence numbers <em>or</em> IP ID field. Sometimes IP.ID will make it through LBs etc. If you're lucky, it may be as simple as doing a diff on two columns of IP ID field.</p><p>BTW, what additional evidence do you need? It seems like you already identified which part of the infrastructure is dropping packets. One word of caution. <em>Make</em> sure it's not the span port that's dropping the packets. If there is packet loss, you <em>have</em> to see retransmissions. So don't get fooled into thinking devices are dropping packets when it's just the span/monitor port that's responsible.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '13, 19:26</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p><span>hansangb</span><br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Jan '13, 19:28</strong> </span></p></div></div><div id="comments-container-18069" class="comments-container"><span id="18098"></span><div id="comment-18098" class="comment"><div id="post-18098-score" class="comment-score"></div><div class="comment-text"><p>The reason I require additional evidence, is, when I showed the device owners the data, they denied it. Yes, I realize how crazy that sounds, but believe me, I was a bit surprised by that reaction myself. I too suspected a span port issue, however, there is only one user traversing through the device and ending up on the other side of this core switch. I plan to place an inline tap between the device and the core switch...simply to rule out a span port issue. If I see the same behavior then I'll know my original findings are valid. thank you, JTech</p></div><div id="comment-18098-info" class="comment-info"><span class="comment-age">(30 Jan '13, 05:54)</span> <span class="comment-user userinfo">JTech_17</span></div></div><span id="18358"></span><div id="comment-18358" class="comment"><div id="post-18358-score" class="comment-score"></div><div class="comment-text"><p>The Keep_Alive and Keep_Alive_ACK packets were not seen on both sides. Pilot was able to show this, though it did take some time to learn the navigation within Pilot. we already use Riverbed Steelhead appliances for our WAN links (we just don't have the Pilot app as part of that contract - though req has been submitted). I placed a NetOptics inline tap between the device and the core, to rule out any span port issues, and the results were <em>exactly</em> the same. The device owner is still skeptical, but that is ok - denial is a hard mountain to climb over. thank you, JTech</p></div><div id="comment-18358-info" class="comment-info"><span class="comment-age">(06 Feb '13, 04:47)</span> <span class="comment-user userinfo">JTech_17</span></div></div></div><div id="comment-tools-18069" class="comment-tools"></div><div class="clear"></div><div id="comment-18069-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18055"></span>

<div id="answer-container-18055" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18055-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18055-score" class="post-score" title="current number of votes">0</div><span id="post-18055-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Dump the two files as text files, the MD5 frame hash only. Corresponding frames should have the same hash in either trace. Or is it a router, NAT or other non-bridge device?</p><p>'cat' the text files, 'sort' them based on MD5 hash and see how many 'uniq' entries you have.</p><p>Hint: the quoted words are handy command line tools for this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '13, 12:41</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-18055" class="comments-container"></div><div id="comment-tools-18055" class="comment-tools"></div><div class="clear"></div><div id="comment-18055-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18067"></span>

<div id="answer-container-18067" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18067-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18067-score" class="post-score" title="current number of votes">0</div><span id="post-18067-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If there's just a up to a few hundred packets to compare I'd proabably just graph the TCP sequence numbers with the Statistics/Time-Sequence Graph for both locations, color them differently in a drawing/picture editing tool and overlay them with each other. That way it should be easy to spot where a dot is missing - but as I said, this only makes sense if you do not have tons of packets that will make the graph so crowded that it becomes unreadable.</p><p>Or you could just export all sequence numbers, sort them by order and compare the two sides. If you have sequence numbers twice and if it is seen only once on the other side it is most likely a retransmission. This only makes sense if you filtered the trace to the one tcp connection, and if sender and receiver use quite different sequence number ranges (which they usually do, but the inital sequence is random, so theoretically they could be even identical for both directions). Sequence numbers tend to stay the same even when passing through NAT gateways and other devices that change parts of the packet. Proxies will be a problem though, as they create completely new TCP sessions and you can't match anything for sure except maybe the actual TCP payload (if there is no encryption taking place).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '13, 17:08</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-18067" class="comments-container"></div><div id="comment-tools-18067" class="comment-tools"></div><div class="clear"></div><div id="comment-18067-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

