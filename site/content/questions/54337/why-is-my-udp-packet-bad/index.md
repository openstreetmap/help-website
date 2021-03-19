+++
type = "question"
title = "Why is my UDP packet bad?"
description = '''Hi I am trying to send a UDP data packet of 13 octets from: 192.168.1.10 port 3001 to: 192.168.1.12 port 3000 Wireshark shows the packet as: PDUType: Fire[Malformed Packet] The destination returns an ICMP packet that Wireshark marks: &#x27;Destination unreachable&#x27;. The UDP packet looks ok to me. How shou...'''
date = "2016-07-26T06:19:00Z"
lastmod = "2016-07-26T07:04:00Z"
weight = 54337
keywords = [ "udp" ]
aliases = [ "/questions/54337" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Why is my UDP packet bad?](/questions/54337/why-is-my-udp-packet-bad)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54337-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54337-score" class="post-score" title="current number of votes">0</div><span id="post-54337-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I am trying to send a UDP data packet of 13 octets from:</p><p>192.168.1.10 port 3001</p><p>to:</p><p>192.168.1.12 port 3000</p><p>Wireshark shows the packet as:</p><p><strong>PDUType: Fire[Malformed Packet]</strong></p><p>The destination returns an ICMP packet that Wireshark marks: 'Destination unreachable'.</p><p>The UDP packet looks ok to me. How should I upload it to here so that someone can help by checking it please?</p><p>Best regards</p><p>David</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jul '16, 06:19</strong></p><img src="https://secure.gravatar.com/avatar/cfb0228285e3c9494d763ba825e7a76c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DavidA_2015&#39;s gravatar image" /><p><span>DavidA_2015</span><br />
<span class="score" title="11 reputation points">11</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DavidA_2015 has one accepted answer">50%</span></p></div></div><div id="comments-container-54337" class="comments-container"><span id="54338"></span><div id="comment-54338" class="comment"><div id="post-54338-score" class="comment-score"></div><div class="comment-text"><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive, Dropbox etc.?</p></div><div id="comment-54338-info" class="comment-info"><span class="comment-age">(26 Jul '16, 06:23)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="54339"></span><div id="comment-54339" class="comment"><div id="post-54339-score" class="comment-score"></div><div class="comment-text"><p>Here it is: <a href="https://www.cloudshark.org/captures/df45a98f996e">https://www.cloudshark.org/captures/df45a98f996e</a></p></div><div id="comment-54339-info" class="comment-info"><span class="comment-age">(26 Jul '16, 06:28)</span> <span class="comment-user userinfo">DavidA_2015</span></div></div></div><div id="comment-tools-54337" class="comment-tools"></div><div class="clear"></div><div id="comment-54337-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="54340"></span>

<div id="answer-container-54340" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54340-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54340-score" class="post-score" title="current number of votes">1</div><span id="post-54340-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="DavidA_2015 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Port 3000 is the default port for the DIS (Distributed Interactive Simulation) protocol. So Wireshark tries to dissect this UDP datagram as being a DIS packet, but the payload is too short (that's why you get the malformed error).</p><p>If this is not a DIS packet and you just want to see the UDP payload, go to Analyze -&gt; Enabled Protocols and uncheck DIS dissector, or go to Edit -&gt; Preferences -&gt; Protocols -&gt; DIS and change the default UDP port value.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '16, 06:47</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-54340" class="comments-container"><span id="54343"></span><div id="comment-54343" class="comment"><div id="post-54343-score" class="comment-score"></div><div class="comment-text"><p>Thank you both for your answers.</p></div><div id="comment-54343-info" class="comment-info"><span class="comment-age">(26 Jul '16, 07:04)</span> <span class="comment-user userinfo">DavidA_2015</span></div></div></div><div id="comment-tools-54340" class="comment-tools"></div><div class="clear"></div><div id="comment-54340-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54341"></span>

<div id="answer-container-54341" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54341-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54341-score" class="post-score" title="current number of votes">1</div><span id="post-54341-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You ICMP packet is being sent to UDP port 3000 which is the default configured port for the DIS protocol, so is being dissected as such.</p><p>To fix this disable the DIS dissector; in the packet details pane, right click the tree item for DIS and selected "Protocol Preferences -&gt;" -&gt; "Disable DIS ...", then in the Enabled Protocols dialog uncheck DIS and click OK on the dialog. Reload the capture using the menu View -&gt; Reload.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '16, 06:51</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-54341" class="comments-container"><span id="54342"></span><div id="comment-54342" class="comment"><div id="post-54342-score" class="comment-score"></div><div class="comment-text"><p><span>@Pascal Quantin</span> was a bit quicker than me :-)</p></div><div id="comment-54342-info" class="comment-info"><span class="comment-age">(26 Jul '16, 06:52)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-54341" class="comment-tools"></div><div class="clear"></div><div id="comment-54341-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

