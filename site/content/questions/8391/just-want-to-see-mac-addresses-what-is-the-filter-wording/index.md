+++
type = "question"
title = "Just want to See MAC Addresses - what is the filter wording?"
description = '''Hi Big Time NEWBIE, just want to know the simple filter term for finding MAC addresses. Can someone please quickly tell me the right filter command string to display MAC only. Also if the command can be written in a way to not show my own MAC address. Thanks PEter'''
date = "2012-01-15T01:31:00Z"
lastmod = "2012-01-17T06:03:00Z"
weight = 8391
keywords = [ "filter", "mac" ]
aliases = [ "/questions/8391" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Just want to See MAC Addresses - what is the filter wording?](/questions/8391/just-want-to-see-mac-addresses-what-is-the-filter-wording)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8391-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8391-score" class="post-score" title="current number of votes">0</div><span id="post-8391-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Big Time NEWBIE, just want to know the simple filter term for finding MAC addresses. Can someone please quickly tell me the right filter command string to display MAC only.</p><p>Also if the command can be written in a way to not show my own MAC address.</p><p>Thanks</p><p>PEter</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '12, 01:31</strong></p><img src="https://secure.gravatar.com/avatar/da264e007810c26d828829e577161848?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="morpheyous&#39;s gravatar image" /><p><span>morpheyous</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="morpheyous has no accepted answers">0%</span></p></div></div><div id="comments-container-8391" class="comments-container"><span id="8397"></span><div id="comment-8397" class="comment"><div id="post-8397-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by "display MAC only"?</p></div><div id="comment-8397-info" class="comment-info"><span class="comment-age">(15 Jan '12, 19:38)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="8402"></span><div id="comment-8402" class="comment"><div id="post-8402-score" class="comment-score"></div><div class="comment-text"><p>just want to apply a filter that display's only Mac addresses only. Dont know how to write the filter as I am a noob</p><p>Ta Pete</p></div><div id="comment-8402-info" class="comment-info"><span class="comment-age">(16 Jan '12, 01:37)</span> <span class="comment-user userinfo">morpheyous</span></div></div><span id="8414"></span><div id="comment-8414" class="comment"><div id="post-8414-score" class="comment-score"></div><div class="comment-text"><p>By "displays only MAC addresses" do you mean that you want to display only packets going to or from particular MAC addresses (but still display all the columns for those packets and, when you select a packet, display all the details of the packet)?</p></div><div id="comment-8414-info" class="comment-info"><span class="comment-age">(16 Jan '12, 10:49)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-8391" class="comment-tools"></div><div class="clear"></div><div id="comment-8391-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8392"></span>

<div id="answer-container-8392" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8392-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8392-score" class="post-score" title="current number of votes">1</div><span id="post-8392-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>remember not to type the qoutes</p><p>source mac filter: "ether.src == macaddress"</p><p>destination mac filter: "ether.dst == macaddress"</p><p>either mac filter: "ether.addr == macaddress"</p><p>to exclude a mac address just put a ! in front of your syntax</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jan '12, 04:12</strong></p><img src="https://secure.gravatar.com/avatar/dbc4d8cb6be85bd586ca4bf211e1337c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thetechfirm&#39;s gravatar image" /><p><span>thetechfirm</span><br />
<span class="score" title="64 reputation points">64</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thetechfirm has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Jan '12, 03:37</strong> </span></p></div></div><div id="comments-container-8392" class="comments-container"><span id="8396"></span><div id="comment-8396" class="comment"><div id="post-8396-score" class="comment-score"></div><div class="comment-text"><p>thetechfirm, thanks so much for replying, as mentioned I am a newbie, i tried placing your exact words in the filter box but got errors. Can u please advise of the exact terms to be put in the filter box, perhaps u can surround with "" for ease.</p><p>Thx</p><p>Pete</p></div><div id="comment-8396-info" class="comment-info"><span class="comment-age">(15 Jan '12, 19:29)</span> <span class="comment-user userinfo">morpheyous</span></div></div><span id="8405"></span><div id="comment-8405" class="comment"><div id="post-8405-score" class="comment-score"></div><div class="comment-text"><p>just edited my response for clarity. I assumed you wanted a display or post capture filter. capture filter syntax would be "ether host macaddress" (without the qoutes)</p></div><div id="comment-8405-info" class="comment-info"><span class="comment-age">(16 Jan '12, 03:39)</span> <span class="comment-user userinfo">thetechfirm</span></div></div><span id="8407"></span><div id="comment-8407" class="comment"><div id="post-8407-score" class="comment-score"></div><div class="comment-text"><p>look I am really sorry, but I get 'not a valid protocol error'</p></div><div id="comment-8407-info" class="comment-info"><span class="comment-age">(16 Jan '12, 06:38)</span> <span class="comment-user userinfo">morpheyous</span></div></div><span id="8409"></span><div id="comment-8409" class="comment"><div id="post-8409-score" class="comment-score"></div><div class="comment-text"><p>Hmmm... I just whipped this video up to illustrate. Let me know if it helps. http://www.youtube.com/watch?v=bvBfOpOYDOc</p></div><div id="comment-8409-info" class="comment-info"><span class="comment-age">(16 Jan '12, 09:16)</span> <span class="comment-user userinfo">thetechfirm</span></div></div><span id="8424"></span><div id="comment-8424" class="comment"><div id="post-8424-score" class="comment-score"></div><div class="comment-text"><p>Hi Tony, thanks heaps for the video, any chance we can chat on Skype - my user is 'callnplay'</p><p>Thx</p><p>Pete</p></div><div id="comment-8424-info" class="comment-info"><span class="comment-age">(17 Jan '12, 01:05)</span> <span class="comment-user userinfo">morpheyous</span></div></div><span id="8427"></span><div id="comment-8427" class="comment not_top_scorer"><div id="post-8427-score" class="comment-score"></div><div class="comment-text"><p>I can chat tonight anytime after 6 pm EST. my skype id is thetechfirm</p></div><div id="comment-8427-info" class="comment-info"><span class="comment-age">(17 Jan '12, 03:13)</span> <span class="comment-user userinfo">thetechfirm</span></div></div><span id="8433"></span><div id="comment-8433" class="comment not_top_scorer"><div id="post-8433-score" class="comment-score"></div><div class="comment-text"><p>Sorry Pete, got my days all mixed up. Got an install scheduled for tonight. Maybe some other time.</p></div><div id="comment-8433-info" class="comment-info"><span class="comment-age">(17 Jan '12, 06:03)</span> <span class="comment-user userinfo">thetechfirm</span></div></div></div><div id="comment-tools-8392" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-8392-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8408"></span>

<div id="answer-container-8408" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8408-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8408-score" class="post-score" title="current number of votes">0</div><span id="post-8408-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can go to <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChUseStatisticsMenuSection.html">Statistics</a> | <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChStatConversations.html#ChStatConversationListWindow">Conversations</a>.<br />
Click on the tab Ethernet to get an overview of all the MAC addresses in the capture file.<br />
Another option is to go to <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChUseStatisticsMenuSection.html">Statistics</a> | <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChStatEndpoints.html#ChStatEndpointListWindow">Endpoints</a> to open the "Enpoints"window.</p><p>BTW<br />
You can learn more about display filters in the <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChWorkDefineFilterSection.html">Wireshark User's Guide</a> or in the <a href="http://wiki.wireshark.org/DisplayFilters">Wireshark Wiki</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jan '12, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p><span>joke</span><br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div></div><div id="comments-container-8408" class="comments-container"></div><div id="comment-tools-8408" class="comment-tools"></div><div class="clear"></div><div id="comment-8408-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

