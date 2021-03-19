+++
type = "question"
title = "Tshark command for the wireshark operation"
description = '''Hi, We are using Wireshark to analyse some SIP messages. Some of the SIP messages are coming as &quot;Malformed packets&quot; (15 0.429555 2606:ae00:93a0:3cf3:0:25:410f:901 2001:1890:1001:2c00::7:5 IPA 1909 unknown 0x47 [Malformed Packet]). If I do the following step I can get the actual message. Right click ...'''
date = "2013-04-18T03:47:00Z"
lastmod = "2013-04-18T05:19:00Z"
weight = 20563
keywords = [ "command", "tshark" ]
aliases = [ "/questions/20563" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark command for the wireshark operation](/questions/20563/tshark-command-for-the-wireshark-operation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20563-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20563-score" class="post-score" title="current number of votes">0</div><span id="post-20563-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, We are using Wireshark to analyse some SIP messages. Some of the SIP messages are coming as "Malformed packets" (15 0.429555 2606:ae00:93a0:3cf3:0:25:410f:901 2001:1890:1001:2c00::7:5 IPA 1909 unknown 0x47 [Malformed Packet]). If I do the following step I can get the actual message. Right click the msg -&gt; select the option Decode As... -&gt; Select the option "Do not decode" -&gt; Select the option "both" in the drop down box "TCP" -&gt; click OK button.</p><p>I would like to know if there is a corresponding tshark command for the above operation.</p><p>Regards, Eldho</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-command" rel="tag" title="see questions tagged &#39;command&#39;">command</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '13, 03:47</strong></p><img src="https://secure.gravatar.com/avatar/f325c5c7e6a762c9bd40b37a175cdeb3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Eldho&#39;s gravatar image" /><p><span>Eldho</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Eldho has no accepted answers">0%</span></p></div></div><div id="comments-container-20563" class="comments-container"></div><div id="comment-tools-20563" class="comment-tools"></div><div class="clear"></div><div id="comment-20563-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20565"></span>

<div id="answer-container-20565" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20565-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20565-score" class="post-score" title="current number of votes">0</div><span id="post-20565-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In Wireshark disable the IPA dissector, it's heuristics are too loose in that they pick up SIP traffic as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '13, 04:21</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-20565" class="comments-container"><span id="20568"></span><div id="comment-20568" class="comment"><div id="post-20568-score" class="comment-score"></div><div class="comment-text"><p>Hi Jap, thanks for the reply. But my objective is to get the command-line option so that we can automate the operation.</p></div><div id="comment-20568-info" class="comment-info"><span class="comment-age">(18 Apr '13, 05:19)</span> <span class="comment-user userinfo">Eldho</span></div></div></div><div id="comment-tools-20565" class="comment-tools"></div><div class="clear"></div><div id="comment-20565-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

