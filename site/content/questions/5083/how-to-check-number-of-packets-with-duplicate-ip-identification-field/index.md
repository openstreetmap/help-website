+++
type = "question"
title = "How to check number of packets with duplicate IP identification Field"
description = '''Hello All, I am working on a capture with UDP packet, as a part of problem isolation i need to find if there are any duplicate packets or packet loss. Concerned traffic is passing through multiple service provider / MPLS links and I have sniffer traces from Server as well as Client to conclude on th...'''
date = "2011-07-17T09:34:00Z"
lastmod = "2011-07-19T10:08:00Z"
weight = 5083
keywords = [ "ip", "identification" ]
aliases = [ "/questions/5083" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to check number of packets with duplicate IP identification Field](/questions/5083/how-to-check-number-of-packets-with-duplicate-ip-identification-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5083-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5083-score" class="post-score" title="current number of votes">0</div><span id="post-5083-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All,</p><p>I am working on a capture with UDP packet, as a part of problem isolation i need to find if there are any duplicate packets or packet loss. Concerned traffic is passing through multiple service provider / MPLS links and I have sniffer traces from Server as well as Client to conclude on this as we cannot have service provider end sniffer traces for sure :-).</p><p>Since concerned application is running on UDP the only way I can think to compare captures is with IP Identification field. I have already noticed that its not been changed by firewall in between.<br />
</p><p>Here are my queries.</p><ol><li><p>Is there a way to find out <strong>HOW MANY PACKETS</strong> and <strong>WHICH ONE</strong> are been sent across with same IP identification number in the capture? Please note, there are no fragmentation i have already checked that using ip.flags.mf==1. So, if there are packets with same identification filed we can conclude there are duplicate packets in network for that source and destination. Once we get the concerned IP.id we can apply filter and conclude on which one and after what duration, after some bps, or tailoring etc etc.</p></li><li><p>After going through to close to few thousands packet i can notice that IP Identification filed is getting incremented as 1 on every packet like 18700, 18701 etc. I have analyzed that by creating a column. Now I would like to know is there a way to check if any specific IP ID is missing in capture.<br />
</p></li></ol><p>I am open to run script if needed.</p><p>Regards,</p><p>-Deepak</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-identification" rel="tag" title="see questions tagged &#39;identification&#39;">identification</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jul '11, 09:34</strong></p><img src="https://secure.gravatar.com/avatar/a8aa1b50bd4e70fe64d8c9612d100eb4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Deepak&#39;s gravatar image" /><p><span>Deepak</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Deepak has one accepted answer">25%</span> </br></br></p></div></div><div id="comments-container-5083" class="comments-container"></div><div id="comment-tools-5083" class="comment-tools"></div><div class="clear"></div><div id="comment-5083-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5131"></span>

<div id="answer-container-5131" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5131-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5131-score" class="post-score" title="current number of votes">0</div><span id="post-5131-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Deepak has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>(1) could probably be solved using <a href="http://wiki.wireshark.org/Mate">MATE</a>. As an example, this is a MATE "script" I used to use to detect SCTP retransmissions (that is, multiple packets with the same TSN number):</p><pre><code>   Pdu sctp_pdu Proto sctp Transport ip {
            //Extract addr From ip.addr;
            //Extract port From sctp.port;
            Extract vtag From sctp.verification_tag;
            Extract tsn From sctp.data_tsn;
            //Extract sctp_chunk From sctp.chunk_type;
    };

    Gop sctpretrans On sctp_pdu Match (vtag, tsn) {
            Start();
            Stop(never);
    };

    Done;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '11, 10:08</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-5131" class="comments-container"></div><div id="comment-tools-5131" class="comment-tools"></div><div class="clear"></div><div id="comment-5131-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

