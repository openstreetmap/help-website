+++
type = "question"
title = "implementing autostop condition on packet capture!"
description = '''Im doing a live capture using pcap librery.. pcap_t pcap_open_live(const char device, int snaplen,int promisc, int to_ms, char *errbuf) then i dump it into a file...  pcap_dumper_t pcap_dump_open(pcap_t p, const char *fname) void pcap_dump(u_char user, struct pcap_pkthdr h,u_char *sp) and then disse...'''
date = "2012-02-16T23:11:00Z"
lastmod = "2012-02-16T23:11:00Z"
weight = 9080
keywords = [ "development", "capture", "pcap", "autostop", "wireshark" ]
aliases = [ "/questions/9080" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [implementing autostop condition on packet capture!](/questions/9080/implementing-autostop-condition-on-packet-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9080-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Im doing a live capture using pcap librery..</p><p>pcap_t <em>pcap_open_live(const char</em> device, int snaplen,int promisc, int to_ms, char *errbuf)</p><p>then i dump it into a file...</p><p>pcap_dumper_t <em>pcap_dump_open(pcap_t</em> p, const char *fname)</p><p>void pcap_dump(u_char <em>user, struct pcap_pkthdr</em> h,u_char *sp)</p><p>and then dissecting it using libwireshark..</p><p>now i want to put a tiimer based autostop condition on packet capturing and dumping.. coudnt find a way how to do it.. as pcap doesnt allow.</p><p>suggest me the ways pls!</p></div><div id="question-tags" class="tags-container tags">development capture pcap autostop wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '12, 23:11</strong></p><img src="https://secure.gravatar.com/avatar/425d250364423a7595a3eb9dea779cb2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanny_D&#39;s gravatar image" /><p>Sanny_D<br />
<span class="score" title="0 reputation points">0</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanny_D has 3 accepted answers">50%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Feb '12, 23:14</p></div></div><div id="comments-container-9080" class="comments-container"></div><div id="comment-tools-9080" class="comment-tools"></div><div class="clear"></div><div id="comment-9080-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

