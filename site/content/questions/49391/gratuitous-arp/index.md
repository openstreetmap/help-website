+++
type = "question"
title = "Gratuitous ARP"
description = '''I have a very small network consisting of 2 MAC minis, 3 Windows PCs, TP-Link router, a Linksys router in bridge mode to act as a wireless repeater and security system DVR. All the Windows PCs report gratuitous ARPS every 2 to 3 seconds from a device that we do not recognize. I have researched this ...'''
date = "2016-01-19T16:21:00Z"
lastmod = "2016-01-19T18:43:00Z"
weight = 49391
keywords = [ "arp", "gratuitous" ]
aliases = [ "/questions/49391" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Gratuitous ARP](/questions/49391/gratuitous-arp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49391-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a very small network consisting of 2 MAC minis, 3 Windows PCs, TP-Link router, a Linksys router in bridge mode to act as a wireless repeater and security system DVR. All the Windows PCs report gratuitous ARPS every 2 to 3 seconds from a device that we do not recognize. I have researched this and I still don't understand why we are getting these. Source : Shenzhen_12:15:40 (ec:71:db:12:15:40)They occur when wireless access is disabled. Does anyone have any ideas? What have I missed? Is there any way to attach a sample (10 frames) to this?<br />
</p><p>Thanks for any assistance!</p></div><div id="question-tags" class="tags-container tags">arp gratuitous</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jan '16, 16:21</strong></p><img src="https://secure.gravatar.com/avatar/a5fbfde85175c811a9ff03dc096b6c11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Olde&#39;s gravatar image" /><p>Olde<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Olde has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-49391" class="comments-container"><span id="49392"></span><div id="comment-49392" class="comment"><div id="post-49392-score" class="comment-score"></div><div class="comment-text"><p>You can upload your trace file to somewhere publicly accessible, like Google Drive, Dropbox, or Cloudshark (www.cloudshark.org) and then edit your question to include the link. There isn't any way to upload here.</p></div><div id="comment-49392-info" class="comment-info"><span class="comment-age">(19 Jan '16, 17:03)</span> Jim Aragon</div></div><span id="49396"></span><div id="comment-49396" class="comment"><div id="post-49396-score" class="comment-score"></div><div class="comment-text"><p>While you upload the file... You can have a look here <a href="http://crnetpackets.com/2015/08/28/special-type-of-arp-packets/">http://crnetpackets.com/2015/08/28/special-type-of-arp-packets/</a></p></div><div id="comment-49396-info" class="comment-info"><span class="comment-age">(19 Jan '16, 22:13)</span> Christian_R</div></div></div><div id="comment-tools-49391" class="comment-tools"></div><div class="clear"></div><div id="comment-49391-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49394"></span>

<div id="answer-container-49394" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49394-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>All the Windows PCs report gratuitous ARPS every 2 to 3 seconds <strong>from a device that we do not recognize</strong>. I have researched this and I still don't understand why we are getting these. Source : Shenzhen_12:15:40 (<strong>ec:71:db</strong>:12:15:40)</p></blockquote><p><strong><a href="https://www.wireshark.org/tools/oui-lookup.html">ec:71:db</a></strong> is the vendor code for "Shenzhen Baichuan Digital Technology Co., Ltd." (<a href="http://www.sz-bcs.com.cn/).">http://www.sz-bcs.com.cn/).</a> They produce/sell <a href="http://www.sz-bcs.com.cn/index.php?c=list&amp;cs=products">IP cameras and DVRs</a>, so the ARPs are most certainly coming from you own DVR system.</p><p>Why is it sending the ARPs? I don't know and (most certainly) we won't be able to figure out by looking at the capture file.</p><p>Probably nothing you should be worried about, but that's a question that should be answered by the vendor of the product.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jan '16, 18:43</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Jan '16, 18:45</p></div></div><div id="comments-container-49394" class="comments-container"><span id="49406"></span><div id="comment-49406" class="comment"><div id="post-49406-score" class="comment-score"></div><div class="comment-text"><p>Thanks to all who responded. I was suspecting the DVR. However, at this time I do not have access to the configuration of the DVR. I am working with the installer to try and resolve this.</p><p>Olde</p></div><div id="comment-49406-info" class="comment-info"><span class="comment-age">(20 Jan '16, 08:52)</span> Olde</div></div></div><div id="comment-tools-49394" class="comment-tools"></div><div class="clear"></div><div id="comment-49394-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

