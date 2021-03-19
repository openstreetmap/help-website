+++
type = "question"
title = "Question regarding Wireshark and port mirroring"
description = '''I am trying to use Wireshark to analyze traffic from my Netgear Stora media server to my Xbox 360. I know (after researching here) that if the PC I have Wireshark installed on is connected to a switch, that switch must allow port mirroring.  My setup:  * Comcast Modem --&amp;gt; Linksys Router (e4200) -...'''
date = "2012-06-26T20:25:00Z"
lastmod = "2013-02-01T17:22:00Z"
weight = 12220
keywords = [ "port", "mirroring" ]
aliases = [ "/questions/12220" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Question regarding Wireshark and port mirroring](/questions/12220/question-regarding-wireshark-and-port-mirroring)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12220-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to use Wireshark to analyze traffic from my Netgear Stora media server to my Xbox 360. I know (after researching here) that if the PC I have Wireshark installed on is connected to a switch, that switch must allow port mirroring.</p><p>My setup:<br />
* Comcast Modem --&gt; Linksys Router (e4200) --&gt; Switch 1 (GS105) &amp; Switch 2 (GS108) &amp; Netgear Stora media server<br />
* The PC with Wireshark installed is connected to Switch 1<br />
* The Xbox is connected to Switch 2<br />
* Netgear Stora media server is connected directly to the Linksys router</p><p>My question is, does the switch the Xbox is connected to also have to allow port mirroring for me to see traffic between the Xbox and the Netgear Stora media server via Wireshark installed on the PC or is this even possible the way they are connected?</p><p>I am going to pickup a Netgear GS105e tomorrow for the PC with Wireshark and I need to know if I also need one for the Xbox connection.</p><p>Thanks in advance for the help.</p></div><div id="question-tags" class="tags-container tags">port mirroring</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '12, 20:25</strong></p><img src="https://secure.gravatar.com/avatar/ee05a314fab76a456f6f76efe2e460db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lorigar&#39;s gravatar image" /><p>lorigar<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lorigar has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Jun '12, 17:27</p></div></div><div id="comments-container-12220" class="comments-container"></div><div id="comment-tools-12220" class="comment-tools"></div><div class="clear"></div><div id="comment-12220-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="12223"></span>

<div id="answer-container-12223" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12223-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>A diagram would be better. I interpret your explanation to mean: Switch 1 is connected to a port on the Linksys router, Switch 2 is connected to another port on the Linksys router, and the Stora media server is connected to a third port on the Linksys router:</p><pre><code>                    Linksys
                       |
     ---------------------------------
     |                 |              |
    SW1               SW2            Stora
     |                 |
 Wireshark            XBox</code></pre><p>If that is correct, then traffic between your Stora media server and your XBox will pass through the Linksys router and Switch 2. It will not pass through Switch 1, which is where the Wireshark PC is connected. Since the traffic never reaches Switch 1, port mirroring on that switch will not help and Wireshark will not be able to capture the traffic you're interested in.</p><p>Your Wireshark PC needs to be connected to a switch that the traffic will pass through, and that switch needs to be capable of port mirroring. No, you can't really do what you want with your current setup.</p><p>If you can connect the Wireshark PC to Switch 2, where the XBox is connected, you will be able to use port mirroring to capture the traffic you're interested in. Or, you could connect either the XBox or the Stora media server or both to Switch 1.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '12, 22:14</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span> </br></br></p></div></div><div id="comments-container-12223" class="comments-container"><span id="12251"></span><div id="comment-12251" class="comment"><div id="post-12251-score" class="comment-score"></div><div class="comment-text"><p>Jim -</p><p>Thanks so much for taking the time to answer my question. Your answer is what I was afraid of. I went and purchased a Netgear GS108e switch today which allows port mirroring. If I set it up this way, can I do what I am wanting to do:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture.PNG" alt="alt text" /></p><p>On SW3, ports 2, 3, 4 are mirrored and port 1 is the sniffer/destination</p></div><div id="comment-12251-info" class="comment-info"><span class="comment-age">(27 Jun '12, 17:28)</span> lorigar</div></div><span id="12252"></span><div id="comment-12252" class="comment"><div id="post-12252-score" class="comment-score"></div><div class="comment-text"><p>Yes, this will let you do what you want. If you're only interested in traffic between the XBox and the Stora media server, then it is only necessary to mirror Port 3 OR Port 4 to Port 1. If you mirror both ports 3 AND 4, you will see duplicate traffic in your trace file because packets between the XBox and the Stora media server pass through both ports.</p></div><div id="comment-12252-info" class="comment-info"><span class="comment-age">(27 Jun '12, 17:49)</span> Jim Aragon</div></div><span id="12253"></span><div id="comment-12253" class="comment"><div id="post-12253-score" class="comment-score"></div><div class="comment-text"><p>Okay, thanks so much for the information.</p><p>That is good to know because I'm trying to learn how to analyze network performance using Wireshark and am guessing that duplicate traffic would skew the results.</p><p>Thanks again!</p></div><div id="comment-12253-info" class="comment-info"><span class="comment-age">(27 Jun '12, 18:08)</span> lorigar</div></div></div><div id="comment-tools-12223" class="comment-tools"></div><div class="clear"></div><div id="comment-12223-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18248"></span>

<div id="answer-container-18248" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18248-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try using an inexpensive hub, which is basically a dumb switch. It is dumb because it does not segment Ethernet traffic in the way that a switch does by port. Instead, all traffic from one port is replicated to all other ports. This can be useful to act like a kind of port mirroring.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '13, 17:22</strong></p><img src="https://secure.gravatar.com/avatar/8a506d9b6ca5f6ce9c631a10c4724365?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scurrier03&#39;s gravatar image" /><p>scurrier03<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scurrier03 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-18248" class="comments-container"></div><div id="comment-tools-18248" class="comment-tools"></div><div class="clear"></div><div id="comment-18248-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

