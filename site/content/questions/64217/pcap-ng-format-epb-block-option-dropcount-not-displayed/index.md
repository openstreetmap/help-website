+++
type = "question"
title = "Pcap-ng format - EPB block option - dropcount not displayed"
description = '''Hi, Is EPB block option - epb_dropcount displayed on wireshark ?. If so where it&#x27;s shown on wireshark. Thanks, Subhash'''
date = "2017-10-26T01:40:00Z"
lastmod = "2017-10-26T04:34:00Z"
weight = 64217
keywords = [ "pcapng" ]
aliases = [ "/questions/64217" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Pcap-ng format - EPB block option - dropcount not displayed](/questions/64217/pcap-ng-format-epb-block-option-dropcount-not-displayed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64217-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64217-score" class="post-score" title="current number of votes">0</div><span id="post-64217-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Is EPB block option - epb_dropcount displayed on wireshark ?. If so where it's shown on wireshark.</p><p>Thanks, Subhash</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcapng" rel="tag" title="see questions tagged &#39;pcapng&#39;">pcapng</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '17, 01:40</strong></p><img src="https://secure.gravatar.com/avatar/38a15fccab6827bd3319fe93cf058e1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="subhashmohan&#39;s gravatar image" /><p><span>subhashmohan</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="subhashmohan has no accepted answers">0%</span></p></div></div><div id="comments-container-64217" class="comments-container"></div><div id="comment-tools-64217" class="comment-tools"></div><div class="clear"></div><div id="comment-64217-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64220"></span>

<div id="answer-container-64220" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64220-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64220-score" class="post-score" title="current number of votes">0</div><span id="post-64220-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="subhashmohan has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The dialog from Statistics -&gt; Capture File Properties has a "Dropped packets" column but it always seems to be "unknown" for me.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '17, 02:56</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-64220" class="comments-container"><span id="64223"></span><div id="comment-64223" class="comment"><div id="post-64223-score" class="comment-score"></div><div class="comment-text"><p>yes right. Even i see the same. I think it's per interface. This is mentioned in each packet, so this should be displayed on each packet i guess</p></div><div id="comment-64223-info" class="comment-info"><span class="comment-age">(26 Oct '17, 04:17)</span> <span class="comment-user userinfo">subhashmohan</span></div></div><span id="64224"></span><div id="comment-64224" class="comment"><div id="post-64224-score" class="comment-score"></div><div class="comment-text"><p>if it should be anywhere at all, it should be in the <code>frame</code> layer of the dissection tree (middle pane). Some EPB options are shown there if present in the file.</p></div><div id="comment-64224-info" class="comment-info"><span class="comment-age">(26 Oct '17, 04:34)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-64220" class="comment-tools"></div><div class="clear"></div><div id="comment-64220-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

