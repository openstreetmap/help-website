+++
type = "question"
title = "Wireshark filter &quot;tcp&quot; is also showing SIP packets"
description = '''Hi all, Why I type &quot; TCP &quot; in filter box in order to get TCP message,it still display SIP/SDP message ? could you help me to find the reasion ? thanks '''
date = "2013-04-12T01:59:00Z"
lastmod = "2013-04-16T05:28:00Z"
weight = 20369
keywords = [ "filter" ]
aliases = [ "/questions/20369" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark filter "tcp" is also showing SIP packets](/questions/20369/wireshark-filter-tcp-is-also-showing-sip-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20369-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20369-score" class="post-score" title="current number of votes">0</div><span id="post-20369-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>Why I type " TCP " in filter box in order to get TCP message,it still display SIP/SDP message ?</p><p>could you help me to find the reasion ?</p><p>thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Apr '13, 01:59</strong></p><img src="https://secure.gravatar.com/avatar/e74ff5199a4df065348253cd811a89fb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vhungvi&#39;s gravatar image" /><p><span>vhungvi</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vhungvi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Apr '13, 00:12</strong> </span></p></div></div><div id="comments-container-20369" class="comments-container"></div><div id="comment-tools-20369" class="comment-tools"></div><div class="clear"></div><div id="comment-20369-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20379"></span>

<div id="answer-container-20379" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20379-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20379-score" class="post-score" title="current number of votes">1</div><span id="post-20379-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Type 'tcp' in the display filter box, then click the 'Apply' button.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Apr '13, 04:22</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-20379" class="comments-container"><span id="20400"></span><div id="comment-20400" class="comment"><div id="post-20400-score" class="comment-score"></div><div class="comment-text"><p>Thanks for help! But My mean,After click "Apply",it also display " TCP " and "SIP" message ,other protocols isn't displayed ?</p></div><div id="comment-20400-info" class="comment-info"><span class="comment-age">(14 Apr '13, 19:35)</span> <span class="comment-user userinfo">vhungvi</span></div></div><span id="20405"></span><div id="comment-20405" class="comment"><div id="post-20405-score" class="comment-score"></div><div class="comment-text"><p>If you filter for <strong>tcp</strong> you will only see TCP traffic. <a href="http://www.ietf.org/rfc/rfc2543.txt">RFC 2543</a> defines UDP <strong>and</strong> TCP for SIP. So, what you see is a SIP request made via TCP.</p></div><div id="comment-20405-info" class="comment-info"><span class="comment-age">(15 Apr '13, 00:59)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="20444"></span><div id="comment-20444" class="comment"><div id="post-20444-score" class="comment-score"></div><div class="comment-text"><p>hi !It still display all SIP message such as SIP/SDP or SIP within OK,ACK,INVITE ...request.I don't reasion here</p></div><div id="comment-20444-info" class="comment-info"><span class="comment-age">(15 Apr '13, 21:33)</span> <span class="comment-user userinfo">vhungvi</span></div></div><span id="20445"></span><div id="comment-20445" class="comment"><div id="post-20445-score" class="comment-score"></div><div class="comment-text"><p>If you filter for <code>tcp</code> in the display filter box, is it still displaying UDP packets?</p><p>If you believe it is, post a screenshot (showing the entire Wireshark window including the filter and the full dissection of one of the UDP packets in question) and post a comment (not an answer - answers aren't for replies to comments, they're for answers to the original question) giving the URL for the screenshot.</p></div><div id="comment-20445-info" class="comment-info"><span class="comment-age">(15 Apr '13, 21:37)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="20448"></span><div id="comment-20448" class="comment"><div id="post-20448-score" class="comment-score"></div><div class="comment-text"><p><a href="http://imageshack.us/photo/my-images/515/79266666.png/">http://imageshack.us/photo/my-images/515/79266666.png/</a></p><p>here is screenshot.</p></div><div id="comment-20448-info" class="comment-info"><span class="comment-age">(15 Apr '13, 21:52)</span> <span class="comment-user userinfo">vhungvi</span></div></div><span id="20450"></span><div id="comment-20450" class="comment not_top_scorer"><div id="post-20450-score" class="comment-score"></div><div class="comment-text"><p>In that screenshot, the selected packet is a TCP packet.</p><p>Please select one of the UDP packets and take a new screenshot.</p></div><div id="comment-20450-info" class="comment-info"><span class="comment-age">(15 Apr '13, 21:59)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="20451"></span><div id="comment-20451" class="comment not_top_scorer"><div id="post-20451-score" class="comment-score"></div><div class="comment-text"><p>HI Guy Harris!</p><p>I don't know who changes the title to be " Wireshark filter "tcp" is showing UDP packets ".But my problem here that when i filter " TCP ",wireshark still display SIP packets.Please help me explain it.thanks</p></div><div id="comment-20451-info" class="comment-info"><span class="comment-age">(16 Apr '13, 00:11)</span> <span class="comment-user userinfo">vhungvi</span></div></div><span id="20466"></span><div id="comment-20466" class="comment not_top_scorer"><div id="post-20466-score" class="comment-score"></div><div class="comment-text"><blockquote><p>hi !It still display all SIP message such as SIP/SDP or SIP within</p></blockquote><p>as I said: That's most certainly SIP <strong>over TCP</strong> (see my comment above).</p></div><div id="comment-20466-info" class="comment-info"><span class="comment-age">(16 Apr '13, 05:28)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-20379" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-20379-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20452"></span>

<div id="answer-container-20452" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20452-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20452-score" class="post-score" title="current number of votes">0</div><span id="post-20452-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>But my problem here that when i filter " TCP ",wireshark still display SIP packets.</p></blockquote><p>That's <strong><em>NOT</em></strong> a problem! SIP can run over TCP; if you filter for "tcp", Wireshark will show you TCP packets, which includes HTTP(-over-TCP) packets, SMB packets where SMB is running over TCP or over the NetBIOS session service (which runs over TCP), NFS-over-TCP packets, ..., and SIP-over-TCP packets. Expecting not to see any of those packets when you filter for "tcp" is a mistake.</p><p>If you don't want to see SIP packets, use the filter "!sip", which means "not SIP".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '13, 00:17</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Apr '13, 00:18</strong> </span></p></div></div><div id="comments-container-20452" class="comments-container"><span id="20459"></span><div id="comment-20459" class="comment"><div id="post-20459-score" class="comment-score"></div><div class="comment-text"><p>OK!thanks for answering</p><p>I understand it now.</p><p>thanks one more!</p></div><div id="comment-20459-info" class="comment-info"><span class="comment-age">(16 Apr '13, 03:05)</span> <span class="comment-user userinfo">vhungvi</span></div></div></div><div id="comment-tools-20452" class="comment-tools"></div><div class="clear"></div><div id="comment-20452-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

