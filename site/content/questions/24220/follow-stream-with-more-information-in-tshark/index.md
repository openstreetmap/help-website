+++
type = "question"
title = "follow stream with more information in tshark"
description = '''Hi I want to save 2000 streams in separate txt files but for my work I need each of ascii files involes full information about all packets that made the stream like follow tcp in wireshark! I ran this script:  for stream in $(tshark -nlr $file -Y tcp.flags.syn==1 -T fields -e tcp.stream | sort -n | ...'''
date = "2013-08-30T23:43:00Z"
lastmod = "2013-08-31T14:35:00Z"
weight = 24220
keywords = [ "tshark", "wireshark" ]
aliases = [ "/questions/24220" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [follow stream with more information in tshark](/questions/24220/follow-stream-with-more-information-in-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24220-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I want to save 2000 streams in separate txt files but for my work I need each of ascii files involes full information about all packets that made the stream like follow tcp in wireshark!</p><p>I ran this script:</p><pre><code>  for stream in $(tshark -nlr $file -Y tcp.flags.syn==1 -T fields -e tcp.stream | sort -n | uniq | sed &#39;s/\r//&#39;)
    do
        echo &quot;Processing stream $stream&quot;
        tshark -nlr $file -qz &quot;follow,tcp,ascii,$stream&quot; &gt; stream-$stream.log
    done</code></pre><p>but this script give me just a little information like that:</p><pre><code> Follow: tcp,ascii
    Filter: tcp.stream eq 962
    Node 0: 245.234.7.168:51099
    Node 1: 40.170.249.141:80</code></pre><p>I want to save all of information about all packets in the stream in one file. tnx</p></div><div id="question-tags" class="tags-container tags">tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Aug '13, 23:43</strong></p><img src="https://secure.gravatar.com/avatar/372d4c266bc96a0ef9b71b291c582d2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Soroor&#39;s gravatar image" /><p>Soroor<br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Soroor has no accepted answers">0%</span></p></div></div><div id="comments-container-24220" class="comments-container"><span id="24228"></span><div id="comment-24228" class="comment"><div id="post-24228-score" class="comment-score"></div><div class="comment-text"><p>by running this script, information for all of streams are 2 lines "node 0 and node 1"(for stream 0 to 2000) ! for example for stream 0:</p><pre><code>Follow: tcp,ascii
Filter: tcp.stream eq 0
Node 0: 245.234.7.50:57850
Node 1: 40.170.249.45:995</code></pre><p>like stream 962 that I have mentioned before!</p><p>in wireshark with running tcp.stream eq 0 I can see many more information like length,flags,TTL and etc for all packets in that specific stream. is there any script to do this in tshark? cause I need all of this information for programming on my trace in separate stream files. tnx for your attention.</p></div><div id="comment-24228-info" class="comment-info"><span class="comment-age">(31 Aug '13, 07:44)</span> Soroor</div></div></div><div id="comment-tools-24220" class="comment-tools"></div><div class="clear"></div><div id="comment-24220-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="24227"></span>

<div id="answer-container-24227" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24227-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What makes you think there is more information available for that stream, 962 in this case? What more does Wireshark show if you filter using <code>tcp.stream eq 962</code> then <em>"Follow TCP Stream"</em>? More than likely, there's no data being transferred for that particular stream and so there's nothing more to show/save.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Aug '13, 07:15</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-24227" class="comments-container"></div><div id="comment-tools-24227" class="comment-tools"></div><div class="clear"></div><div id="comment-24227-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24242"></span>

<div id="answer-container-24242" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24242-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not sure, but I believe you want to write single TCP conversations/streams into separate files, possibly in pcap format.</p><p>Well, there are several ways to do that.</p><p>Please see the answers for the following questions and the tools mentioned there.</p><blockquote><p><a href="http://ask.wireshark.org/questions/16690/split-pcap-file-into-smaller-pcap-file-according-to-tcp-flow">http://ask.wireshark.org/questions/16690/split-pcap-file-into-smaller-pcap-file-according-to-tcp-flow</a><br />
<a href="http://ask.wireshark.org/questions/4677/easy-way-to-save-tcp-streams">http://ask.wireshark.org/questions/4677/easy-way-to-save-tcp-streams</a><br />
<a href="http://ask.wireshark.org/questions/19995/automated-tcp-reassembler">http://ask.wireshark.org/questions/19995/automated-tcp-reassembler</a><br />
</p></blockquote><p>See also the tools here</p><blockquote><p><a href="http://wiki.wireshark.org/Tools">http://wiki.wireshark.org/Tools</a></p></blockquote><p>If I misunderstand your questions, please add more details.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Aug '13, 14:35</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-24242" class="comments-container"></div><div id="comment-tools-24242" class="comment-tools"></div><div class="clear"></div><div id="comment-24242-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

