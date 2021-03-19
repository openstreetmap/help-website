+++
type = "question"
title = "DNS attack"
description = '''Hi all, is this showing that there was a DNS attack ? because DNS attack would be flood with SYN packets and not ACK packets   '''
date = "2016-12-02T09:00:00Z"
lastmod = "2016-12-11T02:50:00Z"
weight = 57791
keywords = [ "dnsattack" ]
aliases = [ "/questions/57791" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [DNS attack](/questions/57791/dns-attack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57791-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57791-score" class="post-score" title="current number of votes">0</div><span id="post-57791-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, is this showing that there was a DNS attack ? because DNS attack would be flood with SYN packets and not ACK packets</p><p><img src="https://osqa-ask.wireshark.org/upfiles/DNS_attack.jpg" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/Conversations_3.jpg" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/Conversations_4.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dnsattack" rel="tag" title="see questions tagged &#39;dnsattack&#39;">dnsattack</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '16, 09:00</strong></p><img src="https://secure.gravatar.com/avatar/149d6f8eb0595bad31c406551c9654a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="doran_lum&#39;s gravatar image" /><p><span>doran_lum</span><br />
<span class="score" title="11 reputation points">11</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="doran_lum has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Dec '16, 00:22</strong> </span></p></div></div><div id="comments-container-57791" class="comments-container"></div><div id="comment-tools-57791" class="comment-tools"></div><div class="clear"></div><div id="comment-57791-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57798"></span>

<div id="answer-container-57798" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57798-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57798-score" class="post-score" title="current number of votes">3</div><span id="post-57798-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, this is not DNS attack. This looks like an ordinary unidirectional TCP data transfer. Why do you think DNS attack is "flood with SYN packets"? DNS flood attacks usually use UDP which has nothing to do with SYN flag concept. See the next article:</p><p><a href="https://www.incapsula.com/ddos/attack-glossary/dns-flood.html">https://www.incapsula.com/ddos/attack-glossary/dns-flood.html</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '16, 10:23</strong></p><img src="https://secure.gravatar.com/avatar/1e22670f8d643ca08d658b80a6782932?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Packet_vlad&#39;s gravatar image" /><p><span>Packet_vlad</span><br />
<span class="score" title="436 reputation points">436</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Packet_vlad has 5 accepted answers">20%</span></p></img></div></div><div id="comments-container-57798" class="comments-container"><span id="57806"></span><div id="comment-57806" class="comment"><div id="post-57806-score" class="comment-score"></div><div class="comment-text"><p>Thank you. Does this means a high load of TCP data transfer which might have slow down the network ?</p></div><div id="comment-57806-info" class="comment-info"><span class="comment-age">(02 Dec '16, 20:20)</span> <span class="comment-user userinfo">doran_lum</span></div></div><span id="57807"></span><div id="comment-57807" class="comment"><div id="post-57807-score" class="comment-score">1</div><div class="comment-text"><p>It's hard to tell just looking at the screenshot. An influence of this stream can vary from "almost none" to "heavy". It depends on many factors:</p><p>1) How often it happens (once, every 5 min, intermittently);</p><p>2) For how long time it lasts (2 seconds, 10 minutes, constantly);</p><p>3) What's you available bandwith.</p><p>Now I can do some calculations from your screenshot (roughly): used bandwith = received data / (end time - start time) = (1506*16 + 1506(unseen) + 619) / (520.413477 - 520.397597) = 26221 Bytes / 0.01588 sec = 1651196 Bytes/sec ~ 13 Mbit/sec.</p><p>But again, I don't know how long did it last. Maybe, that's absolutely not a problem.</p><p>To get full unferstanding you first need to formalize you complaint like the next: web-access is slow 1-2 times a day for 10-15 min usually close to 1pm. Then you can capture traffic when the slowdown is observed (you can use Wireshark ring buffer feature if you don't know the time of next occurence). And after, if you find exactly this stream is causing your slowdown, then will be the time to dig deeper to find what proccess starts the stream.</p></div><div id="comment-57807-info" class="comment-info"><span class="comment-age">(02 Dec '16, 23:11)</span> <span class="comment-user userinfo">Packet_vlad</span></div></div><span id="57808"></span><div id="comment-57808" class="comment"><div id="post-57808-score" class="comment-score"></div><div class="comment-text"><p>1) This has happen intermittently</p><p>2) It lasted for 10 minutes</p><p>Thanks so much for the calculations, I will also analyze what might have trigger this. I also took a look under Conversation and found this to be the 2nd highest bytes count during the capture. I also attached the conversation in the questions.</p><p>Another quick question for this port 9001, I understand it's network traffic and directory information but are we able to tell what is going on from each packet ?</p></div><div id="comment-57808-info" class="comment-info"><span class="comment-age">(03 Dec '16, 00:21)</span> <span class="comment-user userinfo">doran_lum</span></div></div><span id="57999"></span><div id="comment-57999" class="comment"><div id="post-57999-score" class="comment-score"></div><div class="comment-text"><p>Can I ask what does *16 for the first received data is for ?</p></div><div id="comment-57999-info" class="comment-info"><span class="comment-age">(11 Dec '16, 00:46)</span> <span class="comment-user userinfo">doran_lum</span></div></div><span id="58000"></span><div id="comment-58000" class="comment"><div id="post-58000-score" class="comment-score"></div><div class="comment-text"><p>Could you please clarify you question, I don't understand what you mean.</p></div><div id="comment-58000-info" class="comment-info"><span class="comment-age">(11 Dec '16, 01:21)</span> <span class="comment-user userinfo">Packet_vlad</span></div></div><span id="58002"></span><div id="comment-58002" class="comment not_top_scorer"><div id="post-58002-score" class="comment-score"></div><div class="comment-text"><p>sorry i mean this portion why would you multiple 16 firstly and then later add 619 ?</p><p>(1506*16 + 1506(unseen) + 619)</p></div><div id="comment-58002-info" class="comment-info"><span class="comment-age">(11 Dec '16, 02:26)</span> <span class="comment-user userinfo">doran_lum</span></div></div><span id="58004"></span><div id="comment-58004" class="comment not_top_scorer"><div id="post-58004-score" class="comment-score"></div><div class="comment-text"><p>I just looked at your first screenshot and calculated Byte sum of all packets (frames) came from node with IP of 5.135.184.158. There are 16 packets of 1506 Bytes each + 1 unseen packet of 1506 Bytes + one packet of 619 Bytes. I didn't count the first packet of 619 Bytes because this is our 'relative zero' time moment.</p><p>But this is nothing special, you can just build I/O graph in Wireshark and do not do all this stuff.</p></div><div id="comment-58004-info" class="comment-info"><span class="comment-age">(11 Dec '16, 02:50)</span> <span class="comment-user userinfo">Packet_vlad</span></div></div></div><div id="comment-tools-57798" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-57798-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

