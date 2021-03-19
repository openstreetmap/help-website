+++
type = "question"
title = "Sections in a PDML file for a DNS response"
description = '''Hello, I&#x27;m using the &#x27;dns.resp.name&#x27; field(s) in the PDML for a DNS query response packet to find the canonical and alias domain names for the domain requested (I&#x27;m using a response because I want the aliases and canonical domain as well as the one in the DNS request). I noticed that, if an SOA reco...'''
date = "2016-11-19T14:39:00Z"
lastmod = "2016-11-19T14:39:00Z"
weight = 57462
keywords = [ "pdml", "dns" ]
aliases = [ "/questions/57462" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Sections in a PDML file for a DNS response](/questions/57462/sections-in-a-pdml-file-for-a-dns-response)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57462-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm using the 'dns.resp.name' field(s) in the PDML for a DNS query response packet to find the canonical and alias domain names for the domain requested (I'm using a response because I want the aliases and canonical domain as well as the one in the DNS request). I noticed that, if an SOA record is returned, dns.resp.name also captures the root domain of the DNS zone, which is something that I don't want my program to capture when parsing the files.</p><p>I noticed that there are four DNS sections: Questions, Answer RRs, Authority RRs and Additional RRs. SOA records fall into the section of Authority RRs, so I'm hoping that the only record types returned in the Answer RRs section are A and CNAME records - if so, I can limit my program to take domains from this section. Is this correct, or are there others returned in this section as well that I need to be aware of?</p><p>Thanks :)</p></div><div id="question-tags" class="tags-container tags">pdml dns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '16, 14:39</strong></p><img src="https://secure.gravatar.com/avatar/05aa98a3a949c17526355a407a7c506e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lobster&#39;s gravatar image" /><p>Lobster<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lobster has no accepted answers">0%</span></p></div></div><div id="comments-container-57462" class="comments-container"><span id="57468"></span><div id="comment-57468" class="comment"><div id="post-57468-score" class="comment-score"></div><div class="comment-text"><p>Have you thought about PTR records?</p></div><div id="comment-57468-info" class="comment-info"><span class="comment-age">(19 Nov '16, 16:14)</span> Jaap ♦</div></div></div><div id="comment-tools-57462" class="comment-tools"></div><div class="clear"></div><div id="comment-57462-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

