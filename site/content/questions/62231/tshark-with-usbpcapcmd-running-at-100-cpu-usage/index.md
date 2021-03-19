+++
type = "question"
title = "tshark with USBPcapCMD running at 100% cpu usage"
description = '''Hi all, i&#x27;m having a problem when im running wireshark/tshark on Windows7 with e.g. tshark.exe -i &#92;.&#92;USBPcap1 everything is running fine, but the taskmanager show me a cpu usage of 100% for USBPCapCMD.exe the whole time the program is running. if i start the USBPCapCMD.exe seperately without the tsh...'''
date = "2017-06-22T03:32:00Z"
lastmod = "2017-06-22T13:17:00Z"
weight = 62231
keywords = [ "usbpcapcmd", "tshark", "wireshark", "usbpcap", "cpu" ]
aliases = [ "/questions/62231" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [tshark with USBPcapCMD running at 100% cpu usage](/questions/62231/tshark-with-usbpcapcmd-running-at-100-cpu-usage)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62231-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62231-score" class="post-score" title="current number of votes">0</div><span id="post-62231-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>i'm having a problem when im running wireshark/tshark on Windows7 with e.g.</p><p>tshark.exe -i \.\USBPcap1 everything is running fine, but the taskmanager show me a cpu usage of 100% for USBPCapCMD.exe the whole time the program is running.</p><p>if i start the USBPCapCMD.exe seperately without the tshark it just takes 1-5% of the cpu usage at all.</p><p>any tips/hints whats the difference between the call of tshark and usbpcapcmd.exe and how i can fix this ?!</p><p>wireshark version is 2.2.7 64-bit, with included USBPcap Version</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-usbpcapcmd" rel="tag" title="see questions tagged &#39;usbpcapcmd&#39;">usbpcapcmd</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-usbpcap" rel="tag" title="see questions tagged &#39;usbpcap&#39;">usbpcap</span> <span class="post-tag tag-link-cpu" rel="tag" title="see questions tagged &#39;cpu&#39;">cpu</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jun '17, 03:32</strong></p><img src="https://secure.gravatar.com/avatar/4476d3d342ad67928c0e111035b7555d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="itsbasti&#39;s gravatar image" /><p><span>itsbasti</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="itsbasti has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Jun '17, 03:34</strong> </span></p></div></div><div id="comments-container-62231" class="comments-container"><span id="62236"></span><div id="comment-62236" class="comment"><div id="post-62236-score" class="comment-score"></div><div class="comment-text"><p>This seems to be a common problem. See also <a href="https://ask.wireshark.org/questions/54676/maxing-out-cpu-monitoring-usb-traffic-on-windows">this</a> question and the answer by sindy. You might try a recent <a href="https://www.wireshark.org/download/automated/">automated</a> version of Wireshark to see if there's any performance improvements over 2.2.7, and if so to report your findings.</p></div><div id="comment-62236-info" class="comment-info"><span class="comment-age">(22 Jun '17, 07:19)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-62231" class="comment-tools"></div><div class="clear"></div><div id="comment-62231-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62250"></span>

<div id="answer-container-62250" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62250-score" class="post-score" title="current number of votes">0</div><span id="post-62250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cmaynard has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is a consequence of extcap interface in USBPcap. See <a href="https://github.com/desowin/usbpcap/issues/32">this issue</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '17, 13:17</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-62250" class="comments-container"></div><div id="comment-tools-62250" class="comment-tools"></div><div class="clear"></div><div id="comment-62250-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

