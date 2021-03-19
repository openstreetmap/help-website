+++
type = "question"
title = "Create display filter programmatically from protocol dissector"
description = '''Hello, In our environment, we are processing pcapng files with a proprietary protocol that are captured/created by another device and we want to analyze these files using Wireshark. The capture files may have packets captured from multiple interfaces and we would like the ability to filter the packe...'''
date = "2016-09-15T09:09:00Z"
lastmod = "2016-09-15T18:56:00Z"
weight = 55566
keywords = [ "dissector", "display-filter" ]
aliases = [ "/questions/55566" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Create display filter programmatically from protocol dissector](/questions/55566/create-display-filter-programmatically-from-protocol-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55566-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55566-score" class="post-score" title="current number of votes">0</div><span id="post-55566-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, In our environment, we are processing pcapng files with a proprietary protocol that are captured/created by another device and we want to analyze these files using Wireshark. The capture files may have packets captured from multiple interfaces and we would like the ability to filter the packet display by interface. I have written a protocol dissector (similar to the plugins/gryphon dissector) and would like to automatically generate the filters during packet dissection, if possible. I could add the filters manually, but the number of interfaces vary depending on the device that generated the pcap file and it requires checking the capture file properties to know what interfaces are present. Is there any way to create and add display filters from within a protocol descriptor? Another alternative would be to do this when the file is opened, but it's not clear to me where the best place to do this is.</p><p>As a secondary question, it would also be nice to display the filtered packets for each interface in another tab or window. From what I've read, the only way to do this is to open a second instance of Wireshark. Does anyone know of an alternate way to accomplish this?</p><p>Thank you.</p><p>-Ron</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Sep '16, 09:09</strong></p><img src="https://secure.gravatar.com/avatar/7c43878a44520e91d5d620644548f598?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RonW&#39;s gravatar image" /><p><span>RonW</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RonW has no accepted answers">0%</span></p></div></div><div id="comments-container-55566" class="comments-container"><span id="55576"></span><div id="comment-55576" class="comment"><div id="post-55576-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by "the filters"? To which filters are you referring?</p></div><div id="comment-55576-info" class="comment-info"><span class="comment-age">(15 Sep '16, 18:30)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="55577"></span><div id="comment-55577" class="comment"><div id="post-55577-score" class="comment-score"></div><div class="comment-text"><p>I'm only referring to display filters. Our capture files are created external to Wireshark so capture filters are not really of much use in this scenario. And a further clarification...when I referred to manually adding the filters, I was talking about adding them through the GUI menu "Analyze-&gt;Display Filters", which is what I'm trying to avoid requiring the user to do. Thanks again.</p></div><div id="comment-55577-info" class="comment-info"><span class="comment-age">(15 Sep '16, 18:51)</span> <span class="comment-user userinfo">RonW</span></div></div></div><div id="comment-tools-55566" class="comment-tools"></div><div class="clear"></div><div id="comment-55566-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55578"></span>

<div id="answer-container-55578" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55578-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55578-score" class="post-score" title="current number of votes">0</div><span id="post-55578-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately, there are no APIs in Wireshark to allow any code to add to that list of filters; the list that comes with Wireshark is just a text file that's part of the Wireshark source repository, it's not generated by code.</p><p>You could request such an API by filing an enhancement request on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>.</p><p>As for the secondary question, that should be asked separately; this is a Q&amp;A site, not a forum, so there should only be one question per question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '16, 18:56</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-55578" class="comments-container"></div><div id="comment-tools-55578" class="comment-tools"></div><div class="clear"></div><div id="comment-55578-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

