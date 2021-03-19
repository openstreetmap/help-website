+++
type = "question"
title = "Add comment in a PCAP file"
description = '''Hi, I&#x27;m outputting wifi packets in a PCAP file and I&#x27;d like to insert a comment that would be easily seen in wireshark/tcpdump to tell me if I dropped packets while logging. I think pcap standard doesn&#x27;t have anything to add a direct comment but maybe I could add a special 802.11 packet in a way tha...'''
date = "2015-05-19T07:57:00Z"
lastmod = "2017-06-23T15:09:00Z"
weight = 42540
keywords = [ "logging", "pcap" ]
aliases = [ "/questions/42540" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Add comment in a PCAP file](/questions/42540/add-comment-in-a-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42540-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm outputting wifi packets in a PCAP file and I'd like to insert a comment that would be easily seen in wireshark/tcpdump to tell me if I dropped packets while logging.</p><p>I think pcap standard doesn't have anything to add a direct comment but maybe I could add a special 802.11 packet in a way that could make it easy to spot the packet drop count?</p><p>Any idea? Thanks</p></div><div id="question-tags" class="tags-container tags">logging pcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '15, 07:57</strong></p><img src="https://secure.gravatar.com/avatar/3537b17fc33775ad9ec4e969cbd320bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Francois&#39;s gravatar image" /><p>Francois<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Francois has no accepted answers">0%</span></p></div></div><div id="comments-container-42540" class="comments-container"></div><div id="comment-tools-42540" class="comment-tools"></div><div class="clear"></div><div id="comment-42540-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="42541"></span>

<div id="answer-container-42541" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42541-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, why don't you use the PCAPng file format instead? It supports file and frame comments, and it also supports saving the packet drop count.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '15, 08:01</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 May '15, 08:02</p></div></div><div id="comments-container-42541" class="comments-container"><span id="42542"></span><div id="comment-42542" class="comment"><div id="post-42542-score" class="comment-score"></div><div class="comment-text"><p>Will PCAPng work with tcpdump as well?</p></div><div id="comment-42542-info" class="comment-info"><span class="comment-age">(19 May '15, 08:06)</span> Francois</div></div><span id="42543"></span><div id="comment-42543" class="comment"><div id="post-42543-score" class="comment-score"></div><div class="comment-text"><p>that depends on the tcpdump version as far as I know</p></div><div id="comment-42543-info" class="comment-info"><span class="comment-age">(19 May '15, 08:08)</span> Jasper ♦♦</div></div><span id="42551"></span><div id="comment-42551" class="comment"><div id="post-42551-score" class="comment-score"></div><div class="comment-text"><p>I think it has more to do with the version of libpcap than the version of tcpdump, although there may be some undocumented dependencies. I don't see any mention of pcap-ng in the <a href="http://www.tcpdump.org/tcpdump-changes.txt">tcpdump changelog</a>; however, it is mentioned in the <a href="http://www.tcpdump.org/libpcap-changes.txt">libpcap changelog</a>. It appears that limited support for pcap-ng was first added in libpcap 1.1.0 with further pcap-ng related changes made in 1.1.2, 1.2.1, and 1.6.2.</p><p>You could also use either Wireshark or <code>editcap</code> to simply save the pcap file as a pcapng file where you could then add packet comments using Wireshark.</p></div><div id="comment-42551-info" class="comment-info"><span class="comment-age">(19 May '15, 09:37)</span> cmaynard ♦♦</div></div><span id="42553"></span><div id="comment-42553" class="comment"><div id="post-42553-score" class="comment-score"></div><div class="comment-text"><p>Yes, it's a libpcap issue. Newer versions of libpcap can read pcap-ng files, as long as all interfaces in the file have the same link-layer header type and snapshot length (that's a limitation of the current libpcap API), although there's no current WinPcap version based on any of those newer versions). With newer versions of libpcap, tcpdump can read pcap-ng files, although it doesn't see the packet comments (again, an API limitation).</p></div><div id="comment-42553-info" class="comment-info"><span class="comment-age">(19 May '15, 11:37)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-42541" class="comment-tools"></div><div class="clear"></div><div id="comment-42541-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="62271"></span>

<div id="answer-container-62271" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62271-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you don't want to depend on specific libpcap version, I'd advise you to use <a href="https://github.com/seladb/PcapPlusPlus">PcapPlusPlus</a> which has its own implementation of reading and writing pcap-ng files, one which has no dependency on libpcap. Here is a short example of writing a packet and a comment:</p><pre><code>uint8_t* myPacket = ....;
size_t myPacketLen = ....;
timeval timestamp = ....;
char* myComment = ....;

RawPacket rawPacket(myPacket, myPacketLen, timestamp, false);

PcapNgFileWriterDevice pcapngWriter(&quot;my/pcapng/file/path&quot;);
pcapngWriter.open();
pcapngWriter.writePacket(rawPacket, myComment);
pcapngWriter.close();</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jun '17, 15:09</strong></p><img src="https://secure.gravatar.com/avatar/0b6fc0687623a56d9f42c88153062754?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="seladb&#39;s gravatar image" /><p>seladb<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="seladb has no accepted answers">0%</span></p></div></div><div id="comments-container-62271" class="comments-container"><span id="62275"></span><div id="comment-62275" class="comment"><div id="post-62275-score" class="comment-score"></div><div class="comment-text"><p>The reason why the libpcap version matters here is that only sufficiently recent (as in "1.1 and later") versions of libpcap can read pcapng files, so if you write out a pcapng file, it can't be read by libpcap prior to 1.1.0, regardless of <em>what</em> software you use to write it. PcapPlusPlus can't write pcapng files that libpcap prior to 1.1.0 can read - <em>nothing</em> can.</p><p>Perhaps PcapPlusPlus will make it easier for Francois to write pcapng files with comments, but if he wants the files to be readable even by, for example, tcpdump on systems with a pre-1.1.0 libpcap, it can't do that.</p></div><div id="comment-62275-info" class="comment-info"><span class="comment-age">(23 Jun '17, 18:01)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-62271" class="comment-tools"></div><div class="clear"></div><div id="comment-62271-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

