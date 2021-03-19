+++
type = "question"
title = "Can`t capture EtherCAT packet"
description = '''Hello I installed Wireshark v1.4.3 When I tried to capture EtherCAT packet from my Realtek NIC, I can not see the EtherCAT packet. I only can capture DHCP protocol packet.  Should I have to config other option to capture EtherCAT packet?'''
date = "2011-02-16T20:54:00Z"
lastmod = "2013-09-13T01:59:00Z"
weight = 2391
keywords = [ "ethercat" ]
aliases = [ "/questions/2391" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can\`t capture EtherCAT packet](/questions/2391/cant-capture-ethercat-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2391-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>I installed Wireshark v1.4.3</p><p>When I tried to capture EtherCAT packet from my Realtek NIC, I can not see the EtherCAT packet.</p><p>I only can capture DHCP protocol packet.</p><p>Should I have to config other option to capture EtherCAT packet?</p></div><div id="question-tags" class="tags-container tags">ethercat</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '11, 20:54</strong></p><img src="https://secure.gravatar.com/avatar/dcdc3810672c3ab1141e05a55f9a78ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Younghyun%20Jo&#39;s gravatar image" /><p>Younghyun Jo<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Younghyun Jo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Feb '11, 23:10</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-2391" class="comments-container"><span id="8735"></span><div id="comment-8735" class="comment"><div id="post-8735-score" class="comment-score"></div><div class="comment-text"><p>Hello i have a similiar problem. I cant capture ethercat messages. I am connecting to a beckhoff i/o module(EK1100) using a cross network cable. I use Twincat program for ethercat master protocol. There is no problem with the operation of the device. On same pc i use wireshark to monitor messages.</p><p>The program has two modes: run and config mode. I can capture an ethercat message which shows the switching between modes but when input and output values change i can not get a message. In twincat program i can see what has changed. I did not change anythin in wireshark and i have all the plugins, i use version 1.4.3. I could notunderstand what is going on any help will be helpful.</p></div><div id="comment-8735-info" class="comment-info"><span class="comment-age">(31 Jan '12, 11:15)</span> Hakan Kapson</div></div></div><div id="comment-tools-2391" class="comment-tools"></div><div class="clear"></div><div id="comment-2391-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2393"></span>

<div id="answer-container-2393" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2393-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>According to <a href="http://www.ethercat.org/en/technology.html#3.1">http://www.ethercat.org/en/technology.html#3.1</a>, EtherCAT uses either Ethertype 0x88A4 or UDP port 0x88A4. And at the link layer, it's just ethernet.So you don't have to do anything special to be able to capture EtherCAT packets. Take a look at <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a> for information on how to capture in different setups.</p><p>Regarding dissecting of the EtherCAT frame, it's done in a separate plugin, have you installed all the plugins that came with Wireshark?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '11, 22:52</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2393" class="comments-container"><span id="2394"></span><div id="comment-2394" class="comment"><div id="post-2394-score" class="comment-score"></div><div class="comment-text"><p>I am sure I already installed ethercat plugin for wireshark.</p><p>I can see ethercat.dll in Wiresharkplugins1.4.3 directory.</p><p>I don`t know why this problem happened to me.</p><p>Does anyboy has another idea?</p></div><div id="comment-2394-info" class="comment-info"><span class="comment-age">(16 Feb '11, 23:00)</span> Younghyun Jo</div></div><span id="2396"></span><div id="comment-2396" class="comment"><div id="post-2396-score" class="comment-score"></div><div class="comment-text"><p>(I converted your "answer" to a "comment" to adhere to the Q&amp;A nature of this site)</p><p>Is the PC you are capturing on communicating over EtherCAT itself? If not, did you enable "promiscuous mode"? How is your capturing PC connected to the network that transfers EtherCAT messages? Did you check the CaptureSetup link I mentioned earlier?</p></div><div id="comment-2396-info" class="comment-info"><span class="comment-age">(17 Feb '11, 00:35)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-2393" class="comment-tools"></div><div class="clear"></div><div id="comment-2393-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24628"></span>

<div id="answer-container-24628" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24628-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hello, i have come across the same problem. I have found the solution in the Slave Implementation Guide. The steps below are the solution.</p><ol><li>I/O Devices-&gt;your device-&gt;Adapter-&gt;set the Promiscuous Mode( use with Netmon/ Wireshark only)</li><li>Scan Boxes</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '13, 01:59</strong></p><img src="https://secure.gravatar.com/avatar/d009eaf6079a2d8d30d28d456d974dde?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ecatrui&#39;s gravatar image" /><p>Ecatrui<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ecatrui has no accepted answers">0%</span></p></div></div><div id="comments-container-24628" class="comments-container"></div><div id="comment-tools-24628" class="comment-tools"></div><div class="clear"></div><div id="comment-24628-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

