+++
type = "question"
title = "How to display &quot; Full request URI&quot; in the Columns please?"
description = '''Hi, I got a problem using Wireshark. When I used wireshark to capture packets,only display seven columns,number,time,source IP,destination IP,protocal,length,infomation.I want to display &quot;Full request URI&quot;,But there are no &quot;Full reques URI&quot; in the &quot;Display All&quot; which contained in the &quot;Displayed colu...'''
date = "2013-04-06T19:58:00Z"
lastmod = "2013-04-08T02:18:00Z"
weight = 20143
keywords = [ "wireshart", "request", "http" ]
aliases = [ "/questions/20143" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to display " Full request URI" in the Columns please?](/questions/20143/how-to-display-full-request-uri-in-the-columns-please)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20143-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20143-score" class="post-score" title="current number of votes">0</div><span id="post-20143-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I got a problem using Wireshark. When I used wireshark to capture packets,only display seven columns,number,time,source IP,destination IP,protocal,length,infomation.I want to display "Full request URI",But there are no "Full reques URI" in the "Display All" which contained in the "Displayed columns".How to display " Full request URI" in the Columns please?</p><p>Tips:I had seen someone's wireshark that could display "Full request URI" in the columns,but he didn't know how to set.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshart" rel="tag" title="see questions tagged &#39;wireshart&#39;">wireshart</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '13, 19:58</strong></p><img src="https://secure.gravatar.com/avatar/a5787fc0a393220b43b03769e140343a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="manlei&#39;s gravatar image" /><p><span>manlei</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="manlei has no accepted answers">0%</span></p></div></div><div id="comments-container-20143" class="comments-container"></div><div id="comment-tools-20143" class="comment-tools"></div><div class="clear"></div><div id="comment-20143-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20144"></span>

<div id="answer-container-20144" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20144-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20144-score" class="post-score" title="current number of votes">3</div><span id="post-20144-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Go to the packet details pane and expand the HTTP Request which contains the field "full request URI" and right click on that field .You can get a new window with multiple options where u will see apply as column .Click that and you are good to go.Your full request uri will be displayed as column along with 7 defaults in your packet list pane.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Apr '13, 20:09</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Apr '13, 20:11</strong> </span></p></div></div><div id="comments-container-20144" class="comments-container"><span id="20150"></span><div id="comment-20150" class="comment"><div id="post-20150-score" class="comment-score"></div><div class="comment-text"><p>Thanks,let me try.</p></div><div id="comment-20150-info" class="comment-info"><span class="comment-age">(07 Apr '13, 04:45)</span> <span class="comment-user userinfo">manlei</span></div></div><span id="20163"></span><div id="comment-20163" class="comment"><div id="post-20163-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot! As you say ,I successfully added "Full request URI" in the columns.</p></div><div id="comment-20163-info" class="comment-info"><span class="comment-age">(08 Apr '13, 01:06)</span> <span class="comment-user userinfo">manlei</span></div></div><span id="20164"></span><div id="comment-20164" class="comment"><div id="post-20164-score" class="comment-score"></div><div class="comment-text"><p>Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-20164-info" class="comment-info"><span class="comment-age">(08 Apr '13, 02:18)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-20144" class="comment-tools"></div><div class="clear"></div><div id="comment-20144-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

