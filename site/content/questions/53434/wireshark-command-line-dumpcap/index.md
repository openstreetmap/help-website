+++
type = "question"
title = "Wireshark Command Line Dumpcap"
description = '''Hey all, we are running a command line wireshark as shown below. Dumpcap -i 1 –b files:100 –b filesize:100000 –w e:&#92;wireshark&#92;sitenum_p.pcap Today it runs for 100 files and shuts down, I believe by the syntax this is by design. Looking for the ability for it to write the 100 or more files and then o...'''
date = "2016-06-14T04:21:00Z"
lastmod = "2016-06-14T04:21:00Z"
weight = 53434
keywords = [ "commandline", "dumpcap" ]
aliases = [ "/questions/53434" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Command Line Dumpcap](/questions/53434/wireshark-command-line-dumpcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53434-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey all, we are running a command line wireshark as shown below.</p><p>Dumpcap -i 1 –b files:100 –b filesize:100000 –w e:\wireshark\sitenum_p.pcap</p><p>Today it runs for 100 files and shuts down, I believe by the syntax this is by design. Looking for the ability for it to write the 100 or more files and then once completed start over overwriting the directory as needed. Any way to do this via command line?</p><p>Mike</p></div><div id="question-tags" class="tags-container tags">commandline dumpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jun '16, 04:21</strong></p><img src="https://secure.gravatar.com/avatar/7fb57087e2d64846ea7547b6505c122c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="2hype4u&#39;s gravatar image" /><p>2hype4u<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="2hype4u has no accepted answers">0%</span></p></div></div><div id="comments-container-53434" class="comments-container"><span id="53435"></span><div id="comment-53435" class="comment"><div id="post-53435-score" class="comment-score"></div><div class="comment-text"><p>What is your OS and which version and what is your Wireshark version?</p></div><div id="comment-53435-info" class="comment-info"><span class="comment-age">(14 Jun '16, 05:27)</span> Jaap ♦</div></div><span id="53446"></span><div id="comment-53446" class="comment"><div id="post-53446-score" class="comment-score"></div><div class="comment-text"><p>Wireshark 2.0.3, WIndows 2012 R2</p></div><div id="comment-53446-info" class="comment-info"><span class="comment-age">(14 Jun '16, 16:19)</span> 2hype4u</div></div><span id="53469"></span><div id="comment-53469" class="comment"><div id="post-53469-score" class="comment-score"></div><div class="comment-text"><p>Your command should work (I have a line like that running exactly as you want it to) - unless you specify an autostop condition the ringbuffer should go on until you stop it manually.</p></div><div id="comment-53469-info" class="comment-info"><span class="comment-age">(15 Jun '16, 09:40)</span> Jasper ♦♦</div></div><span id="53479"></span><div id="comment-53479" class="comment"><div id="post-53479-score" class="comment-score"></div><div class="comment-text"><p>This works as expected for me on Win 7 and I don't think the different OS will change anything in dumpcap behaviour.</p><p>As a test, try reducing the value of the <code>files</code> and <code>filesize</code> arguments just to see what happens quite quickly.</p></div><div id="comment-53479-info" class="comment-info"><span class="comment-age">(15 Jun '16, 14:01)</span> grahamb ♦</div></div><span id="53487"></span><div id="comment-53487" class="comment"><div id="post-53487-score" class="comment-score"></div><div class="comment-text"><p>not sure why but it stops after running the 100, like clockwork. I actually have my NOC monitoring for when it stops so we can restart it. Not very efficient but we need the captures for troubleshooting. Not sure what is causing it to stop then.</p></div><div id="comment-53487-info" class="comment-info"><span class="comment-age">(16 Jun '16, 01:36)</span> 2hype4u</div></div><span id="53490"></span><div id="comment-53490" class="comment not_top_scorer"><div id="post-53490-score" class="comment-score"></div><div class="comment-text"><p>What is the packet rate on the interface you monitor? Is it a saturated link?</p></div><div id="comment-53490-info" class="comment-info"><span class="comment-age">(16 Jun '16, 02:12)</span> Jaap ♦</div></div><span id="53500"></span><div id="comment-53500" class="comment not_top_scorer"><div id="post-53500-score" class="comment-score"></div><div class="comment-text"><p>What is the <code>e</code> drive? Is it on a remote server? Does it stop after 100 files if you write to a local drive?</p><p>Also, what version of Wireshark/dumpcap are you using?</p></div><div id="comment-53500-info" class="comment-info"><span class="comment-age">(16 Jun '16, 10:38)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-53434" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-53434-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

