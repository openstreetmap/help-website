+++
type = "question"
title = "Wireshark not reassembling tcp/http (jpg)"
description = '''Hi, I am a total newb wireshark user. Downloaded to monitor traffic on home network to protect kids. I am trying to view images that are flowing though the server. The relevant protocol settings (that are enabled by default anyway, on current version - 1.10) are enabled to allow reassembly (TCP/HTTP...'''
date = "2014-06-08T22:09:00Z"
lastmod = "2014-06-09T03:44:00Z"
weight = 33565
keywords = [ "image", "export", "reassemble" ]
aliases = [ "/questions/33565" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark not reassembling tcp/http (jpg)](/questions/33565/wireshark-not-reassembling-tcphttp-jpg)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33565-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am a total newb wireshark user. Downloaded to monitor traffic on home network to protect kids.</p><p>I am trying to view images that are flowing though the server. The relevant protocol settings (that are enabled by default anyway, on current version - 1.10) are enabled to allow reassembly (TCP/HTTP). However when I go to Edit &gt; Export Objects &gt; HTTP - the image files are always broken into 'packets' usually of 1460 byte size. All the tutorials I have seen and read suggest that this window should display complete, reassembled files ready to be saved and viewed. Am I missing something?</p><p>Thanks in advance,</p><p>N</p></div><div id="question-tags" class="tags-container tags">image export reassemble</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '14, 22:09</strong></p><img src="https://secure.gravatar.com/avatar/99432725fc1a1cf29236f2ccbcbb2244?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wakingwoken&#39;s gravatar image" /><p>wakingwoken<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wakingwoken has no accepted answers">0%</span></p></div></div><div id="comments-container-33565" class="comments-container"></div><div id="comment-tools-33565" class="comment-tools"></div><div class="clear"></div><div id="comment-33565-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33568"></span>

<div id="answer-container-33568" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33568-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That usually only happens if "Allow subdissector to reassemble TCP streams" is not activated in the TCP protocol preferences. If you are sure that you have the reassembly enabled for TCP then this looks like a bug to me, unless your capture has a different problem.</p><p>What you could do is to try and see if <a href="http://www.netresec.com/?page=NetworkMiner">Network Miner</a> works with your trace file - if it does, it should be working with Wireshark, too. The free edition only reads pcap formatted files, so if yours is a pcapng file you need to save it in Wireshark as pcap first.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jun '14, 03:44</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-33568" class="comments-container"><span id="33573"></span><div id="comment-33573" class="comment"><div id="post-33573-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply.</p><p>TCP is enabled.</p><p>I should mention I am running RPCAPD on Tomato firmware to enable this capture. Could this have anything to do with it?</p></div><div id="comment-33573-info" class="comment-info"><span class="comment-age">(09 Jun '14, 04:36)</span> wakingwoken</div></div><span id="33574"></span><div id="comment-33574" class="comment"><div id="post-33574-score" class="comment-score"></div><div class="comment-text"><p>...and yes, pcap file works in Network Minor - images display without any fiddly extracting. so easy. Maybe I'll just use NM - did in 2 mins what i've been trying to do for hours in Wireshark!</p></div><div id="comment-33574-info" class="comment-info"><span class="comment-age">(09 Jun '14, 04:47)</span> wakingwoken</div></div><span id="33575"></span><div id="comment-33575" class="comment"><div id="post-33575-score" class="comment-score"></div><div class="comment-text"><p>Go ahead then - Wireshark is great for network analysis, but some specialized tools like NM may work better in certain situations. Still a bit strange that reassembly doesn't seem to work for you...</p></div><div id="comment-33575-info" class="comment-info"><span class="comment-age">(09 Jun '14, 04:49)</span> Jasper ♦♦</div></div><span id="33577"></span><div id="comment-33577" class="comment"><div id="post-33577-score" class="comment-score"></div><div class="comment-text"><p>Well from a brief look, NM cant capture via rpcapd, so i guess i'll be using both, unless Wireshark sorts itself out with a fresh install. Thanks for your help!</p></div><div id="comment-33577-info" class="comment-info"><span class="comment-age">(09 Jun '14, 05:51)</span> wakingwoken</div></div></div><div id="comment-tools-33568" class="comment-tools"></div><div class="clear"></div><div id="comment-33568-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

