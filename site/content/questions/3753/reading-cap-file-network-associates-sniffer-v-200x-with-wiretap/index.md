+++
type = "question"
title = "reading .cap file (Network Associates Sniffer v 2.00x) with wiretap"
description = '''can anyone point me to wireshark documentation that will tell me how to write a standalone program that reads a .cap file (created by NA Sniffer version 2.0) and give me a pcap_pkthdr offset? Thanks. Mark Young'''
date = "2011-04-27T09:43:00Z"
lastmod = "2011-04-27T10:40:00Z"
weight = 3753
keywords = [ "na", "sniffer", "wiretap" ]
aliases = [ "/questions/3753" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [reading .cap file (Network Associates Sniffer v 2.00x) with wiretap](/questions/3753/reading-cap-file-network-associates-sniffer-v-200x-with-wiretap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3753-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3753-score" class="post-score" title="current number of votes">0</div><span id="post-3753-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>can anyone point me to wireshark documentation that will tell me how to write a standalone program that reads a .cap file (created by NA Sniffer version 2.0) and give me a pcap_pkthdr offset?</p><p>Thanks. Mark Young</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-na" rel="tag" title="see questions tagged &#39;na&#39;">na</span> <span class="post-tag tag-link-sniffer" rel="tag" title="see questions tagged &#39;sniffer&#39;">sniffer</span> <span class="post-tag tag-link-wiretap" rel="tag" title="see questions tagged &#39;wiretap&#39;">wiretap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Apr '11, 09:43</strong></p><img src="https://secure.gravatar.com/avatar/74a9a40762ca34440641198a0cecb073?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="markfyoung&#39;s gravatar image" /><p><span>markfyoung</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="markfyoung has no accepted answers">0%</span></p></div></div><div id="comments-container-3753" class="comments-container"></div><div id="comment-tools-3753" class="comment-tools"></div><div class="clear"></div><div id="comment-3753-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3754"></span>

<div id="answer-container-3754" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3754-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3754-score" class="post-score" title="current number of votes">0</div><span id="post-3754-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The <a href="http://wiki.wireshark.org/Development/LibpcapFileFormat" title="Libpcap file format">Libpcap file format</a> is pretty straightforward. You can implement a reader program in whatever your favorite language is.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '11, 10:33</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-3754" class="comments-container"><span id="3756"></span><div id="comment-3756" class="comment"><div id="post-3756-score" class="comment-score"></div><div class="comment-text"><p>he's not talking about libpcap, he wants to read NAI Sniffer .cap files (do not let the extension fool you into thinking that it is enough to detect the file format or Jaap will hunt you down :-D)</p></div><div id="comment-3756-info" class="comment-info"><span class="comment-age">(27 Apr '11, 10:40)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-3754" class="comment-tools"></div><div class="clear"></div><div id="comment-3754-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3755"></span>

<div id="answer-container-3755" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3755-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3755-score" class="post-score" title="current number of votes">0</div><span id="post-3755-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Uh oh, depending on what you want to do you're in for quite an amount of trouble. I have written a standalone program that reads NAI v2.00 cap files, and it has some strange features that makes reading it quite a challenge (talking about ring buffered captures; quite funny - not to say "annoying" - how they implemented them).</p><p>What you can do is read the source code of the according Wireshark module, which would be in <strong>/wiretap/netxray.c</strong>. Yes, quite confusing, but I guess it's called Netxray because that was the Windows program the DOS-Sniffer was merged with back in... the last century as far as I know.</p><p>Keep in mind that the Wireshark code does not always know what each bit and byte is good for. I have reverse engineered a few of the unknown bytes myself, but I haven't checked if the Wireshark wiretap code knows about their functionality in the meantime. I always wanted to give feedback on those but didn't have the time yet.</p><p>If you can give more details of what you want to do I may be able to give some additional tips.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '11, 10:38</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Apr '11, 10:41</strong> </span></p></div></div><div id="comments-container-3755" class="comments-container"></div><div id="comment-tools-3755" class="comment-tools"></div><div class="clear"></div><div id="comment-3755-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

