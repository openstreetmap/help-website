+++
type = "question"
title = "how i capture traffic from my huawai usb modem"
description = '''i have a tata photon usb modem.. i have installed winpcap. bt it doesnot showes it in the list of interface list ... now what i have to do to capture the data trafic from my usb modem.. i have also ethernet driver installed on my system...  pls help me '''
date = "2014-11-02T01:01:00Z"
lastmod = "2014-11-06T22:11:00Z"
weight = 37531
keywords = [ "interface", "usbmodem", "list" ]
aliases = [ "/questions/37531" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how i capture traffic from my huawai usb modem](/questions/37531/how-i-capture-traffic-from-my-huawai-usb-modem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37531-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37531-score" class="post-score" title="current number of votes">0</div><span id="post-37531-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i have a tata photon usb modem.. i have installed winpcap. bt it doesnot showes it in the list of interface list ... now what i have to do to capture the data trafic from my usb modem.. i have also ethernet driver installed on my system... pls help me</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span> <span class="post-tag tag-link-usbmodem" rel="tag" title="see questions tagged &#39;usbmodem&#39;">usbmodem</span> <span class="post-tag tag-link-list" rel="tag" title="see questions tagged &#39;list&#39;">list</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Nov '14, 01:01</strong></p><img src="https://secure.gravatar.com/avatar/6fdedfce944cebd7249a5e5010517757?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rahul%20Mourya&#39;s gravatar image" /><p><span>Rahul Mourya</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rahul Mourya has no accepted answers">0%</span></p></div></div><div id="comments-container-37531" class="comments-container"></div><div id="comment-tools-37531" class="comment-tools"></div><div class="clear"></div><div id="comment-37531-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37532"></span>

<div id="answer-container-37532" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37532-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37532-score" class="post-score" title="current number of votes">0</div><span id="post-37532-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As you noticed, WinPcap is not able to see those interfaces. So the only remaining options are:</p><ul><li>Use Microsoft <a href="http://www.microsoft.com/en-us/download/details.aspx?id=4865">Network Monitor</a> or <a href="http://www.microsoft.com/en-us/download/details.aspx?id=44226">Message Analyzer</a> to do the capture</li><li>Use <a href="http://desowin.org/usbpcap/">USBPcap</a> to capture at USB level the modem traffic and use Wireshark 1.12.1 to visualize it</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '14, 04:12</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-37532" class="comments-container"><span id="37636"></span><div id="comment-37636" class="comment"><div id="post-37636-score" class="comment-score"></div><div class="comment-text"><p>bt usbpcap is also not working....</p></div><div id="comment-37636-info" class="comment-info"><span class="comment-age">(06 Nov '14, 21:55)</span> <span class="comment-user userinfo">Rahul Mourya</span></div></div><span id="37637"></span><div id="comment-37637" class="comment"><div id="post-37637-score" class="comment-score"></div><div class="comment-text"><p>Are you sure you followed USBPcap tutorial properly? Are USB packets captured, but not decoded, or USB packets are not captured? USB decoding usually needs the USB enumeration capture so as to know how to decode the traffic. Ensure to start USBPcap before plugging you modem.</p></div><div id="comment-37637-info" class="comment-info"><span class="comment-age">(06 Nov '14, 22:11)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-37532" class="comment-tools"></div><div class="clear"></div><div id="comment-37532-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

