+++
type = "question"
title = "Identify Bandwidth Hog"
description = '''Can I use Wireshark to idenitify a bandwidth hog, i.e. a user/pc that is perhaps watching videos or on peer to peer file sharing networks and thus using high bandwidth? Thank you'''
date = "2012-03-06T12:07:00Z"
lastmod = "2016-04-01T13:50:00Z"
weight = 9405
keywords = [ "high", "bandwidth", "bandwidthutilization" ]
aliases = [ "/questions/9405" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Identify Bandwidth Hog](/questions/9405/identify-bandwidth-hog)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9405-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9405-score" class="post-score" title="current number of votes">0</div><span id="post-9405-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can I use Wireshark to idenitify a bandwidth hog, i.e. a user/pc that is perhaps watching videos or on peer to peer file sharing networks and thus using high bandwidth?</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-high" rel="tag" title="see questions tagged &#39;high&#39;">high</span> <span class="post-tag tag-link-bandwidth" rel="tag" title="see questions tagged &#39;bandwidth&#39;">bandwidth</span> <span class="post-tag tag-link-bandwidthutilization" rel="tag" title="see questions tagged &#39;bandwidthutilization&#39;">bandwidthutilization</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '12, 12:07</strong></p><img src="https://secure.gravatar.com/avatar/f7df6d5abe5f578848df8d0734711db8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="IT%20Tropolis&#39;s gravatar image" /><p><span>IT Tropolis</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="IT Tropolis has no accepted answers">0%</span></p></div></div><div id="comments-container-9405" class="comments-container"></div><div id="comment-tools-9405" class="comment-tools"></div><div class="clear"></div><div id="comment-9405-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9407"></span>

<div id="answer-container-9407" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9407-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9407-score" class="post-score" title="current number of votes">2</div><span id="post-9407-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="IT Tropolis has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes you can...</p><p>... by using "Statistics -&gt; Endpoints". Click on the IP tab and then sort on the column you find most interesting.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '12, 12:12</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-9407" class="comments-container"><span id="51235"></span><div id="comment-51235" class="comment"><div id="post-51235-score" class="comment-score"></div><div class="comment-text"><p>hello SYN-bit, after go to Statistics-Endpoints, the only IP tab I have is IPv4:332. Is that the one I should click on. To find the bandwidth hog, which column should I look into Bytes,Tx Packets, TX Bytes, RX Packets,Rx Bytes?</p></div><div id="comment-51235-info" class="comment-info"><span class="comment-age">(28 Mar '16, 09:24)</span> <span class="comment-user userinfo">ipodtrip</span></div></div><span id="51242"></span><div id="comment-51242" class="comment"><div id="post-51242-score" class="comment-score"></div><div class="comment-text"><p>I would sort the rows first by Bytes A-&gt;B and then by Bytes B-&gt;A (by clicking on column name) and look for the maximum value of both (as assignment of A and B roles to endpoints of a given conversation depends on the order of occurrence of the addresses in the capture). But having no TCP and/or UDP tab is strange, haven't you disabled the dissectors?</p></div><div id="comment-51242-info" class="comment-info"><span class="comment-age">(28 Mar '16, 13:31)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="51351"></span><div id="comment-51351" class="comment"><div id="post-51351-score" class="comment-score"></div><div class="comment-text"><p>let me try to disable the dissectors. Really appericate your help.</p></div><div id="comment-51351-info" class="comment-info"><span class="comment-age">(01 Apr '16, 10:04)</span> <span class="comment-user userinfo">ipodtrip</span></div></div><span id="51363"></span><div id="comment-51363" class="comment"><div id="post-51363-score" class="comment-score"></div><div class="comment-text"><p>It may well be a chain of misunderstandings. I thought you <strong>complained</strong> that there are no other tabs than the IP one in the <code>Statistics -&gt; Endpoints</code> window, so I've suggested you to check whether the dissectors of TCP and UDP are not disabled by chance, assuming that disabling them would cause the TCP and UDP tabs to go missing. But maybe you actually wanted IPv6 on top/instead of IPv4?</p><p>I've checked now and found that disabling TCP and UDP dissectors doesn't hide their tabs, it only makes them empty. So do not disable the dissectors (or re-enable them if you already did).</p><p>Which version of Wireshark do you run? In 2.0.2, pressing the <code>Endpoint Types</code> button gives you a checklist of tabs to be shown, so you can verify that tickboxes next to layers/protocols you are interested in are checked.</p></div><div id="comment-51363-info" class="comment-info"><span class="comment-age">(01 Apr '16, 13:50)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-9407" class="comment-tools"></div><div class="clear"></div><div id="comment-9407-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

