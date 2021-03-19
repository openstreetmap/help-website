+++
type = "question"
title = "Extract file included in HTTP upload"
description = '''I have a pcap with a HTTP upload of an image. Wonder if there is a way to extract the image to file with Wireshark.  My Wireshark has version 1.10.6. When I tried &quot;Export Objects&quot; --&amp;gt; HTTP, I got the entire HTTP body of the HTTP POST message. The body includes things like Multi-part boundary etc ...'''
date = "2015-12-05T16:03:00Z"
lastmod = "2015-12-09T07:30:00Z"
weight = 48309
keywords = [ "http", "wireshark" ]
aliases = [ "/questions/48309" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Extract file included in HTTP upload](/questions/48309/extract-file-included-in-http-upload)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48309-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48309-score" class="post-score" title="current number of votes">0</div><span id="post-48309-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a pcap with a HTTP upload of an image. Wonder if there is a way to extract the image to file with Wireshark.<br />
</p><p>My Wireshark has version 1.10.6. When I tried "Export Objects" --&gt; HTTP, I got the entire HTTP body of the HTTP POST message. The body includes things like Multi-part boundary etc and so it's not an image.</p><p><a href="https://www.cloudshark.org/captures/31eb5d62d660">pcap here</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '15, 16:03</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p><span>pktUser1001</span><br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span> </br></p></div></div><div id="comments-container-48309" class="comments-container"></div><div id="comment-tools-48309" class="comment-tools"></div><div class="clear"></div><div id="comment-48309-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="48310"></span>

<div id="answer-container-48310" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48310-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48310-score" class="post-score" title="current number of votes">0</div><span id="post-48310-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pktUser1001 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I get a similar result with 1.12.7., so it looks like a bug of the object export. Please file a bug report at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a></p><p><strong>UPDATE</strong>: same with Wireshark 2.0.0, so definitely a bug or some form of encoding that is not yet implemented in the code. <strong>However</strong> if you remove the leading text lines in the exported file <strong>with a HEX editor</strong> up to '%PNG', you will get the correct image.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Dec '15, 03:39</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Dec '15, 03:47</strong> </span></p></div></div><div id="comments-container-48310" class="comments-container"><span id="48313"></span><div id="comment-48313" class="comment"><div id="post-48313-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt, reported it at: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11859">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11859</a></p></div><div id="comment-48313-info" class="comment-info"><span class="comment-age">(06 Dec '15, 19:12)</span> <span class="comment-user userinfo">pktUser1001</span></div></div></div><div id="comment-tools-48310" class="comment-tools"></div><div class="clear"></div><div id="comment-48310-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="48376"></span>

<div id="answer-container-48376" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48376-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48376-score" class="post-score" title="current number of votes">0</div><span id="post-48376-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use <a href="http://www.netresec.com/?page=Networkminer">NetworkMiner</a> to extract any file uploaded with an HTTP POST. Just open the PCAP and NetworkMiner will carve out the files to disk for you.</p><p><a href="http://www.netresec.com/?page=Networkminer">http://www.netresec.com/?page=Networkminer</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Dec '15, 03:25</strong></p><img src="https://secure.gravatar.com/avatar/f3f4e29f86f75cd52ba86565a658dcd9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Netresec_LJ&#39;s gravatar image" /><p><span>Netresec_LJ</span><br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Netresec_LJ has no accepted answers">0%</span></p></div></div><div id="comments-container-48376" class="comments-container"><span id="48378"></span><div id="comment-48378" class="comment"><div id="post-48378-score" class="comment-score"></div><div class="comment-text"><p><span>@Netresec_LJ</span>, that's good to know. Wonder if NetworkMiner allows user to select a HTTP POST request and extract the files in the HTTP POST body? This allows user to pair up the extracted file with the HTTP request. Thanks.</p></div><div id="comment-48378-info" class="comment-info"><span class="comment-age">(09 Dec '15, 06:18)</span> <span class="comment-user userinfo">pktUser1001</span></div></div><span id="48380"></span><div id="comment-48380" class="comment"><div id="post-48380-score" class="comment-score"></div><div class="comment-text"><p><span>@pktUser1001</span>, NetworkMiner will extract all files from all HTTP POST requests in the loaded PCAP file. But the details you request are available in the "Files" tab of NetworkMiner. You will see the URL and a lot more details there for each extracted file.</p></div><div id="comment-48380-info" class="comment-info"><span class="comment-age">(09 Dec '15, 07:19)</span> <span class="comment-user userinfo">Netresec_LJ</span></div></div><span id="48381"></span><div id="comment-48381" class="comment"><div id="post-48381-score" class="comment-score"></div><div class="comment-text"><p><span>@Netresec_LJ</span>, I saw it now. Very nice. Wish the extracted upload-file will have a HTTP URL in addition to other parameters such as src ip, src port dst ip, dst port etc.</p></div><div id="comment-48381-info" class="comment-info"><span class="comment-age">(09 Dec '15, 07:30)</span> <span class="comment-user userinfo">pktUser1001</span></div></div></div><div id="comment-tools-48376" class="comment-tools"></div><div class="clear"></div><div id="comment-48376-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

