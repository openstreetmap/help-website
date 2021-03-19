+++
type = "question"
title = "Remove duplicate packets editcap"
description = '''Hello We have traces which contain duplicate packets. We clear them with editcap. However some of them include the same frame instance with a VLAN tag and without. Since those 2 are considered different one of them is not removed. Is there a way to do this? thanks Manolis'''
date = "2015-10-19T13:16:00Z"
lastmod = "2015-10-23T17:04:00Z"
weight = 46710
keywords = [ "editcap" ]
aliases = [ "/questions/46710" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Remove duplicate packets editcap](/questions/46710/remove-duplicate-packets-editcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46710-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46710-score" class="post-score" title="current number of votes">0</div><span id="post-46710-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>We have traces which contain duplicate packets. We clear them with editcap. However some of them include the same frame instance with a VLAN tag and without. Since those 2 are considered different one of them is not removed. Is there a way to do this?</p><p>thanks Manolis</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-editcap" rel="tag" title="see questions tagged &#39;editcap&#39;">editcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '15, 13:16</strong></p><img src="https://secure.gravatar.com/avatar/fabda3280c9880e01f17cbb8c96a698d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="manolis&#39;s gravatar image" /><p><span>manolis</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="manolis has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Oct '15, 21:34</strong> </span></p></div></div><div id="comments-container-46710" class="comments-container"></div><div id="comment-tools-46710" class="comment-tools"></div><div class="clear"></div><div id="comment-46710-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46714"></span>

<div id="answer-container-46714" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46714-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46714-score" class="post-score" title="current number of votes">0</div><span id="post-46714-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If all VLAN tagged frame are duplicates only that just filter these away. But it's probably not that simple...</p><p>As of yet there's no way to do that within Wireshark or its tools. You may have luck with other tools, maybe trace wrangler.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '15, 13:34</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-46714" class="comments-container"><span id="46715"></span><div id="comment-46715" class="comment"><div id="post-46715-score" class="comment-score"></div><div class="comment-text"><p>TraceWrangler can't do this (yet), but SuperDeduper might, see <a href="http://goo.gl/Yy49W3">http://goo.gl/Yy49W3</a></p></div><div id="comment-46715-info" class="comment-info"><span class="comment-age">(19 Oct '15, 13:42)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="46717"></span><div id="comment-46717" class="comment"><div id="post-46717-score" class="comment-score"></div><div class="comment-text"><p>I thought it could when reading <a href="https://www.tracewrangler.com/documentation/VLANs.html">the documentation</a>?</p></div><div id="comment-46717-info" class="comment-info"><span class="comment-age">(19 Oct '15, 13:56)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="46718"></span><div id="comment-46718" class="comment"><div id="post-46718-score" class="comment-score"></div><div class="comment-text"><p>Hello</p><p>Unfortunatelly not. It looks like tcpdump in linux captures and stores frames,,,, 1. sometimes only after the VLAN tag has been stripped,,,, 2. sometimes only with the VLAN tag included,,,, 3. sometimes it captures and shows both frames.</p><p>So I'm looking to see if editcap has the ability to compare all other frame data <strong><em>except</em></strong> the VLAN tag and if they match then remove either one ...</p><p>Thanks for the suggestions I will try the other trace tools as well :-)</p><p>br Manolis</p></div><div id="comment-46718-info" class="comment-info"><span class="comment-age">(19 Oct '15, 13:58)</span> <span class="comment-user userinfo">manolis</span></div></div><span id="46719"></span><div id="comment-46719" class="comment"><div id="post-46719-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@Jaap</span>: regarding TraceWrangler: yeah it can remove VLAN tags, but not deduplicate based on them. "Removing" means, that the frame is modified by cutting away the VLAN tag bytes, not the whole frame.</p></div><div id="comment-46719-info" class="comment-info"><span class="comment-age">(19 Oct '15, 14:01)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="46726"></span><div id="comment-46726" class="comment"><div id="post-46726-score" class="comment-score"></div><div class="comment-text"><p>Not sure I can find this option in editcap (or wireshark in general). The editcap guide does not even include the word vlan. Any ideas?</p></div><div id="comment-46726-info" class="comment-info"><span class="comment-age">(19 Oct '15, 16:11)</span> <span class="comment-user userinfo">manolis</span></div></div><span id="46729"></span><div id="comment-46729" class="comment not_top_scorer"><div id="post-46729-score" class="comment-score"></div><div class="comment-text"><p><span>@manolis</span>: Please reply with comments instead of new answers. See the FAQ of this site.</p></div><div id="comment-46729-info" class="comment-info"><span class="comment-age">(19 Oct '15, 16:22)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="46742"></span><div id="comment-46742" class="comment not_top_scorer"><div id="post-46742-score" class="comment-score"></div><div class="comment-text"><p>ok now I got the point. Thanks,,, trying TraceWrangler</p></div><div id="comment-46742-info" class="comment-info"><span class="comment-age">(19 Oct '15, 21:31)</span> <span class="comment-user userinfo">manolis</span></div></div><span id="46745"></span><div id="comment-46745" class="comment not_top_scorer"><div id="post-46745-score" class="comment-score"></div><div class="comment-text"><p><span>@Jasper</span>: Think of it in the Unix way, use one tool for one specific job. So use trace wrangler to strip out the VLAN headers, then the new file will have the duplicates that editcap can go over and deduplicate.</p></div><div id="comment-46745-info" class="comment-info"><span class="comment-age">(19 Oct '15, 23:51)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="46901"></span><div id="comment-46901" class="comment not_top_scorer"><div id="post-46901-score" class="comment-score"></div><div class="comment-text"><p>Thanks so far for the answers.</p><p>News: I can only find a windows based version of TraceWrangler. Both 32 and 64 bit versions crash while working on the imported traces and also corrupt the frames during the process.</p><p>When I run SuperDeduper I get the msg that it's not a valid windows application. Cannot find any info in the web about this application. Should I run it in linux of somekind?</p><p>Any other ideas are welcome.</p><p>thanks Manolis</p></div><div id="comment-46901-info" class="comment-info"><span class="comment-age">(23 Oct '15, 17:04)</span> <span class="comment-user userinfo">manolis</span></div></div></div><div id="comment-tools-46714" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-46714-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

