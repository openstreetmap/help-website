+++
type = "question"
title = "New to this software, trying to diagnose issues with new isp"
description = '''Hi, I&#x27;m new to trying to diagnose networking issues, but I&#x27;m having lots of trouble with skype and games disconnecting briefly. I just moved, and my apartment complex provides Comcast Xfinity. I&#x27;ve been running WireShark for about 20 minutes and I&#x27;ve already hit 18 Errors and 13 Warnings, which seem...'''
date = "2013-06-16T17:59:00Z"
lastmod = "2013-06-17T07:06:00Z"
weight = 22108
keywords = [ "timeout" ]
aliases = [ "/questions/22108" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [New to this software, trying to diagnose issues with new isp](/questions/22108/new-to-this-software-trying-to-diagnose-issues-with-new-isp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22108-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22108-score" class="post-score" title="current number of votes">0</div><span id="post-22108-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm new to trying to diagnose networking issues, but I'm having lots of trouble with skype and games disconnecting briefly. I just moved, and my apartment complex provides Comcast Xfinity. I've been running WireShark for about 20 minutes and I've already hit 18 Errors and 13 Warnings, which seems like a lot. I'm not sure where to start in diagnosing these issues, but my goal is to establish a really solid connection. Most of my errors list either Malformed Packet or Unexpected EID Prefix AFI. Can anyone help me out? If so, do you need any more information? Thanks for your time :)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timeout" rel="tag" title="see questions tagged &#39;timeout&#39;">timeout</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jun '13, 17:59</strong></p><img src="https://secure.gravatar.com/avatar/92e7c7febedb72d3e7a4914c00b2677f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="legendml&#39;s gravatar image" /><p><span>legendml</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="legendml has no accepted answers">0%</span></p></div></div><div id="comments-container-22108" class="comments-container"><span id="22109"></span><div id="comment-22109" class="comment"><div id="post-22109-score" class="comment-score"></div><div class="comment-text"><p>Assuming there's nothing sensitive or confidiential in the trace, can you start by saving the packets you captured as a file (File &gt; Save As), and upload it (<a href="http://cloudshark.org">http://cloudshark.org</a>) then post the URL to the capture?</p><p>The warnings and errors you see might not actually be a problem. With default settings there are a few common false-positives that Wireshark will complain about. The malformed packet complaint may just mean that it's trying to decode it as the wrong protocol for example.</p></div><div id="comment-22109-info" class="comment-info"><span class="comment-age">(16 Jun '13, 18:30)</span> <span class="comment-user userinfo">Quadratic</span></div></div><span id="22111"></span><div id="comment-22111" class="comment"><div id="post-22111-score" class="comment-score"></div><div class="comment-text"><p>Sure, is there any way to parse these recordings? The recording I have is far too large to upload.</p><p>Here's a 2nd scan with 15 errors in under 3 minutes <a href="http://cloudshark.org/captures/cbc3e08111bb">http://cloudshark.org/captures/cbc3e08111bb</a></p></div><div id="comment-22111-info" class="comment-info"><span class="comment-age">(16 Jun '13, 20:44)</span> <span class="comment-user userinfo">legendml</span></div></div></div><div id="comment-tools-22108" class="comment-tools"></div><div class="clear"></div><div id="comment-22108-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22118"></span>

<div id="answer-container-22118" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22118-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22118-score" class="post-score" title="current number of votes">0</div><span id="post-22118-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are a lot of ICMP Destination unreachable messages in your capture ("Host unreachable", "Port Unreachable", "Communication administratively filtered"). That could be either your own (misconfigured) firewall, or a (misconfigured) firewall at the ISP that drop some UDP connections.</p><p>After you have checked your own Firewall, please contact your ISP and ask them for help.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '13, 06:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-22118" class="comments-container"></div><div id="comment-tools-22118" class="comment-tools"></div><div class="clear"></div><div id="comment-22118-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22120"></span>

<div id="answer-container-22120" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22120-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22120-score" class="post-score" title="current number of votes">0</div><span id="post-22120-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looking at your capture file, I see about 250 Kbit of uplink traffic (mostly bittorrent). I also see quite a few retransmissions. Some of the retransmissions are caused by the ACK from you back to the server not reaching the server, others seem to be caused by data segments that you send but we're not received by the remote end. It looks like your uplink is having problems.</p><p>What are the specifications of this internet connection with regards to up/down speed? And are you the only sharing the Internet connection with others in your apartment complex? You might (collectively) saturate your uplink.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '13, 07:06</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-22120" class="comments-container"></div><div id="comment-tools-22120" class="comment-tools"></div><div class="clear"></div><div id="comment-22120-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

