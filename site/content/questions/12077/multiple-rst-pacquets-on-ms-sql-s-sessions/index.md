+++
type = "question"
title = "Multiple [RST] pacquets on ms-sql-s sessions."
description = '''Dear all, Is there someone who can explain to me why in my Wireshark captures I have sessions that ends with several RST packets following normal TCP end Session and the other not. I want to specifie that hosts concerned are always the same hosts but in different processes numbers here attaching the...'''
date = "2012-06-20T08:51:00Z"
lastmod = "2012-06-27T03:59:00Z"
weight = 12077
keywords = [ "rst" ]
aliases = [ "/questions/12077" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Multiple \[RST\] pacquets on ms-sql-s sessions.](/questions/12077/multiple-rst-pacquets-on-ms-sql-s-sessions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12077-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12077-score" class="post-score" title="current number of votes">0</div><span id="post-12077-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear all,</p><p>Is there someone who can explain to me why in my Wireshark captures I have sessions that ends with several RST packets following normal TCP end Session and the other not.</p><p>I want to specifie that hosts concerned are always the same hosts but in different processes numbers</p><p>here attaching the captures. <img alt="Alt text" title="[RST] paquets.png"></img> <img alt="Alt text" title="paquets.png"></img> <img alt="Alt text" title="without [RST] Paquets.png"></img></p><p>Thank you for your help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jun '12, 08:51</strong></p><img src="https://secure.gravatar.com/avatar/ac8004598616d057bd81de78d142de04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KD001&#39;s gravatar image" /><p><span>KD001</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KD001 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-12077" class="comments-container"><span id="12080"></span><div id="comment-12080" class="comment"><div id="post-12080-score" class="comment-score">1</div><div class="comment-text"><p>can you please upload the capture file somewhere (maybe <a href="http://cloudshark.org">cloudshark.org</a>) and post the link.</p><p>BTW: do you know of any IDS (intrusion detection system) or any firewall in the path to the SQL server?</p></div><div id="comment-12080-info" class="comment-info"><span class="comment-age">(20 Jun '12, 11:17)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="12130"></span><div id="comment-12130" class="comment"><div id="post-12130-score" class="comment-score"></div><div class="comment-text"><p>hi kurt,</p><p>here is the link to the capture. <a href="https://www.cloudshark.org/captures/c2b111ed1b79">https://www.cloudshark.org/captures/c2b111ed1b79</a></p><p>thank you for all.</p></div><div id="comment-12130-info" class="comment-info"><span class="comment-age">(22 Jun '12, 04:00)</span> <span class="comment-user userinfo">KD001</span></div></div></div><div id="comment-tools-12077" class="comment-tools"></div><div class="clear"></div><div id="comment-12077-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12141"></span>

<div id="answer-container-12141" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12141-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12141-score" class="post-score" title="current number of votes">0</div><span id="post-12141-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In the capture file we can only see the first two frames of the 3-way TCP handshake (SYN, SYN-ACK but no ACK!) and then either a FIN or a RST. Where did you capture that data? On the Netscreen firewall?</p><p>If yes, the multiple TCP Resets could be generated by the firewall (IDS on the Firewall or regular behaviour). To verify, I suggest to capture in front of the firewall and after the firewall. Then compare the capture files.</p><p>Do you have any network problems with those RESETS or are you just curious about it?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '12, 23:20</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></img></div></div><div id="comments-container-12141" class="comments-container"><span id="12228"></span><div id="comment-12228" class="comment"><div id="post-12228-score" class="comment-score"></div><div class="comment-text"><p>Hello Kurt, 1 / in fact I do not have ACK packets because I put a filter to capture only the SYN, FIN and RST. I wanted to limit the number of packs ... because if not everyone tired of ACK packets have, and it would have been too many frames.</p><p>2 / I actually have a firewall between the client and server. and I wondered why sometimes I RST packets after the normal closing time of 4.</p><p>I launched this catch because I have a user who said that the network is Responsible for the failure of some transfers. I think it's Sql Server which is the responsable. But I have to prove.</p></div><div id="comment-12228-info" class="comment-info"><span class="comment-age">(27 Jun '12, 01:24)</span> <span class="comment-user userinfo">KD001</span></div></div><span id="12232"></span><div id="comment-12232" class="comment"><div id="post-12232-score" class="comment-score"></div><div class="comment-text"><blockquote><p>2 / I actually have a firewall between the client and server. and I wondered why sometimes I RST packets after the normal closing time of 4.</p></blockquote><p>It could be the Firewall or the Client. According to the MAC addresses you captured between the Firewall (Netscreen) and the next Router (Cisco). In that case you cannot tell if the Firewall sent the RESET or the Client. You need to capture between Client and Firewall AND between Firewall/Router.</p><p>Furthermore you need to look at the SQL traffic itself, not just the TCP Flags. Maybe there is an error message in the answer from the SQL server that gives you a hint.</p><blockquote><p>I launched this catch because I have a user who said that<br />
the network is Responsible for the failure of some transfers.<br />
I think it's Sql Server which is the responsible. But I have to prove.</p></blockquote><p>Your capture does not contain any special hints about SQL problems. To analyze those, we would need:</p><ul><li>more information about the SQL server problems (performance, connection problems, etc.)</li><li>a capture file with SQL traffic for a period of time where the users reported a problem.</li></ul><p>Regards<br />
Kurt</p></div><div id="comment-12232-info" class="comment-info"><span class="comment-age">(27 Jun '12, 03:59)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-12141" class="comment-tools"></div><div class="clear"></div><div id="comment-12141-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

