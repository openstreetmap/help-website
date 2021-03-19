+++
type = "question"
title = "tshark follow tcp flow for a 400M pcap file extremely slow"
description = '''I have a 400M bytes pcap file which contains one TCP flow. I want to extract the transferred data on this flow. So I follow tcp flow and extract the data to tmp file. The command is as below. Result of this command is correct. But the performance is very bad. It takes 7~8 minutes. Is there any metho...'''
date = "2017-07-27T06:58:00Z"
lastmod = "2017-07-27T06:58:00Z"
weight = 63178
keywords = [ "performance", "tshark" ]
aliases = [ "/questions/63178" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark follow tcp flow for a 400M pcap file extremely slow](/questions/63178/tshark-follow-tcp-flow-for-a-400m-pcap-file-extremely-slow)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63178-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a 400M bytes pcap file which contains one TCP flow. I want to extract the transferred data on this flow. So I follow tcp flow and extract the data to tmp file. The command is as below. Result of this command is correct. But the performance is very bad. It takes 7~8 minutes. Is there any method to improve the performance?</p><p>tshark -n -r "query29_reconstructFileFTP32705_1.pcap" -q -z "follow,tcp,raw,10.79.46.6:54775,10.140.40.209:60901" &gt; fm_tmp_txt</p></div><div id="question-tags" class="tags-container tags">performance tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '17, 06:58</strong></p><img src="https://secure.gravatar.com/avatar/bc9f7943ad233739add550153eb30642?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hdl2041827&#39;s gravatar image" /><p>hdl2041827<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hdl2041827 has no accepted answers">0%</span></p></div></div><div id="comments-container-63178" class="comments-container"></div><div id="comment-tools-63178" class="comment-tools"></div><div class="clear"></div><div id="comment-63178-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

