+++
type = "question"
title = "Create a custom text file from wireshark"
description = '''Hi, I have a pcap USB file which I am using to decode a custom protocol. My protocol analyzer expect a stream of hex bytes which I need to export from wireshark. Is there anyway to do this? I need to export only bulk out packets which are issues from the host to the device. Right now I select each p...'''
date = "2016-07-15T03:15:00Z"
lastmod = "2016-07-15T10:21:00Z"
weight = 54073
keywords = [ "hexdump", "usb" ]
aliases = [ "/questions/54073" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Create a custom text file from wireshark](/questions/54073/create-a-custom-text-file-from-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54073-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a pcap USB file which I am using to decode a custom protocol. My protocol analyzer expect a stream of hex bytes which I need to export from wireshark. Is there anyway to do this? I need to export only bulk out packets which are issues from the host to the device. Right now I select each packet and copy this field. <img src="https://osqa-ask.wireshark.org/upfiles/wireshark_Z7YOrYl.png" alt="alt text" /></p><p>I then open a text file and paste the data. The data format looks like this "byte1:byte2:byte3:byte4:....." I need a continous stream of all the bytes, in the capture data section. Does anyone know how to do this?</p></div><div id="question-tags" class="tags-container tags">hexdump usb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '16, 03:15</strong></p><img src="https://secure.gravatar.com/avatar/cee98eff17201224821eee933106b0d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="losang&#39;s gravatar image" /><p>losang<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="losang has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 15 Jul '16, 03:16</p></div></div><div id="comments-container-54073" class="comments-container"></div><div id="comment-tools-54073" class="comment-tools"></div><div class="clear"></div><div id="comment-54073-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54076"></span>

<div id="answer-container-54076" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54076-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe you can use <a href="https://www.wireshark.org/docs/man-pages/tshark.html"><code>tshark</code></a> and <a href="http://linux.die.net/man/1/sed"><code>sed</code></a>?</p><p>For example:</p><pre><code>tshark -r usbfile.pcapng -Y usb.capdata -T fields -e usb.capdata | sed s/://g</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '16, 10:21</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-54076" class="comments-container"><span id="54090"></span><div id="comment-54090" class="comment"><div id="post-54090-score" class="comment-score"></div><div class="comment-text"><p>Let me try that out.</p></div><div id="comment-54090-info" class="comment-info"><span class="comment-age">(15 Jul '16, 19:15)</span> losang</div></div><span id="54095"></span><div id="comment-54095" class="comment"><div id="post-54095-score" class="comment-score"></div><div class="comment-text"><p>I have no idea how complex your protocol is and using which language you have written your analyzer, but have you checked the possibility to write a dissector in Lua, allowing you to code only the dissection logic and get the access to the whole power of Wireshark, such as display filters, export possibilities etc.? Doing the same in C is of course even better but the advantage of Lua is that you do not need to compile Wireshark.</p></div><div id="comment-54095-info" class="comment-info"><span class="comment-age">(16 Jul '16, 05:41)</span> sindy</div></div></div><div id="comment-tools-54076" class="comment-tools"></div><div class="clear"></div><div id="comment-54076-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

