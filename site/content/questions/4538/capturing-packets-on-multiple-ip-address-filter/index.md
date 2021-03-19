+++
type = "question"
title = "Capturing Packets on Multiple IP Address (FIlter)"
description = '''I&#x27;m looking for the syntax to do a capture filter on WireShark, by capturing the traffic on several (specific) IP addresses. I understand how to capture a range, and an individual IP address. However, the application I am capturing on is spread of a &#x27;bucket&#x27; of IP addresses/servers, of which other a...'''
date = "2011-06-13T08:08:00Z"
lastmod = "2015-11-10T08:05:00Z"
weight = 4538
keywords = [ "traffic", "packet-capture", "networking", "wireshark" ]
aliases = [ "/questions/4538" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Capturing Packets on Multiple IP Address (FIlter)](/questions/4538/capturing-packets-on-multiple-ip-address-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4538-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4538-score" class="post-score" title="current number of votes">0</div><span id="post-4538-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm looking for the syntax to do a capture filter on WireShark, by capturing the traffic on several (specific) IP addresses. I understand how to capture a range, and an individual IP address. However, the application I am capturing on is spread of a 'bucket' of IP addresses/servers, of which other applications are based within the same range. See my example:</p><p>ECommerce App Servers: 192.168.1.2, 192.168.1.3, 192.168.1.4. - <strong>This is what I want to capture on (filtered on these exact IPs)</strong> I have tried 'host 192.168.1.2 host 192.168.1.3' etc. There are other applications within this range, e.g. PayRoll App is on 192.168.1.5, and I don't want to see any of this in my capture. Therefore 'net 192.168.1.0/24' to capture the whole range will not work for me.</p><p>an anyone provide me the syntax? Is it even possible?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-packet-capture" rel="tag" title="see questions tagged &#39;packet-capture&#39;">packet-capture</span> <span class="post-tag tag-link-networking" rel="tag" title="see questions tagged &#39;networking&#39;">networking</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jun '11, 08:08</strong></p><img src="https://secure.gravatar.com/avatar/5cc656d6aa03b448fd4a48ef863f9cf1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scankified&#39;s gravatar image" /><p><span>scankified</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scankified has no accepted answers">0%</span></p></div></div><div id="comments-container-4538" class="comments-container"></div><div id="comment-tools-4538" class="comment-tools"></div><div class="clear"></div><div id="comment-4538-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4540"></span>

<div id="answer-container-4540" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4540-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4540-score" class="post-score" title="current number of votes">0</div><span id="post-4540-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="scankified has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, you can use the capture filter:</p><pre><code>host 192.168.1.2 or host 192.168.1.3 or host 192.168.1.4</code></pre><p>Or even shorter:</p><pre><code>host 192.168.1.2 or 192.168.1.3 or 192.168.1.4</code></pre><p>If you want to capture a whole subnet, <strong>but</strong> one IP, you can use:</p><pre><code>net 192.168.1.0/24 and not host 192.168.1.5</code></pre><p>Hope this helps!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '11, 08:14</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Jun '11, 10:37</strong> </span></p></div></div><div id="comments-container-4540" class="comments-container"><span id="47470"></span><div id="comment-47470" class="comment"><div id="post-47470-score" class="comment-score"></div><div class="comment-text"><p>This codes not working host ip and others I using a 1.12.8 version</p></div><div id="comment-47470-info" class="comment-info"><span class="comment-age">(10 Nov '15, 07:47)</span> <span class="comment-user userinfo">harutokawasaki</span></div></div><span id="47471"></span><div id="comment-47471" class="comment"><div id="post-47471-score" class="comment-score"></div><div class="comment-text"><p>What's not working? Note you should really raise your own question, not piggy back on another, and in it show the <strong>exact</strong> filter that doesn't work for you</p></div><div id="comment-47471-info" class="comment-info"><span class="comment-age">(10 Nov '15, 08:05)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-4540" class="comment-tools"></div><div class="clear"></div><div id="comment-4540-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

