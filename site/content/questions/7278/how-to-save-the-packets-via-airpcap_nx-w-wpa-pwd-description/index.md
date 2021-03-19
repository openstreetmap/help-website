+++
type = "question"
title = "How to save the packets via AirPcap_Nx /w wpa-pwd description"
description = '''Hello,  Thank you for everyone who is working for this site. :) I&#x27;m a AirPcap reseller and one of my customer faced a strange symptom while saving wireless trace via Wireshark. They&#x27;re using WPA-PWD and save the captured trace using Multiple_Capture_files.  Every file size is 50MB and they can decod...'''
date = "2011-11-08T06:29:00Z"
lastmod = "2011-11-20T17:54:00Z"
weight = 7278
keywords = [ "nx", "pwd", "airpcap", "wpa" ]
aliases = [ "/questions/7278" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to save the packets via AirPcap\_Nx /w wpa-pwd description](/questions/7278/how-to-save-the-packets-via-airpcap_nx-w-wpa-pwd-description)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7278-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7278-score" class="post-score" title="current number of votes">0</div><span id="post-7278-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, Thank you for everyone who is working for this site. :) I'm a AirPcap reseller and one of my customer faced a strange symptom while saving wireless trace via Wireshark. They're using WPA-PWD and save the captured trace using Multiple_Capture_files.</p><p>Every file size is 50MB and they can decode the first file without any problem but they can't read the packets from the second files because all packets were encrypted. Of course, user put in their WPA-PWD key. That's why they can open the first captured file without problem. We don't know why Wireshark don't apply WPA-PWD key from the second files while using multiple files. Do anybody have faced this sort of problem? Can user decode all captured files without re-put in WPA-PWD key? Please advise me how to configure Wireshark in this case.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nx" rel="tag" title="see questions tagged &#39;nx&#39;">nx</span> <span class="post-tag tag-link-pwd" rel="tag" title="see questions tagged &#39;pwd&#39;">pwd</span> <span class="post-tag tag-link-airpcap" rel="tag" title="see questions tagged &#39;airpcap&#39;">airpcap</span> <span class="post-tag tag-link-wpa" rel="tag" title="see questions tagged &#39;wpa&#39;">wpa</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '11, 06:29</strong></p><img src="https://secure.gravatar.com/avatar/3e6308f1567aab76eb8e68c5e4a9b284?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sunny%20Hilliter&#39;s gravatar image" /><p><span>Sunny Hilliter</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sunny Hilliter has no accepted answers">0%</span></p></div></div><div id="comments-container-7278" class="comments-container"></div><div id="comment-tools-7278" class="comment-tools"></div><div class="clear"></div><div id="comment-7278-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7522"></span>

<div id="answer-container-7522" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7522-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7522-score" class="post-score" title="current number of votes">0</div><span id="post-7522-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When decrypting data, whether via radiotap or regular packets, the login packets must exist in the file that's being decrypted. When the 2nd or subsequent files captured are loaded those login packets are there, then it can't decrypt the file. I had mentioned this also about a year ago, and I think at the time the recommended resolution was to merge the files. To me that made the files so large that they became difficult to handle. So I just used more specific filters to capture more of what I was looking for to keep the file size smaller.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '11, 17:54</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p><span>John_Modlin</span><br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-7522" class="comments-container"></div><div id="comment-tools-7522" class="comment-tools"></div><div class="clear"></div><div id="comment-7522-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

