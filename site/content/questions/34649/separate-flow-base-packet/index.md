+++
type = "question"
title = "separate flow base packet"
description = '''hello, I have a pcap file and I am going to separate flow base packet ( and save them on file optionally) then separate request and response packet ( and save them on file) I use Linux. Is there any app or method to do this ? thanks'''
date = "2014-07-15T03:08:00Z"
lastmod = "2014-07-27T01:39:00Z"
weight = 34649
keywords = [ "flow" ]
aliases = [ "/questions/34649" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [separate flow base packet](/questions/34649/separate-flow-base-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34649-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>hello, I have a pcap file and I am going to separate flow base packet ( and save them on file optionally) then separate request and response packet ( and save them on file) I use Linux. Is there any app or method to do this ? thanks</p></div><div id="question-tags" class="tags-container tags">flow</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '14, 03:08</strong></p><img src="https://secure.gravatar.com/avatar/d4b0725fbcdc688d55ded6e98ca5e35f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mhch&#39;s gravatar image" /><p>mhch<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mhch has no accepted answers">0%</span></p></div></div><div id="comments-container-34649" class="comments-container"></div><div id="comment-tools-34649" class="comment-tools"></div><div class="clear"></div><div id="comment-34649-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="34651"></span>

<div id="answer-container-34651" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34651-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use tcpflow on Linux</p><blockquote><p><a href="https://github.com/simsong/tcpflow">https://github.com/simsong/tcpflow</a></p></blockquote><p>or tcpick</p><blockquote><p><a href="http://tcpick.sourceforge.net/">http://tcpick.sourceforge.net/</a></p></blockquote><p>Or another tools from the following list</p><blockquote><p><a href="http://wiki.wireshark.org/Tools">http://wiki.wireshark.org/Tools</a></p></blockquote><p>On Windows there is SplitCap</p><blockquote><p><a href="http://www.netresec.com/?page=SplitCap">http://www.netresec.com/?page=SplitCap</a></p></blockquote><p>And finally, you can also use tshark</p><blockquote><p>tshark -nr input.pcap -Y "tcp.stream eq 1" -w stream1.pcap</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '14, 03:16</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-34651" class="comments-container"><span id="34701"></span><div id="comment-34701" class="comment"><div id="post-34701-score" class="comment-score"></div><div class="comment-text"><p>I used tcpflow and separated flows but yet I have problem by response/request separation Can you help me ? thanks</p></div><div id="comment-34701-info" class="comment-info"><span class="comment-age">(16 Jul '14, 03:00)</span> mhch</div></div><span id="34708"></span><div id="comment-34708" class="comment"><div id="post-34708-score" class="comment-score"></div><div class="comment-text"><p>request/response of which protocol?</p></div><div id="comment-34708-info" class="comment-info"><span class="comment-age">(16 Jul '14, 07:51)</span> Kurt Knochner ♦</div></div><span id="34785"></span><div id="comment-34785" class="comment"><div id="post-34785-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt Knochner I have a pcap file that include every protocol like ftp http https and so on. I going to separate every flows and then separate every responses and requests.</p></div><div id="comment-34785-info" class="comment-info"><span class="comment-age">(19 Jul '14, 22:03)</span> mhch</div></div></div><div id="comment-tools-34651" class="comment-tools"></div><div class="clear"></div><div id="comment-34651-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="34929"></span>

<div id="answer-container-34929" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34929-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I wrote a script with bash and used tcpflow in my script this is my script : set -vx read -p "where is your pcap file ? " pcap tcpflow -a -o /tmp/outdir -r $pcap ls /tmp/outdir&gt;/tmp/list while read line do P1=<code>echo $line|cut -d "-" -f 1</code> P2=<code>echo $line|cut -d "-" -f 2</code> if [ -d $P1-$P2 ] || [ -d $P2-$P1 ] then continue else mkdir -p $P1-$P2/$P1 mkdir -p $P1-$P2/$P2 fi find $packets -name "$P1-$P2<em>" -exec mv {} $P1-$P2/$P1 \; find $packets -name "$P2-$P1</em>" -exec mv {} $P1-$P2/$P2 \; done&lt;/tmp/list set +vx</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '14, 01:39</strong></p><img src="https://secure.gravatar.com/avatar/d4b0725fbcdc688d55ded6e98ca5e35f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mhch&#39;s gravatar image" /><p>mhch<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mhch has no accepted answers">0%</span></p></div></div><div id="comments-container-34929" class="comments-container"></div><div id="comment-tools-34929" class="comment-tools"></div><div class="clear"></div><div id="comment-34929-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

