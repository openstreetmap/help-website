+++
type = "question"
title = "Load capture file from command line, using wireshark.exe"
description = '''How do I load capture file from command line, using wireshark.exe I am unable to load a pcap file into the GUI of Wireshark via a command line load, using run of wireshark.exe. I will put in some options and display filters on the load later. Right now I cannot even seem to get the GUI to load point...'''
date = "2017-03-15T11:20:00Z"
lastmod = "2017-03-15T11:25:00Z"
weight = 60093
keywords = [ "load", "commandline", "command", "line" ]
aliases = [ "/questions/60093" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Load capture file from command line, using wireshark.exe](/questions/60093/load-capture-file-from-command-line-using-wiresharkexe)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60093-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do I load capture file from command line, using wireshark.exe</p><p>I am unable to load a pcap file into the GUI of Wireshark via a command line load, using run of wireshark.exe. I will put in some options and display filters on the load later. Right now I cannot even seem to get the GUI to load pointing at a pcap. I can open the pcap in the GUI by just bringing up the GUI "FIRST" and then opening the pcap, but this way of loading is not going to work for my purposes.</p></div><div id="question-tags" class="tags-container tags">load commandline command line</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Mar '17, 11:20</strong></p><img src="https://secure.gravatar.com/avatar/6e471bff6123375a31e8503a5adde86f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tptools&#39;s gravatar image" /><p>tptools<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tptools has no accepted answers">0%</span></p></div></div><div id="comments-container-60093" class="comments-container"></div><div id="comment-tools-60093" class="comment-tools"></div><div class="clear"></div><div id="comment-60093-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60094"></span>

<div id="answer-container-60094" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60094-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use</p><pre><code>wireshark -r filename</code></pre><p>You can see all command line parameters by running</p><pre><code>wireshark -h</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '17, 11:25</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-60094" class="comments-container"><span id="60095"></span><div id="comment-60095" class="comment"><div id="post-60095-score" class="comment-score"></div><div class="comment-text"><p>Tried that and doesn't work:</p><pre><code>C:\Program Files\Wireshark&gt;wireshark -r D:\Capture\shark 01 now is the Time.pcapng</code></pre></div><div id="comment-60095-info" class="comment-info"><span class="comment-age">(15 Mar '17, 11:39)</span> tptools</div></div><span id="60096"></span><div id="comment-60096" class="comment"><div id="post-60096-score" class="comment-score"></div><div class="comment-text"><p>If your filename has spaces, use quotation marks:</p><pre><code>C:\Program Files\Wireshark&gt;wireshark -r &quot;D:\Capture\shark 01 now is the Time.pcapng&quot;</code></pre></div><div id="comment-60096-info" class="comment-info"><span class="comment-age">(15 Mar '17, 11:40)</span> Jasper ♦♦</div></div><span id="60098"></span><div id="comment-60098" class="comment"><div id="post-60098-score" class="comment-score"></div><div class="comment-text"><p>Figured it out, and is not documented ANYWHERE.. CANNOT have any spaces in the filename of the pcap.</p></div><div id="comment-60098-info" class="comment-info"><span class="comment-age">(15 Mar '17, 13:24)</span> tptools</div></div><span id="60099"></span><div id="comment-60099" class="comment"><div id="post-60099-score" class="comment-score"></div><div class="comment-text"><p>This is NOT good when one uses Wireshark and pcaps within for "forensic" purposes, as I do. Especially when one must maintain MD5 hashes of the files used for evidence and during research of.</p></div><div id="comment-60099-info" class="comment-info"><span class="comment-age">(15 Mar '17, 13:27)</span> tptools</div></div><span id="60102"></span><div id="comment-60102" class="comment"><div id="post-60102-score" class="comment-score"></div><div class="comment-text"><p>Not true. You should have read my comment about putting the filename in quotation marks. And this is not the fault of Wireshark, it's command line behavior that is the same for all programs you run.</p></div><div id="comment-60102-info" class="comment-info"><span class="comment-age">(15 Mar '17, 13:57)</span> Jasper ♦♦</div></div></div><div id="comment-tools-60094" class="comment-tools"></div><div class="clear"></div><div id="comment-60094-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

