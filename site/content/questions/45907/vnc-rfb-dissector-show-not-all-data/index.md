+++
type = "question"
title = "VNC (RFB) dissector show not all data"
description = '''If I set filter = &quot;vnc&quot; part of traffic not detected. Filter &quot;tcp.port rq 5900&quot; work more correct. Dissector not show data from packets like UserInit message, ServerInit, handshake, security options and any other data. Just binary data shown like in any another TCP packet. Also shown only data which...'''
date = "2015-09-17T02:27:00Z"
lastmod = "2015-09-17T07:54:00Z"
weight = 45907
keywords = [ "filter", "rfb", "dissector", "vnc" ]
aliases = [ "/questions/45907" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [VNC (RFB) dissector show not all data](/questions/45907/vnc-rfb-dissector-show-not-all-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45907-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45907-score" class="post-score" title="current number of votes">0</div><span id="post-45907-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If I set filter = "vnc" part of traffic not detected. Filter "tcp.port rq 5900" work more correct. Dissector not show data from packets like UserInit message, ServerInit, handshake, security options and any other data. Just binary data shown like in any another TCP packet. Also shown only data which was sent from server to client. But I want to see packets with queries from client to server.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/2015-09-17_12-03-40_kSODtGhg.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-rfb" rel="tag" title="see questions tagged &#39;rfb&#39;">rfb</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-vnc" rel="tag" title="see questions tagged &#39;vnc&#39;">vnc</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Sep '15, 02:27</strong></p><img src="https://secure.gravatar.com/avatar/190022cb69a9814e45aca6206ef4075c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="QuAzI&#39;s gravatar image" /><p><span>QuAzI</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="QuAzI has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Sep '15, 02:30</strong> </span></p></div></div><div id="comments-container-45907" class="comments-container"><span id="45908"></span><div id="comment-45908" class="comment"><div id="post-45908-score" class="comment-score"></div><div class="comment-text"><p>Can you see any traffic at all from your client to anywhere? If not you have an (unfortunately common) issue with your Windows setup. The usual culprits are 3rd party VPN and AV software, do you have any of those installed?</p></div><div id="comment-45908-info" class="comment-info"><span class="comment-age">(17 Sep '15, 03:19)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="45909"></span><div id="comment-45909" class="comment"><div id="post-45909-score" class="comment-score"></div><div class="comment-text"><p>I have no VPN and AV software installed at this PC. I can see all trafic in real LAN but this host work on VirtualBox 5.0.4 VM.</p><p>VM Network adapter settings:</p><ul><li><p>Attached to: Host-only Adapter</p></li><li><p>Name: VirtualBox Host-Only Ethernet Adapter</p></li></ul></div><div id="comment-45909-info" class="comment-info"><span class="comment-age">(17 Sep '15, 03:41)</span> <span class="comment-user userinfo">QuAzI</span></div></div><span id="45910"></span><div id="comment-45910" class="comment"><div id="post-45910-score" class="comment-score"></div><div class="comment-text"><p>VNC Server is RealVNC-5.2.3 (latest at this moment) with disabled security. I try write VNC client but I can't properly view traffic</p></div><div id="comment-45910-info" class="comment-info"><span class="comment-age">(17 Sep '15, 03:51)</span> <span class="comment-user userinfo">QuAzI</span></div></div><span id="45913"></span><div id="comment-45913" class="comment"><div id="post-45913-score" class="comment-score"></div><div class="comment-text"><p>Thanks. This can help resolve tracing trouble.</p></div><div id="comment-45913-info" class="comment-info"><span class="comment-age">(17 Sep '15, 04:21)</span> <span class="comment-user userinfo">QuAzI</span></div></div></div><div id="comment-tools-45907" class="comment-tools"></div><div class="clear"></div><div id="comment-45907-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45912"></span>

<div id="answer-container-45912" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45912-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45912-score" class="post-score" title="current number of votes">1</div><span id="post-45912-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe VB <a href="https://www.virtualbox.org/wiki/Network_tips">network tracing</a> might help.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '15, 04:14</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-45912" class="comments-container"><span id="45915"></span><div id="comment-45915" class="comment"><div id="post-45915-score" class="comment-score"></div><div class="comment-text"><p>I don't know why but traffic parsed from VB completely decoded now except some TCP packets</p><p><img src="https://osqa-ask.wireshark.org/upfiles/2015-09-17_14-34-57_AZqcJ5Hr.png" alt="alt text" /></p></div><div id="comment-45915-info" class="comment-info"><span class="comment-age">(17 Sep '15, 04:37)</span> <span class="comment-user userinfo">QuAzI</span></div></div><span id="45917"></span><div id="comment-45917" class="comment"><div id="post-45917-score" class="comment-score">1</div><div class="comment-text"><p>That looks normal to me, the first few frames with TCP as the protocol are ones that are "control" information for the TCP connection such as SYN, ACK etc. where there is no VNC protocol information.</p><p>The other reason for frames showing as TCP are where the frame contains a portion of the higher protocol PDU. e.g. frames 45, 46, you should see the completed VNC PDU a little further down.</p></div><div id="comment-45917-info" class="comment-info"><span class="comment-age">(17 Sep '15, 06:13)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="45918"></span><div id="comment-45918" class="comment"><div id="post-45918-score" class="comment-score"></div><div class="comment-text"><p>Thanks for comments. Now everything is good</p></div><div id="comment-45918-info" class="comment-info"><span class="comment-age">(17 Sep '15, 07:12)</span> <span class="comment-user userinfo">QuAzI</span></div></div><span id="45919"></span><div id="comment-45919" class="comment"><div id="post-45919-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-45919-info" class="comment-info"><span class="comment-age">(17 Sep '15, 07:54)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-45912" class="comment-tools"></div><div class="clear"></div><div id="comment-45912-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

