+++
type = "question"
title = "Decode Packet:  500 USD Reward"
description = '''Dear Friends,  Please find the link to a captured TCP transmission between 2 devices (not from internet). The packets of interst are from a devide at 192.0.0.192 to another devide at 192.0.0.200 . (please filter).  https://we.tl/UXE33nmye8 The packets of interest beginn after 21:15:30. Each PSH pack...'''
date = "2017-10-27T15:19:00Z"
lastmod = "2017-10-29T17:33:00Z"
weight = 64310
keywords = [ "challenge" ]
aliases = [ "/questions/64310" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decode Packet: 500 USD Reward](/questions/64310/decode-packet-500-usd-reward)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64310-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear Friends,</p><p>Please find the link to a captured TCP transmission between 2 devices (not from internet). The packets of interst are from a devide at 192.0.0.192 to another devide at 192.0.0.200 . (please filter).</p><p><a href="https://we.tl/UXE33nmye8">https://we.tl/UXE33nmye8</a></p><p>The packets of interest beginn after 21:15:30. Each PSH packet has a "Data" Payload, which I am not able to decode (understand). Some of the packets have AASCII data, which makes sense, but most of it makes no sense. I am inclined to believe that the data is not encrypted.</p><p>The "Data" is encoding for some numbers (scientific numbers). The first person who can decode and explain how the data is organised in the packets will get a reward of 500 USD.</p><p>Thanks and Regards</p></div><div id="question-tags" class="tags-container tags">challenge</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Oct '17, 15:19</strong></p><img src="https://secure.gravatar.com/avatar/cc2ff464fe93c21b35a895bc5564aed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="guest1&#39;s gravatar image" /><p>guest1<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="guest1 has no accepted answers">0%</span></p></div></div><div id="comments-container-64310" class="comments-container"><span id="64319"></span><div id="comment-64319" class="comment"><div id="post-64319-score" class="comment-score"></div><div class="comment-text"><p>Looks a lot like HP-GL/2.</p></div><div id="comment-64319-info" class="comment-info"><span class="comment-age">(28 Oct '17, 03:04)</span> Jaap ♦</div></div><span id="64320"></span><div id="comment-64320" class="comment"><div id="post-64320-score" class="comment-score"></div><div class="comment-text"><p>Dear Friend you may be right. It is indeed an HP machine. Can you help to get it decoded ?</p></div><div id="comment-64320-info" class="comment-info"><span class="comment-age">(28 Oct '17, 04:26)</span> guest1</div></div><span id="64329"></span><div id="comment-64329" class="comment"><div id="post-64329-score" class="comment-score"></div><div class="comment-text"><p>See <a href="https://en.wikipedia.org/wiki/HP-GL">the Wikipedia page for HP-GL</a> for information about HP-GL and links to HP documents about HP-GL and HP-GL/2.</p></div><div id="comment-64329-info" class="comment-info"><span class="comment-age">(29 Oct '17, 13:35)</span> Guy Harris ♦♦</div></div><span id="64330"></span><div id="comment-64330" class="comment"><div id="post-64330-score" class="comment-score"></div><div class="comment-text"><p>Note also that one port is port 9100; <code>/etc/services</code> on my machine says:</p><pre><code>hp-pdl-datastr  9100/udp     # PDL Data Streaming Port
hp-pdl-datastr  9100/tcp     # PDL Data Streaming Port</code></pre><p>"PDL" probably stands for "Page Description Language", and the page description language in question is probably <a href="https://en.wikipedia.org/wiki/Printer_Command_Language">HP Printer Command Language</a>. As that Wikipedia page says, "HP-GL/2 and PJL are supported by later versions of PCL.", so the data going over the wire is probably some version of HP PCL, with HP-GL/2 included in it.</p><p>See also <a href="http://danieru.com/2013/06/06/what-is-port-9100-how-to-print-to-it/">What is port 9100 &amp; How to print to it</a>.</p></div><div id="comment-64330-info" class="comment-info"><span class="comment-age">(29 Oct '17, 17:30)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-64310" class="comment-tools"></div><div class="clear"></div><div id="comment-64310-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64331"></span>

<div id="answer-container-64331" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64331-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>NOTE: as the banner says</p><blockquote><p>This is our old Q&amp;A Site. Please post any new questions and answers at <a href="http://ask.wireshark.org">ask.wireshark.org</a>.</p></blockquote><p>and this site may become read-only at some point, so you probably won't get much more help here.</p><p>Either you'll have to:</p><ul><li>decode it yourself by hand, using the documentation for HP PCL and HP-GL;</li><li>write a Wireshark dissector for HP PCL, and have it dissect port 9100 traffic;</li><li>have somebody else write the dissector.</li></ul><p>(I'm too busy to work on it right now.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Oct '17, 17:33</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-64331" class="comments-container"></div><div id="comment-tools-64331" class="comment-tools"></div><div class="clear"></div><div id="comment-64331-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

