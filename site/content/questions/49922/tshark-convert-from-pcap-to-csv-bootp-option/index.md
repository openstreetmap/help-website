+++
type = "question"
title = "tshark convert from pcap to csv bootp option?"
description = '''Hello, I want to convert pcap file to csv.  The pcap file contains only bootp packets. I want export all bootp field (inc. all bootp header info + all options) without specify them. Is it possible ? My final goal is to compare two pcap trace files. Right now, the best result is with:  tshark -nr inp...'''
date = "2016-02-06T03:42:00Z"
lastmod = "2016-02-06T03:42:00Z"
weight = 49922
keywords = [ "tshark", "export-to-csv", "bootp" ]
aliases = [ "/questions/49922" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark convert from pcap to csv bootp option?](/questions/49922/tshark-convert-from-pcap-to-csv-bootp-option)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49922-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,<br />
I want to convert pcap file to csv.<br />
The pcap file contains only bootp packets.<br />
I want export all bootp field (inc. all bootp header info + all options) without specify them. Is it possible ?</p><p>My final goal is to compare two pcap trace files.</p><p>Right now, the best result is with:<br />
</p><blockquote><p>tshark -nr input.pcapng -T pdml</p></blockquote><p>But it is too verbose and once line per packet.</p><p>I also try this:</p><blockquote><p>tshark -r input.pcapng -T fields -e bootp.id -e bootp.hw.mac_addr -e bootp.ip.client -e bootp.option.dhcp -e bootp.option.vendor_class_id -e bootp.option.ip_address_lease_time -e bootp.option.renewal_time_value -e bootp.option.rebinding_time_value -e bootp.option.classless_static.route</p></blockquote><p>But several values of option (for example : bootp.option.classless_static.route) don't be dump into the csv file.</p><p>Thx in adv</p></div><div id="question-tags" class="tags-container tags">tshark export-to-csv bootp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Feb '16, 03:42</strong></p><img src="https://secure.gravatar.com/avatar/60dcaa141db15eabd2113be6f7039fde?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_wooofer_&#39;s gravatar image" /><p>_wooofer_<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_wooofer_ has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-49922" class="comments-container"></div><div id="comment-tools-49922" class="comment-tools"></div><div class="clear"></div><div id="comment-49922-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

