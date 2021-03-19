+++
type = "question"
title = "I can not capture my fortiClient interface"
description = '''Hi all, I have a Windows 7 PC running wireshark. I connect to another network using Fortinet FortiClient. I need to capture the traffic going through this interface but I can not see this interface in the interfaces list. Reinstalling wireshark didnt help. Do anybody knows how can I add FortiClient ...'''
date = "2013-04-03T02:17:00Z"
lastmod = "2013-04-03T03:19:00Z"
weight = 20037
keywords = [ "forticlient" ]
aliases = [ "/questions/20037" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [I can not capture my fortiClient interface](/questions/20037/i-can-not-capture-my-forticlient-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20037-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20037-score" class="post-score" title="current number of votes">0</div><span id="post-20037-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I have a Windows 7 PC running wireshark. I connect to another network using Fortinet FortiClient. I need to capture the traffic going through this interface but I can not see this interface in the interfaces list. Reinstalling wireshark didnt help.</p><p>Do anybody knows how can I add FortiClient interface to wireshark and capture?</p><p>SSL VPN Forticlient version : 4.0.2143</p><p>Wireshark Version 1.8.5</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-forticlient" rel="tag" title="see questions tagged &#39;forticlient&#39;">forticlient</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Apr '13, 02:17</strong></p><img src="https://secure.gravatar.com/avatar/4b970287cdbdf82db3590652ca6640ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="uyuce&#39;s gravatar image" /><p><span>uyuce</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="uyuce has no accepted answers">0%</span></p></div></div><div id="comments-container-20037" class="comments-container"><span id="20039"></span><div id="comment-20039" class="comment"><div id="post-20039-score" class="comment-score"></div><div class="comment-text"><p>I upgraded to</p><p>wireshark Version 1.8.6 Forticlient:5.0.2.225</p><p>Now I can see the Forticlient interface on the interfaces list but the IP is 0.0.0.0 and I do not see any packets flowing on this interface.</p><p>Don't konw how to fix it.</p></div><div id="comment-20039-info" class="comment-info"><span class="comment-age">(03 Apr '13, 02:57)</span> <span class="comment-user userinfo">uyuce</span></div></div></div><div id="comment-tools-20037" class="comment-tools"></div><div class="clear"></div><div id="comment-20037-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20040"></span>

<div id="answer-container-20040" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20040-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20040-score" class="post-score" title="current number of votes">0</div><span id="post-20040-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Does the FortiClient create a PPP interface? Can you start your SSL-VPN tunnel before starting Wireshark? Does Wireshark correctly list the IP address of the PPP interface when started after establishing the tunnel? Does it show any packets then?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Apr '13, 03:01</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-20040" class="comments-container"><span id="20043"></span><div id="comment-20043" class="comment"><div id="post-20043-score" class="comment-score"></div><div class="comment-text"><p>Yes FortiClient create a PPP interface. I did stop wireshark and Forticlient. Started VPN and after that started wireshark. Wireshark again listed the IP address as 0.0.0.0 and showed no packets. When I check all of the ınterfaces and monitor, I can not see any packets going through the fortinet eighter.</p></div><div id="comment-20043-info" class="comment-info"><span class="comment-age">(03 Apr '13, 03:13)</span> <span class="comment-user userinfo">uyuce</span></div></div><span id="20044"></span><div id="comment-20044" class="comment"><div id="post-20044-score" class="comment-score"></div><div class="comment-text"><p>(please use "add a comment" instead of adding a new answer when adding a reaction to an answer, please see the FAQ for details)</p><p>OK, Wireshark uses WinPcap to list interfaces and to capture from the interfaces. If WinPcap is not able to capture from the FortiClient's PPP interface, you can contact the WinPcap team at <a href="http://www.winpcap.org/contact.htm">http://www.winpcap.org/contact.htm</a></p></div><div id="comment-20044-info" class="comment-info"><span class="comment-age">(03 Apr '13, 03:19)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-20040" class="comment-tools"></div><div class="clear"></div><div id="comment-20040-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

