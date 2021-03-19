+++
type = "question"
title = "What&#x27; s the best way to split tcp streams on large pcap files?"
description = '''Hi, I&#x27;m trying to dump all tcp streams from a large pcap file into separate files. I&#x27;ve used the lua interface for doing it at the best way possible. But the problem is that i reach the error &quot;Too many open files&quot; on the operating system because not all flow my and with a FIN and there is no way to ...'''
date = "2015-01-10T13:18:00Z"
lastmod = "2016-07-23T12:36:00Z"
weight = 39030
keywords = [ "large", "lua", "pcap" ]
aliases = [ "/questions/39030" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [What' s the best way to split tcp streams on large pcap files?](/questions/39030/what-s-the-best-way-to-split-tcp-streams-on-large-pcap-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39030-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39030-score" class="post-score" title="current number of votes">0</div><span id="post-39030-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm trying to dump all tcp streams from a large pcap file into separate files. I've used the lua interface for doing it at the best way possible. But the problem is that i reach the error "Too many open files" on the operating system because not all flow my and with a FIN and there is no way to acknowledge that the packet is the last packet on a tcp strem. Thx in advance, Leonardo</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-large" rel="tag" title="see questions tagged &#39;large&#39;">large</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jan '15, 13:18</strong></p><img src="https://secure.gravatar.com/avatar/ab78a806d088c069e693b1ac598ad4fb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="singletron&#39;s gravatar image" /><p><span>singletron</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="singletron has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Jan '15, 09:44</strong> </span></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span></p></div></div><div id="comments-container-39030" class="comments-container"><span id="39052"></span><div id="comment-39052" class="comment"><div id="post-39052-score" class="comment-score">1</div><div class="comment-text"><p>Perhaps there needs to be a way in Lua to open a "Dumper" file in append mode, so you could open and close the appropriate Dumper file on each packet to avoid running out of file handles. (or keep up to a few hundred open at any given time, and close them when you get too many)</p></div><div id="comment-39052-info" class="comment-info"><span class="comment-age">(11 Jan '15, 09:36)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="39053"></span><div id="comment-39053" class="comment"><div id="post-39053-score" class="comment-score">1</div><div class="comment-text"><p>Added enhancement <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10847">bug 10847</a>.</p></div><div id="comment-39053-info" class="comment-info"><span class="comment-age">(11 Jan '15, 09:43)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="39059"></span><div id="comment-39059" class="comment"><div id="post-39059-score" class="comment-score"></div><div class="comment-text"><p>Dumper in append mode would really be a plus and solve this issue. What i'm trying now is to load all the tcp streams into memory and dumping them after into files. But this is a really memory hungry process. What i'm finding out also is that the ByteArray class only accepts hex string as input and that is not compatible with the Tvb raw output also. Will try the BitOp lua module to see if it speeds up the process. But thanks for the feedback!</p></div><div id="comment-39059-info" class="comment-info"><span class="comment-age">(11 Jan '15, 14:29)</span> <span class="comment-user userinfo">singletron</span></div></div><span id="39064"></span><div id="comment-39064" class="comment"><div id="post-39064-score" class="comment-score">1</div><div class="comment-text"><p>You can already create a <code>ByteArray</code> from a <code>Tvb</code> - just create a <code>TvbRange</code> of the <code>Tvb</code>, and call <code>bytes()</code> of the <code>TvbRange</code> - that returns a <code>ByteArray</code>. In other words:</p><pre><code>-- assuming myTvb is a Tvb object
local barray = myTvb():bytes()

-- or this way
local barray = myTvb:range():bytes()

-- or this longer way
local tvbr = myTvb:range()
local barray = tvbr:bytes()</code></pre></div><div id="comment-39064-info" class="comment-info"><span class="comment-age">(11 Jan '15, 16:29)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="39065"></span><div id="comment-39065" class="comment"><div id="post-39065-score" class="comment-score"></div><div class="comment-text"><p>Wow that is cool i think this is going to make my script work in a feasible speed! Many thanks!</p></div><div id="comment-39065-info" class="comment-info"><span class="comment-age">(11 Jan '15, 16:38)</span> <span class="comment-user userinfo">singletron</span></div></div></div><div id="comment-tools-39030" class="comment-tools"></div><div class="clear"></div><div id="comment-39030-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="39042"></span>

<div id="answer-container-39042" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39042-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39042-score" class="post-score" title="current number of votes">0</div><span id="post-39042-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think you might want to use a tool other than Wireshark for that, because as you noticed you'll run into the file handle problem when trying to separate a large number of streams. Right now I'd recommend <a href="https://github.com/simsong/tcpflow">TCPFlow</a>, which should help you getting your streams.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jan '15, 06:02</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-39042" class="comments-container"><span id="39060"></span><div id="comment-39060" class="comment"><div id="post-39060-score" class="comment-score"></div><div class="comment-text"><p>The problem with TCPFlow is that it creates streams into the two way separate flows. I would have to write some extra code to put them together into a single file. Thanks!</p></div><div id="comment-39060-info" class="comment-info"><span class="comment-age">(11 Jan '15, 14:31)</span> <span class="comment-user userinfo">singletron</span></div></div><span id="39061"></span><div id="comment-39061" class="comment"><div id="post-39061-score" class="comment-score"></div><div class="comment-text"><p>And of course it doesn't have the robustness of wireshark if you want to deal with more complex filters.</p></div><div id="comment-39061-info" class="comment-info"><span class="comment-age">(11 Jan '15, 14:32)</span> <span class="comment-user userinfo">singletron</span></div></div><span id="39062"></span><div id="comment-39062" class="comment"><div id="post-39062-score" class="comment-score">1</div><div class="comment-text"><p>You could merge the two flows with mergecap, by timestamp. That can be scripted easily.</p><p>Filtering could be done in Wireshark before exporting the single flows. So that should not be a problem.</p></div><div id="comment-39062-info" class="comment-info"><span class="comment-age">(11 Jan '15, 14:34)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-39042" class="comment-tools"></div><div class="clear"></div><div id="comment-39042-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54256"></span>

<div id="answer-container-54256" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54256-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54256-score" class="post-score" title="current number of votes">0</div><span id="post-54256-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I developed a tool that fits exactly to your needs: <a href="https://github.com/seladb/PcapPlusPlus/tree/master/Examples/PcapSplitter">PcapSplitter</a>. There's also a compiled version for several OS's <a href="https://www.dropbox.com/sh/5go4ca778nu4zrm/AABbpDieIPBWQ0sGFNCWU7mza?dl=0">here</a>. It can split pcap files into streams and it doesn't have a "too many open files" problem as it closes and reopens files during its run. You should run it in the following way to achieve what you need:</p><pre><code>./PcapSplitter -f /path/to/your/file.pcap -o /output/dir -m connection</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '16, 12:36</strong></p><img src="https://secure.gravatar.com/avatar/0b6fc0687623a56d9f42c88153062754?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="seladb&#39;s gravatar image" /><p><span>seladb</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="seladb has no accepted answers">0%</span></p></div></div><div id="comments-container-54256" class="comments-container"></div><div id="comment-tools-54256" class="comment-tools"></div><div class="clear"></div><div id="comment-54256-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

