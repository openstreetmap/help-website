+++
type = "question"
title = "to display specific fields from m2pa pcap on command line using tshark command"
description = '''Hi, I have a m2pa pcap [which contains MAP protocol sigtran traffic] &amp;amp; i want to display what all different opcodes are there in each packet for MAP protocol. I have tried below command which is working fine on MTP2 pcap, but not working on m2pa pcap. tshark -r ul_success.pcap -R &quot;gsm_map&quot; -T fi...'''
date = "2017-05-03T21:35:00Z"
lastmod = "2017-05-04T04:33:00Z"
weight = 61218
keywords = [ "tshark" ]
aliases = [ "/questions/61218" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [to display specific fields from m2pa pcap on command line using tshark command](/questions/61218/to-display-specific-fields-from-m2pa-pcap-on-command-line-using-tshark-command)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61218-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61218-score" class="post-score" title="current number of votes">0</div><span id="post-61218-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a m2pa pcap [which contains MAP protocol sigtran traffic] &amp; i want to display what all different opcodes are there in each packet for MAP protocol. I have tried below command which is working fine on MTP2 pcap, but not working on m2pa pcap.</p><p>tshark -r ul_success.pcap -R "gsm_map" -T fields -e gsm_old.localValue</p><p>After running above command on m2pa pcap, i am getting below printing tshark: -R without -2 is deprecated. For single-pass filtering use -Y. &amp; nothing else as output. can you please help?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '17, 21:35</strong></p><img src="https://secure.gravatar.com/avatar/bebac401dddf6f00ccece933fa717379?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swapnilawale&#39;s gravatar image" /><p><span>swapnilawale</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swapnilawale has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 May '17, 21:45</strong> </span></p></div></div><div id="comments-container-61218" class="comments-container"><span id="61219"></span><div id="comment-61219" class="comment"><div id="post-61219-score" class="comment-score"></div><div class="comment-text"><p>What happens if you replace -R with -Y or add -2 to the command?</p></div><div id="comment-61219-info" class="comment-info"><span class="comment-age">(03 May '17, 21:56)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="61220"></span><div id="comment-61220" class="comment"><div id="post-61220-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/42/anders"></a><a href="https://ask.wireshark.org/users/42/anders">@Anders</a> I tried. it is not giving any output, it will be in waiting state &amp; after sometime same blank screen with no output</p></div><div id="comment-61220-info" class="comment-info"><span class="comment-age">(03 May '17, 22:02)</span> <span class="comment-user userinfo">swapnilawale</span></div></div><span id="61225"></span><div id="comment-61225" class="comment"><div id="post-61225-score" class="comment-score"></div><div class="comment-text"><p>What happens if you run it without "-R", "-T", and "-e"? Do you see the packets decoded up to the MAP layer?</p></div><div id="comment-61225-info" class="comment-info"><span class="comment-age">(04 May '17, 04:33)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-61218" class="comment-tools"></div><div class="clear"></div><div id="comment-61218-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

