+++
type = "question"
title = "Group by mac address"
description = '''Hello, I searched a lot but I don&#x27;t find a solution. I would to know if it is possible in tshark to filter the traffic (in Bytes) for each mac address exemple :  00:ce:56:fd:34:ab -&amp;gt; 8000 Bytes 00:ce:89:fd:37:c8 -&amp;gt; 16788 Bytes  I have started something like this : tshark -r myfile -qz io,stat,...'''
date = "2011-03-01T08:29:00Z"
lastmod = "2011-03-02T10:41:00Z"
weight = 2610
keywords = [ "filter", "mac", "sum", "address" ]
aliases = [ "/questions/2610" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Group by mac address](/questions/2610/group-by-mac-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2610-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2610-score" class="post-score" title="current number of votes">0</div><span id="post-2610-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I searched a lot but I don't find a solution. I would to know if it is possible in tshark to filter the traffic (in Bytes) for each mac address</p><p>exemple :</p><pre><code>00:ce:56:fd:34:ab -&gt; 8000 Bytes
00:ce:89:fd:37:c8 -&gt; 16788 Bytes</code></pre><p>I have started something like this :</p><pre><code>tshark -r myfile -qz io,stat,0,1,SUM(...</code></pre><p>Any idea please ?</p><p>kevin</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-sum" rel="tag" title="see questions tagged &#39;sum&#39;">sum</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Mar '11, 08:29</strong></p><img src="https://secure.gravatar.com/avatar/1a1e2f1e06c192d99dc63a0ddacb74d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="steameraproject&#39;s gravatar image" /><p><span>steameraproject</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="steameraproject has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Mar '11, 14:06</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-2610" class="comments-container"></div><div id="comment-tools-2610" class="comment-tools"></div><div class="clear"></div><div id="comment-2610-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="2615"></span>

<div id="answer-container-2615" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2615-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2615-score" class="post-score" title="current number of votes">0</div><span id="post-2615-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try this:<br />
tshark -r test.pcap -q -z conv,eth,eth.addr==00:ce:56:fd:34:ab -z conv,eth,eth.addr==00:ce:89:fd:37:c8<br />
<br />
Just some other examples:<br />
$ tshark -r test.pcap -q -z conv,eth<br />
$ tshark -r test.pcap -q -z conv,eth -z conv,ip -z conv,tcp<br />
$ tshark -r test.pcap -q -z conv,tcp,ip.addr==192.168.100.1 -z conv,ip,ip.addr==192.168.136.1</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '11, 10:32</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p><span>joke</span><br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Mar '11, 03:40</strong> </span></p></div></div><div id="comments-container-2615" class="comments-container"></div><div id="comment-tools-2615" class="comment-tools"></div><div class="clear"></div><div id="comment-2615-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2633"></span>

<div id="answer-container-2633" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2633-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2633-score" class="post-score" title="current number of votes">0</div><span id="post-2633-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thank you so much for your quick response !! I will try this tomorrow.</p><p>Another question : My goal is to detect abnormal traffic volume during the night (virus...) I do not necessarily know all the mac address as they connect to wifi</p><p>so is it possible to combine the data volume per mac address without knowing them ?</p><p>something like this :</p><pre><code> tshark -r test.pcap -q -z conv,eth,eth.addr==*</code></pre><p>thank you again kevin</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Mar '11, 09:38</strong></p><img src="https://secure.gravatar.com/avatar/1a1e2f1e06c192d99dc63a0ddacb74d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="steameraproject&#39;s gravatar image" /><p><span>steameraproject</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="steameraproject has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-2633" class="comments-container"></div><div id="comment-tools-2633" class="comment-tools"></div><div class="clear"></div><div id="comment-2633-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2635"></span>

<div id="answer-container-2635" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2635-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2635-score" class="post-score" title="current number of votes">0</div><span id="post-2635-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To see all ethernet conversations use:<br />
$ tshark -r test.pcap -q -z conv,eth<br />
<br />
To redirect output to a text file use:<br />
$ tshark -r test.pcap -q -z conv,eth &gt; test.txt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Mar '11, 10:41</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p><span>joke</span><br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div></div><div id="comments-container-2635" class="comments-container"></div><div id="comment-tools-2635" class="comment-tools"></div><div class="clear"></div><div id="comment-2635-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

