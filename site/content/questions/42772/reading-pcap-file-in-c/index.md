+++
type = "question"
title = "Reading pcap file in C#"
description = '''Hello everyone, I would like to know how to read a pcap file in c#. I don&#x27;t need something which will read it and parse it, because I want to parse it by myself. I just need a hand to have some input before my parse part. I hope that was clear enough. Thank you :)'''
date = "2015-05-31T03:06:00Z"
lastmod = "2015-06-01T04:28:00Z"
weight = 42772
keywords = [ "c#", "pcap", "packet" ]
aliases = [ "/questions/42772" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Reading pcap file in C\#](/questions/42772/reading-pcap-file-in-c)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42772-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone,</p><p>I would like to know how to read a pcap file in c#. I don't need something which will read it and parse it, because I want to parse it by myself. I just need a hand to have some input before my parse part. I hope that was clear enough.</p><p>Thank you :)</p></div><div id="question-tags" class="tags-container tags">c# pcap packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 May '15, 03:06</strong></p><img src="https://secure.gravatar.com/avatar/75ba7cb3a1d2474ae3ff71c0edad54a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="superithy&#39;s gravatar image" /><p>superithy<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="superithy has no accepted answers">0%</span></p></div></div><div id="comments-container-42772" class="comments-container"></div><div id="comment-tools-42772" class="comment-tools"></div><div class="clear"></div><div id="comment-42772-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="42773"></span>

<div id="answer-container-42773" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42773-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You mean you want some information about how a pcap file is structured? See this Wiki Page:</p><p><a href="https://wiki.wireshark.org/Development/LibpcapFileFormat">https://wiki.wireshark.org/Development/LibpcapFileFormat</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '15, 04:29</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-42773" class="comments-container"><span id="42774"></span><div id="comment-42774" class="comment"><div id="post-42774-score" class="comment-score"></div><div class="comment-text"><p>I'll read that.</p><p>Thank you very much ! :)</p></div><div id="comment-42774-info" class="comment-info"><span class="comment-age">(31 May '15, 04:32)</span> superithy</div></div></div><div id="comment-tools-42773" class="comment-tools"></div><div class="clear"></div><div id="comment-42773-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42775"></span>

<div id="answer-container-42775" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42775-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Even though you said you didn't want parser help, you still might look at <a href="https://github.com/PcapDotNet/Pcap.Net">pcap.net</a>. Lots of useful stuff for C# folks there when dealing with pcap files amongst other things.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '15, 07:20</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-42775" class="comments-container"><span id="42776"></span><div id="comment-42776" class="comment"><div id="post-42776-score" class="comment-score"></div><div class="comment-text"><p>And <code>OfflinePacketCommunicator::OpenFile()</code> calls <code>pcap_open_offline()</code>, so it uses libpcap's/WinPcap's code to read capture files, meaning that, even if <em>all</em> you want to do is just read the file and parse the packets yourself, it should be able to do that without you having to write your own code to read pcap files.</p><p>(It also means that, on UN*Xes with newer libpcap and with some form of .NET environment installed, it will also be able to read many pcap-ng files; currently, WinPcap can't read pcap-ng files, but that will probably be possible in a future WinPcap release, once it's based on a newer version of libpcap.)</p></div><div id="comment-42776-info" class="comment-info"><span class="comment-age">(31 May '15, 14:12)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-42775" class="comment-tools"></div><div class="clear"></div><div id="comment-42775-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42790"></span>

<div id="answer-container-42790" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42790-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please try SharpPcap</p><blockquote><p><a href="http://sourceforge.net/projects/sharppcap/">http://sourceforge.net/projects/sharppcap/</a><br />
<a href="https://github.com/rubystream/SharpPcap">https://github.com/rubystream/SharpPcap</a><br />
<a href="http://www.codeproject.com/Articles/12458/SharpPcap-A-Packet-Capture-Framework-for-NET">http://www.codeproject.com/Articles/12458/SharpPcap-A-Packet-Capture-Framework-for-NET</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '15, 04:28</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-42790" class="comments-container"></div><div id="comment-tools-42790" class="comment-tools"></div><div class="clear"></div><div id="comment-42790-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

