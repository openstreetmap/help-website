+++
type = "question"
title = "Follow TCP stream by layer"
description = '''Hello, I&#x27;m analyzing a 3-layer protocol (3 layers on top of tcp), and I use the &quot;Follow TCP stream&quot; a lot. This option, however, shows all data in layers above TCP. Is there a way to use &quot;Follow TCP stream&quot; without viewing all layers above TCP? Can I choose which layers appear? Thanks Nitay'''
date = "2013-08-29T07:46:00Z"
lastmod = "2013-08-31T15:26:00Z"
weight = 24165
keywords = [ "follow.tcp.stream" ]
aliases = [ "/questions/24165" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Follow TCP stream by layer](/questions/24165/follow-tcp-stream-by-layer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24165-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm analyzing a 3-layer protocol (3 layers on top of tcp), and I use the "Follow TCP stream" a lot. This option, however, shows all data in layers above TCP. Is there a way to use "Follow TCP stream" without viewing all layers above TCP? Can I choose which layers appear?</p><p>Thanks</p><p>Nitay</p></div><div id="question-tags" class="tags-container tags">follow.tcp.stream</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Aug '13, 07:46</strong></p><img src="https://secure.gravatar.com/avatar/cf80c41726cc4ecbf60678ed38645f0a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nitay&#39;s gravatar image" /><p>nitay<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nitay has no accepted answers">0%</span></p></div></div><div id="comments-container-24165" class="comments-container"></div><div id="comment-tools-24165" class="comment-tools"></div><div class="clear"></div><div id="comment-24165-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="24245"></span>

<div id="answer-container-24245" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24245-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>In my case - I need it for Modbus communication (Modbus commands on top of ModbusTCP comms - shows as different layers in Wireshark)</p></blockquote><p>If you just need the Modbus fields in text form, you could try to use tshark</p><blockquote><p>tshark -nr input.pcap -R "mbtcp" -T fields -E header=y -e frame.number -e ip.src -e ip.dst -e modbus.func_code -e modbus.data</p></blockquote><p>Sample Output:</p><pre><code>frame.number    ip.src  ip.dst  modbus.func_code        modbus.data
4       192.168.45.20   192.168.45.205  126     05:03:01:00:00:30
5       192.168.45.205  192.168.45.20   126     07:03:01:00:00:30:08:99
6       192.168.45.20   192.168.45.205  126     05:03:10:00:00:30
7       192.168.45.205  192.168.45.20   126
8       192.168.45.20   192.168.45.205  126     05:03:01:0f:ff:51
9       192.168.45.205  192.168.45.20   126     07:03:01:0f:ff:51:d2:21
10      192.168.45.20   192.168.45.205  126     05:03:08:00:01:51</code></pre><p>See the docs for more Modbus fields</p><blockquote><p><a href="http://www.wireshark.org/docs/dfref/m/mbtcp.html">http://www.wireshark.org/docs/dfref/m/mbtcp.html</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Aug '13, 15:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 Aug '13, 15:29</p></div></div><div id="comments-container-24245" class="comments-container"><span id="24276"></span><div id="comment-24276" class="comment"><div id="post-24276-score" class="comment-score"></div><div class="comment-text"><p>I'll try that, thanks! I think it could be nice to add a graphic feature that does exactly that though</p></div><div id="comment-24276-info" class="comment-info"><span class="comment-age">(02 Sep '13, 02:04)</span> nitay</div></div><span id="24280"></span><div id="comment-24280" class="comment"><div id="post-24280-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>I think it could be nice to add a graphic feature that does exactly that though</p></blockquote><p>That feature is already there. Just add <strong>custom columns</strong> with the field names <strong>modbus.func_code</strong> and <strong>modbus.data</strong></p></div><div id="comment-24280-info" class="comment-info"><span class="comment-age">(02 Sep '13, 04:36)</span> Kurt Knochner ♦</div></div><span id="24454"></span><div id="comment-24454" class="comment"><div id="post-24454-score" class="comment-score"></div><div class="comment-text"><p>I mean, something that resembles the "Follow TCP Stream" screen</p></div><div id="comment-24454-info" class="comment-info"><span class="comment-age">(08 Sep '13, 04:13)</span> nitay</div></div><span id="24455"></span><div id="comment-24455" class="comment"><div id="post-24455-score" class="comment-score"></div><div class="comment-text"><p>Modbus doesn't have the concept of beginning and ending a session unlike TCP so there is no "stream" to follow.</p><p>What is it you actually want to see that "resembles a TCP stream"?</p></div><div id="comment-24455-info" class="comment-info"><span class="comment-age">(08 Sep '13, 07:23)</span> grahamb ♦</div></div><span id="24466"></span><div id="comment-24466" class="comment"><div id="post-24466-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I mean, something that resembles the "Follow TCP Stream" screen</p></blockquote><p>Can you please add a sample pcap file and some information about the output you want to have?</p></div><div id="comment-24466-info" class="comment-info"><span class="comment-age">(09 Sep '13, 01:54)</span> Kurt Knochner ♦</div></div><span id="28047"></span><div id="comment-28047" class="comment not_top_scorer"><div id="post-28047-score" class="comment-score"></div><div class="comment-text"><p>I'm sorry for bringing this up again! It seems that the data for packets larger than ~70 bytes isn't being printed. Any idea why?</p></div><div id="comment-28047-info" class="comment-info"><span class="comment-age">(12 Dec '13, 04:31)</span> nitay</div></div><span id="28049"></span><div id="comment-28049" class="comment not_top_scorer"><div id="post-28049-score" class="comment-score"></div><div class="comment-text"><p>can you post a sample capture file somewhere (google drive, dropbox, cloudshark.org or mega.co.nz)?</p></div><div id="comment-28049-info" class="comment-info"><span class="comment-age">(12 Dec '13, 04:52)</span> Kurt Knochner ♦</div></div><span id="28114"></span><div id="comment-28114" class="comment not_top_scorer"><div id="post-28114-score" class="comment-score"></div><div class="comment-text"><p>Converted into its own question: <a href="http://ask.wireshark.org/questions/28050/tshark-doesnt-display-the-longer-data-fields-mbtcp">http://ask.wireshark.org/questions/28050/tshark-doesnt-display-the-longer-data-fields-mbtcp</a></p></div><div id="comment-28114-info" class="comment-info"><span class="comment-age">(15 Dec '13, 01:31)</span> nitay</div></div></div><div id="comment-tools-24245" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-24245-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24177"></span>

<div id="answer-container-24177" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24177-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there a way to use "Follow TCP stream" without viewing all layers above TCP?</p></blockquote><p>No, because "Follow TCP Stream" is intended to show all the bytes of the TCP segments, which means showing all the layers.</p><p>If you can more precisely specify what you want to see, a <em>separate</em> feature could perhaps be implemented to provide that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Aug '13, 15:03</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-24177" class="comments-container"><span id="24238"></span><div id="comment-24238" class="comment"><div id="post-24238-score" class="comment-score"></div><div class="comment-text"><p>Okay, let's take SMB for example, which lies on NetBIOS session service, which runs on TCP. I'd like a way to follow the SMB data without viewing the NetBIOS "noise"</p><p>In my case - I need it for Modbus communication (Modbus commands on top of ModbusTCP comms - shows as different layers in Wireshark)</p></div><div id="comment-24238-info" class="comment-info"><span class="comment-age">(31 Aug '13, 13:09)</span> nitay</div></div><span id="24239"></span><div id="comment-24239" class="comment"><div id="post-24239-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Okay, let's take SMB for example, which lies on NetBIOS session service, which runs on TCP. I'd like a way to follow the SMB data without viewing the NetBIOS "noise"</p></blockquote><p>In Follow TCP Stream, that's <em>all</em> really noise, with the possible exception of text file blocks being read and written and directories being scanned, as it's an attempt to display binary data as "text". If your protocol isn't a largely text-based protocol, Follow TCP Stream is useful only as a quick way to filter the display (run Follow TCP Stream and then close the Follow TCP Stream window).</p><p>In that example, what you want is something very different from Follow TCP Stream; either you want a display that shows, in a separate window, some or all of the dissection at the SMB layer, or you want a way to show, in the main window, SMB without some or all of the layers below it.</p><p>In your particular Modbus example, what <em>exactly</em> are you asking for?</p></div><div id="comment-24239-info" class="comment-info"><span class="comment-age">(31 Aug '13, 13:51)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-24177" class="comment-tools"></div><div class="clear"></div><div id="comment-24177-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

