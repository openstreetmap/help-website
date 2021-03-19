+++
type = "question"
title = "Question about ICMP packet between ISP gateway and client PC"
description = '''Hi All, I am a wireshark beginner. I am trying to troubleshoot my home network problem. I ping the gateway bypass my router and get back the ICMP response. But I don&#x27;t know why there are some ICMP responses which are from other destinations instead of gateway. Is it possible to make impact in my rou...'''
date = "2017-09-26T08:52:00Z"
lastmod = "2017-09-27T09:16:00Z"
weight = 63651
keywords = [ "icmp", "wireshark" ]
aliases = [ "/questions/63651" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Question about ICMP packet between ISP gateway and client PC](/questions/63651/question-about-icmp-packet-between-isp-gateway-and-client-pc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63651-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63651-score" class="post-score" title="current number of votes">0</div><span id="post-63651-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All, I am a wireshark beginner. I am trying to troubleshoot my home network problem. I ping the gateway bypass my router and get back the ICMP response. But I don't know why there are some ICMP responses which are from other destinations instead of gateway. <strong><em>Is it possible to make impact in my router(LAN network) ? I sort the packet capture by protocol.</em></strong><img src="https://osqa-ask.wireshark.org/upfiles/1_lUENkPm.png" alt="alt text" /> my ip 119.246.66.11<br />
my gateway ip 119.246.64.1</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-icmp" rel="tag" title="see questions tagged &#39;icmp&#39;">icmp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '17, 08:52</strong></p><img src="https://secure.gravatar.com/avatar/2180cd3810337f1e3431cf6bb918ee63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bennylam1113&#39;s gravatar image" /><p><span>bennylam1113</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bennylam1113 has no accepted answers">0%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Sep '17, 09:13</strong> </span></p></div></div><div id="comments-container-63651" class="comments-container"></div><div id="comment-tools-63651" class="comment-tools"></div><div class="clear"></div><div id="comment-63651-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63652"></span>

<div id="answer-container-63652" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63652-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63652-score" class="post-score" title="current number of votes">0</div><span id="post-63652-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I assume your IP is 119.246.66.11, so it's telling other IP addresses that some ports they try to access on your IP aren't available (the black packets). If you look inside the black packets you'll find quoted packets at the bottom of each packet, telling you what the packet causing the "Port unreachable" message was.</p><p>BTW: in general, it makes no sense to sort the packet list by protocol, because it makes it very hard to see context of the conversation. I recommend filtering on IP pairs instead if you want to limit what you're showing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '17, 09:00</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-63652" class="comments-container"><span id="63653"></span><div id="comment-63653" class="comment"><div id="post-63653-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper,</p><p>thanks first. but i want to know is it a normal situation? I am finding the reason why my network is unstable. ISP problem or my router problem. This is the capture when I connect to router and ping the gateway.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/icmp_2.png" width="640" /></p></div><div id="comment-63653-info" class="comment-info"><span class="comment-age">(26 Sep '17, 09:20)</span> <span class="comment-user userinfo">bennylam1113</span></div></div><span id="63654"></span><div id="comment-63654" class="comment"><div id="post-63654-score" class="comment-score"></div><div class="comment-text"><p>Sorry, had to convert your answer to a comment, which messes up the image scaling (and I can't remember the trick to resize it)...</p><p>You seem to have some packet loss when it comes to ping packets. Ping isn't that reliable unfortunately, so it's only a small indicator of a problem. You'd need to capture problematic TCP connections and determine packet loss for those if you want something more solid. You can determine packet loss by looking (filtering) for TCP analysis symptoms, e.g. Duplicate ACKs, Retransmissions and lost segments.</p></div><div id="comment-63654-info" class="comment-info"><span class="comment-age">(26 Sep '17, 09:40)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="63657"></span><div id="comment-63657" class="comment"><div id="post-63657-score" class="comment-score"></div><div class="comment-text"><p>Hi, I uploaded my packet capture in <a href="https://www.sendspace.com/file/00bplf">https://www.sendspace.com/file/00bplf</a> I will buy books to learn more about wireshark.</p><p>In my ASUS router, issue start in: Sep 27 23:58:46 WAN Connection: Ethernet link up. Sep 27 23:58:46 rc_service: wanduck 390:notify_rc restart_wan_if 0 Sep 27 23:58:48 wan: mac clone: [wan0_hwaddr] == [44:8a:5b:29:d4:05]</p><p>I took this router to my office, to my friends home to check, it is functionable and no any problem. However my friends did not capture any packet. I am so upset. I don't know how to root cause the case. Thank you everyone to share the analyze experience.</p></div><div id="comment-63657-info" class="comment-info"><span class="comment-age">(27 Sep '17, 09:13)</span> <span class="comment-user userinfo">bennylam1113</span></div></div><span id="63658"></span><div id="comment-63658" class="comment"><div id="post-63658-score" class="comment-score">1</div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/145/jasper">@jasper</a></p><p>To fix an overlarge image I replace the link with an <code>&lt;img src="image_URL" width="640" /&gt;</code></p></div><div id="comment-63658-info" class="comment-info"><span class="comment-age">(27 Sep '17, 09:16)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-63652" class="comment-tools"></div><div class="clear"></div><div id="comment-63652-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

